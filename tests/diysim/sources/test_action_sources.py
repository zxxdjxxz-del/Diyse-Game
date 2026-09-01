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
    assert source.element_mode == "fixed"
    assert source.power == 175
    assert source.power_mode == "action"
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


def test_dynamic_element_identity_stays_dynamic_until_encounter_resolution() -> None:
    source = parse_authored_action_text(
        "Cycle Surge",
        "all conscious party members\nMagical / current expression\n175 Power per target\nBase Hit95\n20% Burn",
    )

    assert source.target_scope == "all"
    assert source.damage_kind == "magical"
    assert source.element is None
    assert source.element_mode == "dynamic"
    assert source.element_source == "current_expression"
    assert source.power == 175
    assert source.power_mode == "per_target"
    assert source.base_hit == 95
    assert source.status_chances == (("burn", 20),)


def test_standalone_damage_axis_with_state_driven_element_is_dynamic() -> None:
    source = parse_authored_action_text(
        "Reaction Pressure",
        "one party member\nMagical\nuses the current visible standard element\n180 Power\nBase Hit 100",
    )

    assert source.damage_kind == "magical"
    assert source.element is None
    assert source.element_mode == "dynamic"
    assert source.element_source == "current_visible_standard_element"
    assert source.target_scope == "one"
    assert source.power == 180


def test_standalone_inherited_element_line_is_dynamic_without_uses_wording() -> None:
    source = parse_authored_action_text(
        "Compression Lance",
        "- one party member\n- Magical\n- current inherited element\n- **245 Power**\n- Base Hit **95**",
    )

    assert source.target_scope == "one"
    assert source.damage_kind == "magical"
    assert source.element is None
    assert source.element_mode == "dynamic"
    assert source.element_source == "current_inherited_element"
    assert source.power == 245
    assert source.base_hit == 95


def test_explicit_target_declaration_wins_over_later_comparison_prose() -> None:
    source = parse_authored_action_text(
        "Gate Crush",
        "- all conscious party members\n- Physical / Neutral\n- **165 Power per target**\n"
        "This preserves the split: 20% Staggered single-target while Bound; 15% Staggered AoE while Freed.",
    )

    assert source.target_scope == "all"


def test_target_colon_established_party_member_is_single_target() -> None:
    source = parse_authored_action_text(
        "Heavy Bolt",
        "- target: one established party member\n- Physical / Neutral\n- Power **230**\n- Base Hit **95**",
    )

    assert source.target_scope == "one"


def test_hybrid_compact_element_weights_and_target_are_parsed_without_guessing() -> None:
    source = parse_authored_action_text(
        "Ruin Breach",
        "Hybrid / Ruin75/25 / one target\n**310 Power**\nBase Hit100\n25% Staggered",
    )

    assert source.damage_kind == "hybrid"
    assert source.element == "ruin"
    assert source.element_mode == "fixed"
    assert source.physical_weight == 0.75
    assert source.magical_weight == 0.25
    assert source.target_scope == "one"
    assert source.base_hit == 100
    assert source.status_chances == (("staggered", 25),)


def test_hybrid_split_weight_syntax_is_parsed() -> None:
    source = parse_authored_action_text(
        "Perfect Judgment",
        "Hybrid / Neutral /50% ATK /50% MAG / one target\n310 Power, Base Hit100",
    )

    assert source.damage_kind == "hybrid"
    assert source.element == "neutral"
    assert source.physical_weight == 0.5
    assert source.magical_weight == 0.5
    assert source.target_scope == "one"


def test_multihit_per_hit_power_and_dynamic_element_are_preserved() -> None:
    source = parse_authored_action_text(
        "Pairwise Return",
        "one party member\nup to two Magical hits\none hit for each currently active chamber\neach hit uses that chamber's element\n100 Power per hit\nBase Hit 100 per hit",
    )

    assert source.damage_kind == "magical"
    assert source.element_mode == "dynamic"
    assert source.element_source == "active_chamber_element"
    assert source.power == 100
    assert source.power_mode == "per_hit"
    assert source.hit_count_min == 1
    assert source.hit_count_max == 2
    assert source.is_multihit


def test_exact_multihit_count_is_preserved() -> None:
    source = parse_authored_action_text(
        "Enforcement Sequence",
        "Hybrid / Neutral /50% ATK /50% MAG / one target\n2 × 165 Power = 330 total\nBase Hit100 per hit",
    )

    assert source.hit_count_min == 2
    assert source.hit_count_max == 2
    assert source.power == 165
    assert source.is_multihit


def test_named_action_loader_supports_heading_and_inline_forms() -> None:
    heading = "**First Action**\n- all conscious targets; Magical / Fire; Power **150**; Base Hit **90**; **25 weight**."
    inline = "- **Second Action** — one enemy; Physical / Earth; Power **120**; Base Hit **100**; **75 weight**."

    assert load_named_action_source(heading, "First Action").target_scope == "all"
    assert load_named_action_source(inline, "Second Action").target_scope == "one"
