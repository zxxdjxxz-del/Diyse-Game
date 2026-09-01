"""Source-backed authored data for the Hollow Watch Castellan regression.

This module intentionally contains no battle-loop policy. It owns only the
combat bodies and action definitions required by this encounter.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Literal

from tools.diysim.combat.models import (
    CombatAction,
    Combatant,
    StatusRider,
    TemporaryModifierSpec,
)
from tools.diysim.progression import Stats

Ruleset = Literal["v93_oracle", "current"]


@dataclass(frozen=True)
class HollowWatchActions:
    crest_strike: CombatAction
    resonant_pulse: CombatAction
    mend: CombatAction
    clear_warding: CombatAction
    linebreaker_thrust: CombatAction


def action_set(ruleset: Ruleset) -> HollowWatchActions:
    """Return the same authored actions with ruleset-appropriate MP costs.

    v93_oracle preserves the certified pre-global-reduction costs used by the
    historical true-battle result. current uses the later approved 15% Ability
    MP reduction already written into the current class sheets.
    """
    if ruleset == "v93_oracle":
        crest_cost, pulse_cost, mend_cost, clear_cost = 10, 12, 16, 18
    elif ruleset == "current":
        crest_cost, pulse_cost, mend_cost, clear_cost = 9, 10, 14, 15
    else:
        raise ValueError(f"unknown Hollow Watch ruleset: {ruleset}")

    return HollowWatchActions(
        crest_strike=CombatAction(
            "Crest Strike",
            mp_cost=crest_cost,
            damage_kind="physical",
            element="neutral",
            power=140,
            base_hit=100,
        ),
        resonant_pulse=CombatAction(
            "Resonant Pulse",
            mp_cost=pulse_cost,
            damage_kind="magical",
            element="colorless",
            power=150,
            base_hit=100,
        ),
        mend=CombatAction(
            "Mend",
            action_kind="heal",
            mp_cost=mend_cost,
            target_side="ally",
            heal_max_hp_percent=0.22,
            heal_magic_scaling=1.50,
        ),
        clear_warding=CombatAction(
            "Clear Warding",
            action_kind="heal",
            mp_cost=clear_cost,
            target_side="ally",
            heal_max_hp_percent=0.05,
            clear_harmful_statuses=1,
            temporary_modifiers=(
                TemporaryModifierSpec(
                    "clear_warding_status_resistance",
                    duration_rounds=2,
                    status_resistance_flat=5,
                ),
            ),
        ),
        linebreaker_thrust=CombatAction(
            "Linebreaker Thrust",
            mp_cost=10,
            damage_kind="physical",
            element="neutral",
            power=165,
            base_hit=100,
            defense_penetration=0.15,
        ),
    )


CYANIS = Combatant(
    "Cyanis",
    "party",
    Stats(267, 28, 59, 47, 63, 49, 22),
    evasion=0,
    status_resistance=0,
)

ILYRA = Combatant(
    "Ilyra",
    "party",
    Stats(254, 35, 47, 61, 35, 60, 22),
    evasion=0,
    status_resistance=0,
)

MAEVRA = Combatant(
    "Maevra",
    "party",
    Stats(267, 27, 40, 16, 28, 27, 23),
    evasion=5,
    status_resistance=5,
)

CASTELLAN = Combatant(
    "Hollow Watch Castellan",
    "enemy",
    Stats(450, 0, 42, 27, 27, 24, 25),
    evasion=0,
    status_resistance=5,
    rank="major_boss",
)

BALLISTA = Combatant(
    "Fortress Ballista",
    "enemy",
    Stats(120, 0, 55, 0, 20, 18, 24),
)

WATCH_SEAL = Combatant(
    "Watch Seal",
    "enemy",
    Stats(100, 0, 0, 0, 22, 28, 0),
)

FORTRESS_ACTIONS = (
    CombatAction(
        "Wallbound Strike",
        damage_kind="physical",
        element="neutral",
        power=175,
        base_hit=100,
        weight=65,
    ),
    CombatAction(
        "Bastion Sweep",
        target_scope="all",
        damage_kind="physical",
        element="neutral",
        power=135,
        base_hit=95,
        weight=35,
    ),
)

WALKING_ACTIONS = (
    CombatAction(
        "Fortress Slam",
        damage_kind="physical",
        element="neutral",
        power=220,
        base_hit=95,
        weight=40,
        status_riders=(StatusRider("staggered", 20),),
    ),
    CombatAction(
        "Iron Pursuit",
        damage_kind="physical",
        element="neutral",
        power=180,
        base_hit=100,
        weight=40,
    ),
    CombatAction(
        "Wall-Shear Sweep",
        target_scope="all",
        damage_kind="physical",
        element="neutral",
        power=145,
        base_hit=95,
        weight=20,
    ),
)

HEAVY_BOLT = CombatAction(
    "Fire Heavy Bolt",
    damage_kind="physical",
    element="neutral",
    power=230,
    base_hit=95,
    status_riders=(StatusRider("bleed", 20),),
)

WALKING_TRIGGER_HP = 247
WATCH_SEAL_DIRECT_DAMAGE_REDUCTION = 0.10
REPETITION_LOCKED_BOSS_ACTIONS = frozenset({"Bastion Sweep", "Fortress Slam", "Wall-Shear Sweep"})

__all__ = [
    "BALLISTA",
    "CASTELLAN",
    "CYANIS",
    "FORTRESS_ACTIONS",
    "HEAVY_BOLT",
    "HollowWatchActions",
    "ILYRA",
    "MAEVRA",
    "REPETITION_LOCKED_BOSS_ACTIONS",
    "Ruleset",
    "WALKING_ACTIONS",
    "WALKING_TRIGGER_HP",
    "WATCH_SEAL",
    "WATCH_SEAL_DIRECT_DAMAGE_REDUCTION",
    "action_set",
]
