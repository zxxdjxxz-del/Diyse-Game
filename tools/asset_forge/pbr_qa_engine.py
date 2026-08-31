#!/usr/bin/env python3
"""Static Normal/ORM diagnostics for Diyse Asset Forge material pilots."""
from __future__ import annotations

from pathlib import Path
import json

import numpy as np
from PIL import Image


def analyze_pbr(normal_path: Path, orm_path: Path) -> dict:
    normal=np.array(Image.open(normal_path).convert('RGB'),dtype=np.float32)/255*2-1
    orm=np.array(Image.open(orm_path).convert('RGB'),dtype=np.float32)/255
    xy=np.sqrt(normal[:,:,0]**2+normal[:,:,1]**2)
    rough=orm[:,:,1]; metal=orm[:,:,2]; ao=orm[:,:,0]
    return {
        'normal_xy_p50':round(float(np.percentile(xy,50)),4),
        'normal_xy_p90':round(float(np.percentile(xy,90)),4),
        'normal_xy_gt_0_5_ratio':round(float((xy>0.5).mean()),4),
        'normal_xy_gt_0_75_ratio':round(float((xy>0.75).mean()),4),
        'roughness_p10':round(float(np.percentile(rough,10)),4),
        'roughness_p50':round(float(np.percentile(rough,50)),4),
        'roughness_p90':round(float(np.percentile(rough,90)),4),
        'roughness_lt_0_5_ratio':round(float((rough<0.5).mean()),4),
        'metallic_p50':round(float(np.percentile(metal,50)),4),
        'ao_p50':round(float(np.percentile(ao,50)),4),
        'review_flags':[
            *(['strong_normal_review'] if float((xy>0.5).mean())>0.20 else []),
            *(['glossy_roughness_review'] if float((rough<0.5).mean())>0.25 else []),
        ],
    }


def main() -> int:
    import argparse
    p=argparse.ArgumentParser(prog='diyse-pbr-qa')
    p.add_argument('normal',type=Path); p.add_argument('orm',type=Path)
    a=p.parse_args(); print(json.dumps(analyze_pbr(a.normal,a.orm),indent=2)); return 0

if __name__=='__main__': raise SystemExit(main())
