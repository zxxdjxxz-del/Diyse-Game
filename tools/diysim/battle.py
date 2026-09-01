"""Phase 2 battle runtime layered on the current-canon rule primitives."""
from __future__ import annotations
from dataclasses import dataclass
import math
import random
import statistics
from typing import Literal, Sequence
from .core import CRIT_CHANCE_CAP, adjusted_hit_chance, direct_damage, round_half_up
from .rules import (
    BASIC_ATTACK, BLEED_ESCALATED_RATE, BLEED_INITIAL_RATE, BURN_RATE,
    FREEZE_MAX_AFFECTED_ROUNDS, STUN_LOSS_CHANCE, CombatAction, CombatUnit,
    Combatant, StatusRider, affinity_damage_multiplier, apply_status,
    effective_attack, effective_defense, effective_magic, effective_speed,
    effective_spirit, element_affinity, healing_amount,
    linked_status_affinity_modifier, status_application_chance,
)


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


def turn_order(units: Sequence[CombatUnit]) -> list[CombatUnit]:
    return sorted((u for u in units if u.alive), key=lambda u: (-effective_speed(u), 0 if u.side == "party" else 1, u.stable_index))


def _allies(actor: CombatUnit, units: Sequence[CombatUnit]) -> list[CombatUnit]:
    return [u for u in units if u.side == actor.side]


def _enemies(actor: CombatUnit, units: Sequence[CombatUnit]) -> list[CombatUnit]:
    return [u for u in units if u.side != actor.side]


def _has_target(actor: CombatUnit, action: CombatAction, units: Sequence[CombatUnit]) -> bool:
    if action.target_side == "enemy": return any(u.alive for u in _enemies(actor, units))
    candidates = [actor] if action.target_side == "self" else [u for u in _allies(actor, units) if u.alive]
    if action.action_kind != "heal": return any(u.alive for u in candidates)
    return any(u.alive and (u.hp < u.max_hp or (action.clear_harmful_statuses and u.statuses)) for u in candidates)


def selectable_actions(actor: CombatUnit, units: Sequence[CombatUnit]) -> tuple[CombatAction, ...]:
    legal = tuple(a for a in actor.template.actions if a.mp_cost <= actor.mp and a.weight > 0 and _has_target(actor, a, units))
    if legal: return legal
    return (BASIC_ATTACK,) if any(u.alive for u in _enemies(actor, units)) else ()


def _choose_action(actor: CombatUnit, units: Sequence[CombatUnit], rng: random.Random) -> CombatAction:
    actions = selectable_actions(actor, units)
    if not actions: raise ValueError(f"{actor.template.name} has no selectable action")
    return rng.choices(actions, weights=[a.weight for a in actions], k=1)[0]


def _targets(actor: CombatUnit, action: CombatAction, units: Sequence[CombatUnit], rng: random.Random) -> list[CombatUnit]:
    if action.target_side == "enemy": candidates = [u for u in _enemies(actor, units) if u.alive]
    elif action.target_side == "self": candidates = [actor] if actor.alive else []
    else: candidates = [u for u in _allies(actor, units) if u.alive]
    if action.action_kind == "heal":
        useful = [u for u in candidates if u.hp < u.max_hp or (action.clear_harmful_statuses and u.statuses)]
        if useful: candidates = useful
    if action.target_scope == "all": return candidates
    if not candidates: return []
    if action.action_kind == "heal" and action.target_side != "enemy":
        return [min(candidates, key=lambda u: (u.hp / u.max_hp, u.stable_index))]
    return [rng.choice(candidates)]


def _roll_status(action: CombatAction, rider: StatusRider, target: CombatUnit, rng: random.Random) -> bool:
    if rider.status in target.template.status_immunities: return False
    affinity = element_affinity(target, action.element)
    modifier = linked_status_affinity_modifier(action.element, rider.status, affinity)
    if modifier is None: return False
    chance = status_application_chance(rider.base_chance, affinity_modifier=modifier, specialist_bonus=rider.specialist_bonus, reliability_bonus=rider.reliability_bonus, status_resistance=target.template.status_resistance)
    return rng.random() * 100 < chance and apply_status(target, rider.status)


