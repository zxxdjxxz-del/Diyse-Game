#!/usr/bin/env python3
"""Resolve and stage the bounded Diyse texture-style validation batch.

The authoritative raw Map001-Map116 archives are intentionally not repository
content. This tool runs where those source files are mounted. It resolves every
manifest basename exactly once, hashes it, validates sequence counts, and stages a
read-only copy/hardlink workspace without modifying the source library.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Iterable, Optional

DEFAULT_MANIFEST = Path(__file__).with_name("validation_texture_batch_v1.json")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest(path: Path = DEFAULT_MANIFEST) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    jobs = data.get("jobs") or []
    if len(jobs) != 12:
        raise ValueError(f"Validation batch must contain exactly 12 jobs, found {len(jobs)}")
    if data.get("stop_after_jobs") != 12:
        raise ValueError("Validation batch must remain bounded at stop_after_jobs=12")
    seen: set[str] = set()
    for job in jobs:
        job_id = job.get("id")
        if not job_id or job_id in seen:
            raise ValueError(f"Missing or duplicate validation job id: {job_id!r}")
        seen.add(job_id)
        primary = list(job.get("primary") or [])
        if not primary:
            raise ValueError(f"{job_id}: at least one primary source is required")
        expected = job.get("expected_primary_frames")
        if expected is not None and len(primary) != int(expected):
            raise ValueError(
                f"{job_id}: expected_primary_frames={expected}, manifest contains {len(primary)}"
            )
    return data


def iter_files(root: Path) -> Iterable[Path]:
    for dirpath, _, filenames in os.walk(root):
        base = Path(dirpath)
        for filename in filenames:
            yield base / filename


def build_basename_index(source_root: Path) -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = defaultdict(list)
    for path in iter_files(source_root):
        index[path.name.casefold()].append(path)
    return dict(index)


def resolve_manifest(manifest: dict, source_root: Path) -> dict:
    index = build_basename_index(source_root)
    issues: list[str] = []
    jobs: list[dict] = []

    for job in manifest["jobs"]:
        resolved_files: list[dict] = []
        specs = [
            *(dict(role="primary", filename=name) for name in job.get("primary", [])),
            *(dict(role="companion", filename=name) for name in job.get("companions", [])),
        ]
        for spec in specs:
            filename = spec["filename"]
            matches = index.get(filename.casefold(), [])
            if not matches:
                issues.append(f'{job["id"]}: missing {filename}')
                resolved_files.append({**spec, "status": "missing", "matches": []})
                continue
            if len(matches) > 1:
                issues.append(
                    f'{job["id"]}: ambiguous basename {filename} ({len(matches)} matches)'
                )
                resolved_files.append({
                    **spec,
                    "status": "ambiguous",
                    "matches": [str(path) for path in matches],
                })
                continue
            source = matches[0]
            try:
                digest = sha256_file(source)
                size = source.stat().st_size
            except Exception as exc:
                issues.append(f'{job["id"]}: hash/read failure {filename}: {exc}')
                resolved_files.append({
                    **spec,
                    "status": "hash_failed",
                    "source_path": str(source),
                })
                continue
            resolved_files.append({
                **spec,
                "status": "resolved",
                "source_path": str(source.resolve()),
                "size_bytes": size,
                "sha256": digest,
            })

        jobs.append({
            "id": job["id"],
            "family": job["family"],
            "material_kind": job.get("material_kind", job["family"]),
            "map": job.get("map"),
            "source_kind": job.get("source_kind"),
            "evaluation_target": job.get("evaluation_target"),
            "processing_rule": job.get("processing_rule"),
            "files": resolved_files,
        })

    return {
        "schema": "diyse.asset_forge.validation_source_resolution.v1",
        "batch_id": manifest["id"],
        "valid": not issues,
        "issues": issues,
        "job_count": len(jobs),
        "source_root": str(source_root.resolve()),
        "jobs": jobs,
        "ready_for_staging": not issues,
    }


def stage_resolution(resolution: dict, output_root: Path, mode: str = "copy") -> dict:
    if not resolution.get("valid"):
        raise RuntimeError("Refusing to stage an invalid source resolution")
    if mode not in {"copy", "hardlink"}:
        raise ValueError("mode must be copy or hardlink")

    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True)

    staged_jobs: list[dict] = []
    for job in resolution["jobs"]:
        job_dir = output_root / job["id"]
        primary_dir = job_dir / "primary"
        companion_dir = job_dir / "companions"
        primary_dir.mkdir(parents=True)
        companion_dir.mkdir(parents=True)
        staged_files: list[dict] = []

        for item in job["files"]:
            source = Path(item["source_path"])
            dest_dir = primary_dir if item["role"] == "primary" else companion_dir
            dest = dest_dir / item["filename"]
            if dest.exists():
                raise RuntimeError(f"Staging collision: {dest}")
            if mode == "hardlink":
                os.link(source, dest)
            else:
                shutil.copy2(source, dest)
            staged_files.append({
                "role": item["role"],
                "filename": item["filename"],
                "staged_path": str(dest.resolve()),
                "sha256": item["sha256"],
                "size_bytes": item["size_bytes"],
            })

        job_manifest = {
            "id": job["id"],
            "family": job["family"],
            "material_kind": job["material_kind"],
            "map": job["map"],
            "source_kind": job["source_kind"],
            "evaluation_target": job["evaluation_target"],
            "processing_rule": job["processing_rule"],
            "files": staged_files,
            "status": "staged",
        }
        (job_dir / "JOB_MANIFEST.json").write_text(
            json.dumps(job_manifest, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        staged_jobs.append(job_manifest)

    staging = {
        "schema": "diyse.asset_forge.validation_staging.v1",
        "batch_id": resolution["batch_id"],
        "status": "READY_FOR_ASSET_FORGE_PROCESSING",
        "mode": mode,
        "workspace": str(output_root.resolve()),
        "job_count": len(staged_jobs),
        "jobs": staged_jobs,
    }
    (output_root / "STAGING_MANIFEST.json").write_text(
        json.dumps(staging, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return staging


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="diyse-texture-validation-stager")
    parser.add_argument("source_root", type=Path, help="Mounted raw source-library root")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--resolution", type=Path, default=Path(".asset_forge/texture_validation_source_resolution.json"))
    parser.add_argument("--stage-dir", type=Path)
    parser.add_argument("--mode", choices=["copy", "hardlink"], default="copy")
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    manifest = load_manifest(args.manifest)
    resolution = resolve_manifest(manifest, args.source_root)
    args.resolution.parent.mkdir(parents=True, exist_ok=True)
    args.resolution.write_text(
        json.dumps(resolution, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps({
        "batch_id": resolution["batch_id"],
        "valid": resolution["valid"],
        "issues": resolution["issues"],
        "job_count": resolution["job_count"],
        "resolution": str(args.resolution),
    }, indent=2))
    if not resolution["valid"]:
        return 2
    if args.stage_dir:
        staged = stage_resolution(resolution, args.stage_dir, args.mode)
        print(json.dumps({
            "status": staged["status"],
            "job_count": staged["job_count"],
            "workspace": staged["workspace"],
        }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
