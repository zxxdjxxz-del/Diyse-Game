#!/usr/bin/env python3
"""Install the Diyse v98 subject-folder canon package into this repository.

This tool is intentionally repository-local and deterministic. It replaces only the
legacy documentation layer plus the two root routing files. Runtime/build/test
surfaces are never deleted by this script.

Usage:
    python tools/apply_v98_subject_docs.py /path/to/DIYSE_CANON_REORGANIZATION_v98_REPOSITORY_TRANSITION_AUDIT.zip
    python tools/apply_v98_subject_docs.py /path/to/package.zip --apply

Without --apply the script performs a validation/dry-run only.
"""

from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import shutil
import sys
import tempfile
import zipfile

PACKAGE_DIR = "DIYSE_CANON_REORGANIZATION_v98"
SUBJECT_DIRS = [
    "00_MASTER_CONTROL",
    "01_CHARACTERS",
    "02_STORY",
    "03_DIALOGUE",
    "04_WORLD_AND_LORE",
    "05_BATTLE_SYSTEM",
    "06_CLASSES_AND_ABILITIES",
    "07_CARDS",
    "08_ITEMS_AND_EQUIPMENT",
    "09_ENEMIES_AND_ENCOUNTERS",
    "10_PROGRESSION_AND_EXP",
    "11_QUESTS",
    "12_ECONOMY_AND_REWARDS",
    "13_UI_AND_IMPLEMENTATION",
    "14_ART_AND_VISUALS",
    "15_AUDIO_AND_MUSIC",
    "16_BALANCE_AND_TESTING",
    "90_WORKING",
    "99_ARCHIVE",
]
ROOT_DOC_FILES = ["README.md", "PACKAGE_MANIFEST.json"]
TRANSPORT_ONLY_PREFIX = "V9"
RUNTIME_REQUIRED = [
    ".github",
    ".gitignore",
    "project.godot",
    "export_presets.cfg",
    "game",
    "tests",
    "tools",
]
ROOT_README_SOURCE = Path("90_WORKING/GITHUB_TRANSITION_STAGING/README_PROPOSED.md")
ROOT_AGENTS_SOURCE = Path("90_WORKING/GITHUB_TRANSITION_STAGING/AGENTS_PROPOSED.md")
REQUIRED_AUTHORITY_PATHS = [
    Path("00_MASTER_CONTROL/CURRENT_CANON_STATUS.md"),
    Path("00_MASTER_CONTROL/AUTHORITY_AND_CHANGE_CONTROL.md"),
    Path("00_MASTER_CONTROL/CANON_QUICK_REFERENCE.md"),
    Path("13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_AUTHORITY_PRECEDENCE.md"),
    Path("13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md"),
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def find_repo_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "project.godot").is_file() and (candidate / "game").is_dir():
            return candidate
    raise RuntimeError("Could not locate Diyse repository root (project.godot + game/ required).")


def validate_runtime(repo: Path) -> None:
    missing = [name for name in RUNTIME_REQUIRED if not (repo / name).exists()]
    if missing:
        raise RuntimeError("Required runtime/build surfaces are missing: " + ", ".join(missing))


def safe_extract(zf: zipfile.ZipFile, destination: Path) -> None:
    root = destination.resolve()
    for member in zf.infolist():
        target = (destination / member.filename).resolve()
        if root not in target.parents and target != root:
            raise RuntimeError(f"Unsafe ZIP member path: {member.filename}")
    zf.extractall(destination)


def validate_package(package: Path) -> tuple[int, int]:
    missing_dirs = [name for name in SUBJECT_DIRS if not (package / name).is_dir()]
    if missing_dirs:
        raise RuntimeError("Package is missing subject directories: " + ", ".join(missing_dirs))

    missing_files = [name for name in ROOT_DOC_FILES if not (package / name).is_file()]
    if missing_files:
        raise RuntimeError("Package is missing required root documentation files: " + ", ".join(missing_files))

    for rel in REQUIRED_AUTHORITY_PATHS:
        if not (package / rel).is_file():
            raise RuntimeError(f"Required authority file is missing: {rel}")

    for rel in (ROOT_README_SOURCE, ROOT_AGENTS_SOURCE):
        if not (package / rel).is_file():
            raise RuntimeError(f"Required staged root router is missing: {rel}")

    markdown = sum(1 for p in package.rglob("*.md") if p.is_file())
    total_files = sum(1 for p in package.rglob("*") if p.is_file())
    return markdown, total_files


