from __future__ import annotations

import random

from tools.diysim.combat.action_resolution import resolve_effect
from tools.diysim.combat.derived_stats import effective_base_hit_bonus if False else effective_defense, effective_spirit
from tools.diysim.combat.models import CombatUnit
from tools.diysim.combat.temporary_modifiers import effective_base_hit_bonus
from tools.diysim.encounters.formation_catalog import load_formation_definitions
from tools.diysim.encounters.formation_runtime import FormationActionSelection, build_formation_runtime
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


def _action(definition, name: str):
    return next(action for action in definition.combatant.actions if action.name == name)


def test_enemy_runtime_catalog_classifies_every_discovered_owner_sheet():
    report = audit_enemy_runtime_coverage()
    assert report.total_owner_sheets > 100
    assert report.enemy_sheets > 100
    assert report.unclassified == 0
    assert report.special >= 3
    assert report.generic > 40
    assert report.formation > 0
    assert report.components > 0
    for definition in report.definitions:
        assert definition.kind in {"generic", "formation", "special", "component", "blocked"}
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
        if action.action_kind == "damage":
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


def test_total_defense_effect_is_executable_and_uses_percent_canon():
    definition = _definition("BOGSHELL.md")
    assert definition.kind == "generic"
    assert definition.combatant is not None
    guard = _action(definition, "Shell Guard")
    assert guard.action_kind == "effect"
    assert guard.target_side == "self"
    assert guard.temporary_modifiers[0].defense_percent == 15
    assert guard.temporary_modifiers[0].spirit_percent == 15
    assert guard.temporary_modifiers[0].duration_rounds == 2

    unit = CombatUnit(definition.combatant, 0)
    resolve_effect(unit, guard, unit)
    assert effective_defense(unit) == 36
    assert effective_spirit(unit) == 25


def test_explicit_defense_spirit_effect_survives_reuse_section_filtering():
    definition = _definition("ARCHIVE_SCRIBE_ENGINE.md")
    assert definition.kind == "generic"
    assert definition.combatant is not None
    assert [action.source.name for action in definition.actions] == [
        "Scribe Beam", "Index Burst", "Record Stabilization"
    ]
    stabilization = _action(definition, "Record Stabilization")
    assert stabilization.action_kind == "effect"
    modifier = stabilization.temporary_modifiers[0]
    assert modifier.defense_percent == 10
    assert modifier.spirit_percent == 10
    assert modifier.duration_rounds == 2


def test_preparation_forces_named_follow_up_and_is_once_per_battle():
    definition = _definition("CONVOY_WAR_SORCERER.md")
    assert definition.kind == "generic"
    runtime = build_generic_enemy_runtime(definition)
    round_one_names = {action.name for action in runtime.legal_actions(1)}
    assert "Rift Lance Preparation" not in round_one_names
    assert "Rift Lance" not in round_one_names
    prep = next(action for action in runtime.legal_actions(2) if action.name == "Rift Lance Preparation")
    runtime.commit_action(prep, 2)
    assert [action.name for action in runtime.legal_actions(3)] == ["Rift Lance"]
    runtime.commit_action(runtime.legal_actions(3)[0], 3)
    later_names = {action.name for action in runtime.legal_actions(4)}
    assert "Rift Lance Preparation" not in later_names
    assert "Rift Lance" not in later_names
    assert {"War-Sorcery Bolt", "Shard Volley"}.issubset(later_names)


def test_reload_is_only_legal_when_forced_by_barbed_bolt():
    definition = _definition("BASTION_CROSSBOW_GUARD.md")
    assert definition.kind == "generic"
    runtime = build_generic_enemy_runtime(definition)
    assert "Reload" not in {action.name for action in runtime.legal_actions(1)}
    barbed = next(action for action in runtime.legal_actions(1) if action.name == "Barbed Bolt")
    runtime.commit_action(barbed, 1)
    assert [action.name for action in runtime.legal_actions(2)] == ["Reload"]
    runtime.commit_action(runtime.legal_actions(2)[0], 2)
    assert "Reload" not in {action.name for action in runtime.legal_actions(3)}


def test_chapter3_command_screen_builds_from_formation_authority():
    formations = load_formation_definitions(
        "docs/09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_03_FORMATIONS.md"
    )
    command_screen = next(item for item in formations if item.name == "Command Screen")
    assert command_screen.runtime_ready
    assert [(member.count, member.enemy.name) for member in command_screen.members] == [
        (2, "Command-Station Sentry"),
        (1, "Authority Lens"),
        (2, "Command Ring Drone"),
    ]
    runtime = build_formation_runtime(command_screen)
    assert len(runtime.enemies) == 5
    assert all("construct" in enemy.unit.template.runtime_tags for enemy in runtime.enemies)


def test_authority_lens_targeting_focus_is_formation_executable():
    definition = _definition("AUTHORITY_LENS.md")
    assert definition.kind == "formation"
    assert definition.combatant is not None
    assert "construct" in definition.combatant.runtime_tags
    focus_def = next(item for item in definition.actions if item.source.name == "Targeting Focus")
    assert focus_def.formation_required
    assert focus_def.target_tags == ("construct",)
    assert focus_def.exclude_actor
    assert focus_def.fallback_action == "Authority Ray"

    formations = load_formation_definitions(
        "docs/09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_03_FORMATIONS.md"
    )
    runtime = build_formation_runtime(next(item for item in formations if item.name == "Command Screen"))
    lens_index = next(i for i, enemy in enumerate(runtime.enemies) if enemy.unit.template.name == "Authority Lens")
    eligible = runtime.eligible_allies(lens_index, focus_def)
    assert lens_index not in eligible
    assert len(eligible) == 4

    target_index = eligible[0]
    focus = _action(definition, "Targeting Focus")
    selection = FormationActionSelection(lens_index, focus, (target_index,), "Targeting Focus")
    assert effective_base_hit_bonus(runtime.enemies[target_index].unit) == 0
    runtime.resolve_ally_effect(selection)
    assert effective_base_hit_bonus(runtime.enemies[target_index].unit) == 10


def test_command_ring_drone_relay_is_formation_executable():
    definition = _definition("COMMAND_RING_DRONE.md")
    assert definition.kind == "formation"
    relay_def = next(item for item in definition.actions if item.source.name == "Command Relay")
    assert relay_def.target_tags == ("construct",)
    assert relay_def.exclude_actor
    assert relay_def.fallback_action == "Ring Bolt"


def test_non_damage_and_triggered_behavior_is_not_silently_dropped():
    definition = _definition("FURNACE_SERVITOR.md")
    assert definition.kind == "blocked"
    joined = "\n".join(definition.blockers)
    assert "Feed Furnace: effect target/effect depends on encounter relationship" in joined
    assert "Overheat Vent: triggered/passive action requires runtime trigger" in joined
    assert "no explicit Power-bearing action blocks detected" not in joined


def test_reuse_body_is_not_misclassified_as_an_action():
    definition = _definition("BLACK_HOST_CROSSBOWMAN.md")
    assert definition.kind == "generic"
    assert not any("Chapter-0 body:" in blocker for blocker in definition.blockers)
    assert [action.source.name for action in definition.actions] == ["Crossbow Bolt", "Aimed Bolt"]


def test_support_files_are_components_not_false_enemy_failures():
    definition = _definition("ZEVRAYA_LIFE_FORCE_RESERVOIRS.md")
    assert definition.kind == "component"
