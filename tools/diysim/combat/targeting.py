"""Target eligibility and target selection for the advanced combat runtime."""
from __future__ import annotations
import random
from typing import Sequence

from .models import CombatAction, CombatUnit


def allies(actor: CombatUnit, units: Sequence[CombatUnit]) -> list[CombatUnit]:
    return [unit for unit in units if unit.side == actor.side]


def enemies(actor: CombatUnit, units: Sequence[CombatUnit]) -> list[CombatUnit]:
    return [unit for unit in units if unit.side != actor.side]


def has_target(actor: CombatUnit, action: CombatAction, units: Sequence[CombatUnit]) -> bool:
    if action.target_side == "enemy":
        return any(unit.alive for unit in enemies(actor, units))
    candidates = [actor] if action.target_side == "self" else [unit for unit in allies(actor, units) if unit.alive]
    if action.action_kind != "heal":
        return any(unit.alive for unit in candidates)
    return any(
        unit.alive
        and (unit.hp < unit.max_hp or (action.clear_harmful_statuses and unit.statuses))
        for unit in candidates
    )


def select_targets(
    actor: CombatUnit,
    action: CombatAction,
    units: Sequence[CombatUnit],
    rng: random.Random,
) -> list[CombatUnit]:
    if action.target_side == "enemy":
        candidates = [unit for unit in enemies(actor, units) if unit.alive]
    elif action.target_side == "self":
        candidates = [actor] if actor.alive else []
    else:
        candidates = [unit for unit in allies(actor, units) if unit.alive]

    if action.action_kind == "heal":
        useful = [
            unit
            for unit in candidates
            if unit.hp < unit.max_hp or (action.clear_harmful_statuses and unit.statuses)
        ]
        if useful:
            candidates = useful

    if action.target_scope == "all":
        return candidates
    if not candidates:
        return []
    if action.action_kind == "heal" and action.target_side != "enemy":
        return [min(candidates, key=lambda unit: (unit.hp / unit.max_hp, unit.stable_index))]
    return [rng.choice(candidates)]
