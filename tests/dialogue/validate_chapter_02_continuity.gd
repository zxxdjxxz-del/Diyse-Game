extends SceneTree

const SCENE_PATHS := {
	"S012": "res://game/content/dialogue/chapter_02/S012.tres",
	"S013": "res://game/content/dialogue/chapter_02/S013.tres",
	"S014": "res://game/content/dialogue/chapter_02/S014.tres",
	"S015": "res://game/content/dialogue/chapter_02/S015.tres",
	"S016": "res://game/content/dialogue/chapter_02/S016.tres",
	"C06": "res://game/content/dialogue/chapter_02/C06.tres",
	"C07": "res://game/content/dialogue/chapter_02/C07.tres"
}

var failures: Array[String] = []
var scenes: Dictionary = {}

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	for scene_id in SCENE_PATHS:
		var scene := load(str(SCENE_PATHS[scene_id])) as DiyseDialogueSceneDefinition
		_expect(scene != null, "%s must load for Chapter 2 continuity validation" % scene_id)
		if scene != null:
			scenes[scene_id] = scene

	_validate_optional_gates()
	_validate_s012_waterworks()
	_validate_s013_archive()
	_validate_s014_prisoner_agency_and_address_breach()
	_validate_s015_rhazek_limit()
	_validate_s016_extraction_and_hunt_handoff()
	_validate_c06()
	_validate_c07()
	_validate_knowledge_and_relationship_firewalls()
	_finish()

func _validate_optional_gates() -> void:
	for optional_id in ["C06", "C07"]:
		if not scenes.has(optional_id):
			continue
		var scene: DiyseDialogueSceneDefinition = scenes[optional_id]
		_expect(scene.scene_kind == "character_life", "%s must remain Character-Life" % optional_id)
		_expect(scene.trigger_id.ends_with("after_s016"), "%s must unlock after S016" % optional_id)

func _validate_s012_waterworks() -> void:
	var spoken := _spoken_text("S012")
	for required in [
		"This didn’t come in with the river.",
		"So it entered after filtration.",
		"Somebody put it there.",
		"The lower feed is shut.",
		"And don’t tell them the rest is safe.",
		"Tell them the lower feed is shut. Nothing more.",
		"Find out how they did it."
	]:
		_expect(required in spoken, "S012 lost contamination/water-safety line: %s" % required)
	_expect("the rest is safe" not in spoken.to_lower().replace("don’t tell them the rest is safe", ""), "S012 must not falsely declare all remaining water safe")

func _validate_s013_archive() -> void:
	var spoken := _spoken_text("S013")
	for required in [
		"Fair assumption.",
		"I’m functional.",
		"That wasn’t the question.",
		"It was the answer I had.",
		"These are transfers.",
		"Thirty-one.",
		"Thirty-one what?",
		"People.",
		"Recorded.",
		"Meaning that’s what this record accounts for.",
		"Not everyone who came through.",
		"Harth.",
		"I know."
	]:
		_expect(required in spoken, "S013 lost approved line: %s" % required)
	var cues := _all_cues_text("S013")
	_expect("eligible action actually completes" in cues, "S013 Memory Scribe must key off a completed eligible action")
	_expect("does not read menu selections" in cues.to_lower(), "S013 Memory Scribe must not read unexecuted menu choices")
	_expect("One HP bar" in cues, "S013 Archive Leviathan must remain one HP bar")
	_expect("If a Recorded Pattern actually persists through the threshold" in cues, "S013 Same one?/Yes. exchange must remain conditional")
	_expect("not everyone who came through" in spoken.to_lower(), "S013 must preserve the thirty-one-transfers/not-a-headcount distinction")

