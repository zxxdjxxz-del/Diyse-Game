import importlib.util
import io
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from PIL import Image

MODULE_PATH = Path(__file__).resolve().parents[1] / 'zip_intake_engine.py'
spec = importlib.util.spec_from_file_location('diyse_zip_intake', MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
assert spec.loader is not None
spec.loader.exec_module(mod)


def png_bytes(size=(32, 32), rgba=False, value=120):
    mode = 'RGBA' if rgba else 'RGB'
    color = (value, 80, 40, 200) if rgba else (value, 80, 40)
    image = Image.new(mode, size, color)
    buf = io.BytesIO()
    image.save(buf, 'PNG')
    return buf.getvalue()


class ZipIntakeTests(unittest.TestCase):
    def test_path_classification_and_animation_group(self):
        self.assertEqual(mod.classify_path('Metal/Doors/METAL_big.png', '2.zip'), 'metal')
        self.assertEqual(mod.classify_path('Animated extras/Fire/A/ANIM_fire_A_Frame_12.png', '1.zip'), 'fire')
        group, frame = mod.animation_group('Animated extras/Fire/A/ANIM_fire_A_Frame_12.png')
        self.assertTrue(group.endswith('ANIM_fire_A'))
        self.assertEqual(frame, 12)

    def test_archive_scan_and_exact_member_hash_duplicates(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            z1 = root / '1.zip'
            z2 = root / 'Emission.zip'
            shared = png_bytes((64, 64), rgba=True, value=150)
            with zipfile.ZipFile(z1, 'w') as zf:
                zf.writestr('Animated extras/Mistic/C/ANIM_Mistic_C_frame_1.png', shared)
                zf.writestr('Metal/Doors/door.png', png_bytes((32, 64)))
            with zipfile.ZipFile(z2, 'w') as zf:
                zf.writestr('ANIM_Mistic_frame_1.png', shared)
            result = mod.scan_archives([z1, z2], hash_members=True)
            self.assertEqual(result['totals']['archives'], 2)
            self.assertEqual(result['totals']['file_members'], 3)
            self.assertEqual(result['totals']['image_members'], 3)
            self.assertEqual(len(result['duplicate_groups']), 1)
            emission = [row for row in result['members'] if row['archive'] == 'Emission.zip'][0]
            self.assertEqual(emission['category'], 'emission')
            self.assertTrue(emission['has_alpha'])


if __name__ == '__main__':
    unittest.main()