def clear_bleed_if_full(unit: CombatUnit) -> None:
    if unit.hp >= unit.max_hp: unit.statuses.pop("bleed", None)


def _clear_statuses(unit: CombatUnit, count: int | Literal["all"]) -> None:
    if count == "all": unit.statuses.clear(); return
    for status in list(unit.statuses)[:max(0, int(count))]: unit.statuses.pop(status, None)


def resolve_heal(actor: CombatUnit, action: CombatAction, target: CombatUnit) -> int:
    amount = healing_amount(target.max_hp, round_half_up(effective_magic(actor)), max_hp_percent=action.heal_max_hp_percent, magic_scaling=action.heal_magic_scaling, potency_multiplier=action.healing_potency)
    before = target.hp
    target.hp = min(target.max_hp, target.hp + amount)
    clear_bleed_if_full(target)
    if action.clear_harmful_statuses: _clear_statuses(target, action.clear_harmful_statuses)
    return target.hp - before


def resolve_damage(actor: CombatUnit, action: CombatAction, target: CombatUnit, rng: random.Random) -> int:
    if rng.randint(1, 100) > adjusted_hit_chance(action.base_hit, target.template.evasion): return 0
    crit = rng.random() * 100 < max(0.0, min(CRIT_CHANCE_CAP, action.crit_chance))
    base = direct_damage(action.damage_kind, attack=effective_attack(actor), magic=effective_magic(actor), defense=effective_defense(target), spirit=effective_spirit(target), power=action.power, defense_penetration=action.defense_penetration, spirit_penetration=action.spirit_penetration, physical_weight=action.physical_weight, magical_weight=action.magical_weight, crit=crit, direct_damage_reduction=target.template.direct_damage_reduction)
    damage = round_half_up(base * affinity_damage_multiplier(element_affinity(target, action.element)))
    target.hp = max(0, target.hp - damage)
    if action.damage_kind == "physical" and target.has_status("freeze"): target.statuses.pop("freeze", None)
    if target.alive:
        for rider in action.status_riders: _roll_status(action, rider, target, rng)
    return damage


def _indirect_damage(unit: CombatUnit, rate: float) -> int:
    damage = max(1, round_half_up(unit.max_hp * rate))
    unit.hp = max(0, unit.hp - damage)
    return damage


def bleed_rate(unit: CombatUnit) -> float:
    state = unit.statuses["bleed"]
    table = BLEED_ESCALATED_RATE if state.bleed_escalated else BLEED_INITIAL_RATE
    return table[unit.template.rank]


def complete_turn(unit: CombatUnit, *, acted: bool) -> None:
    bleed = unit.statuses.get("bleed")
    if bleed is None: return
    if acted and unit.alive:
        _indirect_damage(unit, bleed_rate(unit))
        if not unit.alive: return
        bleed = unit.statuses.get("bleed")
        if bleed is None: return
    bleed.bleed_turn_age += 1
    if bleed.bleed_turn_age >= 3: bleed.bleed_escalated = True


def turn_is_blocked(unit: CombatUnit, rng: random.Random) -> bool:
    freeze = unit.statuses.get("freeze")
    if freeze is not None:
        maximum = FREEZE_MAX_AFFECTED_ROUNDS[unit.template.rank]
        upcoming = freeze.affected_turns + 1
        if unit.template.rank == "ordinary" and upcoming >= 3:
            if rng.random() >= 0.80: unit.statuses.pop("freeze", None)
            else:
                freeze.affected_turns += 1
                if freeze.affected_turns >= maximum: unit.statuses.pop("freeze", None)
                return True
        elif upcoming <= maximum:
            freeze.affected_turns += 1
            if freeze.affected_turns >= maximum: unit.statuses.pop("freeze", None)
            return True
        else: unit.statuses.pop("freeze", None)
    stun = unit.statuses.get("stun")
    if stun is not None:
        stun.affected_turns += 1
        blocked = rng.random() < STUN_LOSS_CHANCE[unit.template.rank]
        if stun.affected_turns >= 4: unit.statuses.pop("stun", None)
        if blocked: return True
    return False


