#!/usr/bin/env python3
"""Validate the live Diyse repository authority graph and documentation routes."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

EXPECTED_DOMAIN_DIRS = (
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
)

REQUIRED_AUTHORITY_FILES = (
    "README.md",
    "AGENTS.md",
    "docs/README.md",
    "docs/00_MASTER_CONTROL/DIYSE_MASTER_INDEX.md",
    "docs/00_MASTER_CONTROL/AUTHORITY_AND_CHANGE_CONTROL.md",
    "docs/00_MASTER_CONTROL/CANON_QUICK_REFERENCE.md",
    "docs/00_MASTER_CONTROL/CLASS_TERMINOLOGY_CURRENT.md",
    "docs/00_MASTER_CONTROL/FACE_TERMINOLOGY_CURRENT.md",
    "docs/00_MASTER_CONTROL/TERMINOLOGY_GLOSSARY.md",
    "docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_AUTHORITY_PRECEDENCE.md",
    "docs/13_UI_AND_IMPLEMENTATION/CURRENT_RUNTIME_IMPLEMENTATION_STATUS.md",
    "docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md",
    "docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/VALIDATION_AND_TEST_GATES.md",
    "docs/16_BALANCE_AND_TESTING/TRUE_BATTLES/TRUE_BATTLE_TEST_PROTOCOL.md",
)

REQUIRED_DOMAIN_READMES = tuple(
    f"docs/{domain}/README.md"
    for domain in EXPECTED_DOMAIN_DIRS
    if domain not in {"00_MASTER_CONTROL", "90_WORKING"}
)

ALLOWED_WORKING_TOP_LEVEL = {
    "README.md",
    "ACTIVE_WORK_QUEUE.md",
    "AREA_AND_ROUTE_LAYOUT_PRODUCTION_WORKING.md",
    "PLAYABLE_AREA_INVENTORY_WORKING.md",
    "AREA_LAYOUTS",
}

ROOT_ROUTE_REQUIREMENTS = {
    "README.md": (
        "docs/00_MASTER_CONTROL/DIYSE_MASTER_INDEX.md",
        "docs/00_MASTER_CONTROL/AUTHORITY_AND_CHANGE_CONTROL.md",
        "docs/00_MASTER_CONTROL/CANON_QUICK_REFERENCE.md",
        "docs/13_UI_AND_IMPLEMENTATION/CURRENT_RUNTIME_IMPLEMENTATION_STATUS.md",
        "docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md",
    ),
    "AGENTS.md": (
        "docs/00_MASTER_CONTROL/DIYSE_MASTER_INDEX.md",
        "docs/00_MASTER_CONTROL/AUTHORITY_AND_CHANGE_CONTROL.md",
        "docs/00_MASTER_CONTROL/CANON_QUICK_REFERENCE.md",
        "docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_AUTHORITY_PRECEDENCE.md",
        "docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md",
    ),
}

MASTER_DOMAIN_HEADING_RE = re.compile(r"^### (?P<num>\d{2})_(?P<name>[A-Z0-9_]+)\s*$", re.MULTILINE)
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\((?P<target>[^)]+)\)")


def _normalize_link_target(raw: str) -> str | None:
    target = raw.strip().split()[0].strip("<>")
    if not target:
        return None
    if target.startswith(("#", "http://", "https://", "mailto:", "user://", "res://")):
        return None
    target = unquote(target).split("#", 1)[0].split("?", 1)[0]
    return target or None


def _resolve_link(source: Path, target: str) -> Path:
    if target.startswith("/"):
        return ROOT / target.lstrip("/")
    if target.startswith(("docs/", "game/", "tests/", "tools/", "asset_sources/", ".github/")):
        return ROOT / target
    return (source.parent / target).resolve()


def _validate_markdown_links(errors: list[str]) -> None:
    sources = [ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "docs" / "README.md"]
    sources.extend(sorted(DOCS.rglob("*.md")))

    for source in sources:
        if not source.is_file():
            continue
        text = source.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = _normalize_link_target(match.group("target"))
            if target is None:
                continue
            resolved = _resolve_link(source, target)
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"{source.relative_to(ROOT)}: documentation link escapes repository: {target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"{source.relative_to(ROOT)}: dangling documentation link: {target}"
                )


def main() -> int:
    errors: list[str] = []

    actual_domains = {
        path.name
        for path in DOCS.iterdir()
        if path.is_dir()
    }
    expected_domains = set(EXPECTED_DOMAIN_DIRS)
    missing_domains = sorted(expected_domains - actual_domains)
    unexpected_domains = sorted(actual_domains - expected_domains)

    if missing_domains:
        errors.append(f"missing authority domain directories: {', '.join(missing_domains)}")
    if unexpected_domains:
        errors.append(
            "unexpected top-level docs directories outside the current authority graph: "
            + ", ".join(unexpected_domains)
        )

    for rel in REQUIRED_AUTHORITY_FILES + REQUIRED_DOMAIN_READMES:
        if not (ROOT / rel).is_file():
            errors.append(f"required authority file missing: {rel}")

    working = DOCS / "90_WORKING"
    if working.is_dir():
        actual_working = {path.name for path in working.iterdir()}
        unexpected_working = sorted(actual_working - ALLOWED_WORKING_TOP_LEVEL)
        missing_working = sorted(ALLOWED_WORKING_TOP_LEVEL - actual_working)
        if unexpected_working:
            errors.append(
                "unexpected 90_WORKING top-level surface: " + ", ".join(unexpected_working)
            )
        if missing_working:
            errors.append(
                "required active 90_WORKING surface missing: " + ", ".join(missing_working)
            )

    for rel, required_routes in ROOT_ROUTE_REQUIREMENTS.items():
        path = ROOT / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for route in required_routes:
            if route not in text:
                errors.append(f"{rel}: required authority route missing: {route}")
            elif not (ROOT / route).exists():
                errors.append(f"{rel}: required authority route target missing: {route}")

    master = ROOT / "docs/00_MASTER_CONTROL/DIYSE_MASTER_INDEX.md"
    if master.is_file():
        text = master.read_text(encoding="utf-8")
        headings = [
            f"{m.group('num')}_{m.group('name')}"
            for m in MASTER_DOMAIN_HEADING_RE.finditer(text)
        ]
        expected_numbered = list(EXPECTED_DOMAIN_DIRS[1:17])
        if headings != expected_numbered:
            errors.append(
                "DIYSE_MASTER_INDEX.md numbered domain headings do not exactly match "
                f"the live 00-16 owner set: {headings}"
            )

    _validate_markdown_links(errors)

    if errors:
        print("Repository authority integrity validation FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository authority integrity validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
