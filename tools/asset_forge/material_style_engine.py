#!/usr/bin/env python3
"""Deterministic UV-safe material stylization for Diyse Asset Forge.

This backend is intentionally non-generative: it preserves every pixel coordinate and
serves as the zero-drift baseline for shared trim atlases before optional AI assistance.
"""
from __future__ import annotations

from pathlib import Path
from typing import Literal

import cv2
import numpy as np
from PIL import Image

MaterialKind = Literal['wood','metal','prop','cloth']


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

    # Props and Cloth preserve source hue families rather than collapsing a mixed trim sheet
    # into one color identity.
    hsv=cv2.cvtColor(np.clip(base,0,255).astype(np.uint8),cv2.COLOR_RGB2HSV).astype(np.float32)
    if kind=='prop':
        hsv[:,:,1]*=0.86
        hsv[:,:,2]=np.clip(hsv[:,:,2]*0.98,0,255)
    else:
        hsv[:,:,1]*=0.88
    return cv2.cvtColor(np.clip(hsv,0,255).astype(np.uint8),cv2.COLOR_HSV2RGB).astype(np.float32)


def stylize_material_image(image: Image.Image, kind: MaterialKind) -> Image.Image:
    source=np.array(image.convert('RGB'),dtype=np.uint8)
    sigma=26 if kind in {'wood','cloth'} else 20
    smoothed=cv2.bilateralFilter(source,d=0,sigmaColor=sigma,sigmaSpace=6)
    lab=cv2.cvtColor(smoothed,cv2.COLOR_RGB2LAB)
    lightness=lab[:,:,0].astype(np.float32)/255.0
    levels={'wood':5,'metal':6,'prop':6,'cloth':5}[kind]
    bands=np.round(lightness*levels)/levels
    blend={'wood':0.62,'metal':0.68,'prop':0.52,'cloth':0.46}[kind]
    lab[:,:,0]=(np.clip(blend*bands+(1-blend)*lightness,0,1)*255).astype(np.uint8)
    base=cv2.cvtColor(lab,cv2.COLOR_LAB2RGB).astype(np.float32)
    base=_palette_map(base,source,kind)
    gray=cv2.cvtColor(smoothed,cv2.COLOR_RGB2GRAY)

    if kind in {'wood','metal','prop'}:
        magnitude=np.abs(cv2.Laplacian(gray,cv2.CV_32F,ksize=3))
        percentile={'wood':96.5,'metal':94.0,'prop':97.0}[kind]
        threshold=max(float(np.percentile(magnitude,percentile)),5.0)
        edge=(magnitude>threshold).astype(np.uint8)*255
        edge=_component_mask(edge,min_area={'wood':14,'metal':8,'prop':12}[kind])
        edge=cv2.dilate(edge,np.ones((2,2),np.uint8),iterations=1).astype(np.float32)/255.0
        ink=edge[...,None]
        ink_color=np.array({'wood':[43,30,24.],'metal':[22,25,28.],'prop':[45,39,38.]}[kind],np.float32)
        strength={'wood':0.34,'metal':0.56,'prop':0.25}[kind]
        base=base*(1-strength*ink)+ink_color*(strength*ink)
    else:
        # Cloth receives broad fold modulation rather than contour/edge ink.
        low=cv2.GaussianBlur(gray,(0,0),18).astype(np.float32)
        mid=cv2.GaussianBlur(gray,(0,0),5).astype(np.float32)
        fold=np.clip((mid-low)/255.0,-0.10,0.10)[...,None]
        base=np.clip(base+fold*45,0,255)

    low=cv2.GaussianBlur(gray,(0,0),12 if kind!='cloth' else 16).astype(np.float32)
    residual=(gray.astype(np.float32)-low)/255.0
    amplitude={'wood':7,'metal':9,'prop':6,'cloth':4}[kind]
    base=np.clip(base+residual[...,None]*amplitude,0,255).astype(np.uint8)
    return Image.fromarray(base,'RGB')


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
    parser.add_argument('--kind',choices=['wood','metal','prop','cloth'],required=True)
    args=parser.parse_args()
    stylize_material_file(args.source,args.output,args.kind)
    return 0

if __name__=='__main__':
    raise SystemExit(main())
