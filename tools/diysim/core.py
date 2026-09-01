from __future__ import annotations

from dataclasses import dataclass, field, replace
from itertools import product
import math
import random
import statistics
from typing import Iterable, Literal, Sequence

DamageKind = Literal["physical", "magical", "hybrid"]
Side = Literal["party", "enemy"]
TargetPolicy = Literal["random", "lowest_hp", "highest_attack"]

LEVEL_CAP = 70
BASE_CRIT_CHANCE = 5.0
CRIT_CHANCE_CAP = 50.0
CRIT_MULTIPLIER = 1.5
PENETRATION_CAP = 0.75
MIN_HIT_CHANCE = 5
MAX_HIT_CHANCE = 100

STAT_KEYS = ("hp", "mp", "attack", "magic", "defense", "spirit", "speed")

CLASS_MULTIPLIERS: dict[str, dict[str, float]] = {
    "Crest Knight": {"hp": 1.05, "mp": 0.90, "attack": 1.08, "magic": 0.95, "defense": 1.12, "spirit": 1.00, "speed": 0.96},
    "Blue Warden": {"hp": 1.00, "mp": 1.12, "attack": 0.88, "magic": 1.10, "defense": 0.98, "spirit": 1.10, "speed": 0.98},
    "War Archer": {"hp": 1.00, "mp": 0.95, "attack": 1.15, "magic": 0.82, "defense": 0.95, "spirit": 0.90, "speed": 1.00},
    "Cardweaver": {"hp": 0.88, "mp": 1.15, "attack": 0.85, "magic": 1.08, "defense": 0.86, "spirit": 1.00, "speed": 1.18},
    "Green Arcanist": {"hp": 0.82, "mp": 1.25, "attack": 0.72, "magic": 1.25, "defense": 0.78, "spirit": 1.12, "speed": 1.02},
    "Ruin Vanguard": {"hp": 1.20, "mp": 0.76, "attack": 1.22, "magic": 0.85, "defense": 1.18, "spirit": 0.85, "speed": 0.88},
    "Crest Arcanist": {"hp": 0.90, "mp": 1.15, "attack": 0.85, "magic": 1.15, "defense": 0.92, "spirit": 1.05, "speed": 1.00},
    "Vowblade": {"hp": 1.00, "mp": 0.92, "attack": 1.10, "magic": 0.78, "defense": 1.00, "spirit": 1.12, "speed": 1.02},
    "Routeweaver": {"hp": 0.98, "mp": 1.08, "attack": 1.02, "magic": 1.02, "defense": 0.94, "spirit": 0.98, "speed": 1.05},
    "Proofhunter": {"hp": 0.92, "mp": 1.00, "attack": 1.08, "magic": 1.08, "defense": 0.90, "spirit": 0.96, "speed": 1.04},
    "Axiomblade": {"hp": 1.04, "mp": 0.92, "attack": 1.08, "magic": 1.08, "defense": 1.02, "spirit": 0.96, "speed": 1.00},
    "Ruin Warden": {"hp": 1.05, "mp": 1.05, "attack": 1.00, "magic": 1.05, "defense": 1.02, "spirit": 1.05, "speed": 0.90},
}


def round_half_up(value: float) -> int:
    if value < 0:
        return -math.floor(-value + 0.5)
    return math.floor(value + 0.5)


def round_nearest_100(value: float) -> int:
    # The published EXP table establishes ties-to-even behavior at exact x50
    # boundaries (notably the Lv53 -> Lv54 cost: 13,650 -> 13,600).
    return int(round(value / 100.0)) * 100


@dataclass(frozen=True)
class Stats:
    hp: int
    mp: int
    attack: int
    magic: int
    defense: int
    spirit: int
    speed: int

    def as_dict(self) -> dict[str, int]:
        return {key: getattr(self, key) for key in STAT_KEYS}


def neutral_natural_stats(level: int) -> dict[str, float]:
    if not 1 <= level <= LEVEL_CAP:
        raise ValueError(f"level must be between 1 and {LEVEL_CAP}")
    x = level - 1
    return {
        "hp": 220 + 34 * x + 0.28 * x * x,
        "mp": 28 + 3.25 * x + 0.018 * x * x,
        "attack": 18 + 2.05 * x + 0.008 * x * x,
        "magic": 18 + 2.05 * x + 0.008 * x * x,
        "defense": 16 + 1.70 * x + 0.006 * x * x,
        "spirit": 16 + 1.70 * x + 0.006 * x * x,
        "speed": 22 + 0.52 * x,
    }


def natural_stats(level: int, class_name: str | None = None, equipment: dict[str, int] | None = None) -> Stats:
    raw = neutral_natural_stats(level)
    multipliers = {key: 1.0 for key in STAT_KEYS}
    if class_name is not None:
        try:
            multipliers = CLASS_MULTIPLIERS[class_name]
        except KeyError as exc:
            raise ValueError(f"unknown class: {class_name}") from exc

    rounded = {key: round_half_up(raw[key] * multipliers[key]) for key in STAT_KEYS}
    for key, amount in (equipment or {}).items():
        if key not in STAT_KEYS:
            raise ValueError(f"unknown equipment stat: {key}")
        rounded[key] += int(amount)
    return Stats(**rounded)


def level_up_cost(current_level: int) -> int:
    if not 1 <= current_level < LEVEL_CAP:
        raise ValueError(f"current_level must be between 1 and {LEVEL_CAP - 1}")
    if current_level < 17:
        return 100 * (current_level**2 - (current_level - 1) ** 2)
    base_cost = 100 * (2 * current_level - 1)
    multiplier = 1 + 0.35 * (current_level - 17) / 42
    return round_nearest_100(base_cost * multiplier)


