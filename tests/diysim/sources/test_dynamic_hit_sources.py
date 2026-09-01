from __future__ import annotations

from tools.diysim.sources.dynamic_hits import parse_dynamic_element_hit_rule_text
from tools.diysim.sources.repo import read_repo_text


def _block(text: str, heading: str) -> str:
    marker = f"### {heading}"
    start = text.index(marker) + len(marker)
    next_heading = text.find("\n### ", start)
    if next_heading == -1:
        next_heading = len(text)
    return text[start:next_heading]


def test_worldscar_confluence_spear_is_complete_dynamic_hit_contract() -> None:
    text = read_repo_text("docs/09_ENEMIES_AND_ENCOUNTERS/MAJOR_HUNTS/MAJOR_HUNT_04.md")
    source = parse_dynamic_element_hit_rule_text(
        "Confluence Spear",
        _block(text, "Confluence Spear"),
        context_text=text,
    )

    assert source.complete
    assert source.target_scope == "one"
    assert source.damage_kind == "magical"
    assert source.per_hit_powers == (215, 215)
    assert source.base_hit == 100
    assert source.linked_status_chance == 15
    assert source.max_new_harmful_statuses == 1


def test_unfinished_world_confluence_rupture_is_complete_dynamic_hit_contract() -> None:
    text = read_repo_text("docs/09_ENEMIES_AND_ENCOUNTERS/MAJOR_HUNTS/MAJOR_HUNT_06.md")
    source = parse_dynamic_element_hit_rule_text(
        "Confluence Rupture",
        _block(text, "Confluence Rupture"),
        context_text=text,
    )

    assert source.complete
    assert source.target_scope == "one"
    assert source.damage_kind == "magical"
    assert source.per_hit_powers == (280, 280)
    assert source.base_hit == 100
    assert source.linked_status_chance == 20
    assert source.max_new_harmful_statuses == 1
