extends Node

const SCHEMA_VERSION := 1
const SAVE_PATH := "user://diyse_save.json"
const LEGACY_SAVE_PATH := "user://diyse_7b5g_save.json"

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

func load_state(state: Node, path: String = SAVE_PATH, legacy_fallback_path: String = "") -> Dictionary:
	if state == null or not state.has_method("apply_save_dict"):
		return _failure("Invalid game state.")
	var resolved_path := _resolve_load_path(path, legacy_fallback_path)
	var read_result := read_save_data(resolved_path)
	if not bool(read_result.get("ok", false)):
		return read_result
	if not state.apply_save_dict(read_result["data"]):
		return _failure("Save data is incomplete or invalid.")
	return {
		"ok": true,
		"message": "Load complete.",
		"path": resolved_path,
		"data": read_result["data"],
		"used_legacy_fallback": resolved_path != path
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
	if version != SCHEMA_VERSION:
		return _failure("Unsupported save schema version: %d." % version)
	return {"ok": true, "message": "Save data valid.", "path": path, "data": data}

func has_save(path: String = SAVE_PATH, legacy_fallback_path: String = "") -> bool:
	var resolved_path := _resolve_load_path(path, legacy_fallback_path)
	return bool(read_save_data(resolved_path).get("ok", false))

func _resolve_load_path(path: String, legacy_fallback_path: String = "") -> String:
	if FileAccess.file_exists(path):
		return path
	var fallback_path := legacy_fallback_path
	if fallback_path.is_empty() and path == SAVE_PATH:
		fallback_path = LEGACY_SAVE_PATH
	if not fallback_path.is_empty() and FileAccess.file_exists(fallback_path):
		return fallback_path
	return path

func _failure(message: String) -> Dictionary:
	return {"ok": false, "message": message}
