from __future__ import annotations

import random

from tools.diysim.combat import CombatAction, Combatant, CombatUnit, resolve_damage
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
