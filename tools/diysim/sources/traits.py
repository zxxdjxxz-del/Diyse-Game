"""Repository-backed Trait package lookup.

Trait names, ranks, unlocks, and effect text remain owned by TRAITS.md. This
module only parses that authority into reusable structures for simulation.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re

from .repo import SourceGapError, find_repo_root, read_repo_text

TRAITS_PATH = "docs/06_CLASSES_AND_ABILITIES/TRAITS.md"


@dataclass(frozen=True)
class TraitRankSource:
    label: str
    unlock: str
    effect: str


@dataclass(frozen=True)
class TraitSource:
    character: str
    class_name: str
    trait_name: str
    ranks: tuple[TraitRankSource, ...]
    notes: tuple[str, ...]
    owner_path: str = TRAITS_PATH


def _parse_traits(text: str) -> tuple[TraitSource, ...]:
    lines = text.splitlines()
    records: list[TraitSource] = []
    index = 0
    while index < len(lines):
        match = re.match(r"^###\s+(.+?)\s+—\s+(.+?)\s+—\s+(.+?)\s*$", lines[index])
        if not match:
            index += 1
            continue

        character, class_name, trait_name = (part.strip() for part in match.groups())
        block: list[str] = []
        index += 1
        while index < len(lines) and not re.match(r"^#{2,3}\s+", lines[index]):
            stripped = lines[index].strip()
            if stripped:
                block.append(stripped)
            index += 1

        ranks: list[TraitRankSource] = []
        notes: list[str] = []
        for line in block:
            rank = re.match(r"^-\s+\*\*(Rank\s+[^—:*]+)\s+—\s+([^:*]+):\*\*\s*(.+)$", line)
            if rank:
                ranks.append(TraitRankSource(rank.group(1).strip(), rank.group(2).strip(), rank.group(3).strip()))
            elif line.startswith("-"):
                notes.append(line[1:].strip())

        if not ranks:
            raise SourceGapError(f"Trait package has no parsed ranks: {class_name} / {trait_name}")
        records.append(TraitSource(character, class_name, trait_name, tuple(ranks), tuple(notes)))

    if not records:
        raise SourceGapError("Trait register contains no Trait packages")
    return tuple(records)


@lru_cache(maxsize=4)
def _cached(root_string: str) -> tuple[TraitSource, ...]:
    root = Path(root_string)
    return _parse_traits(read_repo_text(TRAITS_PATH, root=root))


def load_trait_registry(*, root: Path | None = None) -> tuple[TraitSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _cached(str(repo))


def load_trait_source(
    *,
    trait_name: str | None = None,
    class_name: str | None = None,
    root: Path | None = None,
) -> TraitSource:
    if trait_name is None and class_name is None:
        raise ValueError("trait_name or class_name is required")
    matches = list(load_trait_registry(root=root))
    if trait_name is not None:
        matches = [record for record in matches if record.trait_name == trait_name]
    if class_name is not None:
        matches = [record for record in matches if record.class_name == class_name]
    if not matches:
        details = ", ".join(x for x in (trait_name, class_name) if x)
        raise SourceGapError(f"Trait register does not contain requested package: {details}")
    if len(matches) > 1:
        names = ", ".join(f"{record.class_name} / {record.trait_name}" for record in matches)
        raise SourceGapError(f"Trait lookup is ambiguous: {names}")
    return matches[0]


__all__ = [
    "TraitRankSource",
    "TraitSource",
    "load_trait_registry",
    "load_trait_source",
]
