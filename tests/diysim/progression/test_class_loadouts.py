from __future__ import annotations

import pytest

from tools.diysim.progression.class_exp import ClassCexpState
from tools.diysim.progression.class_loadouts import resolve_class_aware_loadout_at_checkpoint


def _gap_codes(row) -> set[str]:
    return {gap.code for gap in row.source_gaps}


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
    with pytest.raises(ValueError, match="consumes Weapon \+ Secondary"):
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


def test_relic_layer_remains_blocked_even_when_subclass_cl_is_high_enough() -> None:
    with pytest.raises(ValueError, match="supports Ordinary gear only"):
        resolve_class_aware_loadout_at_checkpoint(
            "Cyanis",
            "end_ch11",
            equipment_choices={"weapon": "One Bright Law"},
            class_state=ClassCexpState(base_cexp=6_000, subclass_cexp=4_700),
        )
