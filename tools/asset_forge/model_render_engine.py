#!/usr/bin/env python3
"""Small deterministic software renderer for Diyse Asset Forge prop validation.

Purpose: stable neutral/warm/cool review renders from glTF assets without requiring
Blender/OpenGL in CI. It is a validation renderer, not the final Godot renderer.

v2 adds:
- ORM-aware stylized specular response so metal and wood separate more clearly;
- automatic authored lantern emitter anchors in model space;
- a visible emissive core plus restrained halo rather than a fixed screen-space glow hint.
"""
from __future__ import annotations

from pathlib import Path
from typing import Mapping

import numpy as np
import trimesh
from PIL import Image, ImageDraw, ImageFilter


def _camera_basis(view=np.array([1.35, 0.85, 1.55], dtype=np.float64)):
    forward = -view / np.linalg.norm(view)
    world_up = np.array([0.0, 1.0, 0.0])
    right = np.cross(forward, world_up)
    right /= np.linalg.norm(right)
    up = np.cross(right, forward)
    up /= np.linalg.norm(up)
    return right, up, forward


def _load_texture(path: Path) -> np.ndarray:
    return np.array(Image.open(path).convert('RGB'))


def _infer_orm(gltf: Path, material_name: str) -> Path | None:
    name = material_name.lower()
    if 'furniture' in name:
        family = 'Furniture'
    elif 'metal' in name:
        family = 'Metal'
    else:
        return None
    path = gltf.parent / f'T_Trim_{family}_ORM.png'
    return path if path.exists() else None


def _find_emitter_anchor(vertices: np.ndarray, model_name: str):
    """Author a stable model-space emitter for lantern-style props.

    The source Quaternius wall lantern has no emissive material. For validation and later
    engine export we derive an explicit light-source anchor from the lower hanging cage,
    rather than faking a fixed glow at an arbitrary screen coordinate.
    """
    if 'lantern' not in model_name.lower():
        return None
    ymin, ymax = vertices[:, 1].min(), vertices[:, 1].max()
    cutoff = ymin + (ymax - ymin) * 0.38
    lower = vertices[vertices[:, 1] <= cutoff]
    if len(lower) < 8:
        lower = vertices
    center = np.median(lower, axis=0)
    center[2] = np.percentile(lower[:, 2], 60)
    radius = float(max((lower.max(0) - lower.min(0))[[0, 1]].max() * 0.16, 0.035))
    return center, radius


