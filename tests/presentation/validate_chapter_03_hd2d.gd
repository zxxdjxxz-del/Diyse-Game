extends SceneTree

const PRESENTATION_DIR := "res://game/content/presentation/chapter_03/"
const DIALOGUE_DIR := "res://game/content/dialogue/current/chapter_03/"
const ScenePresentationDefinition = preload("res://game/presentation/scene_presentation_definition.gd")

var failures: Array[String] = []

const EXPECTED := {
	"B01": {"environment": "CH03_CAELORA", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B02": {"environment": "CH03_ROYAL_PALACE", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B03": {"environment": "CH03_ROYAL_PALACE", "background": "", "cutscene": "C2", "vfx": "V1", "encounter": "none"},
	"B04": {"environment": "CH03_ROYAL_PALACE", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B05": {"environment": "CH03_OLD_CITY_ARCHIVES", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B06": {"environment": "CH03_OLD_CITY_ARCHIVES", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B07": {"environment": "CH03_OLD_CITY_ARCHIVES", "background": "CH03_OLD_CITY_ARCHIVES", "cutscene": "C1", "vfx": "V1", "encounter": "random_allowed"},
	"B08": {"environment": "CH03_OLD_CITY_ARCHIVES", "background": "CH03_OLD_CITY_ARCHIVES", "cutscene": "C1", "vfx": "V1", "encounter": "random_allowed"},
	"B09": {"environment": "CH03_OLD_CITY_ARCHIVES", "background": "CH03_OLD_CITY_ARCHIVES", "cutscene": "C1", "vfx": "V1", "encounter": "random_allowed"},
	"B10": {"environment": "CH03_OLD_CITY_ARCHIVES", "background": "CH03_OLD_CITY_ARCHIVES", "cutscene": "C1", "vfx": "V1", "encounter": "random_allowed"},
	"B11": {"environment": "CH03_OLD_CITY_ARCHIVES", "background": "CH03_ARCHIVE_SCRIBE_ENGINE", "cutscene": "C2", "vfx": "V2", "encounter": "fixed_authored"},
	"B12": {"environment": "CH03_OLD_CITY_ARCHIVES", "background": "", "cutscene": "C2", "vfx": "V1", "encounter": "none"},
	"B13": {"environment": "CH03_ROYAL_PALACE", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B14": {"environment": "CH03_CRESTHAVEN", "background": "CH03_FIRST_COMMAND_WARDEN", "cutscene": "C2", "vfx": "V3", "encounter": "mixed"},
	"B15": {"environment": "CH03_CRESTHAVEN", "background": "", "cutscene": "C2", "vfx": "V1", "encounter": "none"},
	"C06": {"environment": "CH03_CRESTHAVEN", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
	"C07": {"environment": "CH03_CRESTHAVEN", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
}

func _initialize() -> void:
	_validate_scene_sidecars()
	_validate_environment_states()
	_validate_current_story_boundaries()
	_validate_legacy_layer_removed()
	_validate_no_enemy_or_elite_placement()
	_finish()

func _validate_scene_sidecars() -> void:
	for scene_id in EXPECTED.keys():
		var presentation = load(PRESENTATION_DIR + scene_id + ".tres")
		var dialogue = load(DIALOGUE_DIR + scene_id + ".tres")
		_expect(presentation != null, "%s current HD-2D presentation sidecar must load" % scene_id)
		_expect(dialogue != null, "%s current dialogue Resource must load" % scene_id)
		if presentation == null or dialogue == null:
			continue
		var schema_failures: Array[String] = presentation.validate_schema()
		_expect(schema_failures.is_empty(), "%s sidecar must validate: %s" % [scene_id, str(schema_failures)])
		var expected: Dictionary = EXPECTED[scene_id]
		_expect(str(presentation.scene_id) == scene_id, "%s presentation slot ID mismatch" % scene_id)
		_expect(str(presentation.chapter_id) == "chapter_03", "%s sidecar chapter mismatch" % scene_id)
		_expect(str(dialogue.chapter_id) == "chapter_03", "%s current dialogue chapter mismatch" % scene_id)
		_expect(str(dialogue.scene_id).begins_with("CH03_%s_" % scene_id), "%s presentation must pair with the current canonical dialogue scene" % scene_id)
		_expect(str(presentation.environment_family) == str(expected["environment"]), "%s environment family mismatch" % scene_id)
		_expect(str(presentation.battle_background_family) == str(expected["background"]), "%s battle-background family mismatch" % scene_id)
		_expect(str(presentation.cutscene_tier) == str(expected["cutscene"]), "%s cutscene tier mismatch" % scene_id)
		_expect(str(presentation.vfx_tier) == str(expected["vfx"]), "%s VFX tier mismatch" % scene_id)
		_expect(str(presentation.encounter_mode) == str(expected["encounter"]), "%s encounter-mode mismatch" % scene_id)
		_expect(presentation.has_tag("HD2D"), "%s must be marked HD2D" % scene_id)
		for tag in presentation.presentation_tags:
			_expect("ELITE" not in str(tag).to_upper(), "%s sidecar must not encode Elite placement: %s" % [scene_id, tag])

func _validate_environment_states() -> void:
	var expected_states := {
		"environment_caelora.tres": {"id": "CH03_CAELORA", "required": ["BASE", "ACTIVE", "POST_STORY"]},
		"environment_royal_palace.tres": {"id": "CH03_ROYAL_PALACE", "required": ["BASE", "ACTIVE", "POST_STORY"]},
		"environment_old_city_archives.tres": {"id": "CH03_OLD_CITY_ARCHIVES", "required": ["BASE", "ACTIVE", "OPEN", "POST_BOSS", "CLEARED", "POST_STORY"]},
		"environment_cresthaven.tres": {"id": "CH03_CRESTHAVEN", "required": ["BASE", "ESTABLISHMENT", "ACTIVE", "OPEN", "POST_BOSS", "CLEARED", "POST_STORY"]},
	}
	for filename in expected_states.keys():
		var definition = load(PRESENTATION_DIR + filename)
		_expect(definition != null, "%s environment-state Resource must load" % filename)
		if definition == null:
			continue
		var schema_failures: Array[String] = definition.validate_schema()
		_expect(schema_failures.is_empty(), "%s environment-state Resource must validate: %s" % [filename, str(schema_failures)])
		var expected: Dictionary = expected_states[filename]
		_expect(str(definition.environment_id) == str(expected["id"]), "%s environment ID mismatch" % filename)
		for required_state in expected["required"]:
			_expect(definition.allows_state(str(required_state)), "%s must expose state %s" % [filename, required_state])

func _validate_current_story_boundaries() -> void:
	var b01 = load(PRESENTATION_DIR + "B01.tres")
	var b02 = load(PRESENTATION_DIR + "B02.tres")
	var b03 = load(PRESENTATION_DIR + "B03.tres")
	var b06 = load(PRESENTATION_DIR + "B06.tres")
	var b08 = load(PRESENTATION_DIR + "B08.tres")
	var b11 = load(PRESENTATION_DIR + "B11.tres")
	var b12 = load(PRESENTATION_DIR + "B12.tres")
	var b14 = load(PRESENTATION_DIR + "B14.tres")
	var b15 = load(PRESENTATION_DIR + "B15.tres")
	var c06 = load(PRESENTATION_DIR + "C06.tres")
	var c07 = load(PRESENTATION_DIR + "C07.tres")
	_expect(str(b01.encounter_mode) == "none" and b01.has_tag("FUNCTIONING_CAPITAL"), "B01 Caelora arrival must remain non-hostile")
	_expect(b02.has_tag("NO_RETIRED_CH2_MURAL"), "B02 must not restore the retired Chapter-2 mural")
	_expect(b03.has_tag("CALDER_UNREVEALED") and b03.has_tag("NO_CARD_CLASSIFICATION"), "B03 must preserve the impossible-orders reveal firewall")
	_expect(b06.has_tag("NIMERA_PERMANENT_JOIN") and b06.has_tag("NO_ANCIENT_BARRIER"), "B06 must recruit Nimera without restoring the Ancient Barrier")
	_expect(b08.has_tag("PRIME_TERM_UNDEFINED") and b08.has_tag("NO_CARD_PRIME_CLASSIFICATION"), "B08 may establish the Ancient Prime term without classifying Cyanis's Card")
	_expect(str(b11.encounter_mode) == "fixed_authored" and b11.has_tag("ARCHIVE_SCRIBE_ENGINE_BOSS"), "B11 must be the mandatory Archive Scribe Engine boss")
	_expect(b11.has_tag("NO_FIRST_COMMAND_WARDEN") and b11.has_tag("NO_RUBY_STABILIZATION"), "B11 must not inherit the retired Caelora Warden/Ruby sequence")
	_expect(b12.has_tag("WESTWAYS_RECORDBOOK") and b12.has_tag("WAYFINDER_HAND_COPY"), "B12 must preserve the current recordbook/Wayfinder-copy provenance")
	_expect(str(b14.encounter_mode) == "mixed" and b14.has_tag("FIRST_COMMAND_WARDEN"), "B14 must own the Cresthaven tower-base traversal and First Command Warden")
	_expect(b14.has_tag("PREVIOUS_ERROR_THEN_LAST_SENTINEL_CONFIRMED") and b14.has_tag("LAST_SENTINEL_CONFIRMED_FINAL_MESSAGE"), "B14 must preserve the Warden shutdown message order")
	_expect(b14.has_tag("RUBY_AFTER_WARDEN_INERT") and b14.has_tag("NO_PRIME_MANIFESTATION"), "B14 Ruby stabilization must occur only after the inert Warden and without Prime manifestation")
	_expect(b15.has_tag("CRESTHAVEN_HEADQUARTERS") and b15.has_tag("IVORYBRIDGE_HYPOTHESIS"), "B15 must establish headquarters and keep Ivorybridge as a hypothesis")
	_expect(b15.has_tag("NO_PRIME_MANIFESTATION"), "B15 must not manifest Last Sentinel")
	for scene in [c06, c07]:
		_expect(str(scene.environment_family) == "CH03_CRESTHAVEN", "Chapter-3 Character-Life scenes must occur during Cresthaven cleanup")

func _validate_legacy_layer_removed() -> void:
	for legacy_scene in ["S017", "S018", "S019", "S020", "S021", "H01", "H02", "H03", "H04"]:
		_expect(not ResourceLoader.exists(PRESENTATION_DIR + legacy_scene + ".tres"), "Legacy Chapter-3 presentation sidecar must be removed: %s" % legacy_scene)
	for legacy_environment in [
		"environment_caelora_civic_judicial.tres",
		"environment_old_city_suppressed_archives.tres",
		"environment_deep_command_station.tres",
		"environment_cresthaven_state_1.tres",
	]:
		_expect(not ResourceLoader.exists(PRESENTATION_DIR + legacy_environment), "Retired Chapter-3 environment presentation must be removed: %s" % legacy_environment)

func _validate_no_enemy_or_elite_placement() -> void:
	var definition = ScenePresentationDefinition.new()
	var property_names: Array[String] = []
	for property in definition.get_property_list():
		property_names.append(str(property.get("name", "")))
	for forbidden in ["enemy_id", "enemy_ids", "elite_id", "elite_ids", "encounter_table", "enemy_roster", "enemy_placement", "elite_placement"]:
		_expect(forbidden not in property_names, "Scene presentation sidecars must not own enemy/Elite placement field: %s" % forbidden)

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Chapter 3 current B01-B15 HD-2D presentation validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
