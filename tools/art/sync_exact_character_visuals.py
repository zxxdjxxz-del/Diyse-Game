#!/usr/bin/env python3
import base64
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STAGE = ROOT / ".binary_sync" / "2026-09-22"
MANIFEST = ROOT / "asset_sources/characters/current/APPROVED_SOURCE_MANIFEST.json"
README = ROOT / "asset_sources/characters/current/README.md"

data = json.loads(MANIFEST.read_text(encoding="utf-8"))
processed = []

for key, meta in data["characters"].items():
    parts_dir = STAGE / key / "parts"
    parts = sorted(parts_dir.glob("*.b64part"))
    if not parts:
        raise SystemExit(f"Missing staged payload for {key}")

    encoded = "".join(p.read_text(encoding="ascii") for p in parts)
    raw = base64.b64decode("".join(encoded.split()), validate=True)

    actual_sha256 = hashlib.sha256(raw).hexdigest()
    expected_sha256 = meta["sha256"]
    if actual_sha256 != expected_sha256:
        raise SystemExit(f"{key}: SHA-256 mismatch: {actual_sha256} != {expected_sha256}")
    if len(raw) != meta["size_bytes"]:
        raise SystemExit(f"{key}: size mismatch: {len(raw)} != {meta['size_bytes']}")

    destination = ROOT / meta["expected_repository_path"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(raw)
    meta["exact_binary_sync"] = "complete"
    processed.append(key)

if len(processed) != len(data["characters"]):
    raise SystemExit("Not every registered character source was reconstructed")

MANIFEST.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

readme = README.read_text(encoding="utf-8")
readme = readme.replace("**Exact-binary sync state:** PENDING.", "**Exact-binary sync state:** COMPLETE.")
README.write_text(readme, encoding="utf-8")

shutil.rmtree(STAGE)
binary_root = ROOT / ".binary_sync"
if binary_root.exists() and not any(binary_root.iterdir()):
    binary_root.rmdir()

print("Synced and verified: " + ", ".join(processed))
