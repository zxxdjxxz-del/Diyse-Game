from __future__ import annotations

import random

from tools.diysim.core import (
    ActionProfile,
    BattleScenario,
    CombatantTemplate,
    Stats,
    adjusted_hit_chance,
    cumulative_exp,
    direct_damage,
    level_from_exp,
    natural_stats,
    neutral_natural_stats,
    run_battle,
    simulate,
)
from tools.diysim.progression import (
    ProgressionSegment,
    exp_at_level_progress,
    project_progression,
    required_average_exp_per_encounter,
)


def test_level_one_neutral_anchor() -> None:
    assert neutral_natural_stats(1) == {
        "hp": 220.0,
        "mp": 28.0,
        "attack": 18.0,
        "magic": 18.0,
        "defense": 16.0,
        "spirit": 16.0,
        "speed": 22.0,
    }


def test_class_multiplier_then_equipment() -> None:
    stats = natural_stats(1, "Crest Knight", {"hp": 10, "attack": 2})
    assert stats.hp == 241
    assert stats.attack == 21
    assert stats.defense == 18


def test_exp_curve_matches_current_table_anchors() -> None:
    assert cumulative_exp(17) == 25_600
    assert cumulative_exp(18) == 28_900
    assert cumulative_exp(62) == 448_100
    assert cumulative_exp(70) == 594_100
    assert level_from_exp(448_099) == 61
    assert level_from_exp(448_100) == 62
    assert level_from_exp(999_999) == 70


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
    a = run_battle(scenario, random.Random(123))
    b = run_battle(scenario, random.Random(123))
    assert a == b


def test_monte_carlo_summary_is_repeatable() -> None:
    scenario = _tiny_scenario()
    a = simulate(scenario, runs=100, seed=77)
    b = simulate(scenario, runs=100, seed=77)
    assert a == b
    assert a.party_wins + a.enemy_wins + a.draws == 100


def test_progression_projection_tracks_checkpoints() -> None:
    start = cumulative_exp(20)
    route = (
        ProgressionSegment("Field encounters", count=10, exp_each=500, completion_rate=0.7),
        ProgressionSegment("Boss", flat_exp=2_000),
    )
    projection = project_progression(start, route)
    assert projection.start_level == 20
    assert projection.total_gained_exp == 5_500
    assert projection.final_exp == start + 5_500
    assert len(projection.checkpoints) == 2
    assert projection.checkpoints[0].gained_exp == 3_500
    assert projection.checkpoints[1].segment == "Boss"


def test_required_average_exp_solver_hits_target_checkpoint() -> None:
    start = cumulative_exp(20)
    target = exp_at_level_progress(22, 0.5)
    average = required_average_exp_per_encounter(
        start_exp=start,
        target_level=22,
        target_level_progress=0.5,
        encounter_count=10,
        fixed_exp=1_000,
    )
    assert average == (target - start - 1_000) / 10