def cumulative_exp(level: int) -> int:
    if not 1 <= level <= LEVEL_CAP:
        raise ValueError(f"level must be between 1 and {LEVEL_CAP}")
    if level <= 17:
        return 100 * (level - 1) ** 2
    total = 100 * 16**2
    for current_level in range(17, level):
        total += level_up_cost(current_level)
    return total


def level_from_exp(exp: int) -> int:
    if exp < 0:
        raise ValueError("exp cannot be negative")
    level = 1
    for candidate in range(2, LEVEL_CAP + 1):
        if exp < cumulative_exp(candidate):
            break
        level = candidate
    return level


def exp_to_next_level(exp: int) -> int:
    level = level_from_exp(exp)
    if level == LEVEL_CAP:
        return 0
    return cumulative_exp(level + 1) - exp


def adjusted_hit_chance(action_base_hit: int, target_evasion: int, *, base_hit_percent: float = 1.0, flat_base_hit: int = 0, evasion_percent: float = 1.0, flat_evasion: int = 0) -> int:
    adjusted_base_hit = round_half_up(action_base_hit * base_hit_percent) + flat_base_hit
    effective_evasion = round_half_up(target_evasion * evasion_percent) + flat_evasion
    return max(MIN_HIT_CHANCE, min(MAX_HIT_CHANCE, adjusted_base_hit - effective_evasion))


def _capped_penetration(value: float) -> float:
    return max(0.0, min(PENETRATION_CAP, value))


def physical_damage(attack: float, defense: float, power: float, *, defense_penetration: float = 0.0) -> float:
    effective_defense = max(0.0, defense) * (1.0 - _capped_penetration(defense_penetration))
    denominator = attack + effective_defense
    if attack <= 0 or denominator <= 0:
        return 0.0
    return (attack * attack / denominator) * (power / 100.0)


def magical_damage(magic: float, spirit: float, power: float, *, spirit_penetration: float = 0.0) -> float:
    effective_spirit = max(0.0, spirit) * (1.0 - _capped_penetration(spirit_penetration))
    denominator = magic + effective_spirit
    if magic <= 0 or denominator <= 0:
        return 0.0
    return (magic * magic / denominator) * (power / 100.0)


def direct_damage(kind: DamageKind, *, attack: float, magic: float, defense: float, spirit: float, power: float, defense_penetration: float = 0.0, spirit_penetration: float = 0.0, physical_weight: float = 0.5, magical_weight: float = 0.5, crit: bool = False, direct_damage_reduction: float = 0.0) -> int:
    if power < 0:
        raise ValueError("power cannot be negative")
    if kind == "physical":
        pre = physical_damage(attack, defense, power, defense_penetration=defense_penetration)
    elif kind == "magical":
        pre = magical_damage(magic, spirit, power, spirit_penetration=spirit_penetration)
    elif kind == "hybrid":
        if physical_weight < 0 or magical_weight < 0:
            raise ValueError("hybrid weights cannot be negative")
        if not math.isclose(physical_weight + magical_weight, 1.0, abs_tol=1e-9):
            raise ValueError("hybrid weights must sum to 1.0")
        pre = physical_weight * physical_damage(attack, defense, power, defense_penetration=defense_penetration) + magical_weight * magical_damage(magic, spirit, power, spirit_penetration=spirit_penetration)
    else:
        raise ValueError(f"unknown damage kind: {kind}")

    if crit:
        pre *= CRIT_MULTIPLIER
    reduction = max(0.0, min(1.0, direct_damage_reduction))
    return max(0, round_half_up(pre * (1.0 - reduction)))


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
    # Exact Speed ties: party before enemy. Within a side, scenario order is the
    # deterministic stand-in for player-selected party tie order / stable enemy order.
    return sorted((unit for unit in units if unit.alive), key=lambda unit: (-unit.stats.speed, 0 if unit.side == "party" else 1, unit.stable_index))


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


def scale_enemy_side(scenario: BattleScenario, *, hp_multiplier: float = 1.0, attack_multiplier: float = 1.0, defense_multiplier: float = 1.0) -> BattleScenario:
    if min(hp_multiplier, attack_multiplier, defense_multiplier) <= 0:
        raise ValueError("multipliers must be positive")
    scaled = []
    for enemy in scenario.enemies:
        stats = enemy.stats
        scaled_stats = replace(
            stats,
            hp=max(1, round_half_up(stats.hp * hp_multiplier)),
            attack=max(0, round_half_up(stats.attack * attack_multiplier)),
            defense=max(0, round_half_up(stats.defense * defense_multiplier)),
        )
        scaled.append(replace(enemy, stats=scaled_stats))
    return replace(scenario, enemies=tuple(scaled))


def sweep_enemy_stats(scenario: BattleScenario, *, hp_multipliers: Sequence[float], attack_multipliers: Sequence[float], defense_multipliers: Sequence[float], runs: int = 2_000, seed: int = 1) -> list[dict[str, float | int]]:
    rows: list[dict[str, float | int]] = []
    for index, (hp_mult, attack_mult, defense_mult) in enumerate(product(hp_multipliers, attack_multipliers, defense_multipliers)):
        candidate = scale_enemy_side(scenario, hp_multiplier=hp_mult, attack_multiplier=attack_mult, defense_multiplier=defense_mult)
        summary = simulate(candidate, runs=runs, seed=seed + index)
        rows.append({
            "hp_multiplier": hp_mult,
            "attack_multiplier": attack_mult,
            "defense_multiplier": defense_mult,
            "win_rate": summary.win_rate,
            "wipe_rate": summary.wipe_rate,
            "any_ko_rate": summary.any_ko_rate,
            "median_rounds": summary.median_rounds,
            "p90_rounds": summary.p90_rounds,
            "mean_remaining_party_hp": summary.mean_remaining_party_hp,
        })
    return rows
