from tools.diysim.encounters.story_bosses.matron_zevraya.repo_loader import load_zevraya_repo_data
from tools.diysim.encounters.story_bosses.matron_zevraya.split_stats import apply_zevraya_split_stat_overlay
from tools.diysim.overlays import BalanceOverlay


def test_zevraya_offense_split_does_not_raise_defense_spirit_or_speed() -> None:
    owner = load_zevraya_repo_data()
    scaled = apply_zevraya_split_stat_overlay(
        owner,
        BalanceOverlay(offensive_stat_level_offset=5),
    )

    for before, after in (
        (owner.blood_matron.stats, scaled.blood_matron.stats),
        (owner.perfected_war_mother.stats, scaled.perfected_war_mother.stats),
    ):
        assert after.attack > before.attack
        assert after.magic > before.magic
        assert after.defense == before.defense
        assert after.spirit == before.spirit
        assert after.speed == before.speed
        assert after.hp == before.hp
        assert after.mp == before.mp


def test_zevraya_defense_and_speed_splits_are_independent() -> None:
    owner = load_zevraya_repo_data()
    defense_scaled = apply_zevraya_split_stat_overlay(
        owner,
        BalanceOverlay(defensive_stat_level_offset=5),
    )
    speed_scaled = apply_zevraya_split_stat_overlay(
        owner,
        BalanceOverlay(speed_stat_level_offset=5),
    )

    assert defense_scaled.blood_matron.stats.defense > owner.blood_matron.stats.defense
    assert defense_scaled.blood_matron.stats.spirit > owner.blood_matron.stats.spirit
    assert defense_scaled.blood_matron.stats.attack == owner.blood_matron.stats.attack
    assert defense_scaled.blood_matron.stats.speed == owner.blood_matron.stats.speed

    assert speed_scaled.blood_matron.stats.speed > owner.blood_matron.stats.speed
    assert speed_scaled.blood_matron.stats.attack == owner.blood_matron.stats.attack
    assert speed_scaled.blood_matron.stats.defense == owner.blood_matron.stats.defense
