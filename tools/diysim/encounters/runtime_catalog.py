"""Repo-backed runtime coverage for the Diyse enemy roster.

No enemy numeric canon lives here. Owner sheets are discovered at runtime and
classified by whether DiySim can execute their complete combat behavior.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Literal

from tools.diysim.combat.models import CombatAction, Combatant, StatusRider
from tools.diysim.progression.stats import Stats
from tools.diysim.sources.actions import AuthoredActionSource, parse_authored_action_text
from tools.diysim.sources.actors import parse_stat_row
from tools.diysim.sources.markdown import find_markdown_table
from tools.diysim.sources.repo import SourceGapError, find_repo_root, read_repo_text

RuntimeKind = Literal["generic", "special", "component", "blocked"]

ENEMY_ROOT = Path("docs/09_ENEMIES_AND_ENCOUNTERS")
OWNER_DIRS: dict[str, str] = {
    "ordinary": "ORDINARY_ENEMIES",
    "elite": "ELITES",
    "regional_hunt": "REGIONAL_HUNTS",
    "major_hunt": "MAJOR_HUNTS",
    "quest_boss": "QUEST_BOSSES",
    "story_boss": "STORY_BOSSES",
    "support": "SUPPORT_OBJECTS",
}

SPECIAL_RUNTIME_PATHS: dict[str, str] = {
    "docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/HOLLOW_WATCH_CASTELLAN.md":
        "tools.diysim.encounters.story_bosses.hollow_watch_castellan",
    "docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/FIRST_COMMAND_WARDEN.md":
        "tools.diysim.encounters.story_bosses.first_command_warden.runtime",
    "docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/MATRON_ZEVRAYA.md":
        "tools.diysim.encounters.story_bosses.matron_zevraya",
}

_NON_OWNER_FILE_TOKENS = (
    "README", "REGISTER", "INDEX", "MIGRATION", "TERMINOLOGY", "RULES",
    "ARCHITECTURE", "CHECKLIST", "SUMMARY", "RAW_STATS", "CERTIFICATION",
    "HANDOFF",
)
_NON_OWNER_EXACT = {"CHARACTER_QUEST_BOSSES"}
_REQUIRED_GENERIC_STATS = ("hp", "attack", "magic", "defense", "spirit", "speed")
_POWER_AUTHORITY = re.compile(
    r"(?im)(?:^|\n)\s*(?:[-*]\s*)?(?:\*\*)?Power(?:\*\*)?\s*:?\s*(?:\*\*)?(?:\d+(?:\.\d+)?|N/?A)\b"
    r"|\b\d+(?:\.\d+)?\s+Power(?:\s+per\s+target)?\b"
)
_TRIGGER_ONLY = re.compile(
    r"\bpassive\b|\bon[- ]defeat\b|\btrigger(?:ed| only)?\b|not an ordinary selected action",
    re.I,
)
_STATEFUL_SHEET = re.compile(
    r"^##+\s+.*(?:State|Phase|Form)\b|\bfresh HP\b|\bphase transition\b|"
    r"\btransition(?:s|ed)?\s+(?:at|when|once|into|to)\b|\bonce HP\b|"
    r"\bwhen HP\b|\bat\s+\d+%\s+(?:Max\s+)?HP\b",
    re.I | re.M,
)
_SEQUENCE_RULE = re.compile(
    r"\bmust be followed by\b|\bnext action\b|\bfixed sequence\b|\baction cycle\b|"
    r"\bon the following turn\b|\bthen uses\b",
    re.I,
)


@dataclass(frozen=True)
class RuntimeActionDefinition:
    source: AuthoredActionSource
    action: CombatAction | None
    blockers: tuple[str, ...]
    repetition_lock_rounds: int | None
    non_damage: bool
    triggered: bool = False


@dataclass(frozen=True)
class EnemyRuntimeDefinition:
    name: str
    category: str
    source_path: str
    kind: RuntimeKind
    displayed_level: int | None
    combatant: Combatant | None
    actions: tuple[RuntimeActionDefinition, ...]
    blockers: tuple[str, ...]
    special_runtime: str | None = None

    @property
    def executable(self) -> bool:
        return self.kind in {"generic", "special"}

    @property
    def direct_damage_actions(self) -> tuple[CombatAction, ...]:
        return tuple(
            action.action for action in self.actions
            if action.action is not None and not action.non_damage and not action.triggered
        )


@dataclass(frozen=True)
class RuntimeCoverageSummary:
    total_owner_sheets: int
    enemy_sheets: int
    components: int
    generic: int
    special: int
    blocked: int
    unclassified: int
    definitions: tuple[EnemyRuntimeDefinition, ...]

    @property
    def executable(self) -> int:
        return self.generic + self.special

    @property
    def coverage_rate(self) -> float:
        return self.executable / self.enemy_sheets if self.enemy_sheets else 1.0


def _relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _is_owner_sheet(path: Path) -> bool:
    upper = path.stem.upper()
    return upper not in _NON_OWNER_EXACT and not any(token in upper for token in _NON_OWNER_FILE_TOKENS)


def discover_enemy_owner_paths(*, root: Path | None = None) -> tuple[tuple[str, str], ...]:
    repo = (root or find_repo_root()).resolve()
    found: list[tuple[str, str]] = []
    for category, directory in OWNER_DIRS.items():
        folder = repo / ENEMY_ROOT / directory
        if not folder.exists():
            continue
        for path in sorted(folder.rglob("*.md")):
            if _is_owner_sheet(path):
                found.append((category, _relative(path, repo)))
    return tuple(found)


def _title(text: str, source_path: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", text, re.M)
    if match:
        return re.sub(r"\s+", " ", match.group(1)).strip()
    return Path(source_path).stem.replace("_", " ").title()


def _first_stat_row(text: str):
    rows = find_markdown_table(text, ("HP",))
    if not rows:
        raise SourceGapError("no HP-bearing stat table")
    return parse_stat_row(rows[0])


def _action_blocks(text: str) -> tuple[tuple[str, str], ...]:
    """Return H2-H5 blocks that contain explicit numeric/N/A Power authority."""
    matches = list(re.finditer(r"^(#{2,5})\s+(.+?)\s*$", text, re.M))
    result: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        if not _POWER_AUTHORITY.search(body):
            continue
        name = re.sub(r"\*+", "", match.group(2)).strip()
        result.append((name, body))
    return tuple(result)


def _repetition_lock(raw_text: str) -> int | None:
    match = re.search(r"(\d+)[- ]round repetition lock", raw_text, re.I)
    return int(match.group(1)) if match else None


def _non_damage(raw_text: str) -> bool:
    return bool(re.search(r"Power\s*:\s*(?:\*\*)?N/?A\b|no direct damage", raw_text, re.I))


def _to_action(source: AuthoredActionSource, *, triggered: bool) -> tuple[CombatAction | None, tuple[str, ...], bool]:
    non_damage = _non_damage(source.raw_text)
    blockers: list[str] = []
    if non_damage:
        blockers.append(f"{source.name}: non-damage effect requires runtime handler")
        return None, tuple(blockers), True

    for field in ("target_scope", "damage_kind", "power", "base_hit"):
        if getattr(source, field) is None:
            blockers.append(f"{source.name}: missing {field}")
    if source.element_mode == "dynamic":
        blockers.append(
            f"{source.name}: dynamic element requires encounter-state resolver ({source.element_source})"
        )
    elif source.element is None:
        blockers.append(f"{source.name}: missing fixed element")
    if source.is_multihit:
        blockers.append(f"{source.name}: multihit requires encounter/action-specific runtime")
    if triggered:
        blockers.append(f"{source.name}: triggered/passive action requires runtime trigger")
    if blockers:
        return None, tuple(blockers), False

    assert source.target_scope in {"one", "all"}
    assert source.damage_kind in {"physical", "magical", "hybrid"}
    assert source.element is not None
    assert source.power is not None and source.base_hit is not None
    return CombatAction(
        source.name,
        target_scope=source.target_scope,
        damage_kind=source.damage_kind,
        element=source.element,
        power=source.power,
        base_hit=source.base_hit,
        physical_weight=source.physical_weight,
        magical_weight=source.magical_weight,
        weight=source.weight,
        status_riders=tuple(StatusRider(status, chance) for status, chance in source.status_chances),
    ), (), False


def load_enemy_runtime_definition(
    source_path: str,
    *,
    category: str,
    root: Path | None = None,
) -> EnemyRuntimeDefinition:
    repo = (root or find_repo_root()).resolve()
    text = read_repo_text(source_path, root=repo)
    name = _title(text, source_path)

    if category == "support":
        return EnemyRuntimeDefinition(
            name, category, source_path, "component", None, None, (),
            ("encounter support/component; attach to parent encounter runtime",),
        )

    special = SPECIAL_RUNTIME_PATHS.get(source_path)
    if special is not None:
        return EnemyRuntimeDefinition(name, category, source_path, "special", None, None, (), (), special)

    blockers: list[str] = []
    if "→" in name or _STATEFUL_SHEET.search(text):
        blockers.append("state/phase/form behavior requires encounter-specific runtime")
    if _SEQUENCE_RULE.search(text):
        blockers.append("authored action sequence/cycle requires runtime scheduler")

    combatant: Combatant | None = None
    displayed_level: int | None = None
    try:
        stat_source = _first_stat_row(text)
        missing_stats = tuple(field for field in _REQUIRED_GENERIC_STATS if not stat_source.has(field))
        if missing_stats:
            blockers.append("missing runtime stats: " + ", ".join(missing_stats))
        if not stat_source.has("level"):
            blockers.append("missing displayed level")
        if not missing_stats and stat_source.has("level"):
            values = stat_source.values
            displayed_level = values["level"]
            combatant = Combatant(
                name=name,
                side="enemy",
                stats=Stats(
                    hp=values["hp"], mp=values.get("mp", 0), attack=values["attack"],
                    magic=values["magic"], defense=values["defense"],
                    spirit=values["spirit"], speed=values["speed"],
                ),
                evasion=values.get("evasion", 0),
                status_resistance=values.get("status_resistance", 0),
                rank="regional_hunt" if category == "regional_hunt" else (
                    "major_boss" if category in {"major_hunt", "story_boss", "quest_boss"} else "ordinary"
                ),
            )
    except (SourceGapError, KeyError, ValueError) as exc:
        blockers.append(f"stat parser: {exc}")

    action_defs: list[RuntimeActionDefinition] = []
    action_blocks = _action_blocks(text)
    if not action_blocks:
        blockers.append("no explicit Power-bearing action blocks detected")
    for action_name, raw_text in action_blocks:
        source = parse_authored_action_text(action_name, raw_text)
        triggered = bool(_TRIGGER_ONLY.search(raw_text))
        action, action_blockers, non_damage = _to_action(source, triggered=triggered)
        action_defs.append(RuntimeActionDefinition(
            source, action, action_blockers, _repetition_lock(raw_text), non_damage, triggered
        ))
        blockers.extend(action_blockers)

    damaging_actions = tuple(
        defn.action for defn in action_defs
        if defn.action is not None and not defn.triggered
    )
    if combatant is not None and damaging_actions:
        combatant = Combatant(
            name=combatant.name, side=combatant.side, stats=combatant.stats,
            actions=damaging_actions, evasion=combatant.evasion, rank=combatant.rank,
            status_resistance=combatant.status_resistance,
        )
    elif combatant is not None and not damaging_actions:
        blockers.append("no generic selected direct-damage action is executable")

    unique_blockers = tuple(dict.fromkeys(blockers))
    return EnemyRuntimeDefinition(
        name=name, category=category, source_path=source_path,
        kind="blocked" if unique_blockers else "generic",
        displayed_level=displayed_level,
        combatant=combatant if not unique_blockers else None,
        actions=tuple(action_defs), blockers=unique_blockers,
    )


def build_enemy_runtime_catalog(*, root: Path | None = None) -> tuple[EnemyRuntimeDefinition, ...]:
    return tuple(
        load_enemy_runtime_definition(path, category=category, root=root)
        for category, path in discover_enemy_owner_paths(root=root)
    )


def audit_enemy_runtime_coverage(*, root: Path | None = None) -> RuntimeCoverageSummary:
    definitions = build_enemy_runtime_catalog(root=root)
    components = sum(definition.kind == "component" for definition in definitions)
    generic = sum(definition.kind == "generic" for definition in definitions)
    special = sum(definition.kind == "special" for definition in definitions)
    blocked = sum(definition.kind == "blocked" for definition in definitions)
    enemy_sheets = len(definitions) - components
    return RuntimeCoverageSummary(
        total_owner_sheets=len(definitions), enemy_sheets=enemy_sheets, components=components,
        generic=generic, special=special, blocked=blocked,
        unclassified=len(definitions) - components - generic - special - blocked,
        definitions=definitions,
    )


__all__ = [
    "EnemyRuntimeDefinition", "OWNER_DIRS", "RuntimeActionDefinition",
    "RuntimeCoverageSummary", "SPECIAL_RUNTIME_PATHS", "audit_enemy_runtime_coverage",
    "build_enemy_runtime_catalog", "discover_enemy_owner_paths", "load_enemy_runtime_definition",
]
