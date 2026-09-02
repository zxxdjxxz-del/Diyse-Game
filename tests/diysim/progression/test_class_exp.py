from __future__ import annotations

import pytest

from tools.diysim.progression.class_exp import (
    CexpAllocationSegment,
    ClassCexpState,
    apply_class_cexp,
    cexp_to_next_class_level,
    class_level_from_cexp,
    class_state_at_volition,
    mandatory_base_cexp_at_end_chapter,
    post_volition_cexp_available_at_checkpoint,
    project_class_cexp,
)
from tools.diysim.sources.class_exp import (
    load_campaign_cexp_budgets,
    load_character_starting_cexp,
    load_chapter13_cexp_split,
    load_class_level_thresholds,
)


def test_class_level_thresholds_are_loaded_from_repo_authority() -> None:
    rows = load_class_level_thresholds()
    assert len(rows) == 13
    assert [(row.class_level, row.cumulative_cexp) for row in rows[:5]] == [
        (1, 0),
        (2, 150),
        (3, 350),
        (4, 600),
        (5, 950),
    ]
    assert rows[11].class_level == 12
    assert rows[11].cumulative_cexp == 4_950
    assert rows[11].cexp_to_next == 1_050
    assert rows[12].class_level == 13
    assert rows[12].cumulative_cexp == 6_000
    assert rows[12].cexp_to_next is None


def test_recruitment_starting_cexp_and_handoffs_match_v92() -> None:
    rows = {row.character: row for row in load_character_starting_cexp()}
    assert rows["Cyanis"].starting_base_class_level == 1
    assert rows["Cyanis"].starting_base_cexp == 0
    assert rows["Cyanis"].recruitment_chapter_cexp_after_join == 0
    assert rows["Torren"].starting_base_class_level == 4
    assert rows["Torren"].starting_base_cexp == 600
    assert rows["Torren"].recruitment_chapter_cexp_after_join == 150
    assert rows["Nimera"].recruitment_chapter_cexp_after_join == 300
    assert rows["Vaelira"].starting_base_cexp == 1_800
    assert rows["Vaelira"].recruitment_chapter_cexp_after_join == 500
    assert rows["Seyrik"].starting_base_class_level == 8
    assert rows["Seyrik"].starting_base_cexp == 2_300
    assert rows["Seyrik"].recruitment_chapter_cexp_after_join == 0


def test_campaign_cexp_budgets_cover_all_13_chapters() -> None:
    rows = {row.chapter: row.cexp for row in load_campaign_cexp_budgets()}
    assert rows == {
        1: 350,
        2: 450,
        3: 550,
        4: 650,
        5: 800,
        6: 950,
        7: 1_200,
        8: 1_300,
        9: 1_450,
        10: 1_200,
        11: 1_800,
        12: 1_250,
        13: 1_750,
    }
    assert sum(rows[chapter] for chapter in range(1, 8)) == 4_950
    assert sum(rows[chapter] for chapter in range(8, 14)) == 8_750


def test_chapter13_last_shelter_split_is_source_backed() -> None:
    split = load_chapter13_cexp_split()
    assert split.pre_last_shelter == 1_500
    assert split.post_last_shelter == 250


def test_pre_volition_mandatory_cexp_reproduces_corrected_volition_centers() -> None:
    expected = {
        "Cyanis": 4_950,
        "Ilyra": 4_950,
        "Torren": 5_350,
        "Nimera": 4_500,
        "Vaelira": 5_250,
        "Seyrik": 3_500,
    }
    assert {
        character: mandatory_base_cexp_at_end_chapter(character, 7)
        for character in expected
    } == expected
    assert {
        character: class_state_at_volition(character).base_class_level
        for character in expected
    } == {
        "Cyanis": 12,
        "Ilyra": 12,
        "Torren": 12,
        "Nimera": 11,
        "Vaelira": 12,
        "Seyrik": 10,
    }
    assert all(
        class_state_at_volition(character).subclass_cexp == 0
        for character in expected
    )


