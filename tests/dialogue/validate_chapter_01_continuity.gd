extends SceneTree

const REGISTRY_PATH := "res://game/content/dialogue/chapter_01/chapter_01_dialogue_registry.tres"
const SCENE_PATHS := {
	"S007": "res://game/content/dialogue/chapter_01/S007.tres",
	"S008": "res://game/content/dialogue/chapter_01/S008.tres",
	"S009": "res://game/content/dialogue/chapter_01/S009.tres",
	"S010": "res://game/content/dialogue/chapter_01/S010.tres",
	"S011": "res://game/content/dialogue/chapter_01/S011.tres",
	"C03": "res://game/content/dialogue/chapter_01/C03.tres",
	"C04": "res://game/content/dialogue/chapter_01/C04.tres",
	"C05": "res://game/content/dialogue/chapter_01/C05.tres"
}

var failures: Array[String] = []
var scenes: Dictionary = {}

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var registry := load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry
	_expect(registry != null, "Chapter 1 registry must load")
	if registry == null:
		_finish()
		return

	for scene_id in SCENE_PATHS:
		var scene := load(str(SCENE_PATHS[scene_id])) as DiyseDialogueSceneDefinition
		_expect(scene != null, "%s must load for continuity validation" % scene_id)
		if scene != null:
			scenes[scene_id] = scene

	_validate_order_and_party()
	_validate_durable_handoffs()
	_validate_knowledge_firewall()
	_validate_character_life()
	_validate_c04_final_version()
	_validate_torren_maevra_progression()
	_finish()

func _validate_order_and_party() -> void:
	if scenes.has("S007"):
		var s007: DiyseDialogueSceneDefinition = scenes["S007"]
		for required in ["cyanis", "ilyra", "maevra"]:
			_expect(required in s007.participants, "S007 missing required participant: %s" % required)
	if scenes.has("S009"):
		var s009: DiyseDialogueSceneDefinition = scenes["S009"]
		for required in ["torren", "maevra", "cyanis", "ilyra", "edda"]:
			_expect(required in s009.participants, "S009 missing required participant: %s" % required)
	for optional_id in ["C03", "C04", "C05"]:
		if scenes.has(optional_id):
			var scene: DiyseDialogueSceneDefinition = scenes[optional_id]
			_expect(scene.scene_kind == "character_life", "%s must remain Character-Life" % optional_id)
			_expect(scene.trigger_id.ends_with("after_s011"), "%s must unlock after S011 and remain order-independent" % optional_id)

func _validate_durable_handoffs() -> void:
	_expect(_last_flags("S007").has("PARTY_ADD_MAEVRA_GUEST"), "S007 lost Maevra guest-party handoff")
	_expect(_last_flags("S009").has("ROSTER_ADD_TORREN_PERMANENT"), "S009 lost Torren permanent-roster handoff")
	var final_flags := _last_flags("S011")
	for required in [
		"STORY_CHAPTER_01_COMPLETE",
		"ROUTE_DUNMERE_UNLOCKED",
		"UNLOCK_C03_TORRENS_VERSION_OF_DINNER",
		"UNLOCK_C04_WHAT_THE_MAP_SAYS",
		"UNLOCK_C05_TWO_PROFESSIONALS_COMPLAINING_ABOUT_CYANIS",
		"DO_NOT_AUTO_SKIP_CHARACTER_LIFE_SCENES"
	]:
		_expect(final_flags.has(required), "S011 lost Chapter 1 durable handoff: %s" % required)

func _validate_knowledge_firewall() -> void:
	var mandatory_spoken := ""
	for scene_id in ["S007", "S008", "S009", "S010", "S011"]:
		mandatory_spoken += "\n" + _spoken_text(scene_id).to_lower()
	for forbidden in ["last sentinel", "prime manifestation", "underground crest network", "the entity", "nimera"]:
		_expect(forbidden not in mandatory_spoken, "Chapter 1 leaked later-story knowledge into spoken dialogue: %s" % forbidden)

	var s011 := _spoken_text("S011")
	for required in ["Grace.", "Might.", "Acuity here.", "Ruin."]:
		_expect(required in s011, "S011 lost operational Face-language beat: %s" % required)
	_expect("Resource here." not in s011, "S011 must not regress to the retired Resource Face terminology")
	_expect("Why are Faces on a route map?" in s011, "S011 lost the Wayfinder technical-cartography question")
	_expect("Same Face." in s011 and "Not the same pattern." in s011, "S011 lost bounded sealed-Card/Wayfinder comparison")
	_expect("Last Sentinel" not in s011 and "Prime" not in s011, "S011 must not identify the sealed Card as Prime/Last Sentinel")

