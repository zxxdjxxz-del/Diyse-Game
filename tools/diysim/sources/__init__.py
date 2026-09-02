"""Repository-backed source access for diysim.

Diyse canon belongs to the repository, never to simulator-owned snapshots.
"""

from .abilities import AbilityRegistryEntry, AbilitySource, load_ability_registry, load_ability_source
from .actions import AuthoredActionSource, find_named_action_line, load_named_action_source, parse_authored_action_text
from .actors import EnemyRegistryEntry, StatBlockSource, find_enemy_registry_entries, load_enemy_registry, load_stat_row, load_stat_table, parse_stat_row
from .analogues import FunctionalAnalogueRuleSource, parse_functional_analogue_rule_text
from .audit import SourceAuditIssue, SourceAuditReport, audit_repo_sources
from .class_equipment_access import (
    DonorEquipmentAccessSource,
    load_character_donor_equipment_access,
    load_donor_equipment_access,
)
from .class_exp import (
    CAMPAIGN_CEXP_BUDGETS_PATH,
    CLASS_CEXP_CAP,
    CLASS_EXP_CEXP_PATH,
    CLASS_LEVEL_CAP,
    CLASS_RECRUITMENT_CEXP_PATH,
    CampaignCexpBudgetSource,
    CharacterStartingCexpSource,
    Chapter13CexpSplitSource,
    ClassLevelThresholdSource,
    load_campaign_cexp_budgets,
    load_character_starting_cexp,
    load_chapter13_cexp_split,
    load_class_level_thresholds,
)
from .combat import CombatRules, load_combat_rules
from .consumables import ConsumableSource, load_consumable, load_consumable_register
from .dynamic_hits import DynamicElementHitRuleSource, parse_dynamic_element_hit_rule_text
from .enemies import EnemySystemRules, MissingWeightSelection, load_enemy_system_rules
from .entities import EntityRole, EntityStatSource, parse_entity_stat_sources
from .equipment import EquipmentSource, combine_equipment_bonuses, load_equipment, load_equipment_register
from .legacies import (
    DONOR_LEGACY_ACCESS_PATH,
    LEGACY_MASTER_REGISTER_PATH,
    LEGACY_PROJECT_RULES_PATH,
    DonorLegacyAccessSource,
    LegacyItemSource,
    LegacyProjectRuleSource,
    load_character_donor_legacy_access,
    load_character_legacy_package,
    load_donor_legacy_access,
    load_legacy_item,
    load_legacy_items,
    load_legacy_project_rules,
)
from .markdown import (
    extract_heading_block,
    extract_markdown_table,
    extract_markdown_tables,
    find_line_value,
    find_markdown_table,
)
from .party import PartyRules, load_party_rules
from .readiness import (
    OWNER_DOMAINS,
    OwnerFileReadiness,
    ReadinessIssue,
    SimulationReadinessReport,
    audit_owner_file,
    audit_simulation_readiness,
)
from .relics import (
    RELIC_PLACEMENT_PATH,
    RELIC_WEAPONS_PATH,
    RelicPlacementSource,
    RelicWeaponSource,
    load_relic_placement,
    load_relic_placements,
    load_relic_weapon,
    load_relic_weapons,
)
from .replays import BoundedReplayRuleSource, parse_bounded_replay_rule_text
from .repo import RepoSourceError, SourceGapError, find_repo_root, read_repo_text
from .traits import TraitRankSource, TraitSource, load_trait_registry, load_trait_source

__all__ = [
    "AbilityRegistryEntry",
    "AbilitySource",
    "AuthoredActionSource",
    "BoundedReplayRuleSource",
    "CAMPAIGN_CEXP_BUDGETS_PATH",
    "CLASS_CEXP_CAP",
    "CLASS_EXP_CEXP_PATH",
    "CLASS_LEVEL_CAP",
    "CLASS_RECRUITMENT_CEXP_PATH",
    "CampaignCexpBudgetSource",
    "Chapter13CexpSplitSource",
    "CharacterStartingCexpSource",
    "ClassLevelThresholdSource",
    "CombatRules",
    "ConsumableSource",
    "DONOR_LEGACY_ACCESS_PATH",
    "DonorEquipmentAccessSource",
    "DonorLegacyAccessSource",
    "DynamicElementHitRuleSource",
    "EnemyRegistryEntry",
    "EnemySystemRules",
    "EntityRole",
    "EntityStatSource",
    "EquipmentSource",
    "FunctionalAnalogueRuleSource",
    "LEGACY_MASTER_REGISTER_PATH",
    "LEGACY_PROJECT_RULES_PATH",
    "LegacyItemSource",
    "LegacyProjectRuleSource",
    "MissingWeightSelection",
    "OWNER_DOMAINS",
    "OwnerFileReadiness",
    "PartyRules",
    "RELIC_PLACEMENT_PATH",
    "RELIC_WEAPONS_PATH",
    "ReadinessIssue",
    "RelicPlacementSource",
    "RelicWeaponSource",
    "RepoSourceError",
    "SimulationReadinessReport",
    "SourceAuditIssue",
    "SourceAuditReport",
    "SourceGapError",
    "StatBlockSource",
    "TraitRankSource",
    "TraitSource",
    "audit_owner_file",
    "audit_repo_sources",
    "audit_simulation_readiness",
    "combine_equipment_bonuses",
    "extract_heading_block",
    "extract_markdown_table",
    "extract_markdown_tables",
    "find_enemy_registry_entries",
    "find_line_value",
    "find_markdown_table",
    "find_named_action_line",
    "find_repo_root",
    "load_ability_registry",
    "load_ability_source",
    "load_campaign_cexp_budgets",
    "load_character_donor_equipment_access",
    "load_character_donor_legacy_access",
    "load_character_legacy_package",
    "load_character_starting_cexp",
    "load_chapter13_cexp_split",
    "load_class_level_thresholds",
    "load_combat_rules",
    "load_consumable",
    "load_consumable_register",
    "load_donor_equipment_access",
    "load_donor_legacy_access",
    "load_enemy_registry",
    "load_enemy_system_rules",
    "load_equipment",
    "load_equipment_register",
    "load_legacy_item",
    "load_legacy_items",
    "load_legacy_project_rules",
    "load_named_action_source",
    "load_party_rules",
    "load_relic_placement",
    "load_relic_placements",
    "load_relic_weapon",
    "load_relic_weapons",
    "load_stat_row",
    "load_stat_table",
    "load_trait_registry",
    "load_trait_source",
    "parse_authored_action_text",
    "parse_bounded_replay_rule_text",
    "parse_dynamic_element_hit_rule_text",
    "parse_entity_stat_sources",
    "parse_functional_analogue_rule_text",
    "parse_stat_row",
    "read_repo_text",
]
