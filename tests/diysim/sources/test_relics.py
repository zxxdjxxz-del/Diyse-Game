from __future__ import annotations

from collections import Counter

from tools.diysim.sources.relics import (
    load_relic_placement,
    load_relic_placements,
    load_relic_weapon,
    load_relic_weapons,
)


def test_relic_placement_covers_all_36_relics_with_locked_chapter_cadence() -> None:
    rows = load_relic_placements()
    assert len(rows) == 36
    assert Counter(row.chapter for row in rows) == {
        6: 5,
        7: 5,
        8: 5,
        9: 5,
        10: 5,
        11: 5,
        12: 6,
    }


def test_relic_first_acquisition_lookup_preserves_chapter_and_source() -> None:
    first_measure = load_relic_placement("First Measure")
    assert first_measure.chapter == 6
    assert "Weather Crown" in first_measure.acquisition_source
    assert not first_measure.explicitly_guaranteed

    quiet_rebuke = load_relic_placement("Quiet Rebuke")
    assert quiet_rebuke.chapter == 6
    assert quiet_rebuke.explicitly_guaranteed

    one_bright_law = load_relic_placement("One Bright Law")
    assert one_bright_law.chapter == 11

    after_the_wound = load_relic_placement("After the Wound")
    assert after_the_wound.chapter == 12


def test_relic_weapon_family_table_covers_all_16_surviving_weapons() -> None:
    rows = load_relic_weapons()
    assert len(rows) == 16
    assert Counter(row.character for row in rows) == {
        "Cyanis": 3,
        "Ilyra": 3,
        "Torren": 3,
        "Nimera": 3,
        "Vaelira": 2,
        "Seyrik": 2,
    }


def test_relic_weapon_handedness_follows_explicit_family_rules() -> None:
    assert load_relic_weapon("One Good Line").family == "Great Bow"
    assert load_relic_weapon("One Good Line").consumes_secondary
    assert load_relic_weapon("After the Wound").family == "Two-Handed Sword"
    assert load_relic_weapon("After the Wound").consumes_secondary
    assert load_relic_weapon("Pair of Knives").family == "Conduit"
    assert not load_relic_weapon("Pair of Knives").consumes_secondary
    assert load_relic_weapon("One Bright Law").family == "Arcane Staff"
    assert not load_relic_weapon("One Bright Law").consumes_secondary
