"""Prepared-item decisions for the non-canon S020 true-battle candidate."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from tools.diysim.combat.consumables import ConsumableEffect, PreparedInventory, load_consumable_effect
from tools.diysim.combat.models import CombatUnit

from .policy import WardenPartyActions
from .working_snapshot import load_warden_working_snapshot


@dataclass(frozen=True)
class PreparedItemDecision:
    effect: ConsumableEffect
    target: CombatUnit


def build_warden_prepared_inventory(*, root: Path | None = None) -> PreparedInventory:
    snapshot = load_warden_working_snapshot(root=root)
    # Resolve every named item against current item authority before a run begins.
    for name in snapshot.prepared_consumables:
        load_consumable_effect(name, root=root)
    return PreparedInventory(snapshot.prepared_consumables)


def _first_ko(party: list[CombatUnit]) -> CombatUnit | None:
    return next((unit for unit in party if not unit.alive), None)


def _control_target(party: list[CombatUnit]) -> CombatUnit | None:
    controlled = [unit for unit in party if unit.alive and (unit.has_status("stun") or unit.has_status("staggered"))]
    if not controlled:
        return None
    return min(controlled, key=lambda unit: (0 if unit.has_status("stun") else 1, unit.stable_index))


def _lowest_hp(party: list[CombatUnit]) -> CombatUnit | None:
    conscious = [unit for unit in party if unit.alive]
    if not conscious:
        return None
    return min(conscious, key=lambda unit: (unit.hp / unit.max_hp, unit.stable_index))


def choose_prepared_item(
    actor: CombatUnit,
    party: list[CombatUnit],
    inventory: PreparedInventory,
    actions: WardenPartyActions,
    *,
    root: Path | None = None,
) -> PreparedItemDecision | None:
    """Choose a visible-state Item action before ordinary Ability selection."""
    ko_target = _first_ko(party)
    if ko_target is not None and inventory.available("Rousing Salts"):
        return PreparedItemDecision(load_consumable_effect("Rousing Salts", root=root), ko_target)

    control_target = _control_target(party)
    if control_target is not None and inventory.available("Stability Remedy"):
        # Preserve Ilyra's own cleanse when she can legally solve the problem;
        # another conscious actor can spend the prepared remedy instead.
        if actor.template.name != "Ilyra" or actor.mp < actions.clear_warding.mp_cost:
            return PreparedItemDecision(load_consumable_effect("Stability Remedy", root=root), control_target)

    low = _lowest_hp(party)
    if (
        low is not None
        and low.hp / low.max_hp < 0.30
        and inventory.available("Restorative Salve")
    ):
        if actor.template.name != "Ilyra" or actor.mp < actions.mend.mp_cost:
            return PreparedItemDecision(load_consumable_effect("Restorative Salve", root=root), low)

    ilyra = next((unit for unit in party if unit.alive and unit.template.name == "Ilyra"), None)
    if (
        ilyra is not None
        and ilyra.mp < actions.mend.mp_cost
        and inventory.available("Flow Tonic")
        and any(unit.alive and unit.hp / unit.max_hp < 0.60 for unit in party)
    ):
        return PreparedItemDecision(load_consumable_effect("Flow Tonic", root=root), ilyra)

    return None


__all__ = [
    "PreparedItemDecision",
    "build_warden_prepared_inventory",
    "choose_prepared_item",
]
