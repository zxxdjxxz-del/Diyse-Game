"""Standard cross-boss DiySim pressure wrapper for Hollow Watch Castellan."""
from __future__ import annotations

from dataclasses import replace
from pathlib import Path
import random

from tools.diysim.overlays import (
    STANDARD_BOSS_OFFENSIVE_LEVEL_OFFSET,
    STANDARD_BOSS_POWER_MULTIPLIER,
    scale_direct_damage_power,
    scale_selected_core_stat_level,
)

from .certification import _summarize
from .policy import SmartPolicyConfig
from .repo_loader import load_hollow_watch_repo_data
from .runtime import HollowWatchSummary, _run_hollow_watch_smart_with_data
from .snapshots import with_hollow_watch_party_snapshot

CASTELLAN_DISPLAYED_LEVEL = 6


def simulate_hollow_watch_standard_profile(
    level: int,
    *,
    policy: SmartPolicyConfig = SmartPolicyConfig(),
    runs: int = 2_000,
    seed: int = 93,
    root: Path | None = None,
) -> HollowWatchSummary:
    """Run Hollow Watch with +5 Castellan ATK/MAG and x1.20 hostile Power.

    The Castellan's DEF, Spirit, Speed, HP and MP stay authored. The global
    direct-damage Power multiplier also applies to Heavy Bolt, because it is a
    hostile direct-damage action inside the boss encounter.
    """
    if runs < 1:
        raise ValueError("runs must be positive")

    data = with_hollow_watch_party_snapshot(
        load_hollow_watch_repo_data(root=root),
        level,
        root=root,
    )
    castellan_stats = scale_selected_core_stat_level(
        data.castellan.stats,
        displayed_level=CASTELLAN_DISPLAYED_LEVEL,
        level_offset=STANDARD_BOSS_OFFENSIVE_LEVEL_OFFSET,
        stat_keys=("attack", "magic"),
        root=root,
    )
    data = replace(
        data,
        castellan=replace(data.castellan, stats=castellan_stats),
        fortress_actions=tuple(
            scale_direct_damage_power(action, STANDARD_BOSS_POWER_MULTIPLIER)
            for action in data.fortress_actions
        ),
        walking_actions=tuple(
            scale_direct_damage_power(action, STANDARD_BOSS_POWER_MULTIPLIER)
            for action in data.walking_actions
        ),
        heavy_bolt=scale_direct_damage_power(
            data.heavy_bolt,
            STANDARD_BOSS_POWER_MULTIPLIER,
        ),
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


__all__ = ["simulate_hollow_watch_standard_profile"]
