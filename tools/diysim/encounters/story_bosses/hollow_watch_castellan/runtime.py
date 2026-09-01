"""Encounter-specific Hollow Watch runtime backed only by repo source data."""
from __future__ import annotations
from dataclasses import dataclass, replace
import math
from pathlib import Path
import random
import statistics
from typing import Literal

from tools.diysim.combat.action_resolution import resolve_damage, resolve_heal
from tools.diysim.combat.basic_attack import basic_attack_action
from tools.diysim.combat.models import CombatAction, CombatUnit, TemporaryModifierSpec
from tools.diysim.combat.status_runtime import complete_turn, end_round, turn_is_blocked
from tools.diysim.combat.temporary_modifiers import apply_temporary_modifier
from tools.diysim.combat.turn_order import turn_order

from .policy import (
    RoundStartView,
    SmartPolicyConfig,
    choose_cyanis_action,
    choose_ilyra_action,
    choose_maevra_action,
    next_harmonized_prime,
)
from .repo_loader import HollowWatchRepoData, load_hollow_watch_repo_data

CastellanState = Literal["fortress", "walking"]
BallistaPhase = Literal["prepare", "fire", "reload"]


@dataclass(frozen=True)
class HollowWatchOutcome:
    winner: Literal["party", "enemy", "draw"]
    rounds: int
    any_party_ko: bool
    party_hp_fraction: float
    party_mp_fraction: float
    ballista_shots: int
    staggered_exposed: bool
    castellan_state_reached: CastellanState


@dataclass(frozen=True)
class HollowWatchSummary:
    runs: int
    win_rate: float
    wipe_rate: float
    any_ko_rate: float
    mean_rounds: float
    median_rounds: float
    p10_rounds: float
    p90_rounds: float
    mean_remaining_party_hp: float
    mean_remaining_party_mp: float
    mean_ballista_shots: float
    staggered_exposure_rate: float


def _weighted_boss_action(
    data: HollowWatchRepoData,
    state: CastellanState,
    last_action: str | None,
    rng: random.Random,
) -> CombatAction:
    actions = data.fortress_actions if state == "fortress" else data.walking_actions
    legal = tuple(
        action
        for action in actions
        if not (action.name == last_action and action.name in data.repetition_locked_actions)
    )
    weights = tuple(action.weight for action in legal)
    if any(weight is None for weight in weights):
        raise ValueError("Hollow Watch action weights must come from explicit repo authority")
    return rng.choices(legal, weights=weights, k=1)[0]


def _random_conscious(party: list[CombatUnit], rng: random.Random) -> CombatUnit:
    legal = [unit for unit in party if unit.alive]
    if not legal:
        raise ValueError("no conscious party target")
    return rng.choice(legal)


def _resolve_boss_action(
    boss: CombatUnit,
    action: CombatAction,
    party: list[CombatUnit],
    rng: random.Random,
) -> bool:
    targets = [unit for unit in party if unit.alive]
    if action.target_scope == "one":
        targets = [_random_conscious(party, rng)]
    staggered_exposed = False
    for target in targets:
        had_staggered = target.has_status("staggered")
        resolve_damage(boss, action, target, rng)
        if not had_staggered and target.has_status("staggered"):
            staggered_exposed = True
    return staggered_exposed


def _set_seal_reduction(boss: CombatUnit, data: HollowWatchRepoData, active: bool) -> None:
    reduction = data.watch_seal_reduction if active else 0.0
    if boss.template.direct_damage_reduction != reduction:
        boss.template = replace(boss.template, direct_damage_reduction=reduction)


def _maybe_transition(
    boss: CombatUnit,
    seal: CombatUnit,
    state: CastellanState,
    data: HollowWatchRepoData,
) -> CastellanState:
    if state == "fortress" and boss.alive and boss.hp <= data.walking_trigger_hp:
        _set_seal_reduction(boss, data, False)
        return "walking"
    _set_seal_reduction(boss, data, state == "fortress" and seal.alive)
    return state


def _party_fraction(party: list[CombatUnit], attr: str, max_attr: str) -> float:
    total = sum(max(0, getattr(unit, attr)) for unit in party)
    maximum = sum(getattr(unit, max_attr) for unit in party)
    return total / maximum if maximum else 0.0


def _any_ko(party: list[CombatUnit], previous: bool) -> bool:
    return previous or any(not unit.alive for unit in party)


def _mend_with_trait(
    action: CombatAction,
    target: CombatUnit,
    data: HollowWatchRepoData,
    *,
    trait_available: bool,
) -> CombatAction:
    if trait_available and target.hp / target.max_hp < data.gentle_continuance_threshold:
        return replace(action, heal_max_hp_percent=action.heal_max_hp_percent + data.gentle_continuance_bonus)
    return action


