extends SceneTree

var failures: Array[String] = []

const CH0_REGISTRY := "res://game/content/dialogue/chapter_00/chapter_00_dialogue_registry.tres"
const CH1_REGISTRY := "res://game/content/dialogue/chapter_01/chapter_01_dialogue_registry.tres"
const CH2_REGISTRY := "res://game/content/dialogue/chapter_02/chapter_02_dialogue_registry.tres"
const CH3_REGISTRY := "res://game/content/dialogue/chapter_03/chapter_03_dialogue_registry.tres"

const CH1_COUNTS := {
	"S007": 104,
	"S008": 81,
	"S009": 150,
	"S010": 154,
	"S011": 122,
	"C03": 27,
	"C04": 33,
	"C05": 80,
}

const CH2_COUNTS := {
	"S012": 6,
	"S013": 8,
	"S014": 9,
	"S015": 6,
	"S016": 8,
	"C06": 10,
	"C07": 11,
}

const CH3_COUNTS := {
	"S017": 14,
	"S018": 14,
	"S019": 13,
	"S020": 12,
	"S021": 12,
	"H01": 4,
	"H02": 10,
	"H03": 10,
	"H04": 10,
}

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var ch0_registry = load(CH0_REGISTRY)
	var ch1_registry = load(CH1_REGISTRY)
	var ch2_registry = load(CH2_REGISTRY)
	var ch3_registry = load(CH3_REGISTRY)
	_expect(ch0_registry != null, "Chapter 0 registry must load")
	_expect(ch1_registry != null, "Chapter 1 registry must load")
	_expect(ch2_registry != null, "Chapter 2 registry must load")
	_expect(ch3_registry != null, "Chapter 3 registry must load")
	if ch0_registry == null or ch1_registry == null or ch2_registry == null or ch3_registry == null:
		_finish()
		return

	_validate_ch0(ch0_registry)
	_validate_ch1(ch1_registry)
	_validate_ch2(ch2_registry)
	_validate_ch3(ch3_registry)
	_finish()

func _load_scene(path: String, registry, expected_count: int = -1):
	var scene = load(path)
	_expect(scene != null, "%s must load" % path)
	if scene == null:
		return null
	var schema_failures: Array[String] = scene.validate_schema(registry)
	_expect(schema_failures.is_empty(), "%s schema failures: %s" % [path, str(schema_failures)])
	if expected_count >= 0:
		_expect(scene.beats.size() == expected_count, "%s beat count changed: expected %d, got %d" % [path, expected_count, scene.beats.size()])
	var runner_beats: Array[Dictionary] = scene.to_runner_beats(registry)
	_expect(runner_beats.size() == scene.beats.size(), "%s must adapt one-for-one to runner beats" % path)
	return scene

func _scene_path(chapter: String, scene_id: String) -> String:
	return "res://game/content/dialogue/%s/%s.tres" % [chapter, scene_id]

func _spoken(scene) -> String:
	var parts: Array[String] = []
	for beat in scene.beats:
		var text := str(beat.get("text", ""))
		if not text.is_empty():
			parts.append(text)
	return "\n".join(parts)

func _staging(scene) -> String:
	var parts: Array[String] = []
	for beat in scene.beats:
		var cues = beat.get("cues", {})
		if cues is Dictionary:
			parts.append(str(cues.get("staging", "")))
	return "\n".join(parts)

func _all_flags(scene) -> Array[String]:
	var result: Array[String] = []
	for beat in scene.beats:
		var cues = beat.get("cues", {})
		if cues is Dictionary:
			var flags = cues.get("implementation_flags", [])
			if flags is Array:
				for flag in flags:
					result.append(str(flag))
	return result

func _speaker_at(scene, beat_id: String) -> String:
	for beat in scene.beats:
		if str(beat.get("beat_id", "")) == beat_id:
			return str(beat.get("speaker_id", ""))
	return ""

func _text_at(scene, beat_id: String) -> String:
	for beat in scene.beats:
		if str(beat.get("beat_id", "")) == beat_id:
			return str(beat.get("text", ""))
	return ""

