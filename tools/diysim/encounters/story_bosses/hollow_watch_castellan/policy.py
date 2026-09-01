"""Player-policy reconstruction for the Hollow Watch regression.

The v93 report specifies policy priorities but does not preserve the exact HP
threshold used by its test harness. The threshold below is therefore explicitly
a regression-policy parameter, not Diyse combat canon.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from typing import Mapping

from tools.diysim.combat.models import BASIC_ATTACK, CombatAction, CombatUnit

from .data import HollowWatchActions


@dataclass(frozen=True)
class SmartPolicyConfig:
    heal_trigger_hp_fraction: float = 0.55
    clear_round_start_harmful_status: bool = True

    def __post_init__(self) -> None:
        if not 0.0 <= self.heal_trigger_hp_fraction <= 1.0:
            raise ValueError("heal_trigger_hp_fraction must be between 0 and 1")


@dataclass(frozen=True)
class RoundStartView:
    hp: Mapping[str, int]
    statuses: Mapping[str, frozenset[str]]

    @classmethod
    def capture(cls, party: list[CombatUnit]) -> "RoundStartView":
        return cls(
            hp={unit.template.name: unit.hp for unit in party},
            statuses={unit.template.name: frozenset(unit.statuses) for unit in party},
        )

    def hp_fraction(self, unit: CombatUnit) -> float:
        return self.hp[unit.template.name] / unit.max_hp


def choose_cyanis_action(
    actor: CombatUnit,
    actions: HollowWatchActions,
    *,
    ballista_alive: bool,
    harmonized_prime: str | None,
) -> CombatAction:
    if ballista_alive and actor.mp >= actions.crest_strike.mp_cost:
        return actions.crest_strike

    if harmonized_prime == "magical" and actor.mp >= actions.resonant_pulse.mp_cost:
        return replace(actions.resonant_pulse, final_damage_multiplier=1.10)
    if harmonized_prime == "physical" and actor.mp >= actions.crest_strike.mp_cost:
        return replace(actions.crest_strike, final_damage_multiplier=1.10)

    if actor.mp >= actions.crest_strike.mp_cost:
        return actions.crest_strike
    if actor.mp >= actions.resonant_pulse.mp_cost:
        return actions.resonant_pulse
    return BASIC_ATTACK


def next_harmonized_prime(action: CombatAction) -> str | None:
    """Return the opposite-side prime established by a Crest Knight Ability."""
    if action.name == "Crest Strike":
        return "magical"
    if action.name == "Resonant Pulse":
        return "physical"
    return None


def choose_maevra_action(actor: CombatUnit, actions: HollowWatchActions) -> CombatAction:
    if actor.mp >= actions.linebreaker_thrust.mp_cost:
        return actions.linebreaker_thrust
    return BASIC_ATTACK


def choose_ilyra_action(
    actor: CombatUnit,
    party: list[CombatUnit],
    actions: HollowWatchActions,
    round_start: RoundStartView,
    *,
    ballista_alive: bool,
    config: SmartPolicyConfig,
) -> tuple[CombatAction, CombatUnit | None]:
    if ballista_alive:
        return BASIC_ATTACK, None

    alive = [unit for unit in party if unit.alive]
    if config.clear_round_start_harmful_status and actor.mp >= actions.clear_warding.mp_cost:
        afflicted = [
            unit
            for unit in alive
            if round_start.statuses.get(unit.template.name, frozenset())
        ]
        if afflicted:
            target = min(afflicted, key=round_start.hp_fraction)
            return actions.clear_warding, target

    if actor.mp >= actions.mend.mp_cost:
        low = [
            unit
            for unit in alive
            if round_start.hp_fraction(unit) <= config.heal_trigger_hp_fraction
        ]
        if low:
            target = min(low, key=round_start.hp_fraction)
            return actions.mend, target

    return BASIC_ATTACK, None


__all__ = [
    "RoundStartView",
    "SmartPolicyConfig",
    "choose_cyanis_action",
    "choose_ilyra_action",
    "choose_maevra_action",
    "next_harmonized_prime",
]
