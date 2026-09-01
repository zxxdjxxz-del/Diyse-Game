"""Four-element affinity rules and linked-status affinity modifiers."""
from __future__ import annotations

from .models import Affinity, CombatUnit, Element, StatusName

AFFINITY_DAMAGE_MULTIPLIERS = {
    "weak": 1.25,
    "neutral": 1.0,
    "resistant": 0.8,
    "strongly_resistant": 0.6,
    "immune": 0.0,
}

LINKED_STATUS = {
    "fire": "burn",
    "ice": "freeze",
    "lightning": "stun",
    "earth": "staggered",
}


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


def element_affinity(unit: CombatUnit, element: Element) -> Affinity:
    if element in ("neutral", "colorless"):
        return "neutral"
    return unit.template.elemental_affinities.get(element, "neutral")
