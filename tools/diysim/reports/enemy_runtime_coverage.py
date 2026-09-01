"""Human/JSON friendly DiySim enemy-runtime coverage reporting."""
from __future__ import annotations

from pathlib import Path

from tools.diysim.encounters.runtime_catalog import audit_enemy_runtime_coverage


def enemy_runtime_coverage_dict(*, root: Path | None = None, include_definitions: bool = True) -> dict[str, object]:
    report = audit_enemy_runtime_coverage(root=root)
    payload: dict[str, object] = {
        "total_owner_sheets": report.total_owner_sheets,
        "generic": report.generic,
        "special": report.special,
        "blocked": report.blocked,
        "unclassified": report.unclassified,
        "executable": report.executable,
        "coverage_rate": report.coverage_rate,
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
