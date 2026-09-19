#!/usr/bin/env python3
"""Deterministic UV-safe material stylization for Diyse Asset Forge.

This backend is intentionally non-generative: it preserves pixel registration and
serves as the zero-drift baseline for shared materials and texture-family validation.
The active texture-facing style parameters live in ``texture_style_contract_v1.json``.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Literal

import cv2
import numpy as np
from PIL import Image

MaterialKind = Literal['wood','metal','prop','cloth','stone','foliage','grass']
CONTRACT_PATH = Path(__file__).with_name('texture_style_contract_v1.json')


def _load_contract() -> dict:
    return json.loads(CONTRACT_PATH.read_text(encoding='utf-8'))


STYLE_CONTRACT = _load_contract()


def material_profile(kind: MaterialKind) -> dict:
    return dict(STYLE_CONTRACT.get('material_profiles', {}).get(kind, {}))


def _component_mask(mask: np.ndarray, min_area: int) -> np.ndarray:
    count, labels, stats, _ = cv2.connectedComponentsWithStats(mask.astype(np.uint8), 8)
    output=np.zeros_like(mask,dtype=np.uint8)
    for index in range(1,count):
        if stats[index,cv2.CC_STAT_AREA] >= min_area:
            output[labels==index]=255
    return output


def _palette_map(base: np.ndarray, source: np.ndarray, kind: MaterialKind) -> np.ndarray:
    lum=(0.2126*base[:,:,0]+0.7152*base[:,:,1]+0.0722*base[:,:,2])/255.0
    t=np.clip(lum,0,1)[...,None]
    if kind=='wood':
        dark=np.array([64,41,29.],np.float32)
        mid=np.array([126,80,47.],np.float32)
        light=np.array([184,132,79.],np.float32)
        palette=np.where(t<0.55,dark+(mid-dark)*(t/0.55),mid+(light-mid)*((t-0.55)/0.45))
        return 0.52*base+0.48*palette
    if kind=='metal':
        dark=np.array([34,38,42.],np.float32)
        mid=np.array([82,89,94.],np.float32)
        light=np.array([170,174,171.],np.float32)
        palette=np.where(t<0.60,dark+(mid-dark)*(t/0.60),mid+(light-mid)*((t-0.60)/0.40))
        warmth=np.clip((source[:,:,0].astype(np.float32)-source[:,:,2].astype(np.float32)-8)/55,0,1)[...,None]
        rust=np.array([116,67,44.],np.float32)
        return (0.32*base+0.68*palette)*(1-0.18*warmth)+rust*(0.18*warmth)

    # Mixed, cloth, stone, and vegetation families preserve their source hue identity.
    hsv=cv2.cvtColor(np.clip(base,0,255).astype(np.uint8),cv2.COLOR_RGB2HSV).astype(np.float32)
    if kind=='prop':
        hsv[:,:,1]*=0.86
        hsv[:,:,2]=np.clip(hsv[:,:,2]*0.98,0,255)
    elif kind=='cloth':
        hsv[:,:,1]*=0.88
    elif kind in {'stone','foliage','grass'}:
        profile=material_profile(kind)
        hsv[:,:,1]*=float(profile.get('saturation_scale',1.0))
        if kind=='stone':
            hsv[:,:,2]=np.clip(hsv[:,:,2]*0.98,0,255)
        else:
            hsv[:,:,2]=np.clip(hsv[:,:,2]*0.99,0,255)
    return cv2.cvtColor(np.clip(hsv,0,255).astype(np.uint8),cv2.COLOR_HSV2RGB).astype(np.float32)


def _edge_parameters(kind: MaterialKind) -> tuple[float,int,float,np.ndarray]:
    defaults={
        'wood':(96.5,14,0.34,[43,30,24.]),
        'metal':(94.0,8,0.56,[22,25,28.]),
        'prop':(97.0,12,0.25,[45,39,38.]),
    }
    if kind in defaults:
        percentile,min_area,strength,color=defaults[kind]
        return percentile,min_area,strength,np.array(color,np.float32)
    profile=material_profile(kind)
    color={
        'stone':[38,36,34.],
        'foliage':[25,43,29.],
        'grass':[29,47,27.],
    }[kind]
    return (
        float(profile.get('edge_percentile',98.0)),
        int(profile.get('edge_min_area',12)),
        float(profile.get('edge_strength',0.18)),
        np.array(color,np.float32),
    )


def stylize_material_image(image: Image.Image, kind: MaterialKind) -> Image.Image:
    if kind not in {'wood','metal','prop','cloth','stone','foliage','grass'}:
        raise ValueError(f'Unsupported material kind: {kind}')

    has_alpha='A' in image.getbands() or ('transparency' in image.info)
    alpha=image.convert('RGBA').getchannel('A').copy() if has_alpha else None
    alpha_np=np.array(alpha,dtype=np.uint8) if alpha is not None else None

    source=np.array(image.convert('RGB'),dtype=np.uint8)
    sigma={
        'wood':26,'metal':20,'prop':20,'cloth':26,
        'stone':24,'foliage':30,'grass':28,
    }[kind]
    smoothed=cv2.bilateralFilter(source,d=0,sigmaColor=sigma,sigmaSpace=6)
    lab=cv2.cvtColor(smoothed,cv2.COLOR_RGB2LAB)
    lightness=lab[:,:,0].astype(np.float32)/255.0

    if kind in {'stone','foliage','grass'}:
        profile=material_profile(kind)
        levels=int(profile.get('value_levels',5))
        blend=float(profile.get('value_blend',0.55))
    else:
        levels={'wood':5,'metal':6,'prop':6,'cloth':5}[kind]
        blend={'wood':0.62,'metal':0.68,'prop':0.52,'cloth':0.46}[kind]

    bands=np.round(lightness*levels)/levels
    lab[:,:,0]=(np.clip(blend*bands+(1-blend)*lightness,0,1)*255).astype(np.uint8)
    base=cv2.cvtColor(lab,cv2.COLOR_LAB2RGB).astype(np.float32)
    base=_palette_map(base,source,kind)
    gray=cv2.cvtColor(smoothed,cv2.COLOR_RGB2GRAY)

    if kind in {'wood','metal','prop','stone','foliage','grass'}:
        magnitude=np.abs(cv2.Laplacian(gray,cv2.CV_32F,ksize=3))
        percentile,min_area,strength,ink_color=_edge_parameters(kind)
        threshold=max(float(np.percentile(magnitude,percentile)),5.0)
        edge=(magnitude>threshold).astype(np.uint8)*255

        # Transparent vegetation must not acquire a universal dark silhouette outline.
        if kind in {'foliage','grass'} and alpha_np is not None:
            interior=(alpha_np>32).astype(np.uint8)*255
            interior=cv2.erode(interior,np.ones((3,3),np.uint8),iterations=1)
            edge=cv2.bitwise_and(edge,interior)

        edge=_component_mask(edge,min_area=min_area)
        edge=cv2.dilate(edge,np.ones((2,2),np.uint8),iterations=1).astype(np.float32)/255.0
        ink=edge[...,None]
        base=base*(1-strength*ink)+ink_color*(strength*ink)
    else:
        # Cloth receives broad fold modulation rather than contour/edge ink.
        low=cv2.GaussianBlur(gray,(0,0),18).astype(np.float32)
        mid=cv2.GaussianBlur(gray,(0,0),5).astype(np.float32)
        fold=np.clip((mid-low)/255.0,-0.10,0.10)[...,None]
        base=np.clip(base+fold*45,0,255)

    # Vegetation receives a low-amplitude cluster-mass modulation rather than leaf-by-leaf detail.
    if kind in {'foliage','grass'}:
        low_mass=cv2.GaussianBlur(gray,(0,0),12 if kind=='foliage' else 9).astype(np.float32)
        mass=np.clip((gray.astype(np.float32)-low_mass)/255.0,-0.08,0.08)[...,None]
        base=np.clip(base+mass*(22 if kind=='foliage' else 16),0,255)

    low=cv2.GaussianBlur(gray,(0,0),12 if kind not in {'cloth','foliage','grass'} else (16 if kind=='cloth' else 14)).astype(np.float32)
    residual=(gray.astype(np.float32)-low)/255.0
    if kind in {'stone','foliage','grass'}:
        amplitude=float(material_profile(kind).get('residual_amplitude',3))
    else:
        amplitude={'wood':7,'metal':9,'prop':6,'cloth':4}[kind]
    base=np.clip(base+residual[...,None]*amplitude,0,255).astype(np.uint8)

    result=Image.fromarray(base,'RGB')
    if alpha is not None:
        result.putalpha(alpha)
    return result


def stylize_material_file(source: Path, output: Path, kind: MaterialKind) -> None:
    with Image.open(source) as image:
        styled=stylize_material_image(image,kind)
    output.parent.mkdir(parents=True,exist_ok=True)
    styled.save(output,format='PNG')


def main() -> int:
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('source',type=Path)
    parser.add_argument('output',type=Path)
    parser.add_argument('--kind',choices=['wood','metal','prop','cloth','stone','foliage','grass'],required=True)
    args=parser.parse_args()
    stylize_material_file(args.source,args.output,args.kind)
    return 0

if __name__=='__main__':
    raise SystemExit(main())
