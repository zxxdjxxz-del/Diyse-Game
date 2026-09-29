extends SceneTree

const SCENE_PATHS := {
	"B01": "res://game/content/dialogue/current/chapter_01/B01.tres",
	"B02": "res://game/content/dialogue/current/chapter_01/B02.tres",
	"B03": "res://game/content/dialogue/current/chapter_01/B03.tres",
	"B04": "res://game/content/dialogue/current/chapter_01/B04.tres",
	"B05": "res://game/content/dialogue/current/chapter_01/B05.tres",
	"B06": "res://game/content/dialogue/current/chapter_01/B06.tres",
	"B07": "res://game/content/dialogue/current/chapter_01/B07.tres",
	"B08": "res://game/content/dialogue/current/chapter_01/B08.tres",
	"B09": "res://game/content/dialogue/current/chapter_01/B09.tres",
	"B10": "res://game/content/dialogue/current/chapter_01/B10.tres",
	"B11": "res://game/content/dialogue/current/chapter_01/B11.tres",
	"B12": "res://game/content/dialogue/current/chapter_01/B12.tres",
	"C02": "res://game/content/dialogue/current/chapter_01/C02.tres",
	"C03": "res://game/content/dialogue/current/chapter_01/C03.tres",
	"C04": "res://game/content/dialogue/current/chapter_01/C04.tres",
}

const B10_SOURCE := "res://docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CH01_B10_THORNHIDE_DIALOGUE.md"
const B11_SOURCE := "res://docs/03_DIALOGUE/PRODUCTION/CHAPTER_01/CH01_B11_THE_JUNCTION_HIDDEN_MONUMENT_DIALOGUE.md"

var failures: Array[String] = []
var scenes: Dictionary = {}

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	for scene_id in SCENE_PATHS:
		var scene := load(str(SCENE_PATHS[scene_id])) as DiyseDialogueSceneDefinition
		_expect(scene != null, "%s current Chapter 1 Resource must load" % scene_id)
		if scene != null:
			scenes[scene_id] = scene

	_validate_current_structure()
	_validate_party_and_handoffs()
	_validate_retired_structure_firewall()
	_validate_knowledge_firewall()
	_validate_wayfinder_faces()
	_validate_thornhide_stalker()
	_validate_character_life()
	_finish()

func _validate_current_structure() -> void:
	for beat_number in range(1, 13):
		var scene_id := "B%02d" % beat_number
		_expect(scenes.has(scene_id), "Missing current mandatory scene %s" % scene_id)
		if not scenes.has(scene_id):
			continue
		var scene: DiyseDialogueSceneDefinition = scenes[scene_id]
		_expect(scene.scene_kind == "mandatory", "%s must remain mandatory" % scene_id)
		_expect(scene.chapter_id == "chapter_01", "%s must remain chapter_01" % scene_id)

	for optional_id in ["C02", "C03", "C04"]:
		_expect(scenes.has(optional_id), "Missing current Character-Life scene %s" % optional_id)
		if scenes.has(optional_id):
			_expect((scenes[optional_id] as DiyseDialogueSceneDefinition).scene_kind == "character_life", "%s must remain Character-Life" % optional_id)

	_expect(scenes.size() == 15, "Current Chapter 1 runtime set must contain exactly B01-B12 plus C02-C04")

	if scenes.has("B10"):
		var b10: DiyseDialogueSceneDefinition = scenes["B10"]
		_expect(b10.scene_id == "CH01_B10_THORNHIDE", "B10 technical scene_id must remain filename-aligned")
		_expect(b10.story_position.contains("Thornhide Stalker"), "B10 story position must use Thornhide Stalker")

func _validate_party_and_handoffs() -> void:
	if scenes.has("B01"):
		for required in ["cyanis", "ilyra", "maevra"]:
			_expect(required in (scenes["B01"] as DiyseDialogueSceneDefinition).participants, "B01 missing required participant: %s" % required)

	for scene_id in ["B03", "B04", "B05", "B06", "B07", "B08", "B09", "B10", "B11", "B12"]:
		if scenes.has(scene_id):
			_expect("torren" in (scenes[scene_id] as DiyseDialogueSceneDefinition).participants, "%s must include Torren" % scene_id)

	var b08_flags := _all_flags("B08")
	_expect("ROSTER_ADD_TORREN_PERMANENT" in b08_flags, "B08 lost Torren permanent-roster handoff")

	var b12_flags := _all_flags("B12")
	for required in [
		"STORY_CHAPTER_01_COMPLETE",
		"UNLOCK_C02_TORRENS_VERSION_OF_DINNER",
		"UNLOCK_C03_WHAT_THE_MAP_SAYS",
		"UNLOCK_C04_NOT_PROFESSIONALLY",
	]:
		_expect(required in b12_flags, "B12 lost current Chapter 1 handoff: %s" % required)

	for flag in b12_flags:
		var upper_flag := str(flag).to_upper()
		_expect("C05" not in upper_flag, "B12 must not restore retired Chapter-1 C05 numbering")
		_expect("HUNT" not in upper_flag and "CISTERN" not in upper_flag, "B12 must not unlock retired Chapter-1 Hunt content: %s" % flag)

