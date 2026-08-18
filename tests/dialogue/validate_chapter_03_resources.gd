extends SceneTree

const REGISTRY_PATH := "res://game/content/dialogue/chapter_03/chapter_03_dialogue_registry.tres"
const SCENE_SPECS := [
	{"id": "S017", "path": "res://game/content/dialogue/chapter_03/S017.tres", "source": "res://docs/chapters/dialogue/chapter_03/S017.md", "kind": "mandatory", "location": "LOC_CAELORA_CONTAINMENT", "trigger": "trigger.chapter_03.s017"},
	{"id": "S018", "path": "res://game/content/dialogue/chapter_03/S018.tres", "source": "res://docs/chapters/dialogue/chapter_03/S018.md", "kind": "mandatory", "location": "LOC_CAELORA_JUDICIAL_CAUSEWAY", "trigger": "trigger.chapter_03.s018"},
	{"id": "S019", "path": "res://game/content/dialogue/chapter_03/S019.tres", "source": "res://docs/chapters/dialogue/chapter_03/S019.md", "kind": "mandatory", "location": "LOC_OLD_CITY_SUPPRESSED_ARCHIVES", "trigger": "trigger.chapter_03.s019"},
	{"id": "S020", "path": "res://game/content/dialogue/chapter_03/S020.tres", "source": "res://docs/chapters/dialogue/chapter_03/S020.md", "kind": "mandatory", "location": "LOC_OLD_CITY_COMMAND_STATION", "trigger": "trigger.chapter_03.s020"},
	{"id": "S021", "path": "res://game/content/dialogue/chapter_03/S021.tres", "source": "res://docs/chapters/dialogue/chapter_03/S021.md", "kind": "mandatory", "location": "LOC_CRESTHAVEN", "trigger": "trigger.chapter_03.s021.next_morning"},
	{"id": "H01", "path": "res://game/content/dialogue/chapter_03/H01.tres", "source": "res://docs/chapters/dialogue/chapter_03/H01.md", "kind": "character_life", "location": "LOC_CRESTHAVEN_ARCHIVE_COMMON", "trigger": "trigger.chapter_03.h01.after_s019.at_cresthaven"},
	{"id": "H02", "path": "res://game/content/dialogue/chapter_03/H02.tres", "source": "res://docs/chapters/dialogue/chapter_03/H02.md", "kind": "character_life", "location": "LOC_CRESTHAVEN_RECORDS_ROOM", "trigger": "trigger.chapter_03.h02.after_s018.at_cresthaven"},
	{"id": "H03", "path": "res://game/content/dialogue/chapter_03/H03.tres", "source": "res://docs/chapters/dialogue/chapter_03/H03.md", "kind": "character_life", "location": "LOC_CRESTHAVEN_MEDICAL", "trigger": "trigger.chapter_03.h03.after_s019.at_cresthaven"},
	{"id": "H04", "path": "res://game/content/dialogue/chapter_03/H04.tres", "source": "res://docs/chapters/dialogue/chapter_03/H04.md", "kind": "character_life", "location": "LOC_CRESTHAVEN_COMMON", "trigger": "trigger.chapter_03.h04.after_s021"}
]

var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var registry := load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry
	_expect(registry != null, "Chapter 3 portrait registry must load")
	if registry == null:
		_finish()
		return
	for spec in SCENE_SPECS:
		_validate_scene(spec, registry)
	_finish()

func _validate_scene(spec: Dictionary, registry: DiyseDialoguePortraitRegistry) -> void:
	var scene_id := str(spec["id"])
	var scene := load(str(spec["path"])) as DiyseDialogueSceneDefinition
	_expect(scene != null, "%s Resource must load" % scene_id)
	if scene == null:
		return
	for failure in scene.validate_schema(registry):
		failures.append("%s schema: %s" % [scene_id, failure])
	_expect(scene.scene_id == scene_id, "%s scene_id changed" % scene_id)
	_expect(scene.chapter_id == "chapter_03", "%s must remain chapter_03" % scene_id)
	_expect(scene.scene_kind == str(spec["kind"]), "%s scene_kind changed" % scene_id)
	_expect(scene.location_id == str(spec["location"]), "%s location_id changed" % scene_id)
	_expect(scene.trigger_id == str(spec["trigger"]), "%s trigger_id changed" % scene_id)
	_expect(scene.completion_flag == "scene.%s.complete" % scene_id.to_lower(), "%s completion flag changed" % scene_id)
	_expect(not scene.beats.is_empty(), "%s must contain beats" % scene_id)

	var resource_spoken: Array[Dictionary] = []
	for beat in scene.beats:
		var speaker_id := str(beat.get("speaker_id", ""))
		if not speaker_id.is_empty():
			resource_spoken.append({"speaker_id": speaker_id, "text": str(beat.get("text", ""))})

	var source_spoken := _parse_source_spoken(str(spec["source"]), scene_id)
	_expect(source_spoken.size() == resource_spoken.size(), "%s source/Resource spoken-line counts differ: source %d, Resource %d" % [scene_id, source_spoken.size(), resource_spoken.size()])
	var compare_count: int = min(source_spoken.size(), resource_spoken.size())
	for i in range(compare_count):
		var expected: Dictionary = source_spoken[i]
		var actual: Dictionary = resource_spoken[i]
		if expected != actual:
			failures.append("%s exact dialogue mismatch at spoken line %d: expected %s, got %s" % [scene_id, i + 1, str(expected), str(actual)])
			break

	var source_participants: Array[String] = []
	for item in source_spoken:
		var speaker_id := str(item["speaker_id"])
		if speaker_id not in source_participants:
			source_participants.append(speaker_id)
	for speaker_id in source_participants:
		_expect(speaker_id in scene.participants, "%s participants missing source speaker %s" % [scene_id, speaker_id])

func _parse_source_spoken(path: String, scene_id: String) -> Array[Dictionary]:
	var result: Array[Dictionary] = []
	var source := FileAccess.get_file_as_string(path)
	_expect(not source.is_empty(), "%s controlling Markdown source must be readable: %s" % [scene_id, path])
	var current_section := ""
	for raw_line in source.split("\n"):
		var line := str(raw_line).strip_edges()
		if line.begins_with("### ") or line.begins_with("## "):
			current_section = line
			continue
		if current_section.is_empty() or not line.begins_with("**"):
			continue
		var separator := line.find(":**")
		if separator < 0:
			continue
		var source_name := line.substr(2, separator - 2)
		if source_name != source_name.to_upper():
			continue
		var text := line.substr(separator + 3).strip_edges()
		result.append({"speaker_id": _speaker_id(source_name), "text": text})
	return result

func _speaker_id(source_name: String) -> String:
	var value := source_name.strip_edges().to_lower()
	value = value.replace("’", "").replace("'", "")
	value = value.replace("—", " ").replace("–", " ").replace("/", " ")
	var output := ""
	var previous_underscore := false
	for i in range(value.length()):
		var code := value.unicode_at(i)
		var is_letter := code >= 97 and code <= 122
		var is_digit := code >= 48 and code <= 57
		if is_letter or is_digit:
			output += value.substr(i, 1)
			previous_underscore = false
		elif not output.is_empty() and not previous_underscore:
			output += "_"
			previous_underscore = true
	return output.trim_suffix("_")

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Chapter 3 exact dialogue Resource/schema/source-parity validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
