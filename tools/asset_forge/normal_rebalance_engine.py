#!/usr/bin/env python3
"""Deterministic tangent-normal rebalance for Diyse Asset Forge.

Used when PBR QA finds excessive normal relief on a shared material atlas. The operation
preserves UV coordinates and image dimensions while reducing X/Y perturbation toward the
flat tangent-space normal (128,128,255).
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image


def rebalance_normal_image(image: Image.Image, strength: float = 0.72) -> Image.Image:
    if not 0.0 <= strength <= 1.0:
        raise ValueError('strength must be between 0 and 1')

    rgb = np.array(image.convert('RGB'), dtype=np.float32) / 255.0
    normal = rgb * 2.0 - 1.0
    x = normal[..., 0] * strength
    y = normal[..., 1] * strength
    z = np.sqrt(np.clip(1.0 - x * x - y * y, 0.0, 1.0))
    rebuilt = np.stack([x, y, z], axis=-1)
    encoded = np.clip((rebuilt * 0.5 + 0.5) * 255.0, 0, 255).astype(np.uint8)
    return Image.fromarray(encoded, 'RGB')


def rebalance_normal_file(source: Path, output: Path, strength: float = 0.72) -> None:
    with Image.open(source) as image:
        result = rebalance_normal_image(image, strength=strength)
    output.parent.mkdir(parents=True, exist_ok=True)
    result.save(output, format='PNG')


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(prog='diyse-normal-rebalance')
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--strength', type=float, default=0.72)
    args = parser.parse_args()
    rebalance_normal_file(args.source, args.output, strength=args.strength)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
