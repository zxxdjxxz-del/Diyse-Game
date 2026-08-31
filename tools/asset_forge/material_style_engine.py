#!/usr/bin/env python3
"""Deterministic UV-safe material stylization for Diyse Asset Forge.

This backend is intentionally non-generative: it preserves every pixel coordinate and
is suitable as a zero-drift baseline for shared trim atlases before optional AI edits.
"""
from __future__ import annotations

from pathlib import Path
from typing import Literal

import cv2
import numpy as np
from PIL import Image

MaterialKind = Literal['wood','metal']


def _palette_map(base: np.ndarray, source: np.ndarray, kind: MaterialKind) -> np.ndarray:
    lum=(0.2126*base[:,:,0]+0.7152*base[:,:,1]+0.0722*base[:,:,2])/255.0
    t=np.clip(lum,0,1)[...,None]
    if kind=='wood':
        dark=np.array([62,39,27.],np.float32)
        mid=np.array([125,76,43.],np.float32)
        light=np.array([182,126,71.],np.float32)
        pal=np.where(t<0.55,dark+(mid-dark)*(t/0.55),mid+(light-mid)*((t-0.55)/0.45))
        return 0.45*base+0.55*pal
    dark=np.array([35,39,42.],np.float32)
    mid=np.array([79,85,89.],np.float32)
    light=np.array([155,159,157.],np.float32)
    pal=np.where(t<0.60,dark+(mid-dark)*(t/0.60),mid+(light-mid)*((t-0.60)/0.40))
    warmth=np.clip((source[:,:,0].astype(np.float32)-source[:,:,2].astype(np.float32)-8)/55,0,1)[...,None]
    rust=np.array([116,65,42.],np.float32)
    pal=pal*(1-0.32*warmth)+rust*(0.32*warmth)
    return 0.35*base+0.65*pal


def stylize_material_image(image: Image.Image, kind: MaterialKind) -> Image.Image:
    source=np.array(image.convert('RGB'),dtype=np.uint8)
    sm=cv2.bilateralFilter(source,d=0,sigmaColor=24 if kind=='wood' else 18,sigmaSpace=5)
    lab=cv2.cvtColor(sm,cv2.COLOR_RGB2LAB)
    L=lab[:,:,0].astype(np.float32)/255.0
    bands=np.round(L*5)/5
    lab[:,:,0]=(np.clip(0.70*bands+0.30*L,0,1)*255).astype(np.uint8)
    base=cv2.cvtColor(lab,cv2.COLOR_LAB2RGB).astype(np.float32)
    base=_palette_map(base,source,kind)

    gray=cv2.cvtColor(sm,cv2.COLOR_RGB2GRAY)
    mag=np.abs(cv2.Laplacian(gray,cv2.CV_32F,ksize=3))
    edge_threshold=max(float(np.percentile(mag,88 if kind=='wood' else 90)),4.0)
    strong_threshold=max(float(np.percentile(mag,96)),edge_threshold)
    edge=(mag>edge_threshold).astype(np.uint8)*255
    edge=cv2.morphologyEx(edge,cv2.MORPH_CLOSE,np.ones((2,2),np.uint8))
    strong=(mag>strong_threshold).astype(np.uint8)*255
    edge1=cv2.dilate(edge,np.ones((2,2),np.uint8),iterations=1).astype(np.float32)/255
    edge2=cv2.dilate(strong,np.ones((3,3),np.uint8),iterations=1).astype(np.float32)/255
    ink=np.clip(0.55*edge1+0.45*edge2,0,1)[...,None]
    ink_color=np.array([39,27,22.] if kind=='wood' else [24,27,29.],np.float32)
    strength=0.55 if kind=='wood' else 0.70
    base=base*(1-strength*ink)+ink_color*(strength*ink)

    low=cv2.GaussianBlur(gray,(0,0),10).astype(np.float32)
    residual=(gray.astype(np.float32)-low)/255.0
    base=np.clip(base+residual[...,None]*12,0,255).astype(np.uint8)
    return Image.fromarray(base,'RGB')


def stylize_material_file(source: Path, output: Path, kind: MaterialKind) -> None:
    with Image.open(source) as im:
        styled=stylize_material_image(im,kind)
    output.parent.mkdir(parents=True,exist_ok=True)
    styled.save(output,format='PNG')


def main() -> int:
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument('source',type=Path)
    p.add_argument('output',type=Path)
    p.add_argument('--kind',choices=['wood','metal'],required=True)
    a=p.parse_args()
    stylize_material_file(a.source,a.output,a.kind)
    return 0

if __name__=='__main__':
    raise SystemExit(main())
