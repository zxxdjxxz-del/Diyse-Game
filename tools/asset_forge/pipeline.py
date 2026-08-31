#!/usr/bin/env python3
"""Diyse Asset Forge v0.4 processing pipeline.

Safe large-batch processing with:
- coordinate-locked atlas patches;
- deterministic animation propagation;
- hard image-generation call caps;
- asset-level checkpointing;
- resume without regenerating successful outputs.
"""
from __future__ import annotations

import argparse
import io
import json
import tempfile
from pathlib import Path
from typing import Optional

from PIL import Image

import forge
import atlas_engine
import animation_engine
import budget_engine


SUCCESS_STATUSES = {
    "generated",
    "generated_anchor",
    "generated_atlas",
    "propagated_from_anchor",
}


class BudgetExceeded(RuntimeError):
    pass


class CountingProvider(forge.Provider):
    def __init__(self, delegate: forge.Provider, max_calls: Optional[int]) -> None:
        self.delegate = delegate
        self.max_calls = max_calls
        self.calls = 0

    @property
    def remaining(self) -> Optional[int]:
        if self.max_calls is None:
            return None
        return max(0, self.max_calls - self.calls)

    def require(self, calls: int) -> None:
        if self.max_calls is not None and self.calls + calls > self.max_calls:
            raise BudgetExceeded(
                f"operation requires {calls} image call(s), but only {self.remaining} remain"
            )

    def edit(self, source: Path, prompt: str, has_alpha: bool) -> bytes:
        self.require(1)
        self.calls += 1
        return self.delegate.edit(source, prompt, has_alpha)


def _normalized_generated_image(
    source: Path,
    image_bytes: bytes,
    *,
    preserve_source_alpha: bool,
) -> Image.Image:
    with Image.open(source).convert("RGBA") as source_image:
        source_size = source_image.size
        source_alpha = source_image.getchannel("A").copy()
    with Image.open(io.BytesIO(image_bytes)).convert("RGBA") as generated:
        if generated.size != source_size:
            generated = generated.resize(source_size, Image.Resampling.LANCZOS)
        if preserve_source_alpha:
            generated.putalpha(source_alpha)
        return generated.copy()


def _save_direct(
    source: Path,
    dest: Path,
    provider: forge.Provider,
    prompt: str,
    *,
    preserve_source_alpha: bool,
) -> None:
    raw = provider.edit(source, prompt, bool(preserve_source_alpha))
    output = _normalized_generated_image(
        source, raw, preserve_source_alpha=preserve_source_alpha
    )
    dest.parent.mkdir(parents=True, exist_ok=True)
    output.save(dest, format="PNG")


def _atlas_processor(
    provider: forge.Provider,
    prompt: str,
    source_has_alpha: bool,
):
    def process(crop: Image.Image, patch: atlas_engine.AtlasPatch) -> Image.Image:
        with tempfile.TemporaryDirectory(prefix="diyse_forge_patch_") as temp_dir:
            patch_path = Path(temp_dir) / f"patch_{patch.index:04d}.png"
            crop.save(patch_path, format="PNG")
            patch_prompt = (
                prompt
                + "\n\nCoordinate-locked atlas crop. "
                + f"Patch {patch.index}; bounds=({patch.x0},{patch.y0})-({patch.x1},{patch.y1}). "
                + "Do not change framing or crop-edge structure. Preserve every functional form that "
                  "touches a crop boundary so overlapping patches can recombine without registration drift."
            )
            raw = provider.edit(patch_path, patch_prompt, source_has_alpha)
            return _normalized_generated_image(
                patch_path, raw, preserve_source_alpha=source_has_alpha
            )
    return process


def _anchor_rows(queue: list[dict]) -> dict[str, dict]:
    anchors: dict[str, dict] = {}
    for row in queue:
        group = row.get("animation_group")
        index = row.get("frame_index")
        if group is None or index is None:
            continue
        current = anchors.get(group)
        if current is None or index < current.get("frame_index", index):
            anchors[group] = row
    return anchors


def _valid_resume_row(previous: dict, current: dict) -> bool:
    if previous.get("status") not in SUCCESS_STATUSES:
        return False
    output = previous.get("output_path")
    if not output or not Path(output).exists():
        return False
    if previous.get("sha256") and current.get("sha256") and previous["sha256"] != current["sha256"]:
        return False
    return True


def _checkpoint(rows: list[dict], path: Optional[Path]) -> None:
    if path is not None:
        forge.write_jsonl(path, rows)


