extends RefCounted
class_name DiyseChapter0104FormationCatalog

const TIER_NAMES := ["light", "standard", "heavy"]

# Engineering/runtime formation catalog.
# Chapters 1-2 are reconciled to the current 2026-09-25 / 2026-09-23 encounter authorities.
# Hunts, fixed authored encounters, mandatory named encounters, and bosses are absent from random pools.
# Tier placement / weights / EXP here remain executable engineering values pending later balance recalibration.
# Enemy identity, formation composition, area caps, and subarea eligibility follow current structural authority.
const AREAS := {
	"ch01_greenhollow": {
		"chapter": 1,
		"max_enemies": 2,
		"formations": {
			"light": [
				{"id": "ch01_greenhollow_l01", "weight": 50.0, "exp": 45, "enemies": ["Thicket Stalker", "Vine Creeper"], "subareas": ["upper_briar_west", "upper_briar_east"]},
				{"id": "ch01_greenhollow_l02", "weight": 50.0, "exp": 45, "enemies": ["Bullhog", "Vine Creeper"], "subareas": ["upper_briar_west", "upper_briar_east"]},
			],
			"standard": [
				{"id": "ch01_greenhollow_s01", "weight": 100.0, "exp": 55, "enemies": ["Thicket Stalker", "Bullhog"], "subareas": ["upper_briar_west", "upper_briar_east"]},
			],
			"heavy": [
				{"id": "ch01_greenhollow_h01", "weight": 100.0, "exp": 70, "enemies": ["Thicket Stalker", "Vine Creeper"], "subareas": ["upper_briar_west", "upper_briar_east"]},
			],
		},
	},
	"ch01_hollow_watch": {
		"chapter": 1,
		"max_enemies": 3,
		"formations": {
			"light": [
				{"id": "ch01_hollow_watch_l01", "weight": 50.0, "exp": 45, "enemies": ["Black Host Raider", "Black Host Crossbowman"], "subareas": ["hw_approach", "hw_surface"]},
				{"id": "ch01_hollow_watch_l02", "weight": 50.0, "exp": 45, "enemies": ["Construct"], "subareas": ["hw_excavation_corridor"]},
			],
			"standard": [
				{"id": "ch01_hollow_watch_s01", "weight": 50.0, "exp": 55, "enemies": ["Black Host Raider", "Black Host Raider", "Black Host Crossbowman"], "subareas": ["hw_approach", "hw_surface"]},
				{"id": "ch01_hollow_watch_s02", "weight": 50.0, "exp": 55, "enemies": ["Construct", "Construct"], "subareas": ["hw_excavation_corridor"]},
			],
			"heavy": [
				{"id": "ch01_hollow_watch_h01", "weight": 50.0, "exp": 70, "enemies": ["Black Host Raider", "Black Host Crossbowman", "Black Host Shieldbearer"], "subareas": ["hw_surface"]},
				{"id": "ch01_hollow_watch_h02", "weight": 50.0, "exp": 70, "enemies": ["Construct", "Construct"], "subareas": ["hw_excavation_corridor"]},
			],
		},
	},
	"ch01_briar_south": {
		"chapter": 1,
		"max_enemies": 4,
		"formations": {
			"light": [
				{"id": "ch01_briar_south_l01", "weight": 50.0, "exp": 45, "enemies": ["Needlewing", "Thicket Stalker", "Bullhog"], "subareas": ["south_opening", "south_early_middle", "south_main_middle", "south_deep", "south_final_leg"]},
				{"id": "ch01_briar_south_l02", "weight": 50.0, "exp": 45, "enemies": ["Needlewing", "Vine Creeper", "Bullhog"], "subareas": ["south_opening", "south_early_middle", "south_main_middle", "south_deep"]},
			],
			"standard": [
				{"id": "ch01_briar_south_s01", "weight": 50.0, "exp": 55, "enemies": ["Burrowclaw", "Thicket Stalker", "Vine Creeper"], "subareas": ["south_early_middle", "south_main_middle", "south_deep", "south_final_leg"]},
				{"id": "ch01_briar_south_s02", "weight": 50.0, "exp": 55, "enemies": ["Barkling", "Bullhog", "Needlewing"], "subareas": ["south_main_middle", "south_deep", "south_final_leg"]},
			],
			"heavy": [
				{"id": "ch01_briar_south_h01", "weight": 50.0, "exp": 70, "enemies": ["Barkling", "Burrowclaw", "Vine Creeper", "Needlewing"], "subareas": ["south_deep"]},
				{"id": "ch01_briar_south_h02", "weight": 50.0, "exp": 70, "enemies": ["Needlewing", "Needlewing", "Thicket Stalker", "Bullhog"], "subareas": ["south_deep"]},
			],
		},
	},
	"ch02_dunmere_waterworks": {
		"chapter": 2,
		"max_enemies": 5,
		"formations": {
			"light": [
				{"id": "ch02_dunmere_l01", "weight": 50.0, "exp": 130, "enemies": ["Bogshell", "Cistern Leech", "Cistern Leech"], "subareas": ["waterworks_early", "waterworks_flooded_middle"]},
				{"id": "ch02_dunmere_l02", "weight": 50.0, "exp": 130, "enemies": ["Needlewing", "Cistern Leech", "Cistern Leech"], "subareas": ["waterworks_early", "waterworks_flooded_middle"]},
			],
			"standard": [
				{"id": "ch02_dunmere_s01", "weight": 50.0, "exp": 165, "enemies": ["Bogshell", "Cistern Leech", "Needlewing", "Needlewing"], "subareas": ["waterworks_early", "waterworks_flooded_middle", "waterworks_ancient_threshold"]},
				{"id": "ch02_dunmere_s02", "weight": 50.0, "exp": 165, "enemies": ["Bogshell", "Cistern Leech", "Cistern Leech", "Cistern Leech"], "subareas": ["waterworks_flooded_middle", "waterworks_ancient_threshold"]},
			],
			"heavy": [
				{"id": "ch02_dunmere_h01", "weight": 100.0, "exp": 200, "enemies": ["Bogshell", "Needlewing", "Needlewing", "Cistern Leech", "Cistern Leech"], "subareas": ["waterworks_flooded_middle", "waterworks_ancient_threshold"]},
			],
		},
	},
	"ch02_sunken_archive": {
		"chapter": 2,
		"max_enemies": 5,
		"formations": {
			"light": [
				{"id": "ch02_archive_l01", "weight": 50.0, "exp": 130, "enemies": ["Bogshell", "Cistern Leech", "Archive Current"], "subareas": ["archive_entrance", "archive_mid"]},
				{"id": "ch02_archive_l02", "weight": 50.0, "exp": 130, "enemies": ["Needlewing", "Archive Current", "Memory Scribe"], "subareas": ["archive_entrance", "archive_mid", "archive_depths"]},
			],
			"standard": [
				{"id": "ch02_archive_s01", "weight": 50.0, "exp": 165, "enemies": ["Archive Current", "Archive Current", "Memory Scribe", "Cistern Leech"], "subareas": ["archive_mid", "archive_depths"]},
				{"id": "ch02_archive_s02", "weight": 50.0, "exp": 165, "enemies": ["Bogshell", "Archive Current", "Memory Scribe", "Needlewing"], "subareas": ["archive_entrance", "archive_mid", "archive_depths"]},
			],
			"heavy": [
				{"id": "ch02_archive_h01", "weight": 100.0, "exp": 200, "enemies": ["Archive Current", "Archive Current", "Memory Scribe", "Bogshell", "Cistern Leech"], "subareas": ["archive_depths"]},
			],
		},
	},
	"ch02_red_transfer_bastion": {
		# Legacy runtime area key retained until the presentation/environment asset is renamed.
		# Current story/encounter identity is Old Bastion.
		"chapter": 2,
		"max_enemies": 6,
		"formations": {
			"light": [
				{"id": "ch02_bastion_l01", "weight": 50.0, "exp": 130, "enemies": ["Black Host Raider", "Black Host Crossbowman", "Ruin Shieldbearer"], "subareas": ["bastion_alarm_opening", "bastion_alerted_interior"]},
				{"id": "ch02_bastion_l02", "weight": 50.0, "exp": 130, "enemies": ["Black Host Raider", "Rift Hound", "Rift Hound", "Black Host Crossbowman"], "subareas": ["bastion_alarm_opening"]},
			],
			"standard": [
				{"id": "ch02_bastion_s01", "weight": 50.0, "exp": 165, "enemies": ["Ruin Shieldbearer", "Black Host Crossbowman", "Black Host Crossbowman", "Black Host Raider"], "subareas": ["bastion_alarm_opening", "bastion_alerted_interior", "bastion_final_ascent"]},
				{"id": "ch02_bastion_s02", "weight": 50.0, "exp": 165, "enemies": ["Ruin Shieldbearer", "Black Host War-Sorcerer", "Black Host Crossbowman", "Black Host Raider"], "subareas": ["bastion_alarm_opening", "bastion_alerted_interior"]},
			],
			"heavy": [
				{"id": "ch02_bastion_h01", "weight": 25.0, "exp": 200, "enemies": ["Ruin Shieldbearer", "Black Host Raider", "Black Host Raider", "Black Host Raider", "Black Host Crossbowman"], "subareas": ["bastion_alerted_interior", "bastion_final_ascent"]},
				{"id": "ch02_bastion_h02", "weight": 25.0, "exp": 200, "enemies": ["Ruin Shieldbearer", "Black Host Raider", "Black Host Raider", "Black Host Crossbowman", "Black Host War-Sorcerer"], "subareas": ["bastion_final_ascent"]},
				{"id": "ch02_bastion_h03", "weight": 25.0, "exp": 200, "enemies": ["Ruin Shieldbearer", "Black Host Raider", "Black Host Crossbowman", "Rift Hound", "Rift Hound"], "subareas": ["bastion_alerted_interior", "bastion_final_ascent"]},
				{"id": "ch02_bastion_h04", "weight": 25.0, "exp": 200, "enemies": ["Ruin Shieldbearer", "Black Host Raider", "Black Host Raider", "Black Host Raider", "Black Host Crossbowman", "Black Host Crossbowman"], "subareas": ["bastion_final_ascent"]},
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
		# Engineering placeholders only. Exact revised Beat-7..10 placement/weights remain open.
		# Archive Scribe Engine is a mandatory Beat-11 boss and is forbidden from random pools.
		"formations": {
			"light": [
				{"id": "ch03_archives_l01", "weight": 50.0, "exp": 215, "enemies": ["Judgment Frame", "Erasure Wisp", "Erasure Wisp"]},
				{"id": "ch03_archives_l02", "weight": 50.0, "exp": 215, "enemies": ["Erasure Wisp", "Erasure Wisp", "Judgment Frame"]},
			],
			"standard": [
				{"id": "ch03_archives_s01", "weight": 50.0, "exp": 280, "enemies": ["Judgment Frame", "Judgment Frame", "Erasure Wisp", "Erasure Wisp"]},
				{"id": "ch03_archives_s02", "weight": 50.0, "exp": 280, "enemies": ["Judgment Frame", "Erasure Wisp", "Erasure Wisp", "Erasure Wisp"]},
			],
			"heavy": [
				{"id": "ch03_archives_h01", "weight": 50.0, "exp": 315, "enemies": ["Judgment Frame", "Judgment Frame", "Erasure Wisp", "Erasure Wisp", "Erasure Wisp"]},
				{"id": "ch03_archives_h02", "weight": 50.0, "exp": 315, "enemies": ["Judgment Frame", "Judgment Frame", "Judgment Frame", "Erasure Wisp", "Erasure Wisp"]},
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
