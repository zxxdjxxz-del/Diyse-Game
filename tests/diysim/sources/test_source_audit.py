from __future__ import annotations

from tools.diysim.sources.abilities import load_ability_registry
from tools.diysim.sources.actors import load_enemy_registry
from tools.diysim.sources.audit import audit_repo_sources
from tools.diysim.sources.traits import load_trait_registry


def test_repo_source_audit_resolves_current_core_authority() -> None:
    report = audit_repo_sources()

    assert report.progression_loaded
    assert report.class_cexp_loaded
    assert report.donor_equipment_access_loaded
    assert report.relic_progression_loaded
    assert report.legacy_progression_loaded
    assert report.combat_loaded
    assert report.party_rules_loaded
    assert report.enemy_system_loaded
    assert report.class_level_thresholds == 13
    assert report.class_recruitment_rows == 6
    assert report.campaign_cexp_chapters == 13
    assert report.donor_equipment_access_rows == 6
    assert report.relic_placement_rows == 36
    assert report.relic_weapon_rows == 16
    assert report.legacy_item_rows == 17
    assert report.legacy_donor_rows == 6
    assert report.ability_entries == len(load_ability_registry())
    assert report.ability_sources_resolved == report.ability_entries
    assert report.trait_packages == len(load_trait_registry())
    assert report.enemy_registry_entries == len(load_enemy_registry())
    assert report.ok
    assert report.issues == ()
