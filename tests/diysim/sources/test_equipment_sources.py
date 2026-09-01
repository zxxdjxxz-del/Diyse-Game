from __future__ import annotations

from tools.diysim.sources import combine_equipment_bonuses, load_equipment


def test_equipment_source_reads_current_ordinary_register_values() -> None:
    dunmere = load_equipment("Dunmere Steel")
    assert dunmere.layer == "Ordinary"
    assert dunmere.equipment_type == "Sword"
    assert dunmere.stat_bonuses == {"attack": 42, "magic": 32}

    shield = load_equipment("Yahtrean Shield")
    assert shield.stat_bonuses == {"defense": 15, "spirit": 10}

    focus = load_equipment("Warding Focus")
    assert focus.stat_bonuses == {"magic": 9, "spirit": 19}


def test_equipment_source_preserves_speed_and_persistent_special_stats() -> None:
    tower = load_equipment("Tower Shield")
    assert tower.stat_bonuses == {"defense": 24, "spirit": 7, "speed": -3}

    legacy = load_equipment("That Was Dumb.")
    assert legacy.stat_bonuses == {"defense": 30, "spirit": 28}
    assert legacy.status_resistance_bonus == 12

    hp_legacy = load_equipment("That Didn't Do Shit.")
    assert hp_legacy.stat_bonuses["hp"] == 400


def test_equipment_loadout_combines_current_v105_warden_gear() -> None:
    cyanis, eva, sr = combine_equipment_bonuses(
        ("Dunmere Steel", "Crest Plate", "Yahtrean Shield")
    )
    assert cyanis == {"attack": 42, "magic": 32, "defense": 43, "spirit": 31}
    assert eva == 0
    assert sr == 0

    ilyra, eva, sr = combine_equipment_bonuses(
        ("Blue Wardrod", "Blue Warden Mail", "Warding Focus")
    )
    assert ilyra == {"attack": 33, "magic": 43, "defense": 18, "spirit": 41}
    assert eva == 0
    assert sr == 0
