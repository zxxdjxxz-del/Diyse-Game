"""Compatibility facade for the sectioned Diyse simulator.

Canon data is loaded from repository owner files; this facade exports functions,
not copied rule tables/constants.
"""

from .common import round_half_up
from .combat.criticals import BASE_CRIT_CHANCE, CRIT_CHANCE_CAP, CRIT_MULTIPLIER
from .combat.damage import PENETRATION_CAP, direct_damage, magical_damage, physical_damage
from .combat.hit_evasion import MAX_HIT_CHANCE, MIN_HIT_CHANCE, adjusted_hit_chance
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
from .progression.player_exp import (
    cumulative_exp,
    exp_to_next_level,
    level_from_exp,
    level_up_cost,
    round_nearest_100,
)
from .progression.stats import (
    STAT_KEYS,
    Stats,
    class_multipliers,
    level_cap,
    natural_stats,
    neutral_natural_stats,
)

__all__ = [
    "ActionProfile",
    "BASE_CRIT_CHANCE",
    "BattleOutcome",
    "BattleScenario",
    "BattleUnit",
    "CRIT_CHANCE_CAP",
    "CRIT_MULTIPLIER",
    "CombatantTemplate",
    "DamageKind",
    "MAX_HIT_CHANCE",
    "MIN_HIT_CHANCE",
    "PENETRATION_CAP",
    "STAT_KEYS",
    "Side",
    "SimulationSummary",
    "Stats",
    "TargetPolicy",
    "adjusted_hit_chance",
    "class_multipliers",
    "cumulative_exp",
    "direct_damage",
    "exp_to_next_level",
    "level_cap",
    "level_from_exp",
    "level_up_cost",
    "magical_damage",
    "natural_stats",
    "neutral_natural_stats",
    "physical_damage",
    "round_half_up",
    "round_nearest_100",
    "run_battle",
    "scale_enemy_side",
    "simulate",
    "sweep_enemy_stats",
]
