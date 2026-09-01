"""Stable Phase-1 direct-battle runtime.

This intentionally stays simpler than the richer battle runtime so basic math
regressions remain easy to isolate.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import math
import random
import statistics
from typing import Iterable, Literal, Sequence

from ..progression.stats import Stats
from .criticals import BASE_CRIT_CHANCE, CRIT_CHANCE_CAP
from .damage import direct_damage
from .hit_evasion import adjusted_hit_chance
from .models import DamageKind, Side

TargetPolicy = Literal["random", "lowest_hp", "highest_attack"]


@dataclass(frozen=True)
class ActionProfile:
    name: str
    kind: DamageKind = "physical"
    power: float = 100.0
    base_hit: int = 100
    crit_chance: float = BASE_CRIT_CHANCE
    defense_penetration: float = 0.0
    spirit_penetration: float = 0.0
    physical_weight: float = 0.5
    magical_weight: float = 0.5
    weight: float = 1.0


@dataclass(frozen=True)
class CombatantTemplate:
    name: str
    side: Side
    stats: Stats
    actions: tuple[ActionProfile, ...] = (ActionProfile("Attack"),)
    evasion: int = 0
    direct_damage_reduction: float = 0.0
    target_policy: TargetPolicy = "random"


@dataclass
class BattleUnit:
    template: CombatantTemplate
    stable_index: int
    hp: int = field(init=False)
    ko_counted: bool = False

    def __post_init__(self) -> None:
        self.hp = self.template.stats.hp

    @property
    def alive(self) -> bool:
        return self.hp > 0

    @property
    def side(self) -> Side:
        return self.template.side

    @property
    def stats(self) -> Stats:
        return self.template.stats


@dataclass(frozen=True)
class BattleOutcome:
    winner: Literal["party", "enemy", "draw"]
    rounds: int
    any_party_ko: bool
    party_hp_fraction: float


@dataclass(frozen=True)
class SimulationSummary:
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

    def as_dict(self) -> dict[str, int | float]:
        return {
            "runs": self.runs,
            "party_wins": self.party_wins,
            "enemy_wins": self.enemy_wins,
            "draws": self.draws,
            "win_rate": self.win_rate,
            "wipe_rate": self.wipe_rate,
            "any_ko_rate": self.any_ko_rate,
            "mean_rounds": self.mean_rounds,
            "median_rounds": self.median_rounds,
            "p90_rounds": self.p90_rounds,
            "mean_remaining_party_hp": self.mean_remaining_party_hp,
        }


@dataclass(frozen=True)
class BattleScenario:
    party: tuple[CombatantTemplate, ...]
    enemies: tuple[CombatantTemplate, ...]
    max_rounds: int = 100

    def __post_init__(self) -> None:
        if not 1 <= len(self.party) <= 4:
            raise ValueError("party must contain 1-4 combatants")
        if not 1 <= len(self.enemies) <= 8:
            raise ValueError("enemies must contain 1-8 combatants")
        if self.max_rounds < 1:
            raise ValueError("max_rounds must be positive")
        if any(unit.side != "party" for unit in self.party):
            raise ValueError("all party templates must have side='party'")
        if any(unit.side != "enemy" for unit in self.enemies):
            raise ValueError("all enemy templates must have side='enemy'")


def _choose_action(unit: BattleUnit, rng: random.Random) -> ActionProfile:
    actions = unit.template.actions
    weights = [max(0.0, action.weight) for action in actions]
    if not actions or sum(weights) <= 0:
        raise ValueError(f"{unit.template.name} has no selectable actions")
    return rng.choices(actions, weights=weights, k=1)[0]


def _choose_target(unit: BattleUnit, candidates: Sequence[BattleUnit], rng: random.Random) -> BattleUnit:
    if unit.template.target_policy == "random":
        return rng.choice(list(candidates))
    if unit.template.target_policy == "lowest_hp":
        return min(candidates, key=lambda target: (target.hp / target.stats.hp, target.stable_index))
    if unit.template.target_policy == "highest_attack":
        return max(candidates, key=lambda target: (target.stats.attack, -target.stable_index))
    raise ValueError(f"unsupported target policy: {unit.template.target_policy}")


def _turn_order(units: Iterable[BattleUnit]) -> list[BattleUnit]:
    return sorted(
        (unit for unit in units if unit.alive),
        key=lambda unit: (-unit.stats.speed, 0 if unit.side == "party" else 1, unit.stable_index),
    )


def run_battle(scenario: BattleScenario, rng: random.Random) -> BattleOutcome:
    all_templates = list(scenario.party) + list(scenario.enemies)
    units = [BattleUnit(template=template, stable_index=i) for i, template in enumerate(all_templates)]
    party = [unit for unit in units if unit.side == "party"]
    enemies = [unit for unit in units if unit.side == "enemy"]
    any_party_ko = False

    for round_number in range(1, scenario.max_rounds + 1):
        for actor in _turn_order(units):
            if not actor.alive:
                continue
            targets = [unit for unit in (enemies if actor.side == "party" else party) if unit.alive]
            if not targets:
                break
            action = _choose_action(actor, rng)
            target = _choose_target(actor, targets, rng)
            hit_chance = adjusted_hit_chance(action.base_hit, target.template.evasion)
            if rng.randint(1, 100) > hit_chance:
                continue
            crit_chance = max(0.0, min(CRIT_CHANCE_CAP, action.crit_chance))
            crit = rng.random() * 100.0 < crit_chance
            damage = direct_damage(
                action.kind,
                attack=actor.stats.attack,
                magic=actor.stats.magic,
                defense=target.stats.defense,
                spirit=target.stats.spirit,
                power=action.power,
                defense_penetration=action.defense_penetration,
                spirit_penetration=action.spirit_penetration,
                physical_weight=action.physical_weight,
                magical_weight=action.magical_weight,
                crit=crit,
                direct_damage_reduction=target.template.direct_damage_reduction,
            )
            target.hp = max(0, target.hp - damage)
            if target.side == "party" and not target.alive and not target.ko_counted:
                target.ko_counted = True
                any_party_ko = True

        party_alive = any(unit.alive for unit in party)
        enemy_alive = any(unit.alive for unit in enemies)
        if not enemy_alive:
            total_hp = sum(unit.stats.hp for unit in party)
            remaining = sum(unit.hp for unit in party)
            return BattleOutcome("party", round_number, any_party_ko, remaining / total_hp)
        if not party_alive:
            return BattleOutcome("enemy", round_number, True, 0.0)

    total_hp = sum(unit.stats.hp for unit in party)
    remaining = sum(unit.hp for unit in party)
    return BattleOutcome("draw", scenario.max_rounds, any_party_ko, remaining / total_hp)


def _percentile90(values: Sequence[int]) -> float:
    ordered = sorted(values)
    index = max(0, math.ceil(0.90 * len(ordered)) - 1)
    return float(ordered[index])


def simulate(scenario: BattleScenario, *, runs: int = 10_000, seed: int = 1) -> SimulationSummary:
    if runs < 1:
        raise ValueError("runs must be positive")
    master = random.Random(seed)
    outcomes = [run_battle(scenario, random.Random(master.getrandbits(64))) for _ in range(runs)]
    party_wins = sum(outcome.winner == "party" for outcome in outcomes)
    enemy_wins = sum(outcome.winner == "enemy" for outcome in outcomes)
    draws = runs - party_wins - enemy_wins
    rounds = [outcome.rounds for outcome in outcomes]
    return SimulationSummary(
        runs=runs,
        party_wins=party_wins,
        enemy_wins=enemy_wins,
        draws=draws,
        win_rate=party_wins / runs,
        wipe_rate=enemy_wins / runs,
        any_ko_rate=sum(outcome.any_party_ko for outcome in outcomes) / runs,
        mean_rounds=statistics.fmean(rounds),
        median_rounds=float(statistics.median(rounds)),
        p90_rounds=_percentile90(rounds),
        mean_remaining_party_hp=statistics.fmean(outcome.party_hp_fraction for outcome in outcomes),
    )
