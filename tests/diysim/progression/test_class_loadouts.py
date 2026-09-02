from __future__ import annotations

import pytest

from tools.diysim.progression.class_exp import ClassCexpState
from tools.diysim.progression.class_loadouts import resolve_class_aware_loadout_at_checkpoint
from tools.diysim.progression.legacy_projects import LegacyProjectEvidence, LegacyProjectProof


def _gap_codes(row) -> set[str]:
    return {gap.code for gap in row.source_gaps}


def _legacy_proof(
    state: ClassCexpState,
    item: str,
    *,
    gate_b: bool = True,
) -> LegacyProjectProof:
    return LegacyProjectProof(
        class_state=state,
        evidence=LegacyProjectEvidence(
            character_quest_complete=True,
            precursor_owned=True,
            gate_a_owned=True,
            gate_b_owned=gate_b,
            kessara_project_available=True,
            completed_items=frozenset({item}),
        ),
    )


def test_fresh_subclass_cl1_opens_reciprocal_donor_primary_at_volition() -> None:
    row = resolve_class_aware_loadout_at_checkpoint(
        "Cyanis",
        "end_ch7",
        equipment_choices={"weapon": "Arcanist Staff"},
        class_state=ClassCexpState(base_cexp=4_950, subclass_cexp=0),
    )
    assert row.weapon == "Arcanist Staff"
    assert row.explicit_slots == ("weapon",)


def test_donor_armor_requires_subclass_cl3() -> None:
    with pytest.raises(ValueError, match="requires donor armor access at Subclass CL3"):
        resolve_class_aware_loadout_at_checkpoint(
            "Cyanis",
            "end_ch8",
            equipment_choices={"armor": "Arcanist Weave"},
            class_state=ClassCexpState(base_cexp=6_000, subclass_cexp=150),
        )


def test_subclass_cl3_opens_reciprocal_donor_armor() -> None:
    row = resolve_class_aware_loadout_at_checkpoint(
        "Cyanis",
        "end_ch8",
        equipment_choices={"armor": "Arcanist Weave"},
        class_state=ClassCexpState(base_cexp=5_900, subclass_cexp=350),
    )
    assert row.armor == "Arcanist Weave"
    assert "armor_availability_timing_missing" not in _gap_codes(row)


def test_subclass_cl5_opens_reciprocal_donor_secondary_family() -> None:
    row = resolve_class_aware_loadout_at_checkpoint(
        "Cyanis",
        "end_ch8",
        equipment_choices={"secondary": "Swift Focus"},
        class_state=ClassCexpState(base_cexp=5_300, subclass_cexp=950),
    )
    assert row.secondary == "Swift Focus"
    assert row.explicit_slots == ("secondary",)


def test_full_donor_ordinary_loadout_can_clear_mandatory_loadout_gap_at_cl5() -> None:
    row = resolve_class_aware_loadout_at_checkpoint(
        "Cyanis",
        "end_ch8",
        equipment_choices={
            "weapon": "Veycross Battlestaff",
            "armor": "Arcanist Weave",
            "secondary": "Swift Focus",
        },
        class_state=ClassCexpState(base_cexp=5_300, subclass_cexp=950),
    )
    assert row.weapon == "Veycross Battlestaff"
    assert row.armor == "Arcanist Weave"
    assert row.secondary == "Swift Focus"
    assert row.explicit_slots == ("weapon", "armor", "secondary")
    assert row.slots_complete
    assert not row.source_gaps


def test_donor_weapon_still_obeys_item_availability_timing() -> None:
    with pytest.raises(ValueError, match="Fieldbreaker is first available in Chapter 8"):
        resolve_class_aware_loadout_at_checkpoint(
            "Ilyra",
            "end_ch7",
            equipment_choices={"weapon": "Fieldbreaker"},
            class_state=ClassCexpState(base_cexp=4_950, subclass_cexp=0),
        )


