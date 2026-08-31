from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Callable
import json

import numpy as np
from PIL import Image


@dataclass(frozen=True)
class AtlasPatch:
    index: int
    x0: int
    y0: int
    x1: int
    y1: int

    @property
    def width(self) -> int:
        return self.x1 - self.x0

    @property
    def height(self) -> int:
        return self.y1 - self.y0


def _starts(length: int, tile: int, overlap: int) -> list[int]:
    if tile <= 0:
        raise ValueError("tile must be > 0")
    if overlap < 0 or overlap >= tile:
        raise ValueError("overlap must satisfy 0 <= overlap < tile")
    if length <= tile:
        return [0]
    step = tile - overlap
    out = list(range(0, max(1, length - tile + 1), step))
    last = length - tile
    if out[-1] != last:
        out.append(last)
    return sorted(set(out))


def build_patch_plan(width: int, height: int, tile: int = 768, overlap: int = 96) -> list[AtlasPatch]:
    patches: list[AtlasPatch] = []
    index = 0
    for y in _starts(height, tile, overlap):
        for x in _starts(width, tile, overlap):
            patches.append(AtlasPatch(index, x, y, min(x + tile, width), min(y + tile, height)))
            index += 1
    return patches


def write_patch_manifest(source: Path, output: Path, tile: int = 768, overlap: int = 96) -> dict:
    with Image.open(source) as im:
        patches = build_patch_plan(im.width, im.height, tile=tile, overlap=overlap)
        payload = {
            "source": str(source.resolve()),
            "width": im.width,
            "height": im.height,
            "tile": tile,
            "overlap": overlap,
            "patches": [asdict(p) for p in patches],
        }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload


def _axis_weight(length: int, feather: int, touches_low: bool, touches_high: bool) -> np.ndarray:
    weight = np.ones(length, dtype=np.float32)
    if feather <= 0:
        return weight
    f = min(feather, max(1, length // 2))
    ramp = np.linspace(0.001, 1.0, f, dtype=np.float32)
    if not touches_low:
        weight[:f] = np.minimum(weight[:f], ramp)
    if not touches_high:
        weight[-f:] = np.minimum(weight[-f:], ramp[::-1])
    return weight


def feather_mask(patch: AtlasPatch, canvas_w: int, canvas_h: int, overlap: int) -> np.ndarray:
    wx = _axis_weight(patch.width, overlap, patch.x0 == 0, patch.x1 == canvas_w)
    wy = _axis_weight(patch.height, overlap, patch.y0 == 0, patch.y1 == canvas_h)
    return wy[:, None] * wx[None, :]


PatchProcessor = Callable[[Image.Image, AtlasPatch], Image.Image]


def process_atlas(
    source: Path,
    dest: Path,
    processor: PatchProcessor,
    *,
    tile: int = 768,
    overlap: int = 96,
    preserve_alpha: bool = True,
) -> list[AtlasPatch]:
    """Process an atlas as coordinate-locked overlapping crops.

    The processor must return the same pixel dimensions as its input crop. Atlas
    coordinates are never rearranged. Overlaps are feather-blended, and source
    alpha can be restored after RGB treatment.
    """
    with Image.open(source) as src_im:
        source_has_alpha = "A" in src_im.getbands() or "transparency" in src_im.info
        src = src_im.convert("RGBA")
        width, height = src.size
        patches = build_patch_plan(width, height, tile=tile, overlap=overlap)

        accum = np.zeros((height, width, 4), dtype=np.float64)
        weights = np.zeros((height, width, 1), dtype=np.float64)

        for patch in patches:
            crop = src.crop((patch.x0, patch.y0, patch.x1, patch.y1))
            edited = processor(crop.copy(), patch)
            if edited.size != crop.size:
                raise ValueError(
                    f"patch {patch.index} changed size from {crop.size} to {edited.size}; "
                    "atlas registration would be destroyed"
                )
            array = np.asarray(edited.convert("RGBA"), dtype=np.float64)
            mask = feather_mask(patch, width, height, overlap).astype(np.float64)[..., None]
            accum[patch.y0:patch.y1, patch.x0:patch.x1] += array * mask
            weights[patch.y0:patch.y1, patch.x0:patch.x1] += mask

        out = np.divide(accum, np.maximum(weights, 1e-9))
        out = np.clip(np.rint(out), 0, 255).astype(np.uint8)

        if preserve_alpha and source_has_alpha:
            out[..., 3] = np.asarray(src.getchannel("A"), dtype=np.uint8)

        dest.parent.mkdir(parents=True, exist_ok=True)
        Image.fromarray(out, mode="RGBA").save(dest, format="PNG")
        return patches
