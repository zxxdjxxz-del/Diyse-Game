import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image

MODULE_PATH = Path(__file__).resolve().parents[1] / "forge.py"
spec = importlib.util.spec_from_file_location("diyse_asset_forge", MODULE_PATH)
forge = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = forge
assert spec.loader is not None
spec.loader.exec_module(forge)


class AssetForgeTests(unittest.TestCase):
    def test_classification(self):
        self.assertEqual(forge.classify("gt_1_map084_tree_color.tga"), "foliage")
        self.assertEqual(forge.classify("gt_1_map111_watersurface_color_0.tga"), "water")
        self.assertEqual(forge.classify("gt_5_map092_fire_color_0.tga"), "fire")
        self.assertEqual(forge.classify("gt_0_map109_map_color.tga"), "atlas")

    def test_inventory_and_animation_plan(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            for i in range(3):
                Image.new("RGBA", (64, 64), (10, 100, 20, 128)).save(
                    root / f"gt_1_map081_grass_color_{i}.png"
                )
            records = [forge.asdict(r) for r in forge.inventory(root)]
            self.assertEqual(len(records), 3)
            self.assertTrue(all(r["category"] == "grass" for r in records))
            queue = forge.plan(records)
            self.assertEqual(queue[0]["action"], "ai_style_edit")
            self.assertEqual(queue[1]["action"], "propagate_from_anchor")
            self.assertEqual(queue[2]["action"], "propagate_from_anchor")

    def test_large_atlas_is_structure_preserving(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            Image.new("RGB", (2048, 2048), (100, 100, 100)).save(root / "gt_0_map086_map_color.png")
            rec = forge.asdict(forge.inventory(root)[0])
            self.assertEqual(rec["treatment"], "atlas_structure_preserving")
            planned = forge.plan([rec])[0]
            self.assertEqual(planned["action"], "structure_preserving_pass")

    def test_contact_sheet_uses_actual_outputs(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            out = root / "styled.png"
            Image.new("RGBA", (64, 32), (30, 100, 40, 200)).save(out)
            sheet = root / "sheet.png"
            forge.make_contact_sheet([
                {
                    "relative_path": "tree.png",
                    "category": "foliage",
                    "status": "generated",
                    "output_path": str(out),
                    "qa": {"status": "review"},
                }
            ], sheet, columns=1, thumb=64)
            self.assertTrue(sheet.exists())
            self.assertGreater(sheet.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()
