"""Base Hit / Evasion resolver."""
from __future__ import annotations

from ..common import round_half_up

MIN_HIT_CHANCE = 5
MAX_HIT_CHANCE = 100


def adjusted_hit_chance(action_base_hit: int, target_evasion: int, *, base_hit_percent: float = 1.0, flat_base_hit: int = 0, evasion_percent: float = 1.0, flat_evasion: int = 0) -> int:
    adjusted_base_hit = round_half_up(action_base_hit * base_hit_percent) + flat_base_hit
    effective_evasion = round_half_up(target_evasion * evasion_percent) + flat_evasion
    return max(MIN_HIT_CHANCE, min(MAX_HIT_CHANCE, adjusted_base_hit - effective_evasion))
