"""Status-adjusted combat stat accessors."""
from __future__ import annotations

from .models import CombatUnit


def effective_attack(unit: CombatUnit) -> float:
    return unit.template.stats.attack * (0.8 if unit.has_status("staggered") else 1.0)


def effective_magic(unit: CombatUnit) -> float:
    return unit.template.stats.magic * (0.8 if unit.has_status("staggered") else 1.0)


def effective_defense(unit: CombatUnit) -> float:
    return unit.template.stats.defense * (0.9 if unit.has_status("burn") else 1.0)


def effective_spirit(unit: CombatUnit) -> float:
    return unit.template.stats.spirit * (0.9 if unit.has_status("burn") else 1.0)


def effective_speed(unit: CombatUnit) -> float:
    return unit.template.stats.speed * (0.8 if unit.has_status("staggered") else 1.0)
