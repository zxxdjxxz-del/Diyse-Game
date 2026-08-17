extends SceneTree

const SCENE_PATH := "res://game/content/dialogue/chapter_00/S004.tres"
const REGISTRY_PATH := "res://game/content/dialogue/chapter_00/chapter_00_dialogue_registry.tres"
const EXPECTED_BEAT_COUNT := 57
const ALLOWED_SPEAKERS := ["cyanis", "ilyra", "convoy_superior_officer", "wounded_convoy_escort", "civilian_traveler"]
const FORBIDDEN_SPOKEN_TERMS := [
	"first champion",
	"first mercy",
	"prime",
	"chosen one",
	"chosen-one",
	"prophecy",
	"bearer",
	"we were chosen"
]
const REQUIRED_FLAGS := [
	"ILYRA_FIRST_ENTRY",
	"ILYRA_INDEPENDENT_MEDICAL_AUTHORITY",
	"ILYRA_MEDICAL_JURISDICTION",
	"MUTUAL_JURISDICTION_ESTABLISHED",
	"TRIAGE_CLASSIFICATION",
	"SURVIVOR_ROLE_ASSIGNMENT",
	"INCOMPLETE_CARD_RESPONSE_BEGINS",
	"FRAGMENTARY_GREEN_GOLD_GEOMETRY",
	"WEAK_POSITIONS_STABILIZED",
	"EVACUATION_TIME_CREATED",
	"SLIGHT_FIELD_INFORMATION_EXPANSION",
	"NO_ENEMY_DAMAGE_FROM_RESPONSE",
	"NO_INVULNERABILITY",
	"ILYRA_RECOGNIZES_UNSTABLE_PHYSICAL_MAGICAL_CONDITION",
	"ILYRA_STABILIZES_INCOMPLETE_CONNECTION",
	"ILYRA_CHALLENGES_CYANIS_SELF_NEGLECT",
	"ESTABLISH_INCOMPLETE_PROTECTIVE_RESPONSE",
	"INCOMPLETE_PROTECTIVE_RESPONSE_THREE_ROUNDS",
	"NO_SELECTABLE_CARD_COMMAND",
	"PROTECTIVE_RESPONSE_NOT_CARD_USE",
	"NO_COMPLETE_MANIFESTATION",
	"NO_IDENTITY_REVEAL",
	"ILYRA_NOT_YET_PERMANENT_ROSTER_COMMIT",
	"HANDOFF_TO_S005_CONFRONTATION",
	"COMMIT_S004_ONLY_AFTER_S005_HANDOFF_READY"
]

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var failures: Array[String] = []
	var scene := load(SCENE_PATH) as DiyseDialogueSceneDefinition
	var registry := load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry

	if scene == null:
		failures.append("Could not load S004 production scene Resource")
		_finish(failures)
		return
	if registry == null:
		failures.append("Could not load Chapter 0 production dialogue registry")
		_finish(failures)
		return

	for failure in scene.validate_schema(registry):
		failures.append("Schema: %s" % failure)

	if scene.scene_id != "S004":
		failures.append("S004 scene_id changed: %s" % scene.scene_id)
	if scene.chapter_id != "chapter_00":
		failures.append("S004 must remain in chapter_00")
	if scene.scene_kind != "mandatory":
		failures.append("S004 must remain a mandatory scene")
	if scene.location_id != "LOC_BORDERLANDS_FIELD_TRIAGE_CAMP":
		failures.append("S004 must remain at the approved Field Triage Camp location")
	if scene.trigger_id != "trigger.chapter_00.s004":
		failures.append("S004 trigger ID changed")
	if scene.completion_flag != "scene.s004.complete":
		failures.append("S004 completion flag changed")

	for required_participant in ["cyanis", "ilyra", "convoy_superior_officer"]:
		if required_participant not in scene.participants:
			failures.append("S004 is missing required participant: %s" % required_participant)
	for participant in scene.participants:
		if participant not in ALLOWED_SPEAKERS:
			failures.append("S004 introduces an unapproved participant: %s" % participant)

	if not registry.has_character("ilyra"):
		failures.append("Chapter 0 registry must include Ilyra for S004")
	elif registry.display_name("ilyra") != "Ilyra":
		failures.append("Ilyra display name changed unexpectedly")
	for speaker_id in ALLOWED_SPEAKERS:
		if not registry.has_character(speaker_id):
			failures.append("Chapter 0 registry is missing allowed S004 speaker: %s" % speaker_id)

	if scene.beats.size() != EXPECTED_BEAT_COUNT:
		failures.append("S004 beat count changed: expected %d, got %d" % [EXPECTED_BEAT_COUNT, scene.beats.size()])

	var combined_spoken_text := ""
	var seen_flags: Dictionary = {}
	var first_ilyra_spoken_index := -1
	var protected_line_count := 0
	var cyanis_lines := 0
	var ilyra_lines := 0
	for i in range(scene.beats.size()):
		var beat: Dictionary = scene.beats[i]
		var expected_id := "S004_B%03d" % (i + 1)
		if str(beat.get("beat_id", "")) != expected_id:
			failures.append("S004 beat %d must use stable ID %s" % [i + 1, expected_id])
		var speaker_id := str(beat.get("speaker_id", ""))
		if not speaker_id.is_empty() and speaker_id not in ALLOWED_SPEAKERS:
			failures.append("S004 introduces an unapproved speaking participant: %s" % speaker_id)
		if speaker_id == "ilyra":
			ilyra_lines += 1
			if first_ilyra_spoken_index == -1:
				first_ilyra_spoken_index = i
		if speaker_id == "cyanis":
			cyanis_lines += 1
		var left = beat.get("left", {})
		var right = beat.get("right", {})
		if not (left is Dictionary) or not left.is_empty():
			failures.append("S004 currently uses in-world staging and must not substitute a proof portrait in left slot at %s" % expected_id)
		if not (right is Dictionary) or not right.is_empty():
			failures.append("S004 currently uses in-world staging and must not substitute a proof portrait in right slot at %s" % expected_id)
		var text := str(beat.get("text", ""))
		combined_spoken_text += " " + text.to_lower()
		if text == "The line is holding. Move the wounded now.":
			protected_line_count += 1
		if "res://" in text:
			failures.append("Raw asset path leaked into spoken text at %s" % expected_id)
		var cues = beat.get("cues", {})
		if cues is Dictionary:
			var flags = cues.get("implementation_flags", [])
			if flags is Array:
				for flag in flags:
					seen_flags[str(flag)] = true

	if first_ilyra_spoken_index != 1:
		failures.append("Ilyra's first spoken entry must remain the immediate triage command at S004_B002")
	if cyanis_lines < 8:
		failures.append("S004 must retain Cyanis as a substantive continuing viewpoint")
	if ilyra_lines < 12:
		failures.append("S004 must establish Ilyra as a substantive independent authority, not a cameo")
	if protected_line_count != 1:
		failures.append("S004 must contain the protected Cyanis line exactly once")

	for term in FORBIDDEN_SPOKEN_TERMS:
		if term in combined_spoken_text:
			failures.append("S004 reveals protected later knowledge in spoken dialogue: %s" % term)

	for required_phrase in [
		"then move the crates. she doesn't move.",
		"what do you need?",
		"whatever it is, it's running through you.",
		"i can keep it from getting worse. i can't tell you what it is.",
		"useful enough. different standard.",
		"war-sorcerer at the east cut. one soldier with him.",
		"and they need the treatment space to remain ours."
	]:
		if required_phrase not in combined_spoken_text:
			failures.append("S004 lost required professional/revelation beat: %s" % required_phrase)

	for required_flag in REQUIRED_FLAGS:
		if not seen_flags.has(required_flag):
			failures.append("S004 is missing required authored implementation evidence: %s" % required_flag)

	var final_beat: Dictionary = scene.beats[-1] if not scene.beats.is_empty() else {}
	var final_cues = final_beat.get("cues", {})
	if not (final_cues is Dictionary):
		failures.append("S004 final beat cues are invalid")
	else:
		var final_flags = final_cues.get("implementation_flags", [])
		if not (final_flags is Array) or "HANDOFF_TO_S005_CONFRONTATION" not in final_flags:
			failures.append("S004 must end by handing off to S005 confrontation")
		if not (final_flags is Array) or "ESTABLISH_INCOMPLETE_PROTECTIVE_RESPONSE" not in final_flags:
			failures.append("S004 must establish the incomplete protective response before S005")
		if not (final_flags is Array) or "ILYRA_NOT_YET_PERMANENT_ROSTER_COMMIT" not in final_flags:
			failures.append("S004 must not consume S006 permanent recruitment closure")

	var runner_beats := scene.to_runner_beats(registry)
	if runner_beats.size() != scene.beats.size():
		failures.append("S004 did not adapt one-for-one into generic runner beats")
	for runner_beat in runner_beats:
		if str(runner_beat.get("left_portrait", "")) != "" or str(runner_beat.get("right_portrait", "")) != "":
			failures.append("S004 unexpectedly resolved a proof/temporary portrait asset")
			break

	_finish(failures)

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Diyse Step 7C S004 Field Triage Camp revelation, Ilyra authority, incomplete protective response, S005 handoff, and runner-adaptation validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
