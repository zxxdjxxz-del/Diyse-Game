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


material_style = load_module("diyse_material_style", "material_style_engine.py")
model_render = load_module("diyse_model_render", "model_render_engine.py")


class MaterialAndRenderV05Tests(unittest.TestCase):
    def test_style_is_deterministic_and_size_safe(self):
        image = Image.new("RGB", (96, 64), (120, 70, 40))
        a = np.array(material_style.stylize_material_image(image, "wood"))
        b = np.array(material_style.stylize_material_image(image, "wood"))
        self.assertEqual(a.shape, (64, 96, 3))
        self.assertTrue(np.array_equal(a, b))

    def test_camera_is_y_up(self):
        right, up, forward = model_render._camera_basis()
        world_y = np.array([0.0, 1.0, 0.0])
        self.assertGreater(float(np.dot(up, world_y)), 0.7)
        self.assertAlmostEqual(float(np.dot(right, up)), 0.0, places=6)
        self.assertAlmostEqual(float(np.dot(right, forward)), 0.0, places=6)

    def test_headless_render(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            mesh = trimesh.creation.box(extents=(1, 2, 1))
            uv = np.zeros((len(mesh.vertices), 2), dtype=float)
            material = PBRMaterial(
                name="MI_Trim_Furniture",
                baseColorTexture=Image.new("RGB", (8, 8), (120, 70, 40)),
            )
            mesh.visual = TextureVisuals(uv=uv, material=material)
            files = trimesh.exchange.gltf.export_gltf(trimesh.Scene(mesh))
            for filename, data in files.items():
                (root / filename).write_bytes(data)

            texture = root / "wood.png"
            Image.new("RGB", (16, 16), (130, 75, 40)).save(texture)
            output = root / "out.png"
            model_render.render_gltf(
                root / "model.gltf",
                output,
                {"MI_Trim_Furniture": texture},
                size=128,
            )
            self.assertTrue(output.exists())
            rendered = np.array(Image.open(output))
            self.assertEqual(rendered.shape, (128, 128, 3))
            self.assertGreater(float(np.std(rendered.astype(float))), 1.0)


if __name__ == "__main__":
    unittest.main()
