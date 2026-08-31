#!/usr/bin/env python3
"""Shared-material analysis for Diyse Asset Forge.

This module detects when many 3D assets share the same BaseColor/Normal/ORM trim sheets.
The goal is to restyle shared material sheets once, then validate many models against the
same Diyse material language instead of spending one image-generation call per prop.
"""
from __future__ import annotations

import json
import zipfile
from collections import defaultdict
from pathlib import Path
from typing import Iterable


def gltf_image_dependencies(gltf_json: dict) -> list[str]:
    return [img.get("uri", "") for img in gltf_json.get("images", []) if img.get("uri")]


def basecolor_dependencies(gltf_json: dict) -> list[str]:
    return [x for x in gltf_image_dependencies(gltf_json) if "basecolor" in x.lower()]


def analyze_zip_models(zip_path: Path, model_names: Iterable[str], gltf_root: str = "Exports/glTF") -> dict:
    """Return per-model and shared material dependencies for glTF assets in a ZIP."""
    per_model: dict[str, dict] = {}
    reverse: dict[str, list[str]] = defaultdict(list)

    with zipfile.ZipFile(zip_path) as zf:
        for model in model_names:
            member = f"{gltf_root}/{model}.gltf"
            data = json.loads(zf.read(member))
            all_images = gltf_image_dependencies(data)
            basecolors = basecolor_dependencies(data)
            materials = [m.get("name", "") for m in data.get("materials", [])]
            per_model[model] = {
                "member": member,
                "materials": materials,
                "images": all_images,
                "basecolor_images": basecolors,
            }
            for image in basecolors:
                reverse[image].append(model)

    return {
        "models": per_model,
        "unique_basecolor_images": sorted(reverse),
        "basecolor_usage": {k: sorted(v) for k, v in sorted(reverse.items())},
        "basecolor_generation_calls": len(reverse),
    }


def extract_shared_material_files(zip_path: Path, analysis: dict, output_dir: Path, gltf_root: str = "Exports/glTF") -> list[Path]:
    """Extract only shared BaseColor files required by the analyzed models."""
    output_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    with zipfile.ZipFile(zip_path) as zf:
        for image in analysis["unique_basecolor_images"]:
            member = f"{gltf_root}/{image}"
            dest = output_dir / image
            dest.write_bytes(zf.read(member))
            written.append(dest)
    return written