func _validate_ch0(registry) -> void:
	var s004 = _load_scene(_scene_path("chapter_00", "S004"), registry, 57)
	var s005 = _load_scene(_scene_path("chapter_00", "S005"), registry, 31)
	if s004 == null or s005 == null:
		return
	var combined := (s004.authoring_notes + "\n" + str(s004.beats) + "\n" + s005.authoring_notes + "\n" + str(s005.beats)).to_lower()
	_expect("broken champion's ward" not in combined, "Chapter 0 Resource layer must not restore Broken Champion's Ward terminology")
	_expect("broken_champion_ward" not in combined, "Chapter 0 Resource layer must not restore BROKEN_CHAMPION_WARD flags")
	_expect("ESTABLISH_INCOMPLETE_PROTECTIVE_RESPONSE" in _all_flags(s004), "S004 must establish the neutral incomplete protective-response state")
	_expect("PROTECTIVE_RESPONSE_THREE_ROUNDS" in _all_flags(s005), "S005 must preserve the three-round protection mechanic")
	_expect("PROTECTIVE_RESPONSE_PLUS_20_TOTAL_DEFENSE" in _all_flags(s005), "S005 must preserve +20 Total Defense")
	_expect("PROTECTIVE_RESPONSE_FIRST_ELIGIBLE_DIRECT_HIT_MINUS_20_PERCENT_PER_PARTY_MEMBER" in _all_flags(s005), "S005 must preserve the first-hit reduction mechanic")

func _validate_ch1(registry) -> void:
	var scenes: Dictionary = {}
	var mandatory_total := 0
	for scene_id in CH1_COUNTS.keys():
		var scene = _load_scene(_scene_path("chapter_01", str(scene_id)), registry, int(CH1_COUNTS[scene_id]))
		if scene != null:
			scenes[scene_id] = scene
			if str(scene_id).begins_with("S"):
				mandatory_total += scene.beats.size()
	_expect(mandatory_total == 611, "Chapter 1 mandatory Resource conversion must preserve all 611 recovered S007-S011 beats")
	if not scenes.has("C03") or not scenes.has("C04") or not scenes.has("C05"):
		return
	var c03 = scenes["C03"]
	var c04 = scenes["C04"]
	var c05 = scenes["C05"]
	var c03_text := _spoken(c03)
	_expect("What is that?\nDinner.\nI understood the category." in c03_text, "C03 protected opening must remain intact")
	_expect("When you're cooking for six, you make a meal. Cooking for one, you make enough not to do it again tomorrow." in c03_text, "C03 protected Torren road-cooking line must remain intact")
	_expect("Tomorrow night, you cook.\nI withdraw my complaint.\nToo late." in c03_text, "C03 protected ending must remain intact")
	_expect(_speaker_at(c04, "C04_B009") == "cyanis" and _text_at(c04, "C04_B009") == "Whore.", "C04 hard protected first insult must be Cyanis: Whore.")
	_expect(_speaker_at(c04, "C04_B010") == "torren" and _text_at(c04, "C04_B010") == "Bitch.", "C04 hard protected response must be Torren: Bitch.")
	_expect(_speaker_at(c04, "C04_B012") == "torren" and _text_at(c04, "C04_B012") == "Oh, fuck you.", "C04 protected escalation speaker assignment changed")
	_expect(_speaker_at(c04, "C04_B013") == "cyanis" and _text_at(c04, "C04_B013") == "You called me a bitch.", "C04 protected escalation must preserve Cyanis reply")
	_expect(_speaker_at(c04, "C04_B014") == "torren" and _text_at(c04, "C04_B014") == "You called me a whore.", "C04 protected escalation must preserve Torren reply")
	_expect("Touch the map and I'll break your fucking fingers.\nSee, now we're friends." in _spoken(c04), "C04 map/charcoal friendship beat must remain intact")
	var c05_text := _spoken(c05)
	_expect("Eat.\nEat." in c05_text, "C05 doubled Eat order must remain intact")
	_expect("Were you talking about me?\nYes.\nAt length." in c05_text, "C05 protected talking-about-Cyanis exchange must remain intact")
	_expect("I hate him.\nNo, you don't.\nI know.\nI can still hear you.\nGood." in c05_text, "C05 protected work-stopping ending rhythm must remain intact")

