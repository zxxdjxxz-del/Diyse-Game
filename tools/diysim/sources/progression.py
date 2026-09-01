"""Parse player stat/class/EXP authority directly from repository Markdown."""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re

from .markdown import extract_markdown_table, parse_float, parse_int
from .repo import SourceGapError, find_repo_root, read_repo_text

NATURAL_STAT_PATH = "docs/10_PROGRESSION_AND_EXP/NATURAL_STAT_CURVE.md"
CLASS_STATS_PATH = "docs/06_CLASSES_AND_ABILITIES/SELECTED_CLASS_STAT_PACKAGES.md"
PLAYER_EXP_PATH = "docs/10_PROGRESSION_AND_EXP/PLAYER_EXP_CURVE.md"

STAT_KEYS = ("hp", "mp", "attack", "magic", "defense", "spirit", "speed")


@dataclass(frozen=True)
class ProgressionRules:
    level_cap: int
    natural_coefficients: dict[str, tuple[float, float, float]]
    class_multipliers: dict[str, dict[str, float]]
    cumulative_exp: dict[int, int]


def _parse_polynomial(text: str, label: str) -> tuple[float, float, float]:
    match = re.search(
        rf"\*\*{re.escape(label)}\s*=\s*([0-9.]+)\s*\+\s*([0-9.]+)x(?:\s*\+\s*([0-9.]+)x²)?\*\*",
        text,
    )
    if not match:
        raise SourceGapError(f"Missing natural-stat formula for {label}")
    return float(match.group(1)), float(match.group(2)), float(match.group(3) or 0.0)


def _parse_class_table(text: str, heading: str, name_column: str) -> dict[str, dict[str, float]]:
    rows = extract_markdown_table(text, heading)
    result: dict[str, dict[str, float]] = {}
    key_map = {"HP": "hp", "MP": "mp", "ATK": "attack", "MAG": "magic", "DEF": "defense", "SPR": "spirit", "SPD": "speed"}
    for row in rows:
        name = row[name_column]
        result[name] = {key_map[column]: parse_float(row[column]) for column in key_map}
    return result


def _load(root_string: str) -> ProgressionRules:
    root = Path(root_string)
    natural_text = read_repo_text(NATURAL_STAT_PATH, root=root)
    class_text = read_repo_text(CLASS_STATS_PATH, root=root)
    exp_text = read_repo_text(PLAYER_EXP_PATH, root=root)

    scope = re.search(r"Player Levels\s+(\d+)[–-](\d+)", natural_text)
    if not scope:
        raise SourceGapError("Natural-stat source does not declare its level scope")
    level_cap = int(scope.group(2))

    coefficients = {
        "hp": _parse_polynomial(natural_text, "HP"),
        "mp": _parse_polynomial(natural_text, "MP"),
        "attack": _parse_polynomial(natural_text, "Attack"),
        "magic": _parse_polynomial(natural_text, "Magic"),
        "defense": _parse_polynomial(natural_text, "Defense"),
        "spirit": _parse_polynomial(natural_text, "Spirit"),
        "speed": _parse_polynomial(natural_text, "Speed"),
    }

    multipliers = _parse_class_table(class_text, "Base Classes", "Base Class")
    multipliers.update(_parse_class_table(class_text, "Subclasses", "Subclass"))

    exp_rows = extract_markdown_table(exp_text, "Full table")
    exp_table = {parse_int(row["Level"]): parse_int(row["Cumulative EXP"]) for row in exp_rows}
    if max(exp_table) != level_cap:
        raise SourceGapError("Player EXP table and natural-stat level cap disagree")

    return ProgressionRules(level_cap, coefficients, multipliers, exp_table)


@lru_cache(maxsize=4)
def _cached(root_string: str) -> ProgressionRules:
    return _load(root_string)


def load_progression_rules(*, root: Path | None = None) -> ProgressionRules:
    repo = (root or find_repo_root()).resolve()
    return _cached(str(repo))


__all__ = ["ProgressionRules", "STAT_KEYS", "load_progression_rules"]
