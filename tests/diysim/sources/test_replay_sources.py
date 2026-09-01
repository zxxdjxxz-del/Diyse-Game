from __future__ import annotations

import pytest

from tools.diysim.sources.markdown import extract_heading_block
from tools.diysim.sources.replays import parse_bounded_replay_rule_text
from tools.diysim.sources.repo import read_repo_text


@pytest.mark.parametrize(
    ("path", "heading", "scale", "minimum", "maximum"),
    (
        ("docs/09_ENEMIES_AND_ENCOUNTERS/ORDINARY_ENEMIES/MEMORY_SCRIBE.md", "Recorded Echo", 0.65, 80, 180),
        ("docs/09_ENEMIES_AND_ENCOUNTERS/ORDINARY_ENEMIES/ROLE_ECHO.md", "Replayed Role", 0.70, 100, 220),
        ("docs/09_ENEMIES_AND_ENCOUNTERS/ORDINARY_ENEMIES/DEVOURING_ECHO.md", "Devoured Replay", 0.75, 120, 260),
        ("docs/09_ENEMIES_AND_ENCOUNTERS/ORDINARY_ENEMIES/CALAMITY_MEMORY.md", "Calamity Replay", 0.85, 140, 300),
        ("docs/09_ENEMIES_AND_ENCOUNTERS/ELITES/ARCHIVE_DUPLICANT.md", "Deep Duplicate", 0.80, 110, 240),
    ),
)
def test_current_bounded_replay_owners_parse_to_one_complete_contract(
    path: str,
    heading: str,
    scale: float,
    minimum: int,
    maximum: int,
) -> None:
    text = read_repo_text(path)
    block = extract_heading_block(text, heading)
    source = parse_bounded_replay_rule_text(heading, block)

    assert source.complete
    assert source.power_scale == scale
    assert source.min_total_power == minimum
    assert source.max_total_power == maximum
    assert source.base_hit == 100
    assert source.record_after_completion
    assert source.preserve_damage_identity
    assert source.preserve_target_scope
    assert source.preserve_weights
    assert source.preserve_hit_count
    assert source.use_copier_stats
    assert source.strips_secondary_mechanics
