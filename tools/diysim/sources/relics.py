"""Repository-backed Relic first-acquisition timing and weapon-family authority."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from .markdown import find_markdown_table, parse_int
from .repo import SourceGapError, find_repo_root, read_repo_text

RELIC_PLACEMENT_PATH = "docs/08_ITEMS_AND_EQUIPMENT/RELICS/RELIC_PLACEMENT.md"
RELIC_WEAPONS_PATH = "docs/08_ITEMS_AND_EQUIPMENT/RELICS/RELIC_WEAPONS.md"


@dataclass(frozen=True)
class RelicPlacementSource:
    chapter: int
    relic: str
    acquisition_source: str
    explicitly_guaranteed: bool
    source_path: str = RELIC_PLACEMENT_PATH


@dataclass(frozen=True)
class RelicWeaponSource:
    character: str
    family: str
    relic: str
    source_path: str = RELIC_WEAPONS_PATH

    @property
    def consumes_secondary(self) -> bool:
        return self.family.casefold() in {"great bow", "two-handed sword"}


@lru_cache(maxsize=4)
def _load_placements(root_string: str) -> tuple[RelicPlacementSource, ...]:
    root = Path(root_string)
    text = read_repo_text(RELIC_PLACEMENT_PATH, root=root)
    rows = find_markdown_table(text, ("Chapter", "Relic", "First-acquisition source"))
    entries: list[RelicPlacementSource] = []
    seen: set[str] = set()
    for row in rows:
        relic = row["Relic"].strip()
        key = relic.casefold()
        if key in seen:
            raise SourceGapError(f"Duplicate Relic placement row: {relic}")
        seen.add(key)
        source = row["First-acquisition source"].strip()
        entries.append(
            RelicPlacementSource(
                chapter=parse_int(row["Chapter"]),
                relic=relic,
                acquisition_source=source,
                explicitly_guaranteed="guaranteed" in source.casefold(),
            )
        )
    if len(entries) != 36:
        raise SourceGapError(
            f"Expected 36 Relic first-acquisition rows in {RELIC_PLACEMENT_PATH}, "
            f"found {len(entries)}"
        )
    return tuple(entries)


@lru_cache(maxsize=4)
def _load_weapons(root_string: str) -> tuple[RelicWeaponSource, ...]:
    root = Path(root_string)
    text = read_repo_text(RELIC_WEAPONS_PATH, root=root)
    rows = find_markdown_table(text, ("Character", "Family", "Relic", "Raw stats", "Trait"))
    entries = tuple(
        RelicWeaponSource(
            character=row["Character"].strip(),
            family=row["Family"].strip(),
            relic=row["Relic"].strip(),
        )
        for row in rows
    )
    if len(entries) != 16:
        raise SourceGapError(
            f"Expected 16 Relic weapon rows in {RELIC_WEAPONS_PATH}, found {len(entries)}"
        )
    if len({row.relic.casefold() for row in entries}) != len(entries):
        raise SourceGapError(f"Duplicate Relic weapon identity in {RELIC_WEAPONS_PATH}")
    return entries


def load_relic_placements(*, root: Path | None = None) -> tuple[RelicPlacementSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _load_placements(str(repo))


def load_relic_placement(relic: str, *, root: Path | None = None) -> RelicPlacementSource:
    matches = tuple(
        row for row in load_relic_placements(root=root) if row.relic.casefold() == relic.casefold()
    )
    if not matches:
        raise SourceGapError(f"No first-acquisition placement found for Relic: {relic}")
    if len(matches) != 1:
        raise SourceGapError(f"Ambiguous first-acquisition placement for Relic: {relic}")
    return matches[0]


def load_relic_weapons(*, root: Path | None = None) -> tuple[RelicWeaponSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _load_weapons(str(repo))


def load_relic_weapon(relic: str, *, root: Path | None = None) -> RelicWeaponSource:
    matches = tuple(
        row for row in load_relic_weapons(root=root) if row.relic.casefold() == relic.casefold()
    )
    if not matches:
        raise SourceGapError(f"No Relic weapon-family row found for: {relic}")
    if len(matches) != 1:
        raise SourceGapError(f"Ambiguous Relic weapon-family row for: {relic}")
    return matches[0]


__all__ = [
    "RELIC_PLACEMENT_PATH",
    "RELIC_WEAPONS_PATH",
    "RelicPlacementSource",
    "RelicWeaponSource",
    "load_relic_placement",
    "load_relic_placements",
    "load_relic_weapon",
    "load_relic_weapons",
]
