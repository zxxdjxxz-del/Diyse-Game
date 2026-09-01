from tools.diysim.combat.consumables import (
    PreparedInventory,
    load_consumable_effect,
    use_consumable,
)
from tools.diysim.combat.models import ActiveStatus, CombatUnit, Combatant
from tools.diysim.progression.stats import Stats


def _unit(name: str = "Test", *, hp: int = 600, mp: int = 80) -> CombatUnit:
    return CombatUnit(
        Combatant(
            name=name,
            side="party",
            stats=Stats(hp=hp, mp=mp, attack=50, magic=50, defense=50, spirit=50, speed=30),
        ),
        0,
    )


def test_prepared_inventory_is_finite() -> None:
    inventory = PreparedInventory({"Restorative Salve": 1})
    assert inventory.available("Restorative Salve")
    inventory.consume("Restorative Salve")
    assert inventory.remaining("Restorative Salve") == 0
    assert inventory.total_used == 1


def test_restorative_and_flow_tonic_restore_without_overcap() -> None:
    unit = _unit()
    unit.hp = 100
    unit.mp = 5
    inventory = PreparedInventory({"Restorative Salve": 1, "Flow Tonic": 1})

    use_consumable(inventory, load_consumable_effect("Restorative Salve"), target=unit)
    assert unit.hp == 600
    use_consumable(inventory, load_consumable_effect("Flow Tonic"), target=unit)
    assert unit.mp == 55


def test_stability_remedy_clears_control_statuses_only() -> None:
    unit = _unit()
    unit.statuses["stun"] = ActiveStatus("stun")
    unit.statuses["staggered"] = ActiveStatus("staggered", remaining_rounds=5)
    unit.statuses["bleed"] = ActiveStatus("bleed")
    inventory = PreparedInventory({"Stability Remedy": 1})

    use_consumable(inventory, load_consumable_effect("Stability Remedy"), target=unit)
    assert "stun" not in unit.statuses
    assert "staggered" not in unit.statuses
    assert "bleed" in unit.statuses


def test_rousing_salts_revive_at_quarter_hp() -> None:
    unit = _unit(hp=604)
    unit.hp = 0
    inventory = PreparedInventory({"Rousing Salts": 1})

    use_consumable(inventory, load_consumable_effect("Rousing Salts"), target=unit)
    assert unit.hp == 151
    assert unit.mp == unit.max_mp
