#!/usr/bin/env python3
"""One-command shared-material prop-pack pilot for Diyse Asset Forge."""
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
except ImportError:
    from shared_material_engine import analyze_zip_models
    from material_style_engine import stylize_material_file
    from model_render_engine import render_gltf
    from pbr_qa_engine import analyze_pbr


def _extract_selected(zip_path: Path, models: Iterable[str], analysis: dict, root: Path,
                      gltf_root: str='Exports/glTF') -> Path:
    src=root/'source'; src.mkdir(parents=True,exist_ok=True)
    required=set()
    for model in models:
        required.add(f'{gltf_root}/{model}.gltf')
        for buffer_uri in analysis['models'][model].get('buffers',[]):
            required.add(f'{gltf_root}/{buffer_uri}')
        for image in analysis['models'][model]['images']:
            required.add(f'{gltf_root}/{image}')
    with zipfile.ZipFile(zip_path) as zf:
        names=set(zf.namelist())
        for member in sorted(required):
            if member not in names:
                raise KeyError(f'Missing required ZIP member: {member}')
            dest=src/Path(member).name
            dest.write_bytes(zf.read(member))
    return src


def _material_kind(filename: str) -> str | None:
    n=filename.lower()
    if 'furniture_basecolor' in n: return 'wood'
    if 'metal_basecolor' in n: return 'metal'
    return None


def _material_family_from_basecolor(filename: str) -> str | None:
    n=filename.lower()
    if 'furniture_basecolor' in n: return 'furniture'
    if 'metal_basecolor' in n: return 'metal'
    return None


def _family_for_material(material_name: str) -> str | None:
    n=material_name.lower()
    if 'furniture' in n: return 'furniture'
    if 'metal' in n: return 'metal'
    return None


def _build_sheet(entries: list[dict], output: Path, thumb: int=320, columns: int=4) -> None:
    pad=18; label_h=58; header=62
    rows=(len(entries)+columns-1)//columns
    cell_w=thumb+pad*2; cell_h=thumb+label_h+pad*2
    sheet=Image.new('RGB',(columns*cell_w,header+rows*cell_h),(22,22,24))
    draw=ImageDraw.Draw(sheet); font=ImageFont.load_default()
    draw.text((18,16),'DIYSE ASSET FORGE - REAL PROP PACK REVIEW',fill=(238,228,205),font=font)
    draw.text((18,36),f'Renders: {len(entries)} | deterministic labels and actual glTF outputs',fill=(180,180,180),font=font)
    for i,e in enumerate(entries):
        c=i%columns; r=i//columns; x=c*cell_w; y=header+r*cell_h
        draw.rectangle((x+5,y+5,x+cell_w-5,y+cell_h-5),outline=(72,72,76))
        with Image.open(e['path']).convert('RGB') as im:
            im.thumbnail((thumb,thumb),Image.Resampling.LANCZOS)
            px=x+pad+(thumb-im.width)//2; py=y+pad+(thumb-im.height)//2
            sheet.paste(im,(px,py))
        draw.text((x+pad,y+pad+thumb+7),f"{e['model']} - {e['lighting']}",fill=(238,228,205),font=font)
        draw.text((x+pad,y+pad+thumb+25),e.get('note','real glTF + styled shared trims'),fill=(170,170,170),font=font)
    output.parent.mkdir(parents=True,exist_ok=True); sheet.save(output,'PNG')


def run_prop_pack(zip_path: Path, models: list[str], output_root: Path,
                  lighting_states: tuple[str,...]=('neutral','warm','cool')) -> dict:
    output_root.mkdir(parents=True,exist_ok=True)
    analysis=analyze_zip_models(zip_path,models)
    source=_extract_selected(zip_path,models,analysis,output_root)
    styled_dir=output_root/'styled_materials'; styled_dir.mkdir(exist_ok=True)
    renders_dir=output_root/'renders'; renders_dir.mkdir(exist_ok=True)

    styled_families={}
    pbr={}
    for basecolor in analysis['unique_basecolor_images']:
        kind=_material_kind(basecolor)
        family=_material_family_from_basecolor(basecolor)
        if not kind or not family:
            continue
        src=source/basecolor; dest=styled_dir/f'Diyse_{basecolor}'
        stylize_material_file(src,dest,kind)
        styled_families[family]=dest
        prefix=basecolor.replace('_BaseColor.png','')
        normal=source/f'{prefix}_Normal.png'; orm=source/f'{prefix}_ORM.png'
        if normal.exists() and orm.exists():
            pbr[family]=analyze_pbr(normal,orm)

    render_entries=[]
    for model in models:
        gltf=source/f'{model}.gltf'
        textures={}
        for material_name in analysis['models'][model]['materials']:
            family=_family_for_material(material_name)
            if family in styled_families:
                textures[material_name]=styled_families[family]
        for lighting in lighting_states:
            out=renders_dir/f'{model}__{lighting}.png'
            render_gltf(gltf,out,textures,lighting=lighting,
                        emissive_hint=('lantern' in model.lower() and lighting=='warm'))
            render_entries.append({'model':model,'lighting':lighting,'path':str(out.resolve())})

    sheet=output_root/'review_sheet.png'; _build_sheet(render_entries,sheet)
    manifest={
        'source_zip':str(zip_path.resolve()),
        'models':models,
        'basecolor_usage':analysis['basecolor_usage'],
        'styled_materials':{k:str(v.resolve()) for k,v in styled_families.items()},
        'pbr_qa':pbr,
        'renders':render_entries,
        'review_sheet':str(sheet.resolve()),
        'image_generation_calls':0,
        'status':'technical_pilot_ready_for_visual_review',
    }
    (output_root/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    return manifest


def main() -> int:
    import argparse
    p=argparse.ArgumentParser(prog='diyse-prop-pack-pilot')
    p.add_argument('zip_path',type=Path)
    p.add_argument('--models',nargs='+',required=True)
    p.add_argument('--output-root',type=Path,default=Path('.asset_forge/prop_pack_pilot'))
    p.add_argument('--lighting',nargs='+',choices=['neutral','warm','cool'],default=['neutral','warm','cool'])
    a=p.parse_args()
    result=run_prop_pack(a.zip_path,a.models,a.output_root,tuple(a.lighting))
    print(json.dumps({
        'models':len(result['models']),
        'styled_materials':len(result['styled_materials']),
        'renders':len(result['renders']),
        'image_generation_calls':result['image_generation_calls'],
        'review_sheet':result['review_sheet'],
    },indent=2))
    return 0

if __name__=='__main__': raise SystemExit(main())
