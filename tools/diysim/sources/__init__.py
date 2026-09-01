"""Repository-backed source access for diysim.

Diyse canon belongs to the repository, never to simulator-owned snapshots.
"""

from .repo import RepoSourceError, SourceGapError, find_repo_root, read_repo_text
from .markdown import extract_markdown_table, find_line_value

__all__ = [
    "RepoSourceError",
    "SourceGapError",
    "extract_markdown_table",
    "find_line_value",
    "find_repo_root",
    "read_repo_text",
]