def run_hollow_watch_smart(
    rng: random.Random,
    *,
    policy: SmartPolicyConfig = SmartPolicyConfig(),
    max_rounds: int = 30,
    root: Path | None = None,
) -> HollowWatchOutcome:
    """Run the current repo-authored Hollow Watch normal/smart policy.

    Required values are parsed from repo owner files at call time. Missing
    authority raises SourceGapError before the simulation begins.
    """
    data = load_hollow_watch_repo_data(root=root)
    cyanis = CombatUnit(data.cyanis, 0)
    ilyra = CombatUnit(data.ilyra, 1)
    maevra = CombatUnit(data.maevra, 2)
    boss = CombatUnit(data.castellan, 3)
    ballista = CombatUnit(data.ballista, 4)
    seal = CombatUnit(data.watch_seal, 5)
    party = [cyanis, ilyra, maevra]

    state: CastellanState = "fortress"
    ballista_phase: BallistaPhase = "prepare"
    prepared_target: CombatUnit | None = None
    last_boss_action: str | None = None
    harmonized_prime: str | None = None
    any_ko = False
    ballista_shots = 0
    staggered_exposed = False
    basic_attack = basic_attack_action(root=root)

    _set_seal_reduction(boss, data, True)

    for round_number in range(1, max_rounds + 1):
        round_start = RoundStartView.capture(party)
        gentle_continuance_available = True
        actors = [boss]
        if ballista.alive:
            actors.append(ballista)
        actors.extend(party)

        for actor in turn_order(actors):
            if not actor.alive or not boss.alive:
                continue
            if not any(unit.alive for unit in party):
                break

            if turn_is_blocked(actor, rng):
                complete_turn(actor, acted=False)
                any_ko = _any_ko(party, any_ko)
                continue

            if actor is boss:
                boss_action = _weighted_boss_action(data, state, last_boss_action, rng)
                last_boss_action = boss_action.name
                if _resolve_boss_action(boss, boss_action, party, rng):
                    staggered_exposed = True
                complete_turn(boss, acted=True)
                any_ko = _any_ko(party, any_ko)
                continue

            if actor is ballista:
                if ballista_phase == "prepare":
                    prepared_target = _random_conscious(party, rng)
                    ballista_phase = "fire"
                elif ballista_phase == "fire":
                    if prepared_target is not None and prepared_target.alive:
                        resolve_damage(ballista, data.heavy_bolt, prepared_target, rng)
                        ballista_shots += 1
                    prepared_target = None
                    ballista_phase = "reload"
                else:
                    ballista_phase = "prepare"
                complete_turn(ballista, acted=True)
                any_ko = _any_ko(party, any_ko)
                continue

            target = ballista if ballista.alive else boss

            if actor is maevra:
                action = choose_maevra_action(maevra, data)
                maevra.mp -= action.mp_cost
                resolve_damage(maevra, action, target, rng)
                complete_turn(maevra, acted=True)

            elif actor is cyanis:
                action = choose_cyanis_action(
                    cyanis,
                    data,
                    ballista_alive=ballista.alive,
                    harmonized_prime=harmonized_prime,
                )
                cyanis.mp -= action.mp_cost
                resolve_damage(cyanis, action, target, rng)
                established = next_harmonized_prime(action)
                if established is not None:
                    harmonized_prime = established
                complete_turn(cyanis, acted=True)

            else:
                action, heal_target = choose_ilyra_action(
                    ilyra,
                    party,
                    data,
                    round_start,
                    ballista_alive=ballista.alive,
                    config=policy,
                )
                ilyra.mp -= action.mp_cost
                if action.action_kind == "heal" and heal_target is not None:
                    resolve_heal(
                        ilyra,
                        _mend_with_trait(
                            action,
                            heal_target,
                            data,
                            trait_available=gentle_continuance_available and action.name == data.mend.name,
                        ),
                        heal_target,
                    )
                    if action.name == data.mend.name:
                        gentle_continuance_available = False
                    if action.name == data.clear_warding.name:
                        apply_temporary_modifier(
                            heal_target,
                            TemporaryModifierSpec(
                                effect_id="Clear Warding",
                                duration_rounds=data.clear_warding_sr_rounds,
                                status_resistance_flat=data.clear_warding_sr_bonus,
                            ),
                        )
                else:
                    resolve_damage(ilyra, basic_attack, target, rng)
                complete_turn(ilyra, acted=True)

            any_ko = _any_ko(party, any_ko)
            state = _maybe_transition(boss, seal, state, data)
            if not ballista.alive:
                prepared_target = None

        end_round([*party, boss, ballista])
        any_ko = _any_ko(party, any_ko)

        if not boss.alive:
            return HollowWatchOutcome(
                "party", round_number, any_ko,
                _party_fraction(party, "hp", "max_hp"),
                _party_fraction(party, "mp", "max_mp"),
                ballista_shots, staggered_exposed, state,
            )
        if not any(unit.alive for unit in party):
            return HollowWatchOutcome(
                "enemy", round_number, True, 0.0,
                _party_fraction(party, "mp", "max_mp"),
                ballista_shots, staggered_exposed, state,
            )

    return HollowWatchOutcome(
        "draw", max_rounds, any_ko,
        _party_fraction(party, "hp", "max_hp"),
        _party_fraction(party, "mp", "max_mp"),
        ballista_shots, staggered_exposed, state,
    )


def simulate_hollow_watch_smart(
    *,
    policy: SmartPolicyConfig = SmartPolicyConfig(),
    runs: int = 20_000,
    seed: int = 93,
    root: Path | None = None,
) -> HollowWatchSummary:
    if runs < 1:
        raise ValueError("runs must be positive")
    data = load_hollow_watch_repo_data(root=root)
    master = random.Random(seed)
    outcomes = [
        run_hollow_watch_smart(
            random.Random(master.getrandbits(64)), policy=policy, root=root
        )
        for _ in range(runs)
    ]
    rounds = sorted(outcome.rounds for outcome in outcomes)
    party_wins = sum(outcome.winner == "party" for outcome in outcomes)
    enemy_wins = sum(outcome.winner == "enemy" for outcome in outcomes)

    def percentile(fraction: float) -> float:
        index = max(0, math.ceil(fraction * len(rounds)) - 1)
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


__all__ = [
    "HollowWatchOutcome",
    "HollowWatchSummary",
    "run_hollow_watch_smart",
    "simulate_hollow_watch_smart",
]
