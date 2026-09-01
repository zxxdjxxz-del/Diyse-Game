from __future__ import annotations

from tools.diysim.combat.models import CombatAction, StatusRider, TemporaryModifierSpec
from tools.diysim.combat.replay import (
    BoundedReplayRule,
    BoundedReplayState,
    record_completed_damage_action,
    replay_category_eligible,
    split_total_power_evenly,
    transform_bounded_replay,
)
from tools.diysim.sources.combat import load_combat_rules


def test_bounded_replay_records_completed_damage_signature_only_for_eligible_categories() -> None:
    action = CombatAction(
        name="Threefold Test",
        target_scope="all",
        damage_kind="hybrid",
        element="fire",
        power=301,
        base_hit=94,
        physical_weight=0.75,
        magical_weight=0.25,
        defense_penetration=0.30,
        status_riders=(StatusRider("burn", 20),),
        temporary_modifiers=(TemporaryModifierSpec("test", 1, status_resistance_flat=10),),
    )

    assert replay_category_eligible("ability", action)
    recorded = record_completed_damage_action(action, category="ability", hit_powers=(101, 100, 100))
    assert recorded is not None
    assert recorded.total_power == 301
    assert recorded.hit_count == 3
    assert recorded.damage_kind == "hybrid"
    assert recorded.element == "fire"
    assert recorded.target_scope == "all"
    assert recorded.physical_weight == 0.75
    assert recorded.magical_weight == 0.25

    assert record_completed_damage_action(action, category="item") is None
    assert record_completed_damage_action(action, category="prime_command") is None


def test_bounded_replay_scales_total_power_clamps_then_splits_preserved_hit_count() -> None:
    source = CombatAction(
        name="Source Triple",
        target_scope="one",
        damage_kind="physical",
        element="neutral",
        power=301,
    )
    recorded = record_completed_damage_action(source, category="ability", hit_powers=(101, 100, 100))
    assert recorded is not None

    replay = transform_bounded_replay(
        recorded,
        BoundedReplayRule(power_scale=0.65, min_total_power=80, max_total_power=180, base_hit=100),
        name="Recorded Echo",
    )

    # 301 × .65 rounds above the 180 cap; total Power is capped before splitting.
    assert replay.total_power == 180
    assert replay.hit_powers == (60, 60, 60)
    assert replay.hit_count == 3
    assert replay.target_scope == "one"
    assert replay.damage_kind == "physical"
    assert replay.element == "neutral"
    assert replay.base_hit == 100


def test_even_power_split_is_deterministic_when_total_is_not_divisible() -> None:
    assert split_total_power_evenly(181, 3) == (61, 60, 60)
    assert split_total_power_evenly(182, 3) == (61, 61, 60)


def test_replay_hit_action_strips_source_secondary_mechanics() -> None:
    source = CombatAction(
        name="Loaded Source",
        target_scope="all",
        damage_kind="magical",
        element="lightning",
        power=200,
        base_hit=77,
        defense_penetration=0.50,
        spirit_penetration=0.40,
        status_riders=(StatusRider("stun", 35),),
        temporary_modifiers=(TemporaryModifierSpec("loaded", 2, status_resistance_flat=20),),
    )
    recorded = record_completed_damage_action(source, category="standard_card")
    assert recorded is not None
    replay = transform_bounded_replay(
        recorded,
        BoundedReplayRule(power_scale=0.75, min_total_power=120, max_total_power=260, base_hit=100),
        name="Devoured Replay",
    )
    hit = replay.combat_action_for_hit(replay.hit_powers[0])

    assert hit.base_hit == 100
    assert hit.target_scope == "all"
    assert hit.damage_kind == "magical"
    assert hit.element == "lightning"
    assert hit.defense_penetration == 0.0
    assert hit.spirit_penetration == 0.0
    assert hit.status_riders == ()
    assert hit.temporary_modifiers == ()


def test_basic_attack_records_repo_owned_power_without_runtime_guessing() -> None:
    attack = CombatAction(name="Attack", target_scope="one", damage_kind="physical", element="neutral", power=None)
    recorded = record_completed_damage_action(attack, category="attack")
    assert recorded is not None
    assert recorded.total_power == load_combat_rules().basic_attack_power
    assert recorded.hit_count == 1


def test_bounded_replay_state_replaces_only_with_new_eligible_completed_record() -> None:
    state = BoundedReplayState(
        name="Recorded Echo",
        rule=BoundedReplayRule(power_scale=0.65, min_total_power=80, max_total_power=180, base_hit=100),
    )
    first = CombatAction(name="First", target_scope="one", damage_kind="physical", element="neutral", power=120)
    second = CombatAction(name="Second", target_scope="all", damage_kind="magical", element="fire", power=200)

    assert not state.available
    assert state.observe_completed_action(first, category="ability")
    assert state.available
    assert state.recorded is not None
    assert state.recorded.source_name == "First"

    # Ineligible completed commands do not erase the current most-recent eligible record.
    assert not state.observe_completed_action(second, category="item")
    assert state.recorded is not None
    assert state.recorded.source_name == "First"

    assert state.observe_completed_action(second, category="standard_card")
    assert state.recorded is not None
    assert state.recorded.source_name == "Second"
    assert state.materialize() is not None
    assert state.materialize().target_scope == "all"


def test_bounded_replay_state_materialization_does_not_consume_record() -> None:
    state = BoundedReplayState(
        name="Deep Duplicate",
        rule=BoundedReplayRule(power_scale=0.80, min_total_power=110, max_total_power=240, base_hit=100),
    )
    action = CombatAction(name="Source", target_scope="one", damage_kind="magical", element="colorless", power=180)
    assert state.observe_completed_action(action, category="ability")

    first = state.materialize()
    second = state.materialize()

    assert first is not None
    assert second is not None
    assert first == second
    assert state.available
    assert state.recorded is not None
    assert state.recorded.source_name == "Source"
