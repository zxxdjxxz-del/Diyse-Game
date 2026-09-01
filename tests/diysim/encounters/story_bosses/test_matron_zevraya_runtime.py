import random

from tools.diysim.encounters.story_bosses.matron_zevraya import (
    load_zevraya_working_snapshot,
    run_matron_zevraya,
    simulate_matron_zevraya,
)
from tools.diysim.overlays import BalanceOverlay


def test_zevraya_working_snapshot_has_finite_prepared_inventory() -> None:
    snapshot = load_zevraya_working_snapshot()
    assert snapshot.prepared_consumables == {
        "Restorative Salve": 3,
        "Deepflow Tonic": 2,
        "Trauma Remedy": 2,
        "Stability Remedy": 2,
        "Rousing Salts": 2,
    }


def test_zevraya_runtime_executes_owner_and_non_diluting_modes() -> None:
    owner = run_matron_zevraya(
        random.Random(104),
        player_level=24,
        structure_mode="owner",
        strategy="rush",
        max_rounds=40,
    )
    candidate = run_matron_zevraya(
        random.Random(104),
        player_level=24,
        structure_mode="non_diluting",
        strategy="dismantle",
        max_rounds=40,
    )

    assert owner.winner in {"party", "enemy", "draw"}
    assert candidate.winner in {"party", "enemy", "draw"}
    assert 1 <= owner.rounds <= 40
    assert 1 <= candidate.rounds <= 40
    assert owner.form2_reached
    assert candidate.form2_reached
    assert 0 <= owner.reservoirs_destroyed <= 4
    assert 0 <= candidate.reservoirs_destroyed <= 4


def test_zevraya_small_simulation_accepts_high_side_and_plus5() -> None:
    summary = simulate_matron_zevraya(
        player_level=28,
        structure_mode="non_diluting",
        strategy="dismantle",
        overlay=BalanceOverlay(
            direct_damage_power_multiplier=1.20,
            effective_stat_level_offset=5,
        ),
        runs=3,
        seed=106,
    )
    assert summary.runs == 3
    assert summary.player_level == 28
    assert summary.power_multiplier == 1.20
    assert summary.effective_stat_level_offset == 5
    assert summary.win_rate + summary.wipe_rate <= 1.0
    assert 0.0 <= summary.mean_reservoirs_destroyed <= 4.0


def test_zevraya_rush_does_not_ignore_deployed_brood() -> None:
    summary = simulate_matron_zevraya(
        player_level=24,
        structure_mode="non_diluting",
        strategy="rush",
        overlay=BalanceOverlay(direct_damage_power_multiplier=1.20),
        runs=25,
        seed=106,
    )

    # Rush focuses Zevraya rather than pre-emptively dismantling Reservoirs,
    # but a deployed Brood is a visible finite hostile body and must be answered.
    assert summary.mean_brood_deployments >= 1.5
    assert summary.mean_brood_actions < 5.0
