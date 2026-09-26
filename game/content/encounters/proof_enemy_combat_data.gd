extends RefCounted
class_name DiyseProofEnemyCombatData

# ENGINEERING PROOF DATA ONLY.
# These HP/MP/speed values are not canon, not final balance, and must not be
# promoted into production enemy stats merely because they are executable.
# This layer exists only to prove generated random-formation battle setup.
const DEFINITIONS := {
	"Black Host Raider": {"hp": 28, "mp": 0, "speed": 8},
	"Black Host Crossbowman": {"hp": 24, "mp": 0, "speed": 9},
	"Black Host Shieldbearer": {"hp": 38, "mp": 0, "speed": 5},
	"Ruin Shieldbearer": {"hp": 38, "mp": 0, "speed": 5},
	"Thicket Stalker": {"hp": 30, "mp": 0, "speed": 10},
	"Vine Creeper": {"hp": 24, "mp": 0, "speed": 6},
	"Bullhog": {"hp": 40, "mp": 0, "speed": 7},
	"Needlewing": {"hp": 22, "mp": 0, "speed": 12},
	"Burrowclaw": {"hp": 34, "mp": 0, "speed": 5},
	"Barkling": {"hp": 44, "mp": 0, "speed": 5},
	"Construct": {"hp": 32, "mp": 0, "speed": 8},
	"Bogshell": {"hp": 52, "mp": 0, "speed": 5},
	"Cistern Leech": {"hp": 34, "mp": 0, "speed": 8},
	"Archive Current": {"hp": 40, "mp": 8, "speed": 9},
	"Memory Scribe": {"hp": 42, "mp": 12, "speed": 7},
	"Black Host War-Sorcerer": {"hp": 44, "mp": 20, "speed": 8},
	"Rift Hound": {"hp": 38, "mp": 0, "speed": 11},
	"Judgment Frame": {"hp": 60, "mp": 0, "speed": 7},
	"Erasure Wisp": {"hp": 38, "mp": 10, "speed": 11},
	"Authority Lens": {"hp": 44, "mp": 8, "speed": 8},
	"Grand Inquisitor Frame": {"hp": 88, "mp": 12, "speed": 6},
	"Watch Sentry": {"hp": 58, "mp": 0, "speed": 7},
	"Watch Ballista": {"hp": 64, "mp": 0, "speed": 4},
	"Watch Captain Frame": {"hp": 82, "mp": 0, "speed": 6},
	"Command Guard Frame": {"hp": 72, "mp": 0, "speed": 7},
	"Command Ring Drone": {"hp": 46, "mp": 10, "speed": 9},
	"Reaction Node": {"hp": 52, "mp": 12, "speed": 8},
	"Reaction Hound": {"hp": 48, "mp": 0, "speed": 11},
	"Element Mirror": {"hp": 56, "mp": 14, "speed": 9},
	"Composite Elemental": {"hp": 72, "mp": 18, "speed": 7},
	"Annex Crucible Guard": {"hp": 84, "mp": 8, "speed": 6},
}

static func has_enemy(enemy_name: String) -> bool:
	return DEFINITIONS.has(enemy_name)

static func definition_for(enemy_name: String) -> Dictionary:
	if not DEFINITIONS.has(enemy_name):
		return {}
	var result: Dictionary = DEFINITIONS[enemy_name].duplicate(true)
	result["id"] = enemy_name.to_lower().replace(" ", "_")
	result["display_name"] = enemy_name
	return result

static func build_units(enemy_names: Array) -> Array[Dictionary]:
	var result: Array[Dictionary] = []
	for raw_name in enemy_names:
		var enemy_name := str(raw_name)
		var definition := definition_for(enemy_name)
		if definition.is_empty():
			return []
		result.append(definition)
	return result
