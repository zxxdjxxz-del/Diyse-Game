extends SceneTree

const EXPECTED := {
	"B01": {"scene_id": "CH00_B01_CONVOY_OPENING_AMBUSH", "kind": "mandatory", "spoken": 27},
	"B02": {"scene_id": "CH00_B02_WRECK_FIELD", "kind": "mandatory", "spoken": 44},
	"B03": {"scene_id": "CH00_B03_EVACUATION_RELAY_DECISION", "kind": "mandatory", "spoken": 27},
	"B04": {"scene_id": "CH00_B04_FIELD_TRIAGE_CAMP_ILYRA_FIRST_INCOMPLETE_RESPONSE", "kind": "mandatory", "spoken": 67},
	"B05": {"scene_id": "CH00_B05_CONCEALED_RUIN_VANGUARD", "kind": "mandatory", "spoken": 41},
	"B06": {"scene_id": "CH00_B06_RIFTMAW_WAR_SORCERER_FINAL_BROKEN_CONVOY_CONFRONTATION", "kind": "mandatory", "spoken": 52},
	"B07": {"scene_id": "CH00_B07_AFTERMATH_SURVIVOR_RECOVERY_OVERNIGHT_CAMP", "kind": "mandatory", "spoken": 51},
	"C01": {"scene_id": "CH00_C01_SIX_MINUTES", "kind": "character_life", "spoken": 79},
}

var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var registry := DiyseCurrentDialogueCatalog.load_registry("chapter_00")
	_expect(registry != null, "Current Chapter 0 dialogue registry must load")
	if registry == null:
		_finish()
		return

	var loaded := {}
	var total_spoken := 0

	for slot_id in EXPECTED.keys():
		var scene := DiyseCurrentDialogueCatalog.load_scene("chapter_00", slot_id)
		_expect(scene != null, "Current Chapter 0 scene must load: %s" % slot_id)
		if scene == null:
			continue
		loaded[slot_id] = scene
		for failure in scene.validate_schema(registry):
			failures.append("%s schema: %s" % [slot_id, failure])

		var expected: Dictionary = EXPECTED[slot_id]
		_expect(scene.scene_id == str(expected["scene_id"]), "%s scene_id drifted" % slot_id)
		_expect(scene.chapter_id == "chapter_00", "%s left chapter_00" % slot_id)
		_expect(scene.scene_kind == str(expected["kind"]), "%s scene_kind drifted" % slot_id)
		_expect(scene.trigger_id == "trigger.chapter_00.%s" % slot_id.to_lower(), "%s trigger_id drifted" % slot_id)
		_expect(scene.completion_flag == "scene.ch00_%s.complete" % slot_id.to_lower(), "%s completion_flag drifted" % slot_id)

		var spoken := 0
		for beat in scene.beats:
			if not str(beat.get("speaker_id", "")).is_empty():
				spoken += 1
		_expect(spoken == int(expected["spoken"]), "%s spoken count changed: expected %d, got %d" % [slot_id, int(expected["spoken"]), spoken])
		total_spoken += spoken

	_expect(loaded.size() == 8, "Current Chapter 0 must contain B01-B07 plus C01")
	_expect(total_spoken == 388, "Current Chapter 0 spoken total must remain 388")

	for early_id in ["B01", "B02", "B03"]:
		if loaded.has(early_id):
			_expect("ilyra" not in loaded[early_id].participants, "Ilyra must not enter before B04: %s" % early_id)
	for later_id in ["B04", "B05", "B06", "B07"]:
		if loaded.has(later_id):
			_expect("ilyra" in loaded[later_id].participants, "Ilyra must be present after her B04 entry: %s" % later_id)

	if loaded.has("C01"):
		var c01 = loaded["C01"]
		_expect(c01.participants == Array[String](["ilyra", "cyanis"]), "C01 Six Minutes must remain Ilyra + Cyanis")
		var spoken_text := ""
		for beat in c01.beats:
			spoken_text += " " + str(beat.get("text", "")).to_lower()
		for forbidden in ["first champion", "first mercy", "prime card", "black host", "brackenwall", "vaelkor", "entity"]:
			_expect(forbidden not in spoken_text, "C01 leaked essential plot/lore terminology: %s" % forbidden)

	var fair_count := 0
	var strong_opinion_count := 0
	var wasnt_planning_count := 0
	for slot_id in loaded.keys():
		var scene = loaded[slot_id]
		for beat in scene.beats:
			var text := str(beat.get("text", "")).strip_edges().to_lower()
			if text == "fair.":
				fair_count += 1
			if text.begins_with("you have very strong opinions about"):
				strong_opinion_count += 1
			if text == "wasn't planning to.":
				wasnt_planning_count += 1

	_expect(fair_count <= 1, "Chapter 0 overuses exact acknowledgment 'Fair.'")
	_expect(strong_opinion_count <= 1, "Chapter 0 repeats 'You have very strong opinions about...'")
	_expect(wasnt_planning_count <= 1, "Chapter 0 repeats exact line 'Wasn't planning to.' too often")

	_finish()

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Current Chapter 0 B01-B07 + C01 continuity validation passed: 8 scenes / 388 spoken lines.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
