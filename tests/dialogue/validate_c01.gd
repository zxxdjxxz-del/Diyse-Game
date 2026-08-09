extends SceneTree

const SCENE_PATH := "res://game/content/dialogue/chapter_00/C01.tres"
const REGISTRY_PATH := "res://game/content/dialogue/chapter_00/chapter_00_dialogue_registry.tres"
const EXPECTED_BEAT_COUNT := 40
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
	"entity"
]
const REQUIRED_FLAGS := [
	"C01_CHARACTER_LIFE_BEGIN",
	"OPTIONAL_SKIPPABLE_SCENE",
	"EARLY_PLAYFUL_IRRITATION",
	"ORDINARY_CARE_ACTION",
	"ORDINARY_RECIPROCAL_CARE",
	"COMEDIC_REVERSAL",
	"EARLY_QUIET_FAMILIARITY",
	"C01_CHARACTER_LIFE_END",
	"NO_ESSENTIAL_PLOT_DELIVERY",
	"NO_ROMANCE_PROGRESSION",
	"NO_CARD_OR_PRIME_INFORMATION",
	"HANDOFF_C02_REMAINS_AVAILABLE"
]

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var failures: Array[String] = []
	var scene := load(SCENE_PATH) as DiyseDialogueSceneDefinition
	var registry := load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry
	if scene == null:
		failures.append("Could not load C01 production scene Resource")
		_finish(failures)
		return
	if registry == null:
		failures.append("Could not load Chapter 0 dialogue registry")
		_finish(failures)
		return

	for failure in scene.validate_schema(registry):
		failures.append("Schema: %s" % failure)

	if scene.scene_id != "C01": failures.append("C01 scene_id changed")
	if scene.chapter_id != "chapter_00": failures.append("C01 must remain in chapter_00")
	if scene.scene_kind != "character_life": failures.append("C01 must remain character_life")
	if scene.location_id != "LOC_BORDERLANDS_FIELD_TRIAGE_CAMP": failures.append("C01 location changed")
	if scene.trigger_id != "trigger.chapter_00.c01.after_s006": failures.append("C01 must remain available only after S006")
	if scene.completion_flag != "scene.c01.complete": failures.append("C01 completion flag changed")
	if scene.participants.size() != 2 or scene.participants[0] != "cyanis" or scene.participants[1] != "ilyra": failures.append("C01 participants must remain Cyanis and Ilyra only")
	if scene.beats.size() != EXPECTED_BEAT_COUNT:
		failures.append("C01 beat count changed: expected %d, got %d" % [EXPECTED_BEAT_COUNT, scene.beats.size()])

	var combined_spoken := ""
	var seen_flags: Dictionary = {}
	var cyanis_lines := 0
	var ilyra_lines := 0
	for i in range(scene.beats.size()):
		var beat: Dictionary = scene.beats[i]
		var expected_id := "C01_B%03d" % (i + 1)
		if str(beat.get("beat_id", "")) != expected_id:
			failures.append("C01 beat %d must use stable ID %s" % [i + 1, expected_id])
		var speaker := str(beat.get("speaker_id", ""))
		if not speaker.is_empty() and speaker not in ALLOWED_SPEAKERS:
			failures.append("C01 introduces unapproved speaker: %s" % speaker)
		if speaker == "cyanis": cyanis_lines += 1
		if speaker == "ilyra": ilyra_lines += 1
		var text := str(beat.get("text", ""))
		combined_spoken += " " + text.to_lower()
		if "res://" in text: failures.append("Raw asset path leaked into C01 spoken dialogue")
		var left = beat.get("left", {})
		var right = beat.get("right", {})
		if not (left is Dictionary) or not left.is_empty(): failures.append("C01 must not use a proof portrait in left slot at %s" % expected_id)
		if not (right is Dictionary) or not right.is_empty(): failures.append("C01 must not use a proof portrait in right slot at %s" % expected_id)
		var cues = beat.get("cues", {})
		if cues is Dictionary:
			var flags = cues.get("implementation_flags", [])
			if flags is Array:
				for flag in flags:
					seen_flags[str(flag)] = true

	if cyanis_lines < 10 or ilyra_lines < 10:
		failures.append("C01 must remain a balanced two-character conversation")
	for term in FORBIDDEN_SPOKEN_TERMS:
		if term in combined_spoken:
			failures.append("C01 carries forbidden plot/lore terminology in spoken dialogue: %s" % term)
	for phrase in [
		"you're too close to the fire.",
		"those can both be true.",
		"did you just move my seat?",
		"very localized ground.",
		"they'll be drier than if they're on fire.",
		"if this burns me, i will be difficult about it.",
		"your glove is smoking.",
		"this proves nothing.",
		"no, you didn't."
	]:
		if phrase not in combined_spoken:
			failures.append("C01 lost required playful/ordinary-care beat: %s" % phrase)
	for required_flag in REQUIRED_FLAGS:
		if not seen_flags.has(required_flag):
			failures.append("C01 missing required character-life boundary evidence: %s" % required_flag)

	var runner_beats := scene.to_runner_beats(registry)
	if runner_beats.size() != scene.beats.size():
		failures.append("C01 did not adapt one-for-one into generic runner beats")
	for runner_beat in runner_beats:
		if str(runner_beat.get("left_portrait", "")) != "" or str(runner_beat.get("right_portrait", "")) != "":
			failures.append("C01 unexpectedly resolved a proof/temporary portrait asset")
			break

	_finish(failures)

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Diyse Step 7C C01 character-life, playful-irritation, ordinary-care, no-plot-delivery, and runner-adaptation validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
