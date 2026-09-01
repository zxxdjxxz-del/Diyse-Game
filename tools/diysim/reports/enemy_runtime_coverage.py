"""Human/JSON friendly DiySim enemy-runtime coverage reporting."""
from __future__ import annotations

from collections import Counter
from pathlib import Path

from tools.diysim.encounters.runtime_catalog import audit_enemy_runtime_coverage


def enemy_runtime_coverage_dict(*, root: Path | None = None, include_definitions: bool = True) -> dict[str, object]:
    report = audit_enemy_runtime_coverage(root=root)
    blocked_by_category = Counter(
        definition.category for definition in report.definitions if definition.kind == "blocked"
    )
    blocker_families = Counter()
    for definition in report.definitions:
        if definition.kind != "blocked":
            continue
        for blocker in definition.blockers:
            if "dynamic element" in blocker:
                family = "dynamic_element"
            elif "multihit" in blocker:
                family = "multihit"
            elif "non-damage effect" in blocker:
                family = "non_damage_effect"
            elif "triggered/passive" in blocker:
                family = "triggered_passive"
            elif "state/phase/form" in blocker:
                family = "state_phase_form"
            elif "sequence/cycle" in blocker:
                family = "action_sequence"
            elif "missing" in blocker or "stat parser" in blocker:
                family = "source_or_parser_gap"
            else:
                family = "other"
            blocker_families[family] += 1

    payload: dict[str, object] = {
        "total_owner_sheets": report.total_owner_sheets,
        "enemy_sheets": report.enemy_sheets,
        "support_components": report.components,
        "generic": report.generic,
        "special": report.special,
        "blocked": report.blocked,
        "unclassified": report.unclassified,
        "executable": report.executable,
        "coverage_rate": report.coverage_rate,
        "blocked_by_category": dict(sorted(blocked_by_category.items())),
        "blocker_families": dict(sorted(blocker_families.items())),
    }
    if include_definitions:
        payload["definitions"] = [
            {
                "name": definition.name,
                "category": definition.category,
                "source_path": definition.source_path,
                "kind": definition.kind,
                "displayed_level": definition.displayed_level,
                "special_runtime": definition.special_runtime,
                "direct_damage_actions": [action.name for action in definition.direct_damage_actions],
                "blockers": list(definition.blockers),
            }
            for definition in report.definitions
        ]
    return payload


__all__ = ["enemy_runtime_coverage_dict"]
