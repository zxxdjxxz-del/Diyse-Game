from __future__ import annotations

from tools.diysim.combat.analogue import FunctionalAnalogueRule, FunctionalAnalogueState
from tools.diysim.combat.models import CombatAction, StatusRider


def _rule() -> FunctionalAnalogueRule:
    return FunctionalAnalogueRule(
        single_power=150,
        aoe_power=105,
        base_hit=100,
        physical_element="neutral",
        magical_element="colorless",
        hybrid_element="neutral",
        hybrid_physical_weight=0.50,
        hybrid_magical_weight=0.50,
    )


def test_functional_analogue_accepts_attack_and_damage_ability_but_not_standard_card() -> None:
    state = FunctionalAnalogueState(name="Recorded Analogue", rule=_rule())
    attack = CombatAction(name="Attack", target_scope="one", damage_kind="physical", element="earth", power=None)
    card = CombatAction(name="Card Hit", target_scope="all", damage_kind="magical", element="fire", power=240)

    assert state.observe_completed_action(attack, category="attack")
    assert state.recorded is not None
    assert state.recorded.source_name == "Attack"

    assert not state.observe_completed_action(card, category="standard_card")
    assert state.recorded is not None
    assert state.recorded.source_name == "Attack"


def test_functional_analogue_replaces_element_and_uses_target_shape_power() -> None:
    state = FunctionalAnalogueState(name="Recorded Analogue", rule=_rule())
    source = CombatAction(
        name="Source Spell",
        target_scope="all",
        damage_kind="magical",
        element="lightning",
        power=310,
        base_hit=87,
        spirit_penetration=0.50,
        status_riders=(StatusRider("stun", 30),),
    )
    assert state.observe_completed_action(source, category="ability")

    analogue = state.materialize()
    assert analogue is not None
    assert analogue.target_scope == "all"
    assert analogue.damage_kind == "magical"
    assert analogue.element == "colorless"
    assert analogue.power == 105
    assert analogue.base_hit == 100
    assert analogue.spirit_penetration == 0.0
    assert analogue.status_riders == ()


def test_functional_analogue_hybrid_is_forced_to_authored_fifty_fifty_weights() -> None:
    state = FunctionalAnalogueState(name="Recorded Analogue", rule=_rule())
    source = CombatAction(
        name="Weighted Source",
        target_scope="one",
        damage_kind="hybrid",
        element="ruin",
        power=400,
        physical_weight=0.75,
        magical_weight=0.25,
    )
    assert state.observe_completed_action(source, category="ability")

    analogue = state.materialize()
    assert analogue is not None
    assert analogue.power == 150
    assert analogue.element == "neutral"
    assert analogue.physical_weight == 0.50
    assert analogue.magical_weight == 0.50


def test_functional_analogue_collapses_multihit_and_clears_only_when_consumed() -> None:
    state = FunctionalAnalogueState(name="Recorded Analogue", rule=_rule())
    source = CombatAction(name="Triple", target_scope="one", damage_kind="physical", element="fire", power=300)
    assert state.observe_completed_action(source, category="ability", hit_powers=(100, 100, 100))
    assert state.recorded is not None
    assert state.recorded.hit_count == 3

    preview = state.materialize()
    assert preview is not None
    assert preview.power == 150
    assert state.available

    used = state.consume()
    assert used == preview
    assert not state.available
    assert state.recorded is None
