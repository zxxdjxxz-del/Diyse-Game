"""Player EXP lookup using the repository-owned current EXP table."""
from __future__ import annotations
from pathlib import Path

from ..sources.progression import load_progression_rules


def round_nearest_100(value: float) -> int:
    """General utility retained for analysis; the current EXP curve uses repo table values."""
    return int(round(value / 100.0)) * 100


def level_up_cost(current_level: int, *, root: Path | None = None) -> int:
    rules = load_progression_rules(root=root)
    if not 1 <= current_level < rules.level_cap:
        raise ValueError(f"current_level must be between 1 and {rules.level_cap - 1}")
    return rules.cumulative_exp[current_level + 1] - rules.cumulative_exp[current_level]


def cumulative_exp(level: int, *, root: Path | None = None) -> int:
    rules = load_progression_rules(root=root)
    if not 1 <= level <= rules.level_cap:
        raise ValueError(f"level must be between 1 and {rules.level_cap}")
    return rules.cumulative_exp[level]


def level_from_exp(exp: int, *, root: Path | None = None) -> int:
    if exp < 0:
        raise ValueError("exp cannot be negative")
    rules = load_progression_rules(root=root)
    level = 1
    for candidate in range(2, rules.level_cap + 1):
        if exp < rules.cumulative_exp[candidate]:
            break
        level = candidate
    return level


def exp_to_next_level(exp: int, *, root: Path | None = None) -> int:
    rules = load_progression_rules(root=root)
    level = level_from_exp(exp, root=root)
    if level == rules.level_cap:
        return 0
    return rules.cumulative_exp[level + 1] - exp


__all__ = [
    "cumulative_exp",
    "exp_to_next_level",
    "level_from_exp",
    "level_up_cost",
    "round_nearest_100",
]
