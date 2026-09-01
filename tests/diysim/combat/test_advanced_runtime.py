from __future__ import annotations

import random

from tools.diysim.combat import (
    AdvancedBattleScenario,
    CombatAction,
    Combatant,
    run_advanced_battle,
    simulate_advanced,
)
from tools.diysim.progression import Stats


def test_advanced_battle_spends_mp_and_falls_back_to_basic_attack() -> None:
    party = Combatant(
        "Caster",
        "party",
        Stats(500, 5, 100, 100, 50, 50, 60),
        actions=(CombatAction("Burst", mp_cost=5, damage_kind="magical", power=200, crit_chance=0),),
    )
    enemy = Combatant(
        "Target",
        "enemy",
        Stats(500, 0, 1, 1, 100, 100, 10),
        actions=(CombatAction("Tap", power=1, crit_chance=0),),
    )
    outcome = run_advanced_battle((party,), (enemy,), random.Random(7), max_rounds=10)
    assert outcome.winner == "party"
    assert outcome.party_mp_fraction == 0.0


def test_advanced_battle_applies_elemental_weakness() -> None:
    party = Combatant(
        "Fire Caster",
        "party",
        Stats(500, 0, 1, 120, 50, 50, 60),
        actions=(CombatAction("Flame", damage_kind="magical", element="fire", power=200, crit_chance=0),),
    )
    enemy = Combatant(
        "Weak Target",
        "enemy",
        Stats(100, 0, 1, 1, 50, 100, 10),
        actions=(CombatAction("Tap", power=1, crit_chance=0),),
        elemental_affinities={"fire": "weak"},
    )
    outcome = run_advanced_battle((party,), (enemy,), random.Random(3), max_rounds=2)
    assert outcome.winner == "party"
    assert outcome.rounds == 1


def test_advanced_monte_carlo_is_repeatable() -> None:
    party = Combatant("Hero", "party", Stats(300, 0, 100, 0, 50, 50, 40))
    enemy = Combatant("Enemy", "enemy", Stats(200, 0, 60, 0, 50, 50, 30))
    scenario = AdvancedBattleScenario((party,), (enemy,), max_rounds=20)

    first = simulate_advanced(scenario, runs=100, seed=77)
    second = simulate_advanced(scenario, runs=100, seed=77)

    assert first == second
    assert first.party_wins + first.enemy_wins + first.draws == 100
