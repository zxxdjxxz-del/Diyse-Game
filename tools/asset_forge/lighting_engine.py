from __future__ import annotations

from pathlib import Path
import json

import numpy as np
from PIL import Image


def _load_rgba(path: Path) -> np.ndarray:
    with Image.open(path).convert("RGBA") as image:
        return np.asarray(image, dtype=np.uint8)


def _save_rgba(array: np.ndarray, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(array.astype(np.uint8), mode="RGBA").save(path, format="PNG")


def propagate_lighting_state(
    source_base: Path,
    styled_base: Path,
    source_state: Path,
    dest: Path,
    *,
    ratio_min: float = 0.30,
    ratio_max: float = 3.0,
    strength: float = 1.0,
    preserve_state_alpha: bool = True,
) -> dict:
    """Transfer a source lighting state's relative RGB change onto a styled base.

    This keeps the approved style treatment while preserving the authored direction/
    color behavior of the source lighting state. All three images must have exact
    registration.
    """
    base = _load_rgba(source_base)
    styled = _load_rgba(styled_base)
    state = _load_rgba(source_state)
    if base.shape != styled.shape or base.shape != state.shape:
        raise ValueError("source base, styled base, and lighting state must share exact dimensions")

    base_rgb = base[..., :3].astype(np.float32) / 255.0
    styled_rgb = styled[..., :3].astype(np.float32) / 255.0
    state_rgb = state[..., :3].astype(np.float32) / 255.0
    epsilon = 1.0 / 255.0
    ratio = np.clip((state_rgb + epsilon) / (base_rgb + epsilon), ratio_min, ratio_max)
    if strength != 1.0:
        ratio = 1.0 + (ratio - 1.0) * strength
    output_rgb = np.clip(styled_rgb * ratio, 0.0, 1.0)
    alpha = state[..., 3] if preserve_state_alpha else styled[..., 3]
    output = np.dstack([np.rint(output_rgb * 255.0).astype(np.uint8), alpha])
    _save_rgba(output, dest)
    return {
        "ratio_mean": float(ratio.mean()),
        "ratio_min_observed": float(ratio.min()),
        "ratio_max_observed": float(ratio.max()),
        "strength": strength,
    }


def propagate_lighting_family(
    source_base: Path,
    styled_base: Path,
    states: dict[str, Path],
    output_dir: Path,
    *,
    strength: float = 1.0,
) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    results = {}
    for name, state_path in sorted(states.items()):
        dest = output_dir / f"{state_path.stem}__STYLE_PASS.png"
        results[name] = propagate_lighting_state(
            source_base,
            styled_base,
            state_path,
            dest,
            strength=strength,
        )
        results[name]["output_path"] = str(dest.resolve())
    (output_dir / "lighting_family_profile.json").write_text(
        json.dumps(results, indent=2), encoding="utf-8"
    )
    return results
