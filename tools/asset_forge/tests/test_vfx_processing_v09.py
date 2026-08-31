import importlib.util
import io
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

import numpy as np
from PIL import Image

MODULE_PATH = Path(__file__).resolve().parents[1] / 'vfx_processing_engine.py'
spec = importlib.util.spec_from_file_location('diyse_vfx_processing', MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
assert spec.loader is not None
spec.loader.exec_module(mod)


class VfxProcessingTests(unittest.TestCase):
    def test_grid_parse_and_exact_roundtrip_rgba(self):
        image = Image.new('RGBA', (64, 32))
        arr = np.zeros((32, 64, 4), dtype=np.uint8)
        arr[..., 0] = np.arange(64, dtype=np.uint8)[None, :]
        arr[..., 1] = np.arange(32, dtype=np.uint8)[:, None]
        arr[..., 3] = 255
        image = Image.fromarray(arr, 'RGBA')
        self.assertEqual(mod.parse_grid_from_name('fire_01_8x4.png'), (8, 4))
        qa = mod.grid_roundtrip_qa(image, 8, 4)
        self.assertTrue(qa['exact'])
        self.assertEqual(qa['frame_count'], 32)
        self.assertEqual(qa['max_channel_difference'], 0)

    def test_particle_pairing(self):
        result = mod.pair_particles([
            'bundle/particles/opague/fire_01.png',
            'bundle/particles/alpha/fire_01_a.png',
            'bundle/particles/alpha/smoke_07_strong_a.png',
        ])
        self.assertIn('fire_01', result['matched'])
        self.assertEqual(result['unmatched_color'], [])
        self.assertEqual(len(result['unmatched_alpha']), 1)

    def test_zip_inspection_ignores_metadata_and_counts_grid(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            archive = root / 'vfx.zip'
            buf = io.BytesIO()
            Image.new('RGBA', (40, 20), (255, 120, 0, 200)).save(buf, 'PNG')
            with zipfile.ZipFile(archive, 'w') as zf:
                zf.writestr('__MACOSX/._noise.png', b'junk')
                zf.writestr('bundle/predrawn/fire_4x2.png', buf.getvalue())
                zf.writestr('bundle/particles/opague/fire_01.png', buf.getvalue())
                zf.writestr('bundle/particles/alpha/fire_01_a.png', buf.getvalue())
            result = mod.inspect_vfx_zip(archive)
            self.assertEqual(result['image_members'], 3)
            self.assertEqual(result['grid_sheets'], 1)
            self.assertEqual(result['grid_frames'], 8)
            self.assertTrue(result['all_grid_roundtrips_exact'])
            self.assertEqual(result['matched_particle_pairs'], 1)


if __name__ == '__main__':
    unittest.main()
