extends SceneTree

const SCENE_PATH := "res://game/content/dialogue/chapter_00/C02.tres"
const REGISTRY_PATH := "res://game/content/dialogue/chapter_00/chapter_00_dialogue_registry.tres"
const EXPECTED_BEAT_COUNT := 61
const ALLOWED_SPEAKERS := ["cyanis", "ilyra"]
const FORBIDDEN_SPOKEN_TERMS := [
	"first champion",
	"first mercy",
	"prime",
	"card",
	"black host",
	"brackenwall",
	"war-sorcerer",
	"prophecy",
	"chosen",
	"quest",
	"vaelkor",
	"entity",
	"romance",
	"kiss"
]

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var failures: Array[String] = []
	var scene := load(SCENE_PATH) as DiyseDialogueSceneDefinition
	var registry := load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry
	if scene == null:
		failures.append("Could not load C02 production scene Resource")
		_finish(failures)
		return
	if registry == null:
		failures.append("Could not load Chapter 0 dialogue registry")
		_finish(failures)
		return

	for failure in scene.validate_schema(registry):
		failures.append("Schema: %s" % failure)

	if scene.scene_id != "C02": failures.append("C02 scene_id changed")
	if scene.chapter_id != "chapter_00": failures.append("C02 must remain in chapter_00")
	if scene.scene_kind != "character_life": failures.append("C02 must remain character_life")
	if scene.location_id != "LOC_BORDERLANDS_FIELD_TRIAGE_CAMP": failures.append("C02 location changed")
	if scene.trigger_id != "trigger.chapter_00.c02.after_s006": failures.append("C02 must remain available after S006")
	if scene.completion_flag != "scene.c02.complete": failures.append("C02 completion flag changed")
	if scene.participants != Array[String](["cyanis", "ilyra"]): failures.append("C02 participants must remain Cyanis and Ilyra only")
	if scene.beats.size() != EXPECTED_BEAT_COUNT:
		failures.append("C02 beat count changed: expected %d, got %d" % [EXPECTED_BEAT_COUNT, scene.beats.size()])

	var combined_spoken := ""
	var combined_staging := ""
	var cyanis_lines := 0
	var ilyra_lines := 0
	for i in range(scene.beats.size()):
		var beat: Dictionary = scene.beats[i]
		var expected_id := "C02_B%03d" % (i + 1)
		if str(beat.get("beat_id", "")) != expected_id:
			failures.append("C02 beat %d must use stable ID %s" % [i + 1, expected_id])
		var speaker := str(beat.get("speaker_id", ""))
		if not speaker.is_empty() and speaker not in ALLOWED_SPEAKERS:
			failures.append("C02 introduces unapproved speaker: %s" % speaker)
		if speaker == "cyanis": cyanis_lines += 1
		if speaker == "ilyra": ilyra_lines += 1
		var text := str(beat.get("text", ""))
		combined_spoken += " " + text.to_lower()
		if "res://" in text: failures.append("Raw asset path leaked into C02 spoken dialogue")
		var left = beat.get("left", {})
		var right = beat.get("right", {})
		if not (left is Dictionary) or not left.is_empty(): failures.append("C02 must not use a proof portrait in left slot at %s" % expected_id)
		if not (right is Dictionary) or not right.is_empty(): failures.append("C02 must not use a proof portrait in right slot at %s" % expected_id)
		var cues = beat.get("cues", {})
		if cues is Dictionary:
			combined_staging += " " + str(cues.get("staging", "")).to_lower()

	if cyanis_lines < 15 or ilyra_lines < 15:
		failures.append("C02 must remain a balanced two-character conversation")
	for term in FORBIDDEN_SPOKEN_TERMS:
		if term in combined_spoken:
			failures.append("C02 carries forbidden plot/lore/romance terminology in spoken dialogue: %s" % term)
	for phrase in [
		"when did you eat?",
		"not since before the attack.",
		"and you're standing here telling me to eat.",
		"you haven't eaten yet.",
		"neither have you.",
		"no. i just remembered i was hungry.",
		"this is stupid.",
		"very.",
		"then we're both trapped.",
		"same rule for you.",
		"that seems unnecessarily symmetrical."
	]:
		if phrase not in combined_spoken:
			failures.append("C02 lost required mutual-self-care/quiet-ease beat: %s" % phrase)
	for staging_phrase in [
		"the silence is not awkward",
		"neither cyanis nor ilyra is doing anything useful for anyone else",
		"nothing needs to be said"
	]:
		if staging_phrase not in combined_staging:
			failures.append("C02 lost required quiet-ease staging beat: %s" % staging_phrase)

	var runner_beats := scene.to_runner_beats(registry)
	if runner_beats.size() != scene.beats.size():
		failures.append("C02 did not adapt one-for-one into generic runner beats")
	for runner_beat in runner_beats:
		if str(runner_beat.get("left_portrait", "")) != "" or str(runner_beat.get("right_portrait", "")) != "":
			failures.append("C02 unexpectedly resolved a proof/temporary portrait asset")
			break

	_finish(failures)

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Diyse Step 7C C02 character-life, mutual-self-neglect, food, quiet-ease, no-plot-delivery, and runner-adaptation validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
