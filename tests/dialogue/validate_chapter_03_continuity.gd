extends SceneTree

const CURRENT_DIR := "res://game/content/dialogue/current/chapter_03/"

var failures: Array[String] = []
var scenes: Dictionary = {}

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	for scene_id in ["B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B09", "B10", "B11", "C06", "C07"]:
		var scene := load(CURRENT_DIR + scene_id + ".tres") as DiyseDialogueSceneDefinition
		_expect(scene != null, "%s must load for current Chapter 3 continuity validation" % scene_id)
		if scene != null:
			scenes[scene_id] = scene

	_validate_b05()
	_validate_b06()
	_validate_b07()
	_validate_b08()
	_validate_b09()
	_validate_b10()
	_validate_b11()
	_validate_cleanup_scenes()
	_finish()

func _validate_b05() -> void:
	var scene := _scene("B05")
	if scene == null:
		return
	_expect("nimera" in scene.participants, "B05 must include Nimera")
	_expect(_last_flags("B05").has("ROSTER_ADD_NIMERA_PERMANENT"), "B05 must permanently add Nimera")
	_expect("ancient barrier" not in _spoken("B05"), "B05 must not restore the Ancient Barrier")

func _validate_b06() -> void:
	var spoken := _spoken("B06")
	_expect("prime card" in spoken, "B06 must preserve the historical Prime Card term")
	for forbidden in ["cyanis's card is a prime", "the card is a prime", "face: might", "last sentinel confirmed"]:
		_expect(forbidden not in spoken, "B06 resolves protected knowledge too early: %s" % forbidden)

func _validate_b07() -> void:
	var spoken := _spoken("B07")
	for forbidden in ["last sentinel", "previous error", "deep ruby"]:
		_expect(forbidden not in spoken, "B07 Memory Construct sequence leaked later Cresthaven reveal: %s" % forbidden)

func _validate_b08() -> void:
	var spoken := _spoken("B08")
	_expect("westways" in spoken and "wayfinder" in spoken, "B08 must preserve the Westways/Wayfinder evidence")
	_expect("cresthaven" not in spoken, "B08 must not identify the northern tower as Cresthaven")
	_expect("ivorybridge" not in spoken, "B08 Ancient/copied evidence must not name Ivorybridge")

func _validate_b09() -> void:
	var spoken := _spoken("B09")
	_expect("that's cresthaven." in spoken, "B09 must let Mirena identify Cresthaven")
	_expect("after everyone sleeps." in spoken, "B09 must preserve the offscreen-rest instruction")

func _validate_b10() -> void:
	var scene := _scene("B10")
	if scene == null:
		return
	var previous_error := -1
	var last_sentinel := -1
	var first_ruby := -1
	var authority_lines: Array[String] = []
	for i in range(scene.beats.size()):
		var beat: Dictionary = scene.beats[i]
		var text := _normalize(str(beat.get("text", "")))
		var speaker := str(beat.get("speaker_id", ""))
		if text == "previous error":
			previous_error = i
		if text == "last sentinel confirmed":
			last_sentinel = i
		if "ruby" in text and first_ruby < 0:
			first_ruby = i
		if speaker == "authority_construct":
			authority_lines.append(text)

	_expect(previous_error >= 0, "B10 must contain PREVIOUS ERROR")
	_expect(last_sentinel > previous_error, "B10 must place LAST SENTINEL CONFIRMED after PREVIOUS ERROR")
	_expect(not authority_lines.is_empty() and authority_lines[-1] == "last sentinel confirmed", "LAST SENTINEL CONFIRMED must be the Authority Construct's final spoken message")
	_expect(first_ruby > last_sentinel, "B10 Ruby response must occur only after the Authority Construct's final message")
	_expect("prime manifestation" not in _spoken("B10"), "B10 must not claim a Prime manifestation")

func _validate_b11() -> void:
	var spoken := _spoken("B11")
	_expect("ivorybridge" in spoken, "B11 must choose Ivorybridge as the next practical lead")
	_expect("ivorybridge isn't on that map." in spoken, "B11 must preserve the firewall that Ivorybridge is not on the copied map")
	var flags := _last_flags("B11")
	for required in ["STORY_CHAPTER_03_COMPLETE", "UNLOCK_C06_NIMERA_TAKES_OVER_A_TABLE", "UNLOCK_C07_ILYRA_AND_NIMERA"]:
		_expect(flags.has(required), "B11 lost durable Chapter 3 handoff: %s" % required)

func _validate_cleanup_scenes() -> void:
	for id in ["C06", "C07"]:
		var scene := _scene(id)
		if scene != null:
			_expect(scene.scene_kind == "character_life", "%s must remain Character-Life" % id)

func _scene(id: String) -> DiyseDialogueSceneDefinition:
	return scenes.get(id) as DiyseDialogueSceneDefinition if scenes.has(id) else null

func _spoken(id: String) -> String:
	var scene := _scene(id)
	if scene == null:
		return ""
	var result := ""
	for beat in scene.beats:
		if not str(beat.get("speaker_id", "")).is_empty():
			result += _normalize(str(beat.get("text", ""))) + "\n"
	return result

func _normalize(value: String) -> String:
	return value.to_lower().replace("’", "'").replace("‘", "'").replace("“", "\"").replace("”", "\"").strip_edges()

func _beat_flags(beat: Dictionary) -> Array:
	var cues = beat.get("cues", {})
	if not (cues is Dictionary):
		return []
	var flags = cues.get("implementation_flags", [])
	return flags if flags is Array else []

func _last_flags(id: String) -> Array:
	var scene := _scene(id)
	if scene == null or scene.beats.is_empty():
		return []
	return _beat_flags(scene.beats[-1])

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse current Chapter 3 B01-B11 continuity and reveal-firewall validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
