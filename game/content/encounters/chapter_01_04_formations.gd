extends RefCounted
class_name DiyseChapter0104FormationCatalog

const TIER_NAMES := ["light", "standard", "heavy"]

# Engineering/runtime formation catalog.
# Chapter 1 has been reconciled to the current 2026-09-22 enemy-placement locks.
# Hunts, mandatory named encounters, and bosses are absent from random pools.
# Strong normal-pool enemies such as Watch Captain Frame may appear where current canon permits.
# Chapter-1 formation weights here are executable engineering placeholders. Structural composition/subarea
# eligibility is current; final selection frequency remains open pending the later level/progression rebalance.
const AREAS := {
	"ch01_greenhollow": {
		"chapter": 1,
		"max_enemies": 2,
		"formations": {
			"light": [
				{"id": "ch01_greenhollow_l01", "weight": 50.0, "exp": 45, "enemies": ["Greenhollow Stalker", "Thornvine Creeper"], "subareas": ["upper_briar_west", "upper_briar_east"]},
				{"id": "ch01_greenhollow_l02", "weight": 50.0, "exp": 45, "enemies": ["Greenhollow Stalker", "Greenhollow Stalker"], "subareas": ["upper_briar_west", "upper_briar_east"]},
			],
			"standard": [
				{"id": "ch01_greenhollow_s01", "weight": 50.0, "exp": 55, "enemies": ["Briar Boar", "Thornvine Creeper"], "subareas": ["upper_briar_west", "upper_briar_east"]},
				{"id": "ch01_greenhollow_s02", "weight": 50.0, "exp": 55, "enemies": ["Greenhollow Stalker", "Briar Boar"], "subareas": ["upper_briar_west", "upper_briar_east"]},
			],
			"heavy": [
				{"id": "ch01_greenhollow_h01", "weight": 50.0, "exp": 70, "enemies": ["Thornvine Creeper", "Thornvine Creeper"], "subareas": ["upper_briar_east"]},
				{"id": "ch01_greenhollow_h02", "weight": 50.0, "exp": 70, "enemies": ["Briar Boar", "Briar Boar"], "subareas": ["upper_briar_east"]},
			],
		},
	},
	"ch01_hollow_watch": {
		"chapter": 1,
		"max_enemies": 4,
		"formations": {
			"light": [
				{"id": "ch01_hollow_watch_l01", "weight": 50.0, "exp": 45, "enemies": ["Black Host Raider", "Black Host Raider", "Black Host Crossbowman"], "subareas": ["hw_approach", "hw_surface", "hw_excavation_early", "hw_excavation_transition"]},
				{"id": "ch01_hollow_watch_l02", "weight": 50.0, "exp": 45, "enemies": ["Hollow Watch Sentry", "Hollow Watch Sentry"], "subareas": ["hw_excavation_transition", "hw_excavation_deep", "hw_surviving_channel", "hw_protected_inner"]},
			],
			"standard": [
				{"id": "ch01_hollow_watch_s01", "weight": 50.0, "exp": 55, "enemies": ["Black Host Raider", "Black Host Crossbowman", "Ruin Shieldbearer"], "subareas": ["hw_approach", "hw_surface", "hw_excavation_early", "hw_excavation_transition"]},
				{"id": "ch01_hollow_watch_s02", "weight": 50.0, "exp": 55, "enemies": ["Hollow Watch Sentry", "Hollow Watch Sentry", "Hollow Watch Ballista"], "subareas": ["hw_excavation_transition", "hw_excavation_deep", "hw_surviving_channel", "hw_protected_inner"]},
			],
			"heavy": [
				{"id": "ch01_hollow_watch_h01", "weight": 34.0, "exp": 70, "enemies": ["Black Host Crossbowman", "Black Host Crossbowman", "Ruin Shieldbearer"], "subareas": ["hw_approach", "hw_surface", "hw_excavation_early", "hw_excavation_transition"]},
				{"id": "ch01_hollow_watch_h02", "weight": 33.0, "exp": 70, "enemies": ["Hollow Watch Sentry", "Hollow Watch Ballista", "Hollow Watch Ballista"], "subareas": ["hw_excavation_transition", "hw_excavation_deep", "hw_surviving_channel", "hw_protected_inner"]},
				{"id": "ch01_hollow_watch_h03", "weight": 33.0, "exp": 70, "enemies": ["Watch Captain Frame", "Hollow Watch Sentry", "Hollow Watch Ballista"], "subareas": ["hw_excavation_deep", "hw_surviving_channel", "hw_protected_inner"]},
			],
		},
	},
	"ch01_briar_south": {
		"chapter": 1,
		"max_enemies": 5,
		"formations": {
			"light": [
				{"id": "ch01_briar_south_l01", "weight": 50.0, "exp": 45, "enemies": ["Needlewing", "Greenhollow Stalker", "Briar Boar"], "subareas": ["south_opening", "south_hard_middle", "south_side_approach", "south_final_leg", "south_cleanup_return"]},
				{"id": "ch01_briar_south_l02", "weight": 50.0, "exp": 45, "enemies": ["Rootmaw", "Thornvine Creeper", "Needlewing"], "subareas": ["south_opening", "south_hard_middle", "south_side_approach"]},
			],
			"standard": [
				{"id": "ch01_briar_south_s01", "weight": 50.0, "exp": 55, "enemies": ["Rootmaw", "Thornvine Creeper", "Thornvine Creeper", "Needlewing"], "subareas": ["south_hard_middle", "south_side_approach"]},
				{"id": "ch01_briar_south_s02", "weight": 50.0, "exp": 55, "enemies": ["Brambleback", "Briar Boar", "Thornvine Creeper"], "subareas": ["south_opening", "south_hard_middle", "south_side_approach", "south_final_leg", "south_cleanup_return"]},
			],
			"heavy": [
				{"id": "ch01_briar_south_h01", "weight": 50.0, "exp": 70, "enemies": ["Brambleback", "Briar Boar", "Rootmaw", "Thornvine Creeper"], "subareas": ["south_hard_middle", "south_final_leg", "south_cleanup_return"]},
				{"id": "ch01_briar_south_h02", "weight": 50.0, "exp": 70, "enemies": ["Needlewing", "Needlewing", "Greenhollow Stalker", "Rootmaw", "Briar Boar"], "subareas": ["south_hard_middle", "south_final_leg", "south_cleanup_return"]},
			],
		},
	},
	"ch02_dunmere_waterworks": {
		"chapter": 2,
		"formations": {
			"light": [
				{"id": "ch02_dunmere_l01", "weight": 50.0, "exp": 130, "enemies": ["Cistern Leech", "Cistern Leech", "Bogshell"]},
				{"id": "ch02_dunmere_l02", "weight": 50.0, "exp": 130, "enemies": ["Needlewing", "Cistern Leech", "Cistern Leech"]},
			],
			"standard": [
				{"id": "ch02_dunmere_s01", "weight": 50.0, "exp": 165, "enemies": ["Needlewing", "Bogshell", "Cistern Leech"]},
				{"id": "ch02_dunmere_s02", "weight": 50.0, "exp": 165, "enemies": ["Bogshell", "Bogshell", "Cistern Leech", "Cistern Leech"]},
			],
			"heavy": [
				{"id": "ch02_dunmere_h01", "weight": 50.0, "exp": 200, "enemies": ["Needlewing", "Needlewing", "Bogshell", "Cistern Leech"]},
				{"id": "ch02_dunmere_h02", "weight": 50.0, "exp": 200, "enemies": ["Needlewing", "Bogshell", "Cistern Leech", "Cistern Leech"]},
			],
		},
	},
	"ch02_sunken_archive": {
		"chapter": 2,
		"formations": {
			"light": [
				{"id": "ch02_archive_l01", "weight": 50.0, "exp": 130, "enemies": ["Archive Current", "Memory Scribe", "Hollow Watch Sentry"]},
				{"id": "ch02_archive_l02", "weight": 50.0, "exp": 130, "enemies": ["Needlewing", "Archive Current", "Cistern Leech"]},
			],
			"standard": [
				{"id": "ch02_archive_s01", "weight": 50.0, "exp": 165, "enemies": ["Memory Scribe", "Hollow Watch Sentry", "Archive Current", "Archive Current"]},
				{"id": "ch02_archive_s02", "weight": 50.0, "exp": 165, "enemies": ["Bogshell", "Cistern Leech", "Needlewing", "Archive Current"]},
			],
			"heavy": [
				{"id": "ch02_archive_h01", "weight": 50.0, "exp": 200, "enemies": ["Memory Scribe", "Hollow Watch Sentry", "Hollow Watch Sentry", "Archive Current"]},
				{"id": "ch02_archive_h02", "weight": 50.0, "exp": 200, "enemies": ["Needlewing", "Bogshell", "Cistern Leech", "Memory Scribe"]},
			],
		},
	},
	"ch02_red_transfer_bastion": {
		"chapter": 2,
		"formations": {
			"light": [
				{"id": "ch02_bastion_l01", "weight": 50.0, "exp": 130, "enemies": ["Bastion Crossbow Guard", "Transfer Adept", "Black Host Raider"]},
				{"id": "ch02_bastion_l02", "weight": 50.0, "exp": 130, "enemies": ["Bastion Shield Guard", "Beast Handler", "Rift Hound"]},
			],
			"standard": [
				{"id": "ch02_bastion_s01", "weight": 50.0, "exp": 165, "enemies": ["Bastion Shield Guard", "Bastion Crossbow Guard", "Transfer Adept", "Rift Hound"]},
				{"id": "ch02_bastion_s02", "weight": 50.0, "exp": 165, "enemies": ["Bastion Shield Guard", "Black Host Raider", "Beast Handler", "Rift Hound"]},
			],
			"heavy": [
				{"id": "ch02_bastion_h01", "weight": 50.0, "exp": 200, "enemies": ["Bastion Shield Guard", "Bastion Crossbow Guard", "Bastion Crossbow Guard", "Transfer Adept"]},
				{"id": "ch02_bastion_h02", "weight": 50.0, "exp": 200, "enemies": ["Bastion Shield Guard", "Transfer Adept", "Beast Handler", "Rift Hound"]},
			],
		},
	},
	"ch03_way_fort": {
		"chapter": 3,
		"formations": {
			"light": [
				{"id": "ch03_wayfort_l01", "weight": 50.0, "exp": 215, "enemies": ["Way-Fort Marauder", "Rift Boltman", "Black Host Ward-Sorcerer"]},
				{"id": "ch03_wayfort_l02", "weight": 50.0, "exp": 215, "enemies": ["Way-Fort Marauder", "Way-Fort Marauder", "Rift Boltman"]},
			],
			"standard": [
				{"id": "ch03_wayfort_s01", "weight": 50.0, "exp": 280, "enemies": ["Way-Fort Marauder", "Way-Fort Marauder", "Rift Boltman", "Black Host Ward-Sorcerer"]},
				{"id": "ch03_wayfort_s02", "weight": 50.0, "exp": 280, "enemies": ["Way-Fort Marauder", "Rift Boltman", "Rift Boltman", "Black Host Ward-Sorcerer"]},
			],
			"heavy": [
				{"id": "ch03_wayfort_h01", "weight": 50.0, "exp": 315, "enemies": ["Way-Fort Marauder", "Way-Fort Marauder", "Rift Boltman", "Rift Boltman", "Black Host Ward-Sorcerer"]},
				{"id": "ch03_wayfort_h02", "weight": 50.0, "exp": 315, "enemies": ["Way-Fort Marauder", "Way-Fort Marauder", "Way-Fort Marauder", "Rift Boltman", "Black Host Ward-Sorcerer"]},
			],
		},
	},
	"ch03_suppressed_archives": {
		"chapter": 3,
		"formations": {
			"light": [
				{"id": "ch03_archives_l01", "weight": 50.0, "exp": 215, "enemies": ["Archive Scribe Engine", "Judgment Frame", "Erasure Wisp"]},
				{"id": "ch03_archives_l02", "weight": 50.0, "exp": 215, "enemies": ["Archive Scribe Engine", "Erasure Wisp", "Erasure Wisp"]},
			],
			"standard": [
				{"id": "ch03_archives_s01", "weight": 50.0, "exp": 280, "enemies": ["Judgment Frame", "Archive Scribe Engine", "Erasure Wisp", "Erasure Wisp"]},
				{"id": "ch03_archives_s02", "weight": 50.0, "exp": 280, "enemies": ["Judgment Frame", "Judgment Frame", "Archive Scribe Engine", "Erasure Wisp"]},
			],
			"heavy": [
				{"id": "ch03_archives_h01", "weight": 50.0, "exp": 315, "enemies": ["Judgment Frame", "Judgment Frame", "Archive Scribe Engine", "Erasure Wisp", "Erasure Wisp"]},
				{"id": "ch03_archives_h02", "weight": 50.0, "exp": 315, "enemies": ["Judgment Frame", "Archive Scribe Engine", "Archive Scribe Engine", "Erasure Wisp", "Erasure Wisp"]},
			],
		},
	},
	"ch03_command_station": {
		"chapter": 3,
		"formations": {
			"light": [
				{"id": "ch03_command_l01", "weight": 50.0, "exp": 215, "enemies": ["Command-Station Sentry", "Authority Lens", "Command Ring Drone"]},
				{"id": "ch03_command_l02", "weight": 50.0, "exp": 215, "enemies": ["Command-Station Sentry", "Command Ring Drone", "Command Ring Drone"]},
			],
			"standard": [
				{"id": "ch03_command_s01", "weight": 50.0, "exp": 280, "enemies": ["Command-Station Sentry", "Command-Station Sentry", "Authority Lens", "Command Ring Drone"]},
				{"id": "ch03_command_s02", "weight": 50.0, "exp": 280, "enemies": ["Command-Station Sentry", "Authority Lens", "Command Ring Drone", "Command Ring Drone"]},
			],
			"heavy": [
				{"id": "ch03_command_h01", "weight": 50.0, "exp": 315, "enemies": ["Command-Station Sentry", "Command-Station Sentry", "Authority Lens", "Command Ring Drone", "Command Ring Drone"]},
				{"id": "ch03_command_h02", "weight": 50.0, "exp": 315, "enemies": ["Command-Station Sentry", "Authority Lens", "Authority Lens", "Command Ring Drone", "Command Ring Drone"]},
			],
		},
	},
	"ch04_reaction_annex": {
		"chapter": 4,
		"formations": {
			"light": [
				{"id": "ch04_annex_l01", "weight": 50.0, "exp": 315, "enemies": ["Reaction Node", "Reaction Node", "Reaction Hound", "Element Mirror"]},
				{"id": "ch04_annex_l02", "weight": 50.0, "exp": 315, "enemies": ["Composite Elemental", "Reaction Node", "Reaction Hound", "Element Mirror"]},
			],
			"standard": [
				{"id": "ch04_annex_s01", "weight": 50.0, "exp": 375, "enemies": ["Composite Elemental", "Reaction Node", "Reaction Node", "Reaction Hound", "Element Mirror"]},
				{"id": "ch04_annex_s02", "weight": 50.0, "exp": 375, "enemies": ["Annex Crucible Guard", "Reaction Node", "Reaction Hound", "Element Mirror", "Element Mirror"]},
			],
			"heavy": [
				{"id": "ch04_annex_h01", "weight": 50.0, "exp": 460, "enemies": ["Composite Elemental", "Annex Crucible Guard", "Reaction Node", "Reaction Hound", "Element Mirror", "Element Mirror"]},
				{"id": "ch04_annex_h02", "weight": 50.0, "exp": 460, "enemies": ["Composite Elemental", "Composite Elemental", "Reaction Node", "Reaction Hound", "Element Mirror", "Annex Crucible Guard"]},
			],
		},
	},
}

