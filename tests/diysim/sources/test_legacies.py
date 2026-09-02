from __future__ import annotations

from collections import Counter

from tools.diysim.sources.equipment import load_equipment
from tools.diysim.sources.legacies import (
    load_character_donor_legacy_access,
    load_character_legacy_package,
    load_donor_legacy_access,
    load_legacy_item,
    load_legacy_items,
    load_legacy_project_rules,
)


def test_legacy_master_register_covers_all_17_items() -> None:
    rows = load_legacy_items()
    assert len(rows) == 17
    assert Counter(row.character for row in rows) == {
        "Cyanis": 3,
        "Ilyra": 4,
        "Torren": 2,
        "Nimera": 3,
        "Vaelira": 3,
        "Seyrik": 2,
    }
    assert len({row.legacy.casefold() for row in rows}) == 17


def test_legacy_items_cross_resolve_to_equipment_register_owner_and_layer() -> None:
    for row in load_legacy_items():
        item = load_equipment(row.legacy)
        assert item.layer == "Legacy"
        assert item.owner == row.character


def test_legacy_package_lookup_and_handedness_are_source_backed() -> None:
    torren = load_character_legacy_package("Torren")
    assert {row.legacy for row in torren} == {
        "Should've Moved.",
        "Figured You'd Come This Way.",
    }
    assert load_legacy_item("Should've Moved.").consumes_secondary
    assert load_legacy_item("Good Fuck, Definitely. Good Fuck.").consumes_secondary
    assert load_legacy_item("You Are Finished.").consumes_secondary
    assert not load_legacy_item("There's Your Problem.").consumes_secondary


def test_donor_legacy_access_matches_all_six_reciprocal_pairs() -> None:
    rows = load_donor_legacy_access()
    assert len(rows) == 6
    assert {row.receiver: row.donor for row in rows} == {
        "Cyanis": "Vaelira",
        "Ilyra": "Seyrik",
        "Torren": "Nimera",
        "Nimera": "Torren",
        "Vaelira": "Cyanis",
        "Seyrik": "Ilyra",
    }
    assert load_character_donor_legacy_access("Cyanis").donor == "Vaelira"


def test_legacy_project_rules_preserve_completion_and_uniqueness_requirements() -> None:
    rules = load_legacy_project_rules()
    assert rules.native_base_class_level == 13
    assert rules.requires_all_four_core_masteries
    assert rules.requires_character_quest
    assert rules.requires_quest_component
    assert rules.requires_precursor
    assert rules.requires_gate_a
    assert rules.requires_gate_b
    assert rules.requires_kessara
    assert rules.donor_requires_existing_item
    assert rules.unique_not_copied