def process_v2(
    queue: list[dict],
    output_root: Path,
    provider_name: str,
    *,
    limit: Optional[int] = None,
    atlas_tile: int = 768,
    atlas_overlap: int = 96,
    provider: Optional[forge.Provider] = None,
    max_ai_calls: Optional[int] = None,
    resume_results: Optional[list[dict]] = None,
    checkpoint_path: Optional[Path] = None,
) -> list[dict]:
    if provider_name not in {"dry-run", "openai"}:
        raise ValueError("provider_name must be dry-run or openai")
    if max_ai_calls is not None and max_ai_calls < 0:
        raise ValueError("max_ai_calls must be >= 0")

    counting_provider: Optional[CountingProvider] = None
    if provider_name == "openai":
        delegate = provider if provider is not None else forge.OpenAIProvider()
        counting_provider = CountingProvider(delegate, max_ai_calls)

    anchors = _anchor_rows(queue)
    previous_by_rel = {
        row["relative_path"]: row
        for row in (resume_results or [])
        if row.get("relative_path")
    }

    results: list[dict] = []
    result_by_relative_path: dict[str, dict] = {}
    processed_assets = 0

    # Pass 1: direct assets, animation anchors, and atlases.
    for raw_row in queue:
        row = dict(raw_row)
        rel = row["relative_path"]

        previous = previous_by_rel.get(rel)
        if previous and _valid_resume_row(previous, row):
            resumed = dict(previous)
            resumed["resumed"] = True
            results.append(resumed)
            result_by_relative_path[rel] = resumed
            _checkpoint(results, checkpoint_path)
            continue

        if row.get("action") == "propagate_from_anchor":
            results.append(row)
            result_by_relative_path[rel] = row
            continue

        if limit is not None and processed_assets >= limit:
            row["status"] = "deferred_limit"
            results.append(row)
            result_by_relative_path[rel] = row
            continue

        source = Path(row["source_path"])
        dest = forge.output_path(output_root, row)
        action = row.get("action")
        try:
            if provider_name == "dry-run":
                row["status"] = "planned_v2"
            elif action == "ai_style_edit":
                assert counting_provider is not None
                counting_provider.require(1)
                preserve_alpha = bool(row.get("animation_group")) and bool(row.get("has_alpha"))
                _save_direct(
                    source,
                    dest,
                    counting_provider,
                    row["prompt"],
                    preserve_source_alpha=preserve_alpha,
                )
                row["status"] = "generated_anchor" if row.get("animation_group") else "generated"
            elif action == "structure_preserving_pass":
                assert counting_provider is not None
                required_calls = budget_engine.patch_count(
                    int(row["width"]),
                    int(row["height"]),
                    atlas_tile,
                    atlas_overlap,
                )
                counting_provider.require(required_calls)
                source_has_alpha = bool(row.get("has_alpha"))
                patches = atlas_engine.process_atlas(
                    source,
                    dest,
                    _atlas_processor(counting_provider, row["prompt"], source_has_alpha),
                    tile=atlas_tile,
                    overlap=atlas_overlap,
                    preserve_alpha=source_has_alpha,
                )
                row["atlas_patch_count"] = len(patches)
                row["status"] = "generated_atlas"
            else:
                raise ValueError(f"Unsupported v0.4 pass-1 action: {action}")

            if dest.exists():
                row["output_path"] = str(dest.resolve())
                row["output_sha256"] = forge.sha256_file(dest)
        except BudgetExceeded as exc:
            row["status"] = "budget_blocked"
            row["error"] = str(exc)
        except Exception as exc:
            row["status"] = "error"
            row["error"] = f"{type(exc).__name__}: {exc}"

        if counting_provider is not None:
            row["ai_calls_used_total"] = counting_provider.calls
            row["ai_calls_remaining"] = counting_provider.remaining

        processed_assets += 1
        results.append(row)
        result_by_relative_path[rel] = row
        _checkpoint(results, checkpoint_path)

    # Pass 2: deterministic propagation. Zero image calls.
    for result_index, raw_row in enumerate(list(results)):
        if raw_row.get("action") != "propagate_from_anchor":
            continue

        row = dict(raw_row)
        rel = row["relative_path"]
        previous = previous_by_rel.get(rel)
        if previous and _valid_resume_row(previous, row):
            resumed = dict(previous)
            resumed["resumed"] = True
            results[result_index] = resumed
            result_by_relative_path[rel] = resumed
            _checkpoint(results, checkpoint_path)
            continue

        if provider_name == "dry-run":
            row["status"] = "planned_animation_propagation"
            results[result_index] = row
            _checkpoint(results, checkpoint_path)
            continue

        if limit is not None and processed_assets >= limit:
            row["status"] = "deferred_limit"
            results[result_index] = row
            continue

        group = row.get("animation_group")
        anchor = anchors.get(group)
        if not anchor:
            row["status"] = "error"
            row["error"] = "animation_anchor_not_found"
            results[result_index] = row
            _checkpoint(results, checkpoint_path)
            continue

        anchor_result = result_by_relative_path.get(anchor["relative_path"], anchor)
        anchor_output = anchor_result.get("output_path")
        if not anchor_output or not Path(anchor_output).exists():
            row["status"] = "blocked"
            row["error"] = "styled_animation_anchor_not_available"
            results[result_index] = row
            _checkpoint(results, checkpoint_path)
            continue

        try:
            profile = animation_engine.learn_profile(
                Path(anchor["source_path"]), Path(anchor_output)
            )
            dest = forge.output_path(output_root, row)
            animation_engine.apply_profile(Path(row["source_path"]), dest, profile)
            row["output_path"] = str(dest.resolve())
            row["output_sha256"] = forge.sha256_file(dest)
            row["status"] = "propagated_from_anchor"
            row["animation_anchor_relative_path"] = anchor["relative_path"]
            row["animation_profile_edge_gain"] = round(profile.edge_gain, 6)
        except Exception as exc:
            row["status"] = "error"
            row["error"] = f"{type(exc).__name__}: {exc}"

        if counting_provider is not None:
            row["ai_calls_used_total"] = counting_provider.calls
            row["ai_calls_remaining"] = counting_provider.remaining

        processed_assets += 1
        results[result_index] = row
        result_by_relative_path[rel] = row
        _checkpoint(results, checkpoint_path)

    return results


