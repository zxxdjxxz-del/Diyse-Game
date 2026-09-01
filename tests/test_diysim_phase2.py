from __future__ import annotations

import random

from tools.diysim.core import Stats
from tools.diysim.rules import (
    CombatAction, CombatUnit, Combatant, affinity_damage_multiplier, apply_status,
    effective_defense, effective_spirit, healing_amount,
    linked_status_affinity_modifier, resolve_mp_cost, status_application_chance,
)
from tools.diysim.battle import (
    complete_turn, end_round, resolve_heal, run_advanced_battle, turn_is_blocked,
)


def _unit(*, rank="ordinary", hp=1000, mp=100, magic=100, status_resistance=0) -> CombatUnit:
    template = Combatant(
        "Test",
        "party",
        Stats(hp, mp, 100, magic, 100, 100, 50),
        rank=rank,
        status_resistance=status_resistance,
    )
    return CombatUnit(template, 0)


def test_current_elemental_affinity_multipliers() -> None:
    assert affinity_damage_multiplier("weak") == 1.25
    assert affinity_damage_multiplier("neutral") == 1.0
    assert affinity_damage_multiplier("resistant") == 0.8
    assert affinity_damage_multiplier("strongly_resistant") == 0.6
    assert affinity_damage_multiplier("immune") == 0.0


def test_linked_status_affinity_modifier() -> None:
    assert linked_status_affinity_modifier("fire", "burn", "weak") == 10
    assert linked_status_affinity_modifier("fire", "burn", "resistant") == -10
    assert linked_status_affinity_modifier("fire", "burn", "strongly_resistant") == -10
    assert linked_status_affinity_modifier("fire", "burn", "immune") is None
    assert linked_status_affinity_modifier("fire", "stun", "weak") == 0


def test_status_application_resolver_and_clamp() -> None:
    assert status_application_chance(35, affinity_modifier=10, status_resistance=5) == 40
    assert status_application_chance(1, status_resistance=15) == 5
    assert status_application_chance(99, specialist_bonus=20) == 95
    assert status_application_chance(50, immune=True) == 0


def test_mp_cost_resolver_matches_current_modifier_example() -> None:
    assert resolve_mp_cost(30, remaining_cost_factors=(0.80, 0.85)) == 20
    assert resolve_mp_cost(10, flat_delta=-1) == 9
    assert resolve_mp_cost(0, remaining_cost_factors=(0.80,)) == 0


def test_blue_warden_healing_formulas() -> None:
    assert healing_amount(1000, 100, max_hp_percent=0.22, magic_scaling=1.50) == 370
    assert healing_amount(1000, 100, max_hp_percent=0.10, magic_scaling=0.90) == 190
    assert healing_amount(1000, 100, max_hp_percent=0.22, magic_scaling=1.50, potency_multiplier=1.10) == 407


def test_burn_penalties_and_high_rank_damage_tick() -> None:
    unit = _unit(rank="major_boss")
    apply_status(unit, "burn")
    assert effective_defense(unit) == 90
    assert effective_spirit(unit) == 90
    end_round([unit])
    assert unit.hp == 970
    assert unit.statuses["burn"].remaining_rounds == 3


def test_staggered_duration_converts_for_major_boss() -> None:
    unit = _unit(rank="major_boss")
    apply_status(unit, "staggered")
    assert unit.statuses["staggered"].remaining_rounds == 3
    for _ in range(3):
        end_round([unit])
    assert "staggered" not in unit.statuses


def test_bleed_action_round_cadence_and_escalation() -> None:
    unit = _unit(hp=1000)
    apply_status(unit, "bleed")

    complete_turn(unit, acted=True)
    assert unit.hp == 970
    end_round([unit])
    assert unit.hp == 940

    complete_turn(unit, acted=True)
    assert unit.hp == 910
    end_round([unit])
    assert unit.hp == 880

    complete_turn(unit, acted=True)
    assert unit.hp == 850
    assert unit.statuses["bleed"].bleed_escalated is True
    end_round([unit])
    assert unit.hp == 810


def test_bleed_lost_turn_ages_without_action_proc() -> None:
    unit = _unit(hp=1000)
    apply_status(unit, "bleed")
    complete_turn(unit, acted=False)
    assert unit.hp == 1000
    assert unit.statuses["bleed"].bleed_turn_age == 1


def test_full_heal_clears_bleed_before_post_action_proc() -> None:
    caster = _unit(hp=1000, magic=100)
    caster.hp = 500
    apply_status(caster, "bleed")
    action = CombatAction(
        "Self Mend",
        action_kind="heal",
        target_side="self",
        heal_max_hp_percent=1.0,
    )
    resolve_heal(caster, action, caster)
    assert caster.hp == caster.max_hp
    assert "bleed" not in caster.statuses
    complete_turn(caster, acted=True)
    assert caster.hp == caster.max_hp


def test_major_boss_freeze_blocks_exactly_one_affected_round() -> None:
    unit = _unit(rank="major_boss")
    apply_status(unit, "freeze")
    assert turn_is_blocked(unit, random.Random(1)) is True
    assert "freeze" not in unit.statuses
    assert turn_is_blocked(unit, random.Random(1)) is False


def test_stun_expires_after_four_affected_turns() -> None:
    class AlwaysBlock:
        def random(self) -> float:
            return 0.0

    unit = _unit()
    apply_status(unit, "stun")
    for i in range(4):
        assert turn_is_blocked(unit, AlwaysBlock()) is True
        if i < 3:
            assert "stun" in unit.statuses
    assert "stun" not in unit.statuses


def test_advanced_battle_spends_mp_and_falls_back_to_basic_attack() -> None:
    party = Combatant(
        "Caster",
        "party",
        Stats(500, 5, 100, 100, 50, 50, 60),
        actions=(CombatAction("Burst", mp_cost=5, damage_kind="magical", power=200, crit_chance=0),),
    )
    enemy = Combatant(
        "Target",
        "enemy",
        Stats(500, 0, 1, 1, 100, 100, 10),
        actions=(CombatAction("Tap", power=1, crit_chance=0),),
    )
    outcome = run_advanced_battle((party,), (enemy,), random.Random(7), max_rounds=10)
    assert outcome.winner == "party"
    assert outcome.party_mp_fraction == 0.0


def test_advanced_battle_applies_elemental_weakness() -> None:
    party = Combatant(
        "Fire Caster",
        "party",
        Stats(500, 0, 1, 120, 50, 50, 60),
        actions=(CombatAction("Flame", damage_kind="magical", element="fire", power=200, crit_chance=0),),
    )
    enemy = Combatant(
        "Weak Target",
        "enemy",
        Stats(100, 0, 1, 1, 50, 100, 10),
        actions=(CombatAction("Tap", power=1, crit_chance=0),),
        elemental_affinities={"fire": "weak"},
    )
    outcome = run_advanced_battle((party,), (enemy,), random.Random(3), max_rounds=2)
    assert outcome.winner == "party"
    assert outcome.rounds == 1
