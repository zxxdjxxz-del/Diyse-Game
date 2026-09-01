"""Repository-backed class Ability lookup.

This module stores source locations and parsing logic only. Ability names,
classes, MP costs, Powers, unlocks, and effects are read from repo authority at
runtime.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re

from .markdown import extract_markdown_tables, find_markdown_table, parse_int
from .repo import SourceGapError, find_repo_root, read_repo_text

ABILITY_REGISTER_PATH = "docs/06_CLASSES_AND_ABILITIES/ABILITY_MASTER_REGISTER.md"
POWER_REGISTER_PATH = "docs/06_CLASSES_AND_ABILITIES/CLASS_ACTION_POWER_REGISTER.md"
CLASS_SOURCE_DIRS = (
    "docs/06_CLASSES_AND_ABILITIES/BASE_CLASSES",
    "docs/06_CLASSES_AND_ABILITIES/SUBCLASSES",
)


@dataclass(frozen=True)
class AbilityRegistryEntry:
    character: str
    class_name: str
    line: str
    unlock: str
    ability: str
    mp_text: str

    @property
    def fixed_mp(self) -> int | None:
        return parse_int(self.mp_text) if re.fullmatch(r"\d+", self.mp_text.strip()) else None


@dataclass(frozen=True)
class AbilitySource:
    registry: AbilityRegistryEntry
    owner_path: str
    owner_effect: str
    owner_mp_text: str
    power_index_text: str | None

    @property
    def fixed_mp(self) -> int | None:
        return self.registry.fixed_mp


def _registry(root: Path) -> tuple[AbilityRegistryEntry, ...]:
    text = read_repo_text(ABILITY_REGISTER_PATH, root=root)
    rows = find_markdown_table(text, ("Character", "Class", "Line", "Unlock", "Ability", "MP"))
    entries = tuple(
        AbilityRegistryEntry(
            character=row["Character"],
            class_name=row["Class"],
            line=row["Line"],
            unlock=row["Unlock"],
            ability=row["Ability"],
            mp_text=row["MP"],
        )
        for row in rows
    )
    if not entries:
        raise SourceGapError("Ability master register is empty")
    return entries


def _power_index(root: Path) -> dict[tuple[str, str], str]:
    text = read_repo_text(POWER_REGISTER_PATH, root=root)
    index: dict[tuple[str, str], str] = {}
    for rows in extract_markdown_tables(text):
        if not rows or not {"Class", "Ability", "Direct-damage Power"}.issubset(rows[0]):
            continue
        for row in rows:
            key = (row["Class"], row["Ability"])
            value = row["Direct-damage Power"]
            if key in index and index[key] != value:
                raise SourceGapError(f"Conflicting Power-index entries for {key[0]} / {key[1]}")
            index[key] = value
    return index


def _class_owner_path(root: Path, class_name: str) -> str:
    matches: list[str] = []
    for relative_dir in CLASS_SOURCE_DIRS:
        source_dir = root / relative_dir
        if not source_dir.is_dir():
            continue
        for path in source_dir.glob("*.md"):
            relative = path.relative_to(root).as_posix()
            text = read_repo_text(relative, root=root)
            title = re.search(r"^#\s+Diyse\s+—\s+(.+?)\s*$", text, re.M)
            if title and title.group(1).strip() == class_name:
                matches.append(relative)
    if not matches:
        raise SourceGapError(f"No class owner file found for {class_name}")
    if len(matches) > 1:
        raise SourceGapError(f"Multiple class owner files found for {class_name}: {', '.join(matches)}")
    return matches[0]


def _owner_row(root: Path, owner_path: str, ability: str) -> dict[str, str]:
    text = read_repo_text(owner_path, root=root)
    rows = find_markdown_table(text, ("Unlock", "Ability", "MP", "Current effect"))
    matches = [row for row in rows if row["Ability"] == ability]
    if not matches:
        raise SourceGapError(f"{owner_path} does not define {ability}")
    if len(matches) > 1:
        raise SourceGapError(f"{owner_path} defines {ability} more than once")
    return matches[0]


def _load_registry_cached(root_string: str) -> tuple[AbilityRegistryEntry, ...]:
    return _registry(Path(root_string))


_load_registry_cached = lru_cache(maxsize=4)(_load_registry_cached)


def _load_power_cached(root_string: str) -> dict[tuple[str, str], str]:
    return _power_index(Path(root_string))


_load_power_cached = lru_cache(maxsize=4)(_load_power_cached)


def load_ability_registry(*, root: Path | None = None) -> tuple[AbilityRegistryEntry, ...]:
    repo = (root or find_repo_root()).resolve()
    return _load_registry_cached(str(repo))


def load_ability_source(
    ability: str,
    *,
    class_name: str | None = None,
    root: Path | None = None,
) -> AbilitySource:
    repo = (root or find_repo_root()).resolve()
    matches = [entry for entry in load_ability_registry(root=repo) if entry.ability == ability]
    if class_name is not None:
        matches = [entry for entry in matches if entry.class_name == class_name]
    if not matches:
        qualifier = f" in {class_name}" if class_name else ""
        raise SourceGapError(f"Ability register does not contain {ability}{qualifier}")
    if len(matches) > 1:
        classes = ", ".join(sorted(entry.class_name for entry in matches))
        raise SourceGapError(f"Ability name {ability!r} is ambiguous across: {classes}")

    entry = matches[0]
    owner_path = _class_owner_path(repo, entry.class_name)
    row = _owner_row(repo, owner_path, entry.ability)

    registry_mp = entry.fixed_mp
    owner_mp = parse_int(row["MP"]) if re.fullmatch(r"\d+", row["MP"].strip()) else None
    if registry_mp is not None and owner_mp is not None and registry_mp != owner_mp:
        raise SourceGapError(
            f"MP authority mismatch for {entry.class_name} / {entry.ability}: "
            f"register={registry_mp}, owner={owner_mp}"
        )

    power_text = _load_power_cached(str(repo)).get((entry.class_name, entry.ability))
    return AbilitySource(
        registry=entry,
        owner_path=owner_path,
        owner_effect=row["Current effect"],
        owner_mp_text=row["MP"],
        power_index_text=power_text,
    )


__all__ = [
    "AbilityRegistryEntry",
    "AbilitySource",
    "load_ability_registry",
    "load_ability_source",
]
