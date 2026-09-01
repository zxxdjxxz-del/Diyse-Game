from __future__ import annotations

from tools.diysim.sources.abilities import load_ability_registry
from tools.diysim.sources.audit import audit_repo_sources
from tools.diysim.sources.traits import load_trait_registry


def test_repo_source_audit_resolves_current_core_authority() -> None:
    report = audit_repo_sources()

    assert report.progression_loaded
    assert report.combat_loaded
    assert report.ability_entries == len(load_ability_registry())
    assert report.ability_sources_resolved == report.ability_entries
    assert report.trait_packages == len(load_trait_registry())
    assert report.ok
    assert report.issues == ()
