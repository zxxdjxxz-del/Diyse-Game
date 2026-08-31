import io
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
from PIL import Image

MODULE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_DIR))

import forge
import pipeline


class FakeProvider(forge.Provider):
    def __init__(self):
        self.calls = 0

    def edit(self, source: Path, prompt: str, has_alpha: bool) -> bytes:
        self.calls += 1
        with Image.open(source).convert("RGBA") as image:
            pixels = np.asarray(image).copy()
        pixels[..., :3] = np.clip(pixels[..., :3].astype(np.int16) + 10, 0, 255).astype(np.uint8)
        output = Image.fromarray(pixels, mode="RGBA")
        buffer = io.BytesIO()
        output.save(buffer, format="PNG")
        return buffer.getvalue()


class PipelineV04BudgetResumeTests(unittest.TestCase):
    def test_budget_blocks_whole_atlas_but_zero_call_propagation_finishes_then_resume_reuses_outputs(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            group = str(root / "grass")
            queue = []

            for index, shift in enumerate((0, 3, 6)):
                pixels = np.zeros((32, 32, 4), dtype=np.uint8)
                pixels[8:20, 4 + shift:14 + shift, :3] = 100
                pixels[8:20, 4 + shift:14 + shift, 3] = 255
                source = root / f"frame_{index}.png"
                Image.fromarray(pixels, mode="RGBA").save(source)
                queue.append({
                    "source_path": str(source),
                    "relative_path": source.name,
                    "sha256": forge.sha256_file(source),
                    "width": 32,
                    "height": 32,
                    "has_alpha": True,
                    "animation_group": group,
                    "frame_index": index,
                    "action": "ai_style_edit" if index == 0 else "propagate_from_anchor",
                    "prompt": "style",
                    "category": "grass",
                    "treatment": "animation_anchor",
                    "status": "queued",
                })

            atlas_pixels = np.zeros((600, 900, 4), dtype=np.uint8)
            atlas_pixels[..., :3] = 100
            atlas_pixels[..., 3] = 255
            atlas = root / "atlas.png"
            Image.fromarray(atlas_pixels, mode="RGBA").save(atlas)
            queue.append({
                "source_path": str(atlas),
                "relative_path": atlas.name,
                "sha256": forge.sha256_file(atlas),
                "width": 900,
                "height": 600,
                "has_alpha": True,
                "animation_group": None,
                "frame_index": None,
                "action": "structure_preserving_pass",
                "prompt": "atlas style",
                "category": "atlas",
                "treatment": "atlas_structure_preserving",
                "status": "queued",
            })

            output_root = root / "out"
            checkpoint = root / "results.jsonl"
            first_provider = FakeProvider()
            first = pipeline.process_v2(
                queue,
                output_root,
                "openai",
                provider=first_provider,
                max_ai_calls=1,
                atlas_tile=400,
                atlas_overlap=64,
                checkpoint_path=checkpoint,
            )

            self.assertEqual(first_provider.calls, 1)
            self.assertEqual(first[0]["status"], "generated_anchor")
            self.assertEqual(first[1]["status"], "propagated_from_anchor")
            self.assertEqual(first[2]["status"], "propagated_from_anchor")
            self.assertEqual(first[3]["status"], "budget_blocked")

            second_provider = FakeProvider()
            second = pipeline.process_v2(
                queue,
                output_root,
                "openai",
                provider=second_provider,
                max_ai_calls=10,
                atlas_tile=400,
                atlas_overlap=64,
                resume_results=first,
                checkpoint_path=checkpoint,
            )

            self.assertTrue(second[0].get("resumed"))
            self.assertTrue(second[1].get("resumed"))
            self.assertTrue(second[2].get("resumed"))
            self.assertEqual(second[3]["status"], "generated_atlas")
            self.assertGreater(second_provider.calls, 1)


if __name__ == "__main__":
    unittest.main()
