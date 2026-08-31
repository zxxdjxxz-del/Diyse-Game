import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
from PIL import Image

MODULE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_DIR))

import budget_engine
import lighting_engine
import qa_engine


class LightingEngineTests(unittest.TestCase):
    def test_lighting_state_preserves_style_base_and_state_direction(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            base = np.zeros((64, 64, 4), dtype=np.uint8)
            base[..., :3] = 100
            base[..., 3] = 255
            styled = base.copy()
            styled[..., :3] = (80, 120, 160)
            state = base.copy()
            state[:, :32, :3] = 50
            state[:, 32:, :3] = 180

            base_path = root / "base.png"
            styled_path = root / "styled.png"
            state_path = root / "state.png"
            output_path = root / "output.png"
            Image.fromarray(base, mode="RGBA").save(base_path)
            Image.fromarray(styled, mode="RGBA").save(styled_path)
            Image.fromarray(state, mode="RGBA").save(state_path)

            lighting_engine.propagate_lighting_state(
                base_path, styled_path, state_path, output_path
            )
            output = np.asarray(Image.open(output_path).convert("RGBA"))
            self.assertEqual(output.shape, state.shape)
            self.assertLess(output[:, :32, :3].mean(), output[:, 32:, :3].mean())
            self.assertTrue(np.array_equal(output[..., 3], state[..., 3]))


class QaEngineTests(unittest.TestCase):
    def test_identity_atlas_has_zero_seam_regression(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            pixels = np.zeros((64, 64, 4), dtype=np.uint8)
            pixels[..., :3] = 100
            pixels[..., 3] = 255
            source = root / "source.png"
            Image.fromarray(pixels, mode="RGBA").save(source)
            plan = [
                {"x0": 0, "x1": 32, "y0": 0, "y1": 64},
                {"x0": 32, "x1": 64, "y0": 0, "y1": 64},
            ]
            result = qa_engine.atlas_seam_regression(source, source, plan)
            self.assertEqual(result["status"], "review")
            self.assertEqual(result["worst_new_seam_jump"], 0.0)

    def test_flicker_regression_is_one_for_constant_style_offset(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            source_frames = []
            output_frames = []
            for index in range(3):
                pixels = np.zeros((32, 32, 4), dtype=np.uint8)
                pixels[..., 3] = 255
                pixels[:, index * 2:index * 2 + 8, :3] = 100
                source = root / f"source_{index}.png"
                Image.fromarray(pixels, mode="RGBA").save(source)
                source_frames.append(source)

                styled = pixels.copy()
                styled[..., :3] = np.clip(styled[..., :3].astype(np.int16) + 10, 0, 255).astype(np.uint8)
                output = root / f"output_{index}.png"
                Image.fromarray(styled, mode="RGBA").save(output)
                output_frames.append(output)

            result = qa_engine.animation_flicker_regression(source_frames, output_frames)
            self.assertEqual(result["status"], "review")
            self.assertAlmostEqual(result["regression_ratio"], 1.0, places=5)


class BudgetEngineTests(unittest.TestCase):
    def test_propagated_frames_cost_zero_generation_calls(self):
        queue = [
            {"action": "ai_style_edit", "category": "grass", "width": 64, "height": 64},
            {"action": "propagate_from_anchor", "category": "grass", "width": 64, "height": 64},
            {"action": "structure_preserving_pass", "category": "atlas", "width": 2048, "height": 2048},
        ]
        result = budget_engine.estimate_generation_calls(queue)
        self.assertEqual(result["by_action"]["propagate_from_anchor"], 0)
        self.assertEqual(result["by_action"]["ai_style_edit"], 1)
        self.assertEqual(result["by_action"]["structure_preserving_pass"], 9)
        self.assertEqual(result["estimated_image_generation_calls"], 10)


if __name__ == "__main__":
    unittest.main()
