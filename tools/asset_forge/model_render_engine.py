#!/usr/bin/env python3
"""Deterministic software renderer for Diyse Asset Forge prop validation.

Stable neutral/warm/cool review renders from glTF assets without Blender/OpenGL.
This is a validation renderer, not the final Godot renderer.
"""
from __future__ import annotations

from pathlib import Path
from typing import Mapping

import numpy as np
import trimesh
from PIL import Image, ImageDraw, ImageFilter


def _camera_basis(view=np.array([1.35,0.85,1.55],dtype=np.float64)):
    forward=-view/np.linalg.norm(view); world_up=np.array([0.0,1.0,0.0])
    right=np.cross(forward,world_up); right/=np.linalg.norm(right)
    up=np.cross(right,forward); up/=np.linalg.norm(up)
    return right,up,forward


def _load_texture(path: Path) -> np.ndarray:
    return np.array(Image.open(path).convert('RGB'))


def _family_from_texture_path(path: Path) -> str | None:
    name=path.name.lower()
    for family in ('furniture','metal','props','cloth'):
        if f'{family}_basecolor' in name:
            return family.capitalize()
    return None


def _infer_orm(gltf: Path, basecolor_path: Path) -> Path | None:
    family=_family_from_texture_path(basecolor_path)
    if not family: return None
    path=gltf.parent/f'T_Trim_{family}_ORM.png'
    return path if path.exists() else None


def _find_emitter_anchor(vertices: np.ndarray, model_name: str):
    if 'lantern' not in model_name.lower(): return None
    ymin,ymax=vertices[:,1].min(),vertices[:,1].max(); cutoff=ymin+(ymax-ymin)*0.38
    lower=vertices[vertices[:,1]<=cutoff]
    if len(lower)<8: lower=vertices
    center=np.median(lower,axis=0); center[2]=np.percentile(lower[:,2],60)
    radius=float(max((lower.max(0)-lower.min(0))[[0,1]].max()*0.16,0.035))
    return center,radius


