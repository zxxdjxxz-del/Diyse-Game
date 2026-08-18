extends SceneTree

const SCENE_PATHS := {
	"S017": "res://game/content/dialogue/chapter_03/S017.tres",
	"S018": "res://game/content/dialogue/chapter_03/S018.tres",
	"S019": "res://game/content/dialogue/chapter_03/S019.tres",
	"S020": "res://game/content/dialogue/chapter_03/S020.tres",
	"S021": "res://game/content/dialogue/chapter_03/S021.tres",
	"H01": "res://game/content/dialogue/chapter_03/H01.tres",
	"H02": "res://game/content/dialogue/chapter_03/H02.tres",
	"H03": "res://game/content/dialogue/chapter_03/H03.tres",
	"H04": "res://game/content/dialogue/chapter_03/H04.tres"
}

var failures: Array[String] = []
var scenes: Dictionary = {}

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	for scene_id in SCENE_PATHS:
		var scene := load(str(SCENE_PATHS[scene_id])) as DiyseDialogueSceneDefinition
		_expect(scene != null, "%s must load for Chapter 3 continuity validation" % scene_id)
		if scene != null:
			scenes[scene_id] = scene
	_validate_s017()
	_validate_s018()
	_validate_s019()
	_validate_s020()
	_validate_s021()
	_validate_optional_scenes()
	_validate_geography_and_knowledge_firewalls()
	_finish()

func _validate_s017() -> void:
	var spoken := _normalized_spoken("S017")
	for required in [
		"they knew which line to put us in.",
		"contained under custodial authority.",
		"there should be something before this.",
		"no, commander. it wasn't included in the copy.",
		"where's the declaration?",
		"then we find out.",
		"food before constitutional crisis."
	]:
		_expect(required in spoken, "S017 lost containment/order-chain line: %s" % required)
	for forbidden in ["last sentinel", "prime card", "ruby", "might."]:
		_expect(forbidden not in spoken, "S017 leaked later Card identification: %s" % forbidden)

func _validate_s018() -> void:
	var spoken := _normalized_spoken("S018")
	for required in [
		"that's an order that should not exist.",
		"they used real pieces to make something false.",
		"prove it.",
		"i know it is contradictory.",
		"belief is not the standard.",
		"neither is pretending.",
		"the order was protecting itself.",
		"enter the suppressed archives."
	]:
		_expect(required in spoken, "S018 lost approved authority line: %s" % required)
	var encounter_sections := _flag_sections("S018", "AUTHORED_ENCOUNTER_HANDOFF")
	_expect(encounter_sections.size() == 2, "S018 must retain exactly two authored nonlethal authority encounters, got %s" % str(encounter_sections))
	_expect(_last_flags("S018").has("UNLOCK_H02_TORREN_MAEVRA_UNSUPERVISED"), "S018 must preserve H02 eligibility unlock")
	_expect("maevra." not in _speaker_texts("S018", "torren"), "S018 must not advance Torren's deliberate Maevra address before H02")

func _validate_s019() -> void:
	var spoken := _normalized_spoken("S019")
	for required in [
		"oh, you miserable ancient piece of shit.",
		"thank fuck.",
		"parts of the place work.",
		"something downstream combined the answers.",
		"i'm coming with you.",
		"not unless one of you has secretly become authorized by a dead civilization.",
		"not this week.",
		"deeper command records."
	]:
		_expect(required in spoken, "S019 lost approved Archive/Nimera line: %s" % required)
	var final_flags := _last_flags("S019")
	for required_flag in [
		"PARTY_NIMERA_PERMANENT_JOINED",
		"FORMATION_CHOOSE_FOUR_ENABLED",
		"UNLOCK_H01_NIMERA_TAKES_OVER_A_TABLE",
		"UNLOCK_H03_ILYRA_AND_NIMERA"
	]:
		_expect(final_flags.has(required_flag), "S019 lost durable handoff: %s" % required_flag)
	for forbidden in ["last sentinel", "prime card", "ruby"]:
		_expect(forbidden not in spoken, "S019 leaked later identification: %s" % forbidden)
	_expect("hunt" not in spoken, "S019 denied judgment branch must not tease Hunt in dialogue")

