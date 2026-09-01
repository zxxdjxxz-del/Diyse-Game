"""Advanced battle-loop orchestration.

Subsystem logic lives in dedicated combat modules. This file owns only the
battle loop and repeated-run aggregation.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import random
import statistics
from typing import Sequence

from .action_resolution import resolve_damage, resolve_heal
from .action_selection import choose_action, selectable_actions
from .models import CombatUnit, Combatant
from .outcomes import AdvancedBattleOutcome, AdvancedSimulationSummary, make_outcome, update_party_ko_flag
from .status_runtime import complete_turn, end_round, turn_is_blocked
from .targeting import select_targets
from .turn_order import turn_order


@dataclass(frozen=True)
class AdvancedBattleScenario:
    party: tuple[Combatant, ...]
    enemies: tuple[Combatant, ...]
    max_rounds: int = 100

    def __post_init__(self) -> None:
        if not 1 <= len(self.party) <= 4:
            raise ValueError("party must contain 1-4 combatants")
        if not 1 <= len(self.enemies) <= 8:
            raise ValueError("enemies must contain 1-8 combatants")
        if self.max_rounds < 1:
            raise ValueError("max_rounds must be positive")
        if any(unit.side != "party" for unit in self.party):
            raise ValueError("all party combatants must have side='party'")
        if any(unit.side != "enemy" for unit in self.enemies):
            raise ValueError("all enemy combatants must have side='enemy'")


def run_advanced_battle(
    party_templates: Sequence[Combatant],
    enemy_templates: Sequence[Combatant],
    rng: random.Random,
    *,
    max_rounds: int = 100,
) -> AdvancedBattleOutcome:
    if not 1 <= len(party_templates) <= 4:
        raise ValueError("party must contain 1-4 combatants")
    if not 1 <= len(enemy_templates) <= 8:
        raise ValueError("enemies must contain 1-8 combatants")

    units = [
        CombatUnit(template, index)
        for index, template in enumerate(tuple(party_templates) + tuple(enemy_templates))
    ]
    party = [unit for unit in units if unit.side == "party"]
    enemies = [unit for unit in units if unit.side == "enemy"]
    any_ko = False

    for round_number in range(1, max_rounds + 1):
        for actor in turn_order(units):
            if not actor.alive:
                continue
            opposing = enemies if actor.side == "party" else party
            if not any(unit.alive for unit in opposing):
                break

            if turn_is_blocked(actor, rng):
                complete_turn(actor, acted=False)
                any_ko = update_party_ko_flag(party, any_ko)
                continue

            action = choose_action(actor, units, rng)
            actor.mp -= action.mp_cost
            for target in select_targets(actor, action, units, rng):
                if action.action_kind == "heal":
                    resolve_heal(actor, action, target)
                else:
                    resolve_damage(actor, action, target, rng)

            complete_turn(actor, acted=True)
            any_ko = update_party_ko_flag(party, any_ko)

        end_round(units)
        any_ko = update_party_ko_flag(party, any_ko)
        party_alive = any(unit.alive for unit in party)
        enemy_alive = any(unit.alive for unit in enemies)
        if not enemy_alive:
            return make_outcome("party", round_number, party, any_ko)
        if not party_alive:
            return make_outcome("enemy", round_number, party, True)

    return make_outcome("draw", max_rounds, party, any_ko)


def simulate_advanced(
    scenario: AdvancedBattleScenario,
    *,
    runs: int = 10_000,
    seed: int = 1,
) -> AdvancedSimulationSummary:
    if runs < 1:
        raise ValueError("runs must be positive")
    master = random.Random(seed)
    outcomes = [
        run_advanced_battle(
            scenario.party,
            scenario.enemies,
            random.Random(master.getrandbits(64)),
            max_rounds=scenario.max_rounds,
        )
        for _ in range(runs)
    ]
    party_wins = sum(outcome.winner == "party" for outcome in outcomes)
    enemy_wins = sum(outcome.winner == "enemy" for outcome in outcomes)
    rounds = sorted(outcome.rounds for outcome in outcomes)
    p90_index = max(0, math.ceil(0.90 * len(rounds)) - 1)
    return AdvancedSimulationSummary(
        runs=runs,
        party_wins=party_wins,
        enemy_wins=enemy_wins,
        draws=runs - party_wins - enemy_wins,
        win_rate=party_wins / runs,
        wipe_rate=enemy_wins / runs,
        any_ko_rate=sum(outcome.any_party_ko for outcome in outcomes) / runs,
        mean_rounds=statistics.fmean(rounds),
        median_rounds=float(statistics.median(rounds)),
        p90_rounds=float(rounds[p90_index]),
        mean_remaining_party_hp=statistics.fmean(outcome.party_hp_fraction for outcome in outcomes),
        mean_remaining_party_mp=statistics.fmean(outcome.party_mp_fraction for outcome in outcomes),
    )


__all__ = [
    "AdvancedBattleOutcome",
    "AdvancedBattleScenario",
    "AdvancedSimulationSummary",
    "complete_turn",
    "end_round",
    "resolve_damage",
    "resolve_heal",
    "run_advanced_battle",
    "selectable_actions",
    "simulate_advanced",
    "turn_is_blocked",
    "turn_order",
]