def test_two_slot_donor_primary_consumes_secondary() -> None:
    row = resolve_class_aware_loadout_at_checkpoint(
        "Ilyra",
        "end_ch7",
        equipment_choices={"weapon": "Ruin Vanguard Sword"},
        class_state=ClassCexpState(base_cexp=4_950, subclass_cexp=0),
    )
    assert row.weapon == "Ruin Vanguard Sword"
    assert row.secondary is None
    assert row.secondary_consumed_by_weapon


def test_two_slot_donor_primary_rejects_explicit_secondary() -> None:
    with pytest.raises(ValueError, match=r"consumes Weapon \+ Secondary"):
        resolve_class_aware_loadout_at_checkpoint(
            "Ilyra",
            "end_ch7",
            equipment_choices={
                "weapon": "Ruin Vanguard Sword",
                "secondary": "Tower Shield",
            },
            class_state=ClassCexpState(base_cexp=4_950, subclass_cexp=0),
        )


def test_unproven_donor_secondary_family_is_not_inferred() -> None:
    with pytest.raises(ValueError, match="does not prove Focus as the reciprocal donor Secondary family"):
        resolve_class_aware_loadout_at_checkpoint(
            "Torren",
            "end_ch8",
            equipment_choices={"secondary": "Swift Focus"},
            class_state=ClassCexpState(base_cexp=5_700, subclass_cexp=950),
        )


def test_without_class_state_existing_native_only_rejection_is_preserved() -> None:
    with pytest.raises(ValueError, match="not native ordinary weapon equipment for Cyanis"):
        resolve_class_aware_loadout_at_checkpoint(
            "Cyanis",
            "end_ch7",
            equipment_choices={"weapon": "Arcanist Staff"},
        )


def test_impossible_class_state_is_rejected_before_donor_access() -> None:
    with pytest.raises(ValueError, match="only 1300 mandatory CEXP"):
        resolve_class_aware_loadout_at_checkpoint(
            "Cyanis",
            "end_ch8",
            equipment_choices={"weapon": "Arcanist Staff"},
            class_state=ClassCexpState(base_cexp=6_000, subclass_cexp=1_000),
        )


def test_native_relic_can_be_assumed_owned_after_its_first_acquisition_chapter() -> None:
    row = resolve_class_aware_loadout_at_checkpoint(
        "Cyanis",
        "end_ch7",
        equipment_choices={"weapon": "First Measure"},
        class_state=ClassCexpState(base_cexp=4_950, subclass_cexp=0),
    )
    assert row.weapon == "First Measure"
    assert row.explicit_slots == ("weapon",)


def test_donor_relic_requires_subclass_cl7_equipment_mastery() -> None:
    with pytest.raises(ValueError, match="requires donor Relic eligibility at Subclass CL7"):
        resolve_class_aware_loadout_at_checkpoint(
            "Cyanis",
            "end_ch9",
            equipment_choices={"weapon": "Turning Prism"},
            class_state=ClassCexpState(base_cexp=6_000, subclass_cexp=1_700),
        )


def test_subclass_cl7_can_use_assumed_owned_reciprocal_donor_relic() -> None:
    row = resolve_class_aware_loadout_at_checkpoint(
        "Cyanis",
        "end_ch9",
        equipment_choices={"weapon": "Turning Prism"},
        class_state=ClassCexpState(base_cexp=5_900, subclass_cexp=1_800),
    )
    assert row.weapon == "Turning Prism"
    assert row.explicit_slots == ("weapon",)


def test_donor_relic_still_obeys_first_acquisition_chapter() -> None:
    with pytest.raises(ValueError, match="One Bright Law is first obtainable in Chapter 11"):
        resolve_class_aware_loadout_at_checkpoint(
            "Cyanis",
            "end_ch9",
            equipment_choices={"weapon": "One Bright Law"},
            class_state=ClassCexpState(base_cexp=5_900, subclass_cexp=1_800),
        )


