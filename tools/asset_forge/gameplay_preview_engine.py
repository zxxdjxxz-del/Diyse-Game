#!/usr/bin/env python3
"""Deterministic gameplay-scale preview composition for Diyse Asset Forge.

Uses each source glTF's real physical extents to scale validation renders relative to one
another and to a representative 1.75-unit field-character silhouette. This catches cases
where a prop only looks readable because its individual review render was zoomed to fill a
thumbnail.
"""
from __future__ import annotations

from pathlib import Path
from typing import Mapping

import numpy as np
import trimesh
from PIL import Image, ImageDraw, ImageFilter, ImageFont


def model_extent(gltf: Path) -> np.ndarray:
    scene = trimesh.load(gltf, force='scene', process=False)
    vertices = []
    for node in scene.graph.nodes_geometry:
        transform, geometry_name = scene.graph[node]
        mesh = scene.geometry[geometry_name]
        vertices.append(trimesh.transform_points(mesh.vertices, transform))
    if not vertices:
        raise RuntimeError(f'No geometry found: {gltf}')
    points = np.vstack(vertices)
    return points.max(0) - points.min(0)


def _key_background(path: Path) -> Image.Image:
    image = Image.open(path).convert('RGB')
    array = np.array(image).astype(np.int16)
    samples = np.vstack([
        array[:8, :8].reshape(-1, 3),
        array[:8, -8:].reshape(-1, 3),
        array[-8:, :8].reshape(-1, 3),
        array[-8:, -8:].reshape(-1, 3),
    ])
    background = np.median(samples, axis=0)
    distance = np.sqrt(((array - background) ** 2).sum(2))
    alpha = np.clip((distance - 5) * 18, 0, 255).astype(np.uint8)
    rgba = np.dstack([array.astype(np.uint8), alpha])
    result = Image.fromarray(rgba, 'RGBA')
    box = result.getbbox()
    return result.crop(box) if box else result


def compose_preview(
    gltfs: Mapping[str, Path],
    renders: Mapping[str, Path],
    output: Path,
    width: int = 1280,
    height: int = 720,
    pixels_per_unit: float = 155.0,
    character_height_units: float = 1.75,
) -> None:
    canvas = Image.new('RGB', (width, height), (26, 25, 27))
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()

    wall_y = int(height * 0.68)
    draw.rectangle((0, 0, width, wall_y), fill=(33, 31, 30))
    draw.rectangle((0, wall_y, width, height), fill=(44, 38, 31))
    for y in range(wall_y + 24, height, 34):
        draw.line((0, y, width, y), fill=(51, 44, 36), width=1)
    draw.line((0, wall_y, width, wall_y), fill=(74, 62, 49), width=2)

    contact = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    contact_draw = ImageDraw.Draw(contact)
    contact_draw.ellipse((90, wall_y - 4, width - 80, height - 22), fill=(0, 0, 0, 42))
    contact = contact.filter(ImageFilter.GaussianBlur(28))
    canvas = Image.alpha_composite(canvas.convert('RGBA'), contact).convert('RGB')

    placements = {
        'Barrel': (0.18, wall_y + 5, 'ground'),
        'Chair_1': (0.39, wall_y + 5, 'ground'),
        'Workbench': (0.72, wall_y + 3, 'ground'),
        'Lantern_Wall': (0.83, wall_y - int(height * 0.35), 'wall'),
    }

    for model, (x_fraction, baseline, placement_kind) in placements.items():
        if model not in renders or model not in gltfs:
            continue
        extent = model_extent(gltfs[model])
        foreground = _key_background(renders[model])
        target_height = max(int(extent[1] * pixels_per_unit), 32)
        scale = target_height / max(foreground.height, 1)
        target_width = max(int(foreground.width * scale), 1)
        foreground = foreground.resize((target_width, target_height), Image.Resampling.LANCZOS)
        x = int(width * x_fraction - target_width / 2)
        y = int(baseline - target_height) if placement_kind == 'ground' else int(baseline)
        canvas.paste(foreground, (x, y), foreground)

    # Representative field-character scale marker. This is a neutral measurement silhouette,
    # not a character-art authority.
    character_height = int(character_height_units * pixels_per_unit)
    character_x = int(width * 0.53)
    character_base = wall_y + 5
    character_y = character_base - character_height
    draw = ImageDraw.Draw(canvas)
    head_radius = max(int(character_height * 0.07), 6)
    head_center_y = character_y + head_radius + 3
    draw.ellipse(
        (
            character_x - head_radius,
            head_center_y - head_radius,
            character_x + head_radius,
            head_center_y + head_radius,
        ),
        fill=(18, 18, 20),
        outline=(112, 105, 94),
    )
    body_top = head_center_y + head_radius
    body_bottom = character_base - int(character_height * 0.12)
    shoulder = int(character_height * 0.10)
    draw.polygon(
        [
            (character_x - shoulder, body_top + 8),
            (character_x + shoulder, body_top + 8),
            (character_x + int(shoulder * 0.58), body_bottom),
            (character_x - int(shoulder * 0.58), body_bottom),
        ],
        fill=(19, 19, 21),
        outline=(112, 105, 94),
    )
    draw.line(
        (character_x - int(shoulder * 0.32), body_bottom, character_x - int(shoulder * 0.40), character_base),
        fill=(112, 105, 94),
        width=3,
    )
    draw.line(
        (character_x + int(shoulder * 0.32), body_bottom, character_x + int(shoulder * 0.40), character_base),
        fill=(112, 105, 94),
        width=3,
    )

    draw.rectangle((16, 14, 488, 62), fill=(20, 20, 22))
    draw.text((28, 24), 'B10 GAMEPLAY-SCALE WORKSHOP INTEGRATION', fill=(234, 224, 202), font=font)
    draw.text(
        (28, 43),
        f'real glTF extents | {character_height_units:.2f}-unit character | shared-material validation',
        fill=(170, 170, 170),
        font=font,
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, 'PNG')


def main() -> int:
    raise SystemExit('Use compose_preview() from prop_pack_pipeline.py')


if __name__ == '__main__':
    main()
