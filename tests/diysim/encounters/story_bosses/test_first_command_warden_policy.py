from __future__ import annotations

from tools.diysim.combat.models import CombatUnit
from tools.diysim.encounters.story_bosses.first_command_warden.policy import (
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
    assert actions.wardens_valor.power == 170
    assert actions.cinder_shot.power == 155
    assert actions.weave_burst.power == 130
    assert actions.mend.heal_max_hp_percent == 0.22
    assert actions.mend.healing_potency == 1.10
    assert actions.gentle_continuance_bonus == 0.05


def test_gentle_continuance_applies_only_below_half_hp() -> None:
    party = _party()
    ilyra = next(unit for unit in party if unit.template.name == "Ilyra")
    cyanis = next(unit for unit in party if unit.template.name == "Cyanis")
    actions = load_warden_party_actions()

    cyanis.hp = int(cyanis.max_hp * 0.40)
    category, action, target = choose_player_action(
        ilyra,
        party,
        actions,
        sealed_category=None,
        config=WardenPolicyConfig(mend_below_hp_fraction=0.60),
    )
    assert category == "Ability"
    assert target is cyanis
    assert action.name == "Mend"
    assert action.heal_max_hp_percent == 0.27

    cyanis.hp = int(cyanis.max_hp * 0.55)
    category, action, target = choose_player_action(
        ilyra,
        party,
        actions,
        sealed_category=None,
        config=WardenPolicyConfig(mend_below_hp_fraction=0.60),
    )
    assert category == "Ability"
    assert target is cyanis
    assert action.name == "Mend"
    assert action.heal_max_hp_percent == 0.22
