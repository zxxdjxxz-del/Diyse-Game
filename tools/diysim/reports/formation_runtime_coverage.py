"""Coverage reporting for repo-owned ordinary encounter formations."""
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import re

from tools.diysim.encounters.formation_catalog import build_formation_catalog

NUMBERED_CHAPTERS = tuple(range(14))


def _chapter_key(source_path: str) -> str:
    match = re.search(r"CHAPTER_(\d+)_FORMATIONS\.md$", source_path)
    return str(int(match.group(1))) if match else Path(source_path).stem


def formation_runtime_coverage_dict(*, root: Path | None = None, include_formations: bool = True) -> dict[str, object]:
    formations = build_formation_catalog(root=root)
    ready = [formation for formation in formations if formation.runtime_ready]
    blocked = [formation for formation in formations if not formation.runtime_ready]

    by_chapter: dict[str, dict[str, int]] = defaultdict(lambda: {"total": 0, "runtime_ready": 0, "blocked": 0})
    # Keep every numbered story chapter visible in the report even when the repo
    # intentionally has no ordinary-formation owner file for that chapter.
    for chapter in NUMBERED_CHAPTERS:
        by_chapter[str(chapter)]

    source_chapters = sorted(
        {_chapter_key(formation.source_path) for formation in formations},
        key=lambda value: int(value) if value.isdigit() else 999,
    )
    chapters_without_formation_source = [
        str(chapter) for chapter in NUMBERED_CHAPTERS if str(chapter) not in source_chapters
    ]

    unresolved_labels = Counter()
    blocked_members = Counter()
    propagated_enemy_blockers = Counter()

    for formation in formations:
        chapter = _chapter_key(formation.source_path)
        by_chapter[chapter]["total"] += 1
        by_chapter[chapter]["runtime_ready" if formation.runtime_ready else "blocked"] += 1
        for member in formation.members:
            if member.enemy is None:
                unresolved_labels[member.label] += 1
                continue
            if member.enemy.kind == "blocked":
                blocked_members[member.enemy.name] += 1
                for blocker in member.enemy.blockers:
                    propagated_enemy_blockers[blocker] += 1

    payload: dict[str, object] = {
        "total_formations": len(formations),
        "runtime_ready": len(ready),
        "blocked": len(blocked),
        "coverage_rate": len(ready) / len(formations) if formations else 1.0,
        "formation_source_chapters": source_chapters,
        "chapters_without_formation_source": chapters_without_formation_source,
        "unresolved_owner_labels": dict(sorted(unresolved_labels.items())),
        "blocked_member_runtimes": dict(sorted(blocked_members.items())),
        "propagated_enemy_blockers": dict(sorted(propagated_enemy_blockers.items())),
        "by_chapter": dict(sorted(by_chapter.items(), key=lambda item: int(item[0]) if item[0].isdigit() else 999)),
    }
    if include_formations:
        payload["formations"] = [
            {
                "chapter": _chapter_key(formation.source_path),
                "name": formation.name,
                "composition": formation.composition_text,
                "weight": formation.weight,
                "phase": formation.phase,
                "source_path": formation.source_path,
                "runtime_ready": formation.runtime_ready,
                "blockers": list(formation.blockers),
                "members": [
                    {
                        "count": member.count,
                        "label": member.label,
                        "enemy": member.enemy.name if member.enemy else None,
                        "runtime_kind": member.enemy.kind if member.enemy else None,
                        "blocker": member.blocker,
                    }
                    for member in formation.members
                ],
            }
            for formation in formations
        ]
    return payload


__all__ = ["formation_runtime_coverage_dict"]
