"""Repo-wide simulation-readiness audit for enemy encounter authority.

This module never supplies gameplay fallbacks. It scans current owner files and
classifies blockers as either:
- source_gap: an action-shaped owning block appears to omit information required to simulate;
- parser_gap: the text may be complete, referenced elsewhere, or summarized, but
  the generic reader cannot yet normalize/link it safely.

The audit is intentionally broader than any one encounter package.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from .actions import AuthoredActionSource, parse_authored_action_text
from .analogues import parse_functional_analogue_rule_text
from .dynamic_hits import parse_dynamic_element_hit_rule_text
from .entities import EntityStatSource, parse_entity_stat_sources
from .references import resolve_enabled_action_references
from .replays import parse_bounded_replay_rule_text
from .repo import find_repo_root

OWNER_DOMAINS: tuple[tuple[str, str], ...] = (
    ("ordinary_enemies", "docs/09_ENEMIES_AND_ENCOUNTERS/ORDINARY_ENEMIES"),
    ("support_objects", "docs/09_ENEMIES_AND_ENCOUNTERS/SUPPORT_OBJECTS"),
    ("elites", "docs/09_ENEMIES_AND_ENCOUNTERS/ELITES"),
    ("story_bosses", "docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES"),
    ("regional_hunts", "docs/09_ENEMIES_AND_ENCOUNTERS/REGIONAL_HUNTS"),
    ("major_hunts", "docs/09_ENEMIES_AND_ENCOUNTERS/MAJOR_HUNTS"),
)

_NO_DAMAGE_RE = re.compile(r"Power\s*:\s*N/A\s*[—-]\s*no direct damage|Power\s+N/A", re.I)
_REFERENCE_RE = re.compile(
    r"(?:^|\n)Authority:\s*(?:\n)?`[^`]+`|(?:^|\n)(?:Enables|While functional, .+? may use):",
    re.I,
)

_STRUCTURAL_HEADING_TERMS = (
    "architecture", "access", "interaction", "certification", "recertification",
    "verdict", "reference", "notes", "handoff", "boundary", "summary", "status",
    "route", "progression", "fresh-body rule", "numerical boundary", "pressure check",
    "duration exception", "current working", "body",
)

_FUNCTIONAL_ANALOGUE_HEADINGS = frozenset({
    "recorded physical analogue",
    "recorded magical analogue",
    "recorded hybrid analogue",
    "recorded analogue",
})


@dataclass(frozen=True)
class ReadinessIssue:
    severity: str  # source_gap | parser_gap
    domain: str
    path: str
    subject: str
    code: str
    message: str

    def as_dict(self) -> dict[str, str]:
        return {
            "severity": self.severity,
            "domain": self.domain,
            "path": self.path,
            "subject": self.subject,
            "code": self.code,
            "message": self.message,
        }


@dataclass(frozen=True)
class OwnerFileReadiness:
    domain: str
    path: str
    title: str
    stat_rows: int
    action_sections: int
    direct_damage_sections: int
    issues: tuple[ReadinessIssue, ...]

    @property
    def source_gap_count(self) -> int:
        return sum(issue.severity == "source_gap" for issue in self.issues)

    @property
    def parser_gap_count(self) -> int:
        return sum(issue.severity == "parser_gap" for issue in self.issues)

    @property
    def ready(self) -> bool:
        return not self.issues

    def as_dict(self) -> dict[str, object]:
        return {
            "domain": self.domain,
            "path": self.path,
            "title": self.title,
            "stat_rows": self.stat_rows,
            "action_sections": self.action_sections,
            "direct_damage_sections": self.direct_damage_sections,
            "ready": self.ready,
            "source_gap_count": self.source_gap_count,
            "parser_gap_count": self.parser_gap_count,
            "issues": [issue.as_dict() for issue in self.issues],
        }


@dataclass(frozen=True)
class SimulationReadinessReport:
    files: tuple[OwnerFileReadiness, ...]

    @property
    def files_scanned(self) -> int:
        return len(self.files)

    @property
    def all_issues(self) -> tuple[ReadinessIssue, ...]:
        return tuple(issue for file in self.files for issue in file.issues)

    @property
    def source_gaps(self) -> tuple[ReadinessIssue, ...]:
        return tuple(issue for issue in self.all_issues if issue.severity == "source_gap")

    @property
    def parser_gaps(self) -> tuple[ReadinessIssue, ...]:
        return tuple(issue for issue in self.all_issues if issue.severity == "parser_gap")

    @property
    def direct_damage_sections(self) -> int:
        return sum(file.direct_damage_sections for file in self.files)

    @property
    def ready_files(self) -> int:
        return sum(file.ready for file in self.files)

    @property
    def by_domain(self) -> dict[str, dict[str, int]]:
        result: dict[str, dict[str, int]] = {}
        for domain, _ in OWNER_DOMAINS:
            members = [file for file in self.files if file.domain == domain]
            result[domain] = {
                "files": len(members),
                "ready_files": sum(file.ready for file in members),
                "source_gaps": sum(file.source_gap_count for file in members),
                "parser_gaps": sum(file.parser_gap_count for file in members),
                "direct_damage_sections": sum(file.direct_damage_sections for file in members),
            }
        return result

    def as_dict(self, *, include_files: bool = True) -> dict[str, object]:
        payload: dict[str, object] = {
            "files_scanned": self.files_scanned,
            "ready_files": self.ready_files,
            "direct_damage_sections": self.direct_damage_sections,
            "source_gap_count": len(self.source_gaps),
            "parser_gap_count": len(self.parser_gaps),
            "by_domain": self.by_domain,
        }
        if include_files:
            payload["files"] = [file.as_dict() for file in self.files]
        return payload

    def issues_dict(self, severity: str = "all") -> dict[str, object]:
        if severity == "source_gap":
            issues = self.source_gaps
        elif severity == "parser_gap":
            issues = self.parser_gaps
        elif severity == "all":
            issues = self.all_issues
        else:
            raise ValueError(f"unsupported readiness severity: {severity}")
        return {
            "severity": severity,
            "count": len(issues),
            "issues": [issue.as_dict() for issue in issues],
        }


def _title(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", text, re.M)
    return match.group(1).strip() if match else fallback


def _heading_blocks(text: str) -> tuple[tuple[str, str], ...]:
    matches = list(re.finditer(r"^(#{2,4})\s+(.+?)\s*$", text, re.M))
    blocks: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks.append((match.group(2).strip(), text[match.end():end].strip()))
    return tuple(blocks)


def _is_structural_heading(heading: str) -> bool:
    lowered = heading.casefold()
    return any(term in lowered for term in _STRUCTURAL_HEADING_TERMS)


def _is_reference_or_enablement(block: str) -> bool:
    return bool(_REFERENCE_RE.search(block))


def _parse_section(heading: str, block: str) -> AuthoredActionSource:
    return parse_authored_action_text(heading, block)


def _supported_bounded_replay(heading: str, block: str) -> bool:
    return parse_bounded_replay_rule_text(heading, block).complete


def _supported_functional_analogue(heading: str, *, system_complete: bool) -> bool:
    return system_complete and heading.casefold() in _FUNCTIONAL_ANALOGUE_HEADINGS


def _supported_dynamic_hit_package(heading: str, block: str, *, context_text: str) -> bool:
    return parse_dynamic_element_hit_rule_text(heading, block, context_text=context_text).complete


def _action_candidate(
    heading: str,
    block: str,
    *,
    context_text: str,
    functional_analogue_complete: bool = False,
) -> bool:
    if _is_structural_heading(heading):
        return False
    if _NO_DAMAGE_RE.search(block):
        return True
    if _supported_bounded_replay(heading, block):
        return True
    if _supported_functional_analogue(heading, system_complete=functional_analogue_complete):
        return True
    if _supported_dynamic_hit_package(heading, block, context_text=context_text):
        return True
    source = _parse_section(heading, block)
    return any((
        source.damage_kind is not None,
        source.power is not None,
        source.base_hit is not None,
        source.target_scope is not None and source.has_element_identity,
    ))


def _direct_damage_source(heading: str, block: str) -> AuthoredActionSource | None:
    if _NO_DAMAGE_RE.search(block):
        return None
    source = _parse_section(heading, block)
    if source.damage_kind is not None or source.power is not None:
        return source
    return None


def _audit_action(
    domain: str,
    path: str,
    heading: str,
    block: str,
    *,
    context_text: str,
    repo_root: Path,
    current_path: Path,
    functional_analogue_complete: bool = False,
) -> tuple[ReadinessIssue, ...]:
    # Complete inherited-copy and dynamic-hit systems intentionally do not own
    # one fixed element identity in each ordinary-action field. Their repo-backed
    # runtime transforms are the authority for that conditional behavior.
    if _supported_bounded_replay(heading, block):
        return ()
    if _supported_functional_analogue(heading, system_complete=functional_analogue_complete):
        return ()
    if _supported_dynamic_hit_package(heading, block, context_text=context_text):
        return ()

    source = _direct_damage_source(heading, block)
    if source is None:
        return ()

    if _is_reference_or_enablement(block):
        enabled_resolution = resolve_enabled_action_references(
            block,
            repo_root=repo_root,
            current_path=current_path,
        )
        if enabled_resolution.complete:
            return ()

        unresolved = []
        if source.damage_kind is None or not source.has_element_identity:
            unresolved.append("damage kind/element")
        if source.power is None:
            unresolved.append("Power")
        if source.base_hit is None:
            unresolved.append("Base Hit")
        if source.target_scope is None:
            unresolved.append("target scope")
        if unresolved:
            return (ReadinessIssue(
                "parser_gap", domain, path, heading, "referenced_action_unresolved",
                "This section references/enables combat behavior owned or completed elsewhere; generic cross-file linking must resolve: " + ", ".join(unresolved) + ".",
            ),)
        return ()

    issues: list[ReadinessIssue] = []
    action_shaped = source.target_scope is not None and source.damage_kind is not None and source.has_element_identity

    if source.damage_kind is not None and source.has_element_identity and source.power is None:
        severity = "source_gap" if action_shaped else "parser_gap"
        issues.append(ReadinessIssue(
            severity, domain, path, heading,
            "damage_power_missing" if severity == "source_gap" else "damage_power_unresolved",
            "Action-shaped direct-damage block has no exact numeric Power."
            if severity == "source_gap"
            else "Damage identity is mentioned, but the generic reader cannot establish this as the complete action owner before requiring Power.",
        ))
    elif source.power is not None and (source.damage_kind is None or not source.has_element_identity):
        issues.append(ReadinessIssue(
            "parser_gap", domain, path, heading, "damage_identity_unresolved",
            "Numeric direct-damage Power is present, but the shared action parser cannot fully resolve damage kind/element from this section alone.",
        ))

    if source.base_hit is None:
        severity = "source_gap" if action_shaped and source.power is not None else "parser_gap"
        issues.append(ReadinessIssue(
            severity, domain, path, heading,
            "base_hit_missing" if severity == "source_gap" else "base_hit_unresolved",
            "Action-shaped enemy/support direct-damage block has no explicit Base Hit."
            if severity == "source_gap"
            else "The shared action parser cannot safely require Base Hit from this summarized/partial section.",
        ))

    if source.target_scope is None:
        issues.append(ReadinessIssue(
            "parser_gap", domain, path, heading, "target_scope_unresolved",
            "The shared action parser cannot resolve one/all target scope from this action section.",
        ))

    return tuple(issues)


def _entity_subject(title: str, index: int, entity: EntityStatSource) -> str:
    label = f" / {entity.row_label}" if entity.row_label else ""
    return f"{title} / {entity.section_heading}{label} / stat row {index}"


def _audit_stats(
    domain: str,
    path: str,
    title: str,
    entities: tuple[EntityStatSource, ...],
    direct_sources: tuple[AuthoredActionSource, ...],
) -> tuple[ReadinessIssue, ...]:
    if not direct_sources:
        return ()
    if not entities:
        return (ReadinessIssue(
            "parser_gap", domain, path, title, "stat_block_unresolved",
            "This owner contains direct damage but the generic reader found no HP stat table in the same file; stats may be owned by another referenced file.",
        ),)

    acting_required = {"hp", "defense", "spirit", "speed", "evasion"}
    if any(source.damage_kind == "physical" for source in direct_sources):
        acting_required.add("attack")
    if any(source.damage_kind == "magical" for source in direct_sources):
        acting_required.add("magic")
    if any(source.damage_kind == "hybrid" for source in direct_sources):
        acting_required.update(("attack", "magic"))

    passive_required = {"hp", "defense", "spirit", "evasion", "status_resistance"}
    issues: list[ReadinessIssue] = []
    for index, entity in enumerate(entities, start=1):
        if entity.role == "passive_target":
            missing = sorted(field for field in passive_required if not entity.stats.has(field))
            if missing:
                issues.append(ReadinessIssue(
                    "parser_gap", domain, path, _entity_subject(title, index, entity),
                    "passive_target_stats_unresolved",
                    f"Explicit passive target omits defensive fields needed for generic targeting: {', '.join(missing)}.",
                ))
            continue

        missing = sorted(field for field in acting_required if not entity.stats.has(field))
        if missing:
            role_text = "explicit acting combatant" if entity.role == "acting_combatant" else "unresolved entity role"
            issues.append(ReadinessIssue(
                "parser_gap", domain, path, _entity_subject(title, index, entity), "stat_role_unresolved",
                f"{role_text} omits {', '.join(missing)}; associate this stat row with its exact actor/support role before requiring those fields.",
            ))
    return tuple(issues)


def audit_owner_file(path: Path, *, domain: str, repo_root: Path) -> OwnerFileReadiness:
    text = path.read_text(encoding="utf-8")
    relative = path.relative_to(repo_root).as_posix()
    title = _title(text, path.stem)
    entities = parse_entity_stat_sources(text)
    functional_analogue_complete = parse_functional_analogue_rule_text(text).complete

    actions: list[tuple[str, str]] = []
    direct_sources: list[AuthoredActionSource] = []
    issues: list[ReadinessIssue] = []
    for heading, block in _heading_blocks(text):
        if not _action_candidate(
            heading,
            block,
            context_text=text,
            functional_analogue_complete=functional_analogue_complete,
        ):
            continue
        actions.append((heading, block))
        source = _direct_damage_source(heading, block)
        if source is not None:
            direct_sources.append(source)
        issues.extend(_audit_action(
            domain,
            relative,
            heading,
            block,
            context_text=text,
            repo_root=repo_root,
            current_path=path,
            functional_analogue_complete=functional_analogue_complete,
        ))

    issues.extend(_audit_stats(domain, relative, title, entities, tuple(direct_sources)))
    return OwnerFileReadiness(
        domain=domain,
        path=relative,
        title=title,
        stat_rows=len(entities),
        action_sections=len(actions),
        direct_damage_sections=len(direct_sources),
        issues=tuple(issues),
    )


def _should_scan(path: Path) -> bool:
    upper = path.stem.upper()
    if path.name.startswith(".") or path.name.upper() == "README.MD":
        return False
    if "REGISTER" in upper or upper.endswith("_INDEX"):
        return False
    if upper.startswith("MANDATORY_NAMED_RAW_STATS_"):
        return False
    return True


def audit_simulation_readiness(*, root: Path | None = None) -> SimulationReadinessReport:
    repo = (root or find_repo_root()).resolve()
    files: list[OwnerFileReadiness] = []
    for domain, relative_dir in OWNER_DOMAINS:
        directory = repo / relative_dir
        if not directory.exists():
            files.append(OwnerFileReadiness(
                domain=domain,
                path=relative_dir,
                title=relative_dir,
                stat_rows=0,
                action_sections=0,
                direct_damage_sections=0,
                issues=(ReadinessIssue(
                    "source_gap", domain, relative_dir, relative_dir, "owner_directory_missing",
                    "Expected encounter owner directory does not exist.",
                ),),
            ))
            continue
        for path in sorted(directory.rglob("*.md")):
            if _should_scan(path):
                files.append(audit_owner_file(path, domain=domain, repo_root=repo))
    return SimulationReadinessReport(tuple(files))


__all__ = [
    "OWNER_DOMAINS",
    "OwnerFileReadiness",
    "ReadinessIssue",
    "SimulationReadinessReport",
    "audit_owner_file",
    "audit_simulation_readiness",
]
