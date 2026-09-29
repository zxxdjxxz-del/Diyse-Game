extends SceneTree

const REGISTRY_PATH := "res://game/content/dialogue/current/chapter_01/chapter_01_dialogue_registry.tres"

const SCENE_SPECS := [
	{"id": "B01", "path": "res://game/content/dialogue/current/chapter_01/B01.tres", "source": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CH01_B01_BRACKENWALL_PROTOCOL_DIALOGUE.md", "kind": "mandatory"},
	{"id": "B02", "path": "res://game/content/dialogue/current/chapter_01/B02.tres", "source": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CH01_B02_BRIAR_PASSAGE_FIRST_TRAVERSAL_DIALOGUE.md", "kind": "mandatory"},
	{"id": "B03", "path": "res://game/content/dialogue/current/chapter_01/B03.tres", "source": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CH01_B03_GREENHOLLOW_TORREN_DIALOGUE.md", "kind": "mandatory"},
	{"id": "B04", "path": "res://game/content/dialogue/current/chapter_01/B04.tres", "source": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CH01_B04_HOLLOW_WATCH_APPROACH_DIALOGUE.md", "kind": "mandatory"},
	{"id": "B05", "path": "res://game/content/dialogue/current/chapter_01/B05.tres", "source": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CH01_B05_OCCUPIED_HOLLOW_WATCH_FORT_DIALOGUE.md", "kind": "mandatory"},
	{"id": "B06", "path": "res://game/content/dialogue/current/chapter_01/B06.tres", "source": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CH01_B06_HOLLOW_WATCH_EXCAVATION_DIALOGUE.md", "kind": "mandatory"},
	{"id": "B07", "path": "res://game/content/dialogue/current/chapter_01/B07.tres", "source": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CH01_B07_HOLLOW_WATCH_LANDSCAPE_DEPICTION_DIALOGUE.md", "kind": "mandatory"},
	{"id": "B08", "path": "res://game/content/dialogue/current/chapter_01/B08.tres", "source": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CH01_B08_GREENHOLLOW_RESOLUTION_TORREN_RECRUITMENT_DIALOGUE.md", "kind": "mandatory"},
	{"id": "B09", "path": "res://game/content/dialogue/current/chapter_01/B09.tres", "source": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CH01_B09_SOUTHERN_BRIAR_PASSAGE_DIALOGUE.md", "kind": "mandatory"},
	{"id": "B10", "path": "res://game/content/dialogue/current/chapter_01/B10.tres", "source": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CH01_B10_THORNHIDE_DIALOGUE.md", "kind": "mandatory"},
	{"id": "B11", "path": "res://game/content/dialogue/current/chapter_01/B11.tres", "source": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CH01_B11_THE_JUNCTION_HIDDEN_MONUMENT_DIALOGUE.md", "kind": "mandatory"},
	{"id": "B12", "path": "res://game/content/dialogue/current/chapter_01/B12.tres", "source": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CH01_B12_JUNCTION_CAMP_CLEANUP_DIALOGUE.md", "kind": "mandatory"},
	{"id": "C02", "path": "res://game/content/dialogue/current/chapter_01/C02.tres", "source": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/C02_TORRENS_VERSION_OF_DINNER_DIALOGUE.md", "kind": "character_life"},
	{"id": "C03", "path": "res://game/content/dialogue/current/chapter_01/C03.tres", "source": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/C03_WHAT_THE_MAP_SAYS_DIALOGUE.md", "kind": "character_life"},
	{"id": "C04", "path": "res://game/content/dialogue/current/chapter_01/C04.tres", "source": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/C04_NOT_PROFESSIONALLY_DIALOGUE.md", "kind": "character_life"},
]

var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var registry := load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry
	_expect(registry != null, "Current Chapter 1 portrait registry must load")
	if registry == null:
		_finish()
		return

	for spec in SCENE_SPECS:
		_validate_scene(spec, registry)
	_finish()

func _validate_scene(spec: Dictionary, registry: DiyseDialoguePortraitRegistry) -> void:
	var short_id := str(spec["id"])
	var scene := load(str(spec["path"])) as DiyseDialogueSceneDefinition
	_expect(scene != null, "%s current Resource must load" % short_id)
	if scene == null:
		return

	for failure in scene.validate_schema(registry):
		failures.append("%s schema: %s" % [short_id, failure])

	_expect(scene.chapter_id == "chapter_01", "%s must remain chapter_01" % short_id)
	_expect(scene.scene_id.begins_with("CH01_%s_" % short_id), "%s scene_id must use current CH01_%s_* identity" % [short_id, short_id])
	_expect(scene.scene_kind == str(spec["kind"]), "%s scene_kind changed" % short_id)
	_expect(scene.trigger_id == "trigger.chapter_01.%s" % short_id.to_lower(), "%s trigger_id changed" % short_id)
	_expect(scene.completion_flag == "scene.ch01_%s.complete" % short_id.to_lower(), "%s completion flag changed" % short_id)
	_expect(not scene.location_id.is_empty(), "%s location_id must not be empty" % short_id)
	_expect(not scene.story_position.is_empty(), "%s story_position must not be empty" % short_id)

	_validate_source_provenance(short_id, scene, str(spec["source"]))

func _validate_source_provenance(short_id: String, scene: DiyseDialogueSceneDefinition, source_path: String) -> void:
	var res_source_path := "res://" + source_path
	_expect(FileAccess.file_exists(res_source_path), "%s controlling production source must exist: %s" % [short_id, res_source_path])
	if not FileAccess.file_exists(res_source_path):
		return

	var source_text := FileAccess.get_file_as_string(res_source_path)
	_expect(not source_text.is_empty(), "%s controlling production source must be readable" % short_id)
	if source_text.is_empty():
		return

	var source_lines := source_text.split("\n")
	var spoken_count := 0

	for beat in scene.beats:
		var speaker_id := str(beat.get("speaker_id", ""))
		if speaker_id.is_empty():
			continue

		spoken_count += 1
		_expect(speaker_id in scene.participants, "%s spoken speaker missing from participants: %s" % [short_id, speaker_id])

		var cues = beat.get("cues", {})
		_expect(cues is Dictionary, "%s spoken beat is missing cue provenance" % short_id)
		if not (cues is Dictionary):
			continue

		var recorded_path := str(cues.get("source_path", ""))
		_expect(recorded_path == source_path, "%s beat source_path drifted: %s" % [short_id, recorded_path])

		var source_line := int(cues.get("source_line", 0))
		_expect(source_line > 0 and source_line <= source_lines.size(), "%s source_line is outside controlling source: %d" % [short_id, source_line])
		if source_line <= 0 or source_line > source_lines.size():
			continue

		var source_line_text := str(source_lines[source_line - 1]).strip_edges()
		var beat_text := str(beat.get("text", ""))
		_expect(not beat_text.is_empty(), "%s spoken beat has empty text" % short_id)
		_expect(source_line_text.contains(beat_text), "%s source line %d no longer contains compiled dialogue: %s" % [short_id, source_line, beat_text])

	_expect(spoken_count > 0, "%s must contain at least one spoken line" % short_id)

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Chapter 1 current B01-B12/C02-C04 Resource/schema/source-provenance validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
