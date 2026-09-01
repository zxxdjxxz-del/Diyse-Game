"""Repository-backed source access for diysim.

Diyse canon belongs to the repository, never to simulator-owned snapshots.
"""

from .abilities import AbilityRegistryEntry, AbilitySource, load_ability_registry, load_ability_source
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
    "RepoSourceError",
    "SourceGapError",
    "TraitRankSource",
    "TraitSource",
    "extract_heading_block",
    "extract_markdown_table",
    "extract_markdown_tables",
    "find_line_value",
    "find_markdown_table",
    "find_repo_root",
    "load_ability_registry",
    "load_ability_source",
    "load_trait_registry",
    "load_trait_source",
    "read_repo_text",
]