def test_pre_volition_helper_respects_recruitment_chapter_handoffs() -> None:
    assert mandatory_base_cexp_at_end_chapter("Cyanis", 1) == 350
    assert mandatory_base_cexp_at_end_chapter("Torren", 1) == 750
    assert mandatory_base_cexp_at_end_chapter("Nimera", 3) == 900
    assert mandatory_base_cexp_at_end_chapter("Vaelira", 4) == 2_300
    assert mandatory_base_cexp_at_end_chapter("Seyrik", 6) == 2_300
    with pytest.raises(ValueError, match="not recruited"):
        mandatory_base_cexp_at_end_chapter("Seyrik", 5)
    with pytest.raises(ValueError, match="Chapters 0–7 only"):
        mandatory_base_cexp_at_end_chapter("Cyanis", 8)


def test_post_volition_available_cexp_reports_stream_without_allocating_it() -> None:
    assert post_volition_cexp_available_at_checkpoint("end_ch7") == 0
    assert post_volition_cexp_available_at_checkpoint("end_ch8") == 1_300
    assert post_volition_cexp_available_at_checkpoint("end_ch11") == 5_750
    assert post_volition_cexp_available_at_checkpoint("end_ch12") == 7_000
    assert post_volition_cexp_available_at_checkpoint("ch13_start") == 7_000
    assert post_volition_cexp_available_at_checkpoint("ch13_last_shelter") == 8_500
    assert post_volition_cexp_available_at_checkpoint("ch13_ending") == 8_750
    assert post_volition_cexp_available_at_checkpoint("end_ch13") == 8_750


@pytest.mark.parametrize(
    ("cexp", "expected_level", "to_next"),
    [
        (0, 1, 150),
        (149, 1, 1),
        (150, 2, 200),
        (599, 3, 1),
        (600, 4, 350),
        (4_950, 12, 1_050),
        (5_999, 12, 1),
        (6_000, 13, 0),
    ],
)
def test_class_level_math_uses_exact_live_thresholds(
    cexp: int,
    expected_level: int,
    to_next: int,
) -> None:
    assert class_level_from_cexp(cexp) == expected_level
    assert cexp_to_next_class_level(cexp) == to_next


def test_class_cexp_rejects_out_of_range_totals() -> None:
    with pytest.raises(ValueError, match="between 0 and 6000"):
        class_level_from_cexp(-1)
    with pytest.raises(ValueError, match="between 0 and 6000"):
        class_level_from_cexp(6_001)
    with pytest.raises(ValueError, match="base_cexp"):
        ClassCexpState(base_cexp=6_001)


def test_award_goes_only_to_selected_track() -> None:
    start = ClassCexpState(base_cexp=4_950, subclass_cexp=0)
    result = apply_class_cexp(start, 500, "subclass")
    assert result.applied_cexp == 500
    assert result.lost_cexp == 0
    assert result.after.base_cexp == 4_950
    assert result.after.subclass_cexp == 500
    assert result.after.base_class_level == 12
    assert result.after.subclass_class_level == 3


def test_cexp_above_selected_class_cap_is_lost_not_spilled() -> None:
    start = ClassCexpState(base_cexp=5_900, subclass_cexp=1_000)
    result = apply_class_cexp(start, 500, "base")
    assert result.applied_cexp == 100
    assert result.lost_cexp == 400
    assert result.after.base_cexp == 6_000
    assert result.after.subclass_cexp == 1_000


def test_explicit_allocation_projection_can_switch_tracks_without_hidden_policy() -> None:
    start = ClassCexpState(base_cexp=4_950, subclass_cexp=0)
    projection = project_class_cexp(
        start,
        [
            CexpAllocationSegment("finish base", 1_050, "base"),
            CexpAllocationSegment("begin subclass", 1_300, "subclass"),
        ],
    )
    assert projection.checkpoints[0].state == ClassCexpState(
        base_cexp=6_000,
        subclass_cexp=0,
    )
    assert projection.final == ClassCexpState(
        base_cexp=6_000,
        subclass_cexp=1_300,
    )
    assert projection.total_requested_cexp == 2_350
    assert projection.total_applied_cexp == 2_350
    assert projection.total_lost_cexp == 0


def test_projection_records_loss_if_user_keeps_feeding_a_capped_track() -> None:
    projection = project_class_cexp(
        ClassCexpState(base_cexp=6_000, subclass_cexp=0),
        [CexpAllocationSegment("wasted package", 450, "base")],
    )
    assert projection.final == ClassCexpState(base_cexp=6_000, subclass_cexp=0)
    assert projection.total_applied_cexp == 0
    assert projection.total_lost_cexp == 450
