"""Per-turn and end-of-round harmful-status runtime behavior."""
from __future__ import annotations
import random
from typing import Sequence

from ..common import round_half_up
from ..sources.combat import load_combat_rules
from .models import CombatUnit
from .temporary_modifiers import tick_temporary_modifiers


def indirect_damage(unit: CombatUnit, rate: float) -> int:
    damage = max(1, round_half_up(unit.max_hp * rate))
    unit.hp = max(0, unit.hp - damage)
    return damage


def bleed_rate(unit: CombatUnit) -> float:
    rules = load_combat_rules()
    state = unit.statuses["bleed"]
    table = rules.bleed_escalated_rates if state.bleed_escalated else rules.bleed_initial_rates
    return table[unit.template.rank]


def clear_bleed_if_full(unit: CombatUnit) -> None:
    if unit.hp >= unit.max_hp:
        unit.statuses.pop("bleed", None)


def _complete_tactical_states(unit: CombatUnit) -> None:
    """Notify source-owned tactical states that this actor's turn completed."""
    for state in tuple(unit.tactical_states.values()):
        callback = getattr(state, "on_turn_complete", None)
        if callable(callback):
            callback()


def complete_turn(unit: CombatUnit, *, acted: bool) -> None:
    try:
        bleed = unit.statuses.get("bleed")
        if bleed is None:
            return
        if acted and unit.alive:
            indirect_damage(unit, bleed_rate(unit))
            if not unit.alive:
                return
            bleed = unit.statuses.get("bleed")
            if bleed is None:
                return
        bleed.bleed_turn_age += 1
        if bleed.bleed_turn_age >= load_combat_rules().bleed_escalation_turns:
            bleed.bleed_escalated = True
    finally:
        _complete_tactical_states(unit)


def turn_is_blocked(unit: CombatUnit, rng: random.Random) -> bool:
    rules = load_combat_rules()
    freeze = unit.statuses.get("freeze")
    if freeze is not None:
        maximum = rules.freeze_max_rounds[unit.template.rank]
        upcoming = freeze.affected_turns + 1
        persistence_start = rules.freeze_guaranteed_rounds + 1
        if unit.template.rank == "ordinary" and upcoming >= persistence_start:
            if rng.random() >= rules.freeze_persist_chance:
                unit.statuses.pop("freeze", None)
            else:
                freeze.affected_turns += 1
                if freeze.affected_turns >= maximum:
                    unit.statuses.pop("freeze", None)
                return True
        elif upcoming <= maximum:
            freeze.affected_turns += 1
            if freeze.affected_turns >= maximum:
                unit.statuses.pop("freeze", None)
            return True
        else:
            unit.statuses.pop("freeze", None)

    stun = unit.statuses.get("stun")
    if stun is not None:
        stun.affected_turns += 1
        blocked = rng.random() < rules.stun_loss_chances[unit.template.rank]
        if stun.affected_turns >= rules.stun_turns:
            unit.statuses.pop("stun", None)
        if blocked:
            return True
    return False


def end_round(units: Sequence[CombatUnit]) -> None:
    rules = load_combat_rules()
    for unit in units:
        if not unit.alive:
            continue
        burn = unit.statuses.get("burn")
        if burn is not None:
            indirect_damage(unit, rules.burn_rates[unit.template.rank])
            if burn.remaining_rounds is not None:
                burn.remaining_rounds -= 1
                if burn.remaining_rounds <= 0:
                    unit.statuses.pop("burn", None)
        if not unit.alive:
            continue
        if unit.has_status("bleed"):
            indirect_damage(unit, bleed_rate(unit))
        staggered = unit.statuses.get("staggered")
        if staggered is not None and staggered.remaining_rounds is not None:
            staggered.remaining_rounds -= 1
            if staggered.remaining_rounds <= 0:
                unit.statuses.pop("staggered", None)
    tick_temporary_modifiers(units)


__all__ = ["bleed_rate", "clear_bleed_if_full", "complete_turn", "end_round", "indirect_damage", "turn_is_blocked"]
