#!/usr/bin/env python3
"""Grid- and mask-safe VFX processing helpers for Diyse Asset Forge v0.9."""
from __future__ import annotations

import argparse
import io
import json
import re
import zipfile
from pathlib import Path
from typing import Iterable

import numpy as np
from PIL import Image

GRID_RE = re.compile(r"_(\d+)x(\d+)(?:\.[^.]+)$", re.IGNORECASE)
IMAGE_EXTS = {".png", ".tga", ".jpg", ".jpeg", ".webp"}


def is_metadata_path(name: str) -> bool:
    norm = name.replace("\\", "/")
    base = Path(norm).name
    return norm.startswith("__MACOSX/") or "/__MACOSX/" in norm or base == ".DS_Store" or base.startswith("._")


def parse_grid_from_name(name: str) -> tuple[int, int] | None:
    m = GRID_RE.search(Path(name).name)
    return (int(m.group(1)), int(m.group(2))) if m else None


def split_grid(image: Image.Image, cols: int, rows: int) -> list[Image.Image]:
    w, h = image.size
    if cols <= 0 or rows <= 0 or w % cols or h % rows:
        raise ValueError(f"Image {w}x{h} is not evenly divisible by {cols}x{rows}")
    cw, ch = w // cols, h // rows
    return [image.crop((x*cw, y*ch, (x+1)*cw, (y+1)*ch)) for y in range(rows) for x in range(cols)]


def reassemble_grid(frames: list[Image.Image], cols: int, rows: int, *, source: Image.Image | None = None) -> Image.Image:
    if len(frames) != cols * rows:
        raise ValueError("Frame count does not match grid")
    fw, fh = frames[0].size
    mode = source.mode if source is not None else frames[0].mode
    out = Image.new(mode, (fw * cols, fh * rows))
    if source is not None and mode == "P" and source.getpalette() is not None:
        out.putpalette(source.getpalette())
    for i, frame in enumerate(frames):
        out.paste(frame, ((i % cols) * fw, (i // cols) * fh))
    return out


def grid_roundtrip_qa(image: Image.Image, cols: int, rows: int) -> dict:
    rebuilt = reassemble_grid(split_grid(image, cols, rows), cols, rows, source=image)
    a = np.asarray(image.convert("RGBA"), dtype=np.int16)
    b = np.asarray(rebuilt.convert("RGBA"), dtype=np.int16)
    diff = np.abs(a - b)
    return {
        "exact": bool(np.array_equal(a, b)),
        "max_channel_difference": int(diff.max(initial=0)),
        "mean_absolute_difference": float(diff.mean()),
        "frame_count": cols * rows,
        "cell_width": image.width // cols,
        "cell_height": image.height // rows,
    }


def normalize_particle_stem(name: str) -> str:
    stem = Path(name).stem.lower()
    return re.sub(r"_a$", "", stem)


def pair_particles(paths: Iterable[str]) -> dict:
    colors, alphas = {}, {}
    for path in paths:
        norm = path.replace("\\", "/")
        low = norm.lower()
        if "/particles/opague/" in low:
            colors[normalize_particle_stem(norm)] = norm
        elif "/particles/alpha/" in low:
            alphas[normalize_particle_stem(norm)] = norm
    matched = {k: {"color": colors[k], "alpha": alphas[k]} for k in sorted(colors.keys() & alphas.keys())}
    return {
        "matched": matched,
        "unmatched_color": [colors[k] for k in sorted(colors.keys() - alphas.keys())],
        "unmatched_alpha": [alphas[k] for k in sorted(alphas.keys() - colors.keys())],
    }


def inspect_vfx_zip(path: Path) -> dict:
    sheets, images = [], []
    with zipfile.ZipFile(path) as zf:
        names = [n for n in zf.namelist() if not n.endswith("/") and not is_metadata_path(n)]
        image_names = [n for n in names if Path(n).suffix.lower() in IMAGE_EXTS]
        for name in image_names:
            grid = parse_grid_from_name(name)
            row = {"member": name, "grid": grid}
            if grid:
                data = zf.read(name)
                with Image.open(io.BytesIO(data)) as im:
                    im.load()
                    qa = grid_roundtrip_qa(im, *grid)
                row.update(qa)
                sheets.append(row)
            images.append(row)
    pairs = pair_particles(image_names)
    return {
        "archive": path.name,
        "image_members": len(image_names),
        "grid_sheets": len(sheets),
        "grid_frames": sum(s["frame_count"] for s in sheets),
        "all_grid_roundtrips_exact": all(s["exact"] for s in sheets),
        "matched_particle_pairs": len(pairs["matched"]),
        "unmatched_color": pairs["unmatched_color"],
        "unmatched_alpha": pairs["unmatched_alpha"],
        "sheets": sheets,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("archive", type=Path)
    ap.add_argument("--output", type=Path, default=Path(".asset_forge/vfx_processing_manifest.json"))
    args = ap.parse_args()
    result = inspect_vfx_zip(args.archive)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("image_members", "grid_sheets", "grid_frames", "all_grid_roundtrips_exact", "matched_particle_pairs")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
