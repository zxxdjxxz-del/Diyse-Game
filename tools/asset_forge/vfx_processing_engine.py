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


def resolve_grid_layout(width: int, height: int, cols: int, rows: int, max_trailing_padding: int = 16) -> dict:
    """Resolve declared grid plus small right/bottom source padding.

    Some CC0 sheets are power-of-two/padded canvases whose filename grid describes the
    active frame rectangle. Padding is preserved and never treated as an extra frame.
    """
    if cols <= 0 or rows <= 0:
        raise ValueError("Grid dimensions must be positive")
    active_w = (width // cols) * cols
    active_h = (height // rows) * rows
    pad_right = width - active_w
    pad_bottom = height - active_h
    if active_w <= 0 or active_h <= 0 or pad_right > max_trailing_padding or pad_bottom > max_trailing_padding:
        raise ValueError(f"Cannot safely resolve {width}x{height} as {cols}x{rows}; trailing padding would be {pad_right}x{pad_bottom}")
    return {
        "cols": cols,
        "rows": rows,
        "active_width": active_w,
        "active_height": active_h,
        "padding_right": pad_right,
        "padding_bottom": pad_bottom,
        "cell_width": active_w // cols,
        "cell_height": active_h // rows,
    }


def split_grid(image: Image.Image, cols: int, rows: int, *, layout: dict | None = None) -> list[Image.Image]:
    layout = layout or resolve_grid_layout(image.width, image.height, cols, rows)
    cw, ch = layout["cell_width"], layout["cell_height"]
    return [image.crop((x*cw, y*ch, (x+1)*cw, (y+1)*ch)) for y in range(rows) for x in range(cols)]


def reassemble_grid(frames: list[Image.Image], cols: int, rows: int, *, source: Image.Image, layout: dict | None = None) -> Image.Image:
    if len(frames) != cols * rows:
        raise ValueError("Frame count does not match grid")
    layout = layout or resolve_grid_layout(source.width, source.height, cols, rows)
    cw, ch = layout["cell_width"], layout["cell_height"]
    out = source.copy()  # preserves palette, transparency metadata, and source padding
    for i, frame in enumerate(frames):
        if frame.size != (cw, ch):
            raise ValueError("Frame dimensions do not match resolved grid cell")
        out.paste(frame, ((i % cols) * cw, (i // cols) * ch))
    return out


def grid_roundtrip_qa(image: Image.Image, cols: int, rows: int) -> dict:
    layout = resolve_grid_layout(image.width, image.height, cols, rows)
    rebuilt = reassemble_grid(split_grid(image, cols, rows, layout=layout), cols, rows, source=image, layout=layout)
    a = np.asarray(image.convert("RGBA"), dtype=np.int16)
    b = np.asarray(rebuilt.convert("RGBA"), dtype=np.int16)
    diff = np.abs(a - b)
    return {
        "exact": bool(np.array_equal(a, b)),
        "max_channel_difference": int(diff.max(initial=0)),
        "mean_absolute_difference": float(diff.mean()),
        "frame_count": cols * rows,
        **layout,
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
    sheets = []
    with zipfile.ZipFile(path) as zf:
        names = [n for n in zf.namelist() if not n.endswith("/") and not is_metadata_path(n)]
        image_names = [n for n in names if Path(n).suffix.lower() in IMAGE_EXTS]
        for name in image_names:
            grid = parse_grid_from_name(name)
            if not grid:
                continue
            data = zf.read(name)
            with Image.open(io.BytesIO(data)) as im:
                im.load()
                qa = grid_roundtrip_qa(im, *grid)
            sheets.append({"member": name, "declared_grid": grid, **qa})
    pairs = pair_particles(image_names)
    return {
        "archive": path.name,
        "image_members": len(image_names),
        "grid_sheets": len(sheets),
        "grid_frames": sum(s["frame_count"] for s in sheets),
        "padded_grid_sheets": sum(1 for s in sheets if s["padding_right"] or s["padding_bottom"]),
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
    print(json.dumps({k: result[k] for k in ("image_members", "grid_sheets", "grid_frames", "padded_grid_sheets", "all_grid_roundtrips_exact", "matched_particle_pairs")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
