from __future__ import annotations

from tools.diysim.combat.living_archive import (
    LivingArchiveState,
    echo_weave_mp_cost,
    materialize_echo_weave,
)
from tools.diysim.combat.models import CombatAction, CombatUnit, Combatant
from tools.diysim.combat.status_runtime import complete_turn
from tools.diysim.progression import Stats


def _nimera() -> CombatUnit:
    return CombatUnit(
        Combatant(
            name="Nimera",
            side="party",
            stats=Stats(hp=300, mp=60, attack=30, magic=60, defense=30, spirit=40, speed=35),
        ),
        0,
    )


def test_living_archive_keeps_last_records_and_clears_on_turn_completion() -> None:
    state = LivingArchiveState(capacity=2)
    for name, mp in (("A", 9), ("B", 15), ("C", 22)):
        state.observe_completed_action(
            CombatAction(name=name, damage_kind="magical", element="colorless", power=150, mp_cost=mp),
            source_actor="ally",
            category="ability",
        )
    assert [record.action.name for record in state.records] == ["B", "C"]

    nimera = _nimera()
    nimera.tactical_states["living_archive"] = state
    complete_turn(nimera, acted=False)
    assert state.records == []


def test_echo_weave_scales_potency_and_uses_variable_mp_rule() -> None:
    state = LivingArchiveState(capacity=2)
    source = CombatAction(
        name="Warden's Valor",
        mp_cost=15,
        damage_kind="magical",
        element="colorless",
        power=170,
        base_hit=100,
    )
    state.observe_completed_action(source, source_actor="Ilyra", category="ability")
    record = state.records[0]

    assert echo_weave_mp_cost(record, cost_scale=0.75, minimum_mp=8) == 11
    echo = materialize_echo_weave(
        record,
        potency=0.90,
        cost_scale=0.75,
        minimum_mp=8,
    )
    assert echo.name == "Echo Weave"
    assert echo.mp_cost == 11
    assert echo.power == 170
    assert echo.final_damage_multiplier == 0.90
    assert echo.damage_kind == "magical"
    assert echo.element == "colorless"