def install(package: Path, repo: Path) -> None:
    docs = repo / "docs"
    staging = repo / ".v98_docs_staging"

    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir()

    for dirname in SUBJECT_DIRS:
        shutil.copytree(package / dirname, staging / dirname)

    for filename in ROOT_DOC_FILES:
        shutil.copy2(package / filename, staging / filename)

    # Version update summaries are package transport/history artifacts, not active
    # GitHub documentation-root authority. They are intentionally not copied.
    for child in staging.iterdir():
        if child.is_file() and child.name.startswith(TRANSPORT_ONLY_PREFIX) and child.name.endswith("_UPDATE_SUMMARY.md"):
            child.unlink()

    # Replace root routing documents from the v98 staged proposals.
    root_readme = (package / ROOT_README_SOURCE).read_text(encoding="utf-8")
    root_agents = (package / ROOT_AGENTS_SOURCE).read_text(encoding="utf-8")

    if docs.exists():
        shutil.rmtree(docs)
    staging.rename(docs)
    (repo / "README.md").write_text(root_readme, encoding="utf-8")
    (repo / "AGENTS.md").write_text(root_agents, encoding="utf-8")


def validate_installed(repo: Path) -> None:
    docs = repo / "docs"
    for dirname in SUBJECT_DIRS:
        if not (docs / dirname).is_dir():
            raise RuntimeError(f"Installed docs missing subject directory: {dirname}")
    for rel in REQUIRED_AUTHORITY_PATHS:
        if not (docs / rel).is_file():
            raise RuntimeError(f"Installed docs missing required authority path: {rel}")

    readme = (repo / "README.md").read_text(encoding="utf-8")
    agents = (repo / "AGENTS.md").read_text(encoding="utf-8")
    forbidden = "Exactly 8 automatic Mastery Points"
    if forbidden in readme or forbidden in agents:
        raise RuntimeError("Stale 8-Mastery-Point root guidance survived migration.")

    validate_runtime(repo)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zip_path", type=Path, help="v98 repository-transition ZIP")
    parser.add_argument("--apply", action="store_true", help="actually replace docs/ and root routing files")
    args = parser.parse_args()

    zip_path = args.zip_path.resolve()
    if not zip_path.is_file():
        raise RuntimeError(f"ZIP not found: {zip_path}")

    repo = find_repo_root(Path.cwd())
    validate_runtime(repo)

    digest = sha256(zip_path)
    print(f"Repository: {repo}")
    print(f"Package:    {zip_path}")
    print(f"SHA-256:   {digest}")

    with tempfile.TemporaryDirectory(prefix="diyse_v98_") as td:
        temp = Path(td)
        with zipfile.ZipFile(zip_path) as zf:
            if zf.testzip() is not None:
                raise RuntimeError("ZIP integrity check failed.")
            safe_extract(zf, temp)

        package = temp / PACKAGE_DIR
        if not package.is_dir():
            raise RuntimeError(f"Expected package root not found: {PACKAGE_DIR}")

        markdown, total_files = validate_package(package)
        print(f"Validated package: {markdown} Markdown files / {total_files} total files")

        if not args.apply:
            print("DRY RUN PASS — no repository files changed. Re-run with --apply to install.")
            return 0

        install(package, repo)
        validate_installed(repo)

    print("APPLY PASS — v98 subject-folder documentation installed; runtime/build/test surfaces preserved.")
    print("Next: inspect git diff, run stale-reference scans, then run Godot/Android validation gates.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
