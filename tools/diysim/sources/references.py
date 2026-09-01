"""Resolve action summaries that explicitly enable behavior owned elsewhere."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from .actions import AuthoredActionSource, parse_authored_action_text


@dataclass(frozen=True)
class ActionOwnerMatch:
    name: str
    path: str
    source: AuthoredActionSource

    @property
    def complete_direct_damage(self) -> bool:
        return (
            self.source.target_scope in {"one", "all"}
            and self.source.damage_kind in {"physical", "magical", "hybrid"}
            and self.source.has_element_identity
            and self.source.power is not None
            and self.source.base_hit is not None
        )


@dataclass(frozen=True)
class EnabledActionReferenceResolution:
    names: tuple[str, ...]
    matches: tuple[ActionOwnerMatch, ...]

    @property
    def complete(self) -> bool:
        return bool(self.names) and len(self.matches) == len(self.names) and all(
            match.complete_direct_damage for match in self.matches
        )


def _normalize_enabled_name(value: str) -> str:
    name = value.strip().strip("*`")
    # Capability summaries may qualify an enabled action without changing its
    # actual owner heading, e.g. "if inherited, Perfected Siphon". Strip only
    # the known conditional prefix so owner lookup remains exact and does not
    # silently fuzzy-match arbitrary prose.
    name = re.sub(
        r"^(?:if\s+(?:inherited|surviving|survived),\s*)",
        "",
        name,
        flags=re.I,
    )
    return name.strip()


def enabled_damage_action_names(block: str) -> tuple[str, ...]:
    """Extract damaging action names from an `Enables:` capability summary."""
    if not re.search(r"(?:^|\n)Enables:\s*$", block, re.I | re.M):
        return ()
    names: list[str] = []
    for line in block.splitlines():
        match = re.match(
            r"^\s*-\s+(.+?)\s*[—-]\s*(\d+)\s+Power\b",
            line,
            re.I,
        )
        if match:
            names.append(_normalize_enabled_name(match.group(1)))
    return tuple(dict.fromkeys(names))


def _heading_block(text: str, name: str) -> str | None:
    matches = list(re.finditer(r"^(#{2,6})\s+(.+?)\s*$", text, re.M))
    for index, match in enumerate(matches):
        if match.group(2).strip().casefold() != name.casefold():
            continue
        level = len(match.group(1))
        end = len(text)
        for later in matches[index + 1 :]:
            if len(later.group(1)) <= level:
                end = later.start()
                break
        return text[match.end():end].strip()
    return None


def _owner_markdown_paths(repo_root: Path) -> tuple[Path, ...]:
    owner_root = repo_root / "docs" / "09_ENEMIES_AND_ENCOUNTERS"
    if not owner_root.exists():
        return ()
    return tuple(sorted(owner_root.rglob("*.md")))


def resolve_enabled_action_references(
    block: str,
    *,
    repo_root: Path,
    current_path: Path | None = None,
) -> EnabledActionReferenceResolution:
    names = enabled_damage_action_names(block)
    matches: list[ActionOwnerMatch] = []
    current_resolved = current_path.resolve() if current_path is not None else None

    for name in names:
        found: list[ActionOwnerMatch] = []
        for path in _owner_markdown_paths(repo_root):
            if current_resolved is not None and path.resolve() == current_resolved:
                continue
            text = path.read_text(encoding="utf-8")
            action_block = _heading_block(text, name)
            if action_block is None:
                continue
            found.append(ActionOwnerMatch(
                name=name,
                path=path.relative_to(repo_root).as_posix(),
                source=parse_authored_action_text(name, action_block),
            ))
        # Ambiguous references are deliberately unresolved. Exactly one owner is
        # required so the simulator cannot silently choose among duplicate names.
        if len(found) == 1:
            matches.append(found[0])

    return EnabledActionReferenceResolution(names=names, matches=tuple(matches))


__all__ = [
    "ActionOwnerMatch",
    "EnabledActionReferenceResolution",
    "enabled_damage_action_names",
    "resolve_enabled_action_references",
]
