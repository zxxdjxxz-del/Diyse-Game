#!/usr/bin/env python3
"""Reject superseded combat/progression vocabulary in current mechanical authority docs."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SCANNED_ROOTS = tuple(
    ROOT / "docs" / name
    for name in (
        "00_MASTER_CONTROL",
        "05_BATTLE_SYSTEM",
        "06_CLASSES_AND_ABILITIES",
        "07_CARDS",
        "08_ITEMS_AND_EQUIPMENT",
        "09_ENEMIES_AND_ENCOUNTERS",
        "10_PROGRESSION_AND_EXP",
        "13_UI_AND_IMPLEMENTATION",
        "16_BALANCE_AND_TESTING",
    )
)

# These files describe current implementation compatibility/debt and may need to name
# a mismatched runtime field to explain what still has to be migrated.
EXEMPT_PATHS = {
    "docs/13_UI_AND_IMPLEMENTATION/CURRENT_RUNTIME_IMPLEMENTATION_STATUS.md",
    "docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md",
    "docs/13_UI_AND_IMPLEMENTATION/SAVE_DATA.md",
}

RULES = (
    ("Base Hit", re.compile(r"\bBase Hit\b", re.IGNORECASE)),
    ("Evasion stat", re.compile(r"\bEvasion\b", re.IGNORECASE)),
    ("Status Resistance stat", re.compile(r"\bStatus Resistance\b", re.IGNORECASE)),
    ("Burn status", re.compile(r"\bBurn\b")),
    ("Freeze status", re.compile(r"\bFreeze\b")),
    ("Stun status", re.compile(r"\bStun\b")),
    ("Staggered status", re.compile(r"\bStaggered\b")),
    ("Bleed status", re.compile(r"\bBleed(?:ing)?\b")),
    ("Haste status", re.compile(r"\bHaste\b")),
    ("Doom status", re.compile(r"\bDoom\b")),
    ("ATK stat abbreviation", re.compile(r"\bATK\b")),
    ("Power-scale field", re.compile(r"(?:\bPower\s*:|\b\d+(?:\.\d+)?\s+Power\b|\bPower\s+N/?A\b)", re.IGNORECASE)),
    ("normal-round timing", re.compile(r"\bnormal (?:party )?rounds?\b", re.IGNORECASE)),
    ("Prime-round timing", re.compile(r"\bPrime rounds?\b", re.IGNORECASE)),
    ("round-based combat", re.compile(r"\bround-based\b", re.IGNORECASE)),
    ("fixed Level 70", re.compile(r"\b(?:Lv\.?\s*70|Level\s+70)\b", re.IGNORECASE)),
    ("three Standard Card slots", re.compile(r"\b3 (?:equipped|Standard Card slots?) per character\b", re.IGNORECASE)),
    ("Attack stat modifier", re.compile(r"\bAttack\s*(?:\+|−|-)\s*\d", re.IGNORECASE)),
    ("Attack-derived stat wording", re.compile(r"\bAttack-derived\b|\beffective Attack\b", re.IGNORECASE)),
)

REMOVED_ROUTE_NAMES = (
    "ACTION_POWER_REQUIREMENT.md",
    "BASE_HIT_AND_EVASION.md",
    "GUARD.md",
    "PRIME_ROUND_SEQUENCING.md",
    "TURN_AND_ROUND_RULES.md",
)


def main() -> int:
    errors: list[str] = []

    for root in SCANNED_ROOTS:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            rel = path.relative_to(ROOT).as_posix()
            if rel in EXEMPT_PATHS:
                continue
            text = path.read_text(encoding="utf-8")

            for label, pattern in RULES:
                match = pattern.search(text)
                if match:
                    line = text.count("\n", 0, match.start()) + 1
                    errors.append(f"{rel}:{line}: superseded {label}: {match.group(0)!r}")

            for removed in REMOVED_ROUTE_NAMES:
                if removed in text:
                    line = text[: text.index(removed)].count("\n") + 1
                    errors.append(f"{rel}:{line}: references removed route {removed}")

    if errors:
        print("Current combat vocabulary validation FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Current combat vocabulary validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
