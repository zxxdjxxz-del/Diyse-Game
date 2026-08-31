#!/usr/bin/env python3
"""One-command shared-material prop-pack pilot for Diyse Asset Forge.

v2 material-pilot flow:
- discover shared glTF material dependencies;
- extract only the required model/buffer/texture files;
- create UV-safe deterministic BaseColor style candidates;
- run PBR QA and attenuate flagged normal maps without changing UV registration;
- derive exportable model-space emissive anchors for lantern-style props;
- render actual glTF models under neutral/warm/cool validation lighting;
- build a deterministic review sheet from those real model renders;
- build a gameplay-scale integration preview using the real glTF extents.
"""
from __future__ import annotations

import json
import zipfile
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont

try:
    from .shared_material_engine import analyze_zip_models
    from .material_style_engine import stylize_material_file
    from .model_render_engine import render_gltf
    from .pbr_qa_engine import analyze_pbr
    from .normal_rebalance_engine import rebalance_normal_file
    from .emissive_anchor_engine import derive_emissive_anchor
    from .gameplay_preview_engine import compose_preview
except ImportError:
    from shared_material_engine import analyze_zip_models
    from material_style_engine import stylize_material_file
    from model_render_engine import render_gltf
    from pbr_qa_engine import analyze_pbr
    from normal_rebalance_engine import rebalance_normal_file
    from emissive_anchor_engine import derive_emissive_anchor
    from gameplay_preview_engine import compose_preview


def _extract_selected(
    zip_path: Path,
    models: Iterable[str],
    analysis: dict,
    root: Path,
    gltf_root: str = 'Exports/glTF',
) -> Path:
    source = root / 'source'
    source.mkdir(parents=True, exist_ok=True)
    required = set()
    for model in models:
        required.add(f'{gltf_root}/{model}.gltf')
        for buffer_uri in analysis['models'][model].get('buffers', []):
            required.add(f'{gltf_root}/{buffer_uri}')
        for image in analysis['models'][model]['images']:
            required.add(f'{gltf_root}/{image}')

    with zipfile.ZipFile(zip_path) as archive:
        names = set(archive.namelist())
        for member in sorted(required):
            if member not in names:
                raise KeyError(f'Missing required ZIP member: {member}')
            destination = source / Path(member).name
            destination.write_bytes(archive.read(member))
    return source


def _material_kind(filename: str) -> str | None:
    name = filename.lower()
    if 'furniture_basecolor' in name:
        return 'wood'
    if 'metal_basecolor' in name:
        return 'metal'
    return None


def _material_family_from_basecolor(filename: str) -> str | None:
    name = filename.lower()
    if 'furniture_basecolor' in name:
        return 'furniture'
    if 'metal_basecolor' in name:
        return 'metal'
    return None


def _family_for_material(material_name: str) -> str | None:
    name = material_name.lower()
    if 'furniture' in name:
        return 'furniture'
    if 'metal' in name:
        return 'metal'
    return None


def _build_sheet(entries: list[dict], output: Path, thumb: int = 320, columns: int = 4) -> None:
    pad = 18
    label_h = 58
    header = 62
    rows = (len(entries) + columns - 1) // columns
    cell_w = thumb + pad * 2
    cell_h = thumb + label_h + pad * 2
    sheet = Image.new('RGB', (columns * cell_w, header + rows * cell_h), (22, 22, 24))
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    draw.text((18, 16), 'DIYSE ASSET FORGE - REAL PROP PACK REVIEW', fill=(238, 228, 205), font=font)
    draw.text(
        (18, 36),
        f'Renders: {len(entries)} | actual glTF + shared trims + deterministic labels',
        fill=(180, 180, 180),
        font=font,
    )

    for index, entry in enumerate(entries):
        column = index % columns
        row = index // columns
        x = column * cell_w
        y = header + row * cell_h
        draw.rectangle((x + 5, y + 5, x + cell_w - 5, y + cell_h - 5), outline=(72, 72, 76))
        with Image.open(entry['path']).convert('RGB') as image:
            image.thumbnail((thumb, thumb), Image.Resampling.LANCZOS)
            px = x + pad + (thumb - image.width) // 2
            py = y + pad + (thumb - image.height) // 2
            sheet.paste(image, (px, py))
        draw.text(
            (x + pad, y + pad + thumb + 7),
            f"{entry['model']} - {entry['lighting']}",
            fill=(238, 228, 205),
            font=font,
        )
        draw.text(
            (x + pad, y + pad + thumb + 25),
            entry.get('note', 'real glTF + styled shared trims'),
            fill=(170, 170, 170),
            font=font,
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, 'PNG')


