from __future__ import annotations

from tools.diysim.common import round_half_up
from tools.diysim.progression import (
    ProgressionSegment,
    class_multipliers,
    cumulative_exp,
    exp_at_level_progress,
    level_cap,
    level_from_exp,
    natural_stats,
    neutral_natural_stats,
    project_progression,
    required_average_exp_per_encounter,
)
from tools.diysim.sources.progression import load_progression_rules


def test_neutral_stat_calculator_uses_repo_coefficients() -> None:
    rules = load_progression_rules()
    for level in (1, max(1, rules.level_cap // 2), rules.level_cap):
        x = level - 1
        calculated = neutral_natural_stats(level)
        for key, (base, linear, quadratic) in rules.natural_coefficients.items():
            assert calculated[key] == base + linear * x + quadratic * x * x


def test_class_multiplier_then_equipment_uses_repo_package() -> None:
    rules = load_progression_rules()
    class_name = next(iter(class_multipliers()))
    raw = neutral_natural_stats(1)
    stats = natural_stats(1, class_name, {"hp": 10, "attack": 2})
    package = rules.class_multipliers[class_name]

    assert stats.hp == round_half_up(raw["hp"] * package["hp"]) + 10
    assert stats.attack == round_half_up(raw["attack"] * package["attack"]) + 2
    assert stats.defense == round_half_up(raw["defense"] * package["defense"])


def test_exp_lookup_matches_repo_published_table() -> None:
    rules = load_progression_rules()
    sampled_levels = (1, max(2, rules.level_cap // 2), rules.level_cap)
    for level in sampled_levels:
        assert cumulative_exp(level) == rules.cumulative_exp[level]
        assert level_from_exp(rules.cumulative_exp[level]) == level
    assert level_cap() == max(rules.cumulative_exp)


def test_progression_projection_tracks_synthetic_checkpoints() -> None:
    start_level = min(20, level_cap() - 2)
    start = cumulative_exp(start_level)
    route = (
        ProgressionSegment("Synthetic encounters", count=10, exp_each=500, completion_rate=0.7),
        ProgressionSegment("Synthetic fixed reward", flat_exp=2_000),
    )
    projection = project_progression(start, route)
    assert projection.start_level == start_level
    assert projection.total_gained_exp == 5_500
    assert projection.final_exp == start + 5_500
    assert len(projection.checkpoints) == 2
    assert projection.checkpoints[0].gained_exp == 3_500
    assert projection.checkpoints[1].segment == "Synthetic fixed reward"


def test_required_average_exp_solver_hits_target_checkpoint() -> None:
    start_level = min(20, level_cap() - 3)
    target_level = start_level + 2
    start = cumulative_exp(start_level)
    target = exp_at_level_progress(target_level, 0.5)
    average = required_average_exp_per_encounter(
        start_exp=start,
        target_level=target_level,
        target_level_progress=0.5,
        encounter_count=10,
        fixed_exp=1_000,
    )
    assert average == (target - start - 1_000) / 10
