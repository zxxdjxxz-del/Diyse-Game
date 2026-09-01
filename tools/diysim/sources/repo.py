"""Read authoritative Diyse source files from the checked-out repository."""
from __future__ import annotations
from pathlib import Path


class RepoSourceError(RuntimeError):
    """Base error for repository-source failures."""


class SourceGapError(RepoSourceError):
    """Raised when a required authoritative value is absent from the repo."""


def find_repo_root(start: Path | None = None) -> Path:
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
