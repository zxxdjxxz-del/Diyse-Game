from __future__ import annotations

import random

from tools.diysim.encounters.generic_enemy_runtime import build_generic_enemy_runtime
from tools.diysim.encounters.runtime_catalog import (
    audit_enemy_runtime_coverage,
    build_enemy_runtime_catalog,
)
from tools.diysim.overlays import BalanceOverlay


def test_enemy_runtime_catalog_classifies_every_discovered_owner_sheet():
    report = audit_enemy_runtime_coverage()
    assert report.total_owner_sheets > 100
    assert report.unclassified == 0
    assert report.special >= 3
    assert report.generic > 0
    for definition in report.definitions:
        assert definition.kind in {"generic", "special", "blocked"}
        if definition.kind == "blocked":
            assert definition.blockers


def test_administrative_sentinel_is_generic_and_uses_shared_boss_pressure_overlay():
    definition = next(
        item for item in build_enemy_runtime_catalog()
        if item.source_path.endswith("/ADMINISTRATIVE_SENTINEL.md")
    )
    assert definition.kind == "generic"
    assert definition.combatant is not None
    owner = definition.combatant
    runtime = build_generic_enemy_runtime(
        definition,
        overlay=BalanceOverlay(
            direct_damage_power_multiplier=1.20,
            offensive_stat_level_offset=5,
        ),
    )
    assert runtime.combatant.stats.attack > owner.stats.attack
    assert runtime.combatant.stats.magic > owner.stats.magic
    assert runtime.combatant.stats.defense == owner.stats.defense
    assert runtime.combatant.stats.spirit == owner.stats.spirit
    owner_powers = {action.name: action.power for action in owner.actions}
    for action in runtime.combatant.actions:
        assert action.power == owner_powers[action.name] * 1.20


def test_generic_runtime_selects_only_legal_actions_and_commits_locks():
    definition = next(
        item for item in build_enemy_runtime_catalog()
        if item.source_path.endswith("/ADMINISTRATIVE_SENTINEL.md")
    )
    runtime = build_generic_enemy_runtime(definition)
    rng = random.Random(1)
    action = runtime.select_action(1, rng)
    assert action in runtime.legal_actions(1)
    runtime.commit_action(action, 1)
    duration = runtime.repetition_locks.get(action.name)
    if duration:
        assert action not in runtime.legal_actions(1)
