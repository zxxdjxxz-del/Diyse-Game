from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image


def _rgba(path: Path) -> np.ndarray:
    with Image.open(path).convert("RGBA") as image:
        return np.asarray(image, dtype=np.uint8)


def _jump_vertical(array: np.ndarray, x: int) -> float:
    if x <= 0 or x >= array.shape[1]:
        return 0.0
    left = array[:, x - 1, :3].astype(np.float32)
    right = array[:, x, :3].astype(np.float32)
    return float(np.abs(left - right).mean() / 255.0)


def _jump_horizontal(array: np.ndarray, y: int) -> float:
    if y <= 0 or y >= array.shape[0]:
        return 0.0
    upper = array[y - 1, :, :3].astype(np.float32)
    lower = array[y, :, :3].astype(np.float32)
    return float(np.abs(upper - lower).mean() / 255.0)


def atlas_seam_regression(
    source: Path,
    output: Path,
    patch_plan: list[dict],
    *,
    threshold: float = 0.06,
) -> dict:
    """Measure seam discontinuity introduced at patch boundaries.

    Natural source edges are subtracted from output edge jumps, so an authored wall
    or object boundary that happens to sit on a patch boundary is not automatically
    treated as a processing seam.
    """
    source_array = _rgba(source)
    output_array = _rgba(output)
    if source_array.shape != output_array.shape:
        return {"status": "reject", "reason": "dimension_mismatch"}

    xs = sorted(
        {patch["x0"] for patch in patch_plan if patch["x0"] > 0}
        | {patch["x1"] for patch in patch_plan if patch["x1"] < source_array.shape[1]}
    )
    ys = sorted(
        {patch["y0"] for patch in patch_plan if patch["y0"] > 0}
        | {patch["y1"] for patch in patch_plan if patch["y1"] < source_array.shape[0]}
    )

    regressions = []
    for x in xs:
        regressions.append(_jump_vertical(output_array, x) - _jump_vertical(source_array, x))
    for y in ys:
        regressions.append(_jump_horizontal(output_array, y) - _jump_horizontal(source_array, y))

    worst = max(regressions, default=0.0)
    mean = float(np.mean(regressions)) if regressions else 0.0
    return {
        "status": "review" if worst <= threshold else "reject",
        "worst_new_seam_jump": round(float(worst), 6),
        "mean_new_seam_jump": round(mean, 6),
        "threshold": threshold,
        "boundaries_checked": len(regressions),
    }


def alpha_fringe_metrics(path: Path) -> dict:
    """Return a conservative diagnostic for semi-transparent edge color drift.

    This is intentionally a review metric rather than an automatic rejection rule,
    because dark inked edges can be artistically correct in Diyse.
    """
    rgba = _rgba(path)
    alpha = rgba[..., 3].astype(np.float32) / 255.0
    partial = (alpha > 0.0) & (alpha < 1.0)
    opaque = alpha >= 0.98
    if not partial.any():
        return {"partial_pixels": 0, "status": "review", "fringe_contrast": 0.0}

    luminance = rgba[..., :3].astype(np.float32).mean(axis=2) / 255.0
    partial_mean = float(luminance[partial].mean())
    opaque_mean = float(luminance[opaque].mean()) if opaque.any() else partial_mean
    contrast = abs(partial_mean - opaque_mean)
    return {
        "partial_pixels": int(partial.sum()),
        "partial_luma_mean": round(partial_mean, 6),
        "opaque_luma_mean": round(opaque_mean, 6),
        "fringe_contrast": round(contrast, 6),
        "status": "review",
    }


def animation_flicker_regression(
    source_frames: list[Path],
    output_frames: list[Path],
    *,
    threshold_ratio: float = 1.65,
) -> dict:
    """Compare temporal image-change energy before and after styling.

    This is not optical-flow analysis; it is a fast regression gate that catches
    outputs whose frame-to-frame change grows dramatically beyond the source motion.
    """
    if len(source_frames) != len(output_frames) or len(source_frames) < 2:
        raise ValueError("source/output frame lists must have equal length >= 2")

    def temporal_energy(paths: list[Path]) -> tuple[float, list[float]]:
        arrays = [_rgba(path)[..., :3].astype(np.float32) / 255.0 for path in paths]
        if any(array.shape != arrays[0].shape for array in arrays):
            raise ValueError("all frames must share dimensions")
        values = [
            float(np.abs(arrays[index + 1] - arrays[index]).mean())
            for index in range(len(arrays) - 1)
        ]
        return float(np.mean(values)), values

    source_mean, _ = temporal_energy(source_frames)
    output_mean, _ = temporal_energy(output_frames)
    ratio = output_mean / max(source_mean, 1e-6)
    return {
        "source_temporal_energy": round(source_mean, 6),
        "output_temporal_energy": round(output_mean, 6),
        "regression_ratio": round(ratio, 6),
        "threshold_ratio": threshold_ratio,
        "status": "review" if ratio <= threshold_ratio else "reject",
    }
