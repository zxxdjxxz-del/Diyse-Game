from __future__ import annotations

from tools.diysim.sources.entities import parse_entity_stat_sources
from tools.diysim.sources.repo import read_repo_text


def _entities(path: str):
    return parse_entity_stat_sources(read_repo_text(path))


def test_explicit_no_turn_support_is_classified_passive_without_filling_stats() -> None:
    text = """# Synthetic Support

| Object | HP | DEF | Spirit | EVA | SR |
|---|---:|---:|---:|---:|---:|
| Anchor | 100 | 20 | 18 | 0 | 5 |

The Anchor takes no independent ordinary turn and deals no direct damage.
"""
    entity = parse_entity_stat_sources(text)[0]

    assert entity.role == "passive_target"
    assert entity.row_label == "Anchor"
    assert entity.stats.has("hp")
    assert not entity.stats.has("attack")
    assert not entity.stats.has("magic")
    assert not entity.stats.has("speed")


def test_zevraya_reservoir_rows_are_passive_repo_entities() -> None:
    entities = _entities("docs/09_ENEMIES_AND_ENCOUNTERS/SUPPORT_OBJECTS/ZEVRAYA_LIFE_FORCE_RESERVOIRS.md")

    assert len(entities) == 4
    assert {entity.row_label for entity in entities} == {"Sustenance", "Armor", "Brood", "Conduction"}
    assert all(entity.role == "passive_target" for entity in entities)
    assert all(not entity.stats.has("speed") for entity in entities)


def test_chainworks_restraint_anchor_is_passive_while_boss_body_stays_unresolved_or_acting() -> None:
    entities = _entities("docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/CHAINWORKS_BEHEMOTH.md")

    anchor = next(entity for entity in entities if entity.section_heading == "Restraint Anchors")
    boss = entities[0]
    assert anchor.role == "passive_target"
    assert anchor.stats.has("hp")
    assert not anchor.stats.has("speed")
    assert boss.role != "passive_target"


def test_deepforge_functional_assemblies_inherit_explicit_group_no_action_role() -> None:
    entities = _entities("docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/DEEPFORGE_COLOSSUS.md")
    supports = {entity.row_label: entity for entity in entities if entity.row_label in {"Guard Press", "Repair Arm", "Command Loom"}}

    assert set(supports) == {"Guard Press", "Repair Arm", "Command Loom"}
    assert all(entity.role == "passive_target" for entity in supports.values())
    assert all(entity.role_evidence for entity in supports.values())
    assert entities[0].role != "passive_target"


def test_furnace_coolant_valve_is_passive_but_servitor_remains_acting_or_unresolved() -> None:
    entities = _entities("docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/FURNACE_TYRANT.md")
    valve = next(entity for entity in entities if entity.section_heading == "COOLANT VALVES")
    servitor = next(entity for entity in entities if entity.section_heading == "FINITE FURNACE SERVITORS")

    assert valve.role == "passive_target"
    assert servitor.role != "passive_target"


def test_varkesh_retreat_beacons_use_explicit_group_no_turn_rule_without_affecting_black_guard() -> None:
    entities = _entities("docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/MARSHAL_VARKESH_FINAL_CAPTURE.md")
    east = next(entity for entity in entities if entity.section_heading == "East Retreat Beacon")
    west = next(entity for entity in entities if entity.section_heading == "West Retreat Beacon")
    guard = next(entity for entity in entities if entity.section_heading == "Varkesh Black Guard")

    assert east.role == "passive_target"
    assert west.role == "passive_target"
    assert guard.role == "acting_combatant"


def test_custodian_child_support_tables_inherit_parent_neither_takes_turn_rule() -> None:
    entities = _entities("docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/THE_CUSTODIAN.md")
    node = next(entity for entity in entities if entity.section_heading == "Perception Node")
    seal = next(entity for entity in entities if entity.section_heading == "Ruin Containment Seal")

    assert node.role == "passive_target"
    assert seal.role == "passive_target"


def test_hollow_watch_fortress_ballista_is_not_misclassified_as_passive() -> None:
    entities = _entities("docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/HOLLOW_WATCH_CASTELLAN.md")
    ballista = next(entity for entity in entities if entity.section_heading == "Fortress Ballista")

    assert ballista.role != "passive_target"
