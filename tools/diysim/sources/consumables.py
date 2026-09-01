"""Repository-backed consumable definitions.

Item identity/effects stay owned by the consumable master register. This module
parses that authority without assigning carried quantities or tactical policy.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from .markdown import find_markdown_table
from .repo import SourceGapError, find_repo_root, read_repo_text

CONSUMABLE_REGISTER_PATH = (
    "docs/08_ITEMS_AND_EQUIPMENT/CONSUMABLES/CONSUMABLE_MASTER_REGISTER.md"
)


@dataclass(frozen=True)
class ConsumableSource:
    item_id: str
    name: str
    function: str
    role: str


@lru_cache(maxsize=4)
def _cached(root_string: str) -> tuple[ConsumableSource, ...]:
    root = Path(root_string)
    text = read_repo_text(CONSUMABLE_REGISTER_PATH, root=root)
    rows = find_markdown_table(text, ("ID", "Consumable", "Current function", "Role"))
    entries = tuple(
        ConsumableSource(
            item_id=row["ID"],
            name=row["Consumable"],
            function=row["Current function"],
            role=row["Role"],
        )
        for row in rows
    )
    if not entries:
        raise SourceGapError("Consumable master register is empty")
    return entries


def load_consumable_register(*, root: Path | None = None) -> tuple[ConsumableSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _cached(str(repo))


def load_consumable(name: str, *, root: Path | None = None) -> ConsumableSource:
    matches = tuple(
        entry for entry in load_consumable_register(root=root)
        if entry.name.casefold() == name.casefold()
    )
    if not matches:
        raise SourceGapError(f"Unknown consumable in master register: {name}")
    if len(matches) != 1:
        raise SourceGapError(f"Consumable name is ambiguous in master register: {name}")
    return matches[0]


__all__ = [
    "CONSUMABLE_REGISTER_PATH",
    "ConsumableSource",
    "load_consumable",
    "load_consumable_register",
]
