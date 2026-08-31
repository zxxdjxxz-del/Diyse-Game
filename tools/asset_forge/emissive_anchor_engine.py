#!/usr/bin/env python3
"""Derive exportable model-space emissive anchors for light-source props.

Some verified CC0 source models, such as Lantern_Wall, do not ship with an emissive material.
Rather than baking a fake screen-space glow into review renders, Asset Forge records an
explicit model-space emitter anchor that can later drive a Godot light/emissive overlay.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import trimesh


def derive_emissive_anchor(gltf: Path) -> dict | None:
    if 'lantern' not in gltf.stem.lower():
        return None

    scene = trimesh.load(gltf, force='scene', process=False)
    vertices = []
    for node in scene.graph.nodes_geometry:
        transform, geometry_name = scene.graph[node]
        mesh = scene.geometry[geometry_name]
        vertices.append(trimesh.transform_points(mesh.vertices, transform))
    if not vertices:
        return None

    points = np.vstack(vertices)
    ymin, ymax = points[:, 1].min(), points[:, 1].max()
    cutoff = ymin + (ymax - ymin) * 0.38
    lower = points[points[:, 1] <= cutoff]
    if len(lower) < 8:
        lower = points

    center = np.median(lower, axis=0)
    center[2] = np.percentile(lower[:, 2], 60)
    extent = lower.max(0) - lower.min(0)
    radius = float(max(extent[[0, 1]].max() * 0.16, 0.035))
    scene_extent = points.max(0) - points.min(0)

    return {
        'model': gltf.stem,
        'position_model_space': [round(float(x), 6) for x in center],
        'core_radius': round(radius, 6),
        'light_range': round(float(max(scene_extent) * 0.85), 6),
        'color_srgb': [255, 176, 82],
        'intensity_baseline': 1.0,
        'source_authored_emissive': False,
        'authoring_method': 'derived_lower_cage_anchor',
    }


def write_anchor_manifest(gltf: Path, output: Path) -> dict | None:
    anchor = derive_emissive_anchor(gltf)
    if anchor is None:
        return None
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(anchor, indent=2), encoding='utf-8')
    return anchor


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(prog='diyse-emissive-anchor')
    parser.add_argument('gltf', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    anchor = derive_emissive_anchor(args.gltf)
    if args.output and anchor is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(anchor, indent=2), encoding='utf-8')
    print(json.dumps(anchor, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
