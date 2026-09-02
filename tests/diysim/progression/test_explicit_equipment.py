from __future__ import annotations

import json

import pytest

from tools.diysim.cli import main
from tools.diysim.progression.audit import audit_character_checkpoint
from tools.diysim.progression.loadouts import resolve_loadout


def _gap_codes(row) -> set[str]:
    return {gap.code for gap in row.source_gaps}


def test_full_explicit_cyanis_loadout_resolves_mandatory_ownership_gap() -> None:
    row = resolve_loadout(
        "Cyanis",
        5,
        "mandatory",
        equipment_choices={
            "weapon": "Deepforge Blade",
            "armor": "Crestguard Plate",
            "secondary": "War Shield",
        },
    )
    assert row.weapon == "Deepforge Blade"
    assert row.armor == "Crestguard Plate"
    assert row.secondary == "War Shield"
    assert row.explicit_slots == ("weapon", "armor", "secondary")
    assert row.slots_complete
    assert not row.source_gaps


def test_partial_explicit_best_available_only_clears_that_slot_gap() -> None:
    row = resolve_loadout(
        "Cyanis",
        5,
        "best_available",
        equipment_choices={"armor": "Crestguard Plate"},
    )
    assert row.weapon == "Deepforge Blade"
    assert row.armor == "Crestguard Plate"
    assert row.secondary == "Yahtrean Shield"
    assert row.explicit_slots == ("armor",)
    assert "armor_availability_timing_missing" not in _gap_codes(row)
    assert "secondary_availability_timing_missing" in _gap_codes(row)


def test_two_slot_native_weapon_needs_only_explicit_weapon_and_armor() -> None:
    row = resolve_loadout(
        "Torren",
        3,
        "mandatory",
        equipment_choices={
            "weapon": "Command War Bow",
            "armor": "Campaign Mail",
        },
    )
    assert row.weapon == "Command War Bow"
    assert row.armor == "Campaign Mail"
    assert row.secondary is None
    assert row.secondary_consumed_by_weapon
    assert row.explicit_slots == ("weapon", "armor")
    assert row.slots_complete
    assert not row.source_gaps


def test_ilyra_native_shield_secondary_is_source_proven() -> None:
    row = resolve_loadout(
        "Ilyra",
        4,
        "mandatory",
        equipment_choices={
            "weapon": "Crucible Wardrod",
            "armor": "High Warden Mail",
            "secondary": "Tower Shield",
        },
    )
    assert row.secondary == "Tower Shield"
    assert row.slots_complete
    assert not row.source_gaps


def test_vaelira_native_focus_secondary_is_source_proven() -> None:
    row = resolve_loadout(
        "Vaelira",
        4,
        "mandatory",
        equipment_choices={
            "weapon": "Arcanist Staff",
            "armor": "Arcanist Weave",
            "secondary": "Swift Focus",
        },
    )
    assert row.weapon == "Arcanist Staff"
    assert row.secondary == "Swift Focus"
    assert row.slots_complete
    assert not row.source_gaps


def test_explicit_weapon_still_obeys_known_first_availability() -> None:
    with pytest.raises(ValueError, match="Deepforge Blade is first available in Chapter 5"):
        resolve_loadout(
            "Cyanis",
            4,
            "mandatory",
            equipment_choices={"weapon": "Deepforge Blade"},
        )


def test_explicit_weapon_rejects_another_characters_native_item() -> None:
    with pytest.raises(ValueError, match="not native ordinary weapon equipment for Cyanis"):
        resolve_loadout(
            "Cyanis",
            6,
            "mandatory",
            equipment_choices={"weapon": "Fieldbreaker"},
        )


def test_explicit_item_rejects_wrong_slot() -> None:
    with pytest.raises(ValueError, match="occupies armor, not requested slot weapon"):
        resolve_loadout(
            "Cyanis",
            5,
            equipment_choices={"weapon": "Crestguard Plate"},
        )


def test_explicit_progression_equipment_rejects_relic_layer() -> None:
    with pytest.raises(ValueError, match="supports Ordinary gear only"):
        resolve_loadout(
            "Cyanis",
            7,
            equipment_choices={"weapon": "First Measure"},
        )


def test_unproven_native_secondary_access_is_not_inferred() -> None:
    with pytest.raises(ValueError, match="does not prove native Focus Secondary access for Nimera"):
        resolve_loadout(
            "Nimera",
            7,
            equipment_choices={"secondary": "Swift Focus"},
        )


def test_audit_marks_explicit_equipment_and_calculates_stats() -> None:
    row = audit_character_checkpoint(
        "Cyanis",
        5,
        "mandatory",
        equipment_choices={
            "weapon": "Deepforge Blade",
            "armor": "Crestguard Plate",
            "secondary": "War Shield",
        },
    )
    assert row.stats is not None
    assert row.explicit_equipment_slots == ("weapon", "armor", "secondary")
    payload = row.as_dict()
    assert payload["Equipment Selection"] == "Explicit: weapon, armor, secondary"
    assert payload["ATK"] == row.stats.attack
    assert payload["SPR"] == row.stats.spirit


def test_cli_accepts_repeatable_equipment_choices(capsys) -> None:
    exit_code = main([
        "progression-audit",
        "--chapter",
        "5",
        "--character",
        "Cyanis",
        "--equipment-choice",
        "Cyanis:weapon=Deepforge Blade",
        "--equipment-choice",
        "Cyanis:armor=Crestguard Plate",
        "--equipment-choice",
        "Cyanis:secondary=War Shield",
        "--format",
        "json",
    ])
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert payload[0]["Weapon"] == "Deepforge Blade"
    assert payload[0]["Armor"] == "Crestguard Plate"
    assert payload[0]["Secondary"] == "War Shield"
    assert payload[0]["Equipment Selection"] == "Explicit: weapon, armor, secondary"
    assert "later_mandatory_loadout_map_missing" not in payload[0]["Source Gaps"]


def test_cli_rejects_duplicate_equipment_slot() -> None:
    with pytest.raises(SystemExit, match="duplicate --equipment-choice for Cyanis:weapon"):
        main([
            "progression-audit",
            "--chapter",
            "5",
            "--equipment-choice",
            "Cyanis:weapon=Crestblade",
            "--equipment-choice",
            "Cyanis:weapon=Deepforge Blade",
        ])


def test_cli_rejects_unknown_equipment_choice_character() -> None:
    with pytest.raises(SystemExit, match="Unknown permanent character in equipment choices: Fake"):
        main([
            "progression-audit",
            "--chapter",
            "5",
            "--equipment-choice",
            "Fake:weapon=Crestblade",
        ])
