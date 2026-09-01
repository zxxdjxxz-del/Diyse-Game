"""Repo-backed Lv11/Lv13 First Command Warden same-gear party snapshots."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re

from tools.diysim.combat.models import Combatant
from tools.diysim.progression import natural_stats
from tools.diysim.sources import (
    SourceGapError,
    combine_equipment_bonuses,
    extract_heading_block,
    load_ability_registry,
    read_repo_text,
)

V105_PATH = "docs/16_BALANCE_AND_TESTING/FOUR_POINT_BOSS_LEVEL_SENSITIVITY_v105.md"


@dataclass(frozen=True)
class WardenPartySnapshot:
    level: int
    party: tuple[Combatant, ...]
    equipment: dict[str, tuple[str, ...]]


def _base_class_for(character: str, *, root: Path | None = None) -> str:
    classes = {
        entry.class_name
        for entry in load_ability_registry(root=root)
        if entry.character == character and entry.line == "Base"
    }
    if len(classes) != 1:
        raise SourceGapError(f"Expected one current Base Class for {character}, found: {sorted(classes)}")
    return next(iter(classes))


def _clean_equipment_token(token: str) -> str:
    # v105 writes the final loadout item as ordinary sentence prose, so the
    # terminal full stop is punctuation rather than part of the item identity.
    return token.strip().rstrip(".;")


def _parse_v105_warden_setup(*, root: Path | None = None) -> tuple[tuple[int, int], tuple[str, ...], dict[str, tuple[str, ...]]]:
    text = read_repo_text(V105_PATH, root=root)
    block = extract_heading_block(text, "Chapter 3 — First Command Warden")

    comparison = re.search(r"Core comparison:\s*>\s*\*\*Lv(\d+) vs Lv(\d+)\*\*", block, re.I | re.S)
    if not comparison:
        raise SourceGapError(f"{V105_PATH} lacks First Command Warden core level comparison")
    levels = (int(comparison.group(1)), int(comparison.group(2)))

    active_match = re.search(
        r"Active four:\s*(?P<body>(?:\n- [^\n]+){4})",
        block,
        re.I,
    )
    if not active_match:
        raise SourceGapError(f"{V105_PATH} lacks First Command Warden active-four list")
    active = tuple(
        line.removeprefix("- ").strip()
        for line in active_match.group("body").strip().splitlines()
    )

    equipment: dict[str, tuple[str, ...]] = {}
    for character in active:
        match = re.search(
            rf"^-[ \t]*{re.escape(character)}[ \t]*[—-][ \t]*(.+?);?$",
            block,
            re.I | re.M,
        )
        if not match:
            raise SourceGapError(f"{V105_PATH} lacks First Command Warden equipment for {character}")
        equipment[character] = tuple(
            _clean_equipment_token(part) for part in match.group(1).split(" / ")
        )

    return levels, active, equipment


@lru_cache(maxsize=8)
def load_first_command_warden_party_snapshot(
    level: int,
    *,
    root: Path | None = None,
) -> WardenPartySnapshot:
    """Build each immutable same-gear level snapshot once per source root."""
    levels, active, equipment = _parse_v105_warden_setup(root=root)
    if level not in levels:
        raise ValueError(f"v105 First Command Warden comparison owns Lv{levels[0]} and Lv{levels[1]}, not Lv{level}")

    party: list[Combatant] = []
    for character in active:
        class_name = _base_class_for(character, root=root)
        bonuses, evasion, status_resistance = combine_equipment_bonuses(equipment[character], root=root)
        party.append(
            Combatant(
                name=character,
                side="party",
                stats=natural_stats(level, class_name, equipment=bonuses, root=root),
                evasion=evasion,
                status_resistance=status_resistance,
            )
        )

    return WardenPartySnapshot(level=level, party=tuple(party), equipment=equipment)


__all__ = ["V105_PATH", "WardenPartySnapshot", "load_first_command_warden_party_snapshot"]
