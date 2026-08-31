#!/usr/bin/env python3
"""
Diyse Asset Forge v0.1

Batch inventory, classify, plan, generate, and QA visual asset conversions for Diyse.

Design goals:
- Never overwrite source assets.
- Preserve provenance and SHA-256 identity.
- Classify assets into production recipes.
- Group animation frames and lighting-state families.
- Keep AI generation provider-pluggable.
- Default to dry-run planning; explicit provider required for generation.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Optional

SUPPORTED_EXTS = {".png", ".tga", ".jpg", ".jpeg", ".webp"}
FRAME_RE = re.compile(r"^(?P<stem>.*?)(?:[_-](?P<frame>\d+))$")
LIGHTING_RE = re.compile(r"(?P<base>.*?)(?:_(?P<state>ra|rb|rc|rd|re|rf))(?P<suffix>(?:_[^.]*)?)$", re.I)

STYLE_BLOCK = (
    "Diyse visual style: mature seinen-inspired HD-2D fantasy, painterly shape-first rendering, "
    "chaotic variable line weight with thick-to-thin broken tapered strokes used selectively, "
    "strong silhouettes, controlled detail, cinematic atmospheric lighting compatibility, "
    "handcrafted and readable at gameplay scale. Avoid chibi, glossy mobile-game rendering, "
    "photorealism, uniform comic outlines, generic clean-anime polish, and noisy microtexture."
)

CATEGORY_RULES = [
    ("water", ("water", "watersurface", "splash", "river", "ocean", "foam")),
    ("fire", ("fire", "flame", "torch", "candle", "ember", "lava")),
    ("foliage", ("tree", "bush", "leaf", "foliage", "canopy")),
    ("grass", ("grass", "weed", "reed", "plant", "flower")),
    ("stone", ("stone", "rock", "wall", "ruin", "brick", "masonry", "cliff")),
    ("wood", ("wood", "board", "plank", "timber", "barrel", "chair", "workbench")),
    ("cave", ("cave", "cavern", "stalag", "stalac", "crystal")),
    ("ritual", ("ritual", "sigil", "magic", "rune", "glyph", "altar")),
    ("interior", ("curtain", "bed", "table", "shelf", "cabinet", "carpet")),
    ("prop", ("lantern", "prop", "crate", "chest", "tool", "weaponrack")),
]

PROMPT_BY_CATEGORY = {
    "stone": (
        "Reinterpret this stone/environment asset into Diyse's stone grammar. Preserve functional "
        "tile/edge relationships and broad structure. Use painterly stone planes, irregular chips and "
        "fractures, selective deep ink at occlusion/damage, broken thin interior marks, restrained moss, "
        "and low micro-noise. Never outline every block."
    ),
    "foliage": (
        "Reinterpret this foliage asset into Diyse's foliage grammar. Preserve silhouette function and "
        "alpha behavior. Build 3-6 major canopy masses, intentional negative spaces, painterly foliage "
        "values, selective heavy ink at deep overlaps/branch forks, thin broken marks in light, and no "
        "leaf-by-leaf rendering or uniform black contour."
    ),
    "grass": (
        "Reinterpret as grouped painterly grass/vegetation tufts. Keep animation-safe broad shapes, "
        "stable silhouette density, sparse tapered line accents, and avoid frame-specific random detail."
    ),
    "water": (
        "Reinterpret as stylized Diyse water with broad luminous bands, graphic ripples, painterly color "
        "movement, sparse dark accents at selected overlaps, clean transparency, and no photoreal surface noise."
    ),
    "fire": (
        "Reinterpret as graphic Diyse fire/emissive art. Use strong flame silhouettes, bright mostly "
        "line-free cores, tapered ink-like marks at darker flame edges, restrained bloom compatibility, "
        "and clean transparent edges."
    ),
    "wood": (
        "Reinterpret this wood/prop surface into Diyse's painterly material language. Use broad grain, "
        "clear material planes, darker irregular accents at joints/cracks/overlaps, restrained wear, "
        "and no universal toon outline."
    ),
    "cave": (
        "Reinterpret as Diyse subterranean material: large rock planes first, sparse irregular fractures, "
        "deep ink only in crevices/occlusion, painterly mineral or moss breakup, and clear traversal surfaces."
    ),
    "ritual": (
        "Reinterpret as an original Diyse ritual/magical surface. Preserve functional composition only; "
        "use authored asymmetrical sigil hierarchy, variable line weight in inactive marks, selective "
        "emissive glow when active, and avoid generic stock magic-circle geometry."
    ),
    "interior": (
        "Reinterpret this interior asset with painterly material separation, controlled ornament density, "
        "selective variable line accents at seams/folds/carved overlaps, and mature non-glossy fantasy rendering."
    ),
    "prop": (
        "Restyle this prop to feel native to Diyse. Preserve useful geometry/silhouette while replacing "
        "generic material appearance with painterly wood/metal/cloth treatment and selective line influence. "
        "Do not add a universal black toon outline."
    ),
    "generic": (
        "Reinterpret this asset into Diyse's visual language while preserving its functional silhouette, "
        "alpha, seams, and gameplay readability. Simplify noise and use painterly shapes with selective "
        "chaotic variable line accents."
    ),
}


@dataclass
class AssetRecord:
    source_path: str
    relative_path: str
    sha256: str
    bytes: int
    width: int
    height: int
    mode: str
    has_alpha: bool
    category: str
    animation_group: Optional[str]
    frame_index: Optional[int]
    lighting_group: Optional[str]
    lighting_state: Optional[str]
    treatment: str


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def classify(name: str) -> str:
    n = name.lower()
    for category, tokens in CATEGORY_RULES:
        if any(tok in n for tok in tokens):
            return category
    if "map_color" in n or "map_" in n:
        return "atlas"
    return "generic"


def parse_animation(path: Path) -> tuple[Optional[str], Optional[int]]:
    m = FRAME_RE.match(path.stem)
    if not m:
        return None, None
    stem = m.group("stem")
    if any(token in stem.lower() for token in ("color", "frame", "anim", "water", "grass", "fire", "light")):
        return str(path.with_name(stem)), int(m.group("frame"))
    return None, None


def parse_lighting(path: Path) -> tuple[Optional[str], Optional[str]]:
    m = LIGHTING_RE.match(path.stem)
    if not m:
        return None, None
    return str(path.with_name(m.group("base") + m.group("suffix"))), m.group("state").lower()


def choose_treatment(category: str, animation_group: Optional[str], width: int, height: int) -> str:
    if animation_group:
        return "animation_anchor"
    if category == "atlas" or max(width, height) > 1536:
        return "atlas_structure_preserving"
    if category in {"water", "fire", "grass"}:
        return "effect_structure_preserving"
    return "direct_style_edit"


def inspect_image(path: Path) -> tuple[int, int, str, bool]:
    try:
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError("Pillow is required. Install tools/asset_forge/requirements.txt") from exc
    with Image.open(path) as im:
        mode = im.mode
        has_alpha = "A" in mode or ("transparency" in im.info)
        return im.width, im.height, mode, has_alpha


def iter_assets(root: Path) -> Iterable[Path]:
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS:
            yield p


def inventory(root: Path) -> list[AssetRecord]:
    records: list[AssetRecord] = []
    for path in iter_assets(root):
        width, height, mode, has_alpha = inspect_image(path)
        category = classify(path.name)
        animation_group, frame_index = parse_animation(path)
        lighting_group, lighting_state = parse_lighting(path)
        treatment = choose_treatment(category, animation_group, width, height)
        records.append(AssetRecord(
            source_path=str(path.resolve()), relative_path=str(path.relative_to(root)),
            sha256=sha256_file(path), bytes=path.stat().st_size, width=width, height=height,
            mode=mode, has_alpha=has_alpha, category=category, animation_group=animation_group,
            frame_index=frame_index, lighting_group=lighting_group, lighting_state=lighting_state,
            treatment=treatment,
        ))
    return records


def write_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def make_prompt(row: dict) -> str:
    category = row.get("category", "generic")
    recipe = PROMPT_BY_CATEGORY.get(category, PROMPT_BY_CATEGORY["generic"])
    treatment = row.get("treatment", "direct_style_edit")
    functional = (
        "Preserve the source asset's functional geometry, silhouette, transparency intent, tile boundaries, "
        "and registration where relevant. Do not add labels, typography, presentation-board framing, or unrelated objects."
    )
    if treatment == "animation_anchor":
        functional += (
            " This asset belongs to an animation sequence. Treat it as a style anchor: do not invent random "
            "frame-specific details; preserve silhouette landmarks so subsequent frames can inherit the same art language."
        )
    elif treatment == "atlas_structure_preserving":
        functional += (
            " This is a large atlas/composite. Do not rearrange atlas regions. Preserve piece placement and edge logic; "
            "style changes must not destroy modular registration."
        )
    return f"{STYLE_BLOCK}\n\n{recipe}\n\n{functional}"


def plan(records: list[dict]) -> list[dict]:
    min_frame: dict[str, int] = {}
    for r in records:
        g, idx = r.get("animation_group"), r.get("frame_index")
        if g is not None and idx is not None:
            min_frame[g] = min(idx, min_frame.get(g, idx))
    queue = []
    for r in records:
        item = dict(r)
        item["prompt"] = make_prompt(r)
        if r.get("animation_group") and r.get("frame_index") != min_frame[r["animation_group"]]:
            item["action"] = "propagate_from_anchor"
        elif r.get("treatment") == "atlas_structure_preserving":
            item["action"] = "structure_preserving_pass"
        else:
            item["action"] = "ai_style_edit"
        item["status"] = "queued"
        queue.append(item)
    return queue


def png_data_url(path: Path) -> str:
    from PIL import Image
    import io
    with Image.open(path) as im:
        buf = io.BytesIO()
        im.save(buf, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("ascii")


class Provider:
    def edit(self, source: Path, prompt: str, has_alpha: bool) -> bytes:
        raise NotImplementedError


class OpenAIProvider(Provider):
    def __init__(self) -> None:
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise RuntimeError("openai package required for --provider openai") from exc
        self.client = OpenAI()
        self.reasoning_model = os.getenv("DIYSE_FORGE_REASONING_MODEL", "gpt-5.6-terra")
        self.image_model = os.getenv("DIYSE_FORGE_IMAGE_MODEL", "gpt-image-2")

    def edit(self, source: Path, prompt: str, has_alpha: bool) -> bytes:
        background = "transparent" if has_alpha else "auto"
        response = self.client.responses.create(
            model=self.reasoning_model,
            input=[{"role": "user", "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url": png_data_url(source), "detail": "high"},
            ]}],
            tools=[{
                "type": "image_generation", "action": "edit", "model": self.image_model,
                "quality": "high", "size": "auto", "background": background, "output_format": "png",
            }],
        )
        for item in response.output:
            if getattr(item, "type", None) == "image_generation_call":
                result = getattr(item, "result", None)
                if result:
                    return base64.b64decode(result)
        raise RuntimeError("OpenAI response did not contain an image_generation_call result")


def output_path(output_root: Path, row: dict) -> Path:
    rel = Path(row["relative_path"])
    return output_root / rel.parent / (rel.stem + "__STYLE_PASS.png")


def copy_structure_preserving(source: Path, dest: Path) -> None:
    from PIL import Image
    dest.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as im:
        im.save(dest, format="PNG")


def process_queue(queue: list[dict], output_root: Path, provider_name: str, limit: Optional[int]) -> list[dict]:
    provider: Optional[Provider] = OpenAIProvider() if provider_name == "openai" else None
    processed = 0
    results = []
    for row in queue:
        if limit is not None and processed >= limit:
            results.append(row)
            continue
        source = Path(row["source_path"])
        dest = output_path(output_root, row)
        dest.parent.mkdir(parents=True, exist_ok=True)
        action = row["action"]
        try:
            if provider_name == "dry-run":
                row["status"] = "planned"
            elif action == "ai_style_edit":
                assert provider is not None
                dest.write_bytes(provider.edit(source, row["prompt"], bool(row.get("has_alpha"))))
                row["status"] = "generated"
            elif action == "structure_preserving_pass":
                copy_structure_preserving(source, dest)
                row["status"] = "structure_preserved_pending_backend"
            elif action == "propagate_from_anchor":
                copy_structure_preserving(source, dest)
                row["status"] = "animation_frame_preserved_pending_propagation"
            else:
                raise ValueError(f"Unknown action: {action}")
            if dest.exists():
                row["output_path"] = str(dest.resolve())
                row["output_sha256"] = sha256_file(dest)
        except Exception as exc:
            row["status"] = "error"
            row["error"] = f"{type(exc).__name__}: {exc}"
        processed += 1
        results.append(row)
    return results


def alpha_edge_score(path: Path) -> dict:
    from PIL import Image
    with Image.open(path).convert("RGBA") as im:
        hist = im.getchannel("A").histogram()
        transparent, opaque, partial = hist[0], hist[255], sum(hist[1:255])
        total = im.width * im.height
        return {
            "transparent_pixels": transparent, "opaque_pixels": opaque,
            "partial_alpha_pixels": partial,
            "partial_alpha_ratio": round(partial / total, 8) if total else 0.0,
        }


def qa(results: list[dict]) -> list[dict]:
    out = []
    for row in results:
        item = dict(row)
        op = row.get("output_path")
        if not op or not Path(op).exists():
            item["qa"] = {"status": "not_generated"}
            out.append(item)
            continue
        p = Path(op)
        width, height, mode, has_alpha = inspect_image(p)
        q = {
            "status": "review", "width": width, "height": height, "mode": mode, "has_alpha": has_alpha,
            "source_aspect": round(row["width"] / row["height"], 6),
            "output_aspect": round(width / height, 6),
        }
        if row.get("has_alpha"):
            q["alpha"] = alpha_edge_score(p)
        drift = abs(q["source_aspect"] - q["output_aspect"])
        q["aspect_drift"] = round(drift, 6)
        q["aspect_ok"] = drift < 0.02
        if not q["aspect_ok"]:
            q["status"], q["reason"] = "reject", "aspect_ratio_drift"
        item["qa"] = q
        out.append(item)
    return out


def summary(rows: list[dict]) -> dict:
    by_category, by_treatment, by_status = {}, {}, {}
    for r in rows:
        c, t, s = r.get("category", "unknown"), r.get("treatment", "unknown"), r.get("status", "unknown")
        by_category[c] = by_category.get(c, 0) + 1
        by_treatment[t] = by_treatment.get(t, 0) + 1
        by_status[s] = by_status.get(s, 0) + 1
    return {"count": len(rows), "by_category": dict(sorted(by_category.items())),
            "by_treatment": dict(sorted(by_treatment.items())), "by_status": dict(sorted(by_status.items()))}


def cmd_inventory(args: argparse.Namespace) -> None:
    records = inventory(Path(args.source_root))
    write_jsonl(Path(args.output), (asdict(r) for r in records))
    print(json.dumps(summary([asdict(r) for r in records]), indent=2))


def cmd_plan(args: argparse.Namespace) -> None:
    queue = plan(read_jsonl(Path(args.manifest)))
    write_jsonl(Path(args.output), queue)
    print(json.dumps(summary(queue), indent=2))


def cmd_process(args: argparse.Namespace) -> None:
    results = process_queue(read_jsonl(Path(args.queue)), Path(args.output_root), args.provider, args.limit)
    write_jsonl(Path(args.results), results)
    print(json.dumps(summary(results), indent=2))


def cmd_qa(args: argparse.Namespace) -> None:
    reviewed = qa(read_jsonl(Path(args.results)))
    write_jsonl(Path(args.output), reviewed)
    rejects = sum(1 for r in reviewed if r.get("qa", {}).get("status") == "reject")
    print(json.dumps({"count": len(reviewed), "qa_rejects": rejects}, indent=2))


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="diyse-asset-forge")
    sub = p.add_subparsers(dest="command", required=True)
    s = sub.add_parser("inventory", help="Scan images and build provenance-aware manifest")
    s.add_argument("source_root")
    s.add_argument("--output", default=".asset_forge/manifest.jsonl")
    s.set_defaults(func=cmd_inventory)
    s = sub.add_parser("plan", help="Build style-conversion work queue")
    s.add_argument("manifest")
    s.add_argument("--output", default=".asset_forge/queue.jsonl")
    s.set_defaults(func=cmd_plan)
    s = sub.add_parser("process", help="Run queued work")
    s.add_argument("queue")
    s.add_argument("--provider", choices=["dry-run", "openai"], default="dry-run")
    s.add_argument("--output-root", default=".asset_forge/output")
    s.add_argument("--results", default=".asset_forge/results.jsonl")
    s.add_argument("--limit", type=int)
    s.set_defaults(func=cmd_process)
    s = sub.add_parser("qa", help="Run deterministic output QA")
    s.add_argument("results")
    s.add_argument("--output", default=".asset_forge/qa.jsonl")
    s.set_defaults(func=cmd_qa)
    return p


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
