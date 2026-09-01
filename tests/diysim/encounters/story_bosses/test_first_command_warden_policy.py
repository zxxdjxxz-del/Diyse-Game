from __future__ import annotations

from tools.diysim.combat.living_archive import LivingArchiveState
from tools.diysim.combat.models import ActiveStatus, CombatUnit
from tools.diysim.combat.status_runtime import complete_turn
from tools.diysim.encounters.story_bosses.first_command_warden.policy import (
    HARMONIZED_STATE_KEY,
    LIVING_ARCHIVE_STATE_KEY,
    WardenPolicyConfig,
    choose_player_action,
    load_warden_party_actions,
)
from tools.diysim.encounters.story_bosses.first_command_warden.snapshots import (
    load_first_command_warden_party_snapshot,
)


def _party(level: int = 11) -> list[CombatUnit]:
    snapshot = load_first_command_warden_party_snapshot(level)
    return [CombatUnit(template, index) for index, template in enumerate(snapshot.party)]


def test_warden_policy_actions_match_current_repo_package() -> None:
    actions = load_warden_party_actions()
    assert actions.crest_strike.power == 140
    assert actions.resonant_pulse.power == 150
    assert actions.harmonized_crest_multiplier == 1.10
    assert actions.wardens_valor.power == 170
    assert actions.cinder_shot.power == 155
    assert actions.sizing_shot.power == 155
    assert actions.colossus_draw.power == 265
    assert actions.colossus_draw.defense_penetration == 0.25
    assert actions.measured_colossus_penetration == 0.35
    assert actions.hunter_measure_full_rounds == 2
    assert actions.hunter_measure_party_crit_bonus == 10
    assert actions.hunter_measure_torren_crit_bonus == 5
    assert actions.weave_burst.power == 130
    assert actions.living_archive_capacity == 2
    assert actions.echo_weave_potency == 0.90
    assert actions.echo_weave_cost_scale == 0.75
    assert actions.echo_weave_minimum_mp == 8
    assert actions.mend.heal_max_hp_percent == 0.22
    assert actions.mend.healing_potency == 1.10
    assert actions.clear_warding.heal_max_hp_percent == 0.05
    assert actions.clear_warding.clear_harmful_statuses == 1
    assert actions.renewal.target_scope == "all"
    assert actions.renewal.heal_max_hp_percent == 0.10
    assert actions.gentle_continuance_bonus == 0.05


def test_cyanis_alternates_harmonized_crest_and_preserves_prime_through_attack() -> None:
    party = _party()
    cyanis = next(unit for unit in party if unit.template.name == "Cyanis")
    actions = load_warden_party_actions()

    category, action, _ = choose_player_action(
        cyanis,
        party,
        actions,
        sealed_category=None,
        config=WardenPolicyConfig(),
    )
    assert category == "Ability"
    assert action.name == "Crest Strike"
    assert action.final_damage_multiplier == 1.0
    assert cyanis.tactical_states[HARMONIZED_STATE_KEY] == "magical"

    cyanis.mp -= action.mp_cost
    category, action, _ = choose_player_action(
        cyanis,
        party,
        actions,
        sealed_category=None,
        config=WardenPolicyConfig(),
    )
    assert category == "Ability"
    assert action.name == "Resonant Pulse"
    assert action.final_damage_multiplier == 1.10
    assert cyanis.tactical_states[HARMONIZED_STATE_KEY] == "physical"

    category, action, _ = choose_player_action(
        cyanis,
        party,
        actions,
        sealed_category="Ability",
        config=WardenPolicyConfig(),
    )
    assert category == "Attack"
    assert action.name == "Attack"
    assert cyanis.tactical_states[HARMONIZED_STATE_KEY] == "physical"


def test_nimera_uses_quick_study_echo_weave_from_current_archive_window() -> None:
    party = _party()
    cyanis = next(unit for unit in party if unit.template.name == "Cyanis")
    ilyra = next(unit for unit in party if unit.template.name == "Ilyra")
    nimera = next(unit for unit in party if unit.template.name == "Nimera")
    actions = load_warden_party_actions()

    choose_player_action(
        cyanis,
        party,
        actions,
        sealed_category=None,
        config=WardenPolicyConfig(),
    )
    choose_player_action(
        ilyra,
        party,
        actions,
        sealed_category=None,
        config=WardenPolicyConfig(),
    )

    archive = nimera.tactical_states[LIVING_ARCHIVE_STATE_KEY]
    assert isinstance(archive, LivingArchiveState)
    assert [record.action.name for record in archive.records] == ["Crest Strike", "Warden's Valor"]

    category, action, target = choose_player_action(
        nimera,
        party,
        actions,
        sealed_category=None,
        config=WardenPolicyConfig(),
    )
    assert category == "Ability"
    assert target is None
    assert action.name == "Echo Weave"
    assert action.damage_kind == "magical"
    assert action.power == 170
    assert action.final_damage_multiplier == 0.90
    assert action.mp_cost == 11

    complete_turn(nimera, acted=True)
    assert archive.records == []


def test_torren_establishes_measure_then_uses_measured_colossus() -> None:
    party = _party()
    torren = next(unit for unit in party if unit.template.name == "Torren")
    actions = load_warden_party_actions()

    category, action, target = choose_player_action(
        torren,
        party,
        actions,
        sealed_category=None,
        hunter_measure_active=False,
        target_is_ring=False,
        config=WardenPolicyConfig(),
    )
    assert category == "Ability"
    assert target is None
    assert action.name == "Sizing Shot"
    assert action.power == 155

    torren.mp = torren.max_mp
    category, action, target = choose_player_action(
        torren,
        party,
        actions,
        sealed_category=None,
        hunter_measure_active=True,
        target_is_ring=False,
        config=WardenPolicyConfig(),
    )
    assert category == "Ability"
    assert target is None
    assert action.name == "Colossus Draw"
    assert action.power == 265
    assert action.defense_penetration == 0.35
    assert action.crit_chance == 20


def test_ring_target_does_not_receive_boss_measure_bonuses() -> None:
    party = _party()
    torren = next(unit for unit in party if unit.template.name == "Torren")
    torren.mp = torren.max_mp
    actions = load_warden_party_actions()
    _, action, _ = choose_player_action(
        torren,
        party,
        actions,
        sealed_category=None,
        hunter_measure_active=True,
        target_is_ring=True,
        config=WardenPolicyConfig(),
    )
    assert action.name == "Colossus Draw"
    assert action.defense_penetration == 0.25
    assert action.crit_chance is None


def test_ilyra_prioritizes_control_cleanse_then_mend() -> None:
    party = _party()
    ilyra = next(unit for unit in party if unit.template.name == "Ilyra")
    cyanis = next(unit for unit in party if unit.template.name == "Cyanis")
    actions = load_warden_party_actions()

    cyanis.statuses["stun"] = ActiveStatus("stun")
    category, action, target = choose_player_action(
        ilyra,
        party,
        actions,
        sealed_category=None,
        config=WardenPolicyConfig(),
    )
    assert category == "Ability"
    assert action.name == "Clear Warding"
    assert target is cyanis

    cyanis.statuses.clear()
    cyanis.hp = int(cyanis.max_hp * 0.40)
    category, action, target = choose_player_action(
        ilyra,
        party,
        actions,
        sealed_category=None,
        config=WardenPolicyConfig(mend_below_hp_fraction=0.50),
    )
    assert category == "Ability"
    assert target is cyanis
    assert action.name == "Mend"
    # Gentle Continuance belongs to resolution because it is the first direct
    # healing Ability each round; the base action remains the authored 22%.
    assert action.heal_max_hp_percent == 0.22
