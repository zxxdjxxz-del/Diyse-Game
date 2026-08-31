#!/usr/bin/env python3
"""Small deterministic software renderer for Diyse Asset Forge prop validation.

Purpose: stable neutral/warm/cool review renders from glTF assets without requiring
Blender/OpenGL in CI. It is a validation renderer, not the final Godot renderer.
"""
from __future__ import annotations

from pathlib import Path
from typing import Mapping

import numpy as np
import trimesh
from PIL import Image, ImageDraw, ImageFilter


def _camera_basis(view=np.array([1.35,0.85,1.55],dtype=np.float64)):
    # Camera looks from +view toward origin; glTF uses +Y up.
    forward=-view/np.linalg.norm(view)
    world_up=np.array([0.0,1.0,0.0])
    right=np.cross(forward,world_up); right/=np.linalg.norm(right)
    up=np.cross(right,forward); up/=np.linalg.norm(up)
    return right,up,forward


def _load_texture(path: Path) -> np.ndarray:
    return np.array(Image.open(path).convert('RGB'))


def render_gltf(gltf: Path, output: Path, material_textures: Mapping[str,Path], size: int=512,
                lighting: str='neutral', emissive_hint: bool=False) -> None:
    scene=trimesh.load(gltf,force='scene',process=False)
    tex={name:_load_texture(Path(path)) for name,path in material_textures.items()}
    pieces=[]; allv=[]
    for node in scene.graph.nodes_geometry:
        transform,gname=scene.graph[node]
        mesh=scene.geometry[gname]
        uv=np.asarray(mesh.visual.uv,dtype=np.float64)
        mat=mesh.visual.material.name
        if mat not in tex:
            continue
        vertices=trimesh.transform_points(mesh.vertices,transform)
        pieces.append((vertices,np.asarray(mesh.faces,dtype=np.int64),uv,mat))
        allv.append(vertices)
    if not pieces:
        raise RuntimeError(f'No renderable textured geometry found: {gltf}')
    vertices_all=np.vstack(allv)
    center=(vertices_all.min(0)+vertices_all.max(0))/2
    right,up,forward=_camera_basis()
    projected=[]
    for vertices,faces,uv,mat in pieces:
        local=vertices-center
        x=local@right; y=local@up; z=local@forward
        projected.append((local,x,y,z,faces,uv,mat))
    allx=np.concatenate([p[1] for p in projected]); ally=np.concatenate([p[2] for p in projected])
    span=max(np.ptp(allx),np.ptp(ally),1e-6)
    scale=(size*0.76)/span
    bg={'neutral':(26,26,28),'warm':(31,26,23),'cool':(22,27,33)}[lighting]
    light_dir={
        'neutral':np.array([-0.35,0.65,0.68]),
        'warm':np.array([-0.55,0.48,0.68]),
        'cool':np.array([0.30,0.60,0.74]),
    }[lighting].astype(np.float64)
    light_dir/=np.linalg.norm(light_dir)
    tint=np.array({'neutral':(1.0,1.0,1.0),'warm':(1.08,0.93,0.82),'cool':(0.84,0.93,1.08)}[lighting])
    image=np.empty((size,size,3),np.float32); image[:]=bg
    zbuf=np.full((size,size),np.inf,np.float32)

    for local,x,y,z,faces,uv,mat in projected:
        sx=x*scale+size/2; sy=-y*scale+size*0.54; depth=-z
        texture=tex[mat]; H,W=texture.shape[:2]
        for face in faces:
            pts=np.stack([sx[face],sy[face]],axis=1)
            xmin=max(int(np.floor(pts[:,0].min())),0); xmax=min(int(np.ceil(pts[:,0].max())),size-1)
            ymin=max(int(np.floor(pts[:,1].min())),0); ymax=min(int(np.ceil(pts[:,1].max())),size-1)
            if xmax<xmin or ymax<ymin: continue
            a,b,c=pts
            denom=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
            if abs(denom)<1e-9: continue
            xx=np.arange(xmin,xmax+1); yy=np.arange(ymin,ymax+1); X,Y=np.meshgrid(xx,yy)
            w0=((b[1]-c[1])*(X-c[0])+(c[0]-b[0])*(Y-c[1]))/denom
            w1=((c[1]-a[1])*(X-c[0])+(a[0]-c[0])*(Y-c[1]))/denom
            w2=1-w0-w1
            inside=(w0>=-1e-5)&(w1>=-1e-5)&(w2>=-1e-5)
            if not inside.any(): continue
            zz=w0*depth[face[0]]+w1*depth[face[1]]+w2*depth[face[2]]
            zb=zbuf[ymin:ymax+1,xmin:xmax+1]
            mask=inside&(zz<zb)
            if not mask.any(): continue
            tuv=w0[...,None]*uv[face[0]]+w1[...,None]*uv[face[1]]+w2[...,None]*uv[face[2]]
            u=np.mod(tuv[...,0],1.0); v=np.mod(tuv[...,1],1.0)
            tx=np.clip((u*(W-1)).astype(int),0,W-1); ty=np.clip(((1-v)*(H-1)).astype(int),0,H-1)
            color=texture[ty,tx].astype(np.float32)
            tri=local[face]
            normal=np.cross(tri[1]-tri[0],tri[2]-tri[0]); length=np.linalg.norm(normal)
            if length>1e-9: normal/=length
            lam=0.40+0.60*abs(float(np.dot(normal,light_dir)))
            color=np.clip(color*lam*tint,0,255)
            sub=image[ymin:ymax+1,xmin:xmax+1]
            sub[mask]=color[mask]; zb[mask]=zz[mask]

    out=Image.fromarray(image.astype(np.uint8),'RGB')
    if emissive_hint:
        # Validation-only warm light hint: this is not authored emissive material data.
        glow=Image.new('RGBA',out.size,(0,0,0,0)); d=ImageDraw.Draw(glow)
        cx,cy=size*0.43,size*0.60
        for radius,alpha in [(58,18),(38,28),(22,42)]:
            d.ellipse((cx-radius,cy-radius,cx+radius,cy+radius),fill=(255,173,74,alpha))
        glow=glow.filter(ImageFilter.GaussianBlur(12))
        out=Image.alpha_composite(out.convert('RGBA'),glow).convert('RGB')
    output.parent.mkdir(parents=True,exist_ok=True); out.save(output,'PNG')


def main() -> int:
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument('gltf',type=Path); p.add_argument('output',type=Path)
    p.add_argument('--furniture',type=Path); p.add_argument('--metal',type=Path)
    p.add_argument('--lighting',choices=['neutral','warm','cool'],default='neutral')
    p.add_argument('--emissive-hint',action='store_true')
    a=p.parse_args()
    mats={}
    if a.furniture: mats['MI_Trim_Furniture']=a.furniture
    if a.metal: mats['MI_Trim_Metal']=a.metal
    render_gltf(a.gltf,a.output,mats,lighting=a.lighting,emissive_hint=a.emissive_hint)
    return 0
if __name__=='__main__': raise SystemExit(main())
