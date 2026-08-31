import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

MODULE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_DIR))

import atlas_engine
import animation_engine


class AtlasEngineTests(unittest.TestCase):
    def test_identity_round_trip_is_pixel_exact(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            source = root / "atlas.png"
            output = root / "atlas_out.png"
            height, width = 1300, 1700
            yy, xx = np.indices((height, width))
            pixels = np.zeros((height, width, 4), dtype=np.uint8)
            pixels[..., 0] = xx % 256
            pixels[..., 1] = yy % 256
            pixels[..., 2] = (xx + yy) % 256
            pixels[..., 3] = 255
            Image.fromarray(pixels, mode="RGBA").save(source)

            patches = atlas_engine.process_atlas(
                source,
                output,
                lambda image, patch: image,
                tile=512,
                overlap=64,
            )
            rebuilt = np.asarray(Image.open(output).convert("RGBA"))
            self.assertGreater(len(patches), 1)
            self.assertTrue(np.array_equal(pixels, rebuilt))

    def test_processor_cannot_change_patch_dimensions(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            source = root / "atlas.png"
            output = root / "atlas_out.png"
            Image.new("RGBA", (900, 600), (100, 100, 100, 255)).save(source)

            def invalid_processor(image, patch):
                return image.resize((image.width - 1, image.height))

            with self.assertRaises(ValueError):
                atlas_engine.process_atlas(
                    source,
                    output,
                    invalid_processor,
                    tile=400,
                    overlap=64,
                )


class AnimationEngineTests(unittest.TestCase):
    def test_propagation_preserves_each_frames_alpha_and_anchor(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            frames = []
            for index, shift in enumerate((0, 5, 10)):
                pixels = np.zeros((64, 64, 4), dtype=np.uint8)
                pixels[16:48, 8 + shift:32 + shift, :3] = (40, 120, 50)
                pixels[16:48, 8 + shift:32 + shift, 3] = 255
                path = root / f"grass_{index}.png"
                Image.fromarray(pixels, mode="RGBA").save(path)
                frames.append(path)

            styled_anchor = root / "styled_anchor.png"
            with Image.open(frames[0]).convert("RGBA") as source_anchor:
                styled = source_anchor.copy()
            array = np.asarray(styled).copy()
            visible = array[..., 3] > 0
            array[visible, :3] = (80, 170, 70)
            styled = Image.fromarray(array, mode="RGBA")
            ImageDraw.Draw(styled).rectangle((8, 16, 31, 47), outline=(20, 40, 20, 255), width=2)
            styled.save(styled_anchor)

            output_dir = root / "out"
            animation_engine.propagate_sequence(frames, styled_anchor, output_dir)

            anchor_out = np.asarray(Image.open(output_dir / "grass_0__STYLE_PASS.png").convert("RGBA"))
            expected_anchor = np.asarray(Image.open(styled_anchor).convert("RGBA"))
            self.assertTrue(np.array_equal(anchor_out, expected_anchor))

            for index, source_path in enumerate(frames):
                source = np.asarray(Image.open(source_path).convert("RGBA"))
                output = np.asarray(Image.open(output_dir / f"grass_{index}__STYLE_PASS.png").convert("RGBA"))
                self.assertTrue(np.array_equal(source[..., 3], output[..., 3]))

            self.assertTrue((output_dir / "animation_style_profile.json").exists())


if __name__ == "__main__":
    unittest.main()
