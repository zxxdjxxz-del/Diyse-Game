from __future__ import annotations

from tools.diysim.sources.actions import load_named_action_source, parse_authored_action_text


def test_authored_action_parser_reads_only_fields_present_in_source_text() -> None:
    source = parse_authored_action_text(
        "Synthetic Strike",
        "one conscious target; Physical / Neutral; Power **175**; Base Hit **96**; "
        "**21% base Bleed**; **63 weight**.",
    )

    assert source.target_scope == "one"
    assert source.damage_kind == "physical"
    assert source.element == "neutral"
    assert source.power == 175
    assert source.base_hit == 96
    assert source.weight == 63
    assert source.status_chances == (("bleed", 21),)


def test_missing_authored_fields_stay_missing_instead_of_receiving_fallbacks() -> None:
    source = parse_authored_action_text("Synthetic Gap", "one conscious target; Power **220**.")

    assert source.power == 220
    assert source.damage_kind is None
    assert source.element is None
    assert source.base_hit is None
    assert source.weight is None
    assert source.missing("damage_kind", "element", "base_hit", "weight") == (
        "damage_kind",
        "element",
        "base_hit",
        "weight",
    )


def test_named_action_loader_supports_heading_and_inline_forms() -> None:
    heading = "**First Action**\n- all conscious targets; Magical / Fire; Power **150**; Base Hit **90**; **25 weight**."
    inline = "- **Second Action** — one enemy; Physical / Earth; Power **120**; Base Hit **100**; **75 weight**."

    assert load_named_action_source(heading, "First Action").target_scope == "all"
    assert load_named_action_source(inline, "Second Action").target_scope == "one"
