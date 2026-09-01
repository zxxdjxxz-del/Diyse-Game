from tools.diysim.encounters.story_bosses.matron_zevraya import (
    load_zevraya_party_snapshot,
    load_zevraya_repo_data,
)


def test_zevraya_v105_snapshots_use_same_active_four_and_gear() -> None:
    lv24 = load_zevraya_party_snapshot(24)
    lv28 = load_zevraya_party_snapshot(28)

    assert tuple(unit.name for unit in lv24.party) == ("Cyanis", "Ilyra", "Torren", "Vaelira")
    assert tuple(unit.name for unit in lv28.party) == tuple(unit.name for unit in lv24.party)
    assert lv24.equipment == lv28.equipment
    assert lv24.equipment["Cyanis"] == ("Deepforge Blade", "Caeloran Plate", "Yahtrean Shield")
    assert lv24.equipment["Ilyra"] == ("Crucible Wardrod", "Warden Fieldmail", "Warding Focus")
    assert lv24.equipment["Torren"] == ("Command War Bow", "Annex Guard Mail")
    assert lv24.equipment["Vaelira"] == ("Arcanist Staff", "Green Arcanist Garb")

    by_name_24 = {unit.name: unit for unit in lv24.party}
    by_name_28 = {unit.name: unit for unit in lv28.party}
    for name in by_name_24:
        assert by_name_28[name].stats.hp > by_name_24[name].stats.hp
        assert by_name_28[name].stats.defense >= by_name_24[name].stats.defense
        assert by_name_28[name].stats.spirit >= by_name_24[name].stats.spirit


def test_zevraya_owner_package_is_complete_and_repo_backed() -> None:
    data = load_zevraya_repo_data()

    assert data.blood_matron.stats.hp == 4400
    assert data.perfected_war_mother.stats.hp == 5200
    assert data.crimson_trigger_fraction == 0.45
    assert set(data.reservoirs) == {"Sustenance", "Armor", "Brood", "Conduction"}
    assert data.reservoirs["Sustenance"].hp == 320
    assert data.reservoirs["Armor"].defense == 64
    assert data.reservoirs["Conduction"].spirit == 66

    assert [action.name for action in data.form1_core_actions] == [
        "Ritual Incision",
        "Alteration Lance",
        "Surgical Sweep",
        "Ruin Infusion",
    ]
    assert data.crimson_arc.power == 165
    assert [action.name for action in data.form2_core_actions] == [
        "Perfected Tearing Blade",
        "Ruin Scythe",
        "Warbody Crush",
        "Perfected Ruin Wave",
    ]

    assert data.sustenance_draw.heal_from_actual_damage_fraction == 0.35
    assert data.perfected_siphon.heal_from_actual_damage_fraction == 0.40
    assert data.perfected_siphon.successful_use_cap == 2
    assert data.armor_plating.defense_bonus == 0.15
    assert data.warbody_plating.spirit_bonus == 0.15
    assert data.controlled_reconstruction.heal_amount == 240
    assert data.controlled_reconstruction.successful_use_cap == 1

    assert data.weather_conduction.cycle == ("gale", "storm", "frost")
    assert data.weather_conduction.power == 200
    assert data.weather_conduction.stun_chance == 15
    assert data.weather_conduction.freeze_chance == 20
    assert data.perfected_conduction.power == 230

    assert data.brood_organism.hp == 260
    assert data.brood_organism.action.power == 155
    assert data.perfected_brood_organism.hp == 320
    assert data.perfected_brood_organism.action.power == 175
    assert data.non_diluting_candidate_documented is True
