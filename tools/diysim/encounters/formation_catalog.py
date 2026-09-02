"""Repo-backed ordinary encounter formation catalog.

Formation files own composition and selection weight only. Enemy bodies and
actions continue to come from their individual runtime owner sheets.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re

from tools.diysim.sources.markdown import extract_markdown_tables
from tools.diysim.sources.repo import find_repo_root, read_repo_text

from .runtime_catalog import EnemyRuntimeDefinition, build_enemy_runtime_catalog

FORMATION_ROOT = Path("docs/09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS")
FORMATION_SOURCE_RE = re.compile(r"CHAPTER_(\d+)(?:_RECOVERED)?_FORMATIONS\.md$")
_OWNER_CHAPTER_RE = re.compile(r"\*\*Chapter:\*\*\s*\*?\*?(\d+)\b", re.I)


@dataclass(frozen=True)
class FormationMember:
    count: int
    label: str
    enemy: EnemyRuntimeDefinition | None
    blocker: str | None = None


@dataclass(frozen=True)
class EncounterFormationDefinition:
    name: str
    composition_text: str
    weight: float | None
    phase: str | None
    source_path: str
    members: tuple[FormationMember, ...]

    @property
    def blockers(self) -> tuple[str, ...]:
        return tuple(member.blocker for member in self.members if member.blocker is not None)

    @property
    def runtime_ready(self) -> bool:
        return not self.blockers and all(
            member.enemy is not None and member.enemy.kind in {"generic", "formation"}
            for member in self.members
        )


def formation_chapter_number(source_path: str) -> int | None:
    """Return the numbered chapter owned by a standard or recovered formation file."""
    match = FORMATION_SOURCE_RE.search(source_path)
    return int(match.group(1)) if match else None


def discover_formation_paths(*, root: Path | None = None) -> tuple[str, ...]:
    repo = (root or find_repo_root()).resolve()
    folder = repo / FORMATION_ROOT
    if not folder.exists():
        return ()
    return tuple(
        path.relative_to(repo).as_posix()
        for path in sorted(folder.glob("CHAPTER_*_FORMATIONS.md"))
        if formation_chapter_number(path.name) is not None
    )


def _normalize(value: str) -> str:
    value = value.replace("–", "-").replace("—", "-")
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def _singularize_last_word(value: str) -> str:
    words = value.split()
    if not words:
        return value
    word = words[-1]
    if word.endswith("men") and len(word) > 3:
        word = word[:-3] + "man"
    elif word.endswith("ies") and len(word) > 3:
        word = word[:-3] + "y"
    elif word.endswith("istae") and len(word) > 5:
        word = word[:-1]
    elif word.endswith("oes") and len(word) > 3:
        word = word[:-2]
    elif word.endswith(("ses", "xes", "zes", "ches", "shes")) and len(word) > 3:
        word = word[:-2]
    elif word.endswith("s") and not word.endswith("ss") and len(word) > 1:
        word = word[:-1]
    words[-1] = word
    return " ".join(words)


def _enemy_index(
    definitions: tuple[EnemyRuntimeDefinition, ...],
) -> tuple[dict[str, EnemyRuntimeDefinition], dict[str, tuple[EnemyRuntimeDefinition, ...]]]:
    index: dict[str, EnemyRuntimeDefinition] = {}
    suffix_candidates: dict[str, list[EnemyRuntimeDefinition]] = defaultdict(list)
    for definition in definitions:
        if definition.kind == "component":
            continue
        aliases = {
            _normalize(definition.name),
            _normalize(Path(definition.source_path).stem),
        }
        for alias in tuple(aliases):
            aliases.add(_singularize_last_word(alias))
        for alias in aliases:
            if alias:
                index[alias] = definition

        name_words = _normalize(definition.name).split()
        for start in range(max(0, len(name_words) - 5), len(name_words) - 1):
            suffix = " ".join(name_words[start:])
            if len(suffix.split()) >= 2:
                suffix_candidates[suffix].append(definition)
                singular = _singularize_last_word(suffix)
                if singular != suffix:
                    suffix_candidates[singular].append(definition)
    return index, {key: tuple(value) for key, value in suffix_candidates.items()}


def _declared_owner_chapter(definition: EnemyRuntimeDefinition, repo: Path) -> int | None:
    text = read_repo_text(definition.source_path, root=repo)
    match = _OWNER_CHAPTER_RE.search(text)
    return int(match.group(1)) if match else None


def _resolve_enemy(
    label: str,
    index: dict[str, EnemyRuntimeDefinition],
    suffix_candidates: dict[str, tuple[EnemyRuntimeDefinition, ...]],
    *,
    formation_chapter: int | None,
    repo: Path,
) -> EnemyRuntimeDefinition | None:
    key = _normalize(label)
    singular = _singularize_last_word(key)
    definition = index.get(key) or index.get(singular)
    if definition is not None:
        return definition
    candidates = suffix_candidates.get(key) or suffix_candidates.get(singular) or ()
    unique = {candidate.source_path: candidate for candidate in candidates}
    if len(unique) == 1:
        return next(iter(unique.values()))
    if formation_chapter is not None and unique:
        chapter_matches = [
            candidate for candidate in unique.values()
            if _declared_owner_chapter(candidate, repo) == formation_chapter
        ]
        if len(chapter_matches) == 1:
            return chapter_matches[0]
    return None


def _parse_member(
    part: str,
    index: dict[str, EnemyRuntimeDefinition],
    suffix_candidates: dict[str, tuple[EnemyRuntimeDefinition, ...]],
    *,
    formation_chapter: int | None,
    repo: Path,
) -> FormationMember:
    cleaned = part.strip()
    if not cleaned:
        return FormationMember(0, cleaned, None, "unparsed formation member: empty member")
    match = re.match(r"^(?:(\d+)\s+)?(.+?)\s*$", cleaned)
    if not match:
        return FormationMember(0, cleaned, None, f"unparsed formation member: {cleaned}")
    count = int(match.group(1) or 1)
    label = match.group(2).strip()
    definition = _resolve_enemy(
        label, index, suffix_candidates,
        formation_chapter=formation_chapter, repo=repo,
    )
    if definition is None:
        return FormationMember(count, label, None, f"unresolved enemy owner for formation label: {label}")
    if definition.kind == "blocked":
        return FormationMember(count, label, definition, f"{definition.name} runtime blocked")
    if definition.kind == "special":
        return FormationMember(count, label, definition, f"{definition.name} uses bespoke boss runtime, not ordinary formation runtime")
    return FormationMember(count, label, definition)


def _weight(value: str | None) -> float | None:
    if not value:
        return None
    match = re.search(r"(\d+(?:\.\d+)?)", value)
    return float(match.group(1)) / 100.0 if match else None


def load_formation_definitions(
    source_path: str,
    *,
    root: Path | None = None,
    enemy_definitions: tuple[EnemyRuntimeDefinition, ...] | None = None,
) -> tuple[EncounterFormationDefinition, ...]:
    repo = (root or find_repo_root()).resolve()
    text = read_repo_text(source_path, root=repo)
    definitions = enemy_definitions or build_enemy_runtime_catalog(root=repo)
    index, suffix_candidates = _enemy_index(definitions)
    chapter = formation_chapter_number(source_path)
    formations: list[EncounterFormationDefinition] = []
    for table in extract_markdown_tables(text):
        if not table or "Formation" not in table[0] or "Composition" not in table[0]:
            continue
        for row in table:
            composition = row["Composition"].strip()
            members = tuple(
                _parse_member(
                    part, index, suffix_candidates,
                    formation_chapter=chapter, repo=repo,
                )
                for part in re.split(r"\s+\+\s+", composition)
            )
            formations.append(EncounterFormationDefinition(
                name=row["Formation"].strip(),
                composition_text=composition,
                weight=_weight(row.get("Weight")),
                phase=row.get("Phase"),
                source_path=source_path,
                members=members,
            ))
    return tuple(formations)


def build_formation_catalog(*, root: Path | None = None) -> tuple[EncounterFormationDefinition, ...]:
    repo = (root or find_repo_root()).resolve()
    enemy_definitions = build_enemy_runtime_catalog(root=repo)
    return tuple(
        formation
        for path in discover_formation_paths(root=repo)
        for formation in load_formation_definitions(path, root=repo, enemy_definitions=enemy_definitions)
    )


__all__ = [
    "EncounterFormationDefinition", "FormationMember", "build_formation_catalog",
    "discover_formation_paths", "formation_chapter_number", "load_formation_definitions",
]
