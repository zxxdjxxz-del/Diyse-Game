from __future__ import annotations

from tools.diysim.combat.damage import direct_damage
from tools.diysim.encounters.story_bosses.first_command_warden import (
    load_first_command_warden_party_snapshot,
)


def test_warden_v105_lv11_same_gear_party_body() -> None:
    snapshot = load_first_command_warden_party_snapshot(11)
    party = {unit.name: unit for unit in snapshot.party}

    assert tuple(party) == ("Cyanis", "Ilyra", "Torren", "Nimera")
    assert party["Cyanis"].stats.as_dict() == {
        "hp": 617, "mp": 56, "attack": 84, "magic": 69,
        "defense": 81, "spirit": 65, "speed": 26,
    }
    assert party["Ilyra"].stats.as_dict() == {
        "hp": 588, "mp": 70, "attack": 68, "magic": 86,
        "defense": 51, "spirit": 78, "speed": 27,
    }
    assert party["Torren"].stats.as_dict() == {
        "hp": 588, "mp": 59, "attack": 93, "magic": 32,
        "defense": 56, "spirit": 48, "speed": 27,
    }
    assert party["Nimera"].stats.as_dict() == {
        "hp": 517, "mp": 72, "attack": 61, "magic": 77,
        "defense": 47, "spirit": 58, "speed": 32,
    }
    assert all(unit.evasion == 0 and unit.status_resistance == 0 for unit in party.values())


def test_warden_v105_lv13_uses_identical_gear_with_only_level_growth() -> None:
    lv11 = load_first_command_warden_party_snapshot(11)
    lv13 = load_first_command_warden_party_snapshot(13)
    low = {unit.name: unit for unit in lv11.party}
    high = {unit.name: unit for unit in lv13.party}

    assert lv11.equipment == lv13.equipment
    assert high["Cyanis"].stats.as_dict() == {
        "hp": 702, "mp": 63, "attack": 89, "magic": 74,
        "defense": 85, "spirit": 68, "speed": 27,
    }
    assert high["Ilyra"].stats.as_dict() == {
        "hp": 668, "mp": 78, "attack": 72, "magic": 91,
        "defense": 55, "spirit": 82, "speed": 28,
    }
    assert high["Torren"].stats.as_dict() == {
        "hp": 668, "mp": 66, "attack": 98, "magic": 36,
        "defense": 59, "spirit": 52, "speed": 28,
    }
    assert high["Nimera"].stats.as_dict() == {
        "hp": 588, "mp": 80, "attack": 65, "magic": 82,
        "defense": 50, "spirit": 61, "speed": 33,
    }
    assert high["Cyanis"].stats.attack > low["Cyanis"].stats.attack
    assert high["Nimera"].stats.hp > low["Nimera"].stats.hp


def _representative_raw_round(level: int) -> int:
    party = {unit.name: unit for unit in load_first_command_warden_party_snapshot(level).party}
    # Conservative direct-damage package used to cross-check the Chapter-3
    # ~342/~370 serious-round estimates: Crest Strike, Warden's Valor,
    # Cinder Shot, and Weave Burst against Warden 43 DEF / 43 Spirit.
    return sum((
        direct_damage("physical", attack=party["Cyanis"].stats.attack, magic=party["Cyanis"].stats.magic,
                      defense=43, spirit=43, power=140),
        direct_damage("magical", attack=party["Ilyra"].stats.attack, magic=party["Ilyra"].stats.magic,
                      defense=43, spirit=43, power=170),
        direct_damage("physical", attack=party["Torren"].stats.attack, magic=party["Torren"].stats.magic,
                      defense=43, spirit=43, power=155),
        direct_damage("magical", attack=party["Nimera"].stats.attack, magic=party["Nimera"].stats.magic,
                      defense=43, spirit=43, power=130),
    ))


def test_warden_reconstructed_bodies_match_ch3_serious_round_anchor() -> None:
    # The source report calls these approximate raw serious-round values.
    # No-crit deterministic damage should land close and preserve the level gap.
    lv11 = _representative_raw_round(11)
    lv13 = _representative_raw_round(13)
    assert lv11 == 338
    assert lv13 == 365
    assert 330 <= lv11 <= 350
    assert 355 <= lv13 <= 380
    assert lv13 > lv11


def test_warden_snapshot_rejects_levels_outside_v105_pair() -> None:
    try:
        load_first_command_warden_party_snapshot(12)
    except ValueError:
        pass
    else:
        raise AssertionError("v105 isolation snapshot should only expose Lv11 and Lv13")
