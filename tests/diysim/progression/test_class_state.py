from __future__ import annotations

import pytest

from tools.diysim.progression.class_exp import ClassCexpState
from tools.diysim.progression.class_state import validate_class_state_at_checkpoint


def test_pre_volition_checkpoint_requires_exact_base_only_state() -> None:
    result = validate_class_state_at_checkpoint(
        "Nimera",
        "end_ch4",
        ClassCexpState(base_cexp=1_550, subclass_cexp=0),
    )
    assert result.state.base_cexp == 1_550
    assert result.post_volition_cexp_available == 0
    assert result.post_volition_cexp_lost == 0


@pytest.mark.parametrize(
    ("character", "base_cexp"),
    [
        ("Cyanis", 4_950),
        ("Ilyra", 4_950),
        ("Torren", 5_350),
        ("Nimera", 4_500),
        ("Vaelira", 5_250),
        ("Seyrik", 3_500),
    ],
)
def test_volition_requires_exact_v92_state(character: str, base_cexp: int) -> None:
    result = validate_class_state_at_checkpoint(
        character,
        "end_ch7",
        ClassCexpState(base_cexp=base_cexp, subclass_cexp=0),
    )
    assert result.volition_state == ClassCexpState(base_cexp=base_cexp, subclass_cexp=0)


def test_pre_volition_subclass_cexp_is_rejected() -> None:
    with pytest.raises(ValueError, match="requires Base 4950 / Subclass 0"):
        validate_class_state_at_checkpoint(
            "Cyanis",
            "end_ch7",
            ClassCexpState(base_cexp=4_950, subclass_cexp=1),
        )


def test_post_volition_state_can_allocate_exact_stream_without_hidden_policy() -> None:
    result = validate_class_state_at_checkpoint(
        "Cyanis",
        "end_ch8",
        ClassCexpState(base_cexp=6_000, subclass_cexp=250),
    )
    assert result.post_volition_cexp_available == 1_300
    assert result.post_volition_cexp_applied == 1_300
    assert result.post_volition_cexp_lost == 0
    assert result.exact_no_loss


def test_post_volition_state_can_lose_cexp_only_after_a_track_caps() -> None:
    result = validate_class_state_at_checkpoint(
        "Cyanis",
        "end_ch8",
        ClassCexpState(base_cexp=6_000, subclass_cexp=0),
    )
    assert result.post_volition_cexp_available == 1_300
    assert result.post_volition_cexp_applied == 1_050
    assert result.post_volition_cexp_lost == 250
    assert not result.exact_no_loss


def test_unaccounted_post_volition_cexp_is_rejected_when_neither_track_is_capped() -> None:
    with pytest.raises(ValueError, match="neither Base nor Subclass is at CL13"):
        validate_class_state_at_checkpoint(
            "Cyanis",
            "end_ch8",
            ClassCexpState(base_cexp=5_800, subclass_cexp=200),
        )


def test_state_requiring_more_cexp_than_checkpoint_has_is_rejected() -> None:
    with pytest.raises(ValueError, match="only 1300 mandatory CEXP"):
        validate_class_state_at_checkpoint(
            "Cyanis",
            "end_ch8",
            ClassCexpState(base_cexp=6_000, subclass_cexp=1_000),
        )


def test_base_cexp_cannot_regress_after_volition() -> None:
    with pytest.raises(ValueError, match="Base CEXP regression"):
        validate_class_state_at_checkpoint(
            "Torren",
            "end_ch8",
            ClassCexpState(base_cexp=5_349, subclass_cexp=1_301),
        )


def test_completed_torren_state_by_end_ch12_can_account_for_lost_cexp() -> None:
    result = validate_class_state_at_checkpoint(
        "Torren",
        "end_ch12",
        ClassCexpState(base_cexp=6_000, subclass_cexp=6_000),
    )
    assert result.post_volition_cexp_available == 7_000
    assert result.post_volition_cexp_applied == 6_650
    assert result.post_volition_cexp_lost == 350


def test_seyrik_full_completion_is_exact_at_last_shelter() -> None:
    result = validate_class_state_at_checkpoint(
        "Seyrik",
        "ch13_last_shelter",
        ClassCexpState(base_cexp=6_000, subclass_cexp=6_000),
    )
    assert result.post_volition_cexp_available == 8_500
    assert result.post_volition_cexp_applied == 8_500
    assert result.post_volition_cexp_lost == 0


def test_ending_can_account_for_post_shelter_cexp_as_cap_loss() -> None:
    result = validate_class_state_at_checkpoint(
        "Seyrik",
        "ch13_ending",
        ClassCexpState(base_cexp=6_000, subclass_cexp=6_000),
    )
    assert result.post_volition_cexp_available == 8_750
    assert result.post_volition_cexp_lost == 250


def test_checkpoint_before_recruitment_is_rejected() -> None:
    with pytest.raises(ValueError, match="not recruited"):
        validate_class_state_at_checkpoint(
            "Seyrik",
            "end_ch5",
            ClassCexpState(base_cexp=0, subclass_cexp=0),
        )
