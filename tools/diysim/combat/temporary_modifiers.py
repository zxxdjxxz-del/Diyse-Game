"""Temporary non-status combat modifiers.

Core-stat changes follow STAT_CHANGES.md: percentage based, different effect
identities stack, positive and negative contributions cap independently at
40%, and same-effect reapplication refreshes/replaces rather than duplicating.
"""
from __future__ import annotations
from typing import Sequence

from ..common import round_half_up
from .models import ActiveTemporaryModifier, CombatUnit, CoreStatName, TemporaryModifierSpec

_CORE_STAT_CAP_PERCENT = 40.0


def apply_temporary_modifier(unit: CombatUnit, spec: TemporaryModifierSpec) -> None:
    unit.temporary_modifiers[spec.effect_id] = ActiveTemporaryModifier(
        effect_id=spec.effect_id,
        remaining_rounds=spec.duration_rounds,
        status_resistance_flat=spec.status_resistance_flat,
        attack_percent=spec.attack_percent,
        magic_percent=spec.magic_percent,
        defense_percent=spec.defense_percent,
        spirit_percent=spec.spirit_percent,
        speed_percent=spec.speed_percent,
        base_hit_flat=spec.base_hit_flat,
        direct_damage_reduction=spec.direct_damage_reduction,
    )


def effective_status_resistance(unit: CombatUnit) -> int:
    return unit.template.status_resistance + sum(
        modifier.status_resistance_flat
        for modifier in unit.temporary_modifiers.values()
    )


def effective_base_hit_bonus(unit: CombatUnit) -> int:
    return sum(modifier.base_hit_flat for modifier in unit.temporary_modifiers.values())


def effective_direct_damage_reduction(unit: CombatUnit) -> float:
    """Use the strongest active legal reduction layer by default."""
    active = [unit.template.direct_damage_reduction]
    active.extend(modifier.direct_damage_reduction for modifier in unit.temporary_modifiers.values())
    return max(active, default=0.0)


def temporary_core_stat_percent(unit: CombatUnit, stat: CoreStatName, *extra_percentages: float) -> float:
    values = [getattr(modifier, f"{stat}_percent") for modifier in unit.temporary_modifiers.values()]
    values.extend(extra_percentages)
    positive = min(_CORE_STAT_CAP_PERCENT, sum(value for value in values if value > 0))
    negative = max(-_CORE_STAT_CAP_PERCENT, sum(value for value in values if value < 0))
    return positive + negative


def apply_core_stat_percent(base_value: float, net_percent: float) -> int:
    return round_half_up(base_value * (1.0 + net_percent / 100.0))


def effective_core_stat(
    unit: CombatUnit,
    stat: CoreStatName,
    *,
    extra_percentages: tuple[float, ...] = (),
) -> int:
    base_value = getattr(unit.template.stats, stat)
    return apply_core_stat_percent(
        base_value,
        temporary_core_stat_percent(unit, stat, *extra_percentages),
    )


def tick_temporary_modifiers(units: Sequence[CombatUnit]) -> None:
    """Consume one numbered-round checkpoint.

    An effect applied during normal turn resolution counts that application
    round as round 1, so its duration is decremented at that round's end.
    """
    for unit in units:
        for effect_id, modifier in list(unit.temporary_modifiers.items()):
            modifier.remaining_rounds -= 1
            if modifier.remaining_rounds <= 0:
                unit.temporary_modifiers.pop(effect_id, None)


__all__ = [
    "apply_core_stat_percent",
    "apply_temporary_modifier",
    "effective_base_hit_bonus",
    "effective_core_stat",
    "effective_direct_damage_reduction",
    "effective_status_resistance",
    "temporary_core_stat_percent",
    "tick_temporary_modifiers",
]
