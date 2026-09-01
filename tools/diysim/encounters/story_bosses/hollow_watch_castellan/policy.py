"""Player-policy logic for Hollow Watch.

Policy thresholds are simulator/test configuration. All Diyse combat values are
provided by repo-backed sources at runtime.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from typing import Mapping

from tools.diysim.combat.basic_attack import basic_attack_action
from tools.diysim.combat.models import CombatAction, CombatUnit
from .repo_loader import HollowWatchRepoData


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
    data: HollowWatchRepoData,
    *,
    ballista_alive: bool,
    harmonized_prime: str | None,
) -> CombatAction:
    if ballista_alive and actor.mp >= data.crest_strike.mp_cost:
        return data.crest_strike

    if harmonized_prime == "magical" and actor.mp >= data.resonant_pulse.mp_cost:
        return replace(data.resonant_pulse, final_damage_multiplier=data.harmonized_rank1_multiplier)
    if harmonized_prime == "physical" and actor.mp >= data.crest_strike.mp_cost:
        return replace(data.crest_strike, final_damage_multiplier=data.harmonized_rank1_multiplier)

    if actor.mp >= data.crest_strike.mp_cost:
        return data.crest_strike
    if actor.mp >= data.resonant_pulse.mp_cost:
        return data.resonant_pulse
    return basic_attack_action()


def next_harmonized_prime(action: CombatAction) -> str | None:
    if action.damage_kind == "physical" and action.name != "Attack":
        return "magical"
    if action.damage_kind == "magical":
        return "physical"
    return None


def choose_maevra_action(actor: CombatUnit, data: HollowWatchRepoData) -> CombatAction:
    if actor.mp >= data.linebreaker_thrust.mp_cost:
        return data.linebreaker_thrust
    return basic_attack_action()


def choose_ilyra_action(
    actor: CombatUnit,
    party: list[CombatUnit],
    data: HollowWatchRepoData,
    round_start: RoundStartView,
    *,
    ballista_alive: bool,
    config: SmartPolicyConfig,
) -> tuple[CombatAction, CombatUnit | None]:
    if ballista_alive:
        return basic_attack_action(), None

    alive = [unit for unit in party if unit.alive]
    if config.clear_round_start_harmful_status and actor.mp >= data.clear_warding.mp_cost:
        afflicted = [
            unit
            for unit in alive
            if round_start.statuses.get(unit.template.name, frozenset())
        ]
        if afflicted:
            target = min(afflicted, key=round_start.hp_fraction)
            return data.clear_warding, target

    if actor.mp >= data.mend.mp_cost:
        low = [
            unit
            for unit in alive
            if round_start.hp_fraction(unit) <= config.heal_trigger_hp_fraction
        ]
        if low:
            target = min(low, key=round_start.hp_fraction)
            return data.mend, target

    return basic_attack_action(), None


__all__ = [
    "RoundStartView",
    "SmartPolicyConfig",
    "choose_cyanis_action",
    "choose_ilyra_action",
    "choose_maevra_action",
    "next_harmonized_prime",
]
