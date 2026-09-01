"""Action legality and weighted selection for the advanced combat runtime."""
from __future__ import annotations
import random
from typing import Sequence

from .models import BASIC_ATTACK, CombatAction, CombatUnit
from .targeting import enemies, has_target


def selectable_actions(actor: CombatUnit, units: Sequence[CombatUnit]) -> tuple[CombatAction, ...]:
    legal = tuple(
        action
        for action in actor.template.actions
        if action.mp_cost <= actor.mp and action.weight > 0 and has_target(actor, action, units)
    )
    if legal:
        return legal
    return (BASIC_ATTACK,) if any(unit.alive for unit in enemies(actor, units)) else ()


def choose_action(actor: CombatUnit, units: Sequence[CombatUnit], rng: random.Random) -> CombatAction:
    actions = selectable_actions(actor, units)
    if not actions:
        raise ValueError(f"{actor.template.name} has no selectable action")
    return rng.choices(actions, weights=[action.weight for action in actions], k=1)[0]
