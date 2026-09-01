"""Prepared-item decisions for the non-canon Zevraya true-battle candidate."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from tools.diysim.combat.consumables import ConsumableEffect, PreparedInventory, load_consumable_effect
from tools.diysim.combat.models import CombatUnit

from .policy import ZevrayaPartyActions
from .working_snapshot import load_zevraya_working_snapshot


@dataclass(frozen=True)
class PreparedItemDecision:
    effect: ConsumableEffect
    target: CombatUnit


def build_zevraya_prepared_inventory(*, root: Path | None = None) -> PreparedInventory:
    snapshot = load_zevraya_working_snapshot(root=root)
    for name in snapshot.prepared_consumables:
        load_consumable_effect(name, root=root)
    return PreparedInventory(snapshot.prepared_consumables)


def _first_ko(party: list[CombatUnit]) -> CombatUnit | None:
    return next((unit for unit in party if not unit.alive), None)


def _lowest_hp(party: list[CombatUnit]) -> CombatUnit | None:
    living = [unit for unit in party if unit.alive]
    return min(living, key=lambda unit: (unit.hp / unit.max_hp, unit.stable_index)) if living else None


def _control_target(party: list[CombatUnit]) -> CombatUnit | None:
    controlled = [
        unit for unit in party
        if unit.alive and (unit.has_status("freeze") or unit.has_status("stun") or unit.has_status("staggered"))
    ]
    if not controlled:
        return None
    return min(
        controlled,
        key=lambda unit: (0 if unit.has_status("freeze") else 1 if unit.has_status("stun") else 2, unit.stable_index),
    )


def _bleed_target(party: list[CombatUnit]) -> CombatUnit | None:
    bleeding = [unit for unit in party if unit.alive and unit.has_status("bleed")]
    if not bleeding:
        return None
    return min(bleeding, key=lambda unit: (unit.hp / unit.max_hp, unit.stable_index))


def choose_prepared_item(
    actor: CombatUnit,
    party: list[CombatUnit],
    inventory: PreparedInventory,
    actions: ZevrayaPartyActions,
    *,
    root: Path | None = None,
) -> PreparedItemDecision | None:
    ko = _first_ko(party)
    if ko is not None and inventory.available("Rousing Salts"):
        return PreparedItemDecision(load_consumable_effect("Rousing Salts", root=root), ko)

    control = _control_target(party)
    if control is not None and inventory.available("Stability Remedy"):
        if actor.template.name != "Ilyra" or actor.mp < actions.clear_warding.mp_cost:
            return PreparedItemDecision(load_consumable_effect("Stability Remedy", root=root), control)

    bleeding = _bleed_target(party)
    if (
        bleeding is not None
        and bleeding.hp / bleeding.max_hp < 0.60
        and inventory.available("Trauma Remedy")
    ):
        return PreparedItemDecision(load_consumable_effect("Trauma Remedy", root=root), bleeding)

    low = _lowest_hp(party)
    if low is not None and low.hp / low.max_hp < 0.28 and inventory.available("Restorative Salve"):
        if actor.template.name != "Ilyra" or actor.mp < actions.mend.mp_cost:
            return PreparedItemDecision(load_consumable_effect("Restorative Salve", root=root), low)

    ilyra = next((unit for unit in party if unit.alive and unit.template.name == "Ilyra"), None)
    if (
        ilyra is not None
        and ilyra.mp < actions.mend.mp_cost
        and inventory.available("Deepflow Tonic")
        and any(unit.alive and unit.hp / unit.max_hp < 0.68 for unit in party)
    ):
        return PreparedItemDecision(load_consumable_effect("Deepflow Tonic", root=root), ilyra)

    return None


__all__ = [
    "PreparedItemDecision",
    "build_zevraya_prepared_inventory",
    "choose_prepared_item",
]
