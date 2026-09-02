from __future__ import annotations

import pytest

from tools.diysim.progression.audit import (
    audit_campaign_checkpoint,
    audit_campaign_named_checkpoint,
    audit_character_checkpoint,
    audit_character_named_checkpoint,
)
from tools.diysim.progression.loadouts import resolve_loadout
from tools.diysim.sources.campaign_progression import (
    load_campaign_level_targets,
    load_character_campaign_sources,
)
from tools.diysim.sources.equipment_availability import (
    load_guaranteed_loadouts,
    load_ordinary_weapon_availability,
)


def _gap_codes(row) -> set[str]:
    return {gap.code for gap in row.source_gaps}


def test_guaranteed_loadouts_are_read_from_starting_authority() -> None:
    rows = {row.character: row for row in load_guaranteed_loadouts()}
    assert rows["Cyanis"].equipment_names == (
        "Crestblade",
        "Crest Plate",
        "Yahtrean Shield",
    )
    assert rows["Cyanis"].level == 1
    assert rows["Ilyra"].equipment_names == (
        "Wardrod",
        "Blue Warden Mail",
        "Warding Focus",
    )
    assert rows["Ilyra"].level == 1


def test_ordinary_weapon_first_availability_is_live_repo_data() -> None:
    rows = {row.name: row for row in load_ordinary_weapon_availability()}
    assert len(rows) == 16
    assert rows["Crestblade"].first_chapter == 0
    assert rows["Deepforge Blade"].first_chapter == 5
    assert rows["Fieldbreaker"].first_chapter == 8


def test_campaign_sources_discover_all_six_native_class_pairs() -> None:
    rows = {row.character: row for row in load_character_campaign_sources()}
    assert len(rows) == 6
    assert rows["Cyanis"].selectable_classes == ("Crest Knight", "Crest Arcanist")
    assert rows["Ilyra"].selectable_classes == ("Blue Warden", "Vowblade")
    assert rows["Torren"].selectable_classes == ("War Archer", "Routeweaver")
    assert rows["Nimera"].selectable_classes == ("Cardweaver", "Proofhunter")
    assert rows["Vaelira"].selectable_classes == ("Green Arcanist", "Axiomblade")
    assert rows["Seyrik"].selectable_classes == ("Ruin Vanguard", "Ruin Warden")
    assert rows["Seyrik"].recruitment_chapter == 6


def test_campaign_level_spine_is_loaded_without_reencoding_levels() -> None:
    rows = {row.chapter: row.level for row in load_campaign_level_targets()}
    assert len(rows) == 13
    assert rows[1] == 5
    assert rows[7] == 32
    assert rows[13] == 62


def test_chapter0_cyanis_audit_reproduces_published_body() -> None:
    row = audit_character_checkpoint("Cyanis", 0, "mandatory")
    assert row.authority_complete
    assert row.level == 1
    assert row.class_name == "Crest Knight"
    assert not row.class_selection_explicit
    assert row.stats is not None
    assert (
        row.stats.hp,
        row.stats.mp,
        row.stats.attack,
        row.stats.magic,
        row.stats.defense,
        row.stats.spirit,
        row.stats.speed,
    ) == (231, 25, 56, 45, 61, 47, 21)
    assert row.evasion == 0
    assert row.status_resistance == 0


def test_chapter0_ilyra_audit_reproduces_published_body() -> None:
    row = audit_character_checkpoint("Ilyra", 0, "mandatory")
    assert row.authority_complete
    assert row.stats is not None
    assert (
        row.stats.hp,
        row.stats.mp,
        row.stats.attack,
        row.stats.magic,
        row.stats.defense,
        row.stats.spirit,
        row.stats.speed,
    ) == (220, 31, 45, 59, 34, 59, 22)


def test_later_mandatory_snapshot_keeps_guaranteed_floor_and_reports_gap() -> None:
    row = audit_character_checkpoint("Cyanis", 2, "mandatory")
    assert row.level == 9
    assert row.weapon == "Crestblade"
    assert row.stats is not None
    assert "later_mandatory_loadout_map_missing" in _gap_codes(row)
    assert not row.authority_complete


def test_expected_route_does_not_treat_shop_availability_as_owned() -> None:
    loadout = resolve_loadout("Cyanis", 2, "expected")
    assert loadout.weapon == "Crestblade"
    assert "expected_loadout_policy_missing" in _gap_codes(loadout)


def test_best_available_advances_only_the_chapter_dated_weapon() -> None:
    row = audit_character_checkpoint("Cyanis", 5, "best_available")
    assert row.weapon == "Deepforge Blade"
    assert row.armor == "Crest Plate"
    assert row.secondary == "Yahtrean Shield"
    assert row.stats is not None
    assert "armor_availability_timing_missing" in _gap_codes(row)
    assert "secondary_availability_timing_missing" in _gap_codes(row)
    assert "route_specific_level_target_missing" in _gap_codes(row)


