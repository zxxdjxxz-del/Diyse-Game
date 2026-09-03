import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


stager = load_module("diyse_validation_source_stager", "validation_source_stager.py")


class ValidationSourceStagerTests(unittest.TestCase):
    def write_manifest(self, root: Path, *, primary=None, companions=None, expected=None) -> Path:
        jobs = []
        for i in range(12):
            p = list(primary if i == 0 and primary is not None else [f"primary_{i}.tga"])
            c = list(companions if i == 0 and companions is not None else [])
            job = {
                "id": f"JOB_{i:02d}",
                "family": "stone" if i < 6 else "foliage",
                "primary": p,
                "companions": c,
            }
            if i == 0 and expected is not None:
                job["expected_primary_frames"] = expected
            jobs.append(job)
        path = root / "manifest.json"
        path.write_text(json.dumps({
            "id": "TEST_BATCH",
            "stop_after_jobs": 12,
            "jobs": jobs,
        }), encoding="utf-8")
        return path

    def populate_all_required(self, source: Path, manifest: dict) -> None:
        source.mkdir(parents=True, exist_ok=True)
        for job in manifest["jobs"]:
            for name in [*job.get("primary", []), *job.get("companions", [])]:
                (source / name).write_bytes(name.encode("utf-8"))

    def test_real_manifest_is_bounded_to_six_stone_six_foliage(self):
        manifest = stager.load_manifest(ROOT / "validation_texture_batch_v1.json")
        self.assertEqual(len(manifest["jobs"]), 12)
        self.assertEqual(sum(j["family"] == "stone" for j in manifest["jobs"]), 6)
        self.assertEqual(sum(j["family"] == "foliage" for j in manifest["jobs"]), 6)
        self.assertEqual(manifest["stop_after_jobs"], 12)

    def test_missing_source_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            manifest_path = self.write_manifest(root)
            manifest = stager.load_manifest(manifest_path)
            source = root / "raw"
            source.mkdir()
            result = stager.resolve_manifest(manifest, source)
            self.assertFalse(result["valid"])
            self.assertTrue(any("missing primary_0.tga" in issue for issue in result["issues"]))

    def test_duplicate_basename_is_ambiguous(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            manifest_path = self.write_manifest(root)
            manifest = stager.load_manifest(manifest_path)
            source = root / "raw"
            self.populate_all_required(source, manifest)
            duplicate_dir = source / "duplicate"
            duplicate_dir.mkdir()
            (duplicate_dir / "primary_0.tga").write_bytes(b"other")
            result = stager.resolve_manifest(manifest, source)
            self.assertFalse(result["valid"])
            self.assertTrue(any("ambiguous basename primary_0.tga" in issue for issue in result["issues"]))

    def test_sequence_count_is_validated_from_manifest(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            path = self.write_manifest(root, primary=["a.tga", "b.tga"], expected=3)
            with self.assertRaises(ValueError):
                stager.load_manifest(path)

    def test_valid_resolution_stages_without_modifying_source(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            manifest_path = self.write_manifest(root, companions=["light.tga"])
            manifest = stager.load_manifest(manifest_path)
            source = root / "raw"
            self.populate_all_required(source, manifest)
            before = {p.name: p.read_bytes() for p in source.iterdir() if p.is_file()}
            resolution = stager.resolve_manifest(manifest, source)
            self.assertTrue(resolution["valid"])
            workspace = root / "staged"
            staged = stager.stage_resolution(resolution, workspace)
            self.assertEqual(staged["status"], "READY_FOR_ASSET_FORGE_PROCESSING")
            self.assertEqual(staged["job_count"], 12)
            self.assertTrue((workspace / "STAGING_MANIFEST.json").exists())
            after = {p.name: p.read_bytes() for p in source.iterdir() if p.is_file()}
            self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
