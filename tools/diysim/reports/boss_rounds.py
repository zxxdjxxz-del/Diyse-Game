"""Cross-boss round-count report under the standard DiySim pressure profile."""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json

from tools.diysim.encounters.story_bosses.first_command_warden.standard_profile import (
    simulate_first_command_warden_standard_profile,
)
from tools.diysim.encounters.story_bosses.hollow_watch_castellan.standard_profile import (
    simulate_hollow_watch_standard_profile,
)
from tools.diysim.encounters.story_bosses.matron_zevraya.split_stats import (
    simulate_matron_zevraya_split,
)
from tools.diysim.overlays import standard_boss_test_overlay


@dataclass(frozen=True)
class BossRoundRow:
    boss: str
    party_band: str
    player_level: int
    strategy: str
    runs: int
    win_rate: float
    wipe_rate: float
    any_ko_rate: float
    mean_rounds: float
    median_rounds: float
    p10_rounds: float
    p90_rounds: float


def _row(boss: str, band: str, level: int, strategy: str, summary) -> BossRoundRow:
    return BossRoundRow(
        boss=boss,
        party_band=band,
        player_level=level,
        strategy=strategy,
        runs=summary.runs,
        win_rate=summary.win_rate,
        wipe_rate=summary.wipe_rate,
        any_ko_rate=summary.any_ko_rate,
        mean_rounds=summary.mean_rounds,
        median_rounds=summary.median_rounds,
        p10_rounds=summary.p10_rounds,
        p90_rounds=summary.p90_rounds,
    )


def run_standard_boss_round_report(*, runs: int = 500, seed: int = 120) -> tuple[BossRoundRow, ...]:
    """Run every currently executable story-boss runtime under one profile.

    Profile: enemy direct-damage Power x1.20 + main boss ATK/MAG +5 effective
    levels. Authored HP, DEF, Spirit and Speed remain unchanged.
    """
    if runs < 1:
        raise ValueError("runs must be positive")

    rows: list[BossRoundRow] = []

    for level, band in ((2, "mandatory"), (3, "high_side")):
        summary = simulate_hollow_watch_standard_profile(
            level,
            runs=runs,
            seed=seed,
        )
        rows.append(_row("Hollow Watch Castellan", band, level, "smart_support_priority", summary))

    for level, band in ((11, "mandatory"), (13, "high_side")):
        summary = simulate_first_command_warden_standard_profile(
            player_level=level,
            runs=runs,
            seed=seed + 10,
        )
        rows.append(_row("First Command Warden", band, level, "current_competent_policy", summary))

    overlay = standard_boss_test_overlay()
    for level, band in ((24, "mandatory"), (28, "high_side")):
        summary = simulate_matron_zevraya_split(
            player_level=level,
            structure_mode="non_diluting",
            strategy="dismantle",
            reservoir_plan=("Brood", "Armor"),
            overlay=overlay,
            use_prepared_inventory=True,
            runs=runs,
            seed=seed + 20,
        )
        rows.append(_row("Matron Zevraya", band, level, "Brood->Armor", summary))

    return tuple(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs", type=int, default=500)
    parser.add_argument("--seed", type=int, default=120)
    args = parser.parse_args()
    rows = run_standard_boss_round_report(runs=args.runs, seed=args.seed)
    print(json.dumps([asdict(row) for row in rows], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()


__all__ = ["BossRoundRow", "run_standard_boss_round_report"]