func _validate_s014_prisoner_agency_and_address_breach() -> void:
	var spoken := _spoken_text("S014")
	for required in [
		"I’m not touching anyone who doesn’t want me to.",
		"Can I look?",
		"Don’t fucking twist it.",
		"May I?",
		"Then later.",
		"All right.",
		"Who wants to.",
		"You keep the door.",
		"Knock.",
		"Who?",
		"Dovaren.",
		"Just Dovaren?",
		"Currently.",
		"Don’t open that gate and assume we’re ready.",
		"We come back first."
	]:
		_expect(required in spoken, "S014 lost prisoner-agency/door-control line: %s" % required)

	var pairs := _spoken_pairs("S014")
	var breach_found := false
	for i in range(max(0, pairs.size() - 1)):
		if str(pairs[i][0]) == "maevra" and str(pairs[i][1]) == "Torren!":
			breach_found = true
			_expect(str(pairs[i + 1][0]) == "maevra" and str(pairs[i + 1][1]) == "Harth.", "S014 Torren! breach must be immediately corrected to Harth.")
			break
	_expect(breach_found, "S014 lost Maevra’s sole involuntary Torren! address breach")
	var cues := _all_cues_text("S014").to_lower()
	_expect("prisoners themselves lower the inside bar" in cues, "S014 prisoners must retain control of the defensible safe-room bar")
	_expect("party does not “lock the prisoners in.”" in cues or "party does not \"lock the prisoners in.\"" in cues, "S014 must not convert the safe room into party-controlled confinement")

func _validate_s015_rhazek_limit() -> void:
	var spoken := _spoken_text("S015")
	for required in [
		"I authorized it.",
		"Wasn’t what I asked.",
		"Yes.",
		"Then we have finished talking.",
		"That’s deliberate.",
		"You won access to it.",
		"You don’t want to.",
		"Open it.",
		"Gallery route opening.",
		"Move."
	]:
		_expect(required in spoken, "S015 lost Rhazek/Bastion line: %s" % required)
	var cues := _all_cues_text("S015")
	_expect("ONE HP BAR" in cues.to_upper(), "S015 Rhazek must remain one HP bar")
	_expect("NO REFORGED COMMANDER" in cues.to_upper(), "S015 must not import Reforged Commander backward")
	_expect("NO BASTION DEVOURER" in cues.to_upper(), "S015 must not import Bastion Devourer backward")
	_expect("withdraws with his remaining personnel" in cues.to_lower(), "S015 Rhazek must survive and withdraw")
	_expect("STATE_BASTION_EXTRACTION_CONTROL_ACQUIRED" in _last_flags("S015"), "S015 lost Bastion extraction-control handoff")
	_expect("STATE_RHAZEK_CH02_WITHDRAWN" in _last_flags("S015"), "S015 lost Rhazek withdrawal state handoff")

func _validate_s016_extraction_and_hunt_handoff() -> void:
	var spoken := _spoken_text("S016")
	for required in [
		"Move.",
		"My brother.",
		"I don’t know.",
		"We can’t go that way now.",
		"They’re cutting the column.",
		"Then we don’t let them.",
		"They’re through.",
		"I do right now.",
		"Bastion controls dropped the west branch lock.",
		"Accessible.",
		"Wouldn’t call it safe.",
		"Not tonight."
	]:
		_expect(required in spoken, "S016 lost extraction/Hunt-state line: %s" % required)

	var encounter_sections := _flag_sections("S016", "AUTHORED_ENCOUNTER_HANDOFF")
	_expect(encounter_sections.size() == 1, "S016 must contain exactly one authored mandatory encounter section, got %s" % str(encounter_sections))
	if encounter_sections.size() == 1:
		_expect("HOLD THE JUNCTION" in str(encounter_sections[0]).to_upper(), "S016 sole authored combat must remain Hold the Junction")

	var scene: DiyseDialogueSceneDefinition = scenes.get("S016")
	if scene != null:
		var threshold_index := -1
		for i in range(scene.beats.size()):
			var flags := _beat_flags(scene.beats[i])
			if flags.has("NO_COMBAT_AFTER_THIS_BEAT"):
				threshold_index = i
				break
		_expect(threshold_index >= 0, "S016 lost final-extraction no-combat threshold")
		if threshold_index >= 0:
			for i in range(threshold_index + 1, scene.beats.size()):
				_expect(not _beat_flags(scene.beats[i]).has("AUTHORED_ENCOUNTER_HANDOFF"), "S016 contains authored combat after the final extraction threshold")

	var final_flags := _last_flags("S016")
	for required_flag in [
		"STORY_CHAPTER_02_COMPLETE",
		"UNLOCK_C06_THREE_PEOPLE_WHO_KNOW_EACH_OTHER_NOW",
		"UNLOCK_C07_BAD_DREAMS_NO_QUESTIONS",
		"UNLOCK_HUNT_02_TRANSFER_EXECUTIONER",
		"DO_NOT_AUTO_SKIP_CHARACTER_LIFE_SCENES"
	]:
		_expect(final_flags.has(required_flag), "S016 lost durable Chapter 2 handoff: %s" % required_flag)

