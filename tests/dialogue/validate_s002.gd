extends SceneTree

const SCENE_PATH := "res://game/content/dialogue/chapter_00/S002.tres"
const REGISTRY_PATH := "res://game/content/dialogue/chapter_00/chapter_00_dialogue_registry.tres"
const EXPECTED_BEAT_COUNT := 49
const ALLOWED_SPEAKERS := ["cyanis", "convoy_superior_officer", "wounded_convoy_escort", "civilian_traveler"]
const FORBIDDEN_SPOKEN_BOUNDARY_TERMS := [
	"ilyra",
	"first champion",
	"prime",
	"pursue",
	"pursuit",
	"prophecy",
	"bloodline",
	"chosen one",
	"chosen-one"
]
const REQUIRED_IMPLEMENTATION_FLAGS := [
	"SURVIVOR_ROLE_ASSIGNMENT",
	"SURVIVOR_ROUTE_READ",
	"UNSTABLE_WRECKAGE_READ",
	"ENEMY_PRESSURE_READ",
	"HANDOFF_TO_CONVOY_RIFT_HOUND_ENCOUNTER",
	"RESUME_AFTER_WRECK_FIELD_COMBAT",
	"BAIT_PATTERN_EVIDENCE",
	"HANDOFF_TO_S003_EVACUATION_RELAY",
	"COMMIT_S002_ONLY_AFTER_REQUIRED_GAMEPLAY_HANDOFF"
]

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var failures: Array[String] = []
	var scene := load(SCENE_PATH) as DiyseDialogueSceneDefinition
	var registry := load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry

	if scene == null:
		failures.append("Could not load S002 production scene Resource")
		_finish(failures)
		return
	if registry == null:
		failures.append("Could not load Chapter 0 production dialogue registry")
		_finish(failures)
		return

	for failure in scene.validate_schema(registry):
		failures.append("Schema: %s" % failure)

	if scene.scene_id != "S002":
		failures.append("S002 scene_id changed: %s" % scene.scene_id)
	if scene.chapter_id != "chapter_00":
		failures.append("S002 must remain in chapter_00")
	if scene.scene_kind != "mandatory":
		failures.append("S002 must remain a mandatory scene")
	if scene.location_id != "LOC_BORDERLANDS_WRECK_FIELD":
		failures.append("S002 must remain at the approved Wreck Field location")
	if scene.trigger_id != "trigger.chapter_00.s002":
		failures.append("S002 trigger ID changed")
	if scene.completion_flag != "scene.s002.complete":
		failures.append("S002 completion flag changed")

	if "cyanis" not in scene.participants:
		failures.append("S002 is missing Cyanis")
	if "ilyra" in scene.participants:
		failures.append("Ilyra must not enter S002; her Chapter 0 arrival belongs to S004")
	for participant in scene.participants:
		if participant not in ALLOWED_SPEAKERS:
			failures.append("S002 introduces an unapproved participant: %s" % participant)

	for required_speaker in ALLOWED_SPEAKERS:
		if not registry.has_character(required_speaker):
			failures.append("Chapter 0 registry is missing S002 speaker: %s" % required_speaker)
	if registry.display_name("cyanis") != "Cyanis":
		failures.append("Cyanis display name changed unexpectedly")
	if registry.display_name("convoy_superior_officer") != "Convoy Officer":
		failures.append("Convoy officer display name changed unexpectedly")
	if registry.display_name("wounded_convoy_escort") != "Wounded Escort":
		failures.append("Wounded escort display name changed unexpectedly")
	if registry.display_name("civilian_traveler") != "Civilian Traveler":
		failures.append("Civilian traveler display name changed unexpectedly")

	if scene.beats.size() != EXPECTED_BEAT_COUNT:
		failures.append("S002 beat count changed: expected %d, got %d" % [EXPECTED_BEAT_COUNT, scene.beats.size()])

	var combined_spoken_text := ""
	var seen_flags: Dictionary = {}
	var cyan_is_speaker := false
	var survivor_role_assignment_count := 0
	for i in range(scene.beats.size()):
		var beat: Dictionary = scene.beats[i]
		var expected_id := "S002_B%03d" % (i + 1)
		if str(beat.get("beat_id", "")) != expected_id:
			failures.append("S002 beat %d must use stable ID %s" % [i + 1, expected_id])
		var speaker_id := str(beat.get("speaker_id", ""))
		if not speaker_id.is_empty() and speaker_id not in ALLOWED_SPEAKERS:
			failures.append("S002 introduces an unapproved speaking participant: %s" % speaker_id)
		if speaker_id == "cyanis":
			cyan_is_speaker = true
		var left = beat.get("left", {})
		var right = beat.get("right", {})
		if not (left is Dictionary) or not left.is_empty():
			failures.append("S002 currently uses in-world staging and must not substitute a proof portrait in left slot at %s" % expected_id)
		if not (right is Dictionary) or not right.is_empty():
			failures.append("S002 currently uses in-world staging and must not substitute a proof portrait in right slot at %s" % expected_id)
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
					if str(flag) == "SURVIVOR_ROLE_ASSIGNMENT":
						survivor_role_assignment_count += 1

	if not cyan_is_speaker:
		failures.append("S002 must retain Cyanis as the active speaking viewpoint")
	if survivor_role_assignment_count < 2:
		failures.append("S002 must visibly give more than one survivor a practical role based on current capacity")

	for term in FORBIDDEN_SPOKEN_BOUNDARY_TERMS:
		if term in combined_spoken_text:
			failures.append("S002 crosses a protected later-scene boundary in spoken dialogue: %s" % term)

	for required_flag in REQUIRED_IMPLEMENTATION_FLAGS:
		if not seen_flags.has(required_flag):
			failures.append("S002 is missing required authored implementation evidence: %s" % required_flag)

	var final_beat: Dictionary = scene.beats[-1] if not scene.beats.is_empty() else {}
	var final_cues = final_beat.get("cues", {})
	if not (final_cues is Dictionary):
		failures.append("S002 final beat cues are invalid")
	else:
		var flags = final_cues.get("implementation_flags", [])
		if not (flags is Array) or "HANDOFF_TO_S003_EVACUATION_RELAY" not in flags:
			failures.append("S002 must end by handing off toward S003 at the Evacuation Relay")
		if not (flags is Array) or "COMMIT_S002_ONLY_AFTER_REQUIRED_GAMEPLAY_HANDOFF" not in flags:
			failures.append("S002 completion must wait for its required gameplay handoff")

	var runner_beats := scene.to_runner_beats(registry)
	if runner_beats.size() != scene.beats.size():
		failures.append("S002 did not adapt one-for-one into generic runner beats")
	for runner_beat in runner_beats:
		if str(runner_beat.get("left_portrait", "")) != "" or str(runner_beat.get("right_portrait", "")) != "":
			failures.append("S002 unexpectedly resolved a proof/temporary portrait asset")
			break

	_finish(failures)

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Diyse Step 7C S002 Wreck Field schema, scene-boundary, gameplay-handoff, and runner-adaptation validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
