from __future__ import annotations

import pytest

from tools.diysim.sources import RepoSourceError, find_repo_root, read_repo_text
from tools.diysim.sources.combat import load_combat_rules
from tools.diysim.sources.progression import STAT_KEYS, load_progression_rules


def test_progression_source_is_self_consistent() -> None:
    rules = load_progression_rules()
    assert rules.level_cap == max(rules.cumulative_exp)
    assert min(rules.cumulative_exp) == 1
    assert all(key in rules.natural_coefficients for key in STAT_KEYS)
    assert rules.class_multipliers
    assert all(set(package) == set(STAT_KEYS) for package in rules.class_multipliers.values())


def test_combat_source_is_self_consistent() -> None:
    rules = load_combat_rules()
    assert rules.min_hit_chance < rules.max_hit_chance
    assert 0 < rules.base_crit_chance <= rules.crit_chance_cap
    assert rules.crit_multiplier > 1
    assert 0 <= rules.penetration_cap <= 1
    assert rules.affinity_damage_multipliers
    assert rules.linked_statuses
    assert rules.status_chance_min < rules.status_chance_max
    assert rules.bleed_escalation_turns > 0


def test_repo_reader_rejects_paths_outside_repo() -> None:
    root = find_repo_root()
    with pytest.raises(RepoSourceError):
        read_repo_text("../outside.md", root=root)
