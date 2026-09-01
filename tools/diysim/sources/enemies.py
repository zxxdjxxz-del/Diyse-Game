"""Repository-backed enemy-system rules used by shared simulation logic."""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re
from typing import Literal

from .repo import SourceGapError, find_repo_root, read_repo_text

ENEMY_SYSTEM_PATH = "docs/09_ENEMIES_AND_ENCOUNTERS/ENEMY_SYSTEM_RULES.md"
ACTION_SELECTION_PATH = "docs/09_ENEMIES_AND_ENCOUNTERS/ACTION_SELECTION_DEFAULT.md"

MissingWeightSelection = Literal["uniform"]


@dataclass(frozen=True)
class EnemySystemRules:
    max_active_enemies: int
    missing_weight_selection: MissingWeightSelection


def _load(root_string: str) -> EnemySystemRules:
    root = Path(root_string)
    system_text = read_repo_text(ENEMY_SYSTEM_PATH, root=root)
    selection_text = read_repo_text(ACTION_SELECTION_PATH, root=root)

    cap = re.search(r"Maximum simultaneously active enemies:\s*>\s*\*\*(\d+)\*\*", system_text)
    if not cap:
        raise SourceGapError("Missing simultaneous-enemy cap in enemy-system authority")

    if re.search(r"select \*\*uniformly at random\*\* among the legal actions", selection_text, re.I):
        missing_weight_selection: MissingWeightSelection = "uniform"
    else:
        raise SourceGapError("Unsupported or missing unweighted enemy-action selection rule")

    return EnemySystemRules(
        max_active_enemies=int(cap.group(1)),
        missing_weight_selection=missing_weight_selection,
    )


@lru_cache(maxsize=4)
def _cached(root_string: str) -> EnemySystemRules:
    return _load(root_string)


def load_enemy_system_rules(*, root: Path | None = None) -> EnemySystemRules:
    repo = (root or find_repo_root()).resolve()
    return _cached(str(repo))


__all__ = ["EnemySystemRules", "MissingWeightSelection", "load_enemy_system_rules"]
