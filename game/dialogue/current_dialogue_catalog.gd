extends RefCounted
class_name DiyseCurrentDialogueCatalog

const MANIFEST_PATH := "res://game/content/dialogue/current/manifest.json"

static var _manifest_cache: Dictionary = {}

static func manifest() -> Dictionary:
	if not _manifest_cache.is_empty():
		return _manifest_cache.duplicate(true)
	var text := FileAccess.get_file_as_string(MANIFEST_PATH)
	if text.is_empty():
		push_error("Current dialogue manifest is missing: %s" % MANIFEST_PATH)
		return {}
	var parsed = JSON.parse_string(text)
	if not (parsed is Dictionary):
		push_error("Current dialogue manifest is not a Dictionary")
		return {}
	_manifest_cache = (parsed as Dictionary).duplicate(true)
	return _manifest_cache.duplicate(true)

static func scene_entry(chapter_id: String, slot_id: String) -> Dictionary:
	var data := manifest()
	var chapters_value = data.get("chapters", {})
	if not (chapters_value is Dictionary):
		return {}
	var chapter_value = (chapters_value as Dictionary).get(chapter_id, {})
	if not (chapter_value is Dictionary):
		return {}
	var scenes_value = (chapter_value as Dictionary).get("scenes", [])
	if not (scenes_value is Array):
		return {}
	for value in scenes_value:
		if value is Dictionary and str(value.get("slot_id", "")) == slot_id:
			return (value as Dictionary).duplicate(true)
	return {}

static func scene_path(chapter_id: String, slot_id: String) -> String:
	return str(scene_entry(chapter_id, slot_id).get("resource_path", ""))

static func load_scene(chapter_id: String, slot_id: String) -> DiyseDialogueSceneDefinition:
	var path := scene_path(chapter_id, slot_id)
	if path.is_empty():
		push_error("No current dialogue scene for %s/%s" % [chapter_id, slot_id])
		return null
	return load(path) as DiyseDialogueSceneDefinition

static func registry_path(chapter_id: String) -> String:
	var data := manifest()
	var chapters_value = data.get("chapters", {})
	if not (chapters_value is Dictionary):
		return ""
	var chapter_value = (chapters_value as Dictionary).get(chapter_id, {})
	if not (chapter_value is Dictionary):
		return ""
	return str((chapter_value as Dictionary).get("registry_path", ""))

static func load_registry(chapter_id: String) -> DiyseDialoguePortraitRegistry:
	var path := registry_path(chapter_id)
	if path.is_empty():
		push_error("No current dialogue registry for %s" % chapter_id)
		return null
	return load(path) as DiyseDialoguePortraitRegistry
