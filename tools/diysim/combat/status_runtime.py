"""Per-turn and end-of-round harmful-status runtime behavior."""
from __future__ import annotations
import random
from typing import Sequence

from ..common import round_half_up
from .models import CombatUnit
from .statuses import (
    BLEED_ESCALATED_RATE,
    BLEED_INITIAL_RATE,
    BURN_RATE,
    FREEZE_MAX_AFFECTED_ROUNDS,
    STUN_LOSS_CHANCE,
)


def indirect_damage(unit: CombatUnit, rate: float) -> int:
    damage = max(1, round_half_up(unit.max_hp * rate))
    unit.hp = max(0, unit.hp - damage)
    return damage


def bleed_rate(unit: CombatUnit) -> float:
    state = unit.statuses["bleed"]
    table = BLEED_ESCALATED_RATE if state.bleed_escalated else BLEED_INITIAL_RATE
    return table[unit.template.rank]


def clear_bleed_if_full(unit: CombatUnit) -> None:
    if unit.hp >= unit.max_hp:
        unit.statuses.pop("bleed", None)


def complete_turn(unit: CombatUnit, *, acted: bool) -> None:
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
    if bleed.bleed_turn_age >= 3:
        bleed.bleed_escalated = True


def turn_is_blocked(unit: CombatUnit, rng: random.Random) -> bool:
    freeze = unit.statuses.get("freeze")
    if freeze is not None:
        maximum = FREEZE_MAX_AFFECTED_ROUNDS[unit.template.rank]
        upcoming = freeze.affected_turns + 1
        if unit.template.rank == "ordinary" and upcoming >= 3:
            if rng.random() >= 0.80:
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
        blocked = rng.random() < STUN_LOSS_CHANCE[unit.template.rank]
        if stun.affected_turns >= 4:
            unit.statuses.pop("stun", None)
        if blocked:
            return True
    return False


def end_round(units: Sequence[CombatUnit]) -> None:
    for unit in units:
        if not unit.alive:
            continue
        burn = unit.statuses.get("burn")
        if burn is not None:
            indirect_damage(unit, BURN_RATE[unit.template.rank])
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
