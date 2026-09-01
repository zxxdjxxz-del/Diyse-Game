from __future__ import annotations

import random

from tools.diysim.combat import (
    ActionProfile,
    BattleScenario,
    CombatantTemplate,
    adjusted_hit_chance,
    direct_damage,
    run_battle,
    simulate,
)
from tools.diysim.progression import Stats


def test_hit_evasion_clamp() -> None:
    assert adjusted_hit_chance(100, 15) == 85
    assert adjusted_hit_chance(200, 0) == 100
    assert adjusted_hit_chance(10, 50) == 5


def test_direct_damage_formula_and_layers() -> None:
    assert direct_damage("physical", attack=100, magic=0, defense=100, spirit=0, power=100) == 50
    assert direct_damage("physical", attack=100, magic=0, defense=100, spirit=0, power=100, defense_penetration=0.75) == 80
    assert direct_damage("physical", attack=100, magic=0, defense=100, spirit=0, power=100, crit=True) == 75
    assert direct_damage("physical", attack=100, magic=0, defense=100, spirit=0, power=100, direct_damage_reduction=0.50) == 25


def test_hybrid_resolves_axes_independently() -> None:
    result = direct_damage(
        "hybrid",
        attack=120,
        magic=80,
        defense=100,
        spirit=40,
        power=100,
        physical_weight=0.75,
        magical_weight=0.25,
    )
    assert result == 62


def _tiny_scenario() -> BattleScenario:
    party = CombatantTemplate(
        "Party",
        "party",
        Stats(300, 0, 100, 0, 50, 50, 40),
        actions=(ActionProfile("Attack", power=100, crit_chance=0),),
    )
    enemy = CombatantTemplate(
        "Enemy",
        "enemy",
        Stats(200, 0, 60, 0, 50, 50, 30),
        actions=(ActionProfile("Attack", power=100, crit_chance=0),),
    )
    return BattleScenario((party,), (enemy,), max_rounds=20)


def test_seeded_battle_is_deterministic() -> None:
    scenario = _tiny_scenario()
    first = run_battle(scenario, random.Random(123))
    second = run_battle(scenario, random.Random(123))
    assert first == second


def test_monte_carlo_summary_is_repeatable() -> None:
    scenario = _tiny_scenario()
    first = simulate(scenario, runs=100, seed=77)
    second = simulate(scenario, runs=100, seed=77)
    assert first == second
    assert first.party_wins + first.enemy_wins + first.draws == 100
