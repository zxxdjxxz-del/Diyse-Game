extends Node

const DEFAULT_AREA := "field_proof"
const STARTING_WALLET_G := 2500
const EQUIPMENT_FACES := ["Might", "Elements", "Grace", "Perception", "Memory", "Ruin"]
const RETIRED_EQUIPMENT_FACE_ALIASES := {
	"resource": "Perception",
	"acuity": "Perception",
	"change": "Memory"
}
const MAX_RELIC_COPY_COMPONENTS_PER_FACE := 3

var current_area: String
var field_position: Vector3
var party: Array[Dictionary]
var inventory: Dictionary
var standard_cards: Array[String]
var primes: Dictionary
var equipment: Dictionary
var relic_inventory: Dictionary
var forge_components: Dictionary
var flags: Dictionary
var rewards: Dictionary
var wallet_g: int

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
	# Exceptional-equipment ownership is stored by stable Relic ID. A forged
	# copy increments quantity on the same Relic identity; it does not create a
	# second item definition with altered stats or Trait data.
	relic_inventory = {}
	# Forge Components live outside the ordinary sellable inventory. Relic-copy
	# components are unique authored records and remain bounded to three per Face.
	forge_components = {}
	flags = {
		"proof_story_flag": false,
		"proof_chest_opened": false,
		"torren_state": "normal"
	}
	# This is proof battle-result payload, not the persistent party wallet.
	# The old `gold` key remains isolated here until battle reward payloads are
	# migrated in their own coordinated pass.
	rewards = {"xp": 0, "gold": 0}
	wallet_g = STARTING_WALLET_G
	clear_transient_encounter_state()

func wallet_balance_g() -> int:
	return wallet_g

func can_afford_g(amount_g: int) -> bool:
	return amount_g >= 0 and wallet_g >= amount_g

func credit_g(amount_g: int) -> bool:
	if amount_g < 0:
		return false
	wallet_g += amount_g
	return true

func spend_g(amount_g: int) -> bool:
	if not can_afford_g(amount_g):
		return false
	wallet_g -= amount_g
	return true

func register_relic_original(relic_id: String, face: String) -> bool:
	var normalized_id := relic_id.strip_edges()
	var canonical_face := _canonical_equipment_face(face)
	if normalized_id.is_empty() or canonical_face.is_empty():
		return false
	# The Relic registration path must never be used to smuggle a Legacy into
	# Kessara's copy system. Future catalog code may use WPN_/ARM_/SEC_ IDs, so
	# no narrower Relic prefix is required here.
	if normalized_id.to_upper().begins_with("LEGACY_"):
		return false
	if relic_inventory.has(normalized_id):
		return false
	relic_inventory[normalized_id] = {
		"face": canonical_face,
		"original_obtained": true,
		"forged_copy": false
	}
	return true

func has_relic_original(relic_id: String) -> bool:
	var record = relic_inventory.get(relic_id.strip_edges(), {})
	return record is Dictionary and bool(record.get("original_obtained", false))

func has_forged_relic_copy(relic_id: String) -> bool:
	var record = relic_inventory.get(relic_id.strip_edges(), {})
	return record is Dictionary and bool(record.get("forged_copy", false))

func relic_face(relic_id: String) -> String:
	var record = relic_inventory.get(relic_id.strip_edges(), {})
	if not (record is Dictionary):
		return ""
	return _canonical_equipment_face(str(record.get("face", "")))

func relic_quantity(relic_id: String) -> int:
	var record = relic_inventory.get(relic_id.strip_edges(), {})
	if not (record is Dictionary):
		return 0
	var quantity := 0
	if bool(record.get("original_obtained", false)):
		quantity += 1
	if bool(record.get("forged_copy", false)):
		quantity += 1
	return quantity

func register_relic_copy_component(component_id: String, face: String) -> bool:
	var normalized_id := component_id.strip_edges()
	var canonical_face := _canonical_equipment_face(face)
	if normalized_id.is_empty() or canonical_face.is_empty():
		return false
	if forge_components.has(normalized_id):
		return false
	if _registered_relic_copy_component_count(canonical_face) >= MAX_RELIC_COPY_COMPONENTS_PER_FACE:
		return false
	forge_components[normalized_id] = {
		"face": canonical_face,
		"purpose": "relic_copy",
		"consumed": false
	}
	return true

func available_relic_copy_component_for_face(face: String) -> String:
	var canonical_face := _canonical_equipment_face(face)
	if canonical_face.is_empty():
		return ""
	var component_ids: Array = forge_components.keys()
	component_ids.sort()
	for raw_id in component_ids:
		var component_id := str(raw_id)
		var record = forge_components.get(component_id, {})
		if not (record is Dictionary):
			continue
		if str(record.get("purpose", "")) != "relic_copy":
			continue
		if _canonical_equipment_face(str(record.get("face", ""))) != canonical_face:
			continue
		if bool(record.get("consumed", false)):
			continue
		return component_id
	return ""

