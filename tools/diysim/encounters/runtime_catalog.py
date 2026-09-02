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
from tools.diysim.sources.enemy_effects import parse_enemy_effect_action
from tools.diysim.sources.markdown import find_markdown_table
from tools.diysim.sources.repo import SourceGapError, find_repo_root, read_repo_text

RuntimeKind = Literal["generic", "formation", "special", "component", "blocked"]
DynamicElementMode = Literal["random_once", "round_cycle"]

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
    r"(?im)(?:^|\n)\s*(?:>\s*)?(?:[-*]\s*)?(?:\*\*)?Power(?:\*\*)?\s*:?\s*(?:\*\*)?(?:\d+(?:\.\d+)?|N/?A)\b"
    r"|\b\d+(?:\.\d+)?\s+Power(?:\s+per\s+target)?\b"
)
_ACTION_LEAD = re.compile(
    r"^(?:>\s*)?(?:[-*]\s*)?(?:\*\*)?(?:"
    r"Power\b|Target\s*:|one\s+(?:conscious\s+|active\s+|established\s+)*party\s+member\b|"
    r"all\s+(?:conscious\s+|active\s+)*party\s+members\b|Physical\b|Magical\b|Hybrid\b|"
    r"Passive\b|On[- ]defeat\b|Trigger(?:ed)?\b"
    r")",
    re.I,
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
_FIXED_SEQUENCE_RULE = re.compile(
    r"\bmust be followed by\b|\bfixed sequence\b|\baction cycle\b|"
    r"\bon the following turn\b|\bthen uses\b",
    re.I,
)
_REQUIRES_PREPARATION_RE = re.compile(
    r"\blegal\s+only\s+after\s+(?:\*\*)?([^\n.*]+?)(?:\*\*)?(?:\.|$)",
    re.I | re.M,
)
_STANDARD_ELEMENT = r"Fire|Ice|Lightning|Earth"
_ELEMENTAL_RIDER_RE = re.compile(
    rf"^\s*-\s*({_STANDARD_ELEMENT})\s+[—-]\s*\*{{0,2}}(\d+)%\s+"
    r"(Burn|Freeze|Stun|Staggered)\b",
    re.I | re.M,
)


@dataclass(frozen=True)
class DynamicElementStateSpec:
    source: str
    mode: DynamicElementMode
    choices: tuple[str, ...] = ()
    cycle: tuple[str, ...] = ()
    initial_element: str | None = None


@dataclass(frozen=True)
class RuntimeActionDefinition:
    source: AuthoredActionSource
    action: CombatAction | None
    blockers: tuple[str, ...]
    repetition_lock_rounds: int | None
    non_damage: bool
    triggered: bool = False
    minimum_round: int = 1
    maximum_uses: int | None = None
    forced_follow_up: str | None = None
    forced_by_action: str | None = None
    requires_preparation: str | None = None
    target_tags: tuple[str, ...] = ()
    exclude_actor: bool = False
    fallback_action: str | None = None
    formation_required: bool = False
    dynamic_element_source: str | None = None
    elemental_status_riders: tuple[tuple[str, str, int], ...] = ()


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
    dynamic_element_states: tuple[DynamicElementStateSpec, ...] = ()

    @property
    def executable(self) -> bool:
        return self.kind in {"generic", "formation", "special"}

    @property
    def direct_damage_actions(self) -> tuple[CombatAction, ...]:
        return tuple(
            item.action for item in self.actions
            if item.action is not None and item.action.action_kind == "damage" and not item.triggered
        )

    @property
    def effect_actions(self) -> tuple[CombatAction, ...]:
        return tuple(
            item.action for item in self.actions
            if item.action is not None and item.action.action_kind == "effect" and not item.triggered
        )


@dataclass(frozen=True)
class RuntimeCoverageSummary:
    total_owner_sheets: int
    enemy_sheets: int
    components: int
    generic: int
    formation: int
    special: int
    blocked: int
    unclassified: int
    definitions: tuple[EnemyRuntimeDefinition, ...]

    @property
    def executable(self) -> int:
        return self.generic + self.formation + self.special

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


def _runtime_tags(text: str) -> frozenset[str]:
    tags: set[str] = set()
    if re.search(r"\bTrue\s+construct\b", text, re.I):
        tags.add("construct")
    if re.search(r"\bTrue\s+machine\b|\*\*Role:\*\*[^\n]*\bmachine\b", text, re.I):
        tags.add("machine")
    return frozenset(tags)


def _first_stat_row(text: str):
    rows = find_markdown_table(text, ("HP",))
    if not rows:
        raise SourceGapError("no HP-bearing stat table")
    return parse_stat_row(rows[0])


def _first_content_line(body: str) -> str:
    for raw_line in body.splitlines():
        line = raw_line.strip()
        if line:
            return line
    return ""


def _looks_like_action_section(body: str) -> bool:
    first_line = _first_content_line(body)
    return bool(first_line and _ACTION_LEAD.search(first_line))


def _action_blocks(text: str) -> tuple[tuple[str, str], ...]:
    matches = list(re.finditer(r"^(#{2,5})\s+(.+?)\s*$", text, re.M))
    result: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        if not _looks_like_action_section(body) or not _POWER_AUTHORITY.search(body):
            continue
        result.append((re.sub(r"\*+", "", match.group(2)).strip(), body))
    return tuple(result)


def _repetition_lock(raw_text: str) -> int | None:
    match = re.search(r"(\d+)[- ]round repetition lock", raw_text, re.I)
    return int(match.group(1)) if match else None


def _non_damage(raw_text: str) -> bool:
    return bool(re.search(r"Power\s*:\s*(?:\*\*)?N/?A\b|no direct damage", raw_text, re.I))


def _requires_preparation(raw_text: str) -> str | None:
    match = _REQUIRES_PREPARATION_RE.search(raw_text)
    return match.group(1).strip() if match else None


def _elemental_status_riders(raw_text: str) -> tuple[tuple[str, str, int], ...]:
    return tuple(
        (element.lower(), status.lower(), int(chance))
        for element, chance, status in _ELEMENTAL_RIDER_RE.findall(raw_text)
    )


def _dynamic_element_state_specs(text: str) -> tuple[DynamicElementStateSpec, ...]:
    specs: list[DynamicElementStateSpec] = []

    assignment = re.search(
        r"assigned\s+exactly\s+one\s*:[ \t]*"
        r"((?:\r?\n[ \t]*-[ \t]*(?:Fire|Ice|Lightning|Earth)[ \t]*){2,})",
        text,
        re.I,
    )
    if assignment:
        choices = tuple(
            item.lower()
            for item in re.findall(r"-\s*(Fire|Ice|Lightning|Earth)\b", assignment.group(1), re.I)
        )
        if choices:
            specs.append(DynamicElementStateSpec("assigned_element", "random_once", choices=choices))

    begins = re.search(r"begins\s+in\s+(Fire|Ice|Lightning|Earth)\s+expression", text, re.I)
    cycle_line = re.search(
        r"(Fire|Ice|Lightning|Earth)\s*→\s*(Fire|Ice|Lightning|Earth)\s*→\s*"
        r"(Fire|Ice|Lightning|Earth)\s*→\s*(Fire|Ice|Lightning|Earth)\s*→\s*"
        r"(Fire|Ice|Lightning|Earth)",
        text,
        re.I,
    )
    if begins and cycle_line:
        raw_cycle = tuple(item.lower() for item in cycle_line.groups())
        cycle = raw_cycle[:-1] if raw_cycle[-1] == raw_cycle[0] else raw_cycle
        initial = begins.group(1).lower()
        if initial in cycle:
            while cycle[0] != initial:
                cycle = cycle[1:] + cycle[:1]
            specs.append(DynamicElementStateSpec(
                "current_expression", "round_cycle", cycle=cycle,
                initial_element=initial,
            ))

    return tuple(specs)


def _direct_action(
    source: AuthoredActionSource,
    *,
    triggered: bool,
    dynamic_states: dict[str, DynamicElementStateSpec],
) -> tuple[CombatAction | None, tuple[str, ...], str | None, tuple[tuple[str, str, int], ...]]:
    blockers: list[str] = []
    for field in ("target_scope", "damage_kind", "power", "base_hit"):
        if getattr(source, field) is None:
            blockers.append(f"{source.name}: missing {field}")

    dynamic_source: str | None = None
    dynamic_riders: tuple[tuple[str, str, int], ...] = ()
    if source.element_mode == "dynamic":
        dynamic_source = source.element_source
        if dynamic_source is None or dynamic_source not in dynamic_states:
            blockers.append(
                f"{source.name}: dynamic element requires encounter-state resolver ({source.element_source})"
            )
        else:
            dynamic_riders = _elemental_status_riders(source.raw_text)
            if source.status_chances and not dynamic_riders:
                blockers.append(
                    f"{source.name}: dynamic element has unresolved element-dependent status rider"
                )
    elif source.element is None:
        blockers.append(f"{source.name}: missing fixed element")

    if source.is_multihit:
        blockers.append(f"{source.name}: multihit requires encounter/action-specific runtime")
    if triggered:
        blockers.append(f"{source.name}: triggered/passive action requires runtime trigger")
    if blockers:
        return None, tuple(blockers), dynamic_source, dynamic_riders

    assert source.target_scope in {"one", "all"}
    assert source.damage_kind in {"physical", "magical", "hybrid"}
    assert source.power is not None and source.base_hit is not None
    element = source.element if source.element is not None else "neutral"
    static_riders = () if dynamic_source is not None else tuple(
        StatusRider(status, chance) for status, chance in source.status_chances
    )
    return CombatAction(
        source.name,
        target_scope=source.target_scope,
        damage_kind=source.damage_kind,
        element=element,
        power=source.power,
        base_hit=source.base_hit,
        physical_weight=source.physical_weight,
        magical_weight=source.magical_weight,
        weight=source.weight,
        status_riders=static_riders,
    ), (), dynamic_source, dynamic_riders


def load_enemy_runtime_definition(source_path: str, *, category: str, root: Path | None = None) -> EnemyRuntimeDefinition:
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
    if _FIXED_SEQUENCE_RULE.search(text):
        blockers.append("authored fixed action sequence/cycle requires runtime scheduler")

    dynamic_specs = _dynamic_element_state_specs(text)
    dynamic_states = {spec.source: spec for spec in dynamic_specs}

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
                runtime_tags=_runtime_tags(text),
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
        non_damage = _non_damage(raw_text)
        kwargs: dict[str, object] = {}
        dynamic_source: str | None = None
        dynamic_riders: tuple[tuple[str, str, int], ...] = ()
        if non_damage and not triggered:
            parsed = parse_enemy_effect_action(action_name, raw_text)
            action = parsed.action
            action_blockers = tuple(f"{action_name}: {item}" for item in parsed.blockers)
            kwargs = {
                "minimum_round": parsed.minimum_round,
                "maximum_uses": parsed.maximum_uses,
                "forced_follow_up": parsed.forced_follow_up,
                "forced_by_action": parsed.forced_by_action,
                "target_tags": parsed.target_tags,
                "exclude_actor": parsed.exclude_actor,
                "fallback_action": parsed.fallback_action,
                "formation_required": parsed.formation_required,
            }
        else:
            action, action_blockers, dynamic_source, dynamic_riders = _direct_action(
                source, triggered=triggered, dynamic_states=dynamic_states,
            )

        action_defs.append(RuntimeActionDefinition(
            source=source,
            action=action,
            blockers=action_blockers,
            repetition_lock_rounds=_repetition_lock(raw_text),
            non_damage=non_damage,
            triggered=triggered,
            requires_preparation=_requires_preparation(raw_text),
            dynamic_element_source=dynamic_source,
            elemental_status_riders=dynamic_riders,
            **kwargs,
        ))
        blockers.extend(action_blockers)

    executable_actions = tuple(
        item.action for item in action_defs if item.action is not None and not item.triggered
    )
    if combatant is not None and executable_actions:
        combatant = Combatant(
            name=combatant.name,
            side=combatant.side,
            stats=combatant.stats,
            actions=executable_actions,
            evasion=combatant.evasion,
            direct_damage_reduction=combatant.direct_damage_reduction,
            rank=combatant.rank,
            status_resistance=combatant.status_resistance,
            status_immunities=combatant.status_immunities,
            elemental_affinities=combatant.elemental_affinities,
            runtime_tags=combatant.runtime_tags,
        )
    elif combatant is not None and not executable_actions:
        blockers.append("no generic selected action is executable")

    unique_blockers = tuple(dict.fromkeys(blockers))
    if unique_blockers:
        kind: RuntimeKind = "blocked"
        combatant_out = None
    else:
        kind = "formation" if any(item.formation_required for item in action_defs) else "generic"
        combatant_out = combatant
    return EnemyRuntimeDefinition(
        name, category, source_path, kind, displayed_level, combatant_out,
        tuple(action_defs), unique_blockers,
        dynamic_element_states=dynamic_specs,
    )


def build_enemy_runtime_catalog(*, root: Path | None = None) -> tuple[EnemyRuntimeDefinition, ...]:
    return tuple(
        load_enemy_runtime_definition(path, category=category, root=root)
        for category, path in discover_enemy_owner_paths(root=root)
    )


def audit_enemy_runtime_coverage(*, root: Path | None = None) -> RuntimeCoverageSummary:
    definitions = build_enemy_runtime_catalog(root=root)
    components = sum(item.kind == "component" for item in definitions)
    generic = sum(item.kind == "generic" for item in definitions)
    formation = sum(item.kind == "formation" for item in definitions)
    special = sum(item.kind == "special" for item in definitions)
    blocked = sum(item.kind == "blocked" for item in definitions)
    enemy_sheets = len(definitions) - components
    return RuntimeCoverageSummary(
        len(definitions), enemy_sheets, components, generic, formation, special, blocked,
        len(definitions) - components - generic - formation - special - blocked,
        definitions,
    )


__all__ = [
    "DynamicElementStateSpec", "EnemyRuntimeDefinition", "OWNER_DIRS", "RuntimeActionDefinition",
    "RuntimeCoverageSummary", "SPECIAL_RUNTIME_PATHS", "audit_enemy_runtime_coverage",
    "build_enemy_runtime_catalog", "discover_enemy_owner_paths", "load_enemy_runtime_definition",
]
