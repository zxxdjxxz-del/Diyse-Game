"""Non-destructive enemy-stat sweep overlays for the simple runtime."""
from __future__ import annotations

from dataclasses import replace
from itertools import product
from typing import Sequence

from ..common import round_half_up
from ..combat.simple_runtime import BattleScenario, simulate


def scale_enemy_side(
    scenario: BattleScenario,
    *,
    hp_multiplier: float = 1.0,
    attack_multiplier: float = 1.0,
    defense_multiplier: float = 1.0,
) -> BattleScenario:
    if min(hp_multiplier, attack_multiplier, defense_multiplier) <= 0:
        raise ValueError("multipliers must be positive")
    scaled = []
    for enemy in scenario.enemies:
        stats = enemy.stats
        scaled_stats = replace(
            stats,
            hp=max(1, round_half_up(stats.hp * hp_multiplier)),
            attack=max(0, round_half_up(stats.attack * attack_multiplier)),
            defense=max(0, round_half_up(stats.defense * defense_multiplier)),
        )
        scaled.append(replace(enemy, stats=scaled_stats))
    return replace(scenario, enemies=tuple(scaled))


def sweep_enemy_stats(
    scenario: BattleScenario,
    *,
    hp_multipliers: Sequence[float],
    attack_multipliers: Sequence[float],
    defense_multipliers: Sequence[float],
    runs: int = 2_000,
    seed: int = 1,
) -> list[dict[str, float | int]]:
    rows: list[dict[str, float | int]] = []
    for index, (hp_mult, attack_mult, defense_mult) in enumerate(
        product(hp_multipliers, attack_multipliers, defense_multipliers)
    ):
        candidate = scale_enemy_side(
            scenario,
            hp_multiplier=hp_mult,
            attack_multiplier=attack_mult,
            defense_multiplier=defense_mult,
        )
        summary = simulate(candidate, runs=runs, seed=seed + index)
        rows.append({
            "hp_multiplier": hp_mult,
            "attack_multiplier": attack_mult,
            "defense_multiplier": defense_mult,
            "win_rate": summary.win_rate,
            "wipe_rate": summary.wipe_rate,
            "any_ko_rate": summary.any_ko_rate,
            "median_rounds": summary.median_rounds,
            "p90_rounds": summary.p90_rounds,
            "mean_remaining_party_hp": summary.mean_remaining_party_hp,
        })
    return rows
