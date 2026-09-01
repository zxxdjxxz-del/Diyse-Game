"""Base Hit / Evasion resolver backed by repository rule values."""
from __future__ import annotations

from ..common import round_half_up
from ..sources.combat import load_combat_rules


def adjusted_hit_chance(action_base_hit: int, target_evasion: int, *, base_hit_percent: float = 1.0, flat_base_hit: int = 0, evasion_percent: float = 1.0, flat_evasion: int = 0) -> int:
    adjusted_base_hit = round_half_up(action_base_hit * base_hit_percent) + flat_base_hit
    effective_evasion = round_half_up(target_evasion * evasion_percent) + flat_evasion
    rules = load_combat_rules()
    return max(rules.min_hit_chance, min(rules.max_hit_chance, adjusted_base_hit - effective_evasion))


__all__ = ["adjusted_hit_chance"]