func _validate_character_life() -> void:
	var c03 := _spoken_text("C03")
	for required in [
		"What is that?",
		"Dinner.",
		"I understood the category.",
		"Hot.",
		"Enough.",
		"Safe.",
		"Cheap.",
		"Tomorrow night, you cook.",
		"I withdraw my complaint.",
		"Too late."
	]:
		_expect(required in c03, "C03 lost approved line: %s" % required)
	var c03_cues := _all_cues_text("C03").to_lower()
	_expect("takes out a blunt" in c03_cues, "C03 lost Torren's post-dinner blunt staging")
	_expect("coals" in c03_cues or "ember" in c03_cues, "C03 must light the blunt from existing fire/coals")
	_expect("lighter" not in c03_cues, "C03 must not introduce a modern lighter")

	var c05 := _spoken_text("C05")
	for required in [
		"You're supposed to be resting.",
		"I am sitting down.",
		"That's not the same thing.",
		"Recently.",
		"That is not an answer.",
		"It was intended as one.",
		"I hate him.",
		"No, you don't.",
		"I know.",
		"I can still hear you.",
		"Good."
	]:
		_expect(required in c05, "C05 lost approved line: %s" % required)

	for optional_id in ["C03", "C04", "C05"]:
		var spoken := _spoken_text(optional_id).to_lower()
		for forbidden in ["last sentinel", "prime", "black host", "vaelkor", "entity"]:
			_expect(forbidden not in spoken, "%s leaked mandatory/later plot terminology: %s" % [optional_id, forbidden])

func _validate_c04_final_version() -> void:
	var c04 := _spoken_text("C04")
	for required in [
		"Evidence ruins everything.",
		"Fuck no.",
		"Old slut.",
		"Bitch.",
		"That says “old cut.”",
		"That says “old slut.”",
		"It’s a C.",
		"It’s an S.",
		"It’s a fucking C.",
		"Then write a fucking C.",
		"You called me an old slut.",
		"You read “old cut” as “old slut.”",
		"Because that’s what you wrote.",
		"Then learn to fucking read.",
		"Touch the map and I’ll break your fucking fingers.",
		"See, now we’re friends.",
		"Good night, Torren.",
		"Fuck off, Cyanis."
	]:
		_expect(required in c04, "C04 lost current final-version line: %s" % required)
	_expect("old whore" not in c04.to_lower(), "C04 must not regress to the superseded old-whore version")
	_expect("\nShore.\n" not in "\n" + c04 + "\n", "C04 must not regress to the superseded Shore reconstruction")

func _validate_torren_maevra_progression() -> void:
	var s009 := _spoken_pairs("S009")
	_expect(_contains_pair(s009, "maevra", "Harth."), "S009 lost Maevra's Harth reunion address")
	_expect(_contains_pair(s009, "torren", "Solmar."), "S009 lost Torren's Solmar reunion address")
	for scene_id in ["S009", "S010", "S011"]:
		for pair in _spoken_pairs(scene_id):
			var speaker := str(pair[0])
			var text := str(pair[1])
			if speaker == "torren":
				_expect(text != "Mae." and text != "Maevra.", "%s advances Torren/Maevra address progression too early" % scene_id)
			if speaker == "maevra":
				_expect(text != "T." and text != "Torren.", "%s advances Torren/Maevra address progression too early" % scene_id)

func _last_flags(scene_id: String) -> Array:
	if not scenes.has(scene_id):
		return []
	var scene: DiyseDialogueSceneDefinition = scenes[scene_id]
	if scene.beats.is_empty():
		return []
	var cues = scene.beats[-1].get("cues", {})
	if not (cues is Dictionary):
		return []
	var flags = cues.get("implementation_flags", [])
	return flags if flags is Array else []

func _spoken_text(scene_id: String) -> String:
	if not scenes.has(scene_id):
		return ""
	var result := ""
	for beat in (scenes[scene_id] as DiyseDialogueSceneDefinition).beats:
		if not str(beat.get("speaker_id", "")).is_empty():
			result += str(beat.get("text", "")) + "\n"
	return result

func _spoken_pairs(scene_id: String) -> Array:
	var result: Array = []
	if not scenes.has(scene_id):
		return result
	for beat in (scenes[scene_id] as DiyseDialogueSceneDefinition).beats:
		var speaker := str(beat.get("speaker_id", ""))
		if not speaker.is_empty():
			result.append([speaker, str(beat.get("text", ""))])
	return result

func _contains_pair(pairs: Array, speaker: String, text: String) -> bool:
	for pair in pairs:
		if str(pair[0]) == speaker and str(pair[1]) == text:
			return true
	return false

func _all_cues_text(scene_id: String) -> String:
	if not scenes.has(scene_id):
		return ""
	var result := ""
	for beat in (scenes[scene_id] as DiyseDialogueSceneDefinition).beats:
		var cues = beat.get("cues", {})
		if not (cues is Dictionary):
			continue
		for key in ["staging", "staging_after", "source_section"]:
			result += "\n" + str(cues.get(key, ""))
	return result

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Step 7C Chapter 1 continuity, final-version, optional-scene, relationship, knowledge-firewall, and durable-handoff validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
