"""Element/affinity rules backed by repository authority."""
from __future__ import annotations

from ..sources.combat import load_combat_rules
from .models import Affinity, CombatUnit, Element, StatusName


def affinity_damage_multiplier(affinity: Affinity) -> float:
    return load_combat_rules().affinity_damage_multipliers[affinity]


def linked_status_affinity_modifier(element: Element, status: StatusName, affinity: Affinity) -> int | None:
    rules = load_combat_rules()
    if rules.linked_statuses.get(element) != status:
        return 0
    return rules.linked_status_affinity_modifiers[affinity]


def element_affinity(unit: CombatUnit, element: Element) -> Affinity:
    if element in ("neutral", "colorless"):
        return "neutral"
    return unit.template.elemental_affinities.get(element, "neutral")


__all__ = ["affinity_damage_multiplier", "element_affinity", "linked_status_affinity_modifier"]
