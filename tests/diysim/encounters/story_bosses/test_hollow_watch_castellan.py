from __future__ import annotations

import pytest

from tools.diysim.encounters.story_bosses.hollow_watch_castellan import (
    collect_hollow_watch_source_gaps,
    load_hollow_watch_repo_data,
)
from tools.diysim.sources import find_repo_root


def test_hollow_watch_current_repo_authority_is_source_complete() -> None:
    assert collect_hollow_watch_source_gaps() == ()


def test_hollow_watch_loads_current_repo_values_without_fallbacks() -> None:
    data = load_hollow_watch_repo_data()

    assert data.castellan.stats.hp == 450
    assert data.castellan.stats.attack == 42
    assert data.castellan.stats.magic == 27
    assert data.castellan.stats.defense == 27
    assert data.castellan.stats.spirit == 24
    assert data.castellan.stats.speed == 25
    assert data.castellan.evasion == 0
    assert data.castellan.status_resistance == 5

    assert data.ballista.stats.hp == 120
    assert data.ballista.stats.attack == 55
    assert data.ballista.stats.defense == 20
    assert data.ballista.stats.spirit == 18
    assert data.ballista.stats.speed == 24
    assert data.ballista.evasion == 0
    assert data.ballista.status_resistance == 10

    assert data.watch_seal.stats.hp == 100
    assert data.watch_seal.stats.defense == 22
    assert data.watch_seal.stats.spirit == 28
    assert data.watch_seal.evasion == 0
    assert data.watch_seal.status_resistance == 10

    assert data.heavy_bolt.power == 230
    assert data.heavy_bolt.base_hit == 95
    assert data.heavy_bolt.damage_kind == "physical"
    assert data.heavy_bolt.element == "neutral"

    assert data.linebreaker_thrust.power == 165
    assert data.linebreaker_thrust.mp_cost == 10
    assert data.linebreaker_thrust.damage_kind == "physical"
    assert data.linebreaker_thrust.element == "neutral"
    assert data.linebreaker_thrust.defense_penetration == pytest.approx(0.15)

    assert [action.weight for action in data.fortress_actions] == [65, 35]
    assert [action.weight for action in data.walking_actions] == [40, 40, 20]
    assert all(action.damage_kind == "physical" for action in data.walking_actions)
    assert all(action.element == "neutral" for action in data.walking_actions)
    assert data.walking_trigger_hp == 247
    assert data.watch_seal_reduction == pytest.approx(0.10)


def test_hollow_watch_has_no_local_numeric_data_module() -> None:
    root = find_repo_root()
    package = root / "tools" / "diysim" / "encounters" / "story_bosses" / "hollow_watch_castellan"
    assert not (package / "data.py").exists()


def test_simulator_has_no_shadow_content_database() -> None:
    root = find_repo_root()
    assert not (root / "tools" / "diysim" / "content").exists()