def test_two_handed_best_available_weapon_consumes_secondary_without_guessing_one() -> None:
    row = audit_character_checkpoint("Torren", 3, "best_available")
    assert row.weapon == "Command War Bow"
    assert row.secondary is None
    assert row.secondary_consumed_by_weapon
    assert row.armor is None
    assert row.stats is None
    assert "guaranteed_join_loadout_missing" in _gap_codes(row)
    assert "armor_availability_timing_missing" in _gap_codes(row)
    assert "secondary_availability_timing_missing" not in _gap_codes(row)


def test_campaign_checkpoint_includes_only_recruited_characters() -> None:
    assert [row.character for row in audit_campaign_checkpoint(0)] == ["Cyanis", "Ilyra"]
    assert [row.character for row in audit_campaign_checkpoint(3)] == [
        "Cyanis",
        "Ilyra",
        "Torren",
        "Nimera",
    ]


def test_end_chapter7_audit_marks_selected_class_as_an_assumption_gap() -> None:
    row = audit_character_checkpoint("Cyanis", 7, "mandatory")
    assert row.class_name == "Crest Knight"
    assert not row.class_selection_explicit
    assert "selected_class_route_missing" in _gap_codes(row)


def test_end_chapter7_explicit_native_subclass_resolves_class_choice() -> None:
    row = audit_character_checkpoint(
        "Cyanis",
        7,
        "mandatory",
        selected_class="Crest Arcanist",
    )
    assert row.class_name == "Crest Arcanist"
    assert row.class_selection_explicit
    assert row.stats is not None
    assert "selected_class_route_missing" not in _gap_codes(row)
    assert any(path.endswith("SUBCLASSES/CREST_ARCANIST.md") for path in row.source_paths)
    assert any(path.endswith("CLASS_SYSTEM_MASTER.md") for path in row.source_paths)


def test_end_chapter7_explicit_base_class_is_also_a_resolved_choice() -> None:
    row = audit_character_checkpoint(
        "Cyanis",
        7,
        "mandatory",
        selected_class="Crest Knight",
    )
    assert row.class_name == "Crest Knight"
    assert row.class_selection_explicit
    assert "selected_class_route_missing" not in _gap_codes(row)


def test_subclass_cannot_be_selected_before_sixfold_volition() -> None:
    with pytest.raises(ValueError, match="not usable.*before the Sixfold Volition"):
        audit_character_checkpoint(
            "Cyanis",
            6,
            "mandatory",
            selected_class="Crest Arcanist",
        )


def test_character_cannot_select_another_characters_subclass() -> None:
    with pytest.raises(ValueError, match="not a selectable class for Cyanis"):
        audit_character_checkpoint(
            "Cyanis",
            7,
            "mandatory",
            selected_class="Vowblade",
        )


def test_campaign_checkpoint_accepts_multiple_explicit_class_choices() -> None:
    rows = {
        row.character: row
        for row in audit_campaign_checkpoint(
            7,
            class_choices={
                "Cyanis": "Crest Arcanist",
                "Ilyra": "Vowblade",
            },
        )
    }
    assert rows["Cyanis"].class_name == "Crest Arcanist"
    assert rows["Ilyra"].class_name == "Vowblade"
    assert rows["Cyanis"].class_selection_explicit
    assert rows["Ilyra"].class_selection_explicit
    assert "selected_class_route_missing" not in _gap_codes(rows["Cyanis"])
    assert "selected_class_route_missing" not in _gap_codes(rows["Ilyra"])
    assert "selected_class_route_missing" in _gap_codes(rows["Torren"])


def test_named_checkpoint_uses_exact_chapter13_internal_level() -> None:
    row = audit_character_named_checkpoint("Cyanis", "ch13_start", "mandatory")
    assert row.chapter == 13
    assert row.checkpoint == "start Ch13"
    assert row.level == 57
    assert row.weapon == "Crestblade"
    assert row.stats is not None
    assert "later_mandatory_loadout_map_missing" in _gap_codes(row)
    assert "selected_class_route_missing" in _gap_codes(row)


def test_named_checkpoint_best_available_keeps_source_gaps_visible() -> None:
    row = audit_character_named_checkpoint("Cyanis", "ch13_last_shelter", "best_available")
    assert row.checkpoint == "Last Shelter"
    assert row.level == 60
    assert row.weapon == "Deepforge Blade"
    assert row.stats is not None
    assert "armor_availability_timing_missing" in _gap_codes(row)
    assert "secondary_availability_timing_missing" in _gap_codes(row)
    assert "route_specific_level_target_missing" in _gap_codes(row)


def test_named_campaign_checkpoint_includes_all_six_by_chapter13() -> None:
    rows = audit_campaign_named_checkpoint("ch13_last_shelter")
    assert [row.character for row in rows] == [
        "Cyanis",
        "Ilyra",
        "Torren",
        "Nimera",
        "Vaelira",
        "Seyrik",
    ]
    assert all(row.level == 60 for row in rows)
