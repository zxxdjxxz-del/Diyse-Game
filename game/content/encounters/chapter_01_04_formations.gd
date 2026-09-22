extends RefCounted
class_name DiyseChapter0104FormationCatalog

const TIER_NAMES := ["light", "standard", "heavy"]

# Engineering/runtime formation catalog.
# Chapter 1 has been reconciled to the current 2026-09-22 enemy-placement locks.
# Hunts, mandatory named encounters, and bosses are absent from random pools.
# Strong normal-pool enemies such as Watch Captain Frame may appear where current canon permits.
# Chapter-1 50/50 tier weights here are executable engineering placeholders; current owning docs keep
# Southern-Briar and Watch-Captain final selection weights open pending encounter revalidation.
const AREAS := {
	"ch01_greenhollow": {
		"chapter": 1,
		"formations": {
			"light": [
				{"id": "ch01_greenhollow_l01", "weight": 50.0, "exp": 45, "enemies": ["Greenhollow Stalker", "Thornvine Creeper"]},
				{"id": "ch01_greenhollow_l02", "weight": 50.0, "exp": 45, "enemies": ["Briar Boar", "Thornvine Creeper"]},
			],
			"standard": [
				{"id": "ch01_greenhollow_s01", "weight": 50.0, "exp": 55, "enemies": ["Greenhollow Stalker", "Briar Boar", "Thornvine Creeper"]},
				{"id": "ch01_greenhollow_s02", "weight": 50.0, "exp": 55, "enemies": ["Greenhollow Stalker", "Thornvine Creeper", "Thornvine Creeper"]},
			],
			"heavy": [
				{"id": "ch01_greenhollow_h01", "weight": 50.0, "exp": 70, "enemies": ["Greenhollow Stalker", "Greenhollow Stalker", "Briar Boar", "Thornvine Creeper"]},
				{"id": "ch01_greenhollow_h02", "weight": 50.0, "exp": 70, "enemies": ["Greenhollow Stalker", "Briar Boar", "Briar Boar", "Thornvine Creeper"]},
			],
		},
	},
	"ch01_hollow_watch": {
		"chapter": 1,
		"formations": {
			"light": [
				{"id": "ch01_hollow_watch_l01", "weight": 50.0, "exp": 45, "enemies": ["Black Host Raider", "Black Host Crossbowman"]},
				{"id": "ch01_hollow_watch_l02", "weight": 50.0, "exp": 45, "enemies": ["Hollow Watch Sentry", "Hollow Watch Sentry"]},
			],
			"standard": [
				{"id": "ch01_hollow_watch_s01", "weight": 50.0, "exp": 55, "enemies": ["Black Host Raider", "Black Host Crossbowman", "Ruin Shieldbearer"]},
				{"id": "ch01_hollow_watch_s02", "weight": 50.0, "exp": 55, "enemies": ["Hollow Watch Sentry", "Hollow Watch Sentry", "Hollow Watch Ballista"]},
			],
			"heavy": [
				{"id": "ch01_hollow_watch_h01", "weight": 50.0, "exp": 70, "enemies": ["Black Host Raider", "Black Host Crossbowman", "Black Host Crossbowman", "Ruin Shieldbearer"]},
				{"id": "ch01_hollow_watch_h02", "weight": 50.0, "exp": 70, "enemies": ["Watch Captain Frame", "Hollow Watch Sentry", "Hollow Watch Ballista"]},
			],
		},
	},
	"ch01_briar_south": {
		"chapter": 1,
		"formations": {
			"light": [
				{"id": "ch01_briar_south_l01", "weight": 50.0, "exp": 45, "enemies": ["Needlewing", "Greenhollow Stalker", "Briar Boar"]},
				{"id": "ch01_briar_south_l02", "weight": 50.0, "exp": 45, "enemies": ["Rootmaw", "Thornvine Creeper", "Needlewing"]},
			],
			"standard": [
				{"id": "ch01_briar_south_s01", "weight": 50.0, "exp": 55, "enemies": ["Rootmaw", "Thornvine Creeper", "Thornvine Creeper", "Needlewing"]},
				{"id": "ch01_briar_south_s02", "weight": 50.0, "exp": 55, "enemies": ["Brambleback", "Briar Boar", "Thornvine Creeper"]},
			],
			"heavy": [
				{"id": "ch01_briar_south_h01", "weight": 50.0, "exp": 70, "enemies": ["Brambleback", "Briar Boar", "Rootmaw", "Thornvine Creeper"]},
				{"id": "ch01_briar_south_h02", "weight": 50.0, "exp": 70, "enemies": ["Needlewing", "Needlewing", "Greenhollow Stalker", "Rootmaw"]},
			],
		},
	},
	"ch02_dunmere_waterworks": {
		"chapter": 2,
		"formations": {
			"light": [
				{"id": "ch02_dunmere_l01", "weight": 50.0, "exp": 130, "enemies": ["Cistern Leech", "Cistern Leech", "Bogshell"]},
				{"id": "ch02_dunmere_l02", "weight": 50.0, "exp": 130, "enemies": ["Redwater Initiate", "Cistern Leech", "Cistern Leech"]},
			],
			"standard": [
				{"id": "ch02_dunmere_s01", "weight": 50.0, "exp": 165, "enemies": ["Redwater Initiate", "Bogshell", "Cistern Leech"]},
				{"id": "ch02_dunmere_s02", "weight": 50.0, "exp": 165, "enemies": ["Bogshell", "Bogshell", "Cistern Leech", "Cistern Leech"]},
			],
			"heavy": [
				{"id": "ch02_dunmere_h01", "weight": 50.0, "exp": 200, "enemies": ["Redwater Initiate", "Redwater Initiate", "Bogshell", "Cistern Leech"]},
				{"id": "ch02_dunmere_h02", "weight": 50.0, "exp": 200, "enemies": ["Redwater Initiate", "Bogshell", "Cistern Leech", "Cistern Leech"]},
			],
		},
	},
	"ch02_sunken_archive": {
		"chapter": 2,
		"formations": {
			"light": [
				{"id": "ch02_archive_l01", "weight": 50.0, "exp": 130, "enemies": ["Archive Current", "Memory Scribe", "Vault Sentinel"]},
				{"id": "ch02_archive_l02", "weight": 50.0, "exp": 130, "enemies": ["Drowned Archive Maw", "Archive Current", "Archive Current"]},
			],
			"standard": [
				{"id": "ch02_archive_s01", "weight": 50.0, "exp": 165, "enemies": ["Memory Scribe", "Vault Sentinel", "Archive Current", "Archive Current"]},
				{"id": "ch02_archive_s02", "weight": 50.0, "exp": 165, "enemies": ["Drowned Archive Maw", "Memory Scribe", "Vault Sentinel", "Archive Current"]},
			],
			"heavy": [
				{"id": "ch02_archive_h01", "weight": 50.0, "exp": 200, "enemies": ["Drowned Archive Maw", "Memory Scribe", "Vault Sentinel", "Vault Sentinel"]},
				{"id": "ch02_archive_h02", "weight": 50.0, "exp": 200, "enemies": ["Drowned Archive Maw", "Memory Scribe", "Memory Scribe", "Archive Current"]},
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
