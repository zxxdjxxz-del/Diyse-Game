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
    def edit(self, source: Path, prompt: str, has_alpha: bool) -> bytes:
        with Image.open(source).convert("RGBA") as image:
            pixels = np.asarray(image).copy()
        pixels[..., :3] = np.clip(pixels[..., :3].astype(np.int16) + 20, 0, 255).astype(np.uint8)
        output = Image.fromarray(pixels, mode="RGBA")
        buffer = io.BytesIO()
        output.save(buffer, format="PNG")
        return buffer.getvalue()


class PipelineV02Tests(unittest.TestCase):
    def test_anchor_propagation_and_atlas_processing(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rows = []
            group = str(root / "grass")

            for index, shift in enumerate((0, 5, 10)):
                pixels = np.zeros((64, 64, 4), dtype=np.uint8)
                pixels[20:40, 10 + shift:30 + shift, :3] = (20, 100, 30)
                pixels[20:40, 10 + shift:30 + shift, 3] = 255
                source = root / f"grass_{index}.png"
                Image.fromarray(pixels, mode="RGBA").save(source)
                rows.append({
                    "source_path": str(source),
                    "relative_path": source.name,
                    "width": 64,
                    "height": 64,
                    "has_alpha": True,
                    "animation_group": group,
                    "frame_index": index,
                    "action": "ai_style_edit" if index == 0 else "propagate_from_anchor",
                    "prompt": "Diyse grass style",
                    "category": "grass",
                    "treatment": "animation_anchor",
                    "status": "queued",
                })

            atlas_pixels = np.zeros((600, 900, 4), dtype=np.uint8)
            atlas_pixels[..., :3] = 100
            atlas_pixels[..., 3] = 255
            atlas_source = root / "map.png"
            Image.fromarray(atlas_pixels, mode="RGBA").save(atlas_source)
            rows.append({
                "source_path": str(atlas_source),
                "relative_path": "map.png",
                "width": 900,
                "height": 600,
                "has_alpha": True,
                "animation_group": None,
                "frame_index": None,
                "action": "structure_preserving_pass",
                "prompt": "Diyse atlas style",
                "category": "atlas",
                "treatment": "atlas_structure_preserving",
                "status": "queued",
            })

            output_root = root / "out"
            results = pipeline.process_v2(
                rows,
                output_root,
                "openai",
                provider=FakeProvider(),
                atlas_tile=400,
                atlas_overlap=64,
            )

            self.assertEqual(
                [row["status"] for row in results],
                ["generated_anchor", "propagated_from_anchor", "propagated_from_anchor", "generated_atlas"],
            )
            self.assertGreater(results[-1]["atlas_patch_count"], 1)

            for row in results:
                image = Image.open(row["output_path"])
                self.assertEqual(image.size, (row["width"], row["height"]))

            for index in range(3):
                source = np.asarray(Image.open(root / f"grass_{index}.png").convert("RGBA"))
                output = np.asarray(Image.open(output_root / f"grass_{index}__STYLE_PASS.png").convert("RGBA"))
                self.assertTrue(np.array_equal(source[..., 3], output[..., 3]))


if __name__ == "__main__":
    unittest.main()