def cmd_process_v2(args: argparse.Namespace) -> None:
    queue = forge.read_jsonl(Path(args.queue))
    results_path = Path(args.results)
    resume_rows = None
    if args.resume and results_path.exists():
        resume_rows = forge.read_jsonl(results_path)

    results = process_v2(
        queue,
        Path(args.output_root),
        args.provider,
        limit=args.limit,
        atlas_tile=args.atlas_tile,
        atlas_overlap=args.atlas_overlap,
        max_ai_calls=args.max_ai_calls,
        resume_results=resume_rows,
        checkpoint_path=results_path if args.checkpoint else None,
    )
    forge.write_jsonl(results_path, results)

    payload = forge.summary(results)
    payload["max_ai_calls"] = args.max_ai_calls
    payload["resume"] = bool(args.resume)
    print(json.dumps(payload, indent=2))


def cmd_atlas_plan(args: argparse.Namespace) -> None:
    payload = atlas_engine.write_patch_manifest(
        Path(args.source), Path(args.output), tile=args.tile, overlap=args.overlap
    )
    print(json.dumps({"patches": len(payload["patches"]), "output": args.output}, indent=2))


def cmd_animation_propagate(args: argparse.Namespace) -> None:
    frames = [Path(path) for path in args.frames]
    profile = animation_engine.propagate_sequence(
        frames,
        Path(args.styled_anchor),
        Path(args.output_dir),
        anchor_index=args.anchor_index,
    )
    print(json.dumps(profile.to_dict(), indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="diyse-asset-forge-v04")
    sub = parser.add_subparsers(dest="command", required=True)

    command = sub.add_parser("process", help="Run safe resumable atlas/animation processing")
    command.add_argument("queue")
    command.add_argument("--provider", choices=["dry-run", "openai"], default="dry-run")
    command.add_argument("--output-root", default=".asset_forge/output")
    command.add_argument("--results", default=".asset_forge/results_v04.jsonl")
    command.add_argument("--limit", type=int, help="Maximum assets handled in this run")
    command.add_argument("--max-ai-calls", type=int, help="Hard image-generation call cap")
    command.add_argument("--resume", action="store_true", help="Reuse successful rows in --results")
    command.add_argument("--checkpoint", action=argparse.BooleanOptionalAction, default=True)
    command.add_argument("--atlas-tile", type=int, default=768)
    command.add_argument("--atlas-overlap", type=int, default=96)
    command.set_defaults(func=cmd_process_v2)

    command = sub.add_parser("atlas-plan", help="Write exact coordinate patch plan for an atlas")
    command.add_argument("source")
    command.add_argument("--output", default=".asset_forge/atlas_plan.json")
    command.add_argument("--tile", type=int, default=768)
    command.add_argument("--overlap", type=int, default=96)
    command.set_defaults(func=cmd_atlas_plan)

    command = sub.add_parser("animation-propagate", help="Propagate an approved anchor style across frames")
    command.add_argument("styled_anchor")
    command.add_argument("frames", nargs="+")
    command.add_argument("--anchor-index", type=int, default=0)
    command.add_argument("--output-dir", default=".asset_forge/animation_output")
    command.set_defaults(func=cmd_animation_propagate)
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
