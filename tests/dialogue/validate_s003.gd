extends SceneTree

const SCENE_PATH := "res://game/content/dialogue/chapter_00/S003.tres"
const REGISTRY_PATH := "res://game/content/dialogue/chapter_00/chapter_00_dialogue_registry.tres"
const EXPECTED_BEAT_COUNT := 35
const ALLOWED_SPEAKERS := ["cyanis", "convoy_superior_officer"]
const FORBIDDEN_SPOKEN_BOUNDARY_TERMS := [
	"ilyra",
	"first champion",
	"prime",
	"prophecy",
	"bloodline",
	"chosen one",
	"chosen-one"
]
const REQUIRED_IMPLEMENTATION_FLAGS := [
	"FIELD_COUNT",
	"NATURAL_BATTLEFIELD_AWARENESS",
	"PURSUIT_RATIONALE",
	"PURSUIT_ORDER_GIVEN",
	"AUTHORED_PURSUIT_REFUSAL",
	"REFUSAL_REASON_EXPOSED_SURVIVORS",
	"REFUSAL_REASON_SPLIT_DEFENDERS",
	"BAIT_RISK_ARGUMENT",
	"S002_EVIDENCE_RECALLED",
	"REFUSAL_REASON_FIELD_AND_CARGO_CONTROL",
	"PROTECTIVE_TACTICAL_COURSE",
	"OFFICER_EVALUATES_EVIDENCE",
	"PURSUIT_ORDER_REVISED",
	"HANDOFF_TO_S004_FIELD_TRIAGE_CAMP",
	"COMMIT_S003_ONLY_AFTER_DECISION_EXECUTION"
]

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var failures: Array[String] = []
	var scene := load(SCENE_PATH) as DiyseDialogueSceneDefinition
	var registry := load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry

	if scene == null:
		failures.append("Could not load S003 production scene Resource")
		_finish(failures)
		return
	if registry == null:
		failures.append("Could not load Chapter 0 production dialogue registry")
		_finish(failures)
		return

	for failure in scene.validate_schema(registry):
		failures.append("Schema: %s" % failure)

	if scene.scene_id != "S003":
		failures.append("S003 scene_id changed: %s" % scene.scene_id)
	if scene.chapter_id != "chapter_00":
		failures.append("S003 must remain in chapter_00")
	if scene.scene_kind != "mandatory":
		failures.append("S003 must remain a mandatory scene")
	if scene.location_id != "LOC_BORDERLANDS_EVACUATION_RELAY":
		failures.append("S003 must remain at the approved Evacuation Relay location")
	if scene.trigger_id != "trigger.chapter_00.s003":
		failures.append("S003 trigger ID changed")
	if scene.completion_flag != "scene.s003.complete":
		failures.append("S003 completion flag changed")

	if scene.participants.size() != 2:
		failures.append("S003 should contain only Cyanis and the convoy superior officer as speaking participants")
	if "cyanis" not in scene.participants:
		failures.append("S003 is missing Cyanis")
	if "convoy_superior_officer" not in scene.participants:
		failures.append("S003 is missing the convoy superior officer")
	if "ilyra" in scene.participants:
		failures.append("Ilyra must not enter S003; her Chapter 0 arrival belongs to S004")
	for participant in scene.participants:
		if participant not in ALLOWED_SPEAKERS:
			failures.append("S003 introduces an unapproved participant: %s" % participant)

	for required_speaker in ALLOWED_SPEAKERS:
		if not registry.has_character(required_speaker):
			failures.append("Chapter 0 registry is missing S003 speaker: %s" % required_speaker)

	if scene.beats.size() != EXPECTED_BEAT_COUNT:
		failures.append("S003 beat count changed: expected %d, got %d" % [EXPECTED_BEAT_COUNT, scene.beats.size()])

	var combined_spoken_text := ""
	var seen_flags: Dictionary = {}
	for i in range(scene.beats.size()):
		var beat: Dictionary = scene.beats[i]
		var expected_id := "S003_B%03d" % (i + 1)
		if str(beat.get("beat_id", "")) != expected_id:
			failures.append("S003 beat %d must use stable ID %s" % [i + 1, expected_id])
		var speaker_id := str(beat.get("speaker_id", ""))
		if not speaker_id.is_empty() and speaker_id not in ALLOWED_SPEAKERS:
			failures.append("S003 introduces an unapproved speaking participant: %s" % speaker_id)
		var left = beat.get("left", {})
		var right = beat.get("right", {})
		if not (left is Dictionary) or not left.is_empty():
			failures.append("S003 currently uses in-world staging and must not substitute a proof portrait in left slot at %s" % expected_id)
		if not (right is Dictionary) or not right.is_empty():
			failures.append("S003 currently uses in-world staging and must not substitute a proof portrait in right slot at %s" % expected_id)
		var text := str(beat.get("text", ""))
		combined_spoken_text += " " + text.to_lower()
		if "res://" in text:
			failures.append("Raw asset path leaked into spoken text at %s" % expected_id)
		var cues = beat.get("cues", {})
		if cues is Dictionary:
			var flags = cues.get("implementation_flags", [])
			if flags is Array:
				for flag in flags:
					seen_flags[str(flag)] = true

	for term in FORBIDDEN_SPOKEN_BOUNDARY_TERMS:
		if term in combined_spoken_text:
			failures.append("S003 crosses a protected S004/later boundary in spoken dialogue: %s" % term)

	if "no, sir. we don't have the line for it." not in combined_spoken_text:
		failures.append("S003 must contain Cyanis's explicit authored pursuit refusal")
	if "wounded and civilians are still exposed" not in combined_spoken_text:
		failures.append("S003 must explicitly state the exposed wounded/civilian reason")
	if "split damaged defenders" not in combined_spoken_text:
		failures.append("S003 must explicitly state the divided-defender reason")
	if "wreckage and recovery wagon" not in combined_spoken_text or "surrender control of the whole field" not in combined_spoken_text:
		failures.append("S003 must explicitly state the wreckage/cargo/field-control reason")
	if "opened one direction for us and closed the rest" not in combined_spoken_text:
		failures.append("S003 must ground the decision in the suspicious S002 north-cut evidence")
	if "relay first" not in combined_spoken_text or "reform on the wagon" not in combined_spoken_text:
		failures.append("S003 must end with the ranking officer issuing the protective revised order")
	if "yes, sir" not in combined_spoken_text:
		failures.append("S003 must preserve Cyanis's acknowledgment of legitimate revised command authority")

	for required_flag in REQUIRED_IMPLEMENTATION_FLAGS:
		if not seen_flags.has(required_flag):
			failures.append("S003 is missing required authored implementation evidence: %s" % required_flag)

	var final_beat: Dictionary = scene.beats[-1] if not scene.beats.is_empty() else {}
	var final_cues = final_beat.get("cues", {})
	if not (final_cues is Dictionary):
		failures.append("S003 final beat cues are invalid")
	else:
		var flags = final_cues.get("implementation_flags", [])
		if not (flags is Array) or "HANDOFF_TO_S004_FIELD_TRIAGE_CAMP" not in flags:
			failures.append("S003 must hand off toward S004 at the Field Triage Camp")
		if not (flags is Array) or "COMMIT_S003_ONLY_AFTER_DECISION_EXECUTION" not in flags:
			failures.append("S003 completion must wait until the revised protective course is executing")

	var runner_beats := scene.to_runner_beats(registry)
	if runner_beats.size() != scene.beats.size():
		failures.append("S003 did not adapt one-for-one into generic runner beats")
	for runner_beat in runner_beats:
		if str(runner_beat.get("left_portrait", "")) != "" or str(runner_beat.get("right_portrait", "")) != "":
			failures.append("S003 unexpectedly resolved a proof/temporary portrait asset")
			break

	_finish(failures)

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Diyse Step 7C S003 Evacuation Relay decision, authority-boundary, and runner-adaptation validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