def end_round(units: Sequence[CombatUnit]) -> None:
    for unit in units:
        if not unit.alive: continue
        burn = unit.statuses.get("burn")
        if burn is not None:
            _indirect_damage(unit, BURN_RATE[unit.template.rank])
            if burn.remaining_rounds is not None:
                burn.remaining_rounds -= 1
                if burn.remaining_rounds <= 0: unit.statuses.pop("burn", None)
        if not unit.alive: continue
        if unit.has_status("bleed"): _indirect_damage(unit, bleed_rate(unit))
        staggered = unit.statuses.get("staggered")
        if staggered is not None and staggered.remaining_rounds is not None:
            staggered.remaining_rounds -= 1
            if staggered.remaining_rounds <= 0: unit.statuses.pop("staggered", None)


def _ko_flag(party: Sequence[CombatUnit], current: bool) -> bool:
    for unit in party:
        if not unit.alive and not unit.ko_counted: unit.ko_counted = True; current = True
    return current


def _outcome(winner, rounds, party, any_ko) -> AdvancedBattleOutcome:
    hp_total, mp_total = sum(u.max_hp for u in party), sum(u.max_mp for u in party)
    return AdvancedBattleOutcome(winner, rounds, any_ko, sum(u.hp for u in party) / hp_total if hp_total else 0.0, sum(u.mp for u in party) / mp_total if mp_total else 1.0)


def run_advanced_battle(party_templates: Sequence[Combatant], enemy_templates: Sequence[Combatant], rng: random.Random, *, max_rounds: int = 100) -> AdvancedBattleOutcome:
    if not 1 <= len(party_templates) <= 4: raise ValueError("party must contain 1-4 combatants")
    if not 1 <= len(enemy_templates) <= 8: raise ValueError("enemies must contain 1-8 combatants")
    units = [CombatUnit(t, i) for i, t in enumerate(tuple(party_templates) + tuple(enemy_templates))]
    party, enemies = [u for u in units if u.side == "party"], [u for u in units if u.side == "enemy"]
    any_ko = False
    for round_number in range(1, max_rounds + 1):
        for actor in turn_order(units):
            if not actor.alive: continue
            if not any(u.alive for u in (enemies if actor.side == "party" else party)): break
            if turn_is_blocked(actor, rng): complete_turn(actor, acted=False); any_ko = _ko_flag(party, any_ko); continue
            action = _choose_action(actor, units, rng)
            actor.mp -= action.mp_cost
            for target in _targets(actor, action, units, rng):
                resolve_heal(actor, action, target) if action.action_kind == "heal" else resolve_damage(actor, action, target, rng)
            complete_turn(actor, acted=True)
            any_ko = _ko_flag(party, any_ko)
        end_round(units); any_ko = _ko_flag(party, any_ko)
        party_alive, enemy_alive = any(u.alive for u in party), any(u.alive for u in enemies)
        if not enemy_alive: return _outcome("party", round_number, party, any_ko)
        if not party_alive: return _outcome("enemy", round_number, party, True)
    return _outcome("draw", max_rounds, party, any_ko)


def simulate_advanced(scenario: AdvancedBattleScenario, *, runs: int = 10_000, seed: int = 1) -> AdvancedSimulationSummary:
    if runs < 1:
        raise ValueError("runs must be positive")
    master = random.Random(seed)
    outcomes = [
        run_advanced_battle(scenario.party, scenario.enemies, random.Random(master.getrandbits(64)), max_rounds=scenario.max_rounds)
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
