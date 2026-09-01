from __future__ import annotations

import pytest

from tools.diysim.combat import CombatAction, Combatant
from tools.diysim.overlays import (
    BalanceOverlay,
    apply_enemy_balance_overlay,
    scale_direct_damage_power,
    scale_effective_core_stat_level,
)
from tools.diysim.progression import Stats


def _warden() -> Combatant:
    return Combatant(
        "First Command Warden",
        "enemy",
        Stats(2850, 0, 72, 72, 43, 43, 30),
        actions=(
            CombatAction("Authority Lance", damage_kind="physical", power=190, base_hit=100),
            CombatAction("Judgment Pulse", damage_kind="magical", power=140, base_hit=100, target_scope="all"),
            CombatAction("Command Seal", action_kind="heal", target_side="self"),
        ),
        evasion=0,
        status_resistance=10,
        rank="major_boss",
    )


def test_power_overlay_scales_direct_damage_only() -> None:
    damage = CombatAction("Hit", power=165, base_hit=100)
    support = CombatAction("Support", action_kind="heal", target_side="self")

    scaled_damage = scale_direct_damage_power(damage, 1.20)
    scaled_support = scale_direct_damage_power(support, 1.20)

    assert scaled_damage.power == pytest.approx(198.0)
    assert scaled_damage.base_hit == 100
    assert scaled_support is support
    assert damage.power == 165


def test_v106_plus5_matches_first_command_warden_reference_line() -> None:
    owner = _warden()
    scaled = scale_effective_core_stat_level(
        owner.stats,
        displayed_level=14,
        level_offset=5,
    )

    assert scaled.hp == 2850
    assert scaled.mp == 0
    assert scaled.attack == 90
    assert scaled.magic == 90
    assert scaled.defense == 53
    assert scaled.spirit == 53
    assert scaled.speed == 33
    assert owner.stats.attack == 72


def test_combined_overlay_is_non_destructive_and_preserves_non_target_fields() -> None:
    owner = _warden()
    overlay = BalanceOverlay(
        direct_damage_power_multiplier=1.20,
        effective_stat_level_offset=5,
    )
    candidate = apply_enemy_balance_overlay(
        owner,
        overlay=overlay,
        displayed_level=14,
    )

    assert candidate is not owner
    assert candidate.stats.hp == owner.stats.hp == 2850
    assert candidate.stats.attack == 90
    assert candidate.stats.magic == 90
    assert candidate.stats.defense == 53
    assert candidate.stats.spirit == 53
    assert candidate.stats.speed == 33
    assert candidate.evasion == owner.evasion == 0
    assert candidate.status_resistance == owner.status_resistance == 10
    assert candidate.actions[0].power == pytest.approx(228.0)
    assert candidate.actions[1].power == pytest.approx(168.0)
    assert candidate.actions[2] is owner.actions[2]

    assert owner.stats.attack == 72
    assert owner.actions[0].power == 190
    assert owner.actions[1].power == 140


def test_overlay_requires_enemy_and_displayed_level_when_needed() -> None:
    party = Combatant("Party", "party", Stats(100, 20, 20, 20, 20, 20, 20))
    with pytest.raises(ValueError):
        apply_enemy_balance_overlay(party, overlay=BalanceOverlay())

    with pytest.raises(ValueError):
        apply_enemy_balance_overlay(
            _warden(),
            overlay=BalanceOverlay(effective_stat_level_offset=5),
        )

    with pytest.raises(ValueError):
        BalanceOverlay(direct_damage_power_multiplier=0)
