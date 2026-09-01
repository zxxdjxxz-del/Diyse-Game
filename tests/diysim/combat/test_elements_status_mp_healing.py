from __future__ import annotations

import random

from tools.diysim.combat import (
    CombatAction,
    CombatUnit,
    Combatant,
    affinity_damage_multiplier,
    apply_status,
    complete_turn,
    effective_defense,
    effective_spirit,
    end_round,
    healing_amount,
    linked_status_affinity_modifier,
    load_combat_rules,
    resolve_heal,
    resolve_mp_cost,
    status_application_chance,
    turn_is_blocked,
)
from tools.diysim.progression import Stats


def _unit(*, rank="ordinary", hp=1000, mp=100, magic=100, status_resistance=0) -> CombatUnit:
    template = Combatant(
        "Test",
        "party",
        Stats(hp, mp, 100, magic, 100, 100, 50),
        rank=rank,
        status_resistance=status_resistance,
    )
    return CombatUnit(template, 0)


def test_elemental_affinity_accessors_reflect_repo_rules() -> None:
    rules = load_combat_rules()
    for affinity, expected in rules.affinity_damage_multipliers.items():
        assert affinity_damage_multiplier(affinity) == expected
    for element, status in rules.linked_statuses.items():
        for affinity, expected in rules.linked_status_affinity_modifiers.items():
            assert linked_status_affinity_modifier(element, status, affinity) == expected


def test_unlinked_status_gets_no_affinity_modifier() -> None:
    rules = load_combat_rules()
    element, linked_status = next(iter(rules.linked_statuses.items()))
    other_status = next(status for status in {"burn", "freeze", "stun", "staggered", "bleed"} if status != linked_status)
    assert linked_status_affinity_modifier(element, other_status, "weak") == 0


def test_status_application_resolver_uses_repo_clamp() -> None:
    rules = load_combat_rules()
    assert status_application_chance(-100) == rules.status_chance_min
    assert status_application_chance(1000) == rules.status_chance_max
    assert status_application_chance(50, immune=True) == 0


def test_mp_cost_resolver_is_generic_math() -> None:
    assert resolve_mp_cost(30, remaining_cost_factors=(0.80, 0.85)) == 20
    assert resolve_mp_cost(10, flat_delta=-1) == 9
    assert resolve_mp_cost(0, remaining_cost_factors=(0.80,)) == 0


def test_healing_formula_is_generic_math() -> None:
    assert healing_amount(1000, 100, max_hp_percent=0.20, magic_scaling=1.25) == 325
    assert healing_amount(1000, 100, max_hp_percent=0.10, magic_scaling=0.50, potency_multiplier=1.20) == 180


def test_burn_penalties_and_high_rank_tick_use_repo_rules() -> None:
    rules = load_combat_rules()
    unit = _unit(rank="major_boss")
    apply_status(unit, "burn")
    assert effective_defense(unit) == unit.template.stats.defense * (1.0 - rules.burn_defense_penalty)
    assert effective_spirit(unit) == unit.template.stats.spirit * (1.0 - rules.burn_spirit_penalty)
    before = unit.hp
    end_round([unit])
    assert unit.hp < before
    assert unit.statuses["burn"].remaining_rounds == rules.burn_rounds - 1


def test_staggered_duration_uses_repo_rank_conversion() -> None:
    rules = load_combat_rules()
    unit = _unit(rank="major_boss")
    apply_status(unit, "staggered")
    duration = rules.staggered_rounds["major_boss"]
    assert unit.statuses["staggered"].remaining_rounds == duration
    for _ in range(duration):
        end_round([unit])
    assert "staggered" not in unit.statuses


def test_bleed_action_round_cadence_and_escalation_uses_repo_rates() -> None:
    rules = load_combat_rules()
    unit = _unit(hp=1000)
    apply_status(unit, "bleed")

    for turn in range(1, rules.bleed_escalation_turns + 1):
        before_action = unit.hp
        complete_turn(unit, acted=True)
        assert unit.hp < before_action
        if turn < rules.bleed_escalation_turns:
            assert unit.statuses["bleed"].bleed_escalated is False
        before_round = unit.hp
        end_round([unit])
        assert unit.hp < before_round

    assert unit.statuses["bleed"].bleed_escalated is True


def test_bleed_lost_turn_ages_without_action_proc() -> None:
    unit = _unit(hp=1000)
    apply_status(unit, "bleed")
    before = unit.hp
    complete_turn(unit, acted=False)
    assert unit.hp == before
    assert unit.statuses["bleed"].bleed_turn_age == 1


def test_full_heal_clears_bleed_before_post_action_proc() -> None:
    caster = _unit(hp=1000, magic=100)
    caster.hp = 500
    apply_status(caster, "bleed")
    action = CombatAction("Synthetic Full Heal", action_kind="heal", target_side="self", heal_max_hp_percent=1.0)
    resolve_heal(caster, action, caster)
    assert caster.hp == caster.max_hp
    assert "bleed" not in caster.statuses
    complete_turn(caster, acted=True)
    assert caster.hp == caster.max_hp


def test_major_boss_freeze_uses_repo_maximum() -> None:
    rules = load_combat_rules()
    unit = _unit(rank="major_boss")
    apply_status(unit, "freeze")
    blocked_turns = 0
    while unit.has_status("freeze") and blocked_turns < 10:
        blocked_turns += int(turn_is_blocked(unit, random.Random(1)))
    assert blocked_turns == rules.freeze_max_rounds["major_boss"]


def test_stun_expires_after_repo_authored_affected_turns() -> None:
    rules = load_combat_rules()

    class AlwaysBlock:
        def random(self) -> float:
            return 0.0

    unit = _unit()
    apply_status(unit, "stun")
    for index in range(rules.stun_turns):
        assert turn_is_blocked(unit, AlwaysBlock()) is True
        if index < rules.stun_turns - 1:
            assert "stun" in unit.statuses
    assert "stun" not in unit.statuses
