extends Node

const DEFAULT_AREA := "field_proof"

var current_area: String
var field_position: Vector3
var party: Array[Dictionary]
var inventory: Dictionary
var standard_cards: Array[String]
var primes: Dictionary
var equipment: Dictionary
var flags: Dictionary
var rewards: Dictionary

# Runtime-only scene handoff state. These fields are intentionally excluded
# from save serialization until encounter-pressure persistence is designed.
var transient_encounter: Dictionary
var transient_encounter_return: Dictionary

func _init() -> void:
	reset_defaults()

func reset_defaults() -> void:
	current_area = DEFAULT_AREA
	field_position = Vector3(0.0, 0.9, 4.0)
	party = [
		{"name": "Cyanis", "hp": 46, "max_hp": 46, "mp": 12, "max_mp": 12},
		{"name": "Ilyra", "hp": 40, "max_hp": 40, "mp": 18, "max_mp": 18},
		{"name": "Torren", "hp": 44, "max_hp": 44, "mp": 10, "max_mp": 10},
		{"name": "Nimera", "hp": 38, "max_hp": 38, "mp": 16, "max_mp": 16}
	]
	inventory = {"Potion": 3}
	standard_cards = ["proof_might_strike"]
	primes = {
		"first_champion": {
			"acquired": true,
			"bearer": "Cyanis",
			"progression_state": "Recovered",
			"available_battle_use_baseline": 1
		}
	}
	equipment = {
		"Cyanis": {"weapon": "Proof Sword", "armor": "Proof Crest Armor"},
		"Ilyra": {"weapon": "Proof Warden Blade", "armor": "Proof Blue Warden Armor"},
		"Torren": {"weapon": "Proof Bow", "armor": "Proof Field Armor"},
		"Nimera": {"weapon": "Proof Cardweaver Implement", "armor": "Proof Archive Coat"}
	}
	flags = {
		"proof_story_flag": false,
		"proof_chest_opened": false,
		"torren_state": "normal"
	}
	rewards = {"xp": 0, "gold": 0}
	clear_transient_encounter_state()

func queue_transient_random_encounter(payload: Dictionary) -> bool:
	if str(payload.get("kind", "")) != "random":
		return false
	if str(payload.get("formation_id", "")).is_empty():
		return false
	var enemies = payload.get("enemies", [])
	if not (enemies is Array) or enemies.is_empty():
		return false
	transient_encounter = payload.duplicate(true)
	transient_encounter_return.clear()
	return true

func has_transient_random_encounter() -> bool:
	return not transient_encounter.is_empty() and str(transient_encounter.get("kind", "")) == "random"

func transient_random_encounter_payload() -> Dictionary:
	return transient_encounter.duplicate(true)

func complete_transient_random_encounter(outcome: String, reward_payload: Dictionary = {}) -> bool:
	if not has_transient_random_encounter():
		return false
	if outcome not in ["victory", "successful_flee", "defeat"]:
		return false
	transient_encounter_return = {
		"outcome": outcome,
		"formation_id": str(transient_encounter.get("formation_id", "")),
		"rewards": reward_payload.duplicate(true)
	}
	transient_encounter.clear()
	return true

func consume_transient_encounter_return() -> Dictionary:
	var result := transient_encounter_return.duplicate(true)
	transient_encounter_return.clear()
	return result

func clear_transient_encounter_state() -> void:
	transient_encounter = {}
	transient_encounter_return = {}

func to_save_dict(schema_version: int) -> Dictionary:
	return {
		"schema_version": schema_version,
		"area": current_area,
		"field_position": {
			"x": field_position.x,
			"y": field_position.y,
			"z": field_position.z
		},
		"party": party.duplicate(true),
		"inventory": inventory.duplicate(true),
		"standard_cards": standard_cards.duplicate(),
		"primes": primes.duplicate(true),
		"equipment": equipment.duplicate(true),
		"flags": flags.duplicate(true),
		"rewards": rewards.duplicate(true)
	}

func apply_save_dict(data: Dictionary) -> bool:
	if not data.has("area") or not data.has("field_position"):
		return false
	var position_data = data.get("field_position")
	if not (position_data is Dictionary):
		return false
	for axis in ["x", "y", "z"]:
		if not position_data.has(axis):
			return false

	current_area = str(data.get("area", DEFAULT_AREA))
	field_position = Vector3(
		float(position_data.get("x", 0.0)),
		float(position_data.get("y", 0.9)),
		float(position_data.get("z", 4.0))
	)
	party = _dictionary_array(data.get("party", []))
	inventory = _dictionary_or_empty(data.get("inventory", {}))
	standard_cards = _string_array(data.get("standard_cards", []))
	primes = _dictionary_or_empty(data.get("primes", {}))
	equipment = _dictionary_or_empty(data.get("equipment", {}))
	flags = _dictionary_or_empty(data.get("flags", {}))
	rewards = _dictionary_or_empty(data.get("rewards", {}))
	# Loading a disk save must never resurrect a stale scene-to-scene random
	# encounter request or battle return result.
	clear_transient_encounter_state()
	return true

func _dictionary_array(value: Variant) -> Array[Dictionary]:
	var result: Array[Dictionary] = []
	if value is Array:
		for entry in value:
			if entry is Dictionary:
				result.append(entry.duplicate(true))
	return result

func _string_array(value: Variant) -> Array[String]:
	var result: Array[String] = []
	if value is Array:
		for entry in value:
			result.append(str(entry))
	return result

func _dictionary_or_empty(value: Variant) -> Dictionary:
	if value is Dictionary:
		return value.duplicate(true)
	return {}
