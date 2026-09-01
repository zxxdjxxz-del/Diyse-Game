"""Status-adjusted combat stat accessors backed by repository values."""
from __future__ import annotations

from ..sources.combat import load_combat_rules
from .models import CombatUnit


def effective_attack(unit: CombatUnit) -> float:
    rules = load_combat_rules()
    return unit.template.stats.attack * (1.0 - rules.staggered_attack_penalty if unit.has_status("staggered") else 1.0)


def effective_magic(unit: CombatUnit) -> float:
    rules = load_combat_rules()
    return unit.template.stats.magic * (1.0 - rules.staggered_magic_penalty if unit.has_status("staggered") else 1.0)


def effective_defense(unit: CombatUnit) -> float:
    rules = load_combat_rules()
    return unit.template.stats.defense * (1.0 - rules.burn_defense_penalty if unit.has_status("burn") else 1.0)


def effective_spirit(unit: CombatUnit) -> float:
    rules = load_combat_rules()
    return unit.template.stats.spirit * (1.0 - rules.burn_spirit_penalty if unit.has_status("burn") else 1.0)


def effective_speed(unit: CombatUnit) -> float:
    rules = load_combat_rules()
    return unit.template.stats.speed * (1.0 - rules.staggered_speed_penalty if unit.has_status("staggered") else 1.0)
