"""Sectioned combat primitives for the Diyse balance simulator."""

from ..sources.combat import CombatRules, load_combat_rules
from .action_resolution import resolve_damage, resolve_heal
from .action_selection import selectable_actions
from .advanced_runtime import (
    AdvancedBattleOutcome,
    AdvancedBattleScenario,
    AdvancedSimulationSummary,
    run_advanced_battle,
    simulate_advanced,
)
from .criticals import base_crit_chance, crit_chance_cap, crit_multiplier
from .damage import direct_damage, magical_damage, physical_damage
from .derived_stats import effective_attack, effective_defense, effective_magic, effective_speed, effective_spirit
from .elements import affinity_damage_multiplier, element_affinity, linked_status_affinity_modifier
from .healing import healing_amount
from .hit_evasion import adjusted_hit_chance
from .models import (
    BASIC_ATTACK,
    ActionKind,
    ActiveStatus,
    ActiveTemporaryModifier,
    Affinity,
    CombatAction,
    CombatUnit,
    Combatant,
    DamageKind,
    Element,
    Rank,
    Side,
    StatusName,
    StatusRider,
    TargetScope,
    TargetSide,
    TemporaryModifierSpec,
)
from .mp import resolve_mp_cost
from .simple_runtime import ActionProfile, BattleOutcome, BattleScenario, CombatantTemplate, SimulationSummary, run_battle, simulate
from .status_runtime import bleed_rate, clear_bleed_if_full, complete_turn, end_round, turn_is_blocked
from .statuses import apply_status, status_application_chance
from .temporary_modifiers import apply_temporary_modifier, effective_status_resistance, tick_temporary_modifiers
from .turn_order import turn_order

__all__ = [
    "ActionKind", "ActionProfile", "ActiveStatus", "ActiveTemporaryModifier",
    "AdvancedBattleOutcome", "AdvancedBattleScenario", "AdvancedSimulationSummary",
    "Affinity", "BASIC_ATTACK", "BattleOutcome", "BattleScenario", "CombatAction",
    "CombatRules", "CombatUnit", "Combatant", "CombatantTemplate", "DamageKind",
    "Element", "Rank", "Side", "SimulationSummary", "StatusName", "StatusRider",
    "TargetScope", "TargetSide", "TemporaryModifierSpec", "adjusted_hit_chance",
    "affinity_damage_multiplier", "apply_status", "apply_temporary_modifier",
    "base_crit_chance", "bleed_rate", "clear_bleed_if_full", "complete_turn",
    "crit_chance_cap", "crit_multiplier", "direct_damage", "effective_attack",
    "effective_defense", "effective_magic", "effective_speed", "effective_spirit",
    "effective_status_resistance", "element_affinity", "end_round", "healing_amount",
    "linked_status_affinity_modifier", "load_combat_rules", "magical_damage",
    "physical_damage", "resolve_damage", "resolve_heal", "resolve_mp_cost",
    "run_advanced_battle", "run_battle", "selectable_actions", "simulate",
    "simulate_advanced", "status_application_chance", "tick_temporary_modifiers",
    "turn_is_blocked", "turn_order",
]
