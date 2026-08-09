extends SceneTree

const SCENE_PATH := "res://game/content/dialogue/chapter_00/S001.tres"
const REGISTRY_PATH := "res://game/content/dialogue/chapter_00/chapter_00_dialogue_registry.tres"
const EXPECTED_BEAT_COUNT := 28
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

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var failures: Array[String] = []
	var scene := load(SCENE_PATH) as DiyseDialogueSceneDefinition
	var registry := load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry

	if scene == null:
		failures.append("Could not load S001 production scene Resource")
		_finish(failures)
		return
	if registry == null:
		failures.append("Could not load Chapter 0 production dialogue registry")
		_finish(failures)
		return

	for failure in scene.validate_schema(registry):
		failures.append("Schema: %s" % failure)

	if scene.scene_id != "S001":
		failures.append("S001 scene_id changed: %s" % scene.scene_id)
	if scene.chapter_id != "chapter_00":
		failures.append("S001 must remain in chapter_00")
	if scene.scene_kind != "mandatory":
		failures.append("S001 must remain a mandatory scene")
	if scene.location_id != "LOC_BORDERLANDS_CONVOY_ROAD":
		failures.append("S001 must remain on the approved Convoy Road location")
	if scene.trigger_id != "trigger.chapter_00.s001":
		failures.append("S001 trigger ID changed")
	if scene.completion_flag != "scene.s001.complete":
		failures.append("S001 completion flag changed")

	if scene.participants.size() != 2:
		failures.append("S001 should contain only Cyanis and the approved convoy superior officer as speaking participants")
	if "cyanis" not in scene.participants:
		failures.append("S001 is missing Cyanis")
	if "convoy_superior_officer" not in scene.participants:
		failures.append("S001 is missing the convoy superior officer")
	if "ilyra" in scene.participants:
		failures.append("Ilyra must not enter S001; her Chapter 0 arrival belongs to S004")

	if not registry.has_character("cyanis"):
		failures.append("Chapter 0 registry is missing Cyanis")
	if not registry.has_character("convoy_superior_officer"):
		failures.append("Chapter 0 registry is missing convoy_superior_officer")
	if registry.display_name("cyanis") != "Cyanis":
		failures.append("Cyanis display name changed unexpectedly")
	if registry.display_name("convoy_superior_officer") != "Convoy Officer":
		failures.append("Convoy officer display name changed unexpectedly")

	if scene.beats.size() != EXPECTED_BEAT_COUNT:
		failures.append("S001 beat count changed: expected %d, got %d" % [EXPECTED_BEAT_COUNT, scene.beats.size()])

	var combined_spoken_text := ""
	for i in range(scene.beats.size()):
		var beat: Dictionary = scene.beats[i]
		var expected_id := "S001_B%03d" % (i + 1)
		if str(beat.get("beat_id", "")) != expected_id:
			failures.append("S001 beat %d must use stable ID %s" % [i + 1, expected_id])
		var speaker_id := str(beat.get("speaker_id", ""))
		if not speaker_id.is_empty() and speaker_id not in ["cyanis", "convoy_superior_officer"]:
			failures.append("S001 introduces an unapproved speaking participant: %s" % speaker_id)
		var left = beat.get("left", {})
		var right = beat.get("right", {})
		if not (left is Dictionary) or not left.is_empty():
			failures.append("S001 currently uses in-world staging and must not substitute a proof portrait in left slot at %s" % expected_id)
		if not (right is Dictionary) or not right.is_empty():
			failures.append("S001 currently uses in-world staging and must not substitute a proof portrait in right slot at %s" % expected_id)
		var text := str(beat.get("text", ""))
		combined_spoken_text += " " + text.to_lower()
		if "res://" in text:
			failures.append("Raw asset path leaked into spoken text at %s" % expected_id)

	for term in FORBIDDEN_SPOKEN_BOUNDARY_TERMS:
		if term in combined_spoken_text:
			failures.append("S001 crosses a protected later-scene boundary in spoken dialogue: %s" % term)

	var final_beat: Dictionary = scene.beats[-1] if not scene.beats.is_empty() else {}
	var final_cues = final_beat.get("cues", {})
	if not (final_cues is Dictionary):
		failures.append("S001 final beat cues are invalid")
	else:
		var flags = final_cues.get("implementation_flags", [])
		if not (flags is Array) or "HANDOFF_TO_COMBAT" not in flags:
			failures.append("S001 must end with a combat handoff flag")
		if not (flags is Array) or "COMMIT_S001_ONLY_AFTER_REQUIRED_GAMEPLAY_HANDOFF" not in flags:
			failures.append("S001 completion must wait for its required gameplay handoff")

	var runner_beats := scene.to_runner_beats(registry)
	if runner_beats.size() != scene.beats.size():
		failures.append("S001 did not adapt one-for-one into generic runner beats")
	for runner_beat in runner_beats:
		if str(runner_beat.get("left_portrait", "")) != "" or str(runner_beat.get("right_portrait", "")) != "":
			failures.append("S001 unexpectedly resolved a proof/temporary portrait asset")
			break

	_finish(failures)

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Diyse Step 7C S001 Opening schema, scene-boundary, and runner-adaptation validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
