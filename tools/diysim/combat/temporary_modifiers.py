"""Temporary non-status combat modifiers.

Status Resistance changes are flat points under current Diyse canon and are
not universal harmful statuses. Same-effect reapplication refreshes/replaces
rather than stacking duplicate copies.
"""
from __future__ import annotations
from typing import Sequence

from .models import ActiveTemporaryModifier, CombatUnit, TemporaryModifierSpec


def apply_temporary_modifier(unit: CombatUnit, spec: TemporaryModifierSpec) -> None:
    unit.temporary_modifiers[spec.effect_id] = ActiveTemporaryModifier(
        effect_id=spec.effect_id,
        remaining_rounds=spec.duration_rounds,
        status_resistance_flat=spec.status_resistance_flat,
    )


def effective_status_resistance(unit: CombatUnit) -> int:
    return unit.template.status_resistance + sum(
        modifier.status_resistance_flat
        for modifier in unit.temporary_modifiers.values()
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
    "apply_temporary_modifier",
    "effective_status_resistance",
    "tick_temporary_modifiers",
]
