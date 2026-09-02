from __future__ import annotations

import pytest

from tools.diysim.progression.class_exp import ClassCexpState
from tools.diysim.progression.legacy_projects import (
    LegacyProjectEvidence,
    LegacyProjectProof,
    validate_native_legacy_item_at_checkpoint,
)


def _proof(character: str, item: str, *, gate_b: bool = True) -> LegacyProjectProof:
    states = {
        "Cyanis": ClassCexpState(base_cexp=6_000, subclass_cexp=5_950),
        "Vaelira": ClassCexpState(base_cexp=6_000, subclass_cexp=6_000),
    }
    return LegacyProjectProof(
        class_state=states[character],
        evidence=LegacyProjectEvidence(
            character_quest_complete=True,
            precursor_owned=True,
            gate_a_owned=True,
            gate_b_owned=gate_b,
            kessara_project_available=True,
            completed_items=frozenset({item}),
        ),
    )


def test_native_legacy_weapon_can_be_proven_at_end_ch12_without_gate_b() -> None:
    proof = _proof("Cyanis", "Move or I Move You.", gate_b=False)
    row = validate_native_legacy_item_at_checkpoint(
        "Cyanis", "Move or I Move You.", "end_ch12", proof
    )
    assert row.is_weapon
    assert not row.gate_b_required


def test_nonweapon_legacy_requires_gate_b() -> None:
    proof = _proof("Cyanis", "That Didn't Do Shit.", gate_b=False)
    with pytest.raises(ValueError, match="requires native Legacy Gate B"):
        validate_native_legacy_item_at_checkpoint(
            "Cyanis", "That Didn't Do Shit.", "end_ch12", proof
        )


def test_legacy_availability_is_not_treated_as_completed_item() -> None:
    proof = LegacyProjectProof(
        class_state=ClassCexpState(base_cexp=6_000, subclass_cexp=5_950),
        evidence=LegacyProjectEvidence(
            character_quest_complete=True,
            precursor_owned=True,
            gate_a_owned=True,
            gate_b_owned=True,
            kessara_project_available=True,
        ),
    )
    with pytest.raises(ValueError, match="not explicitly proven forged/completed"):
        validate_native_legacy_item_at_checkpoint(
            "Cyanis", "Move or I Move You.", "end_ch12", proof
        )


def test_legacy_project_requires_native_base_cl13() -> None:
    proof = LegacyProjectProof(
        class_state=ClassCexpState(base_cexp=5_900, subclass_cexp=6_000),
        evidence=LegacyProjectEvidence(
            character_quest_complete=True,
            precursor_owned=True,
            gate_a_owned=True,
            gate_b_owned=True,
            kessara_project_available=True,
            completed_items=frozenset({"Move or I Move You."}),
        ),
    )
    with pytest.raises(ValueError, match="native Base Class CL13"):
        validate_native_legacy_item_at_checkpoint(
            "Cyanis", "Move or I Move You.", "end_ch12", proof
        )


def test_earlier_project_completion_is_blocked_until_kessara_opening_is_authored() -> None:
    # end_ch11 has enough CEXP for Cyanis Base CL13, but the exact Kessara Legacy-service
    # opening chapter is not published, so DiySim must not backfill it.
    proof = LegacyProjectProof(
        class_state=ClassCexpState(base_cexp=6_000, subclass_cexp=4_700),
        evidence=LegacyProjectEvidence(
            character_quest_complete=True,
            precursor_owned=True,
            gate_a_owned=True,
            gate_b_owned=True,
            kessara_project_available=True,
            completed_items=frozenset({"Move or I Move You."}),
        ),
    )
    with pytest.raises(ValueError, match="does not prove Kessara's exact Legacy-project opening"):
        validate_native_legacy_item_at_checkpoint(
            "Cyanis", "Move or I Move You.", "end_ch11", proof
        )


def test_project_validation_ends_after_last_shelter() -> None:
    proof = LegacyProjectProof(
        class_state=ClassCexpState(base_cexp=6_000, subclass_cexp=6_000),
        evidence=LegacyProjectEvidence(
            character_quest_complete=True,
            precursor_owned=True,
            gate_a_owned=True,
            gate_b_owned=True,
            kessara_project_available=True,
            completed_items=frozenset({"Move or I Move You."}),
        ),
    )
    with pytest.raises(ValueError, match="validation ends at Last Shelter"):
        validate_native_legacy_item_at_checkpoint(
            "Cyanis", "Move or I Move You.", "ch13_ending", proof
        )
