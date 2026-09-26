#!/usr/bin/env python3
"""Validate canonical DIYSE story/dialogue authority naming.

This is intentionally a structural guard, not a canon-content validator.
It prevents legacy workflow-state filenames and scene-ID drift from re-entering
live authority after the September 26, 2026 naming migration.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STORY_ROOT = ROOT / "docs/02_STORY/CHAPTERS"
PROD_ROOT = ROOT / "docs/03_DIALOGUE/PRODUCTION"
DIALOGUE_ROOT = ROOT / "docs/03_DIALOGUE"

CHAPTER_DIR_RE = re.compile(r"^CHAPTER_(\d{2})$")
B_DIALOGUE_RE = re.compile(
    r"^CH(?P<chapter>\d{2})_B(?P<beat>\d{2})_(?P<name>[A-Z0-9_]+)_DIALOGUE\.md$"
)
B_TARGET_RE = re.compile(
    r"^CH(?P<chapter>\d{2})_B(?P<beat>\d{2})_(?P<name>[A-Z0-9_]+)_REHEARSAL_TARGET\.md$"
)
B_SPEC_RE = re.compile(
    r"^CH(?P<chapter>\d{2})_B(?P<beat>\d{2})_(?P<name>[A-Z0-9_]+)_SPEC\.json$"
)
C_DIALOGUE_RE = re.compile(r"^C(?P<scene>\d{2})_(?P<name>[A-Z0-9_]+)_DIALOGUE\.md$")
C_SPEC_RE = re.compile(r"^C(?P<scene>\d{2})_(?P<name>[A-Z0-9_]+)_SPEC\.json$")
STORY_B_RE = re.compile(
    r"^CH\d{2}_B\d{2}(?:_TO_B\d{2})?_[A-Z0-9_]+_(?:STORY_SUPPORT|LOCK)\.md$"
)
STORY_C_RE = re.compile(r"^CH\d{2}_C\d{2}_[A-Z0-9_]+_STORY_SUPPORT\.md$")

LEGACY_PRODUCTION_TOKENS = (
    "REHEARSAL_FIRST",
    "NATURAL_TURN",
    "_WORKING",
    "_CURRENT",
    "_FINAL",
)
LEGACY_STORY_TOKENS = (
    "_WORKING",
    "_CORRECTION",
    "_REVISION",
    "_DRAFT_",
    "BRIARHIDE",
)


def _contiguous(values: set[int]) -> bool:
    if not values:
        return True
    return values == set(range(1, max(values) + 1))


def _scene_id(path: Path, errors: list[str]) -> str | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None
    value = data.get("scene_id")
    if not isinstance(value, str) or not value:
        errors.append(f"{path.relative_to(ROOT)}: missing scene_id")
        return None
    return value


def validate_production(errors: list[str]) -> None:
    character_life_dialogue: dict[int, Path] = {}

    for chapter_dir in sorted(PROD_ROOT.iterdir()):
        if not chapter_dir.is_dir():
            continue
        match = CHAPTER_DIR_RE.fullmatch(chapter_dir.name)
        if not match:
            continue
        chapter = match.group(1)
        dialogue_beats: set[int] = set()
        spec_beats: set[int] = set()
        target_beats: set[int] = set()

        for path in sorted(chapter_dir.iterdir()):
            if not path.is_file():
                continue
            name = path.name

            if any(token in name for token in LEGACY_PRODUCTION_TOKENS) or re.match(
                r"^(?:BEAT_|P\d{2}_|H\d{2}_)", name
            ) or re.search(r"_DRAFT_[A-Z0-9]+", name):
                errors.append(f"{path.relative_to(ROOT)}: legacy/mutable production filename")

            if "DIALOGUE_MANUSCRIPT" in name and name != f"CHAPTER_{chapter}_DIALOGUE_MANUSCRIPT.md":
                errors.append(
                    f"{path.relative_to(ROOT)}: combined manuscript must be "
                    f"CHAPTER_{chapter}_DIALOGUE_MANUSCRIPT.md"
                )

            m = B_DIALOGUE_RE.fullmatch(name)
            if m:
                if m.group("chapter") != chapter:
                    errors.append(f"{path.relative_to(ROOT)}: chapter prefix/folder mismatch")
                dialogue_beats.add(int(m.group("beat")))
                continue

            m = B_TARGET_RE.fullmatch(name)
            if m:
                if m.group("chapter") != chapter:
                    errors.append(f"{path.relative_to(ROOT)}: chapter prefix/folder mismatch")
                target_beats.add(int(m.group("beat")))
                continue

            m = B_SPEC_RE.fullmatch(name)
            if m:
                if m.group("chapter") != chapter:
                    errors.append(f"{path.relative_to(ROOT)}: chapter prefix/folder mismatch")
                spec_beats.add(int(m.group("beat")))
                expected = name.removesuffix("_SPEC.json")
                actual = _scene_id(path, errors)
                if actual is not None and actual != expected:
                    errors.append(
                        f"{path.relative_to(ROOT)}: scene_id {actual!r} != filename identity {expected!r}"
                    )
                continue

            m = C_DIALOGUE_RE.fullmatch(name)
            if m:
                scene = int(m.group("scene"))
                if scene in character_life_dialogue:
                    errors.append(
                        f"{path.relative_to(ROOT)}: duplicate C{scene:02d}; also "
                        f"{character_life_dialogue[scene].relative_to(ROOT)}"
                    )
                else:
                    character_life_dialogue[scene] = path
                continue

            m = C_SPEC_RE.fullmatch(name)
            if m:
                scene = int(m.group("scene"))
                expected = f"CH{chapter}_C{scene:02d}_{m.group('name')}"
                actual = _scene_id(path, errors)
                if actual is not None and actual != expected:
                    errors.append(
                        f"{path.relative_to(ROOT)}: scene_id {actual!r} != filename identity {expected!r}"
                    )
                continue

            if re.match(r"^CH\d{2}_B\d{2}_", name):
                errors.append(f"{path.relative_to(ROOT)}: malformed canonical beat filename")
            if re.match(r"^C\d{2}_", name):
                errors.append(f"{path.relative_to(ROOT)}: malformed canonical Character-Life filename")

        if not _contiguous(dialogue_beats):
            errors.append(
                f"{chapter_dir.relative_to(ROOT)}: approved dialogue beat IDs are not contiguous: "
                f"{sorted(dialogue_beats)}"
            )
        if not _contiguous(spec_beats):
            errors.append(
                f"{chapter_dir.relative_to(ROOT)}: beat spec IDs are not contiguous: "
                f"{sorted(spec_beats)}"
            )
        if target_beats and min(target_beats) < 1:
            errors.append(f"{chapter_dir.relative_to(ROOT)}: invalid rehearsal-target beat ID")

    c_ids = set(character_life_dialogue)
    if not _contiguous(c_ids):
        errors.append(f"Character-Life dialogue IDs are not contiguous: {sorted(c_ids)}")


def validate_story_root(errors: list[str]) -> None:
    for path in sorted(STORY_ROOT.iterdir()):
        if not path.is_file():
            continue
        name = path.name
        if any(token in name for token in LEGACY_STORY_TOKENS):
            errors.append(f"{path.relative_to(ROOT)}: mutable/retired story filename in live root")
        if re.match(r"^CHAPTER_\d{2}_BEAT_\d{1,2}_", name):
            errors.append(
                f"{path.relative_to(ROOT)}: beat-specific support must use CH##_B##_... naming"
            )
        if re.match(r"^CH\d{2}_B\d{2}", name) and not STORY_B_RE.fullmatch(name):
            errors.append(f"{path.relative_to(ROOT)}: malformed beat-specific story support/lock")
        if re.match(r"^CH\d{2}_C\d{2}", name) and not STORY_C_RE.fullmatch(name):
            errors.append(f"{path.relative_to(ROOT)}: malformed Character-Life story support")


def validate_cross_chapter_names(errors: list[str]) -> None:
    for directory in (DIALOGUE_ROOT, PROD_ROOT):
        for path in directory.iterdir():
            if not path.is_file():
                continue
            name = path.name
            if name.startswith("CHAPTER_0_3") or name.startswith("CHAPTER_00_03"):
                errors.append(
                    f"{path.relative_to(ROOT)}: cross-chapter files use CHAPTERS_00_03_..."
                )

    required = [
        PROD_ROOT / "CHAPTERS_00_03_DIALOGUE_SYNC_MANIFEST.md",
        PROD_ROOT / "CHAPTERS_00_03_FULL_SOURCE_CLOSURE_2026-09-13.md",
        DIALOGUE_ROOT / "CHAPTERS_00_03_NATURAL_TURN_RHYTHM_AUDIT_TRACKER.md",
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"{path.relative_to(ROOT)}: required canonical cross-chapter file missing")


def main() -> int:
    errors: list[str] = []
    validate_production(errors)
    validate_story_root(errors)
    validate_cross_chapter_names(errors)

    if errors:
        print("Authority naming validation FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Authority naming validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