static func has_area(area_id: String) -> bool:
	return AREAS.has(area_id)

static func area_ids() -> Array[String]:
	var result: Array[String] = []
	for area_id in AREAS.keys():
		result.append(str(area_id))
	result.sort()
	return result

static func chapter_for_area(area_id: String) -> int:
	if not AREAS.has(area_id):
		return 0
	return int(AREAS[area_id]["chapter"])

static func formations_for_area_tier(area_id: String, tier: String) -> Array:
	if not AREAS.has(area_id) or tier not in TIER_NAMES:
		return []
	var area: Dictionary = AREAS[area_id]
	var formations: Dictionary = area["formations"]
	if not formations.has(tier):
		return []
	return formations[tier].duplicate(true)


static func max_enemies_for_area(area_id: String) -> int:
	if not AREAS.has(area_id):
		return 0
	return int(AREAS[area_id].get("max_enemies", 0))


static func subarea_ids_for_area(area_id: String) -> Array[String]:
	var result: Array[String] = []
	if not AREAS.has(area_id):
		return result
	for tier in TIER_NAMES:
		for formation in AREAS[area_id]["formations"].get(tier, []):
			for subarea in formation.get("subareas", []):
				var subarea_id := str(subarea)
				if subarea_id not in result:
					result.append(subarea_id)
	result.sort()
	return result

static func formation_ids_for_subarea(area_id: String, subarea_id: String) -> Array[String]:
	var result: Array[String] = []
	if not AREAS.has(area_id):
		return result
	for tier in TIER_NAMES:
		for formation in AREAS[area_id]["formations"].get(tier, []):
			if subarea_id in formation.get("subareas", []):
				result.append(str(formation.get("id", "")))
	return result
