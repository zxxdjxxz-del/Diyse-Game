import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import trimesh
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


normal_mod = load_module('diyse_normal_rebalance', 'normal_rebalance_engine.py')
material_mod = load_module('diyse_material_style_v2', 'material_style_engine.py')
emissive_mod = load_module('diyse_emissive_anchor', 'emissive_anchor_engine.py')


class PropRefinementV06Tests(unittest.TestCase):
    def test_normal_rebalance_reduces_xy_strength(self):
        source = np.zeros((32, 32, 3), dtype=np.uint8)
        source[..., 0] = 230
        source[..., 1] = 180
        source[..., 2] = 200
        image = Image.fromarray(source, 'RGB')

        before = source.astype(np.float32) / 255.0 * 2.0 - 1.0
        before_xy = np.sqrt(before[..., 0] ** 2 + before[..., 1] ** 2).mean()
        result = np.array(normal_mod.rebalance_normal_image(image, strength=0.72), dtype=np.float32)
        after = result / 255.0 * 2.0 - 1.0
        after_xy = np.sqrt(after[..., 0] ** 2 + after[..., 1] ** 2).mean()

        self.assertLess(after_xy, before_xy)
        self.assertTrue((after[..., 2] >= 0).all())

    def test_material_stylization_preserves_dimensions(self):
        x = np.linspace(0, 255, 96, dtype=np.uint8)
        source = np.tile(x, (64, 1))
        rgb = np.dstack([source, np.flipud(source), source // 2])
        image = Image.fromarray(rgb, 'RGB')

        wood = material_mod.stylize_material_image(image, 'wood')
        metal = material_mod.stylize_material_image(image, 'metal')

        self.assertEqual(wood.size, image.size)
        self.assertEqual(metal.size, image.size)
        self.assertGreater(np.array(wood).std(), 1.0)
        self.assertGreater(np.array(metal).std(), 1.0)

    def test_lantern_anchor_is_model_space_and_lower_than_bracket(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'Lantern_Test.glb'
            cage = trimesh.creation.box(extents=(0.4, 0.4, 0.4))
            cage.apply_translation((0.0, 0.2, 0.5))
            bracket = trimesh.creation.box(extents=(0.2, 1.0, 0.2))
            bracket.apply_translation((0.0, 1.0, 0.8))
            trimesh.Scene([cage, bracket]).export(path)

            anchor = emissive_mod.derive_emissive_anchor(path)
            self.assertIsNotNone(anchor)
            self.assertEqual(anchor['model'], 'Lantern_Test')
            self.assertLess(anchor['position_model_space'][1], 0.75)
            self.assertGreater(anchor['core_radius'], 0)
            self.assertFalse(anchor['source_authored_emissive'])


if __name__ == '__main__':
    unittest.main()
