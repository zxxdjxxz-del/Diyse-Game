"""Repository-backed actor/stat and enemy-registry parsing.

Missing stat columns stay missing. This layer never turns an absent repo value
into zero or another gameplay value.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from .markdown import extract_markdown_table, find_markdown_table, parse_int
from .repo import SourceGapError, find_repo_root, read_repo_text

ENEMY_REGISTER_PATH = "docs/09_ENEMIES_AND_ENCOUNTERS/ENEMY_MASTER_REGISTER.md"

_STAT_COLUMNS = {
    "Lv": "level",
    "Level": "level",
    "HP": "hp",
    "MP": "mp",
    "ATK": "attack",
    "MAG": "magic",
    "DEF": "defense",
    "Spirit": "spirit",
    "SPR": "spirit",
    "SPD": "speed",
    "EVA": "evasion",
    "SR": "status_resistance",
}

_EXPLICIT_MISSING_STAT_MARKERS = {"-", "--", "---", "—", "–", "n/a", "na", "none"}


@dataclass(frozen=True)
class StatBlockSource:
    values: dict[str, int]
    raw_row: dict[str, str]

    def has(self, field: str) -> bool:
        return field in self.values

    def require(self, *fields: str) -> dict[str, int]:
        missing = tuple(field for field in fields if field not in self.values)
        if missing:
            raise SourceGapError(f"Stat row is missing required fields: {', '.join(missing)}")
        return {field: self.values[field] for field in fields}


@dataclass(frozen=True)
class EnemyRegistryEntry:
    chapter: str
    role: str
    identity: str


def _is_explicit_missing_stat(value: str) -> bool:
    return value.strip().casefold() in _EXPLICIT_MISSING_STAT_MARKERS


def parse_stat_row(row: dict[str, str]) -> StatBlockSource:
    values: dict[str, int] = {}
    for column, field in _STAT_COLUMNS.items():
        if column not in row:
            continue
        raw_value = row[column].strip()
        if not raw_value or _is_explicit_missing_stat(raw_value):
            continue
        value = parse_int(raw_value)
        if field in values and values[field] != value:
            raise SourceGapError(f"Conflicting stat columns for {field}")
        values[field] = value
    if "hp" not in values:
        raise SourceGapError("Stat row does not contain HP")
    return StatBlockSource(values=values, raw_row=dict(row))


def load_stat_table(
    relative_path: str,
    *,
    heading: str | None = None,
    root: Path | None = None,
) -> tuple[StatBlockSource, ...]:
    repo = (root or find_repo_root()).resolve()
    text = read_repo_text(relative_path, root=repo)
    if heading is not None:
        rows = extract_markdown_table(text, heading)
    else:
        rows = find_markdown_table(text, ("HP",))
    return tuple(parse_stat_row(row) for row in rows)


def load_stat_row(
    relative_path: str,
    *,
    heading: str,
    row_index: int = 0,
    root: Path | None = None,
) -> StatBlockSource:
    rows = load_stat_table(relative_path, heading=heading, root=root)
    try:
        return rows[row_index]
    except IndexError as exc:
        raise SourceGapError(f"No stat row {row_index} after {heading!r} in {relative_path}") from exc


@lru_cache(maxsize=4)
def _enemy_registry_cached(root_string: str) -> tuple[EnemyRegistryEntry, ...]:
    root = Path(root_string)
    text = read_repo_text(ENEMY_REGISTER_PATH, root=root)
    rows = find_markdown_table(text, ("Chapter", "Role", "Identity"))
    entries = tuple(
        EnemyRegistryEntry(row["Chapter"], row["Role"], row["Identity"])
        for row in rows
    )
    if not entries:
        raise SourceGapError("Enemy master register is empty")
    return entries


def load_enemy_registry(*, root: Path | None = None) -> tuple[EnemyRegistryEntry, ...]:
    repo = (root or find_repo_root()).resolve()
    return _enemy_registry_cached(str(repo))


def find_enemy_registry_entries(identity_text: str, *, root: Path | None = None) -> tuple[EnemyRegistryEntry, ...]:
    needle = identity_text.casefold()
    return tuple(entry for entry in load_enemy_registry(root=root) if needle in entry.identity.casefold())


__all__ = [
    "EnemyRegistryEntry",
    "StatBlockSource",
    "find_enemy_registry_entries",
    "load_enemy_registry",
    "load_stat_row",
    "load_stat_table",
    "parse_stat_row",
]
