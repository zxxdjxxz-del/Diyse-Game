"""Shared combat data models for the Diyse simulator.

Numeric canon defaults are resolved from repository sources, not stored here.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal

from ..progression.stats import Stats

Side = Literal["party", "enemy"]
DamageKind = Literal["physical", "magical", "hybrid"]
ActionKind = Literal["damage", "heal"]
TargetSide = Literal["enemy", "ally", "self"]
TargetScope = Literal["one", "all"]
Rank = Literal["ordinary", "regional_hunt", "major_boss"]
Element = Literal["neutral", "colorless", "fire", "ice", "lightning", "earth", "ruin"]
Affinity = Literal["weak", "neutral", "resistant", "strongly_resistant", "immune"]
StatusName = Literal["burn", "freeze", "stun", "staggered", "bleed"]


@dataclass(frozen=True)
class StatusRider:
    status: StatusName
    base_chance: float
    specialist_bonus: int = 0
    reliability_bonus: int = 0


@dataclass(frozen=True)
class TemporaryModifierSpec:
    effect_id: str
    duration_rounds: int
    status_resistance_flat: int = 0

    def __post_init__(self) -> None:
        if not self.effect_id:
            raise ValueError("effect_id is required")
        if self.duration_rounds < 1:
            raise ValueError("duration_rounds must be positive")


@dataclass
class ActiveTemporaryModifier:
    effect_id: str
    remaining_rounds: int
    status_resistance_flat: int = 0


@dataclass(frozen=True)
class CombatAction:
    name: str
    action_kind: ActionKind = "damage"
    mp_cost: int = 0
    target_side: TargetSide = "enemy"
    target_scope: TargetScope = "one"
    damage_kind: DamageKind = "physical"
    element: Element = "neutral"
    power: float | None = None
    base_hit: int | None = None
    crit_chance: float | None = None
    defense_penetration: float = 0.0
    spirit_penetration: float = 0.0
    physical_weight: float | None = None
    magical_weight: float | None = None
    final_damage_multiplier: float = 1.0
    heal_max_hp_percent: float = 0.0
    heal_magic_scaling: float = 0.0
    healing_potency: float = 1.0
    clear_harmful_statuses: int | Literal["all"] = 0
    status_riders: tuple[StatusRider, ...] = ()
    temporary_modifiers: tuple[TemporaryModifierSpec, ...] = ()
    weight: float | None = None


@dataclass(frozen=True)
class Combatant:
    name: str
    side: Side
    stats: Stats
    actions: tuple[CombatAction, ...] = ()
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
    temporary_modifiers: dict[str, ActiveTemporaryModifier] = field(default_factory=dict)
    tactical_states: dict[str, str] = field(default_factory=dict)
    ko_counted: bool = False

    def __post_init__(self) -> None:
        self.hp = self.template.stats.hp
        self.mp = self.template.stats.mp

    @property
    def alive(self) -> bool:
        return self.hp > 0

    @property
    def side(self) -> Side:
        return self.template.side

    @property
    def max_hp(self) -> int:
        return self.template.stats.hp

    @property
    def max_mp(self) -> int:
        return self.template.stats.mp

    def has_status(self, status: StatusName) -> bool:
        return status in self.statuses