func forged_relic_count_for_face(face: String) -> int:
	var canonical_face := _canonical_equipment_face(face)
	if canonical_face.is_empty():
		return 0
	var count := 0
	for raw_id in relic_inventory.keys():
		var record = relic_inventory.get(raw_id, {})
		if not (record is Dictionary):
			continue
		if _canonical_equipment_face(str(record.get("face", ""))) != canonical_face:
			continue
		if bool(record.get("forged_copy", false)):
			count += 1
	return count

# Low-level ownership commit retained for proof/migration callers. Production
# Kessara service code must use commit_relic_copy_with_g_fee() so the G charge,
# component consumption, and forged-copy state change form one transaction.
func commit_relic_copy(relic_id: String, component_id: String) -> bool:
	var normalized_relic_id := relic_id.strip_edges()
	var normalized_component_id := component_id.strip_edges()
	if not _relic_copy_commit_is_valid(normalized_relic_id, normalized_component_id):
		return false
	_apply_relic_copy_commit(normalized_relic_id, normalized_component_id)
	return true

func commit_relic_copy_with_g_fee(relic_id: String, component_id: String, fee_g: int) -> bool:
	var normalized_relic_id := relic_id.strip_edges()
	var normalized_component_id := component_id.strip_edges()
	if fee_g < 0 or not can_afford_g(fee_g):
		return false
	if not _relic_copy_commit_is_valid(normalized_relic_id, normalized_component_id):
		return false
	# All failure checks occur before mutation. From this point the three durable
	# state changes are committed together in this single synchronous method.
	_apply_relic_copy_commit(normalized_relic_id, normalized_component_id)
	wallet_g -= fee_g
	return true

func _relic_copy_commit_is_valid(normalized_relic_id: String, normalized_component_id: String) -> bool:
	if not has_relic_original(normalized_relic_id):
		return false
	if has_forged_relic_copy(normalized_relic_id) or relic_quantity(normalized_relic_id) >= 2:
		return false
	var face := relic_face(normalized_relic_id)
	if face.is_empty() or forged_relic_count_for_face(face) >= MAX_RELIC_COPY_COMPONENTS_PER_FACE:
		return false

	var component = forge_components.get(normalized_component_id, {})
	if not (component is Dictionary):
		return false
	if str(component.get("purpose", "")) != "relic_copy":
		return false
	if _canonical_equipment_face(str(component.get("face", ""))) != face:
		return false
	if bool(component.get("consumed", false)):
		return false

	var relic_record = relic_inventory.get(normalized_relic_id, {})
	return relic_record is Dictionary

func _apply_relic_copy_commit(normalized_relic_id: String, normalized_component_id: String) -> void:
	var relic_record: Dictionary = relic_inventory[normalized_relic_id]
	var component: Dictionary = forge_components[normalized_component_id]
	relic_record["forged_copy"] = true
	relic_inventory[normalized_relic_id] = relic_record
	component["consumed"] = true
	forge_components[normalized_component_id] = component

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
		"relic_inventory": relic_inventory.duplicate(true),
		"forge_components": forge_components.duplicate(true),
		"flags": flags.duplicate(true),
		"rewards": rewards.duplicate(true),
		"wallet_g": wallet_g
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
	var loaded_wallet_g := int(data.get("wallet_g", STARTING_WALLET_G))
	if loaded_wallet_g < 0:
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
	# These ownership keys remain optional during migration so older proof saves
	# can normalize into the current schema without inventing Relics/components.
	relic_inventory = _dictionary_or_empty(data.get("relic_inventory", {}))
	forge_components = _dictionary_or_empty(data.get("forge_components", {}))
	flags = _dictionary_or_empty(data.get("flags", {}))
	rewards = _dictionary_or_empty(data.get("rewards", {}))
	wallet_g = loaded_wallet_g
	# Loading a disk save must never resurrect a stale scene-to-scene random
	# encounter request or battle return result.
	clear_transient_encounter_state()
	return true

func _registered_relic_copy_component_count(face: String) -> int:
	var canonical_face := _canonical_equipment_face(face)
	if canonical_face.is_empty():
		return 0
	var count := 0
	for raw_id in forge_components.keys():
		var record = forge_components.get(raw_id, {})
		if not (record is Dictionary):
			continue
		if str(record.get("purpose", "")) != "relic_copy":
			continue
		if _canonical_equipment_face(str(record.get("face", ""))) == canonical_face:
			count += 1
	return count

func _canonical_equipment_face(face: String) -> String:
	var normalized := face.strip_edges().to_lower()
	for candidate in EQUIPMENT_FACES:
		if str(candidate).to_lower() == normalized:
			return str(candidate)
	# Preserve save/data compatibility with retired Face labels while ensuring
	# all newly registered/current-facing records normalize to the current set.
	return str(RETIRED_EQUIPMENT_FACE_ALIASES.get(normalized, ""))

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
