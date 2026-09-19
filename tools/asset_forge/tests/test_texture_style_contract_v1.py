import importlib.util
import json
import sys
import unittest
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import forge_current


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


style = load_module("diyse_texture_style_contract_materials", "material_style_engine.py")


class TextureStyleContractV1Tests(unittest.TestCase):
    def test_contract_is_active_and_user_gated(self):
        contract = forge_current.STYLE_CONTRACT
        self.assertEqual(contract["id"], "DIYSE_ASSET_FORGE_TEXTURE_STYLE_CONTRACT_V1")
        self.assertEqual(contract["status"], "active")
        self.assertFalse(contract["review"]["automatic_approval"])
        self.assertTrue(contract["review"]["user_approval_required"])

    def test_current_planner_uses_graphic_non_painterly_target_language(self):
        prompt = forge_current.make_prompt({
            "category": "stone",
            "treatment": "direct_style_edit",
        })
        lower = prompt.lower()
        self.assertIn("graphic anime-stylized shape-first rendering", lower)
        self.assertIn("large readable stone planes", lower)
        self.assertNotIn("painterly shape-first rendering", lower)
        self.assertNotIn("use painterly stone planes", lower)
        self.assertNotIn("painterly foliage values", lower)

    def test_all_texture_contract_categories_have_prompts(self):
        expected = {
            "stone", "foliage", "grass", "water", "fire", "wood",
            "cave", "ritual", "interior", "prop", "generic",
        }
        self.assertTrue(expected.issubset(forge_current.STYLE_CONTRACT["categories"]))

    def test_new_deterministic_material_families_preserve_dimensions(self):
        image = Image.new("RGB", (96, 64), (105, 92, 76))
        for kind in ("stone", "foliage", "grass"):
            result = style.stylize_material_image(image, kind)
            self.assertEqual(result.size, image.size)

    def test_foliage_preserves_source_alpha_exactly(self):
        image = Image.new("RGBA", (64, 64), (20, 120, 35, 0))
        draw = ImageDraw.Draw(image)
        draw.ellipse((8, 8, 56, 56), fill=(35, 150, 55, 180))
        before = image.getchannel("A").tobytes()
        result = style.stylize_material_image(image, "foliage")
        self.assertEqual(result.getchannel("A").tobytes(), before)

    def test_stone_profile_comes_from_contract_file(self):
        raw = json.loads((ROOT / "texture_style_contract_v1.json").read_text(encoding="utf-8"))
        self.assertEqual(style.material_profile("stone"), raw["material_profiles"]["stone"])


if __name__ == "__main__":
    unittest.main()