def render_gltf(gltf: Path, output: Path, material_textures: Mapping[str,Path], size: int=512,
                lighting: str='neutral', emissive_hint: bool=False, author_emissive: bool|None=None) -> None:
    if author_emissive is None: author_emissive=emissive_hint
    scene=trimesh.load(gltf,force='scene',process=False)
    textures={name:_load_texture(Path(path)) for name,path in material_textures.items()}
    texture_paths={name:Path(path) for name,path in material_textures.items()}
    orm_textures: dict[str,np.ndarray|None]={}; pieces=[]; all_vertices=[]
    for node in scene.graph.nodes_geometry:
        transform,geometry_name=scene.graph[node]; mesh=scene.geometry[geometry_name]
        if getattr(mesh.visual,'uv',None) is None: continue
        material=mesh.visual.material.name
        if material not in textures: continue
        if material not in orm_textures:
            orm_path=_infer_orm(gltf,texture_paths[material])
            orm_textures[material]=_load_texture(orm_path) if orm_path else None
        vertices=trimesh.transform_points(mesh.vertices,transform)
        pieces.append((vertices,np.asarray(mesh.faces,dtype=np.int64),np.asarray(mesh.visual.uv,dtype=np.float64),material))
        all_vertices.append(vertices)
    if not pieces: raise RuntimeError(f'No renderable textured geometry found: {gltf}')

    vertices_all=np.vstack(all_vertices); center=(vertices_all.min(0)+vertices_all.max(0))/2
    right,up,forward=_camera_basis(); view_dir=-forward; projected=[]
    for vertices,faces,uv,material in pieces:
        local=vertices-center; projected.append((local,local@right,local@up,local@forward,faces,uv,material))
    all_x=np.concatenate([p[1] for p in projected]); all_y=np.concatenate([p[2] for p in projected])
    span=max(np.ptp(all_x),np.ptp(all_y),1e-6); scale=(size*0.76)/span
    background={'neutral':(26,26,28),'warm':(31,26,23),'cool':(22,27,33)}[lighting]
    light_dir={'neutral':np.array([-0.35,0.65,0.68]),'warm':np.array([-0.55,0.48,0.68]),'cool':np.array([0.30,0.60,0.74])}[lighting].astype(np.float64)
    light_dir/=np.linalg.norm(light_dir)
    tint=np.array({'neutral':(1.,1.,1.),'warm':(1.08,.93,.82),'cool':(.84,.93,1.08)}[lighting])
    half_vector=light_dir+view_dir; half_vector/=np.linalg.norm(half_vector)
    image=np.empty((size,size,3),np.float32); image[:]=background; zbuffer=np.full((size,size),np.inf,np.float32)

    for local,x,y,z,faces,uv,material in projected:
        sx=x*scale+size/2; sy=-y*scale+size*0.54; depth=-z
        texture=textures[material]; orm=orm_textures[material]; tex_h,tex_w=texture.shape[:2]
        family=_family_from_texture_path(texture_paths[material]); is_metal=family=='Metal'
        for face in faces:
            points=np.stack([sx[face],sy[face]],axis=1)
            xmin=max(int(np.floor(points[:,0].min())),0); xmax=min(int(np.ceil(points[:,0].max())),size-1)
            ymin=max(int(np.floor(points[:,1].min())),0); ymax=min(int(np.ceil(points[:,1].max())),size-1)
            if xmax<xmin or ymax<ymin: continue
            a,b,c=points; denominator=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
            if abs(denominator)<1e-9: continue
            xx=np.arange(xmin,xmax+1); yy=np.arange(ymin,ymax+1); X,Y=np.meshgrid(xx,yy)
            w0=((b[1]-c[1])*(X-c[0])+(c[0]-b[0])*(Y-c[1]))/denominator
            w1=((c[1]-a[1])*(X-c[0])+(a[0]-c[0])*(Y-c[1]))/denominator; w2=1-w0-w1
            inside=(w0>=-1e-5)&(w1>=-1e-5)&(w2>=-1e-5)
            if not inside.any(): continue
            zz=w0*depth[face[0]]+w1*depth[face[1]]+w2*depth[face[2]]; zsub=zbuffer[ymin:ymax+1,xmin:xmax+1]
            mask=inside&(zz<zsub)
            if not mask.any(): continue
            tex_uv=w0[...,None]*uv[face[0]]+w1[...,None]*uv[face[1]]+w2[...,None]*uv[face[2]]
            u=np.mod(tex_uv[...,0],1.0); v=np.mod(tex_uv[...,1],1.0)
            tx=np.clip((u*(tex_w-1)).astype(int),0,tex_w-1); ty=np.clip(((1-v)*(tex_h-1)).astype(int),0,tex_h-1)
            color=texture[ty,tx].astype(np.float32)
            triangle=local[face]; normal=np.cross(triangle[1]-triangle[0],triangle[2]-triangle[0]); length=np.linalg.norm(normal)
            if length>1e-9: normal/=length
            ndotl=abs(float(np.dot(normal,light_dir))); shaded=color*(0.34+0.66*ndotl)*tint
            if orm is not None:
                oh,ow=orm.shape[:2]; otx=np.clip((u*(ow-1)).astype(int),0,ow-1); oty=np.clip(((1-v)*(oh-1)).astype(int),0,oh-1)
                pbr=orm[oty,otx].astype(np.float32)/255.0; shaded*=0.78+0.22*pbr[...,0:1]
                roughness=pbr[...,1:2]; metallic=pbr[...,2:3]
            else:
                roughness=np.full((*mask.shape,1),0.58 if is_metal else 0.82,np.float32)
                metallic=np.full((*mask.shape,1),1.0 if is_metal else 0.0,np.float32)
            ndoth=abs(float(np.dot(normal,half_vector))); power=6+42*(1-roughness)
            specular=np.power(ndoth,power)*(1-roughness)*(0.12+0.88*metallic)
            shaded+=specular*(128 if is_metal else 28)
            shaded=np.clip(shaded,0,255); sub=image[ymin:ymax+1,xmin:xmax+1]; sub[mask]=shaded[mask]; zsub[mask]=zz[mask]

    output_image=Image.fromarray(image.astype(np.uint8),'RGB')
    if author_emissive:
        anchor=_find_emitter_anchor(vertices_all,gltf.stem)
        if anchor is not None:
            world_anchor,radius=anchor; local_anchor=world_anchor-center
            cx=float(local_anchor@right*scale+size/2); cy=float(-(local_anchor@up)*scale+size*0.54); rr=float(max(radius*scale,5))
            halo=Image.new('RGBA',output_image.size,(0,0,0,0)); draw=ImageDraw.Draw(halo)
            for multiplier,alpha in [(1.4,88),(2.3,42),(3.4,18)]:
                r=rr*multiplier; draw.ellipse((cx-r,cy-r,cx+r,cy+r),fill=(255,157,63,alpha))
            halo=halo.filter(ImageFilter.GaussianBlur(float(max(rr*0.65,3)))); output_image=Image.alpha_composite(output_image.convert('RGBA'),halo)
            core=Image.new('RGBA',output_image.size,(0,0,0,0)); d=ImageDraw.Draw(core); r=rr*0.42
            d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=(255,226,151,235)); output_image=Image.alpha_composite(output_image,core).convert('RGB')
    output.parent.mkdir(parents=True,exist_ok=True); output_image.save(output,'PNG')


def main() -> int:
    import argparse
    parser=argparse.ArgumentParser(); parser.add_argument('gltf',type=Path); parser.add_argument('output',type=Path)
    parser.add_argument('--texture',action='append',default=[],help='MATERIAL=/path/to/BaseColor.png')
    parser.add_argument('--lighting',choices=['neutral','warm','cool'],default='neutral'); parser.add_argument('--author-emissive',action='store_true')
    args=parser.parse_args(); materials={}
    for item in args.texture:
        name,path=item.split('=',1); materials[name]=Path(path)
    render_gltf(args.gltf,args.output,materials,lighting=args.lighting,author_emissive=args.author_emissive); return 0

if __name__=='__main__': raise SystemExit(main())