def render_gltf(
    gltf: Path,
    output: Path,
    material_textures: Mapping[str, Path],
    size: int = 512,
    lighting: str = 'neutral',
    emissive_hint: bool = False,
    author_emissive: bool | None = None,
) -> None:
    """Render a glTF using shared styled BaseColor trims and source ORM data.

    `emissive_hint` remains for backward compatibility. New callers should use
    `author_emissive=True`, which binds the glow to a model-space emitter anchor.
    """
    if author_emissive is None:
        author_emissive = emissive_hint

    scene = trimesh.load(gltf, force='scene', process=False)
    textures = {name: _load_texture(Path(path)) for name, path in material_textures.items()}
    orm_textures: dict[str, np.ndarray | None] = {}
    pieces = []
    all_vertices = []

    for node in scene.graph.nodes_geometry:
        transform, geometry_name = scene.graph[node]
        mesh = scene.geometry[geometry_name]
        if getattr(mesh.visual, 'uv', None) is None:
            continue
        material = mesh.visual.material.name
        if material not in textures:
            continue
        if material not in orm_textures:
            orm_path = _infer_orm(gltf, material)
            orm_textures[material] = _load_texture(orm_path) if orm_path else None
        vertices = trimesh.transform_points(mesh.vertices, transform)
        pieces.append((vertices, np.asarray(mesh.faces, dtype=np.int64), np.asarray(mesh.visual.uv, dtype=np.float64), material))
        all_vertices.append(vertices)

    if not pieces:
        raise RuntimeError(f'No renderable textured geometry found: {gltf}')

    vertices_all = np.vstack(all_vertices)
    center = (vertices_all.min(0) + vertices_all.max(0)) / 2
    right, up, forward = _camera_basis()
    view_dir = -forward

    projected = []
    for vertices, faces, uv, material in pieces:
        local = vertices - center
        projected.append((local, local @ right, local @ up, local @ forward, faces, uv, material))

    all_x = np.concatenate([piece[1] for piece in projected])
    all_y = np.concatenate([piece[2] for piece in projected])
    span = max(np.ptp(all_x), np.ptp(all_y), 1e-6)
    scale = (size * 0.76) / span

    background = {
        'neutral': (26, 26, 28),
        'warm': (31, 26, 23),
        'cool': (22, 27, 33),
    }[lighting]
    light_dir = {
        'neutral': np.array([-0.35, 0.65, 0.68]),
        'warm': np.array([-0.55, 0.48, 0.68]),
        'cool': np.array([0.30, 0.60, 0.74]),
    }[lighting].astype(np.float64)
    light_dir /= np.linalg.norm(light_dir)
    tint = np.array({
        'neutral': (1.0, 1.0, 1.0),
        'warm': (1.08, 0.93, 0.82),
        'cool': (0.84, 0.93, 1.08),
    }[lighting])
    half_vector = light_dir + view_dir
    half_vector /= np.linalg.norm(half_vector)

    image = np.empty((size, size, 3), np.float32)
    image[:] = background
    zbuffer = np.full((size, size), np.inf, np.float32)

    for local, x, y, z, faces, uv, material in projected:
        sx = x * scale + size / 2
        sy = -y * scale + size * 0.54
        depth = -z
        texture = textures[material]
        orm = orm_textures[material]
        tex_h, tex_w = texture.shape[:2]
        is_metal = 'metal' in material.lower()

        for face in faces:
            points = np.stack([sx[face], sy[face]], axis=1)
            xmin = max(int(np.floor(points[:, 0].min())), 0)
            xmax = min(int(np.ceil(points[:, 0].max())), size - 1)
            ymin = max(int(np.floor(points[:, 1].min())), 0)
            ymax = min(int(np.ceil(points[:, 1].max())), size - 1)
            if xmax < xmin or ymax < ymin:
                continue

            a, b, c = points
            denominator = (b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1])
            if abs(denominator) < 1e-9:
                continue

            xx = np.arange(xmin, xmax + 1)
            yy = np.arange(ymin, ymax + 1)
            X, Y = np.meshgrid(xx, yy)
            w0 = ((b[1] - c[1]) * (X - c[0]) + (c[0] - b[0]) * (Y - c[1])) / denominator
            w1 = ((c[1] - a[1]) * (X - c[0]) + (a[0] - c[0]) * (Y - c[1])) / denominator
            w2 = 1 - w0 - w1
            inside = (w0 >= -1e-5) & (w1 >= -1e-5) & (w2 >= -1e-5)
            if not inside.any():
                continue

            zz = w0 * depth[face[0]] + w1 * depth[face[1]] + w2 * depth[face[2]]
            zsub = zbuffer[ymin:ymax + 1, xmin:xmax + 1]
            mask = inside & (zz < zsub)
            if not mask.any():
                continue

            tex_uv = w0[..., None] * uv[face[0]] + w1[..., None] * uv[face[1]] + w2[..., None] * uv[face[2]]
            u = np.mod(tex_uv[..., 0], 1.0)
            v = np.mod(tex_uv[..., 1], 1.0)
            tx = np.clip((u * (tex_w - 1)).astype(int), 0, tex_w - 1)
            ty = np.clip(((1 - v) * (tex_h - 1)).astype(int), 0, tex_h - 1)
            color = texture[ty, tx].astype(np.float32)

            triangle = local[face]
            normal = np.cross(triangle[1] - triangle[0], triangle[2] - triangle[0])
            length = np.linalg.norm(normal)
            if length > 1e-9:
                normal /= length

            ndotl = abs(float(np.dot(normal, light_dir)))
            diffuse = 0.34 + 0.66 * ndotl
            shaded = color * diffuse * tint

            if orm is not None:
                orm_h, orm_w = orm.shape[:2]
                otx = np.clip((u * (orm_w - 1)).astype(int), 0, orm_w - 1)
                oty = np.clip(((1 - v) * (orm_h - 1)).astype(int), 0, orm_h - 1)
                pbr = orm[oty, otx].astype(np.float32) / 255.0
                ao = 0.78 + 0.22 * pbr[..., 0:1]
                roughness = pbr[..., 1:2]
                metallic = pbr[..., 2:3]
                shaded *= ao
            else:
                roughness = np.full((*mask.shape, 1), 0.58 if is_metal else 0.78, np.float32)
                metallic = np.full((*mask.shape, 1), 1.0 if is_metal else 0.0, np.float32)

            # Restrained stylized specular. The source ORM remains authority for roughness/metalness,
            # but the validation renderer keeps highlights broad enough to fit Diyse's painterly target.
            ndoth = abs(float(np.dot(normal, half_vector)))
            power = 6 + 42 * (1 - roughness)
            specular = np.power(ndoth, power) * (1 - roughness) * (0.12 + 0.88 * metallic)
            shaded += specular * (128 if is_metal else 34)

            shaded = np.clip(shaded, 0, 255)
            image_sub = image[ymin:ymax + 1, xmin:xmax + 1]
            image_sub[mask] = shaded[mask]
            zsub[mask] = zz[mask]

    output_image = Image.fromarray(image.astype(np.uint8), 'RGB')

    if author_emissive:
        anchor = _find_emitter_anchor(vertices_all, gltf.stem)
        if anchor is not None:
            world_anchor, radius = anchor
            local_anchor = world_anchor - center
            cx = float(local_anchor @ right * scale + size / 2)
            cy = float(-(local_anchor @ up) * scale + size * 0.54)
            render_radius = float(max(radius * scale, 5))

            # Soft halo first.
            halo = Image.new('RGBA', output_image.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(halo)
            for multiplier, alpha in [(1.4, 88), (2.3, 42), (3.4, 18)]:
                rr = render_radius * multiplier
                draw.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), fill=(255, 157, 63, alpha))
            halo = halo.filter(ImageFilter.GaussianBlur(float(max(render_radius * 0.65, 3))))
            output_image = Image.alpha_composite(output_image.convert('RGBA'), halo)

            # Unblurred authored light core so the fixture still reads as an actual emitter rather than
            # a vague warm screen-space haze.
            core = Image.new('RGBA', output_image.size, (0, 0, 0, 0))
            core_draw = ImageDraw.Draw(core)
            core_radius = render_radius * 0.42
            core_draw.ellipse(
                (cx - core_radius, cy - core_radius, cx + core_radius, cy + core_radius),
                fill=(255, 226, 151, 235),
            )
            output_image = Image.alpha_composite(output_image, core).convert('RGB')

    output.parent.mkdir(parents=True, exist_ok=True)
    output_image.save(output, 'PNG')


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('gltf', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--furniture', type=Path)
    parser.add_argument('--metal', type=Path)
    parser.add_argument('--lighting', choices=['neutral', 'warm', 'cool'], default='neutral')
    parser.add_argument('--author-emissive', action='store_true')
    args = parser.parse_args()

    materials = {}
    if args.furniture:
        materials['MI_Trim_Furniture'] = args.furniture
    if args.metal:
        materials['MI_Trim_Metal'] = args.metal
    render_gltf(
        args.gltf,
        args.output,
        materials,
        lighting=args.lighting,
        author_emissive=args.author_emissive,
    )
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
