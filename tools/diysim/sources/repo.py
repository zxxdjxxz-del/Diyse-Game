"""Read authoritative Diyse source files from the checked-out repository."""
from __future__ import annotations
from functools import lru_cache
from pathlib import Path


class RepoSourceError(RuntimeError):
    """Base error for repository-source failures."""


class SourceGapError(RepoSourceError):
    """Raised when a required authoritative value is absent from the repo."""


@lru_cache(maxsize=16)
def find_repo_root(start: Path | None = None) -> Path:
    """Locate the repository root once per distinct starting path.

    Combat resolution asks repo-backed source adapters for cached rule objects
    very frequently. Root discovery is filesystem topology, not gameplay state,
    so caching it avoids repeated Path.resolve()/is_file() walks during large
    Monte Carlo batches without caching any mutable combat content.
    """
    path = (start or Path(__file__)).resolve()
    if path.is_file():
        path = path.parent
    for candidate in (path, *path.parents):
        if (candidate / "AGENTS.md").is_file() and (candidate / "docs").is_dir():
            return candidate
    raise RepoSourceError("Could not locate Diyse repository root")


def read_repo_text(relative_path: str, *, root: Path | None = None) -> str:
    repo = root or find_repo_root()
    target = (repo / relative_path).resolve()
    try:
        target.relative_to(repo.resolve())
    except ValueError as exc:
        raise RepoSourceError(f"Source path escapes repository: {relative_path}") from exc
    if not target.is_file():
        raise SourceGapError(f"Required repository source is missing: {relative_path}")
    return target.read_text(encoding="utf-8")