func _validate_retired_structure_firewall() -> void:
	var active_text := ""
	for scene_id in scenes:
		active_text += "\n" + _spoken_text(scene_id)
		active_text += "\n" + _cue_text(scene_id)

	var lower := active_text.to_lower()
	for retired in [
		"watch castellan",
		"cistern devourer",
		"briarhide",
		"six-channel junction",
		"six channels",
		"forced inner",
	]:
		_expect(retired not in lower, "Current Chapter 1 runtime restored retired structure/name: %s" % retired)

func _validate_knowledge_firewall() -> void:
	var mandatory_spoken := ""
	for beat_number in range(1, 13):
		mandatory_spoken += "\n" + _spoken_text("B%02d" % beat_number).to_lower()

	for forbidden in ["last sentinel", "prime card", "nimera", "vaelira", "seyrik", "the entity"]:
		_expect(forbidden not in mandatory_spoken, "Chapter 1 leaked later-story knowledge into mandatory dialogue: %s" % forbidden)

func _validate_wayfinder_faces() -> void:
	_expect(FileAccess.file_exists(B11_SOURCE), "Current B11 production source must exist")
	if not FileAccess.file_exists(B11_SOURCE):
		return

	var source := FileAccess.get_file_as_string(B11_SOURCE)
	_expect(source.contains("Might. Elements. Grace. Memory. Perception. Ruin."), "B11 must preserve the current six Face markings")
	_expect("Acuity" not in source, "B11 must not restore retired Acuity Face terminology")
	_expect("Resource" not in source, "B11 must not restore retired Resource Face terminology")

func _validate_thornhide_stalker() -> void:
	_expect(FileAccess.file_exists(B10_SOURCE), "Current B10 production source must exist")
	if not FileAccess.file_exists(B10_SOURCE):
		return

	var source := FileAccess.get_file_as_string(B10_SOURCE)
	_expect(source.contains("# Thornhide Stalker"), "B10 source must identify the boss as Thornhide Stalker")
	_expect(source.contains("**BOSS BATTLE — THORNHIDE STALKER**"), "B10 boss marker must use Thornhide Stalker")
	_expect(source.contains("**Cyanis + Ilyra + Torren**"), "B10 must preserve the three-person combat party")
	_expect(source.contains("Maevra remains with the traveling group but does not participate in combat."), "B10 must keep Maevra noncombat")
	_expect(source.contains("no dialogue during active combat"), "B10 must preserve the no-mid-battle-dialogue rule")
	_expect("nonlethal or drive-off resolution" in source, "B10 must retain the explicit retired nonlethal firewall")

func _validate_character_life() -> void:
	_expect(_same_members(_participants("C02"), ["cyanis", "ilyra", "torren", "maevra"]), "C02 participant set drifted")
	_expect(_same_members(_participants("C03"), ["cyanis", "torren"]), "C03 participant set drifted")
	_expect(_same_members(_participants("C04"), ["ilyra", "maevra"]), "C04 participant set drifted")

	var c04 := _spoken_text("C04").to_lower()
	for forbidden in ["twenty-five", "25 years", "lovers", "we were together"]:
		_expect(forbidden not in c04, "C04 exceeded the Chapter-1 Maevra/Torren reveal gate: %s" % forbidden)

func _participants(scene_id: String) -> Array:
	if not scenes.has(scene_id):
		return []
	return (scenes[scene_id] as DiyseDialogueSceneDefinition).participants

func _same_members(actual: Array, expected: Array) -> bool:
	if actual.size() != expected.size():
		return false
	for item in expected:
		if item not in actual:
			return false
	return true

func _all_flags(scene_id: String) -> Array[String]:
	var result: Array[String] = []
	if not scenes.has(scene_id):
		return result

	for beat in (scenes[scene_id] as DiyseDialogueSceneDefinition).beats:
		var cues = beat.get("cues", {})
		if not (cues is Dictionary):
			continue
		var flags = cues.get("implementation_flags", [])
		if not (flags is Array):
			continue
		for flag in flags:
			var flag_text := str(flag)
			if flag_text not in result:
				result.append(flag_text)
	return result

func _spoken_text(scene_id: String) -> String:
	if not scenes.has(scene_id):
		return ""
	var result := ""
	for beat in (scenes[scene_id] as DiyseDialogueSceneDefinition).beats:
		if not str(beat.get("speaker_id", "")).is_empty():
			result += str(beat.get("text", "")) + "\n"
	return result

func _cue_text(scene_id: String) -> String:
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
		print("Diyse Chapter 1 current 12-beat continuity / retirement / Face / Character-Life validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
