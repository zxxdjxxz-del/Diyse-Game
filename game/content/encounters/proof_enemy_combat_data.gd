extends RefCounted
class_name DiyseProofEnemyCombatData

# ENGINEERING PROOF DATA ONLY.
# These HP/MP/speed values are not canon, not final balance, and must not be
# promoted into production enemy stats merely because they are executable.
# This layer exists only to prove generated random-formation battle setup.
const DEFINITIONS := {
	"Greenhollow Stalker": {"hp": 30, "mp": 0, "speed": 10},
	"Thornvine Creeper": {"hp": 24, "mp": 0, "speed": 6},
	"Briar Boar": {"hp": 40, "mp": 0, "speed": 7},
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
