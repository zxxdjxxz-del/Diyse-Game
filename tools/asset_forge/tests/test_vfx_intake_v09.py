import importlib.util
import io
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from PIL import Image

MODULE_PATH = Path(__file__).resolve().parents[1] / 'vfx_intake_engine.py'
spec = importlib.util.spec_from_file_location('diyse_vfx_intake', MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
assert spec.loader is not None
spec.loader.exec_module(mod)


def png_bytes(size=(64, 64), rgba=True, value=160):
    mode = 'RGBA' if rgba else 'RGB'
    color = (value, 90, 40, 220) if rgba else (value, 90, 40)
    image = Image.new(mode, size, color)
    buf = io.BytesIO()
    image.save(buf, 'PNG')
    return buf.getvalue()


class VfxIntakeTests(unittest.TestCase):
    def test_grid_role_kind_and_metadata_filter(self):
        self.assertEqual(mod.spritesheet_grid('predrawn/fire_ring_6x5.png'), (6, 5, 30))
        self.assertEqual(mod.asset_role('bundle/flipbooks/fire_01_8x8.tga'), 'flipbook')
        self.assertEqual(mod.asset_role('bundle/particles/alpha/spark_01_a.png'), 'particle_alpha')
        self.assertEqual(mod.vfx_kind('bundle/predrawn/electric_ring_6x5.png'), 'energy')
        self.assertTrue(mod.is_metadata_member('__MACOSX/bundle/._thing.png'))
        self.assertTrue(mod.is_metadata_member('bundle/.DS_Store'))

    def test_scan_pairs_and_source_frame_totals(self):
        with tempfile.TemporaryDirectory() as td:
            zpath = Path(td) / 'vfx.zip'
            with zipfile.ZipFile(zpath, 'w') as zf:
                zf.writestr('__MACOSX/bundle/._junk.png', b'junk')
                zf.writestr('bundle/predrawn/explosion_6x5.png', png_bytes((120, 100)))
                zf.writestr('bundle/particles/opague/spark_01.png', png_bytes())
                zf.writestr('bundle/particles/alpha/spark_01_a.png', png_bytes(value=90))
                zf.writestr('bundle/particles/alpha/smoke_07_strong_a.png', png_bytes(value=70))
            result = mod.scan_vfx_zip(zpath, hash_members=True)
            self.assertEqual(result['skipped_metadata_members'], 1)
            self.assertEqual(result['image_members'], 4)
            self.assertEqual(result['spritesheet_assets'], 1)
            self.assertEqual(result['spritesheet_frames'], 30)
            self.assertEqual(result['particle_pairs']['matched_color_alpha_pairs'], 1)
            self.assertEqual(result['particle_pairs']['alpha_only'], ['smoke_07_strong'])


if __name__ == '__main__':
    unittest.main()
