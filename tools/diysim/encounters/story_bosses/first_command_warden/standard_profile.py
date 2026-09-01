"""Standard cross-boss DiySim pressure wrapper for First Command Warden."""
from __future__ import annotations

from dataclasses import replace
import math
from pathlib import Path
import random
import statistics

from tools.diysim.overlays import (
    BalanceOverlay,
    STANDARD_BOSS_OFFENSIVE_LEVEL_OFFSET,
    STANDARD_BOSS_POWER_MULTIPLIER,
    scale_selected_core_stat_level,
)

from .policy import WardenPolicyConfig
from .repo_loader import load_first_command_warden_repo_data
from .runtime import WardenSimulationSummary, _run_warden_with_data


def simulate_first_command_warden_standard_profile(
    *,
    player_level: int = 11,
    policy: WardenPolicyConfig = WardenPolicyConfig(),
    use_prepared_inventory: bool = True,
    runs: int = 2_000,
    seed: int = 105,
    root: Path | None = None,
) -> WardenSimulationSummary:
    """Run Warden with +5 ATK/MAG and x1.20 direct-damage Power.

    DEF, Spirit, Speed, HP and MP remain at authored owner values.
    """
    if runs < 1:
        raise ValueError("runs must be positive")

    data = load_first_command_warden_repo_data(root=root)
    scaled_stats = scale_selected_core_stat_level(
        data.warden.stats,
        displayed_level=data.displayed_level,
        level_offset=STANDARD_BOSS_OFFENSIVE_LEVEL_OFFSET,
        stat_keys=("attack", "magic"),
        root=root,
    )
    data = replace(data, warden=replace(data.warden, stats=scaled_stats))
    power_only = BalanceOverlay(
        direct_damage_power_multiplier=STANDARD_BOSS_POWER_MULTIPLIER,
    )

    outcomes = [
        _run_warden_with_data(
            random.Random(seed + index),
            data,
            player_level=player_level,
            overlay=power_only,
            policy=policy,
            max_rounds=30,
            use_prepared_inventory=use_prepared_inventory,
            root=root,
        )
        for index in range(runs)
    ]
    rounds = sorted(outcome.rounds for outcome in outcomes)

    def percentile(fraction: float) -> float:
        index = max(0, math.ceil(fraction * len(rounds)) - 1)
        return float(rounds[index])

    return WardenSimulationSummary(
        runs=runs,
        player_level=player_level,
        prepared_inventory=use_prepared_inventory,
        power_multiplier=STANDARD_BOSS_POWER_MULTIPLIER,
        effective_stat_level_offset=0,
        win_rate=sum(outcome.winner == "party" for outcome in outcomes) / runs,
        wipe_rate=sum(outcome.winner == "enemy" for outcome in outcomes) / runs,
        any_ko_rate=sum(outcome.any_party_ko for outcome in outcomes) / runs,
        mean_rounds=statistics.fmean(rounds),
        median_rounds=float(statistics.median(rounds)),
        p10_rounds=percentile(0.10),
        p90_rounds=percentile(0.90),
        mean_remaining_party_hp=statistics.fmean(outcome.party_hp_fraction for outcome in outcomes),
        mean_remaining_party_mp=statistics.fmean(outcome.party_mp_fraction for outcome in outcomes),
        state_b_reach_rate=sum(outcome.state_b_reached for outcome in outcomes) / runs,
        mean_ruling_attempts=statistics.fmean(outcome.ruling_attempts for outcome in outcomes),
        mean_ruling_resolutions=statistics.fmean(outcome.ruling_resolutions for outcome in outcomes),
        mean_ruling_disruptions=statistics.fmean(outcome.ruling_disruptions for outcome in outcomes),
        mean_seal_reprisals=statistics.fmean(outcome.seal_reprisals for outcome in outcomes),
        mean_analogue_uses=statistics.fmean(outcome.analogue_uses for outcome in outcomes),
        mean_items_used=statistics.fmean(outcome.items_used for outcome in outcomes),
        mean_hunter_measure_establishments=statistics.fmean(
            outcome.hunter_measure_establishments for outcome in outcomes
        ),
        stun_exposure_rate=sum(outcome.stun_exposed for outcome in outcomes) / runs,
        staggered_exposure_rate=sum(outcome.staggered_exposed for outcome in outcomes) / runs,
    )


__all__ = ["simulate_first_command_warden_standard_profile"]
