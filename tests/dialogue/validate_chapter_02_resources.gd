extends SceneTree

const REGISTRY_PATH := "res://game/content/dialogue/chapter_02/chapter_02_dialogue_registry.tres"
const SCENE_SPECS := [
	{"id": "S012", "path": "res://game/content/dialogue/chapter_02/S012.tres", "source": "res://docs/chapters/dialogue/chapter_02/S012.md", "kind": "mandatory", "location": "LOC_DUNMERE_WATERWORKS", "trigger": "trigger.chapter_02.s012"},
	{"id": "S013", "path": "res://game/content/dialogue/chapter_02/S013.tres", "source": "res://docs/chapters/dialogue/chapter_02/S013.md", "kind": "mandatory", "location": "LOC_SUNKEN_ARCHIVE", "trigger": "trigger.chapter_02.s013"},
	{"id": "S014", "path": "res://game/content/dialogue/chapter_02/S014.tres", "source": "res://docs/chapters/dialogue/chapter_02/S014.md", "kind": "mandatory", "location": "LOC_PRISONER_GALLERIES", "trigger": "trigger.chapter_02.s014"},
	{"id": "S015", "path": "res://game/content/dialogue/chapter_02/S015.tres", "source": "res://docs/chapters/dialogue/chapter_02/S015.md", "kind": "mandatory", "location": "LOC_RED_TRANSFER_BASTION", "trigger": "trigger.chapter_02.s015"},
	{"id": "S016", "path": "res://game/content/dialogue/chapter_02/S016.tres", "source": "res://docs/chapters/dialogue/chapter_02/S016.md", "kind": "mandatory", "location": "LOC_EXTRACTION_CAUSEWAY", "trigger": "trigger.chapter_02.s016"},
	{"id": "C06", "path": "res://game/content/dialogue/chapter_02/C06.tres", "source": "res://docs/chapters/dialogue/chapter_02/C06.md", "kind": "character_life", "location": "LOC_DUNMERE_REST_AREA", "trigger": "trigger.chapter_02.c06.after_s016"},
	{"id": "C07", "path": "res://game/content/dialogue/chapter_02/C07.tres", "source": "res://docs/chapters/dialogue/chapter_02/C07.md", "kind": "character_life", "location": "LOC_DUNMERE_REST_AREA", "trigger": "trigger.chapter_02.c07.after_s016"}
]

const SOURCE_SPEAKER_IDS := {
	"CYANIS": "cyanis",
	"ILYRA": "ilyra",
	"MAEVRA": "maevra",
	"TORREN": "torren",
	"WATERMASTER": "watermaster",
	"WORKER": "worker",
	"PARTY ACTOR": "party_actor",
	"PRISONER WOMAN": "prisoner_woman",
	"PRISONER WOMAN — THROUGH DOOR": "prisoner_woman",
	"INJURED MAN": "injured_man",
	"PRISONER": "prisoner",
	"SECOND PRISONER": "second_prisoner",
	"OLDER PRISONER": "older_prisoner",
	"OFFICER": "officer",
	"SECOND OFFICER": "second_officer",
	"RHAZEK": "rhazek",
	"EVACUEE": "evacuee",
	"ILYRA / TORREN": "ilyra_torren"
}

var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var registry := load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry
	_expect(registry != null, "Chapter 2 portrait registry must load")
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
	_expect(scene.chapter_id == "chapter_02", "%s must remain chapter_02" % scene_id)
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
	var standalone_speaker := ""
	for raw_line in source.split("\n"):
		var line := str(raw_line).strip_edges()
		if line.begins_with("### ") or line.begins_with("## "):
			current_section = line
			standalone_speaker = ""
			continue
		if current_section.is_empty():
			continue

		if line.begins_with("**"):
			var separator := line.find(":**")
			if separator >= 0:
				var source_name := line.substr(2, separator - 2)
				if source_name == source_name.to_upper():
					if not SOURCE_SPEAKER_IDS.has(source_name):
						failures.append("%s source contains unmapped dialogue speaker: %s" % [scene_id, source_name])
						continue
					var text := line.substr(separator + 3).strip_edges()
					result.append({"speaker_id": str(SOURCE_SPEAKER_IDS[source_name]), "text": text})
					standalone_speaker = ""
					continue
			if line.ends_with("**") and line.length() > 4:
				var standalone_name := line.substr(2, line.length() - 4)
				if SOURCE_SPEAKER_IDS.has(standalone_name):
					standalone_speaker = standalone_name
					continue

		if not standalone_speaker.is_empty() and not line.is_empty():
			result.append({"speaker_id": str(SOURCE_SPEAKER_IDS[standalone_speaker]), "text": line})
			standalone_speaker = ""
	return result

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Chapter 2 exact dialogue Resource/schema/source-parity validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
