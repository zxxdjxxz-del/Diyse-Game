"""Status- and temporary-modifier-adjusted combat stat accessors."""
from __future__ import annotations

from ..sources.combat import load_combat_rules
from .models import CombatUnit
from .temporary_modifiers import effective_core_stat


def effective_attack(unit: CombatUnit) -> float:
    rules = load_combat_rules()
    status = (-rules.staggered_attack_penalty * 100.0,) if unit.has_status("staggered") else ()
    return effective_core_stat(unit, "attack", extra_percentages=status)


def effective_magic(unit: CombatUnit) -> float:
    rules = load_combat_rules()
    status = (-rules.staggered_magic_penalty * 100.0,) if unit.has_status("staggered") else ()
    return effective_core_stat(unit, "magic", extra_percentages=status)


def effective_defense(unit: CombatUnit) -> float:
    rules = load_combat_rules()
    status = (-rules.burn_defense_penalty * 100.0,) if unit.has_status("burn") else ()
    return effective_core_stat(unit, "defense", extra_percentages=status)


def effective_spirit(unit: CombatUnit) -> float:
    rules = load_combat_rules()
    status = (-rules.burn_spirit_penalty * 100.0,) if unit.has_status("burn") else ()
    return effective_core_stat(unit, "spirit", extra_percentages=status)


def effective_speed(unit: CombatUnit) -> float:
    rules = load_combat_rules()
    status = (-rules.staggered_speed_penalty * 100.0,) if unit.has_status("staggered") else ()
    return effective_core_stat(unit, "speed", extra_percentages=status)
