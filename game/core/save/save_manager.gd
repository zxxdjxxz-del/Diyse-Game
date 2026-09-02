extends Node

const GameStateScript = preload("res://game/core/state/game_state.gd")

const SCHEMA_VERSION := 3
const MIN_SUPPORTED_SCHEMA_VERSION := 1
const SAVE_PATH := "user://diyse_7b5g_save.json"

func save_state(state: Node, path: String = SAVE_PATH) -> Dictionary:
	if state == null or not state.has_method("to_save_dict"):
		return _failure("Invalid game state.")
	var data: Dictionary = state.to_save_dict(SCHEMA_VERSION)
	var file := FileAccess.open(path, FileAccess.WRITE)
	if file == null:
		return _failure("Could not open save file for writing.")
	file.store_string(JSON.stringify(data, "  "))
	file.flush()
	return {"ok": true, "message": "Save complete.", "path": path}

func load_state(state: Node, path: String = SAVE_PATH) -> Dictionary:
	if state == null or not state.has_method("apply_save_dict"):
		return _failure("Invalid game state.")
	var read_result := read_save_data(path)
	if not bool(read_result.get("ok", false)):
		return read_result
	if not state.apply_save_dict(read_result["data"]):
		return _failure("Save data is incomplete or invalid.")
	return {
		"ok": true,
		"message": "Load complete.",
		"path": path,
		"data": read_result["data"],
		"migrated_from_schema": read_result.get("migrated_from_schema", SCHEMA_VERSION)
	}

func read_save_data(path: String = SAVE_PATH) -> Dictionary:
	if not FileAccess.file_exists(path):
		return _failure("No save file found.")
	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		return _failure("Could not open save file.")
	var text := file.get_as_text()
	var parsed = JSON.parse_string(text)
	if not (parsed is Dictionary):
		return _failure("Save file is corrupt or invalid JSON.")
	var data: Dictionary = parsed
	if not data.has("schema_version"):
		return _failure("Save file has no schema version.")
	var version := int(data.get("schema_version", -1))
	if version > SCHEMA_VERSION or version < MIN_SUPPORTED_SCHEMA_VERSION:
		return _failure("Unsupported save schema version: %d." % version)

	var migration := _migrate_to_current_schema(data, version)
	if not bool(migration.get("ok", false)):
		return migration
	return {
		"ok": true,
		"message": "Save data valid.",
		"path": path,
		"data": migration["data"],
		"migrated_from_schema": version
	}

func has_save(path: String = SAVE_PATH) -> bool:
	return bool(read_save_data(path).get("ok", false))

func _migrate_to_current_schema(source: Dictionary, source_version: int) -> Dictionary:
	var data := source.duplicate(true)
	var version := source_version
	while version < SCHEMA_VERSION:
		match version:
			1:
				data = _migrate_v1_to_v2(data)
				version = 2
			2:
				data = _migrate_v2_to_v3(data)
				version = 3
			_:
				return _failure("No migration path from save schema version: %d." % version)
	data["schema_version"] = SCHEMA_VERSION
	return {"ok": true, "data": data}

func _migrate_v1_to_v2(data: Dictionary) -> Dictionary:
	var migrated := data.duplicate(true)
	# Schema v1 had no persistent party wallet. Its `rewards.gold` value is a
	# proof battle-result payload and must not be silently reinterpreted as G.
	# The new wallet therefore enters at the current authoritative starting
	# baseline when normalizing a legacy proof save.
	if not migrated.has("wallet_g"):
		migrated["wallet_g"] = GameStateScript.STARTING_WALLET_G
	migrated["schema_version"] = 2
	return migrated

func _migrate_v2_to_v3(data: Dictionary) -> Dictionary:
	var migrated := data.duplicate(true)
	# Schema v2 still treated the old four-character `party` array as proof state.
	# Do not infer production recruitment from that fixture. Introduce the new
	# permanent roster at the canonical new-game baseline: Cyanis recruited and
	# active, later characters present as stable IDs but unrecruited.
	if not migrated.has("character_roster"):
		migrated["character_roster"] = GameStateScript.default_character_roster()
	if not migrated.has("active_party_ids"):
		migrated["active_party_ids"] = ["cyanis"]
	migrated["schema_version"] = 3
	return migrated

func _failure(message: String) -> Dictionary:
	return {"ok": false, "message": message}
