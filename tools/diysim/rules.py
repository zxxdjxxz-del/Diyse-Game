"""Current-canon Phase 2 rule primitives for Diyse balance simulation.

Authority: ELEMENTS.md, STATUS_EFFECTS.md, MP_COST_RULES.md, BLUE_WARDEN.md.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal, Sequence
from .core import BASE_CRIT_CHANCE, Stats, round_half_up

Side = Literal["party", "enemy"]
DamageKind = Literal["physical", "magical", "hybrid"]
ActionKind = Literal["damage", "heal"]
TargetSide = Literal["enemy", "ally", "self"]
TargetScope = Literal["one", "all"]
Rank = Literal["ordinary", "regional_hunt", "major_boss"]
Element = Literal["neutral", "colorless", "fire", "ice", "lightning", "earth", "ruin"]
Affinity = Literal["weak", "neutral", "resistant", "strongly_resistant", "immune"]
StatusName = Literal["burn", "freeze", "stun", "staggered", "bleed"]

AFFINITY_DAMAGE_MULTIPLIERS = {"weak": 1.25, "neutral": 1.0, "resistant": 0.8, "strongly_resistant": 0.6, "immune": 0.0}
LINKED_STATUS = {"fire": "burn", "ice": "freeze", "lightning": "stun", "earth": "staggered"}
BURN_RATE = {"ordinary": 0.06, "regional_hunt": 0.045, "major_boss": 0.03}
BLEED_INITIAL_RATE = {"ordinary": 0.03, "regional_hunt": 0.0225, "major_boss": 0.015}
BLEED_ESCALATED_RATE = {"ordinary": 0.04, "regional_hunt": 0.03, "major_boss": 0.02}
STUN_LOSS_CHANCE = {"ordinary": 0.40, "regional_hunt": 0.25, "major_boss": 0.20}
STAGGERED_ROUNDS = {"ordinary": 5, "regional_hunt": 4, "major_boss": 3}
FREEZE_MAX_AFFECTED_ROUNDS = {"ordinary": 4, "regional_hunt": 2, "major_boss": 1}


def affinity_damage_multiplier(affinity: Affinity) -> float:
    return AFFINITY_DAMAGE_MULTIPLIERS[affinity]


def linked_status_affinity_modifier(element: Element, status: StatusName, affinity: Affinity) -> int | None:
    if LINKED_STATUS.get(element) != status:
        return 0
    if affinity == "immune":
        return None
    if affinity == "weak":
        return 10
    if affinity in ("resistant", "strongly_resistant"):
        return -10
    return 0


def status_application_chance(base_chance: float, *, affinity_modifier: int = 0, specialist_bonus: int = 0, reliability_bonus: int = 0, status_resistance: int = 0, immune: bool = False) -> float:
    if immune:
        return 0.0
    chance = base_chance + affinity_modifier + specialist_bonus + reliability_bonus - status_resistance
    return max(5.0, min(95.0, chance))


def resolve_mp_cost(base_cost: int, *, flat_delta: int = 0, remaining_cost_factors: Sequence[float] = ()) -> int:
    if base_cost < 0 or any(factor < 0 for factor in remaining_cost_factors):
        raise ValueError("MP costs and remaining-cost factors cannot be negative")
    if base_cost == 0:
        return 0
    value = max(1, base_cost + flat_delta)
    for factor in remaining_cost_factors:
        value *= factor
    return max(1, round_half_up(value))


def healing_amount(target_max_hp: int, caster_magic: int, *, max_hp_percent: float = 0.0, magic_scaling: float = 0.0, potency_multiplier: float = 1.0) -> int:
    if target_max_hp < 1 or caster_magic < 0:
        raise ValueError("invalid healing stats")
    if min(max_hp_percent, magic_scaling, potency_multiplier) < 0:
        raise ValueError("healing parameters cannot be negative")
    return max(0, round_half_up((target_max_hp * max_hp_percent + caster_magic * magic_scaling) * potency_multiplier))


@dataclass(frozen=True)
class StatusRider:
    status: StatusName
    base_chance: float
    specialist_bonus: int = 0
    reliability_bonus: int = 0


@dataclass(frozen=True)
class CombatAction:
    name: str
    action_kind: ActionKind = "damage"
    mp_cost: int = 0
    target_side: TargetSide = "enemy"
    target_scope: TargetScope = "one"
    damage_kind: DamageKind = "physical"
    element: Element = "neutral"
    power: float = 100.0
    base_hit: int = 100
    crit_chance: float = BASE_CRIT_CHANCE
    defense_penetration: float = 0.0
    spirit_penetration: float = 0.0
    physical_weight: float = 0.5
    magical_weight: float = 0.5
    heal_max_hp_percent: float = 0.0
    heal_magic_scaling: float = 0.0
    healing_potency: float = 1.0
    clear_harmful_statuses: int | Literal["all"] = 0
    status_riders: tuple[StatusRider, ...] = ()
    weight: float = 1.0


BASIC_ATTACK = CombatAction("Attack")


@dataclass(frozen=True)
class Combatant:
    name: str
    side: Side
    stats: Stats
    actions: tuple[CombatAction, ...] = (BASIC_ATTACK,)
    evasion: int = 0
    direct_damage_reduction: float = 0.0
    rank: Rank = "ordinary"
    status_resistance: int = 0
    status_immunities: frozenset[StatusName] = frozenset()
    elemental_affinities: dict[str, Affinity] = field(default_factory=dict)


@dataclass
class ActiveStatus:
    name: StatusName
    remaining_rounds: int | None = None
    affected_turns: int = 0
    bleed_turn_age: int = 0
    bleed_escalated: bool = False


@dataclass
class CombatUnit:
    template: Combatant
    stable_index: int
    hp: int = field(init=False)
    mp: int = field(init=False)
    statuses: dict[StatusName, ActiveStatus] = field(default_factory=dict)
    ko_counted: bool = False

    def __post_init__(self) -> None:
        self.hp = self.template.stats.hp
        self.mp = self.template.stats.mp

    @property
    def alive(self) -> bool: return self.hp > 0
    @property
    def side(self) -> Side: return self.template.side
    @property
    def max_hp(self) -> int: return self.template.stats.hp
    @property
    def max_mp(self) -> int: return self.template.stats.mp
    def has_status(self, status: StatusName) -> bool: return status in self.statuses


def element_affinity(unit: CombatUnit, element: Element) -> Affinity:
    if element in ("neutral", "colorless"):
        return "neutral"
    return unit.template.elemental_affinities.get(element, "neutral")


def effective_attack(unit: CombatUnit) -> float:
    return unit.template.stats.attack * (0.8 if unit.has_status("staggered") else 1.0)


def effective_magic(unit: CombatUnit) -> float:
    return unit.template.stats.magic * (0.8 if unit.has_status("staggered") else 1.0)


def effective_defense(unit: CombatUnit) -> float:
    return unit.template.stats.defense * (0.9 if unit.has_status("burn") else 1.0)


def effective_spirit(unit: CombatUnit) -> float:
    return unit.template.stats.spirit * (0.9 if unit.has_status("burn") else 1.0)


def effective_speed(unit: CombatUnit) -> float:
    return unit.template.stats.speed * (0.8 if unit.has_status("staggered") else 1.0)


def apply_status(target: CombatUnit, status: StatusName) -> bool:
    if status in target.template.status_immunities:
        return False
    if status in target.statuses:
        if status == "burn": target.statuses[status].remaining_rounds = 4
        elif status == "staggered": target.statuses[status].remaining_rounds = STAGGERED_ROUNDS[target.template.rank]
        elif status == "bleed": pass
        else: return False
        return True
    duration = 4 if status == "burn" else STAGGERED_ROUNDS[target.template.rank] if status == "staggered" else None
    target.statuses[status] = ActiveStatus(status, remaining_rounds=duration)
    return True
