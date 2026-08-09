extends SceneTree

const REGISTRY_PATH := "res://game/content/dialogue/chapter_00/chapter_00_dialogue_registry.tres"
const MANDATORY_SCENES := [
	["S001", "res://game/content/dialogue/chapter_00/S001.tres", 28],
	["S002", "res://game/content/dialogue/chapter_00/S002.tres", 49],
	["S003", "res://game/content/dialogue/chapter_00/S003.tres", 35],
	["S004", "res://game/content/dialogue/chapter_00/S004.tres", 57],
	["S005", "res://game/content/dialogue/chapter_00/S005.tres", 31],
	["S006", "res://game/content/dialogue/chapter_00/S006.tres", 60]
]
const CHARACTER_LIFE_SCENES := [
	["C01", "res://game/content/dialogue/chapter_00/C01.tres", 40],
	["C02", "res://game/content/dialogue/chapter_00/C02.tres", 61]
]
const EXPECTED_MANDATORY_BEATS := 260
const EXPECTED_OPTIONAL_BEATS := 101

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var failures: Array[String] = []
	var registry := load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry
	if registry == null:
		failures.append("Could not load Chapter 0 dialogue registry")
		_finish(failures)
		return

	var loaded: Dictionary = {}
	var mandatory_beats := 0
	var optional_beats := 0

	for spec in MANDATORY_SCENES:
		var scene_id := str(spec[0])
		var scene := load(str(spec[1])) as DiyseDialogueSceneDefinition
		if scene == null:
			failures.append("Could not load mandatory Chapter 0 scene: %s" % scene_id)
			continue
		loaded[scene_id] = scene
		for failure in scene.validate_schema(registry):
			failures.append("%s schema: %s" % [scene_id, failure])
		if scene.scene_id != scene_id:
			failures.append("%s scene_id changed" % scene_id)
		if scene.chapter_id != "chapter_00":
			failures.append("%s left chapter_00" % scene_id)
		if scene.scene_kind != "mandatory":
			failures.append("%s must remain mandatory" % scene_id)
		if scene.beats.size() != int(spec[2]):
			failures.append("%s beat count changed: expected %d, got %d" % [scene_id, int(spec[2]), scene.beats.size()])
		mandatory_beats += scene.beats.size()

	for spec in CHARACTER_LIFE_SCENES:
		var scene_id := str(spec[0])
		var scene := load(str(spec[1])) as DiyseDialogueSceneDefinition
		if scene == null:
			failures.append("Could not load Chapter 0 Character-Life scene: %s" % scene_id)
			continue
		loaded[scene_id] = scene
		for failure in scene.validate_schema(registry):
			failures.append("%s schema: %s" % [scene_id, failure])
		if scene.scene_id != scene_id:
			failures.append("%s scene_id changed" % scene_id)
		if scene.chapter_id != "chapter_00":
			failures.append("%s left chapter_00" % scene_id)
		if scene.scene_kind != "character_life":
			failures.append("%s must remain optional character_life" % scene_id)
		if not scene.trigger_id.ends_with("after_s006"):
			failures.append("%s must unlock only after S006" % scene_id)
		if scene.beats.size() != int(spec[2]):
			failures.append("%s beat count changed: expected %d, got %d" % [scene_id, int(spec[2]), scene.beats.size()])
		optional_beats += scene.beats.size()

	if mandatory_beats != EXPECTED_MANDATORY_BEATS:
		failures.append("Chapter 0 mandatory authored-beat total changed: expected %d, got %d" % [EXPECTED_MANDATORY_BEATS, mandatory_beats])
	if optional_beats != EXPECTED_OPTIONAL_BEATS:
		failures.append("Chapter 0 optional Character-Life authored-beat total changed: expected %d, got %d" % [EXPECTED_OPTIONAL_BEATS, optional_beats])

	for early_id in ["S001", "S002", "S003"]:
		if loaded.has(early_id) and "ilyra" in (loaded[early_id] as DiyseDialogueSceneDefinition).participants:
			failures.append("Ilyra entered too early in %s; her first Chapter 0 appearance must remain S004" % early_id)
	for later_id in ["S004", "S005", "S006"]:
		if loaded.has(later_id) and "ilyra" not in (loaded[later_id] as DiyseDialogueSceneDefinition).participants:
			failures.append("Ilyra missing from required post-entry scene %s" % later_id)

	var fair_count := 0
	var strong_opinion_count := 0
	var wasnt_planning_count := 0
	for scene_id in loaded.keys():
		var scene: DiyseDialogueSceneDefinition = loaded[scene_id]
		for beat in scene.beats:
			var text := str(beat.get("text", "")).strip_edges().to_lower()
			if text == "fair.":
				fair_count += 1
			if text.begins_with("you have very strong opinions about"):
				strong_opinion_count += 1
			if text == "wasn't planning to.":
				wasnt_planning_count += 1

	if fair_count > 1:
		failures.append("Chapter 0 overuses exact acknowledgment 'Fair.': %d occurrences" % fair_count)
	if strong_opinion_count > 1:
		failures.append("Chapter 0 repeats 'You have very strong opinions about...' across scenes")
	if wasnt_planning_count > 1:
		failures.append("Chapter 0 repeats exact line 'Wasn't planning to.' too often")

	if loaded.has("S006"):
		var s006: DiyseDialogueSceneDefinition = loaded["S006"]
		var final_beat: Dictionary = s006.beats[-1]
		var cues = final_beat.get("cues", {})
		var flags = cues.get("implementation_flags", []) if cues is Dictionary else []
		for required in [
			"ROSTER_ADD_ILYRA_PERMANENT",
			"STORY_CHAPTER_00_COMPLETE",
			"ROUTE_BRACKENWALL_UNLOCKED",
			"UNLOCK_C01_THE_FIRE_IS_TOO_CLOSE",
			"UNLOCK_C02_FOOD_AFTER_TRIAGE",
			"DO_NOT_AUTO_SKIP_CHARACTER_LIFE_SCENES"
		]:
			if not (flags is Array) or required not in flags:
				failures.append("S006 lost Chapter 0 durable handoff: %s" % required)

	for optional_id in ["C01", "C02"]:
		if not loaded.has(optional_id):
			continue
		var scene: DiyseDialogueSceneDefinition = loaded[optional_id]
		var spoken := ""
		for beat in scene.beats:
			spoken += " " + str(beat.get("text", "")).to_lower()
		for forbidden in ["first champion", "first mercy", "prime", "black host", "brackenwall", "vaelkor", "entity", "quest"]:
			if forbidden in spoken:
				failures.append("%s leaked essential plot/lore terminology: %s" % [optional_id, forbidden])

	_finish(failures)

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Diyse Step 7C Chapter 0 continuity, repetition, ordering, optional-scene firewall, beat-budget, and durable-handoff validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
