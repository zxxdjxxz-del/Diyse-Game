extends SceneTree

const SCENE_PATH := "res://game/content/dialogue/chapter_00/S006.tres"
const REGISTRY_PATH := "res://game/content/dialogue/chapter_00/chapter_00_dialogue_registry.tres"
const EXPECTED_BEAT_COUNT := 60
const ALLOWED_SPEAKERS := ["cyanis", "ilyra", "convoy_superior_officer", "wounded_convoy_escort"]
const FORBIDDEN_SPOKEN_TERMS := [
	"first champion",
	"first mercy",
	"prime",
	"chosen one",
	"chosen-one",
	"prophecy",
	"bearer",
	"destiny",
	"join my party",
	"join the party"
]
const REQUIRED_FLAGS := [
	"SURVIVORS_STILL_MISSING",
	"SURVIVOR_COUNT_UNCERTAIN",
	"SURVIVOR_SWEEP_AUTHORIZED",
	"NO_PURSUIT_FINALIZED",
	"CARD_STAYS_SEALED",
	"ROUTE_BRACKENWALL_ESTABLISHED",
	"DAMAGED_CARD_UNANSWERED_RISK",
	"ILYRA_EXPERTISE_MATERIALLY_CHANGES_RECOVERY",
	"ILYRA_PERMANENT_RECRUITMENT_DECISION",
	"SURVIVOR_RECOVERY_UNFINISHED",
	"NO_ROMANCE_RECRUITMENT",
	"NO_DESTINY_RECRUITMENT",
	"SHARED_COMMITMENT_WORK_NOT_FINISHED",
	"ROSTER_ADD_ILYRA_PERMANENT",
	"PARTY_STATE_CYANIS_ILYRA",
	"STORY_CHAPTER_00_COMPLETE",
	"ROUTE_BRACKENWALL_UNLOCKED",
	"CARD_REMAINS_UNIDENTIFIED",
	"FIRST_MERCY_NO_RESPONSE_CH00",
	"UNLOCK_C01_THE_FIRE_IS_TOO_CLOSE",
	"UNLOCK_C02_FOOD_AFTER_TRIAGE",
	"DO_NOT_AUTO_SKIP_CHARACTER_LIFE_SCENES"
]

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var failures: Array[String] = []
	var scene := load(SCENE_PATH) as DiyseDialogueSceneDefinition
	var registry := load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry
	if scene == null:
		failures.append("Could not load S006 production scene Resource")
		_finish(failures)
		return
	if registry == null:
		failures.append("Could not load Chapter 0 production dialogue registry")
		_finish(failures)
		return

	for failure in scene.validate_schema(registry):
		failures.append("Schema: %s" % failure)

	if scene.scene_id != "S006": failures.append("S006 scene_id changed")
	if scene.chapter_id != "chapter_00": failures.append("S006 must remain in chapter_00")
	if scene.scene_kind != "mandatory": failures.append("S006 must remain mandatory")
	if scene.location_id != "LOC_BORDERLANDS_FIELD_TRIAGE_CAMP": failures.append("S006 location changed")
	if scene.trigger_id != "trigger.chapter_00.s006": failures.append("S006 trigger ID changed")
	if scene.completion_flag != "scene.s006.complete": failures.append("S006 completion flag changed")

	for required in ["cyanis", "ilyra", "convoy_superior_officer"]:
		if required not in scene.participants:
			failures.append("S006 missing required participant: %s" % required)
	for participant in scene.participants:
		if participant not in ALLOWED_SPEAKERS:
			failures.append("S006 introduces unapproved participant: %s" % participant)

	if scene.beats.size() != EXPECTED_BEAT_COUNT:
		failures.append("S006 beat count changed: expected %d, got %d" % [EXPECTED_BEAT_COUNT, scene.beats.size()])

	var combined_spoken := ""
	var seen_flags: Dictionary = {}
	for i in range(scene.beats.size()):
		var beat: Dictionary = scene.beats[i]
		var expected_id := "S006_B%03d" % (i + 1)
		if str(beat.get("beat_id", "")) != expected_id:
			failures.append("S006 beat %d must use stable ID %s" % [i + 1, expected_id])
		var speaker := str(beat.get("speaker_id", ""))
		if not speaker.is_empty() and speaker not in ALLOWED_SPEAKERS:
			failures.append("S006 introduces unapproved speaking participant: %s" % speaker)
		var left = beat.get("left", {})
		var right = beat.get("right", {})
		if not (left is Dictionary) or not left.is_empty(): failures.append("S006 must not substitute proof portrait in left slot at %s" % expected_id)
		if not (right is Dictionary) or not right.is_empty(): failures.append("S006 must not substitute proof portrait in right slot at %s" % expected_id)
		var text := str(beat.get("text", ""))
		combined_spoken += " " + text.to_lower()
		if "res://" in text: failures.append("Raw asset path leaked into S006 spoken text")
		var cues = beat.get("cues", {})
		if cues is Dictionary:
			var flags = cues.get("implementation_flags", [])
			if flags is Array:
				for flag in flags:
					seen_flags[str(flag)] = true

	for term in FORBIDDEN_SPOKEN_TERMS:
		if term in combined_spoken:
			failures.append("S006 exposes forbidden recruitment/later terminology in spoken dialogue: %s" % term)

	for phrase in [
		"then we search by people, not numbers.",
		"if someone's pinned, first light is late.",
		"if someone's bleeding, it's later.",
		"it goes to brackenwall sealed. their artifact protocol can decide what happens next.",
		"i'm staying with the recovery.",
		"the convoy still has missing people.",
		"i'm not doing it for you.",
		"there are still people missing.",
		"then we find them.",
		"your hand.",
		"you can wait. don't mistake that for fine.",
		"that was my line.",
		"not what i asked.",
		"i'll manage the sweep. then i sit."
	]:
		if phrase not in combined_spoken:
			failures.append("S006 lost required aftermath/recruitment/relationship beat: %s" % phrase)

	for required_flag in REQUIRED_FLAGS:
		if not seen_flags.has(required_flag):
			failures.append("S006 missing required aftermath/handoff evidence: %s" % required_flag)

	var final_beat: Dictionary = scene.beats[-1] if not scene.beats.is_empty() else {}
	var final_cues = final_beat.get("cues", {})
	if not (final_cues is Dictionary):
		failures.append("S006 final cue dictionary invalid")
	else:
		var final_flags = final_cues.get("implementation_flags", [])
		for required_final in [
			"ROSTER_ADD_ILYRA_PERMANENT",
			"STORY_CHAPTER_00_COMPLETE",
			"ROUTE_BRACKENWALL_UNLOCKED",
			"UNLOCK_C01_THE_FIRE_IS_TOO_CLOSE",
			"UNLOCK_C02_FOOD_AFTER_TRIAGE",
			"DO_NOT_AUTO_SKIP_CHARACTER_LIFE_SCENES"
		]:
			if not (final_flags is Array) or required_final not in final_flags:
				failures.append("S006 final beat missing durable handoff: %s" % required_final)

	var runner_beats := scene.to_runner_beats(registry)
	if runner_beats.size() != scene.beats.size():
		failures.append("S006 did not adapt one-for-one into generic runner beats")
	for runner_beat in runner_beats:
		if str(runner_beat.get("left_portrait", "")) != "" or str(runner_beat.get("right_portrait", "")) != "":
			failures.append("S006 unexpectedly resolved a proof/temporary portrait asset")
			break

	_finish(failures)

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Diyse Step 7C S006 aftermath, Ilyra recruitment, Chapter 0 completion, Brackenwall route, Character-Life unlock, and runner-adaptation validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
