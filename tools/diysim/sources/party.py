"""Repository-backed active-party rules."""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re

from .repo import SourceGapError, find_repo_root, read_repo_text

CANON_QUICK_REFERENCE_PATH = "docs/00_MASTER_CONTROL/CANON_QUICK_REFERENCE.md"


@dataclass(frozen=True)
class PartyRules:
    active_battle_party: int


@lru_cache(maxsize=4)
def _cached(root_string: str) -> PartyRules:
    root = Path(root_string)
    text = read_repo_text(CANON_QUICK_REFERENCE_PATH, root=root)
    match = re.search(r"Active battle party:\s*>\s*\*\*(\d+)\*\*", text)
    if not match:
        raise SourceGapError("Missing active battle party size in master quick reference")
    return PartyRules(active_battle_party=int(match.group(1)))


def load_party_rules(*, root: Path | None = None) -> PartyRules:
    repo = (root or find_repo_root()).resolve()
    return _cached(str(repo))


__all__ = ["PartyRules", "load_party_rules"]
