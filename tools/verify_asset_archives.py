#!/usr/bin/env python3
"""Verify Diyse source archives against the authoritative Markdown manifest.

By default every archive listed in the manifest must be present somewhere under
one of the configured source roots. Use --present-only to validate a partial
staging set without treating absent archives as an error.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path

DEFAULT_MANIFEST = Path(
    "docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/"
    "SOURCE_ARCHIVE_MANIFEST.md"
)
DEFAULT_ROOTS = (
    Path("asset_sources/private_reference"),
    Path("asset_sources/third_party_cc0"),
)
ROW_RE = re.compile(
    r"^\| `(?P<name>[^`]+)` \| (?P<bytes>\d+) \| (?P<files>\d+) \| "
    r"`(?P<sha>[0-9a-fA-F]{64})` \|$"
)


@dataclass(frozen=True)
class ArchiveRecord:
    name: str
    size: int
    member_count: int
    sha256: str


def parse_manifest(path: Path) -> list[ArchiveRecord]:
    records: list[ArchiveRecord] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = ROW_RE.match(line)
        if not match:
            continue
        records.append(
            ArchiveRecord(
                name=match.group("name"),
                size=int(match.group("bytes")),
                member_count=int(match.group("files")),
                sha256=match.group("sha").lower(),
            )
        )
    if not records:
        raise ValueError(f"No archive rows found in manifest: {path}")
    return records


def sha256_file(path: Path, chunk_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def zip_member_count(path: Path) -> int:
    """Return file-member count, excluding explicit directory entries."""
    with zipfile.ZipFile(path) as archive:
        return sum(1 for item in archive.infolist() if not item.is_dir())


def find_candidates(name: str, roots: tuple[Path, ...]) -> list[Path]:
    candidates: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        direct = root / name
        if direct.is_file():
            candidates.append(direct)
        for candidate in root.rglob(name):
            if candidate.is_file() and candidate not in candidates:
                candidates.append(candidate)
    return candidates


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Verify Diyse source ZIPs against SOURCE_ARCHIVE_MANIFEST.md."
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help=f"Manifest path (default: {DEFAULT_MANIFEST})",
    )
    parser.add_argument(
        "--root",
        dest="roots",
        action="append",
        type=Path,
        help=(
            "Archive search root. Repeat to supply multiple roots. Defaults to "
            "asset_sources/private_reference and asset_sources/third_party_cc0."
        ),
    )
    parser.add_argument(
        "--present-only",
        action="store_true",
        help="Validate files that are present; do not fail for missing archives.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    roots = tuple(args.roots) if args.roots else DEFAULT_ROOTS

    try:
        records = parse_manifest(args.manifest)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    verified = 0
    missing = 0
    failures = 0

    print(f"Manifest: {args.manifest}")
    print("Search roots:")
    for root in roots:
        print(f"  - {root}")
    print()

    for record in records:
        candidates = find_candidates(record.name, roots)
        if not candidates:
            missing += 1
            status = "SKIP" if args.present_only else "MISSING"
            print(f"{status:7} {record.name}")
            continue

        if len(candidates) > 1:
            failures += 1
            print(f"DUPLICATE {record.name}")
            for candidate in candidates:
                print(f"          {candidate}")
            continue

        path = candidates[0]
        actual_size = path.stat().st_size
        if actual_size != record.size:
            failures += 1
            print(
                f"BADSIZE {record.name}: expected {record.size}, got {actual_size} "
                f"({path})"
            )
            continue

        try:
            actual_members = zip_member_count(path)
        except (OSError, zipfile.BadZipFile) as exc:
            failures += 1
            print(f"BADZIP  {record.name}: {exc} ({path})")
            continue

        if actual_members != record.member_count:
            failures += 1
            print(
                f"BADCOUNT {record.name}: expected {record.member_count}, "
                f"got {actual_members} ({path})"
            )
            continue

        actual_sha = sha256_file(path)
        if actual_sha != record.sha256:
            failures += 1
            print(
                f"BADHASH {record.name}: expected {record.sha256}, got {actual_sha} "
                f"({path})"
            )
            continue

        verified += 1
        print(f"OK      {record.name}")

    print()
    print(
        f"Verified: {verified} | Missing: {missing} | Failed/duplicate: {failures} "
        f"| Manifest records: {len(records)}"
    )

    if failures:
        return 1
    if missing and not args.present_only:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
