"""Zevraya-specific split-stat sensitivity adapter.

The main Zevraya runtime historically understands the legacy all-core effective
stat-level overlay. This adapter lets sensitivity work vary ATK/MAG,
DEF/Spirit, and Speed independently without rewriting encounter authority.
"""
from __future__ import annotations

from dataclasses import replace
import random
import statistics
from pathlib import Path

from tools.diysim.overlays import BalanceOverlay, scale_selected_core_stat_level

from . import runtime
from .policy import ZevrayaPolicyConfig
from .repo_loader import ZevrayaRepoData, load_zevraya_repo_data


def apply_zevraya_split_stat_overlay(
    data: ZevrayaRepoData,
    overlay: BalanceOverlay,
    *,
    root: Path | None = None,
) -> ZevrayaRepoData:
    """Apply only split stat-level fields to Zevraya's two boss bodies."""
    if overlay.effective_stat_level_offset:
        raise ValueError("split Zevraya adapter does not accept legacy all-core offsets")

    def scale_form(stats, displayed_level: int):
        scaled = stats
        if overlay.offensive_stat_level_offset:
            scaled = scale_selected_core_stat_level(
                scaled,
                displayed_level=displayed_level,
                level_offset=overlay.offensive_stat_level_offset,
                stat_keys=("attack", "magic"),
                root=root,
            )
        if overlay.defensive_stat_level_offset:
            scaled = scale_selected_core_stat_level(
                scaled,
                displayed_level=displayed_level,
                level_offset=overlay.defensive_stat_level_offset,
                stat_keys=("defense", "spirit"),
                root=root,
            )
        if overlay.speed_stat_level_offset:
            scaled = scale_selected_core_stat_level(
                scaled,
                displayed_level=displayed_level,
                level_offset=overlay.speed_stat_level_offset,
                stat_keys=("speed",),
                root=root,
            )
        return scaled

    return replace(
        data,
        blood_matron=replace(
            data.blood_matron,
            stats=scale_form(data.blood_matron.stats, 28),
        ),
        perfected_war_mother=replace(
            data.perfected_war_mother,
            stats=scale_form(data.perfected_war_mother.stats, 29),
        ),
    )


def simulate_matron_zevraya_split(
    *,
    player_level: int = 24,
    structure_mode: runtime.StructureMode = "owner",
    strategy: runtime.Strategy = "rush",
    reservoir_plan: tuple[str, ...] | None = None,
    overlay: BalanceOverlay = BalanceOverlay(),
    policy: ZevrayaPolicyConfig = ZevrayaPolicyConfig(),
    use_prepared_inventory: bool = True,
    runs: int = 1_000,
    seed: int = 104,
    root: Path | None = None,
) -> runtime.ZevrayaSimulationSummary:
    """Run Zevraya with independently selected stat-level offsets."""
    if runs < 1:
        raise ValueError("runs must be positive")
    if overlay.effective_stat_level_offset:
        raise ValueError("use the normal Zevraya simulator for legacy all-core offsets")

    normalized_plan = runtime._normalize_reservoir_plan(strategy, reservoir_plan)
    data = apply_zevraya_split_stat_overlay(
        load_zevraya_repo_data(root=root),
        overlay,
        root=root,
    )
    power_only = BalanceOverlay(
        direct_damage_power_multiplier=overlay.direct_damage_power_multiplier,
    )
    outcomes = [
        runtime._run_zevraya_with_data(
            random.Random(seed + index),
            data,
            player_level=player_level,
            structure_mode=structure_mode,
            strategy=strategy,
            reservoir_plan=normalized_plan,
            overlay=power_only,
            policy=policy,
            use_prepared_inventory=use_prepared_inventory,
            max_rounds=40,
            root=root,
        )
        for index in range(runs)
    ]
    rounds = [outcome.rounds for outcome in outcomes]
    return runtime.ZevrayaSimulationSummary(
        runs=runs,
        player_level=player_level,
        structure_mode=structure_mode,
        strategy=strategy,
        reservoir_plan=normalized_plan,
        prepared_inventory=use_prepared_inventory,
        power_multiplier=overlay.direct_damage_power_multiplier,
        effective_stat_level_offset=0,
        win_rate=sum(outcome.winner == "party" for outcome in outcomes) / runs,
        wipe_rate=sum(outcome.winner == "enemy" for outcome in outcomes) / runs,
        any_ko_rate=sum(outcome.any_party_ko for outcome in outcomes) / runs,
        mean_rounds=statistics.fmean(rounds),
        median_rounds=float(statistics.median(rounds)),
        p10_rounds=runtime._percentile(rounds, 0.10),
        p90_rounds=runtime._percentile(rounds, 0.90),
        mean_remaining_party_hp=statistics.fmean(outcome.party_hp_fraction for outcome in outcomes),
        mean_remaining_party_mp=statistics.fmean(outcome.party_mp_fraction for outcome in outcomes),
        form2_reach_rate=sum(outcome.form2_reached for outcome in outcomes) / runs,
        mean_reservoirs_destroyed=statistics.fmean(outcome.reservoirs_destroyed for outcome in outcomes),
        mean_brood_deployments=statistics.fmean(outcome.brood_deployments for outcome in outcomes),
        mean_brood_actions=statistics.fmean(outcome.brood_actions for outcome in outcomes),
        mean_items_used=statistics.fmean(outcome.items_used for outcome in outcomes),
        mean_hunter_measure_establishments=statistics.fmean(outcome.hunter_measure_establishments for outcome in outcomes),
        mean_sustenance_heal_uses=statistics.fmean(outcome.sustenance_heal_uses for outcome in outcomes),
        mean_reconstruction_uses=statistics.fmean(outcome.reconstruction_uses for outcome in outcomes),
        mean_conduction_uses=statistics.fmean(outcome.conduction_uses for outcome in outcomes),
        mean_plating_uses=statistics.fmean(outcome.plating_uses for outcome in outcomes),
        bleed_exposure_rate=sum(outcome.bleed_exposed for outcome in outcomes) / runs,
        control_exposure_rate=sum(outcome.control_exposed for outcome in outcomes) / runs,
    )


__all__ = [
    "apply_zevraya_split_stat_overlay",
    "simulate_matron_zevraya_split",
]
