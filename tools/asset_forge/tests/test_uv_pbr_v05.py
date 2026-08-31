import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
from PIL import Image
import trimesh
from trimesh.visual.material import PBRMaterial
from trimesh.visual.texture import TextureVisuals

TOOL_ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, TOOL_ROOT / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


uv_usage = load_module("diyse_uv_usage", "uv_usage_engine.py")
pbr_qa = load_module("diyse_pbr_qa", "pbr_qa_engine.py")


class UvAndPbrV05Tests(unittest.TestCase):
    def test_uv_usage_mask_handles_wrapped_uvs(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            mesh = trimesh.creation.box(extents=(1, 1, 1))
            uv = np.tile(
                np.array([[0.1, 0.1], [0.9, 0.1], [1.1, 0.9], [0.1, 0.9]], dtype=float),
                (2, 1),
            )[:len(mesh.vertices)]
            material = PBRMaterial(
                name="MI_Test",
                baseColorTexture=Image.new("RGB", (8, 8), (100, 100, 100)),
            )
            mesh.visual = TextureVisuals(uv=uv, material=material)
            files = trimesh.exchange.gltf.export_gltf(trimesh.Scene(mesh))
            for filename, data in files.items():
                (root / filename).write_bytes(data)

            mask = uv_usage.rasterize_uv_usage([root / "model.gltf"], "MI_Test", size=128)
            report = uv_usage.usage_report(mask, texture_size=256, tile_size=128, overlap=16)
            self.assertGreater(report["coverage_ratio"], 0.0)
            self.assertGreater(report["active_grid_patches"], 0)

    def test_pbr_flags_strong_normal_but_not_matte_roughness(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            normal = np.zeros((16, 16, 3), np.uint8)
            normal[:] = [255, 128, 128]
            orm = np.zeros((16, 16, 3), np.uint8)
            orm[:] = [255, 230, 0]
            Image.fromarray(normal).save(root / "normal.png")
            Image.fromarray(orm).save(root / "orm.png")
            result = pbr_qa.analyze_pbr(root / "normal.png", root / "orm.png")
            self.assertIn("strong_normal_review", result["review_flags"])
            self.assertNotIn("glossy_roughness_review", result["review_flags"])


if __name__ == "__main__":
    unittest.main()