func _validate_s020() -> void:
	var spoken := _normalized_spoken("S020")
	for required in [
		"command warden.",
		"one i don't know.",
		"that's new.",
		"i don't know.",
		"different. that's all i'm saying until i have something to compare it against.",
		"the judicial declaration and the custody authorization. separate inputs.",
		"this system assembled it from two valid records.",
		"made a lie out of two truths.",
		"it's a map.",
		"this is cresthaven.",
		"old crown outpost in southhold. abandoned.",
		"cresthaven tomorrow."
	]:
		_expect(required in spoken, "S020 lost Warden/Cresthaven correction line: %s" % required)
	for forbidden in ["prime card.", "no. might.", "face: might"]:
		_expect(forbidden not in spoken, "S020 identifies Prime/Might too early: %s" % forbidden)
	var cues := _normalized_cues("S020")
	_expect("/previous error/" in cues and "/last sentinel confirmed/" in cues, "S020 lost exact Last Sentinel machine-output staging")
	_expect("no voice. no feeling. nothing. it's just doing that." in spoken, "S020 must preserve no-manifestation response")
	_expect(_flag_count("S020", "BOSS_HANDOFF") == 1, "S020 must contain exactly one First Command Warden boss handoff")
	_expect(_scene_has_flag("S020", "WARDEN_ONE_HP_BAR"), "S020 Warden must remain one HP bar")
	_expect(_scene_has_flag("S020", "WARDEN_SAME_BAR_STATE_CHANGE"), "S020 Warden must retain same-bar state change")
	for required_flag in [
		"STATE_FIRST_COMMAND_WARDEN_DEFEATED",
		"STATE_FALSE_ORDER_ASSEMBLY_PROVED",
		"STATE_TORREN_ROUTE_SKETCH_ACQUIRED",
		"STATE_CRESTHAVEN_IDENTIFIED"
	]:
		_expect(_last_flags("S020").has(required_flag), "S020 lost durable corrected handoff: %s" % required_flag)
	_expect(_scene_has_flag("S020", "POST_WARDEN_COMMAND_RECORD_ROOM"), "S020 must open the command-record room after the Warden")
	_expect(_scene_has_flag("S020", "FALSE_ORDER_ASSEMBLY_EVIDENCE"), "S020 must preserve false-order proof")
	_expect(_scene_has_flag("S020", "TORREN_ROUTE_SKETCH"), "S020 must preserve Torren's copied map")
	_expect(_scene_has_flag("S020", "RETURN_TO_CAELORA_BEFORE_CRESTHAVEN"), "S020 must return to Caelora before Cresthaven")
	_expect(_scene_has_flag("S020", "NO_CRESTHAVEN_TRAVEL_UNTIL_NEXT_MORNING"), "S020 must stop for the night before Cresthaven")
	_expect("old site reference" not in cues and "old site reference" not in spoken, "S020 must not restore the discarded unexplained old-site reference")

func _validate_s021() -> void:
	var spoken := _normalized_spoken("S021")
	for required in [
		"abandoned.",
		"you're late.",
		"then i'm early.",
		"working headquarters. temporary until we understand what the hell is going on.",
		"because those are different fucking sentences.",
		"same relationship.",
		"prime.",
		"might.",
		"why me?",
		"no fucking idea.",
		"last sentinel.",
		"the card is last sentinel.",
		"and the fourth answer is that we still do not know what last sentinel ultimately means.",
		"it is usable."
	]:
		_expect(required in spoken, "S021 lost approved Last Sentinel/Cresthaven line: %s" % required)
	_expect(_scene_has_flag("S021", "CRESTHAVEN_NEXT_MORNING_ARRIVAL"), "S021 must begin with next-morning Cresthaven arrival")
	_expect(_scene_has_flag("S021", "LAST_SENTINEL_RECOVERED_NOT_MANIFESTED"), "S021 must unlock Last Sentinel without manifestation")
	_expect(_flag_count("S021", "AUTHORED_ENCOUNTER_HANDOFF") == 0 and _flag_count("S021", "BOSS_HANDOFF") == 0, "S021 must contain no combat handoff")
	var final_flags := _last_flags("S021")
	for required_flag in [
		"STORY_CHAPTER_03_COMPLETE",
		"PRIME_LAST_SENTINEL_RECOVERED",
		"CRESTHAVEN_PHASE_01_OPERATIONAL",
		"UNLOCK_H04_LAST_SENTINEL_IS_NOT_INVITED",
		"UNLOCK_HUNT_03_ARCHIVE_JUDGMENT_ENGINE",
		"DO_NOT_AUTO_SKIP_CHARACTER_LIFE_SCENES"
	]:
		_expect(final_flags.has(required_flag), "S021 lost durable Chapter 3 handoff: %s" % required_flag)

func _validate_optional_scenes() -> void:
	var h01 := scenes.get("H01") as DiyseDialogueSceneDefinition
	var h02 := scenes.get("H02") as DiyseDialogueSceneDefinition
	var h03 := scenes.get("H03") as DiyseDialogueSceneDefinition
	var h04 := scenes.get("H04") as DiyseDialogueSceneDefinition
	if h01 != null:
		_expect(h01.trigger_id.contains("after_s019") and h01.trigger_id.contains("at_cresthaven"), "H01 must preserve after-S019 eligibility while requiring Cresthaven access")
		for required in ["there was more table a minute ago.", "you're only assigned half that table.", "fuck both of you."]:
			_expect(required in _normalized_spoken("H01"), "H01 lost table-takeover line: %s" % required)
	if h02 != null:
		_expect(h02.trigger_id.contains("after_s018") and h02.trigger_id.contains("at_cresthaven"), "H02 must preserve after-S018 eligibility while requiring Cresthaven access")
		var torren_text := _speaker_texts("H02", "torren")
		_expect("maevra." in torren_text, "H02 must own Torren's first deliberate Maevra")
		for required in ["weather: wet.", "the river was not wrong.", "don't disappear before morning.", "i'll be here."]:
			_expect(required in _normalized_spoken("H02"), "H02 lost protected relationship line: %s" % required)
	if h03 != null:
		_expect(h03.trigger_id.contains("after_s019") and h03.trigger_id.contains("at_cresthaven"), "H03 must preserve after-S019 eligibility while requiring Cresthaven access")
		for required in ["can i?", "you said no.", "good fuck or bad fuck?", "thanks."]:
			_expect(required in _normalized_spoken("H03"), "H03 lost treatment/not-therapy line: %s" % required)
	if h04 != null:
		_expect(h04.trigger_id.ends_with("after_s021"), "H04 must remain post-S021 only")
		var spoken := _normalized_spoken("H04")
		_expect("he's sleeping in the fucking archive." in spoken, "H04 lost approved final line")
		var cues := _normalized_cues("H04")
		_expect("no glow change" in cues and "no response" in cues, "H04 Card case must remain static/non-activated")

