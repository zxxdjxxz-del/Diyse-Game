"""Integrity audit for repository-backed simulator sources.

The audit verifies that required owner files can be parsed and cross-resolved.
It does not compare against a simulator-owned copy of canon.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

from .abilities import load_ability_registry, load_ability_source
from .actors import load_enemy_registry
from .combat import load_combat_rules
from .progression import load_progression_rules
from .repo import RepoSourceError, find_repo_root
from .traits import load_trait_registry


@dataclass(frozen=True)
class SourceAuditIssue:
    domain: str
    subject: str
    message: str

    def as_dict(self) -> dict[str, str]:
        return {"domain": self.domain, "subject": self.subject, "message": self.message}


@dataclass(frozen=True)
class SourceAuditReport:
    progression_loaded: bool
    combat_loaded: bool
    ability_entries: int
    ability_sources_resolved: int
    trait_packages: int
    enemy_registry_entries: int
    issues: tuple[SourceAuditIssue, ...]

    @property
    def ok(self) -> bool:
        return not self.issues

    def as_dict(self) -> dict[str, object]:
        return {
            "ok": self.ok,
            "progression_loaded": self.progression_loaded,
            "combat_loaded": self.combat_loaded,
            "ability_entries": self.ability_entries,
            "ability_sources_resolved": self.ability_sources_resolved,
            "trait_packages": self.trait_packages,
            "enemy_registry_entries": self.enemy_registry_entries,
            "issues": [issue.as_dict() for issue in self.issues],
        }


def audit_repo_sources(*, root: Path | None = None) -> SourceAuditReport:
    repo = (root or find_repo_root()).resolve()
    issues: list[SourceAuditIssue] = []

    progression_loaded = False
    try:
        load_progression_rules(root=repo)
        progression_loaded = True
    except RepoSourceError as exc:
        issues.append(SourceAuditIssue("progression", "global", str(exc)))

    combat_loaded = False
    try:
        load_combat_rules(root=repo)
        combat_loaded = True
    except RepoSourceError as exc:
        issues.append(SourceAuditIssue("combat", "global", str(exc)))

    ability_entries = 0
    ability_sources_resolved = 0
    try:
        registry = load_ability_registry(root=repo)
        ability_entries = len(registry)
        for entry in registry:
            try:
                load_ability_source(entry.ability, class_name=entry.class_name, root=repo)
                ability_sources_resolved += 1
            except RepoSourceError as exc:
                issues.append(
                    SourceAuditIssue(
                        "ability",
                        f"{entry.class_name} / {entry.ability}",
                        str(exc),
                    )
                )
    except RepoSourceError as exc:
        issues.append(SourceAuditIssue("ability", "master register", str(exc)))

    trait_packages = 0
    try:
        traits = load_trait_registry(root=repo)
        trait_packages = len(traits)
        for trait in traits:
            if not trait.ranks:
                issues.append(
                    SourceAuditIssue(
                        "trait",
                        f"{trait.class_name} / {trait.trait_name}",
                        "Trait package has no parsed ranks",
                    )
                )
    except RepoSourceError as exc:
        issues.append(SourceAuditIssue("trait", "register", str(exc)))

    enemy_registry_entries = 0
    try:
        enemy_registry_entries = len(load_enemy_registry(root=repo))
    except RepoSourceError as exc:
        issues.append(SourceAuditIssue("enemy", "master register", str(exc)))

    return SourceAuditReport(
        progression_loaded=progression_loaded,
        combat_loaded=combat_loaded,
        ability_entries=ability_entries,
        ability_sources_resolved=ability_sources_resolved,
        trait_packages=trait_packages,
        enemy_registry_entries=enemy_registry_entries,
        issues=tuple(issues),
    )


__all__ = ["SourceAuditIssue", "SourceAuditReport", "audit_repo_sources"]
