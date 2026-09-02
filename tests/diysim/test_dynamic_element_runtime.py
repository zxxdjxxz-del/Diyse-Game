from __future__ import annotations

import random

from tools.diysim.encounters.formation_catalog import load_formation_definitions
from tools.diysim.encounters.formation_runtime import build_formation_runtime
from tools.diysim.encounters.generic_enemy_runtime import build_generic_enemy_runtime
from tools.diysim.encounters.runtime_catalog import build_enemy_runtime_catalog


def _definition(filename: str):
    return next(
        item for item in build_enemy_runtime_catalog()
        if item.source_path.endswith("/" + filename)
    )


def _action(runtime, name: str, round_number: int):
    return next(action for action in runtime.legal_actions(round_number) if action.name == name)


def test_reaction_node_rolls_one_persistent_assigned_element_and_matching_rider():
    definition = _definition("REACTION_NODE.md")
    assert definition.kind == "generic"
    assert [(spec.source, spec.mode, spec.choices) for spec in definition.dynamic_element_states] == [
        ("assigned_element", "random_once", ("fire", "ice", "lightning", "earth")),
    ]

    runtime = build_generic_enemy_runtime(definition)
    rng = random.Random(7)
    runtime.prepare_round(1, rng)
    assert runtime.dynamic_element_values["assigned_element"] == "lightning"

    pulse = _action(runtime, "Reaction Pulse", 1)
    flash = _action(runtime, "Regulator Flash", 1)
    assert pulse.element == "lightning"
    assert flash.element == "lightning"
    assert [(rider.status, rider.base_chance) for rider in pulse.status_riders] == [("stun", 15)]
    assert flash.status_riders == ()

    runtime.prepare_round(2, rng)
    assert runtime.dynamic_element_values["assigned_element"] == "lightning"
    assert _action(runtime, "Reaction Pulse", 2).element == "lightning"


def test_composite_elemental_cycles_once_by_round_and_resolves_one_matching_rider():
    definition = _definition("COMPOSITE_ELEMENTAL.md")
    assert definition.kind == "generic"
    assert [(spec.source, spec.mode, spec.cycle, spec.initial_element) for spec in definition.dynamic_element_states] == [
        ("current_expression", "round_cycle", ("fire", "ice", "lightning", "earth"), "fire"),
    ]

    runtime = build_generic_enemy_runtime(definition)
    rng = random.Random(3)
    expected = [
        (1, "fire", "burn", 20),
        (2, "ice", "freeze", 20),
        (3, "lightning", "stun", 15),
        (4, "earth", "staggered", 20),
        (5, "fire", "burn", 20),
    ]
    for round_number, element, status, chance in expected:
        runtime.prepare_round(round_number, rng)
        surge = _action(runtime, "Composite Surge", round_number)
        assert surge.element == element
        assert [(rider.status, rider.base_chance) for rider in surge.status_riders] == [(status, chance)]
        # Re-preparing/selecting within the same round must not advance the cycle.
        runtime.prepare_round(round_number, rng)
        assert _action(runtime, "Composite Surge", round_number).element == element


def test_non_crucible_chapter4_formations_become_runtime_ready():
    formations = load_formation_definitions(
        "docs/09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_04_FORMATIONS.md"
    )
    by_name = {formation.name: formation for formation in formations}
    expected_ready = {
        "Annex Probe",
        "Reaction Mesh",
        "Mirror Pack",
        "Composite Screen",
        "Mirror Reaction",
    }
    assert all(by_name[name].runtime_ready for name in expected_ready)
    assert not by_name["Crucible Escort"].runtime_ready
    assert not by_name["Crucible Line"].runtime_ready
    assert not by_name["Guarded Mirror"].runtime_ready
    assert not by_name["Full Annex Pressure"].runtime_ready

    runtime = build_formation_runtime(by_name["Reaction Mesh"], rng=random.Random(11))
    node_states = [
        enemy.runtime.dynamic_element_values["assigned_element"]
        for enemy in runtime.enemies
        if enemy.runtime.combatant.name == "Reaction Node"
    ]
    assert len(node_states) == 2
    assert all(state in {"fire", "ice", "lightning", "earth"} for state in node_states)
