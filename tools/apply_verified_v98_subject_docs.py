#!/usr/bin/env python3
"""Verify the exact v98 transition package, then delegate to the migration installer."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import subprocess
import sys

EXPECTED_SHA256 = "835f63bec93d4cd65be6604b6230bd3eb1ff7d18e7d2bad5b4d3d8539d5da79a"
EXPECTED_NAME = "DIYSE_CANON_REORGANIZATION_v98_REPOSITORY_TRANSITION_AUDIT.zip"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zip_path", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    package = args.zip_path.resolve()
    if not package.is_file():
        print(f"ERROR: package not found: {package}", file=sys.stderr)
        return 1

    actual = sha256(package)
    if actual != EXPECTED_SHA256:
        print("ERROR: v98 payload checksum mismatch; refusing migration.", file=sys.stderr)
        print(f"Expected: {EXPECTED_SHA256}", file=sys.stderr)
        print(f"Actual:   {actual}", file=sys.stderr)
        return 2

    if package.name != EXPECTED_NAME:
        print(f"NOTE: checksum is exact, but filename differs from canonical {EXPECTED_NAME}.")

    installer = Path(__file__).with_name("apply_v98_subject_docs.py")
    command = [sys.executable, str(installer), str(package)]
    if args.apply:
        command.append("--apply")

    print("V98 PAYLOAD VERIFIED — delegating to subject-documentation migration.")
    return subprocess.call(command)


if __name__ == "__main__":
    raise SystemExit(main())
