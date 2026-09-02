"""Resolve equipment/checkpoint authority without duplicating item canon."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re

from .equipment import load_equipment
from .markdown import find_markdown_table
from .repo import SourceGapError, find_repo_root, read_repo_text

STARTING_LOADOUTS_PATH = "docs/08_ITEMS_AND_EQUIPMENT/STARTING_LOADOUTS.md"
ORDINARY_WEAPONS_PATH = "docs/08_ITEMS_AND_EQUIPMENT/WEAPONS/ORDINARY_WEAPONS.md"


@dataclass(frozen=True)
class GuaranteedLoadoutSource:
    character: str
    chapter: int
    weapon: str | None
    armor: str | None
    secondary: str | None
    level: int | None = None
    source_path: str = STARTING_LOADOUTS_PATH

    @property
    def equipment_names(self) -> tuple[str, ...]:
        return tuple(name for name in (self.weapon, self.armor, self.secondary) if name)


@dataclass(frozen=True)
class EquipmentAvailabilitySource:
    name: str
    character: str
    slot: str
    first_chapter: int
    source_path: str


def _named_slot(block: str, label: str) -> str | None:
    match = re.search(
        rf"^- \*\*{re.escape(label)}:\*\*\s*(.+?)(?:\s+—[^\n]*)?$",
        block,
        re.M,
    )
    return match.group(1).strip() if match else None


def _load_guaranteed(root_string: str) -> tuple[GuaranteedLoadoutSource, ...]:
    root = Path(root_string)
    text = read_repo_text(STARTING_LOADOUTS_PATH, root=root)
    heading_matches = list(re.finditer(r"^## Chapter (\d+) — (.+?)\s*$", text, re.M))
    rows: list[GuaranteedLoadoutSource] = []

    for index, match in enumerate(heading_matches):
        end = heading_matches[index + 1].start() if index + 1 < len(heading_matches) else len(text)
        block = text[match.end():end]
        character = match.group(2).strip()
        chapter = int(match.group(1))
        weapon = _named_slot(block, "Primary")
        armor = _named_slot(block, "Armor")
        secondary = _named_slot(block, "Secondary")
        level_match = re.search(r"\bLevel-(\d+)\b", block, re.I)
        level = int(level_match.group(1)) if level_match else None
        if not any((weapon, armor, secondary)):
            continue
        for name in (weapon, armor, secondary):
            if name:
                try:
                    load_equipment(name, root=root)
                except SourceGapError as exc:
                    raise SourceGapError(
                        f"{STARTING_LOADOUTS_PATH} references unknown equipment: {name}"
                    ) from exc
        rows.append(
            GuaranteedLoadoutSource(
                character=character,
                chapter=chapter,
                weapon=weapon,
                armor=armor,
                secondary=secondary,
                level=level,
            )
        )

    if not rows:
        raise SourceGapError(f"No guaranteed loadouts found in {STARTING_LOADOUTS_PATH}")
    return tuple(rows)


def _parse_first_chapter(value: str, *, equipment_name: str) -> int:
    match = re.fullmatch(r"\s*Ch(?:apter)?\s*(\d+)\s*", value, re.I)
    if not match:
        raise SourceGapError(
            f"Unsupported First availability for {equipment_name}: {value!r}"
        )
    return int(match.group(1))


def _load_weapon_availability(root_string: str) -> tuple[EquipmentAvailabilitySource, ...]:
    root = Path(root_string)
    text = read_repo_text(ORDINARY_WEAPONS_PATH, root=root)
    table = find_markdown_table(
        text,
        ("Character", "Equipment", "First availability"),
    )
    rows: list[EquipmentAvailabilitySource] = []

    for row in table:
        name = row["Equipment"]
        try:
            item = load_equipment(name, root=root)
        except SourceGapError as exc:
            raise SourceGapError(
                f"{ORDINARY_WEAPONS_PATH} references unknown equipment: {name}"
            ) from exc
        if item.layer.lower() != "ordinary":
            raise SourceGapError(
                f"{ORDINARY_WEAPONS_PATH} contains non-ordinary equipment: {name}"
            )
        rows.append(
            EquipmentAvailabilitySource(
                name=name,
                character=row["Character"],
                slot="weapon",
                first_chapter=_parse_first_chapter(
                    row["First availability"],
                    equipment_name=name,
                ),
                source_path=ORDINARY_WEAPONS_PATH,
            )
        )

    if not rows:
        raise SourceGapError(
            f"No chapter-aware ordinary weapon availability found in {ORDINARY_WEAPONS_PATH}"
        )
    return tuple(rows)


@lru_cache(maxsize=4)
def _cached_guaranteed(root_string: str) -> tuple[GuaranteedLoadoutSource, ...]:
    return _load_guaranteed(root_string)


@lru_cache(maxsize=4)
def _cached_weapon_availability(root_string: str) -> tuple[EquipmentAvailabilitySource, ...]:
    return _load_weapon_availability(root_string)


def load_guaranteed_loadouts(*, root: Path | None = None) -> tuple[GuaranteedLoadoutSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _cached_guaranteed(str(repo))


def load_ordinary_weapon_availability(
    *, root: Path | None = None
) -> tuple[EquipmentAvailabilitySource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _cached_weapon_availability(str(repo))


__all__ = [
    "EquipmentAvailabilitySource",
    "GuaranteedLoadoutSource",
    "ORDINARY_WEAPONS_PATH",
    "STARTING_LOADOUTS_PATH",
    "load_guaranteed_loadouts",
    "load_ordinary_weapon_availability",
]