func _validate_geography_and_knowledge_firewalls() -> void:
	var s019_location := str((scenes.get("S019") as DiyseDialogueSceneDefinition).location_id) if scenes.has("S019") else ""
	var s020_location := str((scenes.get("S020") as DiyseDialogueSceneDefinition).location_id) if scenes.has("S020") else ""
	var s021_location := str((scenes.get("S021") as DiyseDialogueSceneDefinition).location_id) if scenes.has("S021") else ""
	_expect("OLD_CITY" in s019_location, "S019 must remain in Old City / Suppressed Archives")
	_expect("OLD_CITY" in s020_location, "S020 Warden must remain in Old City command station")
	_expect("CRESTHAVEN" in s021_location and "OLD_CITY" not in s021_location, "S021 Cresthaven must be a separate location")
	var pre_s021 := _normalized_spoken("S017") + _normalized_spoken("S018") + _normalized_spoken("S019")
	_expect("last sentinel" not in pre_s021, "S017-S019 must not know Last Sentinel")
	_expect("prime card" not in pre_s021, "S017-S019 must not identify the recovered Card as Prime")

func _speaker_texts(scene_id: String, speaker_id: String) -> String:
	if not scenes.has(scene_id):
		return ""
	var result := ""
	for beat in (scenes[scene_id] as DiyseDialogueSceneDefinition).beats:
		if str(beat.get("speaker_id", "")) == speaker_id:
			result += _normalize(str(beat.get("text", ""))) + "\n"
	return result

func _normalized_spoken(scene_id: String) -> String:
	if not scenes.has(scene_id):
		return ""
	var result := ""
	for beat in (scenes[scene_id] as DiyseDialogueSceneDefinition).beats:
		if not str(beat.get("speaker_id", "")).is_empty():
			result += _normalize(str(beat.get("text", ""))) + "\n"
	return result

func _normalized_cues(scene_id: String) -> String:
	if not scenes.has(scene_id):
		return ""
	var result := ""
	for beat in (scenes[scene_id] as DiyseDialogueSceneDefinition).beats:
		var cues = beat.get("cues", {})
		if cues is Dictionary:
			result += _normalize(str(cues)) + "\n"
	return result

func _normalize(value: String) -> String:
	return value.to_lower().replace("’", "'").replace("‘", "'").replace("“", "\"").replace("”", "\"")

func _beat_flags(beat: Dictionary) -> Array:
	var cues = beat.get("cues", {})
	if not (cues is Dictionary):
		return []
	var flags = cues.get("implementation_flags", [])
	return flags if flags is Array else []

func _scene_has_flag(scene_id: String, flag: String) -> bool:
	if not scenes.has(scene_id):
		return false
	for beat in (scenes[scene_id] as DiyseDialogueSceneDefinition).beats:
		if _beat_flags(beat).has(flag):
			return true
	return false

func _flag_count(scene_id: String, flag: String) -> int:
	if not scenes.has(scene_id):
		return 0
	var count := 0
	for beat in (scenes[scene_id] as DiyseDialogueSceneDefinition).beats:
		if _beat_flags(beat).has(flag):
			count += 1
	return count

func _flag_sections(scene_id: String, flag: String) -> Array[String]:
	var result: Array[String] = []
	if not scenes.has(scene_id):
		return result
	for beat in (scenes[scene_id] as DiyseDialogueSceneDefinition).beats:
		if not _beat_flags(beat).has(flag):
			continue
		var cues = beat.get("cues", {})
		var section := str(cues.get("source_section", "")) if cues is Dictionary else ""
		if section not in result:
			result.append(section)
	return result

func _last_flags(scene_id: String) -> Array:
	if not scenes.has(scene_id):
		return []
	var scene: DiyseDialogueSceneDefinition = scenes[scene_id]
	if scene.beats.is_empty():
		return []
	return _beat_flags(scene.beats[-1])

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Step 7C Chapter 3 continuity, Cresthaven correction, Last Sentinel firewall, optional-scene, and durable-handoff validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
