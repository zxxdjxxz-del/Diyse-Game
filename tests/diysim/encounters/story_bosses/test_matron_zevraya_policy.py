from tools.diysim.encounters.story_bosses.matron_zevraya import load_zevraya_party_actions


def test_zevraya_party_actions_use_current_cl9_package() -> None:
    actions = load_zevraya_party_actions()

    assert actions.crest_rend.power == 240
    assert actions.crest_rend.damage_kind == "hybrid"
    assert actions.crest_rend.physical_weight == 0.75
    assert actions.crest_rend.magical_weight == 0.25
    assert actions.crest_rend.defense_penetration == 0.30
    assert actions.crest_rend.spirit_penetration == 0.30

    assert actions.mend.mp_cost == 14
    assert actions.revive_mp_cost == 29
    assert actions.revive_fraction == 0.45
    assert actions.lifeline_mp_cost == 34

    assert actions.sizing_shot.power == 155
    assert actions.colossus_draw.power == 265
    assert actions.measured_colossus_penetration == 0.35
    assert actions.hunter_measure_full_rounds == 2
    assert actions.hunter_measure_party_crit_bonus == 10
    assert actions.hunter_measure_torren_crit_bonus == 5

    assert actions.prism_lance.power == 220
    assert actions.prism_lance.element == "earth"
    assert actions.spectrum_cascade.power == 190
    assert actions.spectrum_cascade.target_scope == "all"
    assert actions.elemental_round_discount == 2
