"""Executable First Command Warden sensitivity runtime.

The encounter body/mechanics, party snapshots, abilities, and working balance
scalars are all loaded from repository authority. This module owns only the
runtime state machine and the conservative v105 isolation policy.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
import math
from pathlib import Path
import random
import statistics
from typing import Literal

from tools.diysim.combat.action_resolution import resolve_damage, resolve_heal
from tools.diysim.combat.analogue import FunctionalAnalogueRule, FunctionalAnalogueState
from tools.diysim.combat.models import CombatAction, CombatUnit
from tools.diysim.combat.status_runtime import complete_turn, end_round, turn_is_blocked
from tools.diysim.combat.turn_order import turn_order
from tools.diysim.overlays import BalanceOverlay, scale_direct_damage_power, scale_effective_core_stat_level

from .policy import WardenPolicyConfig, choose_player_action, load_warden_party_actions
from .repo_loader import FirstCommandWardenRepoData, load_first_command_warden_repo_data
from .snapshots import load_first_command_warden_party_snapshot

WardenState = Literal["imposed_authority", "challenged_authority"]


@dataclass
class _SealState:
    marked_category: str
    expires_end_round: int


@dataclass(frozen=True)
class WardenBattleOutcome:
    winner: Literal["party", "enemy", "draw"]
    rounds: int
    any_party_ko: bool
    party_hp_fraction: float
    party_mp_fraction: float
    state_b_reached: bool
    ruling_attempts: int
    ruling_resolutions: int
    ruling_disruptions: int
    seal_reprisals: int
    analogue_uses: int
    stun_exposed: bool
    staggered_exposed: bool


@dataclass(frozen=True)
class WardenSimulationSummary:
    runs: int
    player_level: int
    power_multiplier: float
    effective_stat_level_offset: int
    win_rate: float
    wipe_rate: float
    any_ko_rate: float
    mean_rounds: float
    median_rounds: float
    p10_rounds: float
    p90_rounds: float
    mean_remaining_party_hp: float
    mean_remaining_party_mp: float
    state_b_reach_rate: float
    mean_ruling_attempts: float
    mean_ruling_resolutions: float
    mean_ruling_disruptions: float
    mean_seal_reprisals: float
    mean_analogue_uses: float
    stun_exposure_rate: float
    staggered_exposure_rate: float


def _party_fraction(party: list[CombatUnit], attr: str, max_attr: str) -> float:
    maximum = sum(getattr(unit, max_attr) for unit in party)
    if maximum <= 0:
        return 0.0
    return sum(max(0, getattr(unit, attr)) for unit in party) / maximum


def _random_conscious(party: list[CombatUnit], rng: random.Random) -> CombatUnit:
    legal = [unit for unit in party if unit.alive]
    if not legal:
        raise ValueError("no conscious party target")
    return rng.choice(legal)


def _overlay_action(action: CombatAction, overlay: BalanceOverlay) -> CombatAction:
    return scale_direct_damage_power(action, overlay.direct_damage_power_multiplier)


def _overlay_data(
    data: FirstCommandWardenRepoData,
    overlay: BalanceOverlay,
    *,
    root: Path | None = None,
) -> FirstCommandWardenRepoData:
    warden_stats = data.warden.stats
    if overlay.effective_stat_level_offset:
        warden_stats = scale_effective_core_stat_level(
            warden_stats,
            displayed_level=data.displayed_level,
            level_offset=overlay.effective_stat_level_offset,
            root=root,
        )
    warden = replace(data.warden, stats=warden_stats)
    seal = replace(
        data.command_seal,
        reprisal=_overlay_action(data.command_seal.reprisal, overlay),
    )
    ruling = replace(
        data.major_ruling,
        action=_overlay_action(data.major_ruling.action, overlay),
    )
    return replace(
        data,
        warden=warden,
        state_a_actions=tuple(_overlay_action(action, overlay) for action in data.state_a_actions),
        state_b_actions=tuple(_overlay_action(action, overlay) for action in data.state_b_actions),
        command_seal=seal,
        major_ruling=ruling,
    )


def _action_locked(name: str, round_number: int, locked_through: dict[str, int]) -> bool:
    return round_number <= locked_through.get(name, 0)


def _set_action_lock(
    name: str,
    round_number: int,
    locks: dict[str, int],
    locked_through: dict[str, int],
) -> None:
    duration = locks.get(name)
    if duration:
        locked_through[name] = round_number + duration


def _resolve_enemy_damage(
    boss: CombatUnit,
    action: CombatAction,
    party: list[CombatUnit],
    rng: random.Random,
) -> tuple[bool, bool]:
    targets = [unit for unit in party if unit.alive]
    if action.target_scope == "one":
        targets = [_random_conscious(party, rng)]
    stun_exposed = False
    staggered_exposed = False
    for target in targets:
        had_stun = target.has_status("stun")
        had_staggered = target.has_status("staggered")
        resolve_damage(boss, action, target, rng)
        stun_exposed = stun_exposed or (not had_stun and target.has_status("stun"))
        staggered_exposed = staggered_exposed or (not had_staggered and target.has_status("staggered"))
    return stun_exposed, staggered_exposed


def _legal_seal_targets(
    party: list[CombatUnit],
    last_categories: dict[int, str],
    seals: dict[int, _SealState],
) -> list[CombatUnit]:
    return [
        unit for unit in party
        if unit.alive and unit.stable_index in last_categories and unit.stable_index not in seals
    ]


def _enter_state_b(
    boss: CombatUnit,
    data: FirstCommandWardenRepoData,
    *,
    round_number: int,
    ruling_disruptions: int,
) -> tuple[int, float]:
    protection = data.state_b_protection
    if ruling_disruptions:
        rounds = protection.disrupted_rounds
        reduction = protection.disrupted_reduction
    else:
        rounds = protection.undisrupted_rounds
        reduction = protection.undisrupted_reduction
    boss.template = replace(boss.template, direct_damage_reduction=reduction)
    # Numbered-round timing: application round counts as round 1. If State B is
    # entered during end-round damage, caller applies this after expiry handling,
    # naturally beginning the count with the next round.
    return round_number + rounds - 1, reduction


def _run_warden_with_data(
    rng: random.Random,
    data: FirstCommandWardenRepoData,
    *,
    player_level: int,
    overlay: BalanceOverlay,
    policy: WardenPolicyConfig,
    max_rounds: int,
    root: Path | None = None,
) -> WardenBattleOutcome:
    data = _overlay_data(data, overlay, root=root)
    snapshot = load_first_command_warden_party_snapshot(player_level, root=root)
    actions = load_warden_party_actions(root=root)

    party = [CombatUnit(template, index) for index, template in enumerate(snapshot.party)]
    boss = CombatUnit(data.warden, 4)
    ring = CombatUnit(data.command_ring, 5)

    analogue = FunctionalAnalogueState(
        "Recorded Analogue",
        FunctionalAnalogueRule.from_source(data.recorded_analogue),
    )
    state: WardenState = "imposed_authority"
    state_b_reached = False
    protection_end_round: int | None = None

    last_categories: dict[int, str] = {}
    seals: dict[int, _SealState] = {}
    locked_through: dict[str, int] = {}

    ring_active = False
    ring_available_after_round = 0
    ruling_pending = False
    ruling_disrupted_pending = False
    ruling_attempts = 0
    ruling_resolutions = 0
    ruling_disruptions = 0
    seal_reprisals = 0
    analogue_uses = 0
    any_ko = False
    stun_exposed = False
    staggered_exposed = False

    def mark_kos() -> None:
        nonlocal any_ko
        any_ko = any_ko or any(not unit.alive for unit in party)

    def maybe_disrupt_ring(round_number: int) -> None:
        nonlocal ring_active, ruling_disrupted_pending, ruling_disruptions, ring_available_after_round
        if ring_active and not ring.alive:
            ring_active = False
            ruling_disrupted_pending = True
            ruling_disruptions += 1
            ring_available_after_round = round_number + data.major_ruling.ring_realign_rounds

    def maybe_enter_state_b(round_number: int) -> None:
        nonlocal state, state_b_reached, protection_end_round, ring_active, ruling_pending, ruling_disrupted_pending
        if (
            state == "imposed_authority"
            and boss.alive
            and boss.hp <= boss.max_hp * data.state_b_trigger_fraction
        ):
            state = "challenged_authority"
            state_b_reached = True
            seals.clear()
            ring_active = False
            ruling_pending = False
            ruling_disrupted_pending = False
            protection_end_round, _ = _enter_state_b(
                boss,
                data,
                round_number=round_number,
                ruling_disruptions=ruling_disruptions,
            )

    for round_number in range(1, max_rounds + 1):
        actors = [boss, *party]
        for actor in turn_order(actors):
            if not actor.alive or not boss.alive:
                continue
            if not any(unit.alive for unit in party):
                break

            if turn_is_blocked(actor, rng):
                complete_turn(actor, acted=False)
                mark_kos()
                continue

            if actor is boss:
                # A prepared Major Ruling consumes this turn whether it resolves
                # or was disrupted during the full party preparation cycle.
                if ruling_pending and state == "imposed_authority":
                    if ring_active and ring.alive and not ruling_disrupted_pending:
                        new_stun, new_staggered = _resolve_enemy_damage(
                            boss, data.major_ruling.action, party, rng
                        )
                        stun_exposed = stun_exposed or new_stun
                        staggered_exposed = staggered_exposed or new_staggered
                        ruling_resolutions += 1
                        _set_action_lock("Major Ruling", round_number, data.repetition_locks, locked_through)
                        ring_active = False
                        ring_available_after_round = (
                            round_number + data.major_ruling.ring_realign_rounds
                        )
                    ruling_pending = False
                    ruling_disrupted_pending = False
                    complete_turn(boss, acted=True)
                    mark_kos()
                    continue

                candidates: list[tuple[str, CombatAction | None]] = []
                direct_actions = data.state_a_actions if state == "imposed_authority" else data.state_b_actions
                for action in direct_actions:
                    if not _action_locked(action.name, round_number, locked_through):
                        candidates.append((action.name, action))

                if analogue.available:
                    candidates.append(("Recorded Analogue", None))

                seal_targets = _legal_seal_targets(party, last_categories, seals)
                if (
                    state == "imposed_authority"
                    and seal_targets
                    and not _action_locked("Command Seal", round_number, locked_through)
                ):
                    candidates.append(("Command Seal", None))

                if (
                    state == "imposed_authority"
                    and round_number > ring_available_after_round
                    and not _action_locked("Major Ruling", round_number, locked_through)
                ):
                    candidates.append(("Major Ruling", None))

                if not candidates:
                    raise RuntimeError("First Command Warden has no legal selected action")
                choice_name, choice_action = rng.choice(candidates)

                if choice_name == "Command Seal":
                    target = rng.choice(seal_targets)
                    marked = last_categories[target.stable_index]
                    seals[target.stable_index] = _SealState(
                        marked_category=marked,
                        expires_end_round=round_number + data.command_seal.duration_rounds - 1,
                    )
                    _set_action_lock(choice_name, round_number, data.repetition_locks, locked_through)

                elif choice_name == "Major Ruling":
                    ring = CombatUnit(data.command_ring, 5)
                    ring_active = True
                    ruling_pending = True
                    ruling_disrupted_pending = False
                    ruling_attempts += 1

                elif choice_name == "Recorded Analogue":
                    analogue_action = analogue.consume()
                    if analogue_action is None:
                        raise RuntimeError("Recorded Analogue selected without a record")
                    analogue_action = _overlay_action(analogue_action, overlay)
                    new_stun, new_staggered = _resolve_enemy_damage(
                        boss, analogue_action, party, rng
                    )
                    stun_exposed = stun_exposed or new_stun
                    staggered_exposed = staggered_exposed or new_staggered
                    analogue_uses += 1

                else:
                    assert choice_action is not None
                    new_stun, new_staggered = _resolve_enemy_damage(
                        boss, choice_action, party, rng
                    )
                    stun_exposed = stun_exposed or new_stun
                    staggered_exposed = staggered_exposed or new_staggered
                    _set_action_lock(choice_name, round_number, data.repetition_locks, locked_through)

                complete_turn(boss, acted=True)
                mark_kos()
                continue

            seal = seals.get(actor.stable_index)
            category, action, heal_target = choose_player_action(
                actor,
                party,
                actions,
                sealed_category=seal.marked_category if seal else None,
                config=policy,
            )

            if action.mp_cost:
                actor.mp -= action.mp_cost

            if action.action_kind == "heal":
                if heal_target is None:
                    raise RuntimeError("heal action selected without target")
                resolve_heal(actor, action, heal_target)
            else:
                enemy_targets = [boss]
                if ring_active and ring.alive:
                    if action.target_scope == "all":
                        enemy_targets = [boss, ring]
                    else:
                        enemy_targets = [ring]
                for target in enemy_targets:
                    if target.alive:
                        resolve_damage(actor, action, target, rng)
                maybe_disrupt_ring(round_number)
                maybe_enter_state_b(round_number)
                analogue.observe_completed_action(
                    action,
                    category="ability" if category == "Ability" else "attack",
                )

            last_categories[actor.stable_index] = category
            complete_turn(actor, acted=True)

            active_seal = seals.get(actor.stable_index)
            if active_seal is not None and category == active_seal.marked_category:
                if actor.alive:
                    resolve_damage(boss, data.command_seal.reprisal, actor, rng)
                seal_reprisals += 1
                seals.pop(actor.stable_index, None)

            mark_kos()

        # Existing State-B protection clocks expire before end-of-round-created
        # transitions are checked, matching the global timing rule.
        end_round_units = [*party, boss]
        if ring_active:
            end_round_units.append(ring)
        end_round(end_round_units)
        mark_kos()
        maybe_disrupt_ring(round_number)

        if state == "challenged_authority" and protection_end_round is not None:
            if round_number >= protection_end_round:
                boss.template = replace(boss.template, direct_damage_reduction=0.0)
                protection_end_round = None

        maybe_enter_state_b(round_number)

        for index, seal in list(seals.items()):
            if round_number >= seal.expires_end_round:
                seals.pop(index, None)

        if not boss.alive:
            return WardenBattleOutcome(
                "party", round_number, any_ko,
                _party_fraction(party, "hp", "max_hp"),
                _party_fraction(party, "mp", "max_mp"),
                state_b_reached, ruling_attempts, ruling_resolutions,
                ruling_disruptions, seal_reprisals, analogue_uses,
                stun_exposed, staggered_exposed,
            )
        if not any(unit.alive for unit in party):
            return WardenBattleOutcome(
                "enemy", round_number, True, 0.0,
                _party_fraction(party, "mp", "max_mp"),
                state_b_reached, ruling_attempts, ruling_resolutions,
                ruling_disruptions, seal_reprisals, analogue_uses,
                stun_exposed, staggered_exposed,
            )

    return WardenBattleOutcome(
        "draw", max_rounds, any_ko,
        _party_fraction(party, "hp", "max_hp"),
        _party_fraction(party, "mp", "max_mp"),
        state_b_reached, ruling_attempts, ruling_resolutions,
        ruling_disruptions, seal_reprisals, analogue_uses,
        stun_exposed, staggered_exposed,
    )


def run_first_command_warden(
    rng: random.Random,
    *,
    player_level: int = 11,
    overlay: BalanceOverlay = BalanceOverlay(),
    policy: WardenPolicyConfig = WardenPolicyConfig(),
    max_rounds: int = 30,
    root: Path | None = None,
) -> WardenBattleOutcome:
    data = load_first_command_warden_repo_data(root=root)
    return _run_warden_with_data(
        rng,
        data,
        player_level=player_level,
        overlay=overlay,
        policy=policy,
        max_rounds=max_rounds,
        root=root,
    )


def simulate_first_command_warden(
    *,
    player_level: int = 11,
    overlay: BalanceOverlay = BalanceOverlay(),
    policy: WardenPolicyConfig = WardenPolicyConfig(),
    runs: int = 10_000,
    seed: int = 105,
    root: Path | None = None,
) -> WardenSimulationSummary:
    if runs < 1:
        raise ValueError("runs must be positive")
    data = load_first_command_warden_repo_data(root=root)
    master = random.Random(seed)
    outcomes = [
        _run_warden_with_data(
            random.Random(master.getrandbits(64)),
            data,
            player_level=player_level,
            overlay=overlay,
            policy=policy,
            max_rounds=30,
            root=root,
        )
        for _ in range(runs)
    ]
    rounds = sorted(outcome.rounds for outcome in outcomes)

    def percentile(fraction: float) -> float:
        index = max(0, math.ceil(fraction * len(rounds)) - 1)
        return float(rounds[index])

    return WardenSimulationSummary(
        runs=runs,
        player_level=player_level,
        power_multiplier=overlay.direct_damage_power_multiplier,
        effective_stat_level_offset=overlay.effective_stat_level_offset,
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
        stun_exposure_rate=sum(outcome.stun_exposed for outcome in outcomes) / runs,
        staggered_exposure_rate=sum(outcome.staggered_exposed for outcome in outcomes) / runs,
    )


__all__ = [
    "WardenBattleOutcome",
    "WardenSimulationSummary",
    "run_first_command_warden",
    "simulate_first_command_warden",
]
