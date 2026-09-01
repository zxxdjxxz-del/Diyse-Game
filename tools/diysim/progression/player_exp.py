"""Player EXP curve and level lookup."""
from __future__ import annotations

from .stats import LEVEL_CAP


def round_nearest_100(value: float) -> int:
    return int(round(value / 100.0)) * 100


def level_up_cost(current_level: int) -> int:
    if not 1 <= current_level < LEVEL_CAP:
        raise ValueError(f"current_level must be between 1 and {LEVEL_CAP - 1}")
    if current_level < 17:
        return 100 * (current_level**2 - (current_level - 1) ** 2)
    base_cost = 100 * (2 * current_level - 1)
    multiplier = 1 + 0.35 * (current_level - 17) / 42
    return round_nearest_100(base_cost * multiplier)


def cumulative_exp(level: int) -> int:
    if not 1 <= level <= LEVEL_CAP:
        raise ValueError(f"level must be between 1 and {LEVEL_CAP}")
    if level <= 17:
        return 100 * (level - 1) ** 2
    total = 100 * 16**2
    for current_level in range(17, level):
        total += level_up_cost(current_level)
    return total


def level_from_exp(exp: int) -> int:
    if exp < 0:
        raise ValueError("exp cannot be negative")
    level = 1
    for candidate in range(2, LEVEL_CAP + 1):
        if exp < cumulative_exp(candidate):
            break
        level = candidate
    return level


def exp_to_next_level(exp: int) -> int:
    level = level_from_exp(exp)
    if level == LEVEL_CAP:
        return 0
    return cumulative_exp(level + 1) - exp
