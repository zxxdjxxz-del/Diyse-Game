"""Compatibility facade for the sectioned Diyse simulator.

Canon data is loaded from repository owner files; this facade exports functions,
not copied rule tables/constants.
"""

from .common import round_half_up
from .combat.criticals import base_crit_chance, crit_chance_cap, crit_multiplier
from .combat.damage import direct_damage, magical_damage, physical_damage
from .combat.hit_evasion import adjusted_hit_chance
from .combat.models import DamageKind, Side
from .combat.simple_runtime import (
    ActionProfile,
    BattleOutcome,
    BattleScenario,
    BattleUnit,
    CombatantTemplate,
    SimulationSummary,
    TargetPolicy,
    run_battle,
    simulate,
)
from .overlays.sweeps import scale_enemy_side, sweep_enemy_stats
from .progression.player_exp import cumulative_exp, exp_to_next_level, level_from_exp, level_up_cost, round_nearest_100
from .progression.stats import STAT_KEYS, Stats, class_multipliers, level_cap, natural_stats, neutral_natural_stats
from .sources.combat import load_combat_rules

__all__ = [
    "ActionProfile", "BattleOutcome", "BattleScenario", "BattleUnit", "CombatantTemplate",
    "DamageKind", "STAT_KEYS", "Side", "SimulationSummary", "Stats", "TargetPolicy",
    "adjusted_hit_chance", "base_crit_chance", "class_multipliers", "crit_chance_cap",
    "crit_multiplier", "cumulative_exp", "direct_damage", "exp_to_next_level",
    "level_cap", "level_from_exp", "level_up_cost", "load_combat_rules",
    "magical_damage", "natural_stats", "neutral_natural_stats", "physical_damage",
    "round_half_up", "round_nearest_100", "run_battle", "scale_enemy_side",
    "simulate", "sweep_enemy_stats",
]
