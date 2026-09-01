from __future__ import annotations

from tools.diysim.sources.entities import parse_entity_stat_sources
from tools.diysim.sources.repo import read_repo_text


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
    entities = parse_entity_stat_sources(
        read_repo_text("docs/09_ENEMIES_AND_ENCOUNTERS/SUPPORT_OBJECTS/ZEVRAYA_LIFE_FORCE_RESERVOIRS.md")
    )

    assert len(entities) == 4
    assert {entity.row_label for entity in entities} == {"Sustenance", "Armor", "Brood", "Conduction"}
    assert all(entity.role == "passive_target" for entity in entities)
    assert all(not entity.stats.has("speed") for entity in entities)


def test_chainworks_restraint_anchor_is_passive_while_boss_body_stays_unresolved_or_acting() -> None:
    entities = parse_entity_stat_sources(
        read_repo_text("docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/CHAINWORKS_BEHEMOTH.md")
    )

    anchor = next(entity for entity in entities if entity.section_heading == "Restraint Anchors")
    boss = entities[0]
    assert anchor.role == "passive_target"
    assert anchor.stats.has("hp")
    assert not anchor.stats.has("speed")
    assert boss.role != "passive_target"
