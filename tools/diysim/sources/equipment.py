"""Repository-backed ordinary-equipment stat parsing."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re

from .markdown import find_markdown_table
from .repo import SourceGapError, find_repo_root, read_repo_text

EQUIPMENT_REGISTER_PATH = "docs/08_ITEMS_AND_EQUIPMENT/EQUIPMENT_MASTER_REGISTER.md"

_STAT_LABELS = {
    "ATK": "attack",
    "MAG": "magic",
    "DEF": "defense",
    "SPR": "spirit",
    "SPD": "speed",
}


@dataclass(frozen=True)
class EquipmentSource:
    layer: str
    equipment_type: str
    name: str
    owner: str
    stats_text: str
    stat_bonuses: dict[str, int]
    evasion_bonus: int = 0
    status_resistance_bonus: int = 0


def _named_bonus(text: str, label: str) -> int:
    patterns = (
        rf"{re.escape(label)}\s*([+-]\d+)",
        rf"([+-]\d+)\s*{re.escape(label)}\b",
    )
    for pattern in patterns:
        match = re.search(pattern, text, re.I)
        if match:
            return int(match.group(1))
    return 0


@lru_cache(maxsize=4)
def _load_all(root_string: str) -> tuple[EquipmentSource, ...]:
    root = Path(root_string)
    text = read_repo_text(EQUIPMENT_REGISTER_PATH, root=root)
    rows = find_markdown_table(text, ("Layer", "Type", "Name", "Owner/tradition", "Stats / function"))
    entries: list[EquipmentSource] = []
    for row in rows:
        stats_text = row["Stats / function"]
        bonuses: dict[str, int] = {}
        for label, key in _STAT_LABELS.items():
            match = re.search(rf"([+-]\d+)\s*{label}\b", stats_text, re.I)
            if match:
                bonuses[key] = int(match.group(1))

        max_hp = _named_bonus(stats_text, "Max HP")
        max_mp = _named_bonus(stats_text, "Max MP")
        if max_hp:
            bonuses["hp"] = max_hp
        if max_mp:
            bonuses["mp"] = max_mp

        entries.append(
            EquipmentSource(
                layer=row["Layer"],
                equipment_type=row["Type"],
                name=row["Name"],
                owner=row["Owner/tradition"],
                stats_text=stats_text,
                stat_bonuses=bonuses,
                evasion_bonus=_named_bonus(stats_text, "Evasion"),
                status_resistance_bonus=_named_bonus(stats_text, "Status Resistance"),
            )
        )
    if not entries:
        raise SourceGapError("Equipment master register is empty")
    return tuple(entries)


def load_equipment_register(*, root: Path | None = None) -> tuple[EquipmentSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _load_all(str(repo))


def load_equipment(name: str, *, root: Path | None = None) -> EquipmentSource:
    matches = tuple(entry for entry in load_equipment_register(root=root) if entry.name.casefold() == name.casefold())
    if not matches:
        raise SourceGapError(f"Unknown equipment in master register: {name}")
    if len(matches) != 1:
        raise SourceGapError(f"Equipment name is ambiguous in master register: {name}")
    return matches[0]


def combine_equipment_bonuses(
    names: tuple[str, ...] | list[str],
    *,
    root: Path | None = None,
) -> tuple[dict[str, int], int, int]:
    """Return core-stat, Evasion, and Status Resistance bonuses for a loadout."""
    stats: dict[str, int] = {}
    evasion = 0
    status_resistance = 0
    for name in names:
        item = load_equipment(name, root=root)
        for key, amount in item.stat_bonuses.items():
            stats[key] = stats.get(key, 0) + amount
        evasion += item.evasion_bonus
        status_resistance += item.status_resistance_bonus
    return stats, evasion, status_resistance


__all__ = [
    "EQUIPMENT_REGISTER_PATH",
    "EquipmentSource",
    "combine_equipment_bonuses",
    "load_equipment",
    "load_equipment_register",
]
