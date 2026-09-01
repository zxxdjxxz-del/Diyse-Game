from __future__ import annotations

import random

from tools.diysim.encounters.generic_enemy_runtime import build_generic_enemy_runtime
from tools.diysim.encounters.runtime_catalog import (
    audit_enemy_runtime_coverage,
    build_enemy_runtime_catalog,
)
from tools.diysim.overlays import BalanceOverlay


def _definition(filename: str):
    return next(
        item for item in build_enemy_runtime_catalog()
        if item.source_path.endswith("/" + filename)
    )


def test_enemy_runtime_catalog_classifies_every_discovered_owner_sheet():
    report = audit_enemy_runtime_coverage()
    assert report.total_owner_sheets > 100
    assert report.enemy_sheets > 100
    assert report.unclassified == 0
    assert report.special >= 3
    assert report.generic > 0
    assert report.components > 0
    for definition in report.definitions:
        assert definition.kind in {"generic", "special", "component", "blocked"}
        if definition.kind in {"blocked", "component"}:
            assert definition.blockers


def test_archive_current_is_generic_and_uses_shared_pressure_overlay():
    definition = _definition("ARCHIVE_CURRENT.md")
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
    definition = _definition("ARCHIVE_CURRENT.md")
    runtime = build_generic_enemy_runtime(definition)
    rng = random.Random(1)
    action = runtime.select_action(1, rng)
    assert action in runtime.legal_actions(1)
    runtime.commit_action(action, 1)
    duration = runtime.repetition_locks.get(action.name)
    if duration:
        assert action not in runtime.legal_actions(1)


def test_non_damage_and_triggered_behavior_is_not_silently_dropped():
    definition = _definition("FURNACE_SERVITOR.md")
    assert definition.kind == "blocked"
    joined = "\n".join(definition.blockers)
    assert "Feed Furnace: non-damage effect requires runtime handler" in joined
    assert "Overheat Vent: triggered/passive action requires runtime trigger" in joined
    assert "no explicit Power-bearing action blocks detected" not in joined


def test_reuse_body_is_not_misclassified_as_an_action():
    definition = _definition("BLACK_HOST_CROSSBOWMAN.md")
    assert definition.kind == "generic"
    assert not any("Chapter-0 body:" in blocker for blocker in definition.blockers)
    assert [action.source.name for action in definition.actions] == ["Crossbow Bolt", "Aimed Bolt"]


def test_real_effect_action_survives_reuse_section_filtering():
    definition = _definition("ARCHIVE_SCRIBE_ENGINE.md")
    assert definition.kind == "blocked"
    joined = "\n".join(definition.blockers)
    assert "Record Stabilization: non-damage effect requires runtime handler" in joined
    assert "Chapter-10 Eastern Wayfinder body:" not in joined
    assert [action.source.name for action in definition.actions] == [
        "Scribe Beam", "Index Burst", "Record Stabilization"
    ]


def test_support_files_are_components_not_false_enemy_failures():
    definition = _definition("ZEVRAYA_LIFE_FORCE_RESERVOIRS.md")
    assert definition.kind == "component"
