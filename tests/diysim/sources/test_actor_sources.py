from __future__ import annotations

import pytest

from tools.diysim.sources.actors import (
    find_enemy_registry_entries,
    load_enemy_registry,
    parse_stat_row,
)
from tools.diysim.sources.repo import SourceGapError


def test_stat_source_preserves_absent_fields_as_absent() -> None:
    source = parse_stat_row({"HP": "120", "ATK": "55", "DEF": "20", "Spirit": "18", "SPD": "24"})

    assert source.values == {
        "hp": 120,
        "attack": 55,
        "defense": 20,
        "spirit": 18,
        "speed": 24,
    }
    assert not source.has("mp")
    assert not source.has("magic")


def test_stat_source_requires_explicit_fields_without_zero_fill() -> None:
    source = parse_stat_row({"HP": "100", "DEF": "22", "Spirit": "28"})

    with pytest.raises(SourceGapError, match="speed"):
        source.require("hp", "defense", "spirit", "speed")


def test_enemy_registry_is_read_from_current_repo_register() -> None:
    registry = load_enemy_registry()
    assert registry

    first = registry[0]
    matches = find_enemy_registry_entries(first.identity)
    assert first in matches
