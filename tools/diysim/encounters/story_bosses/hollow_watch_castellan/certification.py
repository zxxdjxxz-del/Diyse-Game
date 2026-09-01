"""Certification helpers for running Hollow Watch against v93 party snapshots."""
from __future__ import annotations

import math
import random
import statistics
from pathlib import Path

from .policy import SmartPolicyConfig
from .repo_loader import load_hollow_watch_repo_data
from .runtime import HollowWatchOutcome, HollowWatchSummary, _run_hollow_watch_smart_with_data
from .snapshots import with_hollow_watch_party_snapshot


def _summarize(outcomes: list[HollowWatchOutcome]) -> HollowWatchSummary:
    runs = len(outcomes)
    rounds = sorted(outcome.rounds for outcome in outcomes)
    party_wins = sum(outcome.winner == "party" for outcome in outcomes)
    enemy_wins = sum(outcome.winner == "enemy" for outcome in outcomes)

    def percentile(fraction: float) -> float:
        index = max(0, math.ceil(fraction * runs) - 1)
        return float(rounds[index])

    return HollowWatchSummary(
        runs=runs,
        win_rate=party_wins / runs,
        wipe_rate=enemy_wins / runs,
        any_ko_rate=sum(outcome.any_party_ko for outcome in outcomes) / runs,
        mean_rounds=statistics.fmean(rounds),
        median_rounds=float(statistics.median(rounds)),
        p10_rounds=percentile(0.10),
        p90_rounds=percentile(0.90),
        mean_remaining_party_hp=statistics.fmean(outcome.party_hp_fraction for outcome in outcomes),
        mean_remaining_party_mp=statistics.fmean(outcome.party_mp_fraction for outcome in outcomes),
        mean_ballista_shots=statistics.fmean(outcome.ballista_shots for outcome in outcomes),
        staggered_exposure_rate=sum(outcome.staggered_exposed for outcome in outcomes) / runs,
    )


def simulate_hollow_watch_v93_snapshot(
    level: int,
    *,
    policy: SmartPolicyConfig = SmartPolicyConfig(),
    runs: int = 2_000,
    seed: int = 93,
    root: Path | None = None,
) -> HollowWatchSummary:
    """Run the current encounter/rules against an exact v93 Lv2 or Lv3 party body.

    This intentionally keeps current class Ability costs and current combat rules.
    Only the printed party body changes between level snapshots.
    """
    if runs < 1:
        raise ValueError("runs must be positive")
    data = with_hollow_watch_party_snapshot(
        load_hollow_watch_repo_data(root=root),
        level,
        root=root,
    )
    master = random.Random(seed)
    outcomes = [
        _run_hollow_watch_smart_with_data(
            random.Random(master.getrandbits(64)),
            data,
            policy=policy,
            max_rounds=30,
        )
        for _ in range(runs)
    ]
    return _summarize(outcomes)


__all__ = ["simulate_hollow_watch_v93_snapshot"]