func _validate_c06() -> void:
	var spoken := _spoken_text("C06")
	for required in [
		"You seen my glove?",
		"Which one?",
		"Your other left.",
		"It’s string with confidence.",
		"Your faces did.",
		"Knife.",
		"You don’t even know what I was going to say.",
		"Seriously?",
		"You’re done.",
		"Still rope.",
		"Get out.",
		"Finally, a workable plan."
	]:
		_expect(required in spoken, "C06 lost approved line: %s" % required)
	var simultaneous_found := false
	for pair in _spoken_pairs("C06"):
		if str(pair[0]) == "ilyra_torren" and str(pair[1]) == "No.":
			simultaneous_found = true
			break
	_expect(simultaneous_found, "C06 must preserve Ilyra/Torren’s simultaneous No. as one simultaneous source line")
	var cues := _all_cues_text("C06").to_lower()
	_expect("nobody asks if anyone is all right" in cues, "C06 must preserve comfortable silence without therapy framing")

func _validate_c07() -> void:
	var spoken := _spoken_text("C07")
	for required in [
		"You’re going to burn your fingers doing that.",
		"That the same shit you had three nights ago?",
		"Got wet.",
		"Wet pockets.",
		"Wet sleeves.",
		"People who say “could be worse.”",
		"If you two are going to whisper, whisper louder.",
		"Dry-footed privilege.",
		"What time is it?",
		"Getting lighter."
	]:
		_expect(required in spoken, "C07 lost Audit78 Rewrite Draft 2 line: %s" % required)
	var cues := _all_cues_text("C07").to_lower()
	_expect("uses one of the remaining coals to light it" in cues, "C07 blunt must be lit from existing coals")
	_expect("no modern lighter" in cues, "C07 must retain explicit no-modern-lighter production lock")
	_expect("no dream visualization" in cues, "C07 must not visualize dreams")
	_expect("nobody asks what another person dreamed about" in cues, "C07 must not force dream disclosure")

func _validate_knowledge_and_relationship_firewalls() -> void:
	var all_spoken := ""
	for scene_id in ["S012", "S013", "S014", "S015", "S016", "C06", "C07"]:
		all_spoken += "\n" + _spoken_text(scene_id).to_lower()
	for forbidden in ["last sentinel", "prime manifestation", "sixfold accord", "nimera", "suppressed archive", "underground crest network"]:
		_expect(forbidden not in all_spoken, "Chapter 2 leaked later-story knowledge into dialogue: %s" % forbidden)

	for scene_id in ["S012", "S013", "S014", "S015", "S016", "C06", "C07"]:
		for pair in _spoken_pairs(scene_id):
			var speaker := str(pair[0])
			var text := str(pair[1])
			if speaker == "torren":
				_expect(text != "Maevra." and text != "Mae.", "%s advances Torren→Maevra address progression too early" % scene_id)
			if speaker == "maevra":
				if not (scene_id == "S014" and text == "Torren!"):
					_expect(text != "Torren." and text != "T.", "%s advances Maevra→Torren address progression too early" % scene_id)

func _last_flags(scene_id: String) -> Array:
	if not scenes.has(scene_id):
		return []
	var scene: DiyseDialogueSceneDefinition = scenes[scene_id]
	if scene.beats.is_empty():
		return []
	return _beat_flags(scene.beats[-1])

func _beat_flags(beat: Dictionary) -> Array:
	var cues = beat.get("cues", {})
	if not (cues is Dictionary):
		return []
	var flags = cues.get("implementation_flags", [])
	return flags if flags is Array else []

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

func _all_cues_text(scene_id: String) -> String:
	if not scenes.has(scene_id):
		return ""
	var result := ""
	for beat in (scenes[scene_id] as DiyseDialogueSceneDefinition).beats:
		var cues = beat.get("cues", {})
		if not (cues is Dictionary):
			continue
		for key in ["staging", "staging_after", "source_section", "source_speaker_label", "delivery"]:
			result += "\n" + str(cues.get(key, ""))
	return result

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Step 7C Chapter 2 continuity, prisoner-agency, Rhazek-limit, encounter-count, relationship, knowledge-firewall, Character-Life, and durable-handoff validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
