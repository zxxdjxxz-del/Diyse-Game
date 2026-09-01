"""Consume-on-use functional analogue copy mechanics.

This is intentionally separate from bounded replay: analogue actions replace
source element/secondary mechanics, collapse multihits, and clear their stored
record after use.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, cast

from ..sources.analogues import FunctionalAnalogueRuleSource
from .models import CombatAction, DamageKind, Element
from .replay import RecordedDamageSignature, ReplayCommandCategory, record_completed_damage_action

_ANALOGUE_ELIGIBLE_CATEGORIES = frozenset({"attack", "ability"})


@dataclass(frozen=True)
class FunctionalAnalogueRule:
    single_power: int
    aoe_power: int
    base_hit: int
    physical_element: Element
    magical_element: Element
    hybrid_element: Element
    hybrid_physical_weight: float
    hybrid_magical_weight: float

    @classmethod
    def from_source(cls, source: FunctionalAnalogueRuleSource) -> "FunctionalAnalogueRule":
        if not source.complete:
            raise ValueError("incomplete functional analogue source")
        assert source.single_power is not None
        assert source.aoe_power is not None
        assert source.base_hit is not None
        assert source.physical_element is not None
        assert source.magical_element is not None
        assert source.hybrid_element is not None
        assert source.hybrid_physical_weight is not None
        assert source.hybrid_magical_weight is not None
        return cls(
            single_power=source.single_power,
            aoe_power=source.aoe_power,
            base_hit=source.base_hit,
            physical_element=cast(Element, source.physical_element),
            magical_element=cast(Element, source.magical_element),
            hybrid_element=cast(Element, source.hybrid_element),
            hybrid_physical_weight=source.hybrid_physical_weight,
            hybrid_magical_weight=source.hybrid_magical_weight,
        )


def analogue_category_eligible(category: ReplayCommandCategory, action: CombatAction) -> bool:
    return category in _ANALOGUE_ELIGIBLE_CATEGORIES and action.action_kind == "damage"


def record_completed_analogue_source(
    action: CombatAction,
    *,
    category: ReplayCommandCategory,
    hit_powers: Iterable[float] | None = None,
) -> RecordedDamageSignature | None:
    if not analogue_category_eligible(category, action):
        return None
    return record_completed_damage_action(action, category=category, hit_powers=hit_powers)


def transform_functional_analogue(
    recorded: RecordedDamageSignature,
    rule: FunctionalAnalogueRule,
    *,
    name: str = "Recorded Analogue",
) -> CombatAction:
    power = rule.single_power if recorded.target_scope == "one" else rule.aoe_power

    damage_kind: DamageKind = recorded.damage_kind
    physical_weight = None
    magical_weight = None
    if damage_kind == "physical":
        element = rule.physical_element
    elif damage_kind == "magical":
        element = rule.magical_element
    else:
        element = rule.hybrid_element
        physical_weight = rule.hybrid_physical_weight
        magical_weight = rule.hybrid_magical_weight

    return CombatAction(
        name=name,
        target_side="enemy",
        target_scope=recorded.target_scope,
        damage_kind=damage_kind,
        element=element,
        power=power,
        base_hit=rule.base_hit,
        physical_weight=physical_weight,
        magical_weight=magical_weight,
        defense_penetration=0.0,
        spirit_penetration=0.0,
        status_riders=(),
        temporary_modifiers=(),
    )


@dataclass
class FunctionalAnalogueState:
    name: str
    rule: FunctionalAnalogueRule
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
        candidate = record_completed_analogue_source(
            action,
            category=category,
            hit_powers=hit_powers,
        )
        if candidate is None:
            return False
        self.recorded = candidate
        return True

    def materialize(self) -> CombatAction | None:
        if self.recorded is None:
            return None
        return transform_functional_analogue(self.recorded, self.rule, name=self.name)

    def consume(self) -> CombatAction | None:
        action = self.materialize()
        if action is not None:
            self.recorded = None
        return action


__all__ = [
    "FunctionalAnalogueRule",
    "FunctionalAnalogueState",
    "analogue_category_eligible",
    "record_completed_analogue_source",
    "transform_functional_analogue",
]
