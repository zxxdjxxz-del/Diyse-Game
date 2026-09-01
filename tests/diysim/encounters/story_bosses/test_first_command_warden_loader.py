from __future__ import annotations

import pytest

from tools.diysim.encounters.story_bosses.first_command_warden import (
    load_first_command_warden_repo_data,
)


def test_warden_loader_reads_current_owner_bodies() -> None:
    data = load_first_command_warden_repo_data()

    assert data.displayed_level == 14
    assert data.warden.stats.as_dict() == {
        "hp": 2850, "mp": 0, "attack": 72, "magic": 72,
        "defense": 43, "spirit": 43, "speed": 30,
    }
    assert data.warden.evasion == 0
    assert data.warden.status_resistance == 10

    assert data.command_ring.stats.as_dict() == {
        "hp": 260, "mp": 0, "attack": 0, "magic": 0,
        "defense": 40, "spirit": 46, "speed": 0,
    }
    assert data.command_ring.evasion == 0
    assert data.command_ring.status_resistance == 10


def test_warden_loader_reads_state_a_actions_and_seal() -> None:
    data = load_first_command_warden_repo_data()
    by_name = {action.name: action for action in data.state_a_actions}

    lance = by_name["Authority Lance"]
    assert (lance.target_scope, lance.damage_kind, lance.element, lance.power, lance.base_hit) == (
        "one", "physical", "neutral", 190, 100,
    )
    pulse = by_name["Judgment Pulse"]
    assert (pulse.target_scope, pulse.damage_kind, pulse.element, pulse.power, pulse.base_hit) == (
        "all", "magical", "colorless", 140, 100,
    )
    assert data.repetition_locks["Judgment Pulse"] == 2

    seal = data.command_seal
    assert seal.duration_rounds == 2
    assert seal.repetition_lock_rounds == 2
    assert seal.categories == ("Attack", "Ability", "Card", "Item", "Defend")
    assert (seal.reprisal.target_scope, seal.reprisal.damage_kind, seal.reprisal.element) == (
        "one", "magical", "colorless",
    )
    assert seal.reprisal.power == 100
    assert seal.reprisal.base_hit == 100


def test_warden_loader_reads_ring_and_recorded_analogue_rules() -> None:
    data = load_first_command_warden_repo_data()
    ruling = data.major_ruling
    assert ruling.preparation_rounds == 1
    assert ruling.repetition_lock_rounds == 3
    assert ruling.ring_realign_rounds == 3
    assert ruling.action.target_scope == "all"
    assert ruling.action.damage_kind == "magical"
    assert ruling.action.element == "colorless"
    assert ruling.action.power == 210
    assert ruling.action.base_hit == 95
    assert [(r.status, r.base_chance) for r in ruling.action.status_riders] == [("stun", 15)]

    analogue = data.recorded_analogue
    assert analogue.complete
    assert analogue.single_power == 150
    assert analogue.aoe_power == 105
    assert analogue.base_hit == 100
    assert analogue.physical_element == "neutral"
    assert analogue.magical_element == "colorless"
    assert analogue.hybrid_element == "neutral"
    assert analogue.hybrid_physical_weight == pytest.approx(0.5)
    assert analogue.hybrid_magical_weight == pytest.approx(0.5)
    assert analogue.max_records == 1
    assert analogue.clear_after_use


def test_warden_loader_reads_state_b_transition_and_actions() -> None:
    data = load_first_command_warden_repo_data()
    by_name = {action.name: action for action in data.state_b_actions}

    crush = by_name["Warden Crush"]
    assert (crush.target_scope, crush.damage_kind, crush.element, crush.power, crush.base_hit) == (
        "one", "physical", "neutral", 245, 100,
    )

    verdict = by_name["Challenged Verdict"]
    assert verdict.damage_kind == "hybrid"
    assert verdict.power == 230
    assert verdict.physical_weight == pytest.approx(0.5)
    assert verdict.magical_weight == pytest.approx(0.5)
    assert [(r.status, r.base_chance) for r in verdict.status_riders] == [("staggered", 20)]

    collapse = by_name["Command Collapse"]
    assert (collapse.target_scope, collapse.damage_kind, collapse.element, collapse.power, collapse.base_hit) == (
        "all", "magical", "colorless", 165, 95,
    )
    assert [(r.status, r.base_chance) for r in collapse.status_riders] == [("stun", 15)]

    assert data.repetition_locks["Challenged Verdict"] == 1
    assert data.repetition_locks["Command Collapse"] == 2
    assert data.state_b_trigger_fraction == pytest.approx(0.45)
    assert data.state_b_protection.disrupted_reduction == pytest.approx(0.10)
    assert data.state_b_protection.disrupted_rounds == 1
    assert data.state_b_protection.undisrupted_reduction == pytest.approx(0.15)
    assert data.state_b_protection.undisrupted_rounds == 2
