import json
import tempfile
import unittest
import zipfile
from pathlib import Path
import importlib.util
import sys

MODULE_PATH = Path(__file__).resolve().parents[1] / "shared_material_engine.py"
spec = importlib.util.spec_from_file_location("diyse_shared_material_engine", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
assert spec.loader is not None
spec.loader.exec_module(mod)


class SharedMaterialEngineTests(unittest.TestCase):
    @staticmethod
    def _gltf(materials, images):
        return json.dumps({
            "materials": [{"name": x} for x in materials],
            "images": [{"uri": x} for x in images],
        })

    def test_shared_basecolor_count(self):
        with tempfile.TemporaryDirectory() as td:
            zpath = Path(td) / "props.zip"
            with zipfile.ZipFile(zpath, "w") as zf:
                zf.writestr("Exports/glTF/Barrel.gltf", self._gltf(["MI_Furniture", "MI_Metal"], [
                    "T_Trim_Furniture_BaseColor.png", "T_Trim_Furniture_Normal.png", "T_Trim_Metal_BaseColor.png"]))
                zf.writestr("Exports/glTF/Chair_1.gltf", self._gltf(["MI_Furniture"], ["T_Trim_Furniture_BaseColor.png"]))
                zf.writestr("Exports/glTF/Lantern_Wall.gltf", self._gltf(["MI_Metal"], ["T_Trim_Metal_BaseColor.png"]))
            result = mod.analyze_zip_models(zpath, ["Barrel", "Chair_1", "Lantern_Wall"])
            self.assertEqual(result["basecolor_generation_calls"], 2)
            self.assertEqual(result["unique_basecolor_images"], [
                "T_Trim_Furniture_BaseColor.png", "T_Trim_Metal_BaseColor.png"])
            self.assertEqual(result["basecolor_usage"]["T_Trim_Metal_BaseColor.png"], ["Barrel", "Lantern_Wall"])

    def test_all_model_discovery_and_usage_counts(self):
        with tempfile.TemporaryDirectory() as td:
            zpath = Path(td) / "props.zip"
            with zipfile.ZipFile(zpath, "w") as zf:
                zf.writestr("Exports/glTF/A.gltf", self._gltf(["MI_Metal"], ["T_Trim_Metal_BaseColor.png"]))
                zf.writestr("Exports/glTF/B.gltf", self._gltf(["MI_Metal", "MI_Cloth"], [
                    "T_Trim_Metal_BaseColor.png", "T_Trim_Cloth_BaseColor.png"]))
                zf.writestr("Exports/glTF/C.gltf", self._gltf(["MI_Cloth"], ["T_Trim_Cloth_BaseColor.png"]))
            result = mod.analyze_all_zip_models(zpath)
            self.assertEqual(result["model_count"], 3)
            self.assertEqual(result["basecolor_usage_counts"]["T_Trim_Metal_BaseColor.png"], 2)
            self.assertEqual(result["basecolor_usage_counts"]["T_Trim_Cloth_BaseColor.png"], 2)


if __name__ == "__main__":
    unittest.main()
