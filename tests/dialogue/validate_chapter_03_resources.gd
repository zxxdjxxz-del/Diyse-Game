extends SceneTree

const REGISTRY_PATH := "res://game/content/dialogue/current/chapter_03/chapter_03_dialogue_registry.tres"
const SOURCE_ROOT := "res://docs/03_DIALOGUE/PRODUCTION/CHAPTER_03/"
const EXPECTED_TOTAL_SPOKEN := 700

const SCENE_SPECS := [
	{"id": "B01", "source": "CH03_B01_CAELORA_GATE_ARRIVAL_DIALOGUE.md"},
	{"id": "B02", "source": "CH03_B02_ROYAL_AUDIENCE_CH2_REPORT_DIALOGUE.md"},
	{"id": "B03", "source": "CH03_B03_IMPOSSIBLE_ORDERS_DIALOGUE.md"},
	{"id": "B04", "source": "CH03_B04_SEAL_NOT_USED_DIALOGUE.md"},
	{"id": "B05", "source": "CH03_B05_LOWER_ARCHIVES_ENTRANCE_NIMERA_JOINS_DIALOGUE.md"},
	{"id": "B06", "source": "CH03_B06_LOWER_ARCHIVES_INVESTIGATION_DIALOGUE.md"},
	{"id": "B07", "source": "CH03_B07_DEEP_ARCHIVES_MEMORY_CONSTRUCT_DIALOGUE.md"},
	{"id": "B08", "source": "CH03_B08_INNER_COLLECTIONS_FINDINGS_DIALOGUE.md"},
	{"id": "B09", "source": "CH03_B09_RETURN_TO_MIRENA_CRESTHAVEN_IDENTIFIED_DIALOGUE.md"},
	{"id": "B10", "source": "CH03_B10_CRESTHAVEN_TOWER_BASE_AUTHORITY_CONSTRUCT_DIALOGUE.md"},
	{"id": "B11", "source": "CH03_B11_CRESTHAVEN_HEADQUARTERS_IVORYBRIDGE_DECISION_DIALOGUE.md"},
	{"id": "C06", "source": "C06_NIMERA_TAKES_OVER_A_TABLE_DIALOGUE.md"},
	{"id": "C07", "source": "C07_ILYRA_AND_NIMERA_DIALOGUE.md"},
]

var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var registry := load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry
	_expect(registry != null, "Chapter 3 current portrait registry must load")
	if registry == null:
		_finish()
		return

	var total_spoken := 0
	for spec in SCENE_SPECS:
		total_spoken += _validate_scene(spec, registry)

	for retired_slot in ["B12", "B13", "B14", "B15"]:
		_expect(not ResourceLoader.exists("res://game/content/dialogue/current/chapter_03/%s.tres" % retired_slot), "Retired Chapter-3 current runtime slot must be absent: %s" % retired_slot)

	_expect(total_spoken == EXPECTED_TOTAL_SPOKEN, "Chapter 3 current spoken total changed: expected %d, got %d" % [EXPECTED_TOTAL_SPOKEN, total_spoken])
	_finish()

func _validate_scene(spec: Dictionary, registry: DiyseDialoguePortraitRegistry) -> int:
	var slot_id := str(spec["id"])
	var scene_path := "res://game/content/dialogue/current/chapter_03/%s.tres" % slot_id
	var source_path := SOURCE_ROOT + str(spec["source"])
	var scene := load(scene_path) as DiyseDialogueSceneDefinition
	_expect(scene != null, "%s current Resource must load" % slot_id)
	if scene == null:
		return 0

	for failure in scene.validate_schema(registry):
		failures.append("%s schema: %s" % [slot_id, failure])

	_expect(scene.chapter_id == "chapter_03", "%s must remain chapter_03" % slot_id)
	_expect(scene.scene_id.begins_with("CH03_%s_" % slot_id), "%s must use the canonical current scene ID" % slot_id)
	_expect(scene.trigger_id == "trigger.chapter_03.%s" % slot_id.to_lower(), "%s trigger ID mismatch" % slot_id)
	_expect(scene.completion_flag == "scene.ch03_%s.complete" % slot_id.to_lower(), "%s completion flag mismatch" % slot_id)

	var resource_spoken: Array[Dictionary] = []
	for beat in scene.beats:
		var speaker_id := str(beat.get("speaker_id", ""))
		if not speaker_id.is_empty():
			resource_spoken.append({"speaker_id": speaker_id, "text": str(beat.get("text", ""))})

	var source_spoken := _parse_source_spoken(source_path, slot_id)
	_expect(source_spoken.size() == resource_spoken.size(), "%s source/Resource spoken counts differ: source %d, Resource %d" % [slot_id, source_spoken.size(), resource_spoken.size()])
	var compare_count: int = min(source_spoken.size(), resource_spoken.size())
	for i in range(compare_count):
		if source_spoken[i] != resource_spoken[i]:
			failures.append("%s exact dialogue mismatch at spoken line %d: expected %s, got %s" % [slot_id, i + 1, str(source_spoken[i]), str(resource_spoken[i])])
			break
	return resource_spoken.size()

func _parse_source_spoken(path: String, slot_id: String) -> Array[Dictionary]:
	var result: Array[Dictionary] = []
	var source := FileAccess.get_file_as_string(path)
	_expect(not source.is_empty(), "%s controlling Markdown source must be readable: %s" % [slot_id, path])
	for raw_line in source.split("\n"):
		var line := str(raw_line).strip_edges()
		if not line.begins_with("**"):
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
		print("Diyse Chapter 3 current B01-B11 + C06/C07 Resource/schema/source-parity validation passed: 700 spoken lines.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
