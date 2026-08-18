extends SceneTree

const REGISTRY_PATH := "res://game/content/dialogue/chapter_01/chapter_01_dialogue_registry.tres"
const SCENE_SPECS := [
	{"id": "S007", "path": "res://game/content/dialogue/chapter_01/S007.tres", "source": "res://docs/chapters/dialogue/chapter_01/S007.md", "kind": "mandatory", "location": "LOC_BRACKENWALL", "trigger": "trigger.chapter_01.s007", "beats": 101, "spoken": 98},
	{"id": "S008", "path": "res://game/content/dialogue/chapter_01/S008.tres", "source": "res://docs/chapters/dialogue/chapter_01/S008.md", "kind": "mandatory", "location": "LOC_HOLLOW_WATCH", "trigger": "trigger.chapter_01.s008", "beats": 68, "spoken": 62},
	{"id": "S009", "path": "res://game/content/dialogue/chapter_01/S009.tres", "source": "res://docs/chapters/dialogue/chapter_01/S009.md", "kind": "mandatory", "location": "LOC_GREENHOLLOW", "trigger": "trigger.chapter_01.s009", "beats": 131, "spoken": 128},
	{"id": "S010", "path": "res://game/content/dialogue/chapter_01/S010.tres", "source": "res://docs/chapters/dialogue/chapter_01/S010.md", "kind": "mandatory", "location": "LOC_BRIAR_PASSAGE", "trigger": "trigger.chapter_01.s010", "beats": 107, "spoken": 106},
	{"id": "S011", "path": "res://game/content/dialogue/chapter_01/S011.tres", "source": "res://docs/chapters/dialogue/chapter_01/S011.md", "kind": "mandatory", "location": "LOC_WAYFINDER_JUNCTION", "trigger": "trigger.chapter_01.s011", "beats": 112, "spoken": 110},
	{"id": "C03", "path": "res://game/content/dialogue/chapter_01/C03.tres", "source": "res://docs/chapters/dialogue/chapter_01/C03.md", "kind": "character_life", "location": "LOC_CHAPTER_01_ROADSIDE_REST", "trigger": "trigger.chapter_01.c03.after_s011", "beats": 89, "spoken": 87},
	{"id": "C04", "path": "res://game/content/dialogue/chapter_01/C04.tres", "source": "res://docs/chapters/dialogue/chapter_01/C04.md", "kind": "character_life", "location": "LOC_BRACKENWALL_ROUTE_ROOM", "trigger": "trigger.chapter_01.c04.after_s011", "beats": 115, "spoken": 114},
	{"id": "C05", "path": "res://game/content/dialogue/chapter_01/C05.tres", "source": "res://docs/chapters/dialogue/chapter_01/C05.md", "kind": "character_life", "location": "LOC_BRACKENWALL_SUPPLY_MEDICAL", "trigger": "trigger.chapter_01.c05.after_s011", "beats": 117, "spoken": 116}
]
const SOURCE_SPEAKER_IDS := {
	"CYANIS": "cyanis",
	"ILYRA": "ilyra",
	"MAEVRA": "maevra",
	"TORREN": "torren",
	"CUSTODY OFFICER": "custody_officer",
	"SERGEANT": "sergeant",
	"SCOUT": "scout",
	"EDDA": "edda",
	"INJURED CIVILIAN": "injured_civilian",
	"RUNNER": "runner"
}

var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var registry := load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry
	_expect(registry != null, "Chapter 1 portrait registry must load")
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
	_expect(scene.chapter_id == "chapter_01", "%s must remain chapter_01" % scene_id)
	_expect(scene.scene_kind == str(spec["kind"]), "%s scene_kind changed" % scene_id)
	_expect(scene.location_id == str(spec["location"]), "%s location_id changed" % scene_id)
	_expect(scene.trigger_id == str(spec["trigger"]), "%s trigger_id changed" % scene_id)
	_expect(scene.completion_flag == "scene.%s.complete" % scene_id.to_lower(), "%s completion flag changed" % scene_id)
	_expect(scene.beats.size() == int(spec["beats"]), "%s beat count changed: expected %d, got %d" % [scene_id, int(spec["beats"]), scene.beats.size()])

	var resource_spoken: Array[Dictionary] = []
	for beat in scene.beats:
		var speaker_id := str(beat.get("speaker_id", ""))
		if not speaker_id.is_empty():
			resource_spoken.append({"speaker_id": speaker_id, "text": str(beat.get("text", ""))})
	_expect(resource_spoken.size() == int(spec["spoken"]), "%s spoken-line count changed: expected %d, got %d" % [scene_id, int(spec["spoken"]), resource_spoken.size()])

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
		if not SOURCE_SPEAKER_IDS.has(source_name):
			failures.append("%s source contains unmapped dialogue speaker: %s" % [scene_id, source_name])
			continue
		var text := line.substr(separator + 3).strip_edges()
		result.append({"speaker_id": str(SOURCE_SPEAKER_IDS[source_name]), "text": text})
	return result

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Chapter 1 exact dialogue Resource/schema/source-parity validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
