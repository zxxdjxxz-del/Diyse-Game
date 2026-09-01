from __future__ import annotations

import random

from tools.diysim.combat import (
    ActionProfile,
    BattleScenario,
    CombatantTemplate,
    adjusted_hit_chance,
    direct_damage,
    load_combat_rules,
    run_battle,
    simulate,
)
from tools.diysim.progression import Stats


def test_hit_evasion_uses_repo_clamp() -> None:
    rules = load_combat_rules()
    assert adjusted_hit_chance(rules.max_hit_chance + 50, 0) == rules.max_hit_chance
    assert adjusted_hit_chance(0, rules.max_hit_chance + 50) == rules.min_hit_chance


def test_direct_damage_formula_and_repo_layers() -> None:
    rules = load_combat_rules()
    base = direct_damage("physical", attack=100, magic=0, defense=100, spirit=0, power=100)
    penetrated = direct_damage(
        "physical",
        attack=100,
        magic=0,
        defense=100,
        spirit=0,
        power=100,
        defense_penetration=rules.penetration_cap,
    )
    critical = direct_damage("physical", attack=100, magic=0, defense=100, spirit=0, power=100, crit=True)
    reduced = direct_damage(
        "physical",
        attack=100,
        magic=0,
        defense=100,
        spirit=0,
        power=100,
        direct_damage_reduction=0.50,
    )

    assert penetrated > base
    assert critical == round(base * rules.crit_multiplier)
    assert reduced < base


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
    assert result > 0


def _tiny_scenario() -> BattleScenario:
    party = CombatantTemplate(
        "Party",
        "party",
        Stats(300, 0, 100, 0, 50, 50, 40),
        actions=(ActionProfile("Attack", crit_chance=0),),
    )
    enemy = CombatantTemplate(
        "Enemy",
        "enemy",
        Stats(200, 0, 60, 0, 50, 50, 30),
        actions=(ActionProfile("Attack", crit_chance=0),),
    )
    return BattleScenario((party,), (enemy,), max_rounds=20)


def test_seeded_battle_is_deterministic() -> None:
    scenario = _tiny_scenario()
    assert run_battle(scenario, random.Random(123)) == run_battle(scenario, random.Random(123))


def test_monte_carlo_summary_is_repeatable() -> None:
    scenario = _tiny_scenario()
    first = simulate(scenario, runs=100, seed=77)
    second = simulate(scenario, runs=100, seed=77)
    assert first == second
    assert first.party_wins + first.enemy_wins + first.draws == 100
