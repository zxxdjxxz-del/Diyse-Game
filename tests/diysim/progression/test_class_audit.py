from __future__ import annotations

import pytest

from tools.diysim.progression.class_audit import (
    audit_campaign_class_aware_named_checkpoint,
    audit_character_class_aware_named_checkpoint,
)
from tools.diysim.progression.class_exp import ClassCexpState


def _gap_codes(row) -> set[str]:
    return {gap.code for gap in row.source_gaps}


def test_class_aware_named_audit_can_use_validated_full_donor_ordinary_loadout() -> None:
    row = audit_character_class_aware_named_checkpoint(
        "Cyanis",
        "end_ch8",
        "mandatory",
        selected_class="Crest Arcanist",
        equipment_choices={
            "weapon": "Veycross Battlestaff",
            "armor": "Arcanist Weave",
            "secondary": "Swift Focus",
        },
        class_state=ClassCexpState(base_cexp=5_300, subclass_cexp=950),
    )
    assert row.checkpoint == "End Ch8"
    assert row.class_name == "Crest Arcanist"
    assert row.class_selection_explicit
    assert row.weapon == "Veycross Battlestaff"
    assert row.armor == "Arcanist Weave"
    assert row.secondary == "Swift Focus"
    assert row.explicit_equipment_slots == ("weapon", "armor", "secondary")
    assert row.stats is not None
    assert row.authority_complete
    assert not row.source_gaps


def test_class_aware_named_audit_keeps_legacy_behavior_without_class_state() -> None:
    with pytest.raises(ValueError, match="not native ordinary weapon equipment for Cyanis"):
        audit_character_class_aware_named_checkpoint(
            "Cyanis",
            "end_ch8",
            equipment_choices={"weapon": "Arcanist Staff"},
        )


def test_class_state_is_rejected_on_nonmandatory_route_until_optional_cexp_is_modeled() -> None:
    with pytest.raises(ValueError, match="mandatory route only"):
        audit_character_class_aware_named_checkpoint(
            "Cyanis",
            "end_ch8",
            "best_available",
            equipment_choices={"weapon": "Arcanist Staff"},
            class_state=ClassCexpState(base_cexp=6_000, subclass_cexp=250),
        )


def test_campaign_class_aware_named_audit_accepts_multiple_character_states() -> None:
    rows = {
        row.character: row
        for row in audit_campaign_class_aware_named_checkpoint(
            "end_ch8",
            class_choices={
                "Cyanis": "Crest Arcanist",
                "Ilyra": "Vowblade",
            },
            class_states={
                "Cyanis": ClassCexpState(base_cexp=5_300, subclass_cexp=950),
                "Ilyra": ClassCexpState(base_cexp=5_300, subclass_cexp=950),
            },
        )
    }
    assert rows["Cyanis"].class_name == "Crest Arcanist"
    assert rows["Ilyra"].class_name == "Vowblade"
    assert "selected_class_route_missing" not in _gap_codes(rows["Cyanis"])
    assert "selected_class_route_missing" in _gap_codes(rows["Torren"])


def test_campaign_class_state_rejects_unknown_character() -> None:
    with pytest.raises(ValueError, match="Unknown permanent character in class-state choices: Fake"):
        audit_campaign_class_aware_named_checkpoint(
            "end_ch8",
            class_states={"Fake": ClassCexpState()},
        )


def test_campaign_class_state_rejects_known_future_recruit() -> None:
    with pytest.raises(ValueError, match="not recruited by End Ch5: Seyrik"):
        audit_campaign_class_aware_named_checkpoint(
            "end_ch5",
            class_states={"Seyrik": ClassCexpState(base_cexp=2_300, subclass_cexp=0)},
        )
