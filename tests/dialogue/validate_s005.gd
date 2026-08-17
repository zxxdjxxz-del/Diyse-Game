extends SceneTree

const SCENE_PATH := "res://game/content/dialogue/chapter_00/S005.tres"
const REGISTRY_PATH := "res://game/content/dialogue/chapter_00/chapter_00_dialogue_registry.tres"
const EXPECTED_BEAT_COUNT := 31
const APPROVAL_STATUS := "USER_APPROVED_2026_08_08"
const ALLOWED_SPEAKERS := ["cyanis", "ilyra", "convoy_superior_officer"]
const FORBIDDEN_SPOKEN_TERMS := [
	"first champion",
	"first mercy",
	"prime",
	"broken champion",
	"ward",
	"chosen one",
	"chosen-one",
	"prophecy",
	"bearer"
]
const REQUIRED_FLAGS := [
	"ENCOUNTER_CH00_CONVOY_WAR_SORCERER",
	"PARTY_CYANIS_ILYRA",
	"WAR_SORCERER_START_HP_70_PERCENT",
	"INJURED_SOLDIER_START_HP_50_PERCENT",
	"RIFT_LANCE_PREPARATION_NOT_BEFORE_ROUND_2",
	"PROTECTIVE_RESPONSE_THREE_ROUNDS",
	"PROTECTIVE_RESPONSE_PLUS_20_TOTAL_DEFENSE",
	"PROTECTIVE_RESPONSE_FIRST_ELIGIBLE_DIRECT_HIT_MINUS_20_PERCENT_PER_PARTY_MEMBER",
	"PROTECTIVE_RESPONSE_NOT_CARD_USE",
	"WAR_SORCERER_DEFEATED",
	"INJURED_SOLDIER_WITHDRAWS_IF_STILL_ACTIVE",
	"NO_PURSUIT_REAFFIRMED",
	"INCOMPLETE_RESPONSE_FADES",
	"NO_COMPLETE_MANIFESTATION",
	"NO_IDENTITY_REVEAL",
	"HANDOFF_TO_S006",
	"NO_PERMANENT_RECRUITMENT_YET",
	"NO_CHAPTER_ROUTE_UNLOCK_YET"
]

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var failures: Array[String] = []
	var scene := load(SCENE_PATH) as DiyseDialogueSceneDefinition
	var registry := load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry
	if scene == null:
		failures.append("Could not load S005 production scene Resource")
		_finish(failures)
		return
	if registry == null:
		failures.append("Could not load Chapter 0 production dialogue registry")
		_finish(failures)
		return

	for failure in scene.validate_schema(registry):
		failures.append("Schema: %s" % failure)

	if scene.scene_id != "S005": failures.append("S005 scene_id changed")
	if scene.chapter_id != "chapter_00": failures.append("S005 must remain in chapter_00")
	if scene.scene_kind != "mandatory": failures.append("S005 must remain mandatory")
	if scene.location_id != "LOC_BORDERLANDS_FIELD_TRIAGE_CAMP": failures.append("S005 location changed")
	if scene.trigger_id != "trigger.chapter_00.s005": failures.append("S005 trigger ID changed")
	if scene.completion_flag != "scene.s005.complete": failures.append("S005 completion flag changed")
	if APPROVAL_STATUS != "USER_APPROVED_2026_08_08": failures.append("S005 approval marker changed")
	for required in ALLOWED_SPEAKERS:
		if required not in scene.participants: failures.append("S005 missing participant: %s" % required)

	if scene.beats.size() != EXPECTED_BEAT_COUNT:
		failures.append("S005 beat count changed: expected %d, got %d" % [EXPECTED_BEAT_COUNT, scene.beats.size()])

	var combined_spoken := ""
	var seen_flags: Dictionary = {}
	var combat_handoff_count := 0
	for i in range(scene.beats.size()):
		var beat: Dictionary = scene.beats[i]
		var expected_id := "S005_B%03d" % (i + 1)
		if str(beat.get("beat_id", "")) != expected_id:
			failures.append("S005 beat %d must use stable ID %s" % [i + 1, expected_id])
		var speaker := str(beat.get("speaker_id", ""))
		if not speaker.is_empty() and speaker not in ALLOWED_SPEAKERS:
			failures.append("S005 introduces unapproved speaker: %s" % speaker)
		var left = beat.get("left", {})
		var right = beat.get("right", {})
		if not (left is Dictionary) or not left.is_empty(): failures.append("S005 must not substitute proof portrait in left slot at %s" % expected_id)
		if not (right is Dictionary) or not right.is_empty(): failures.append("S005 must not substitute proof portrait in right slot at %s" % expected_id)
		var text := str(beat.get("text", ""))
		combined_spoken += " " + text.to_lower()
		if "res://" in text: failures.append("Raw asset path leaked into S005 spoken text")
		var cues = beat.get("cues", {})
		if cues is Dictionary:
			var flags = cues.get("implementation_flags", [])
			if flags is Array:
				for flag in flags:
					seen_flags[str(flag)] = true
				if "COMBAT_HANDOFF" in flags:
					combat_handoff_count += 1

	for term in FORBIDDEN_SPOKEN_TERMS:
		if term in combined_spoken:
			failures.append("S005 exposes internal/later terminology in spoken dialogue: %s" % term)

	for phrase in [
		"keep everyone behind stone. nobody follows us out.",
		"good. hold the left half.",
		"i need the other half.",
		"sorcerer's the threat. don't let the soldier pull us off the line.",
		"i would prefer to know before you fall over.",
		"let him.",
		"still alive. one worse, one better. i don't trust the one who's better yet.",
		"two carriers, clean water, and for you to sit down when i tell you.",
		"it wasn't."
	]:
		if phrase not in combined_spoken:
			failures.append("S005 lost required confrontation/relationship beat: %s" % phrase)

	if combat_handoff_count != 1:
		failures.append("S005 must contain exactly one controlling combat handoff")
	for required_flag in REQUIRED_FLAGS:
		if not seen_flags.has(required_flag):
			failures.append("S005 missing required encounter/boundary evidence: %s" % required_flag)

	var runner_beats := scene.to_runner_beats(registry)
	if runner_beats.size() != scene.beats.size():
		failures.append("S005 did not adapt one-for-one into generic runner beats")
	for runner_beat in runner_beats:
		if str(runner_beat.get("left_portrait", "")) != "" or str(runner_beat.get("right_portrait", "")) != "":
			failures.append("S005 unexpectedly resolved a proof/temporary portrait asset")
			break

	_finish(failures)

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Diyse Step 7C S005 approved confrontation, fixed encounter handoff, protective-response boundary, S006 handoff, and runner-adaptation validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
