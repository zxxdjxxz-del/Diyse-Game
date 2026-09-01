"""Cardweaver Living Archive / Echo Weave tactical-state primitives.

The repository owns eligibility, capacity, potency, and cost values. This module
only supplies the reusable record-window and reproduction mechanics.
"""
from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Literal

from ..common import round_half_up
from .models import CombatAction

ArchiveCategory = Literal["ability", "standard_card"]


@dataclass(frozen=True)
class LivingArchiveRecord:
    source_actor: str
    category: ArchiveCategory
    action: CombatAction
    authored_base_mp: int


@dataclass
class LivingArchiveState:
    capacity: int
    records: list[LivingArchiveRecord] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.capacity < 1:
            raise ValueError("Living Archive capacity must be positive")

    def observe_completed_action(
        self,
        action: CombatAction,
        *,
        source_actor: str,
        category: ArchiveCategory,
        authored_base_mp: int | None = None,
    ) -> None:
        """Record one eligible allied immediate Ability/Card after completion."""
        base_mp = action.mp_cost if authored_base_mp is None else authored_base_mp
        record = LivingArchiveRecord(
            source_actor=source_actor,
            category=category,
            action=action,
            authored_base_mp=max(0, int(base_mp)),
        )
        self.records.append(record)
        if len(self.records) > self.capacity:
            del self.records[:-self.capacity]

    def on_turn_complete(self) -> None:
        """Ordinary Living Archive clears when Nimera completes her next turn."""
        self.records.clear()


def echo_weave_mp_cost(
    record: LivingArchiveRecord,
    *,
    cost_scale: float,
    minimum_mp: int,
) -> int:
    if cost_scale < 0:
        raise ValueError("Echo Weave cost scale cannot be negative")
    if minimum_mp < 1:
        raise ValueError("Echo Weave minimum MP must be positive")
    return max(minimum_mp, round_half_up(record.authored_base_mp * cost_scale))


def materialize_echo_weave(
    record: LivingArchiveRecord,
    *,
    potency: float,
    cost_scale: float,
    minimum_mp: int,
) -> CombatAction:
    """Build Echo Weave using the copier's stats at normal resolution time.

    Callers should record the reproducible authored action package, not
    source-actor-only contextual Trait/temporary bonuses. Direct damage and
    healing potency are scaled after the copied action's ordinary calculation.
    """
    if potency <= 0:
        raise ValueError("Echo Weave potency must be positive")
    mp_cost = echo_weave_mp_cost(
        record,
        cost_scale=cost_scale,
        minimum_mp=minimum_mp,
    )
    action = record.action
    if action.action_kind == "damage":
        return replace(
            action,
            name="Echo Weave",
            mp_cost=mp_cost,
            final_damage_multiplier=action.final_damage_multiplier * potency,
        )
    return replace(
        action,
        name="Echo Weave",
        mp_cost=mp_cost,
        healing_potency=action.healing_potency * potency,
    )


__all__ = [
    "ArchiveCategory",
    "LivingArchiveRecord",
    "LivingArchiveState",
    "echo_weave_mp_cost",
    "materialize_echo_weave",
]
