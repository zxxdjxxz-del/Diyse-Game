import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


shared = load_module('diyse_shared_material_v07', 'shared_material_engine.py')
style = load_module('diyse_material_style_v07', 'material_style_engine.py')


class MaterialFamilyV07Tests(unittest.TestCase):
    def test_material_basecolor_binding_uses_gltf_indices(self):
        gltf = {
            'images': [
                {'uri': 'T_Trim_Cloth_BaseColor.png'},
                {'uri': 'T_Trim_Props_BaseColor.png'},
            ],
            'textures': [
                {'source': 1},
                {'source': 0},
            ],
            'materials': [
                {'name': 'MI_Banner', 'pbrMetallicRoughness': {'baseColorTexture': {'index': 1}}},
                {'name': 'MI_Trim_Props_Vertex', 'pbrMetallicRoughness': {'baseColorTexture': {'index': 0}}},
            ],
        }
        mapping = shared.material_basecolor_dependencies(gltf)
        self.assertEqual(mapping['MI_Banner'], 'T_Trim_Cloth_BaseColor.png')
        self.assertEqual(mapping['MI_Trim_Props_Vertex'], 'T_Trim_Props_BaseColor.png')

    def test_all_four_material_kinds_preserve_dimensions(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            source = root / 'source.png'
            Image.new('RGB', (96, 64), (130, 90, 70)).save(source)
            for kind in ('wood', 'metal', 'prop', 'cloth'):
                output = root / f'{kind}.png'
                style.stylize_material_file(source, output, kind)
                with Image.open(output) as result:
                    self.assertEqual(result.size, (96, 64))

    def test_props_and_cloth_are_not_forced_to_wood_metal_palette(self):
        image = Image.new('RGB', (64, 64), (40, 125, 180))
        prop = style.stylize_material_image(image, 'prop')
        cloth = style.stylize_material_image(image, 'cloth')
        self.assertEqual(prop.size, image.size)
        self.assertEqual(cloth.size, image.size)
        # Hue-preserving families should remain blue-dominant.
        self.assertGreater(prop.getpixel((32, 32))[2], prop.getpixel((32, 32))[0])
        self.assertGreater(cloth.getpixel((32, 32))[2], cloth.getpixel((32, 32))[0])


if __name__ == '__main__':
    unittest.main()
