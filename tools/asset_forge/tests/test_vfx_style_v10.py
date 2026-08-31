import importlib.util
import sys
import unittest
from pathlib import Path

import numpy as np
from PIL import Image

MODULE_PATH = Path(__file__).resolve().parents[1] / 'vfx_style_engine.py'
spec = importlib.util.spec_from_file_location('diyse_vfx_style', MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
assert spec.loader is not None
spec.loader.exec_module(mod)


class VfxStyleTests(unittest.TestCase):
    def make_sheet(self):
        arr = np.zeros((64, 128, 4), dtype=np.uint8)
        # 4x2 grid, each frame 32x32. Vary brightness while retaining motion rhythm.
        for i in range(8):
            y0 = (i // 4) * 32
            x0 = (i % 4) * 32
            yy, xx = np.indices((32, 32))
            cx = 16 + (i % 3) - 1
            cy = 22 - (i % 4)
            radius = 8 + (i % 2)
            mask = ((xx - cx) ** 2 + (yy - cy) ** 2) < radius ** 2
            strength = 90 + i * 18
            arr[y0:y0+32, x0:x0+32, 0][mask] = min(255, strength + 80)
            arr[y0:y0+32, x0:x0+32, 1][mask] = min(255, strength)
            arr[y0:y0+32, x0:x0+32, 2][mask] = 20
            arr[y0:y0+32, x0:x0+32, 3][mask] = 220
        return Image.fromarray(arr, 'RGBA')

    def test_style_preserves_alpha_and_dimensions(self):
        src = self.make_sheet()
        styled = mod.stylize_fire_rgba(src)
        self.assertEqual(src.size, styled.size)
        self.assertTrue(np.array_equal(np.asarray(src)[..., 3], np.asarray(styled)[..., 3]))

    def test_temporal_qa_accepts_structure_preserving_treatment(self):
        src = self.make_sheet()
        styled = mod.stylize_fire_rgba(src)
        qa = mod.temporal_qa(src, styled, 4, 2)
        self.assertTrue(qa['alpha_exact'])
        self.assertGreaterEqual(qa['luminance_rhythm_correlation'], 0.95)
        self.assertTrue(qa['pass'])

    def test_parse_grid(self):
        self.assertEqual(mod.parse_grid('16x4'), (16, 4))
        self.assertEqual(len(mod.split_grid(self.make_sheet(), 4, 2)), 8)


if __name__ == '__main__':
    unittest.main()
