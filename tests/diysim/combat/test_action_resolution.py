from __future__ import annotations

import random

import pytest

from tools.diysim.combat import (
    CombatAction,
    Combatant,
    CombatUnit,
    TemporaryModifierSpec,
    effective_status_resistance,
    end_round,
    resolve_damage,
    resolve_heal,
)
from tools.diysim.progression import Stats


def _attacker() -> CombatUnit:
    return CombatUnit(
        Combatant("Attacker", "party", Stats(100, 0, 100, 0, 50, 50, 20)),
        0,
    )


def _target(hp: int = 500) -> CombatUnit:
    return CombatUnit(
        Combatant("Target", "enemy", Stats(hp, 0, 1, 1, 100, 100, 10)),
        1,
    )


def test_final_damage_multiplier_applies_after_base_damage() -> None:
    actor = _attacker()
    target = _target(100)
    action = CombatAction(
        "Empowered Strike",
        power=100,
        crit_chance=0,
        final_damage_multiplier=1.10,
    )

    damage = resolve_damage(actor, action, target, random.Random(1))

    assert damage == 55
    assert target.hp == 45


def test_fixed_multihit_resolves_each_hit_and_returns_total_damage() -> None:
    actor = _attacker()
    target = _target()
    action = CombatAction(
        "Threefold Strike",
        power=100,
        base_hit=100,
        crit_chance=0,
        hit_count=3,
    )

    damage = resolve_damage(actor, action, target, random.Random(1))

    assert damage == 150
    assert target.hp == 350


def test_fixed_multihit_stops_after_target_is_koed() -> None:
    actor = _attacker()
    target = _target(60)
    action = CombatAction(
        "Overkill Sequence",
        power=100,
        base_hit=100,
        crit_chance=0,
        hit_count=3,
    )

    damage = resolve_damage(actor, action, target, random.Random(1))

    # The second 50-damage hit KOs the 10-HP remainder; the third hit never resolves.
    assert damage == 100
    assert target.hp == 0


def test_fixed_multihit_does_not_end_sequence_when_one_hit_misses() -> None:
    class ScriptedRandom(random.Random):
        def __init__(self) -> None:
            super().__init__(0)
            self.hit_rolls = iter((100, 1))

        def randint(self, a: int, b: int) -> int:
            return next(self.hit_rolls)

        def random(self) -> float:
            return 1.0

    actor = _attacker()
    target = _target()
    action = CombatAction(
        "Twofold Test",
        power=100,
        base_hit=50,
        crit_chance=0,
        hit_count=2,
    )

    damage = resolve_damage(actor, action, target, ScriptedRandom())

    assert damage == 50
    assert target.hp == 450


def test_combat_action_rejects_nonpositive_hit_count() -> None:
    with pytest.raises(ValueError, match="hit_count must be at least 1"):
        CombatAction("Invalid Sequence", power=100, hit_count=0)


def test_flat_status_resistance_modifier_uses_numbered_round_duration() -> None:
    actor = CombatUnit(
        Combatant("Warden", "party", Stats(100, 20, 1, 50, 50, 50, 20)),
        0,
    )
    target = CombatUnit(
        Combatant(
            "Ally",
            "party",
            Stats(100, 0, 1, 1, 50, 50, 10),
            status_resistance=5,
        ),
        1,
    )
    target.hp = 50
    action = CombatAction(
        "Ward",
        action_kind="heal",
        target_side="ally",
        heal_max_hp_percent=0.05,
        temporary_modifiers=(
            TemporaryModifierSpec("ward_sr", duration_rounds=2, status_resistance_flat=5),
        ),
    )

    resolve_heal(actor, action, target)
    assert target.hp == 55
    assert effective_status_resistance(target) == 10

    end_round((actor, target))
    assert effective_status_resistance(target) == 10

    end_round((actor, target))
    assert effective_status_resistance(target) == 5
