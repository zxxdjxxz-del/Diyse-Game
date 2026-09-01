from __future__ import annotations

import pytest

from tools.diysim.encounters.story_bosses.hollow_watch_castellan import (
    collect_hollow_watch_source_gaps,
    load_hollow_watch_repo_data,
)
from tools.diysim.sources import SourceGapError, find_repo_root


def test_hollow_watch_reports_all_current_repo_authority_gaps() -> None:
    gaps = collect_hollow_watch_source_gaps()
    assert any("Maevra Linebreaker" in gap for gap in gaps)
    assert any("Fortress Slam" in gap for gap in gaps)
    assert any("Iron Pursuit" in gap for gap in gaps)
    assert any("Wall-Shear Sweep" in gap for gap in gaps)


def test_hollow_watch_refuses_to_use_simulator_fallbacks() -> None:
    with pytest.raises(SourceGapError) as exc_info:
        load_hollow_watch_repo_data()
    message = str(exc_info.value)
    for gap in collect_hollow_watch_source_gaps():
        assert gap in message


def test_hollow_watch_has_no_local_numeric_data_module() -> None:
    root = find_repo_root()
    package = root / "tools" / "diysim" / "encounters" / "story_bosses" / "hollow_watch_castellan"
    assert not (package / "data.py").exists()


def test_simulator_has_no_shadow_content_database() -> None:
    root = find_repo_root()
    assert not (root / "tools" / "diysim" / "content").exists()
