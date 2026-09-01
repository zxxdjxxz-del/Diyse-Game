from __future__ import annotations

import random

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


def test_final_damage_multiplier_applies_after_base_damage() -> None:
    actor = CombatUnit(
        Combatant("Attacker", "party", Stats(100, 0, 100, 0, 50, 50, 20)),
        0,
    )
    target = CombatUnit(
        Combatant("Target", "enemy", Stats(100, 0, 1, 1, 100, 100, 10)),
        1,
    )
    action = CombatAction(
        "Empowered Strike",
        power=100,
        crit_chance=0,
        final_damage_multiplier=1.10,
    )

    damage = resolve_damage(actor, action, target, random.Random(1))

    assert damage == 55
    assert target.hp == 45


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
