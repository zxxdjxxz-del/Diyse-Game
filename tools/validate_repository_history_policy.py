#!/usr/bin/env python3
"""Enforce the repository policy that superseded project history lives in Git history."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEGACY_ARCHIVE_SEGMENT = "99_" + "ARCHIVE"
TEXT_EXTENSIONS = {
    ".md", ".txt", ".json", ".py", ".gd", ".yml", ".yaml", ".cfg",
    ".tres", ".tscn", ".toml", ".ini",
}


def main() -> int:
    errors: list[str] = []

    archive_root = ROOT / "docs" / LEGACY_ARCHIVE_SEGMENT
    if archive_root.exists():
        errors.append(
            f"{archive_root.relative_to(ROOT)} exists; superseded project history belongs in Git history"
        )

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if LEGACY_ARCHIVE_SEGMENT in text:
            errors.append(
                f"{path.relative_to(ROOT)} still references the removed dedicated history archive"
            )

    if errors:
        print("Repository history policy validation FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository history policy validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
