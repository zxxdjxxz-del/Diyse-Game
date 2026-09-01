"""Player natural-stat curves and selected-class multipliers."""
from __future__ import annotations
from dataclasses import dataclass

from ..common import round_half_up

LEVEL_CAP = 70
STAT_KEYS = ("hp", "mp", "attack", "magic", "defense", "spirit", "speed")

CLASS_MULTIPLIERS: dict[str, dict[str, float]] = {
    "Crest Knight": {"hp": 1.05, "mp": 0.90, "attack": 1.08, "magic": 0.95, "defense": 1.12, "spirit": 1.00, "speed": 0.96},
    "Blue Warden": {"hp": 1.00, "mp": 1.12, "attack": 0.88, "magic": 1.10, "defense": 0.98, "spirit": 1.10, "speed": 0.98},
    "War Archer": {"hp": 1.00, "mp": 0.95, "attack": 1.15, "magic": 0.82, "defense": 0.95, "spirit": 0.90, "speed": 1.00},
    "Cardweaver": {"hp": 0.88, "mp": 1.15, "attack": 0.85, "magic": 1.08, "defense": 0.86, "spirit": 1.00, "speed": 1.18},
    "Green Arcanist": {"hp": 0.82, "mp": 1.25, "attack": 0.72, "magic": 1.25, "defense": 0.78, "spirit": 1.12, "speed": 1.02},
    "Ruin Vanguard": {"hp": 1.20, "mp": 0.76, "attack": 1.22, "magic": 0.85, "defense": 1.18, "spirit": 0.85, "speed": 0.88},
    "Crest Arcanist": {"hp": 0.90, "mp": 1.15, "attack": 0.85, "magic": 1.15, "defense": 0.92, "spirit": 1.05, "speed": 1.00},
    "Vowblade": {"hp": 1.00, "mp": 0.92, "attack": 1.10, "magic": 0.78, "defense": 1.00, "spirit": 1.12, "speed": 1.02},
    "Routeweaver": {"hp": 0.98, "mp": 1.08, "attack": 1.02, "magic": 1.02, "defense": 0.94, "spirit": 0.98, "speed": 1.05},
    "Proofhunter": {"hp": 0.92, "mp": 1.00, "attack": 1.08, "magic": 1.08, "defense": 0.90, "spirit": 0.96, "speed": 1.04},
    "Axiomblade": {"hp": 1.04, "mp": 0.92, "attack": 1.08, "magic": 1.08, "defense": 1.02, "spirit": 0.96, "speed": 1.00},
    "Ruin Warden": {"hp": 1.05, "mp": 1.05, "attack": 1.00, "magic": 1.05, "defense": 1.02, "spirit": 1.05, "speed": 0.90},
}


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


def neutral_natural_stats(level: int) -> dict[str, float]:
    if not 1 <= level <= LEVEL_CAP:
        raise ValueError(f"level must be between 1 and {LEVEL_CAP}")
    x = level - 1
    return {
        "hp": 220 + 34 * x + 0.28 * x * x,
        "mp": 28 + 3.25 * x + 0.018 * x * x,
        "attack": 18 + 2.05 * x + 0.008 * x * x,
        "magic": 18 + 2.05 * x + 0.008 * x * x,
        "defense": 16 + 1.70 * x + 0.006 * x * x,
        "spirit": 16 + 1.70 * x + 0.006 * x * x,
        "speed": 22 + 0.52 * x,
    }


def natural_stats(level: int, class_name: str | None = None, equipment: dict[str, int] | None = None) -> Stats:
    raw = neutral_natural_stats(level)
    multipliers = {key: 1.0 for key in STAT_KEYS}
    if class_name is not None:
        try:
            multipliers = CLASS_MULTIPLIERS[class_name]
        except KeyError as exc:
            raise ValueError(f"unknown class: {class_name}") from exc

    rounded = {key: round_half_up(raw[key] * multipliers[key]) for key in STAT_KEYS}
    for key, amount in (equipment or {}).items():
        if key not in STAT_KEYS:
            raise ValueError(f"unknown equipment stat: {key}")
        rounded[key] += int(amount)
    return Stats(**rounded)
