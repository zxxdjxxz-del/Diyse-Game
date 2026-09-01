"""Action legality and repo-backed selection fallback for the advanced runtime."""
from __future__ import annotations
import random
from typing import Sequence

from ..sources.enemies import load_enemy_system_rules
from .basic_attack import basic_attack_action
from .models import CombatAction, CombatUnit
from .targeting import enemies, has_target


def selectable_actions(actor: CombatUnit, units: Sequence[CombatUnit]) -> tuple[CombatAction, ...]:
    legal = tuple(
        action
        for action in actor.template.actions
        if action.mp_cost <= actor.mp
        and (action.weight is None or action.weight > 0)
        and has_target(actor, action, units)
    )
    if legal:
        return legal
    return (basic_attack_action(),) if any(unit.alive for unit in enemies(actor, units)) else ()


def choose_action(actor: CombatUnit, units: Sequence[CombatUnit], rng: random.Random) -> CombatAction:
    actions = selectable_actions(actor, units)
    if not actions:
        raise ValueError(f"{actor.template.name} has no selectable action")

    weights = tuple(action.weight for action in actions)
    if all(weight is None for weight in weights):
        if actor.side == "enemy":
            rule = load_enemy_system_rules().missing_weight_selection
            if rule != "uniform":
                raise ValueError(f"unsupported repo enemy-selection rule: {rule}")
        # Party-side unweighted selection is a simulator policy, not Diyse canon.
        return rng.choice(actions)
    if any(weight is None for weight in weights):
        raise ValueError(
            f"{actor.template.name} mixes explicit and missing action weights; "
            "repo authority must resolve the selection model before simulation"
        )
    return rng.choices(actions, weights=weights, k=1)[0]
