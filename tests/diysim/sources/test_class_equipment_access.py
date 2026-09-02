from __future__ import annotations

from tools.diysim.sources.class_equipment_access import (
    load_character_donor_equipment_access,
    load_donor_equipment_access,
)


def test_reciprocal_donor_pairs_cover_all_six_permanent_characters() -> None:
    rows = {row.character: row for row in load_donor_equipment_access()}
    assert set(rows) == {"Cyanis", "Ilyra", "Torren", "Nimera", "Vaelira", "Seyrik"}
    assert rows["Cyanis"].donor_character == "Vaelira"
    assert rows["Vaelira"].donor_character == "Cyanis"
    assert rows["Ilyra"].donor_character == "Seyrik"
    assert rows["Seyrik"].donor_character == "Ilyra"
    assert rows["Torren"].donor_character == "Nimera"
    assert rows["Nimera"].donor_character == "Torren"


def test_donor_equipment_milestones_match_current_class_system_authority() -> None:
    row = load_character_donor_equipment_access("Cyanis")
    assert row.primary_class_level == 1
    assert row.armor_class_level == 3
    assert row.secondary_class_level == 5
    assert row.relic_class_level == 7
    assert row.legacy_class_level == 11
    assert row.required_class_level("weapon") == 1
    assert row.required_class_level("armor") == 3
    assert row.required_class_level("secondary") == 5
    assert row.required_class_level("relic") == 7
    assert row.required_class_level("legacy") == 11