def run_prop_pack(
    zip_path: Path,
    models: list[str],
    output_root: Path,
    lighting_states: tuple[str, ...] = ('neutral', 'warm', 'cool'),
) -> dict:
    output_root.mkdir(parents=True, exist_ok=True)
    analysis = analyze_zip_models(zip_path, models)
    source = _extract_selected(zip_path, models, analysis, output_root)
    styled_dir = output_root / 'styled_materials'
    styled_dir.mkdir(exist_ok=True)
    renders_dir = output_root / 'renders'
    renders_dir.mkdir(exist_ok=True)

    styled_families: dict[str, Path] = {}
    styled_normals: dict[str, Path] = {}
    pbr: dict[str, dict] = {}

    for basecolor in analysis['unique_basecolor_images']:
        kind = _material_kind(basecolor)
        family = _material_family_from_basecolor(basecolor)
        if not kind or not family:
            continue

        source_basecolor = source / basecolor
        styled_basecolor = styled_dir / f'Diyse_{basecolor}'
        stylize_material_file(source_basecolor, styled_basecolor, kind)
        styled_families[family] = styled_basecolor

        prefix = basecolor.replace('_BaseColor.png', '')
        normal = source / f'{prefix}_Normal.png'
        orm = source / f'{prefix}_ORM.png'
        if normal.exists() and orm.exists():
            report = analyze_pbr(normal, orm)
            pbr[family] = {'source': report}

            # Only change normals when QA explicitly flags them. Furniture is intentionally
            # attenuated more strongly than metal so carved trim does not become noisy relief.
            if 'strong_normal_review' in report.get('review_flags', []):
                strength = 0.72 if family == 'furniture' else 0.84
                styled_normal = styled_dir / f'Diyse_{prefix}_Normal.png'
                rebalance_normal_file(normal, styled_normal, strength=strength)
                styled_normals[family] = styled_normal
                pbr[family]['normal_rebalance_strength'] = strength
                pbr[family]['rebalanced'] = analyze_pbr(styled_normal, orm)

    render_entries = []
    emissive_anchors: dict[str, dict] = {}

    for model in models:
        gltf = source / f'{model}.gltf'
        textures = {}
        for material_name in analysis['models'][model]['materials']:
            family = _family_for_material(material_name)
            if family in styled_families:
                textures[material_name] = styled_families[family]

        anchor = derive_emissive_anchor(gltf)
        if anchor is not None:
            emissive_anchors[model] = anchor

        for lighting in lighting_states:
            output = renders_dir / f'{model}__{lighting}.png'
            render_gltf(
                gltf,
                output,
                textures,
                lighting=lighting,
                author_emissive=anchor is not None,
            )
            render_entries.append({
                'model': model,
                'lighting': lighting,
                'path': str(output.resolve()),
                'note': 'real glTF + shared trim v2',
            })

    sheet = output_root / 'review_sheet.png'
    _build_sheet(render_entries, sheet)

    neutral_renders = {
        model: renders_dir / f'{model}__neutral.png'
        for model in models
        if (renders_dir / f'{model}__neutral.png').exists()
    }
    gltfs = {model: source / f'{model}.gltf' for model in models}
    gameplay_preview = output_root / 'gameplay_scale_preview.png'
    compose_preview(gltfs, neutral_renders, gameplay_preview)

    manifest = {
        'source_zip': str(zip_path.resolve()),
        'models': models,
        'basecolor_usage': analysis['basecolor_usage'],
        'styled_materials': {key: str(value.resolve()) for key, value in styled_families.items()},
        'styled_normals': {key: str(value.resolve()) for key, value in styled_normals.items()},
        'pbr_qa': pbr,
        'emissive_anchors': emissive_anchors,
        'renders': render_entries,
        'review_sheet': str(sheet.resolve()),
        'gameplay_scale_preview': str(gameplay_preview.resolve()),
        'image_generation_calls': 0,
        'status': 'technical_pilot_v2_ready_for_visual_review',
    }
    (output_root / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    return manifest


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(prog='diyse-prop-pack-pilot')
    parser.add_argument('zip_path', type=Path)
    parser.add_argument('--models', nargs='+', required=True)
    parser.add_argument('--output-root', type=Path, default=Path('.asset_forge/prop_pack_pilot'))
    parser.add_argument('--lighting', nargs='+', choices=['neutral', 'warm', 'cool'], default=['neutral', 'warm', 'cool'])
    args = parser.parse_args()

    result = run_prop_pack(args.zip_path, args.models, args.output_root, tuple(args.lighting))
    print(json.dumps({
        'models': len(result['models']),
        'styled_materials': len(result['styled_materials']),
        'styled_normals': len(result['styled_normals']),
        'emissive_anchors': len(result['emissive_anchors']),
        'renders': len(result['renders']),
        'image_generation_calls': result['image_generation_calls'],
        'review_sheet': result['review_sheet'],
        'gameplay_scale_preview': result['gameplay_scale_preview'],
    }, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
