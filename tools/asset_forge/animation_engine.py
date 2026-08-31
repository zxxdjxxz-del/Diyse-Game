from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json

import numpy as np
from PIL import Image, ImageFilter


@dataclass
class AnimationStyleProfile:
    luts: list[list[int]]
    edge_gain: float
    source_size: tuple[int, int]
    preserve_alpha: bool = True

    def to_dict(self) -> dict:
        return {
            "luts": self.luts,
            "edge_gain": self.edge_gain,
            "source_size": list(self.source_size),
            "preserve_alpha": self.preserve_alpha,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "AnimationStyleProfile":
        return cls(
            luts=data["luts"],
            edge_gain=float(data["edge_gain"]),
            source_size=tuple(data["source_size"]),
            preserve_alpha=bool(data.get("preserve_alpha", True)),
        )


def _quantile_lut(src: np.ndarray, dst: np.ndarray) -> list[int]:
    src = src.reshape(-1)
    dst = dst.reshape(-1)
    if src.size == 0 or dst.size == 0:
        return list(range(256))
    quantiles = np.linspace(0.0, 1.0, 256)
    src_q = np.quantile(src, quantiles)
    dst_q = np.quantile(dst, quantiles)
    unique, idx = np.unique(src_q, return_index=True)
    values = dst_q[idx]
    if len(unique) == 1:
        return [int(np.clip(round(values[0]), 0, 255))] * 256
    mapped = np.interp(np.arange(256, dtype=np.float32), unique, values)
    return np.clip(np.rint(mapped), 0, 255).astype(np.uint8).tolist()


def _edge_mean(rgba: np.ndarray) -> float:
    gray = np.rint(rgba[..., :3].astype(np.float32).mean(axis=2)).astype(np.uint8)
    edge = Image.fromarray(gray, mode="L").filter(ImageFilter.FIND_EDGES)
    return float((np.asarray(edge, dtype=np.float32) / 255.0).mean())


def learn_profile(source_anchor: Path, styled_anchor: Path) -> AnimationStyleProfile:
    """Learn non-spatial style behavior from one approved anchor frame.

    The profile transfers palette distribution and selective edge emphasis. It does
    not copy spatial detail from the anchor, so moving forms in later frames keep
    their own geometry instead of receiving a static painted overlay.
    """
    with Image.open(source_anchor).convert("RGBA") as source_im, Image.open(styled_anchor).convert("RGBA") as styled_im:
        if source_im.size != styled_im.size:
            raise ValueError("styled anchor must have the same dimensions as source anchor")
        source = np.asarray(source_im, dtype=np.uint8)
        styled = np.asarray(styled_im, dtype=np.uint8)

    mask = source[..., 3] > 0
    if not mask.any():
        mask = np.ones(source.shape[:2], dtype=bool)

    luts = [
        _quantile_lut(source[..., channel][mask], styled[..., channel][mask])
        for channel in range(3)
    ]
    source_edge = _edge_mean(source)
    styled_edge = _edge_mean(styled)
    edge_gain = float(np.clip((styled_edge - source_edge) * 2.5, -0.35, 0.55))

    return AnimationStyleProfile(
        luts=luts,
        edge_gain=edge_gain,
        source_size=(source.shape[1], source.shape[0]),
        preserve_alpha=True,
    )


def _edge_map(rgb: np.ndarray) -> np.ndarray:
    gray = np.rint(rgb[..., :3].astype(np.float32).mean(axis=2)).astype(np.uint8)
    edge = Image.fromarray(gray, mode="L").filter(ImageFilter.FIND_EDGES)
    array = np.asarray(edge, dtype=np.float32) / 255.0
    array = np.clip((array - 0.08) / 0.92, 0.0, 1.0)
    return array[..., None]


def apply_profile(source_frame: Path, dest: Path, profile: AnimationStyleProfile) -> None:
    with Image.open(source_frame).convert("RGBA") as image:
        source = np.asarray(image, dtype=np.uint8)

    rgb = source[..., :3]
    mapped = np.empty_like(rgb)
    for channel in range(3):
        lut = np.asarray(profile.luts[channel], dtype=np.uint8)
        mapped[..., channel] = lut[rgb[..., channel]]

    if profile.edge_gain != 0.0:
        edge = _edge_map(rgb)
        work = mapped.astype(np.float32)
        if profile.edge_gain > 0:
            work *= 1.0 - edge * min(profile.edge_gain, 0.75)
        else:
            mean = work.mean(axis=2, keepdims=True)
            work = work * (1.0 + edge * profile.edge_gain) + mean * (-edge * profile.edge_gain)
        mapped = np.clip(np.rint(work), 0, 255).astype(np.uint8)

    alpha = source[..., 3] if profile.preserve_alpha else np.full(source.shape[:2], 255, np.uint8)
    output = np.dstack([mapped, alpha])
    dest.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(output, mode="RGBA").save(dest, format="PNG")


def propagate_sequence(
    source_frames: list[Path],
    styled_anchor: Path,
    output_dir: Path,
    *,
    anchor_index: int = 0,
) -> AnimationStyleProfile:
    if not source_frames:
        raise ValueError("source_frames is empty")
    if anchor_index < 0 or anchor_index >= len(source_frames):
        raise IndexError("anchor_index out of range")

    profile = learn_profile(source_frames[anchor_index], styled_anchor)
    output_dir.mkdir(parents=True, exist_ok=True)

    for index, source in enumerate(source_frames):
        dest = output_dir / (source.stem + "__STYLE_PASS.png")
        if index == anchor_index:
            with Image.open(styled_anchor).convert("RGBA") as image:
                image.save(dest, format="PNG")
        else:
            apply_profile(source, dest, profile)

    (output_dir / "animation_style_profile.json").write_text(
        json.dumps(profile.to_dict(), indent=2), encoding="utf-8"
    )
    return profile