func _validate_ch2(registry) -> void:
	var scenes: Dictionary = {}
	for scene_id in CH2_COUNTS.keys():
		var scene = _load_scene(_scene_path("chapter_02", str(scene_id)), registry, int(CH2_COUNTS[scene_id]))
		if scene != null:
			scenes[scene_id] = scene
	if scenes.size() != CH2_COUNTS.size():
		return
	for scene_id in scenes.keys():
		var note := str(scenes[scene_id].authoring_notes).to_lower()
		_expect("closed-authority" in note, "Chapter 2 %s must remain explicitly marked closed-authority rather than reconstructed final dialogue" % scene_id)
	var s012 = scenes["S012"]
	_expect("Do not declare Dunmere's water safe" in _staging(s012), "S012 must preserve the no-false-water-safe boundary")
	var s013 = scenes["S013"]
	_expect("It copied me." in _staging(s013), "S013 must preserve the protected Ilyra copied-actor line as conditional staging authority")
	_expect("CONDITIONAL_COPIED_ACTOR_LINE_NOT_SERIALIZED" in _all_flags(s013), "S013 must not serialize a copied-actor line unconditionally")
	_expect("thirty-one transfers" in _staging(s013).to_lower(), "S013 must preserve exact thirty-one transfers discovery wording")
	var s014 = scenes["S014"]
	_expect(_text_at(s014, "S014_B006") == "Torren!" and _text_at(s014, "S014_B007") == "Harth.", "S014 protected Maevra address breach changed")
	_expect("REGIONAL_HUNT_BRANCH_VISIBLE_BUT_DENIED" in _all_flags(s014), "S014 must preserve the first-pass denied Hunt branch")
	var s015 = scenes["S015"]
	_expect("ONE_HP_BAR" in _all_flags(s015), "S015 Rhazek must remain one HP bar")
	_expect("SUNDER_THE_GATE" in _all_flags(s015), "S015 must preserve Sunder the Gate recovery")
	var s016 = scenes["S016"]
	_expect("HOLD_THE_JUNCTION" in _all_flags(s016), "S016 must preserve Hold the Junction as the authored encounter")
	_expect("NO_COMBAT_AFTER_THRESHOLD" in _all_flags(s016), "S016 must forbid combat after the final extraction threshold")
	var c06 = scenes["C06"]
	_expect(_speaker_at(c06, "C06_B003") == "torren" and _text_at(c06, "C06_B003") == "Your other left.", "C06 protected glove line changed")
	_expect(_speaker_at(c06, "C06_B008") == "torren" and _text_at(c06, "C06_B008") == "Still rope.", "C06 protected rope callback changed")
	var c07 = scenes["C07"]
	_expect(_speaker_at(c07, "C07_B004") == "cyanis" and _text_at(c07, "C07_B004") == "Your lace is fucked up.", "C07 protected bootlace line changed")
	_expect(_speaker_at(c07, "C07_B009") == "torren" and _text_at(c07, "C07_B009") == "Sit.", "C07 protected Sit line changed")
	_expect("No dream" in c07.authoring_notes, "C07 must keep the no-dream-flashback boundary")

