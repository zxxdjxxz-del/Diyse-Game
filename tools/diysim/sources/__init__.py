"""Repository-backed source access for diysim.

Diyse canon belongs to the repository, never to simulator-owned snapshots.
"""

from .abilities import AbilityRegistryEntry, AbilitySource, load_ability_registry, load_ability_source
from .actions import AuthoredActionSource, find_named_action_line, load_named_action_source, parse_authored_action_text
from .actors import EnemyRegistryEntry, StatBlockSource, find_enemy_registry_entries, load_enemy_registry, load_stat_row, load_stat_table, parse_stat_row
from .audit import SourceAuditIssue, SourceAuditReport, audit_repo_sources
from .enemies import EnemySystemRules, MissingWeightSelection, load_enemy_system_rules
from .entities import EntityRole, EntityStatSource, parse_entity_stat_sources
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
from .replays import BoundedReplayRuleSource, parse_bounded_replay_rule_text
from .repo import RepoSourceError, SourceGapError, find_repo_root, read_repo_text
from .traits import TraitRankSource, TraitSource, load_trait_registry, load_trait_source

__all__ = [
    "AbilityRegistryEntry",
    "AbilitySource",
    "AuthoredActionSource",
    "BoundedReplayRuleSource",
    "EnemyRegistryEntry",
    "EnemySystemRules",
    "EntityRole",
    "EntityStatSource",
    "MissingWeightSelection",
    "OWNER_DOMAINS",
    "OwnerFileReadiness",
    "PartyRules",
    "ReadinessIssue",
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
    "load_enemy_registry",
    "load_enemy_system_rules",
    "load_named_action_source",
    "load_party_rules",
    "load_stat_row",
    "load_stat_table",
    "load_trait_registry",
    "load_trait_source",
    "parse_authored_action_text",
    "parse_bounded_replay_rule_text",
    "parse_entity_stat_sources",
    "parse_stat_row",
    "read_repo_text",
]