def test_native_relic_great_bow_preserves_two_slot_commitment() -> None:
    row = resolve_class_aware_loadout_at_checkpoint(
        "Torren",
        "end_ch7",
        equipment_choices={"weapon": "Falling Compass"},
        class_state=ClassCexpState(base_cexp=5_350, subclass_cexp=0),
    )
    assert row.weapon == "Falling Compass"
    assert row.secondary is None
    assert row.secondary_consumed_by_weapon


def test_shared_relic_secondary_access_is_not_inferred() -> None:
    with pytest.raises(ValueError, match="shared Relic Secondary"):
        resolve_class_aware_loadout_at_checkpoint(
            "Cyanis",
            "end_ch9",
            equipment_choices={"secondary": "One Breath Ahead"},
            class_state=ClassCexpState(base_cexp=5_900, subclass_cexp=1_800),
        )


def test_legacy_choice_still_rejects_without_explicit_project_proof() -> None:
    with pytest.raises(ValueError, match="requires explicit Legacy project proof"):
        resolve_class_aware_loadout_at_checkpoint(
            "Cyanis",
            "end_ch12",
            equipment_choices={"weapon": "Move or I Move You."},
            class_state=ClassCexpState(base_cexp=6_000, subclass_cexp=5_950),
        )


def test_native_completed_legacy_can_be_equipped_at_end_ch12() -> None:
    state = ClassCexpState(base_cexp=6_000, subclass_cexp=5_950)
    row = resolve_class_aware_loadout_at_checkpoint(
        "Cyanis",
        "end_ch12",
        equipment_choices={"weapon": "Move or I Move You."},
        class_state=state,
        legacy_project_proofs={
            "Cyanis": _legacy_proof(state, "Move or I Move You.", gate_b=False)
        },
    )
    assert row.weapon == "Move or I Move You."
    assert row.explicit_slots == ("weapon",)


def test_donor_completed_legacy_requires_subclass_cl11() -> None:
    receiver_state = ClassCexpState(base_cexp=6_000, subclass_cexp=3_450)
    donor_state = ClassCexpState(base_cexp=6_000, subclass_cexp=6_000)
    with pytest.raises(ValueError, match="requires donor Legacy eligibility at Subclass CL11"):
        resolve_class_aware_loadout_at_checkpoint(
            "Cyanis",
            "end_ch12",
            equipment_choices={"weapon": "There's Your Problem."},
            class_state=receiver_state,
            legacy_project_proofs={
                "Vaelira": _legacy_proof(donor_state, "There's Your Problem.", gate_b=False)
            },
        )


def test_subclass_cl11_can_equip_actual_completed_reciprocal_donor_legacy() -> None:
    receiver_state = ClassCexpState(base_cexp=6_000, subclass_cexp=5_950)
    donor_state = ClassCexpState(base_cexp=6_000, subclass_cexp=6_000)
    row = resolve_class_aware_loadout_at_checkpoint(
        "Cyanis",
        "end_ch12",
        equipment_choices={"weapon": "There's Your Problem."},
        class_state=receiver_state,
        legacy_project_proofs={
            "Vaelira": _legacy_proof(donor_state, "There's Your Problem.", gate_b=False)
        },
    )
    assert row.weapon == "There's Your Problem."


def test_native_legacy_great_bow_preserves_two_slot_commitment() -> None:
    state = ClassCexpState(base_cexp=6_000, subclass_cexp=6_000)
    row = resolve_class_aware_loadout_at_checkpoint(
        "Torren",
        "end_ch12",
        equipment_choices={"weapon": "Should've Moved."},
        class_state=state,
        legacy_project_proofs={
            "Torren": _legacy_proof(state, "Should've Moved.", gate_b=False)
        },
    )
    assert row.weapon == "Should've Moved."
    assert row.secondary is None
    assert row.secondary_consumed_by_weapon
