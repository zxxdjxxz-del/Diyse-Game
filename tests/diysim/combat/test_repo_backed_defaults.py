from __future__ import annotations

import random

from tools.diysim.combat import CombatAction, CombatUnit, Combatant, basic_attack_action
from tools.diysim.combat.action_selection import choose_action
from tools.diysim.progression import Stats
from tools.diysim.sources.combat import load_combat_rules


def test_basic_attack_is_built_from_repo_combat_authority() -> None:
    rules = load_combat_rules()
    action = basic_attack_action()

    assert action.power == rules.basic_attack_power
    assert action.base_hit == rules.default_player_base_hit
    assert action.damage_kind is not None
    assert action.element is not None
    assert action.weight is None


def test_missing_action_weights_use_uniform_selection_without_numeric_fallback() -> None:
    actor = CombatUnit(
        Combatant(
            "Synthetic Actor",
            "party",
            Stats(100, 0, 20, 20, 10, 10, 20),
            actions=(
                CombatAction("One", power=100, weight=None),
                CombatAction("Two", power=100, weight=None),
            ),
        ),
        0,
    )
    target = CombatUnit(Combatant("Synthetic Target", "enemy", Stats(100, 0, 1, 1, 10, 10, 10)), 1)

    selected = {choose_action(actor, (actor, target), random.Random(seed)).name for seed in range(20)}
    assert selected == {"One", "Two"}
