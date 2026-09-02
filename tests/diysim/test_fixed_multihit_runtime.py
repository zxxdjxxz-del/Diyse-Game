from __future__ import annotations

from tools.diysim.encounters.runtime_catalog import _direct_action
from tools.diysim.sources.actions import parse_authored_action_text


def _parse(name: str, text: str):
    return parse_authored_action_text(name, text)


def test_exact_per_hit_multihit_builds_shared_combat_action() -> None:
    source = _parse(
        "Enforcement Sequence",
        "one party member\n"
        "Hybrid / Neutral /50% ATK /50% MAG\n"
        "2 × 165 Power = 330 total\n"
        "Base Hit100 per hit",
    )

    action, blockers, dynamic_source, dynamic_riders = _direct_action(
        source,
        triggered=False,
        dynamic_states={},
    )

    assert blockers == ()
    assert dynamic_source is None
    assert dynamic_riders == ()
    assert action is not None
    assert action.power == 165
    assert action.hit_count == 2
    assert action.physical_weight == 0.5
    assert action.magical_weight == 0.5


def test_fixed_multihit_without_per_hit_power_stays_blocked() -> None:
    source = _parse(
        "Ambiguous Barrage",
        "one party member\n"
        "Physical / Neutral\n"
        "2 Physical hits\n"
        "330 Power\n"
        "Base Hit100 per hit",
    )

    action, blockers, _, _ = _direct_action(
        source,
        triggered=False,
        dynamic_states={},
    )

    assert action is None
    assert blockers == (
        "Ambiguous Barrage: fixed multihit lacks explicit per-hit Power authority",
    )


def test_variable_multihit_stays_blocked_even_with_per_hit_power() -> None:
    source = _parse(
        "Variable Barrage",
        "one party member\n"
        "Physical / Neutral\n"
        "2–3 Physical hits\n"
        "120 Power per hit\n"
        "Base Hit100 per hit",
    )

    action, blockers, _, _ = _direct_action(
        source,
        triggered=False,
        dynamic_states={},
    )

    assert action is None
    assert blockers == (
        "Variable Barrage: variable multihit count requires action-specific runtime",
    )
