#!/usr/bin/env python3
"""Deterministic structure-preserving VFX styling for Diyse Asset Forge.

The first production treatment targets fire/flame sheets. It preserves canvas size,
frame registration and source alpha exactly while converting photographic/noisy fire
into broader painterly value masses with selective dark structural accents and a
bright mostly-unoutlined core.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

GRID_RE = re.compile(r"^(\d+)x(\d+)$", re.IGNORECASE)


def _palette_map(value: np.ndarray) -> np.ndarray:
    stops = np.array([0.0, 0.18, 0.35, 0.55, 0.75, 1.0], dtype=np.float32)
    colors = np.array([
        [0.12, 0.015, 0.005],
        [0.28, 0.025, 0.004],
        [0.62, 0.075, 0.005],
        [1.00, 0.26, 0.015],
        [1.00, 0.68, 0.12],
        [1.00, 0.97, 0.72],
    ], dtype=np.float32)
    out = np.zeros((*value.shape, 3), dtype=np.float32)
    for i in range(len(stops) - 1):
        mask = (value >= stops[i]) & (value <= stops[i + 1])
        t = np.clip((value - stops[i]) / (stops[i + 1] - stops[i] + 1e-6), 0, 1)[..., None]
        interp = colors[i] * (1 - t) + colors[i + 1] * t
        out[mask] = interp[mask]
    out[value > stops[-1]] = colors[-1]
    return out


def stylize_fire_rgba(image: Image.Image) -> Image.Image:
    """Apply the B06 v0.1 fire treatment while preserving source alpha exactly."""
    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8)
    rgb = rgba[..., :3].astype(np.float32) / 255.0
    alpha = rgba[..., 3].astype(np.float32) / 255.0

    smooth = np.stack([
        cv2.bilateralFilter((rgb[..., channel] * 255).astype(np.uint8), 5, 35, 35)
        for channel in range(3)
    ], axis=-1).astype(np.float32) / 255.0
    value = np.clip(
        (smooth[..., 0] * 0.2126 + smooth[..., 1] * 0.7152 + smooth[..., 2] * 0.0722) * 1.14,
        0,
        1,
    )

    out = _palette_map(value)
    quantized = np.round(out * 8.0) / 8.0
    out = out * 0.62 + quantized * 0.38

    alpha_u8 = rgba[..., 3]
    eroded = cv2.erode(alpha_u8, np.ones((3, 3), np.uint8), iterations=1)
    border = (alpha_u8.astype(np.int16) - eroded.astype(np.int16)) > 18

    value_u8 = (value * 255).astype(np.uint8)
    gx = cv2.Sobel(value_u8, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(value_u8, cv2.CV_32F, 0, 1, ksize=3)
    gradient = np.sqrt(gx * gx + gy * gy)
    internal = (gradient > 85) & (alpha > 0.25) & (value < 0.62)

    yy, xx = np.indices(alpha.shape)
    broken_line_mask = ((xx * 13 + yy * 7) % 11) < 7
    internal &= broken_line_mask

    ink_strength = np.zeros_like(value, dtype=np.float32)
    ink_strength[border & (value < 0.70)] = 0.50
    ink_strength[internal] = np.maximum(ink_strength[internal], 0.25)
    ink = np.array([0.10, 0.015, 0.005], dtype=np.float32)
    out = out * (1.0 - ink_strength[..., None]) + ink * ink_strength[..., None]

    core = (value > 0.84) & (alpha > 0.5)
    core_mix = np.clip((value - 0.84) / 0.16, 0, 1)[..., None]
    core_color = np.array([1.0, 0.94, 0.72], dtype=np.float32)
    out = np.where(core[..., None], out * (1.0 - core_mix) + core_color * core_mix, out)

    result = np.dstack([
        np.clip(out * 255.0, 0, 255).astype(np.uint8),
        rgba[..., 3],
    ])
    return Image.fromarray(result, "RGBA")


def split_grid(image: Image.Image, cols: int, rows: int) -> list[Image.Image]:
    if image.width % cols or image.height % rows:
        raise ValueError("Sheet dimensions are not evenly divisible by grid")
    cw, ch = image.width // cols, image.height // rows
    return [
        image.crop((x * cw, y * ch, (x + 1) * cw, (y + 1) * ch))
        for y in range(rows)
        for x in range(cols)
    ]


def _frame_luminance_signature(image: Image.Image, cols: int, rows: int) -> np.ndarray:
    values = []
    for frame in split_grid(image.convert("RGBA"), cols, rows):
        rgba = np.asarray(frame, dtype=np.float32) / 255.0
        alpha = rgba[..., 3]
        lum = rgba[..., 0] * 0.2126 + rgba[..., 1] * 0.7152 + rgba[..., 2] * 0.0722
        weight = np.maximum(alpha.sum(), 1e-6)
        values.append(float((lum * alpha).sum() / weight))
    return np.asarray(values, dtype=np.float32)


def temporal_qa(source: Image.Image, styled: Image.Image, cols: int, rows: int) -> dict:
    """Compare frame-to-frame brightness rhythm without demanding identical color."""
    src = _frame_luminance_signature(source, cols, rows)
    dst = _frame_luminance_signature(styled, cols, rows)
    if np.std(src) < 1e-8 or np.std(dst) < 1e-8:
        correlation = 1.0 if np.allclose(src, dst) else 0.0
    else:
        correlation = float(np.corrcoef(src, dst)[0, 1])
    src_delta = np.abs(np.diff(src))
    dst_delta = np.abs(np.diff(dst))
    source_peak = float(src_delta.max(initial=0.0))
    styled_peak = float(dst_delta.max(initial=0.0))
    peak_ratio = styled_peak / source_peak if source_peak > 1e-8 else 1.0
    alpha_exact = bool(np.array_equal(
        np.asarray(source.convert("RGBA"))[..., 3],
        np.asarray(styled.convert("RGBA"))[..., 3],
    ))
    return {
        "frame_count": cols * rows,
        "luminance_rhythm_correlation": correlation,
        "source_peak_frame_delta": source_peak,
        "styled_peak_frame_delta": styled_peak,
        "peak_delta_ratio": float(peak_ratio),
        "alpha_exact": alpha_exact,
        "pass": bool(alpha_exact and correlation >= 0.95 and peak_ratio <= 1.35),
    }


def parse_grid(value: str) -> tuple[int, int]:
    match = GRID_RE.match(value.strip())
    if not match:
        raise argparse.ArgumentTypeError("Grid must be COLSxROWS, for example 16x4")
    return int(match.group(1)), int(match.group(2))


def main() -> int:
    parser = argparse.ArgumentParser(prog="diyse-vfx-style")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--grid", type=parse_grid, required=True)
    parser.add_argument("--qa-json", type=Path)
    args = parser.parse_args()

    source = Image.open(args.input)
    source.load()
    styled = stylize_fire_rgba(source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    styled.save(args.output)

    qa = temporal_qa(source.convert("RGBA"), styled, *args.grid)
    if args.qa_json:
        args.qa_json.parent.mkdir(parents=True, exist_ok=True)
        args.qa_json.write_text(json.dumps(qa, indent=2), encoding="utf-8")
    print(json.dumps(qa, indent=2))
    return 0 if qa["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
