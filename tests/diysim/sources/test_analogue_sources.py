from __future__ import annotations

from tools.diysim.sources.analogues import parse_functional_analogue_rule_text
from tools.diysim.sources.markdown import extract_heading_block
from tools.diysim.sources.repo import read_repo_text


def test_first_command_warden_recorded_action_system_parses_as_complete_functional_analogue() -> None:
    text = read_repo_text("docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/FIRST_COMMAND_WARDEN.md")
    block = extract_heading_block(text, "Recorded action system")
    source = parse_functional_analogue_rule_text(block)

    assert source.complete
    assert source.single_power == 150
    assert source.aoe_power == 105
    assert source.base_hit == 100
    assert source.physical_element == "neutral"
    assert source.magical_element == "colorless"
    assert source.hybrid_element == "neutral"
    assert source.hybrid_physical_weight == 0.50
    assert source.hybrid_magical_weight == 0.50
    assert source.record_after_completion
    assert source.eligible_attack
    assert source.eligible_ability
    assert source.standard_card_ineligible
    assert source.max_records == 1
    assert source.collapse_multihit
    assert source.clear_after_use
    assert source.strips_secondary_mechanics
