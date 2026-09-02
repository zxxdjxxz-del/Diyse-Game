"""Repository-backed Relic first-acquisition timing."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from .markdown import find_markdown_table, parse_int
from .repo import SourceGapError, find_repo_root, read_repo_text

RELIC_PLACEMENT_PATH = "docs/08_ITEMS_AND_EQUIPMENT/RELICS/RELIC_PLACEMENT.md"


@dataclass(frozen=True)
class RelicPlacementSource:
    chapter: int
    relic: str
    acquisition_source: str
    explicitly_guaranteed: bool
    source_path: str = RELIC_PLACEMENT_PATH


@lru_cache(maxsize=4)
def _load_all(root_string: str) -> tuple[RelicPlacementSource, ...]:
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


def load_relic_placements(*, root: Path | None = None) -> tuple[RelicPlacementSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _load_all(str(repo))


def load_relic_placement(relic: str, *, root: Path | None = None) -> RelicPlacementSource:
    matches = tuple(
        row for row in load_relic_placements(root=root) if row.relic.casefold() == relic.casefold()
    )
    if not matches:
        raise SourceGapError(f"No first-acquisition placement found for Relic: {relic}")
    if len(matches) != 1:
        raise SourceGapError(f"Ambiguous first-acquisition placement for Relic: {relic}")
    return matches[0]


__all__ = [
    "RELIC_PLACEMENT_PATH",
    "RelicPlacementSource",
    "load_relic_placement",
    "load_relic_placements",
]
