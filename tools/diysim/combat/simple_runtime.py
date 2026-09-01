"""Stable simple direct-battle runtime using repo-owned rule defaults."""
from __future__ import annotations

from dataclasses import dataclass, field
import math
import random
import statistics
from typing import Iterable, Literal, Sequence

from ..progression.stats import Stats
from ..sources.combat import load_combat_rules
from ..sources.enemies import load_enemy_system_rules
from ..sources.party import load_party_rules
from .basic_attack import basic_attack_action
from .damage import direct_damage
from .hit_evasion import adjusted_hit_chance
from .models import DamageKind, Side

TargetPolicy = Literal["random", "lowest_hp", "highest_attack"]


@dataclass(frozen=True)
class ActionProfile:
    name: str
    kind: DamageKind = "physical"
    power: float | None = None
    base_hit: int | None = None
    crit_chance: float | None = None
    defense_penetration: float = 0.0
    spirit_penetration: float = 0.0
    physical_weight: float | None = None
    magical_weight: float | None = None
    weight: float | None = None


@dataclass(frozen=True)
class CombatantTemplate:
    name: str
    side: Side
    stats: Stats
    actions: tuple[ActionProfile, ...] = ()
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
        return self.__dict__.copy()


@dataclass(frozen=True)
class BattleScenario:
    party: tuple[CombatantTemplate, ...]
    enemies: tuple[CombatantTemplate, ...]
    max_rounds: int = 100

    def __post_init__(self) -> None:
        max_party = load_party_rules().active_battle_party
        max_enemies = load_enemy_system_rules().max_active_enemies
        if not 1 <= len(self.party) <= max_party:
            raise ValueError(f"party must contain 1-{max_party} combatants")
        if not 1 <= len(self.enemies) <= max_enemies:
            raise ValueError(f"enemies must contain 1-{max_enemies} combatants")
        if self.max_rounds < 1:
            raise ValueError("max_rounds must be positive")
        if any(unit.side != "party" for unit in self.party):
            raise ValueError("all party templates must have side='party'")
        if any(unit.side != "enemy" for unit in self.enemies):
            raise ValueError("all enemy templates must have side='enemy'")


def _repo_basic_attack_profile() -> ActionProfile:
    action = basic_attack_action()
    return ActionProfile(
        name=action.name,
        kind=action.damage_kind,
        power=action.power,
        base_hit=action.base_hit,
        crit_chance=action.crit_chance,
        defense_penetration=action.defense_penetration,
        spirit_penetration=action.spirit_penetration,
        physical_weight=action.physical_weight,
        magical_weight=action.magical_weight,
        weight=None,
    )


def _choose_action(unit: BattleUnit, rng: random.Random) -> ActionProfile:
    actions = unit.template.actions
    if not actions:
        return _repo_basic_attack_profile()

    weights = tuple(action.weight for action in actions)
    if all(weight is None for weight in weights):
        if unit.side == "enemy" and load_enemy_system_rules().missing_weight_selection != "uniform":
            raise ValueError("unsupported repo enemy-selection rule")
        return rng.choice(actions)
    if any(weight is None for weight in weights):
        raise ValueError(
            f"{unit.template.name} mixes explicit and missing action weights; "
            "source/policy authority must resolve selection before simulation"
        )
    if sum(max(0.0, weight) for weight in weights) <= 0:
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
    rules = load_combat_rules()
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
            base_hit = rules.default_player_base_hit if action.base_hit is None else action.base_hit
            if rng.randint(1, 100) > adjusted_hit_chance(base_hit, target.template.evasion):
                continue
            crit_chance = rules.base_crit_chance if action.crit_chance is None else action.crit_chance
            crit_chance = max(0.0, min(rules.crit_chance_cap, crit_chance))
            crit = rng.random() * 100.0 < crit_chance
            if action.power is None:
                if action.name != "Attack":
                    raise ValueError(f"action {action.name!r} has no authored Power")
                power = rules.basic_attack_power
            else:
                power = action.power
            if action.kind == "hybrid":
                if action.physical_weight is None or action.magical_weight is None:
                    raise ValueError(f"hybrid action {action.name!r} requires authored weights")
                physical_weight = action.physical_weight
                magical_weight = action.magical_weight
            else:
                physical_weight = 0.5 if action.physical_weight is None else action.physical_weight
                magical_weight = 0.5 if action.magical_weight is None else action.magical_weight
            damage = direct_damage(
                action.kind,
                attack=actor.stats.attack,
                magic=actor.stats.magic,
                defense=target.stats.defense,
                spirit=target.stats.spirit,
                power=power,
                defense_penetration=action.defense_penetration,
                spirit_penetration=action.spirit_penetration,
                physical_weight=physical_weight,
                magical_weight=magical_weight,
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
