"""Generic bounded action-record/replay mechanics.

This module implements the shared behavior used by current Memory/Echo/Duplicate
owners. Encounter-specific scale/clamp values come from repository source data.
"""
from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Iterable, Literal

from ..common import round_half_up
from ..sources.combat import load_combat_rules
from ..sources.replays import BoundedReplayRuleSource
from .action_resolution import resolve_damage
from .models import CombatAction, CombatUnit, DamageKind, Element, TargetScope

ReplayCommandCategory = Literal[
    "attack",
    "ability",
    "standard_card",
    "item",
    "defend",
    "reaction",
    "summon",
    "ultimate",
    "prime_invocation",
    "prime_command",
    "support",
]

_ELIGIBLE_REPLAY_CATEGORIES = frozenset({"attack", "ability", "standard_card"})


@dataclass(frozen=True)
class RecordedDamageSignature:
    source_name: str
    damage_kind: DamageKind
    element: Element
    target_scope: TargetScope
    total_power: int
    hit_count: int
    physical_weight: float | None
    magical_weight: float | None


@dataclass(frozen=True)
class BoundedReplayRule:
    power_scale: float
    min_total_power: int
    max_total_power: int
    base_hit: int

    @classmethod
    def from_source(cls, source: BoundedReplayRuleSource) -> "BoundedReplayRule":
        if not source.complete:
            raise ValueError(f"incomplete bounded replay source: {source.name}")
        assert source.power_scale is not None
        assert source.min_total_power is not None
        assert source.max_total_power is not None
        assert source.base_hit is not None
        return cls(
            power_scale=source.power_scale,
            min_total_power=source.min_total_power,
            max_total_power=source.max_total_power,
            base_hit=source.base_hit,
        )


@dataclass(frozen=True)
class ResolvedReplayAction:
    name: str
    damage_kind: DamageKind
    element: Element
    target_scope: TargetScope
    hit_powers: tuple[int, ...]
    base_hit: int
    physical_weight: float | None
    magical_weight: float | None

    @property
    def total_power(self) -> int:
        return sum(self.hit_powers)

    @property
    def hit_count(self) -> int:
        return len(self.hit_powers)

    def combat_action_for_hit(self, hit_power: int) -> CombatAction:
        return CombatAction(
            name=self.name,
            target_side="enemy",
            target_scope=self.target_scope,
            damage_kind=self.damage_kind,
            element=self.element,
            power=hit_power,
            base_hit=self.base_hit,
            physical_weight=self.physical_weight,
            magical_weight=self.magical_weight,
            # Bounded replay canon strips source riders, penetration, healing,
            # resource/stat effects, forced targeting, and extra actions.
            defense_penetration=0.0,
            spirit_penetration=0.0,
            status_riders=(),
            temporary_modifiers=(),
        )


def replay_category_eligible(category: ReplayCommandCategory, action: CombatAction) -> bool:
    """Return whether a completed action is eligible for bounded replay recording."""
    return category in _ELIGIBLE_REPLAY_CATEGORIES and action.action_kind == "damage"


def _source_total_power(action: CombatAction, hit_powers: Iterable[float] | None) -> tuple[int, int]:
    if hit_powers is not None:
        powers = tuple(float(value) for value in hit_powers)
        if not powers:
            raise ValueError("hit_powers cannot be empty")
        return round_half_up(sum(powers)), len(powers)

    if action.power is None:
        if action.name != "Attack":
            raise ValueError(f"cannot record damage action {action.name!r} without authored Power")
        return load_combat_rules().basic_attack_power, 1
    return round_half_up(action.power), 1


def record_completed_damage_action(
    action: CombatAction,
    *,
    category: ReplayCommandCategory,
    hit_powers: Iterable[float] | None = None,
) -> RecordedDamageSignature | None:
    """Snapshot the completed direct-damage signature after resolution.

    The caller is responsible for invoking this only after the source action has
    completed; ineligible command categories return None.
    """
    if not replay_category_eligible(category, action):
        return None

    total_power, hit_count = _source_total_power(action, hit_powers)
    if action.damage_kind == "hybrid" and (action.physical_weight is None or action.magical_weight is None):
        raise ValueError(f"hybrid action {action.name!r} requires authored weights before recording")

    return RecordedDamageSignature(
        source_name=action.name,
        damage_kind=action.damage_kind,
        element=action.element,
        target_scope=action.target_scope,
        total_power=total_power,
        hit_count=hit_count,
        physical_weight=action.physical_weight,
        magical_weight=action.magical_weight,
    )


def split_total_power_evenly(total_power: int, hit_count: int) -> tuple[int, ...]:
    if total_power < 0:
        raise ValueError("total_power cannot be negative")
    if hit_count < 1:
        raise ValueError("hit_count must be positive")
    quotient, remainder = divmod(total_power, hit_count)
    return tuple(quotient + (1 if index < remainder else 0) for index in range(hit_count))


def transform_bounded_replay(
    recorded: RecordedDamageSignature,
    rule: BoundedReplayRule,
    *,
    name: str,
) -> ResolvedReplayAction:
    converted = round_half_up(recorded.total_power * rule.power_scale)
    total_power = max(rule.min_total_power, min(rule.max_total_power, converted))
    return ResolvedReplayAction(
        name=name,
        damage_kind=recorded.damage_kind,
        element=recorded.element,
        target_scope=recorded.target_scope,
        hit_powers=split_total_power_evenly(total_power, recorded.hit_count),
        base_hit=rule.base_hit,
        physical_weight=recorded.physical_weight,
        magical_weight=recorded.magical_weight,
    )


@dataclass
class BoundedReplayState:
    """Persistent most-recent-record state for bounded replay enemies.

    These current replay owners keep the most recent eligible completed record.
    A later ineligible action does not erase it, and using the replay does not
    consume it. Encounter mechanics with consume-on-use semantics should use a
    different state type.
    """

    name: str
    rule: BoundedReplayRule
    recorded: RecordedDamageSignature | None = None

    @property
    def available(self) -> bool:
        return self.recorded is not None

    def observe_completed_action(
        self,
        action: CombatAction,
        *,
        category: ReplayCommandCategory,
        hit_powers: Iterable[float] | None = None,
    ) -> bool:
        candidate = record_completed_damage_action(
            action,
            category=category,
            hit_powers=hit_powers,
        )
        if candidate is None:
            return False
        self.recorded = candidate
        return True

    def materialize(self) -> ResolvedReplayAction | None:
        if self.recorded is None:
            return None
        return transform_bounded_replay(self.recorded, self.rule, name=self.name)


def resolve_bounded_replay(
    actor: CombatUnit,
    replay: ResolvedReplayAction,
    targets: Iterable[CombatUnit],
    rng: random.Random,
) -> int:
    """Resolve all preserved replay hits using the copier's own combat stats."""
    target_list = tuple(targets)
    total_damage = 0
    for hit_power in replay.hit_powers:
        hit_action = replay.combat_action_for_hit(hit_power)
        for target in target_list:
            if target.alive:
                total_damage += resolve_damage(actor, hit_action, target, rng)
    return total_damage


__all__ = [
    "BoundedReplayRule",
    "BoundedReplayState",
    "RecordedDamageSignature",
    "ReplayCommandCategory",
    "ResolvedReplayAction",
    "record_completed_damage_action",
    "replay_category_eligible",
    "resolve_bounded_replay",
    "split_total_power_evenly",
    "transform_bounded_replay",
]
