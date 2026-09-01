from __future__ import annotations

import pytest

from tools.diysim.encounters.story_bosses.hollow_watch_castellan import load_hollow_watch_repo_data
from tools.diysim.sources import SourceGapError, find_repo_root


def test_hollow_watch_refuses_to_use_a_simulator_fallback_for_maevra() -> None:
    with pytest.raises(SourceGapError, match="Maevra Linebreaker"):
        load_hollow_watch_repo_data()


def test_hollow_watch_has_no_local_numeric_data_module() -> None:
    root = find_repo_root()
    package = root / "tools" / "diysim" / "encounters" / "story_bosses" / "hollow_watch_castellan"
    assert not (package / "data.py").exists()


def test_simulator_has_no_shadow_content_database() -> None:
    root = find_repo_root()
    assert not (root / "tools" / "diysim" / "content").exists()
