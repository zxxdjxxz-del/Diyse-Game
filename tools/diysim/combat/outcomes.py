"""Advanced battle outcomes and Monte Carlo summary models."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Literal, Sequence

from .models import CombatUnit


@dataclass(frozen=True)
class AdvancedSimulationSummary:
    runs: int
    party_wins: int
    enemy_wins: int
    draws: int
    win_rate: float
    wipe_rate: float
    any_ko_rate: float
    mean_rounds: float
    median_rounds: float
    p90_rounds: float
    mean_remaining_party_hp: float
    mean_remaining_party_mp: float

    def as_dict(self) -> dict[str, int | float]:
        return self.__dict__.copy()


@dataclass(frozen=True)
class AdvancedBattleOutcome:
    winner: Literal["party", "enemy", "draw"]
    rounds: int
    any_party_ko: bool
    party_hp_fraction: float
    party_mp_fraction: float


def update_party_ko_flag(party: Sequence[CombatUnit], current: bool) -> bool:
    for unit in party:
        if not unit.alive and not unit.ko_counted:
            unit.ko_counted = True
            current = True
    return current


def make_outcome(
    winner: Literal["party", "enemy", "draw"],
    rounds: int,
    party: Sequence[CombatUnit],
    any_ko: bool,
) -> AdvancedBattleOutcome:
    hp_total = sum(unit.max_hp for unit in party)
    mp_total = sum(unit.max_mp for unit in party)
    return AdvancedBattleOutcome(
        winner,
        rounds,
        any_ko,
        sum(unit.hp for unit in party) / hp_total if hp_total else 0.0,
        sum(unit.mp for unit in party) / mp_total if mp_total else 1.0,
    )
