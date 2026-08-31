#!/usr/bin/env python3
"""Deterministic UV-safe material stylization for Diyse Asset Forge.

This backend is intentionally non-generative: it preserves every pixel coordinate and
is suitable as a zero-drift baseline for shared trim atlases before optional AI edits.

v2 refinement rules:
- preserve broad authored source planes instead of generating an edge field from every detail;
- keep only sparse meaningful existing dark strokes for wood;
- give metal stronger controlled plane/highlight separation without a universal outline;
- preserve exact UV registration and image dimensions.
"""
from __future__ import annotations

from pathlib import Path
from typing import Literal

import cv2
import numpy as np
from PIL import Image

MaterialKind = Literal['wood', 'metal']


def _palette(lum: np.ndarray, kind: MaterialKind) -> np.ndarray:
    t = np.clip(lum, 0, 1)[..., None]
    if kind == 'wood':
        dark = np.array([55, 35, 25.], np.float32)
        mid = np.array([116, 72, 43.], np.float32)
        light = np.array([174, 121, 74.], np.float32)
        return np.where(
            t < 0.50,
            dark + (mid - dark) * (t / 0.50),
            mid + (light - mid) * ((t - 0.50) / 0.50),
        )

    dark = np.array([42, 47, 52.], np.float32)
    mid = np.array([95, 103, 110.], np.float32)
    light = np.array([184, 190, 192.], np.float32)
    return np.where(
        t < 0.58,
        dark + (mid - dark) * (t / 0.58),
        mid + (light - mid) * ((t - 0.58) / 0.42),
    )


def _large_components(mask: np.ndarray, min_area: int) -> np.ndarray:
    count, labels, stats, _ = cv2.connectedComponentsWithStats(mask.astype(np.uint8), 8)
    out = np.zeros(mask.shape, np.uint8)
    for index in range(1, count):
        if stats[index, cv2.CC_STAT_AREA] >= min_area:
            out[labels == index] = 1
    return out


def stylize_material_image(image: Image.Image, kind: MaterialKind) -> Image.Image:
    source = np.array(image.convert('RGB'), dtype=np.uint8)

    # Broad painterly planes while keeping the source's authored trim layout intact.
    smooth = cv2.bilateralFilter(
        source,
        d=0,
        sigmaColor=18 if kind == 'wood' else 14,
        sigmaSpace=4,
    )
    gray = cv2.cvtColor(smooth, cv2.COLOR_RGB2GRAY).astype(np.float32) / 255.0
    broad = cv2.GaussianBlur(gray, (0, 0), 3.0)

    levels = 7 if kind == 'wood' else 8
    bands = np.round(broad * (levels - 1)) / (levels - 1)
    grouped = 0.62 * broad + 0.38 * bands
    palette = _palette(grouped, kind)

    # The Quaternius trims are already stylized; preserve a little source color evidence rather
    # than replacing the whole atlas with a flat procedural palette.
    if kind == 'wood':
        base = 0.18 * smooth.astype(np.float32) + 0.82 * palette
    else:
        base = 0.12 * smooth.astype(np.float32) + 0.88 * palette

    # Preserve only meaningful existing dark marks. The earlier pass used a Laplacian edge field,
    # which made wood look over-inked because every small source groove became a dark stroke.
    low = cv2.GaussianBlur(gray, (0, 0), 5.0)
    dark_residual = np.maximum(low - gray, 0)
    positive = dark_residual[dark_residual > 0]
    percentile = 96.5 if kind == 'wood' else 94.0
    threshold = float(np.percentile(positive, percentile)) if positive.size else 0.05
    mask = (dark_residual > max(threshold, 0.025)).astype(np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
    mask = _large_components(mask, min_area=10 if kind == 'wood' else 7)
    if kind == 'wood':
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((1, 3), np.uint8))

    ink = cv2.GaussianBlur(mask.astype(np.float32), (0, 0), 0.55)[..., None]
    ink_color = np.array([48, 31, 23.] if kind == 'wood' else [27, 31, 34.], np.float32)
    strength = 0.34 if kind == 'wood' else 0.48
    base = base * (1 - strength * ink) + ink_color * (strength * ink)

    # Controlled highlights. Wood gets only sparse worn/light-facing accents. Metal retains stronger
    # authored highlight separation so it stays distinct from wood under neutral gameplay lighting.
    high_residual = np.maximum(gray - cv2.GaussianBlur(gray, (0, 0), 7.0), 0)
    high_positive = high_residual[high_residual > 0]
    high_percentile = 98.5 if kind == 'wood' else 94.0
    high_threshold = float(np.percentile(high_positive, high_percentile)) if high_positive.size else 0.05
    high_mask = (high_residual > max(high_threshold, 0.025)).astype(np.uint8)
    high_mask = _large_components(high_mask, min_area=12 if kind == 'wood' else 6)
    highlight = cv2.GaussianBlur(high_mask.astype(np.float32), (0, 0), 0.70)[..., None]

    if kind == 'wood':
        highlight_color = np.array([205, 151, 91.], np.float32)
        highlight_strength = 0.10
    else:
        highlight_color = np.array([218, 222, 218.], np.float32)
        highlight_strength = 0.24

    base = base * (1 - highlight_strength * highlight) + highlight_color * (highlight_strength * highlight)

    # Restore only low-frequency material variation; high-frequency pore/scratch noise stays suppressed.
    residual = (gray - cv2.GaussianBlur(gray, (0, 0), 12.0))[..., None]
    base = np.clip(base + residual * (5 if kind == 'wood' else 3), 0, 255).astype(np.uint8)
    return Image.fromarray(base, 'RGB')


def stylize_material_file(source: Path, output: Path, kind: MaterialKind) -> None:
    with Image.open(source) as image:
        styled = stylize_material_image(image, kind)
    output.parent.mkdir(parents=True, exist_ok=True)
    styled.save(output, format='PNG')


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--kind', choices=['wood', 'metal'], required=True)
    args = parser.parse_args()
    stylize_material_file(args.source, args.output, args.kind)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
