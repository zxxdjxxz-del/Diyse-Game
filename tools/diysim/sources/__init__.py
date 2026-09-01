"""Repository-backed source access for diysim.

Diyse canon belongs to the repository, never to simulator-owned snapshots.
"""

from .abilities import AbilityRegistryEntry, AbilitySource, load_ability_registry, load_ability_source
from .actions import AuthoredActionSource, find_named_action_line, load_named_action_source, parse_authored_action_text
from .audit import SourceAuditIssue, SourceAuditReport, audit_repo_sources
from .markdown import (
    extract_heading_block,
    extract_markdown_table,
    extract_markdown_tables,
    find_line_value,
    find_markdown_table,
)
from .repo import RepoSourceError, SourceGapError, find_repo_root, read_repo_text
from .traits import TraitRankSource, TraitSource, load_trait_registry, load_trait_source

__all__ = [
    "AbilityRegistryEntry",
    "AbilitySource",
    "AuthoredActionSource",
    "RepoSourceError",
    "SourceAuditIssue",
    "SourceAuditReport",
    "SourceGapError",
    "TraitRankSource",
    "TraitSource",
    "audit_repo_sources",
    "extract_heading_block",
    "extract_markdown_table",
    "extract_markdown_tables",
    "find_line_value",
    "find_markdown_table",
    "find_named_action_line",
    "find_repo_root",
    "load_ability_registry",
    "load_ability_source",
    "load_named_action_source",
    "load_trait_registry",
    "load_trait_source",
    "parse_authored_action_text",
    "read_repo_text",
]
