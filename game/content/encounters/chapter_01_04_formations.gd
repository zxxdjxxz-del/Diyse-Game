extends RefCounted
class_name DiyseChapter0104FormationCatalog

const TIER_NAMES := ["light", "standard", "heavy"]

# Engineering/runtime formation catalog.
# Chapters 1-4 are reconciled to the current structural encounter authorities.
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
	"ch02_old_bastion": {
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
	"ch03_old_city_archives": {
		"chapter": 3,
		"max_enemies": 6,
		# Exact composition/subarea eligibility is current authority.
		# Tier weights and EXP remain engineering/runtime values pending final progression certification.
		"formations": {
			"light": [
				{"id": "ch03_old_city_l01", "weight": 25.0, "exp": 215, "enemies": ["Judgment Frame", "Erasure Wisp", "Erasure Wisp"], "subareas": ["lower_archives"]},
				{"id": "ch03_old_city_l02", "weight": 25.0, "exp": 215, "enemies": ["Judgment Frame", "Authority Lens", "Erasure Wisp"], "subareas": ["lower_archives"]},
				{"id": "ch03_old_city_l03", "weight": 25.0, "exp": 215, "enemies": ["Judgment Frame", "Judgment Frame", "Erasure Wisp", "Authority Lens"], "subareas": ["lower_archives"]},
				{"id": "ch03_old_city_l04", "weight": 25.0, "exp": 215, "enemies": ["Judgment Frame", "Erasure Wisp", "Erasure Wisp", "Authority Lens"], "subareas": ["lower_archives"]},
			],
			"standard": [
				{"id": "ch03_old_city_s01", "weight": 11.0, "exp": 280, "enemies": ["Judgment Frame", "Erasure Wisp", "Erasure Wisp", "Authority Lens"], "subareas": ["buried_collections"]},
				{"id": "ch03_old_city_s02", "weight": 11.0, "exp": 280, "enemies": ["Judgment Frame", "Judgment Frame", "Erasure Wisp", "Authority Lens"], "subareas": ["buried_collections"]},
				{"id": "ch03_old_city_s03", "weight": 11.0, "exp": 280, "enemies": ["Judgment Frame", "Erasure Wisp", "Erasure Wisp", "Erasure Wisp", "Authority Lens"], "subareas": ["buried_collections"]},
				{"id": "ch03_old_city_s04", "weight": 11.0, "exp": 280, "enemies": ["Judgment Frame", "Judgment Frame", "Erasure Wisp", "Erasure Wisp", "Authority Lens"], "subareas": ["buried_collections"]},
				{"id": "ch03_old_city_s05", "weight": 11.0, "exp": 280, "enemies": ["Judgment Frame", "Authority Lens", "Authority Lens", "Erasure Wisp"], "subareas": ["hall_of_seals"]},
				{"id": "ch03_old_city_s06", "weight": 11.0, "exp": 280, "enemies": ["Judgment Frame", "Judgment Frame", "Authority Lens", "Erasure Wisp", "Erasure Wisp"], "subareas": ["hall_of_seals"]},
				{"id": "ch03_old_city_s07", "weight": 11.0, "exp": 280, "enemies": ["Judgment Frame", "Authority Lens", "Authority Lens", "Erasure Wisp", "Erasure Wisp"], "subareas": ["hall_of_seals"]},
				{"id": "ch03_old_city_s08", "weight": 11.0, "exp": 280, "enemies": ["Judgment Frame", "Judgment Frame", "Authority Lens", "Authority Lens", "Erasure Wisp"], "subareas": ["hall_of_seals"]},
				{"id": "ch03_old_city_s09", "weight": 12.0, "exp": 280, "enemies": ["Judgment Frame", "Archive Current", "Authority Lens", "Erasure Wisp", "Erasure Wisp"], "subareas": ["hall_to_deep_transition"]},
			],
			"heavy": [
				{"id": "ch03_old_city_h01", "weight": 22.5, "exp": 315, "enemies": ["Judgment Frame", "Archive Current", "Archive Current", "Authority Lens", "Erasure Wisp"], "subareas": ["deep_archives"]},
				{"id": "ch03_old_city_h02", "weight": 22.5, "exp": 315, "enemies": ["Judgment Frame", "Judgment Frame", "Archive Current", "Authority Lens", "Erasure Wisp"], "subareas": ["deep_archives"]},
				{"id": "ch03_old_city_h03", "weight": 22.5, "exp": 315, "enemies": ["Judgment Frame", "Archive Current", "Archive Current", "Erasure Wisp", "Erasure Wisp", "Authority Lens"], "subareas": ["deep_archives"]},
				{"id": "ch03_old_city_h04", "weight": 22.5, "exp": 315, "enemies": ["Judgment Frame", "Judgment Frame", "Archive Current", "Erasure Wisp", "Erasure Wisp", "Authority Lens"], "subareas": ["deep_archives"]},
				{"id": "ch03_old_city_h05", "weight": 5.0, "exp": 315, "enemies": ["Grand Inquisitor Frame", "Judgment Frame", "Authority Lens", "Erasure Wisp"], "subareas": ["deep_archives"]},
				{"id": "ch03_old_city_h06", "weight": 5.0, "exp": 315, "enemies": ["Grand Inquisitor Frame", "Judgment Frame", "Archive Current", "Authority Lens", "Erasure Wisp"], "subareas": ["deep_archives"]},
			],
		},
	},
	"ch03_cresthaven_tower": {
		"chapter": 3,
		"max_enemies": 6,
		"formations": {
			"light": [
				{"id": "ch03_cresthaven_l01", "weight": 25.0, "exp": 215, "enemies": ["Watch Sentry", "Watch Sentry", "Watch Ballista", "Authority Lens"], "subareas": ["tower_foundation"]},
				{"id": "ch03_cresthaven_l02", "weight": 25.0, "exp": 215, "enemies": ["Watch Sentry", "Watch Ballista", "Watch Ballista", "Authority Lens"], "subareas": ["tower_foundation"]},
				{"id": "ch03_cresthaven_l03", "weight": 25.0, "exp": 215, "enemies": ["Watch Captain Frame", "Watch Sentry", "Watch Ballista", "Authority Lens"], "subareas": ["tower_foundation"]},
				{"id": "ch03_cresthaven_l04", "weight": 25.0, "exp": 215, "enemies": ["Watch Sentry", "Watch Sentry", "Watch Ballista", "Watch Ballista", "Authority Lens"], "subareas": ["tower_foundation"]},
			],
			"standard": [
				{"id": "ch03_cresthaven_s01", "weight": 20.0, "exp": 280, "enemies": ["Command Guard Frame", "Authority Lens", "Command Ring Drone", "Command Ring Drone"], "subareas": ["command_interior"]},
				{"id": "ch03_cresthaven_s02", "weight": 20.0, "exp": 280, "enemies": ["Command Guard Frame", "Command Guard Frame", "Authority Lens", "Command Ring Drone", "Command Ring Drone"], "subareas": ["command_interior"]},
				{"id": "ch03_cresthaven_s03", "weight": 20.0, "exp": 280, "enemies": ["Command Guard Frame", "Watch Sentry", "Watch Ballista", "Authority Lens", "Command Ring Drone"], "subareas": ["command_interior"]},
				{"id": "ch03_cresthaven_s04", "weight": 20.0, "exp": 280, "enemies": ["Watch Captain Frame", "Command Guard Frame", "Authority Lens", "Command Ring Drone", "Command Ring Drone"], "subareas": ["command_interior"]},
				{"id": "ch03_cresthaven_s05", "weight": 20.0, "exp": 280, "enemies": ["Command Guard Frame", "Watch Sentry", "Watch Ballista", "Watch Ballista", "Authority Lens", "Command Ring Drone"], "subareas": ["command_interior"]},
			],
			"heavy": [
				{"id": "ch03_cresthaven_h01", "weight": 20.0, "exp": 315, "enemies": ["Command Guard Frame", "Command Guard Frame", "Authority Lens", "Command Ring Drone", "Command Ring Drone"], "subareas": ["warden_approach"]},
				{"id": "ch03_cresthaven_h02", "weight": 20.0, "exp": 315, "enemies": ["Command Guard Frame", "Watch Sentry", "Watch Ballista", "Authority Lens", "Command Ring Drone"], "subareas": ["warden_approach"]},
				{"id": "ch03_cresthaven_h03", "weight": 20.0, "exp": 315, "enemies": ["Watch Captain Frame", "Command Guard Frame", "Authority Lens", "Command Ring Drone", "Command Ring Drone"], "subareas": ["warden_approach"]},
				{"id": "ch03_cresthaven_h04", "weight": 20.0, "exp": 315, "enemies": ["Command Guard Frame", "Watch Sentry", "Watch Ballista", "Watch Ballista", "Authority Lens", "Command Ring Drone"], "subareas": ["warden_approach"]},
				{"id": "ch03_cresthaven_h05", "weight": 20.0, "exp": 315, "enemies": ["Watch Captain Frame", "Command Guard Frame", "Watch Sentry", "Watch Ballista", "Authority Lens", "Command Ring Drone"], "subareas": ["warden_approach"]},
			],
		},
	},
	"ch04_reaction_annex": {
		"chapter": 4,
		"max_enemies": 5,
		# Repeatable baseline rows use recovered authoritative 30/45/25 weights.
		# Annex Duelist is intentionally not encoded here until its one-time/frequency insertion is locked.
		"formations": {
			"light": [
				{"id": "ch04_annex_l01", "weight": 30.0, "exp": 315, "enemies": ["Reaction Node", "Reaction Hound", "Reaction Hound", "Element Mirror"], "subareas": ["annex_early"]},
				{"id": "ch04_annex_l02", "weight": 45.0, "exp": 315, "enemies": ["Reaction Node", "Reaction Node", "Reaction Hound", "Composite Elemental"], "subareas": ["annex_early"]},
				{"id": "ch04_annex_l03", "weight": 25.0, "exp": 315, "enemies": ["Reaction Node", "Reaction Hound", "Element Mirror", "Composite Elemental"], "subareas": ["annex_early"]},
			],
			"standard": [
				{"id": "ch04_annex_s01", "weight": 30.0, "exp": 375, "enemies": ["Reaction Node", "Reaction Node", "Reaction Hound", "Composite Elemental"], "subareas": ["annex_mid"]},
				{"id": "ch04_annex_s02", "weight": 45.0, "exp": 375, "enemies": ["Element Mirror", "Reaction Hound", "Reaction Hound", "Composite Elemental"], "subareas": ["annex_mid"]},
				{"id": "ch04_annex_s03", "weight": 25.0, "exp": 375, "enemies": ["Reaction Node", "Element Mirror", "Composite Elemental", "Annex Crucible Guard"], "subareas": ["annex_mid"]},
			],
			"heavy": [
				{"id": "ch04_annex_h01", "weight": 30.0, "exp": 460, "enemies": ["Annex Crucible Guard", "Composite Elemental", "Reaction Node", "Reaction Hound"], "subareas": ["annex_late", "central_regulation"]},
				{"id": "ch04_annex_h02", "weight": 45.0, "exp": 460, "enemies": ["Annex Crucible Guard", "Annex Crucible Guard", "Element Mirror", "Reaction Hound", "Reaction Hound"], "subareas": ["annex_late", "central_regulation"]},
				{"id": "ch04_annex_h03", "weight": 25.0, "exp": 460, "enemies": ["Annex Crucible Guard", "Composite Elemental", "Element Mirror", "Reaction Node", "Reaction Hound"], "subareas": ["annex_late", "central_regulation"]},
			],
		},
	}
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
