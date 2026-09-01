"""Compatibility facade for the sectioned advanced battle runtime."""

from .combat.advanced_runtime import (
    AdvancedBattleOutcome,
    AdvancedBattleScenario,
    AdvancedSimulationSummary,
    bleed_rate,
    clear_bleed_if_full,
    complete_turn,
    end_round,
    resolve_damage,
    resolve_heal,
    run_advanced_battle,
    selectable_actions,
    simulate_advanced,
    turn_is_blocked,
    turn_order,
)

__all__ = [
    "AdvancedBattleOutcome",
    "AdvancedBattleScenario",
    "AdvancedSimulationSummary",
    "bleed_rate",
    "clear_bleed_if_full",
    "complete_turn",
    "end_round",
    "resolve_damage",
    "resolve_heal",
    "run_advanced_battle",
    "selectable_actions",
    "simulate_advanced",
    "turn_is_blocked",
    "turn_order",
]
