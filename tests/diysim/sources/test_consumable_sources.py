from tools.diysim.sources import load_consumable, load_consumable_register


def test_consumable_register_reads_current_twenty_items() -> None:
    entries = load_consumable_register()
    assert len(entries) == 20
    restorative = load_consumable("Restorative Salve")
    assert restorative.item_id == "C02"
    assert restorative.function == "Restore 750 HP to one ally"


def test_chapter_three_warden_consumables_come_from_current_register() -> None:
    assert "50 MP" in load_consumable("Flow Tonic").function
    assert "Freeze / Stun / Staggered" in load_consumable("Stability Remedy").function
    assert "25% Max HP" in load_consumable("Rousing Salts").function
