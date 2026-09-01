"""Healing, direct-damage, and status-rider action resolution."""
from __future__ import annotations
import random
from typing import Literal

from ..common import round_half_up
from ..sources.combat import load_combat_rules
from .damage import direct_damage
from .derived_stats import effective_attack, effective_defense, effective_magic, effective_spirit
from .elements import affinity_damage_multiplier, element_affinity, linked_status_affinity_modifier
from .healing import healing_amount
from .hit_evasion import adjusted_hit_chance
from .models import CombatAction, CombatUnit, StatusRider
from .status_runtime import clear_bleed_if_full
from .statuses import apply_status, status_application_chance
from .temporary_modifiers import apply_temporary_modifier, effective_status_resistance


def roll_status(action: CombatAction, rider: StatusRider, target: CombatUnit, rng: random.Random) -> bool:
    if rider.status in target.template.status_immunities:
        return False
    affinity = element_affinity(target, action.element)
    modifier = linked_status_affinity_modifier(action.element, rider.status, affinity)
    if modifier is None:
        return False
    chance = status_application_chance(
        rider.base_chance,
        affinity_modifier=modifier,
        specialist_bonus=rider.specialist_bonus,
        reliability_bonus=rider.reliability_bonus,
        status_resistance=effective_status_resistance(target),
    )
    return rng.random() * 100 < chance and apply_status(target, rider.status)


def clear_statuses(unit: CombatUnit, count: int | Literal["all"]) -> None:
    if count == "all":
        unit.statuses.clear()
        return
    for status in list(unit.statuses)[:max(0, int(count))]:
        unit.statuses.pop(status, None)


def resolve_heal(actor: CombatUnit, action: CombatAction, target: CombatUnit) -> int:
    amount = healing_amount(
        target.max_hp,
        round_half_up(effective_magic(actor)),
        max_hp_percent=action.heal_max_hp_percent,
        magic_scaling=action.heal_magic_scaling,
        potency_multiplier=action.healing_potency,
    )
    before = target.hp
    target.hp = min(target.max_hp, target.hp + amount)
    clear_bleed_if_full(target)
    if action.clear_harmful_statuses:
        clear_statuses(target, action.clear_harmful_statuses)
    for modifier in action.temporary_modifiers:
        apply_temporary_modifier(target, modifier)
    return target.hp - before


def resolve_damage(actor: CombatUnit, action: CombatAction, target: CombatUnit, rng: random.Random) -> int:
    rules = load_combat_rules()
    base_hit = rules.default_player_base_hit if action.base_hit is None else action.base_hit
    if rng.randint(1, 100) > adjusted_hit_chance(base_hit, target.template.evasion):
        return 0

    crit_chance = rules.base_crit_chance if action.crit_chance is None else action.crit_chance
    crit = rng.random() * 100 < max(0.0, min(rules.crit_chance_cap, crit_chance))

    if action.power is None:
        if action.name != "Attack":
            raise ValueError(f"damage action {action.name!r} has no repo/authored Power")
        power = rules.basic_attack_power
    else:
        power = action.power

    if action.damage_kind == "hybrid":
        if action.physical_weight is None or action.magical_weight is None:
            raise ValueError(f"hybrid action {action.name!r} requires authored weights")
        physical_weight = action.physical_weight
        magical_weight = action.magical_weight
    else:
        physical_weight = 0.5 if action.physical_weight is None else action.physical_weight
        magical_weight = 0.5 if action.magical_weight is None else action.magical_weight

    base = direct_damage(
        action.damage_kind,
        attack=effective_attack(actor),
        magic=effective_magic(actor),
        defense=effective_defense(target),
        spirit=effective_spirit(target),
        power=power,
        defense_penetration=action.defense_penetration,
        spirit_penetration=action.spirit_penetration,
        physical_weight=physical_weight,
        magical_weight=magical_weight,
        crit=crit,
        direct_damage_reduction=target.template.direct_damage_reduction,
    )
    damage = round_half_up(
        base
        * affinity_damage_multiplier(element_affinity(target, action.element))
        * action.final_damage_multiplier
    )
    target.hp = max(0, target.hp - damage)
    if action.damage_kind == "physical" and target.has_status("freeze"):
        target.statuses.pop("freeze", None)
    if target.alive:
        for rider in action.status_riders:
            roll_status(action, rider, target, rng)
        for modifier in action.temporary_modifiers:
            apply_temporary_modifier(target, modifier)
    return damage
