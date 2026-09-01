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

        max_hp = re.search(r"Max HP\s*([+-]\d+)", stats_text, re.I)
        max_mp = re.search(r"Max MP\s*([+-]\d+)", stats_text, re.I)
        evasion = re.search(r"Evasion\s*([+-]\d+)", stats_text, re.I)
        status_resistance = re.search(r"Status Resistance\s*([+-]\d+)", stats_text, re.I)
        if max_hp:
            bonuses["hp"] = int(max_hp.group(1))
        if max_mp:
            bonuses["mp"] = int(max_mp.group(1))

        entries.append(
            EquipmentSource(
                layer=row["Layer"],
                equipment_type=row["Type"],
                name=row["Name"],
                owner=row["Owner/tradition"],
                stats_text=stats_text,
                stat_bonuses=bonuses,
                evasion_bonus=int(evasion.group(1)) if evasion else 0,
                status_resistance_bonus=int(status_resistance.group(1)) if status_resistance else 0,
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
