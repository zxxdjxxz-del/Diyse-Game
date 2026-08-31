#!/usr/bin/env python3
"""Shared-material analysis for Diyse Asset Forge.

Detect shared BaseColor/Normal/ORM trim sheets across glTF assets so one material pass
can update many props. Material-family routing is resolved from actual glTF texture
bindings rather than material-name guesses.
"""
from __future__ import annotations

import json
import zipfile
from collections import defaultdict
from pathlib import Path
from typing import Iterable


def gltf_image_dependencies(gltf_json: dict) -> list[str]:
    return [img.get('uri','') for img in gltf_json.get('images',[]) if img.get('uri')]


def basecolor_dependencies(gltf_json: dict) -> list[str]:
    return [x for x in gltf_image_dependencies(gltf_json) if 'basecolor' in x.lower()]


def material_basecolor_dependencies(gltf_json: dict) -> dict[str,str]:
    """Resolve material name -> BaseColor image URI from glTF indices."""
    images=gltf_json.get('images',[])
    textures=gltf_json.get('textures',[])
    out: dict[str,str]={}
    for index,material in enumerate(gltf_json.get('materials',[])):
        name=material.get('name') or f'material_{index}'
        pbr=material.get('pbrMetallicRoughness',{})
        tex_info=pbr.get('baseColorTexture')
        if not tex_info:
            continue
        tex_index=tex_info.get('index')
        if tex_index is None or not (0 <= tex_index < len(textures)):
            continue
        source_index=textures[tex_index].get('source')
        if source_index is None or not (0 <= source_index < len(images)):
            continue
        uri=images[source_index].get('uri','')
        if uri:
            out[name]=uri
    return out


def discover_gltf_models(zip_path: Path, gltf_root: str='Exports/glTF') -> list[str]:
    prefix=gltf_root.rstrip('/')+'/'
    with zipfile.ZipFile(zip_path) as zf:
        return sorted(Path(n).stem for n in zf.namelist() if n.startswith(prefix) and n.endswith('.gltf'))


def analyze_zip_models(zip_path: Path, model_names: Iterable[str], gltf_root: str='Exports/glTF') -> dict:
    per_model: dict[str,dict]={}
    reverse: dict[str,list[str]]=defaultdict(list)
    with zipfile.ZipFile(zip_path) as zf:
        for model in model_names:
            member=f'{gltf_root}/{model}.gltf'
            data=json.loads(zf.read(member))
            all_images=gltf_image_dependencies(data)
            basecolors=basecolor_dependencies(data)
            materials=[m.get('name','') for m in data.get('materials',[])]
            material_basecolors=material_basecolor_dependencies(data)
            buffers=[b.get('uri','') for b in data.get('buffers',[]) if b.get('uri')]
            per_model[model]={
                'member':member,
                'materials':materials,
                'material_basecolors':material_basecolors,
                'buffers':buffers,
                'images':all_images,
                'basecolor_images':basecolors,
            }
            for image in basecolors:
                reverse[image].append(model)
    return {
        'models':per_model,
        'unique_basecolor_images':sorted(reverse),
        'basecolor_usage':{k:sorted(v) for k,v in sorted(reverse.items())},
        'basecolor_generation_calls':len(reverse),
    }


def analyze_all_zip_models(zip_path: Path, gltf_root: str='Exports/glTF') -> dict:
    models=discover_gltf_models(zip_path,gltf_root=gltf_root)
    analysis=analyze_zip_models(zip_path,models,gltf_root=gltf_root)
    analysis['model_count']=len(models)
    analysis['basecolor_usage_counts']={k:len(v) for k,v in analysis['basecolor_usage'].items()}
    return analysis


def extract_shared_material_files(zip_path: Path, analysis: dict, output_dir: Path, gltf_root: str='Exports/glTF') -> list[Path]:
    output_dir.mkdir(parents=True,exist_ok=True)
    written=[]
    with zipfile.ZipFile(zip_path) as zf:
        for image in analysis['unique_basecolor_images']:
            member=f'{gltf_root}/{image}'
            dest=output_dir/image
            dest.write_bytes(zf.read(member)); written.append(dest)
    return written


def main() -> int:
    import argparse
    p=argparse.ArgumentParser(prog='diyse-shared-materials')
    p.add_argument('zip_path',type=Path)
    p.add_argument('--models',nargs='*')
    p.add_argument('--all-models',action='store_true')
    p.add_argument('--extract',type=Path)
    a=p.parse_args()
    if a.all_models or not a.models:
        result=analyze_all_zip_models(a.zip_path)
    else:
        result=analyze_zip_models(a.zip_path,a.models)
    if a.extract:
        extract_shared_material_files(a.zip_path,result,a.extract)
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0

if __name__=='__main__': raise SystemExit(main())
