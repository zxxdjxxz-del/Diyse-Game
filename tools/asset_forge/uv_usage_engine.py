#!/usr/bin/env python3
"""UV occupancy analysis for Diyse Asset Forge shared-material workflows.

Rasterizes actual model UV triangles into a texture-space mask, including wrapped UVs,
so material edits can be scoped to regions sampled by selected models without changing UVs.
"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

import numpy as np
import trimesh
from PIL import Image, ImageDraw, ImageFilter


def _shifted_triangle_copies(tri: np.ndarray):
    minv=tri.min(axis=0); maxv=tri.max(axis=0)
    sx0=int(np.floor(minv[0]-1)); sx1=int(np.ceil(maxv[0]))
    sy0=int(np.floor(minv[1]-1)); sy1=int(np.ceil(maxv[1]))
    for sx in range(sx0,sx1+1):
        for sy in range(sy0,sy1+1):
            shifted=tri-np.array([sx,sy],dtype=np.float64)
            mn=shifted.min(axis=0); mx=shifted.max(axis=0)
            if mx[0] < 0 or mn[0] > 1 or mx[1] < 0 or mn[1] > 1:
                continue
            yield shifted


def rasterize_uv_usage(gltf_paths: Iterable[Path], material_name: str, size: int=512,
                       dilation: int=2) -> Image.Image:
    mask=Image.new('L',(size,size),0)
    draw=ImageDraw.Draw(mask)
    for gltf in gltf_paths:
        scene=trimesh.load(Path(gltf),force='scene',process=False)
        for geometry in scene.geometry.values():
            material=getattr(getattr(geometry,'visual',None),'material',None)
            if getattr(material,'name',None) != material_name:
                continue
            uv=getattr(geometry.visual,'uv',None)
            if uv is None:
                continue
            uv=np.asarray(uv,dtype=np.float64)
            for face in np.asarray(geometry.faces,dtype=np.int64):
                tri=uv[face]
                for shifted in _shifted_triangle_copies(tri):
                    pts=[(float(u*(size-1)),float((1-v)*(size-1))) for u,v in shifted]
                    draw.polygon(pts,fill=255)
    if dilation>0:
        kernel=max(3,dilation*2+1)
        if kernel%2==0: kernel+=1
        mask=mask.filter(ImageFilter.MaxFilter(kernel))
    return mask


def usage_report(mask: Image.Image, texture_size: int=2048, tile_size: int=768,
                 overlap: int=96, threshold: float=0.001) -> dict:
    arr=np.array(mask)>0
    coverage=float(arr.mean()) if arr.size else 0.0
    bbox=mask.getbbox()
    stride=max(1,tile_size-overlap)
    starts=[]
    for dimension in (texture_size,texture_size):
        vals=list(range(0,dimension,stride))
        vals=sorted(set(min(v,max(0,dimension-tile_size)) for v in vals))
        starts.append(vals)
    xs,ys=starts
    occupancy=np.array(mask.resize((texture_size,texture_size),Image.Resampling.NEAREST))>0
    active=[]
    for y in ys:
        for x in xs:
            sub=occupancy[y:min(y+tile_size,texture_size),x:min(x+tile_size,texture_size)]
            ratio=float(sub.mean()) if sub.size else 0.0
            if ratio>threshold:
                active.append({'x':x,'y':y,'coverage':round(ratio,6)})
    return {
        'coverage_ratio':round(coverage,6),
        'bbox_mask_pixels':bbox,
        'mask_size':mask.size,
        'texture_size':texture_size,
        'tile_size':tile_size,
        'overlap':overlap,
        'total_grid_patches':len(xs)*len(ys),
        'active_grid_patches':len(active),
        'active_patches':active,
    }


def main() -> int:
    import argparse, json
    p=argparse.ArgumentParser(prog='diyse-uv-usage')
    p.add_argument('gltf',nargs='+',type=Path)
    p.add_argument('--material',required=True)
    p.add_argument('--mask-size',type=int,default=512)
    p.add_argument('--texture-size',type=int,default=2048)
    p.add_argument('--tile-size',type=int,default=768)
    p.add_argument('--overlap',type=int,default=96)
    p.add_argument('--mask-out',type=Path)
    a=p.parse_args()
    mask=rasterize_uv_usage(a.gltf,a.material,size=a.mask_size)
    if a.mask_out:
        a.mask_out.parent.mkdir(parents=True,exist_ok=True); mask.save(a.mask_out,'PNG')
    print(json.dumps(usage_report(mask,a.texture_size,a.tile_size,a.overlap),indent=2))
    return 0

if __name__=='__main__': raise SystemExit(main())