func _validate_ch3(registry) -> void:
	var scenes: Dictionary = {}
	for scene_id in CH3_COUNTS.keys():
		var scene = _load_scene(_scene_path("chapter_03", str(scene_id)), registry, int(CH3_COUNTS[scene_id]))
		if scene != null:
			scenes[scene_id] = scene
	if scenes.size() != CH3_COUNTS.size():
		return
	for scene_id in scenes.keys():
		var note := str(scenes[scene_id].authoring_notes).to_lower()
		_expect("closed-authority" in note, "Chapter 3 %s must remain explicitly marked closed-authority rather than newly rewritten dialogue" % scene_id)
	var s017 = scenes["S017"]
	_expect(s017.location_id == "LOC_CAELORA_CONTAINMENT", "S017 must remain in Caelora")
	_expect("prime" not in _spoken(s017).to_lower(), "S017 spoken dialogue must not identify Prime")
	_expect("last sentinel" not in _spoken(s017).to_lower(), "S017 spoken dialogue must not identify Last Sentinel")
	var s018 = scenes["S018"]
	_expect("AUTHORED_NONLETHAL_CONFRONTATION_1" in _all_flags(s018) and "AUTHORED_NONLETHAL_CONFRONTATION_2" in _all_flags(s018), "S018 must preserve exactly two authored nonlethal authority confrontations")
	_expect(_speaker_at(s018, "S018_B013") == "torren" and _text_at(s018, "S018_B013") == "Solmar.", "S018 must preserve Torren's formal Solmar address")
	var s019 = scenes["S019"]
	_expect(s019.location_id == "LOC_OLD_CITY_SUPPRESSED_ARCHIVES", "S019 must remain in Old City / Suppressed Archives")
	_expect(_text_at(s019, "S019_B007") == "That's another section.", "S019 Hunt-branch opening changed")
	_expect(_text_at(s019, "S019_B009") == "Not unless one of you has secretly become authorized by a dead civilization.", "S019 protected denied-branch line changed")
	_expect(_text_at(s019, "S019_B010") == "Not this week." and _text_at(s019, "S019_B011") == "Then no.", "S019 protected denied-branch ending changed")
	var s020 = scenes["S020"]
	_expect(s020.location_id == "LOC_OLD_CITY_COMMAND_STATION", "S020 must remain in the Old City command-station sequence, not Cresthaven")
	_expect("/PREVIOUS ERROR/" in _staging(s020) and "/LAST SENTINEL CONFIRMED/" in _staging(s020), "S020 exact Ancient output changed")
	_expect("might" not in _spoken(s020).to_lower(), "S020 spoken dialogue must not identify Might")
	_expect("NO_PRIME_MANIFESTATION" in _all_flags(s020), "S020 must prohibit Prime manifestation")
	var s021 = scenes["S021"]
	_expect(s021.location_id == "LOC_CRESTHAVEN_COMMAND_ESTABLISHMENT", "S021 must occur at separate Cresthaven")
	_expect("FOURTH BOUNDED ANSWER" in _staging(s021), "S021 must preserve the fourth answer: meaning unknown")
	_expect("NO_MANIFESTATION" in _all_flags(s021), "S021 must unlock Last Sentinel without manifesting it")
	_expect("CRESTHAVEN_CH3_ESTABLISHMENT" in _all_flags(s021), "S021 must expose only the Chapter 3 Cresthaven establishment state")
	var h02 = scenes["H02"]
	_expect(_speaker_at(h02, "H02_B004") == "torren" and _text_at(h02, "H02_B004") == "Maevra.", "H02 first deliberate Torren->Maevra address changed")
	_expect("Don't disappear before morning.\nWasn't planning to.\nThat isn't the same thing.\nI'll be here." in _spoken(h02), "H02 protected ending changed")
	var h03 = scenes["H03"]
	_expect("Well. Fuck.\nGood fuck or bad fuck?\nDon't steal my language.\nYou brought a lot of it." in _spoken(h03), "H03 protected language-theft exchange changed")
	var h04 = scenes["H04"]
	_expect(_speaker_at(h04, "H04_B009") == "nimera" and _text_at(h04, "H04_B009") == "He's sleeping in the fucking Archive.", "H04 controlling final Nimera line changed")
	_expect("does not move, speak, react, glow autonomously, choose, want, or manifest" in _staging(h04), "H04 must keep Last Sentinel physically inert")

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("DIYSE Chapters 0-3 dialogue Resource synchronization validation passed: Ch0 terminology rebased, Ch1 exact conversion preserved, Ch2/3 closed-authority shells bounded, and Chapter 3 geography/Prime/relationship locks intact.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
