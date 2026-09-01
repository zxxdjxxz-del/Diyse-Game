"""Runtime for authored multihit commands that use current and next cycle elements."""
from __future__ import annotations

from dataclasses import dataclass
import random

from .action_resolution import resolve_damage, roll_status
from .models import CombatAction, CombatUnit, DamageKind, Element, StatusRider, TargetScope

STANDARD_ELEMENT_CYCLE: tuple[Element, ...] = ("fire", "ice", "lightning", "earth")
_LINKED_STATUS = {
    "fire": "burn",
    "ice": "freeze",
    "lightning": "stun",
    "earth": "staggered",
}


@dataclass(frozen=True)
class ResolvedDynamicHitPackage:
    name: str
    target_scope: TargetScope
    damage_kind: DamageKind
    hits: tuple[CombatAction, ...]
    max_new_harmful_statuses: int


def next_cycle_element(current: Element, cycle: tuple[Element, ...] = STANDARD_ELEMENT_CYCLE) -> Element:
    if current not in cycle:
        raise ValueError(f"element {current!r} is not in the authored cycle")
    return cycle[(cycle.index(current) + 1) % len(cycle)]


def build_current_next_hit_package(
    *,
    name: str,
    target_scope: TargetScope,
    damage_kind: DamageKind,
    current_element: Element,
    per_hit_powers: tuple[int, int],
    base_hit: int,
    linked_status_chance: int,
    max_new_harmful_statuses: int = 1,
    cycle: tuple[Element, ...] = STANDARD_ELEMENT_CYCLE,
) -> ResolvedDynamicHitPackage:
    elements = (current_element, next_cycle_element(current_element, cycle))
    hits = tuple(
        CombatAction(
            name=f"{name} — hit {index}",
            target_scope=target_scope,
            damage_kind=damage_kind,
            element=element,
            power=power,
            base_hit=base_hit,
        )
        for index, (element, power) in enumerate(zip(elements, per_hit_powers), start=1)
    )
    return ResolvedDynamicHitPackage(
        name=name,
        target_scope=target_scope,
        damage_kind=damage_kind,
        hits=hits,
        max_new_harmful_statuses=max_new_harmful_statuses,
    )


def resolve_dynamic_hit_package(
    actor: CombatUnit,
    package: ResolvedDynamicHitPackage,
    target: CombatUnit,
    rng: random.Random,
    *,
    linked_status_chance: int,
) -> tuple[int, ...]:
    """Resolve hits in order while enforcing the command-wide new-status cap."""
    damages: list[int] = []
    statuses_added = 0
    for hit in package.hits:
        damage = resolve_damage(actor, hit, target, rng)
        damages.append(damage)
        if damage <= 0 or not target.alive or statuses_added >= package.max_new_harmful_statuses:
            continue
        status = _LINKED_STATUS.get(hit.element)
        if status is None:
            continue
        rider = StatusRider(status=status, base_chance=float(linked_status_chance))
        if roll_status(hit, rider, target, rng):
            statuses_added += 1
    return tuple(damages)


__all__ = [
    "ResolvedDynamicHitPackage",
    "STANDARD_ELEMENT_CYCLE",
    "build_current_next_hit_package",
    "next_cycle_element",
    "resolve_dynamic_hit_package",
]
