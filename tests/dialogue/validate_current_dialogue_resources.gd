extends SceneTree

const EXPECTED_TOTAL_SPOKEN := 2001

var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var data := DiyseCurrentDialogueCatalog.manifest()
	_expect(not data.is_empty(), "Current runtime dialogue manifest must load")
	if data.is_empty():
		_finish()
		return

	_expect(str(data.get("schema", "")) == "diyse_current_runtime_dialogue_manifest_v1", "Current runtime dialogue manifest schema changed")
	_expect(int(data.get("expected_total_spoken", -1)) == EXPECTED_TOTAL_SPOKEN, "Manifest expected spoken total changed")

	var chapters_value = data.get("chapters", {})
	_expect(chapters_value is Dictionary, "Manifest chapters must be a Dictionary")
	if not (chapters_value is Dictionary):
		_finish()
		return

	var total_spoken := 0
	var scene_count := 0
	for chapter_id in ["chapter_00", "chapter_01", "chapter_02", "chapter_03"]:
		var chapter_value = (chapters_value as Dictionary).get(chapter_id, {})
		_expect(chapter_value is Dictionary, "%s manifest entry is missing" % chapter_id)
		if not (chapter_value is Dictionary):
			continue
		var chapter: Dictionary = chapter_value
		var registry := DiyseCurrentDialogueCatalog.load_registry(chapter_id)
		_expect(registry != null, "%s current portrait registry must load" % chapter_id)
		if registry == null:
			continue

		var scenes_value = chapter.get("scenes", [])
		_expect(scenes_value is Array, "%s scenes must be an Array" % chapter_id)
		if not (scenes_value is Array):
			continue

		for entry_value in scenes_value:
			_expect(entry_value is Dictionary, "%s scene manifest entry must be a Dictionary" % chapter_id)
			if not (entry_value is Dictionary):
				continue
			var entry: Dictionary = entry_value
			var slot_id := str(entry.get("slot_id", ""))
			var scene := DiyseCurrentDialogueCatalog.load_scene(chapter_id, slot_id)
			_expect(scene != null, "%s/%s current Resource must load" % [chapter_id, slot_id])
			if scene == null:
				continue

			for failure in scene.validate_schema(registry):
				failures.append("%s/%s schema: %s" % [chapter_id, slot_id, failure])

			_expect(scene.scene_id == str(entry.get("scene_id", "")), "%s/%s scene_id differs from manifest" % [chapter_id, slot_id])
			_expect(scene.chapter_id == chapter_id, "%s/%s chapter_id changed" % [chapter_id, slot_id])
			_expect(scene.scene_kind == str(entry.get("scene_kind", "")), "%s/%s scene_kind differs from manifest" % [chapter_id, slot_id])

			var spoken := 0
			for beat in scene.beats:
				if not str(beat.get("speaker_id", "")).is_empty():
					spoken += 1
			_expect(spoken == int(entry.get("spoken_lines", -1)), "%s/%s spoken-line count differs from manifest" % [chapter_id, slot_id])
			total_spoken += spoken
			scene_count += 1

	_expect(scene_count == 56, "Current runtime dialogue scene count changed: expected 56, got %d" % scene_count)
	_expect(total_spoken == EXPECTED_TOTAL_SPOKEN, "Current runtime dialogue spoken total changed: expected %d, got %d" % [EXPECTED_TOTAL_SPOKEN, total_spoken])
	_expect(int(data.get("total_spoken", -1)) == EXPECTED_TOTAL_SPOKEN, "Manifest compiled spoken total changed")
	_finish()

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Current Chapters 0-3 runtime dialogue Resources validated: 56 scenes / 2001 spoken lines.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
