"""Player stat construction using repository-owned progression/class data."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

from ..common import round_half_up
from ..sources.progression import STAT_KEYS, load_progression_rules


@dataclass(frozen=True)
class Stats:
    hp: int
    mp: int
    attack: int
    magic: int
    defense: int
    spirit: int
    speed: int

    def as_dict(self) -> dict[str, int]:
        return {key: getattr(self, key) for key in STAT_KEYS}


def level_cap(*, root: Path | None = None) -> int:
    return load_progression_rules(root=root).level_cap


def class_multipliers(*, root: Path | None = None) -> dict[str, dict[str, float]]:
    return load_progression_rules(root=root).class_multipliers


def neutral_natural_stats(level: int, *, root: Path | None = None) -> dict[str, float]:
    rules = load_progression_rules(root=root)
    if not 1 <= level <= rules.level_cap:
        raise ValueError(f"level must be between 1 and {rules.level_cap}")
    x = level - 1
    return {
        key: base + linear * x + quadratic * x * x
        for key, (base, linear, quadratic) in rules.natural_coefficients.items()
    }


def natural_stats(
    level: int,
    class_name: str | None = None,
    equipment: dict[str, int] | None = None,
    *,
    root: Path | None = None,
) -> Stats:
    raw = neutral_natural_stats(level, root=root)
    multipliers = {key: 1.0 for key in STAT_KEYS}
    if class_name is not None:
        try:
            multipliers = load_progression_rules(root=root).class_multipliers[class_name]
        except KeyError as exc:
            raise ValueError(f"unknown class: {class_name}") from exc

    rounded = {key: round_half_up(raw[key] * multipliers[key]) for key in STAT_KEYS}
    for key, amount in (equipment or {}).items():
        if key not in STAT_KEYS:
            raise ValueError(f"unknown equipment stat: {key}")
        rounded[key] += int(amount)
    return Stats(**rounded)


__all__ = [
    "STAT_KEYS",
    "Stats",
    "class_multipliers",
    "level_cap",
    "natural_stats",
    "neutral_natural_stats",
]
