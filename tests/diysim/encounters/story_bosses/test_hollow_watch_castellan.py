from __future__ import annotations

import random

from tools.diysim.encounters.story_bosses.hollow_watch_castellan import (
    SmartPolicyConfig,
    action_set,
    run_hollow_watch_smart,
    simulate_hollow_watch_smart,
)
from tools.diysim.encounters.story_bosses.hollow_watch_castellan.runtime import _weighted_boss_action


def test_historical_and_current_mp_rules_are_kept_separate() -> None:
    historical = action_set("v93_oracle")
    current = action_set("current")

    assert historical.crest_strike.mp_cost == 10
    assert historical.resonant_pulse.mp_cost == 12
    assert historical.mend.mp_cost == 16
    assert historical.clear_warding.mp_cost == 18

    assert current.crest_strike.mp_cost == 9
    assert current.resonant_pulse.mp_cost == 10
    assert current.mend.mp_cost == 14
    assert current.clear_warding.mp_cost == 15

    assert historical.linebreaker_thrust.mp_cost == current.linebreaker_thrust.mp_cost == 10


def test_repetition_locked_castellan_actions_cannot_repeat() -> None:
    rng = random.Random(11)
    assert {
        _weighted_boss_action("fortress", "Bastion Sweep", rng).name
        for _ in range(100)
    } == {"Wallbound Strike"}

    walking_after_slam = {
        _weighted_boss_action("walking", "Fortress Slam", rng).name
        for _ in range(500)
    }
    assert "Fortress Slam" not in walking_after_slam
    assert walking_after_slam <= {"Iron Pursuit", "Wall-Shear Sweep"}


def test_smart_policy_destroys_ballista_before_heavy_bolt() -> None:
    for seed in range(50):
        outcome = run_hollow_watch_smart(
            random.Random(seed),
            ruleset="v93_oracle",
        )
        assert outcome.winner == "party"
        assert outcome.ballista_shots == 0
        assert outcome.castellan_state_reached == "walking"


def test_historical_v93_oracle_shape_is_reproduced() -> None:
    summary = simulate_hollow_watch_smart(
        ruleset="v93_oracle",
        policy=SmartPolicyConfig(heal_trigger_hp_fraction=0.55),
        runs=2_000,
        seed=93,
    )

    assert summary.win_rate == 1.0
    assert summary.wipe_rate == 0.0
    assert summary.any_ko_rate == 0.0
    assert 6.15 <= summary.mean_rounds <= 6.45
    assert summary.median_rounds == 6.0
    assert summary.p10_rounds == 6.0
    assert summary.p90_rounds == 7.0
    assert 0.64 <= summary.mean_remaining_party_hp <= 0.71
    assert summary.mean_ballista_shots == 0.0
    assert 0.10 <= summary.staggered_exposure_rate <= 0.20


def test_current_mp_reduction_is_not_frozen_to_v93_oracle() -> None:
    historical = simulate_hollow_watch_smart(
        ruleset="v93_oracle",
        runs=1_000,
        seed=9301,
    )
    current = simulate_hollow_watch_smart(
        ruleset="current",
        runs=1_000,
        seed=9301,
    )

    assert current.win_rate == 1.0
    assert current.mean_rounds < historical.mean_rounds
    assert current.median_rounds <= historical.median_rounds
