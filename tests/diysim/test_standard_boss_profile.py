from tools.diysim.overlays import (
    STANDARD_BOSS_OFFENSIVE_LEVEL_OFFSET,
    STANDARD_BOSS_POWER_MULTIPLIER,
    standard_boss_test_overlay,
)


def test_standard_boss_profile_is_offense_only_plus5_and_power_x1_20():
    overlay = standard_boss_test_overlay()
    assert STANDARD_BOSS_POWER_MULTIPLIER == 1.20
    assert STANDARD_BOSS_OFFENSIVE_LEVEL_OFFSET == 5
    assert overlay.direct_damage_power_multiplier == 1.20
    assert overlay.offensive_stat_level_offset == 5
    assert overlay.defensive_stat_level_offset == 0
    assert overlay.speed_stat_level_offset == 0
    assert overlay.effective_stat_level_offset == 0
