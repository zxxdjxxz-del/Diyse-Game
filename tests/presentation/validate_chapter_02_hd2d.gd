extends SceneTree

const PRESENTATION_DIR := "res://game/content/presentation/chapter_02/"
const DIALOGUE_DIR := "res://game/content/dialogue/chapter_02/"
const ScenePresentationDefinition = preload("res://game/presentation/scene_presentation_definition.gd")

var failures: Array[String] = []

const EXPECTED := {
	"S012": {"environment": "CH02_DUNMERE_WATERWORKS", "background": "", "cutscene": "C2", "vfx": "V1", "encounter": "none"},
	"S013": {"environment": "CH02_SUNKEN_ARCHIVE", "background": "CH02_SUNKEN_ARCHIVE", "cutscene": "C2", "vfx": "V2", "encounter": "mixed"},
	"S014": {"environment": "CH02_PRISONER_TRANSFER_SERVICE", "background": "CH02_PRISONER_TRANSFER_SERVICE", "cutscene": "C2", "vfx": "V1", "encounter": "mixed"},
	"S015": {"environment": "CH02_RED_TRANSFER_BASTION", "background": "CH02_RED_TRANSFER_BASTION", "cutscene": "C2", "vfx": "V2", "encounter": "mixed"},
	"S016": {"environment": "CH02_EXTRACTION_CAUSEWAY", "background": "CH02_EXTRACTION_CAUSEWAY", "cutscene": "C1", "vfx": "V1", "encounter": "fixed_authored"},
	"C06": {"environment": "CH02_DUNMERE_WATERWORKS", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
	"C07": {"environment": "CH02_DUNMERE_WATERWORKS", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
}

func _initialize() -> void:
	_validate_scene_sidecars()
	_validate_environment_states()
	_validate_encounter_boundaries()
	_validate_no_enemy_or_elite_placement()
	_finish()

func _validate_scene_sidecars() -> void:
	for scene_id in EXPECTED.keys():
		var presentation = load(PRESENTATION_DIR + scene_id + ".tres")
		var dialogue = load(DIALOGUE_DIR + scene_id + ".tres")
		_expect(presentation != null, "%s HD-2D presentation sidecar must load" % scene_id)
		_expect(dialogue != null, "%s closed dialogue Resource must still load" % scene_id)
		if presentation == null:
			continue
		var schema_failures: Array[String] = presentation.validate_schema()
		_expect(schema_failures.is_empty(), "%s sidecar must validate: %s" % [scene_id, str(schema_failures)])
		var expected: Dictionary = EXPECTED[scene_id]
		_expect(str(presentation.scene_id) == scene_id, "%s sidecar scene ID mismatch" % scene_id)
		_expect(str(presentation.chapter_id) == "chapter_02", "%s sidecar chapter mismatch" % scene_id)
		_expect(str(presentation.environment_family) == str(expected["environment"]), "%s environment family mismatch" % scene_id)
		_expect(str(presentation.battle_background_family) == str(expected["background"]), "%s battle-background family mismatch" % scene_id)
		_expect(str(presentation.cutscene_tier) == str(expected["cutscene"]), "%s cutscene tier mismatch" % scene_id)
		_expect(str(presentation.vfx_tier) == str(expected["vfx"]), "%s VFX tier mismatch" % scene_id)
		_expect(str(presentation.encounter_mode) == str(expected["encounter"]), "%s encounter-mode mismatch" % scene_id)
		_expect(presentation.has_tag("HD2D"), "%s must be marked HD2D" % scene_id)
		for tag in presentation.presentation_tags:
			_expect("ELITE" not in str(tag).to_upper(), "%s sidecar must not encode Elite placement through tag: %s" % [scene_id, tag])

func _validate_environment_states() -> void:
	var expected_states := {
		"environment_dunmere_waterworks.tres": {"id": "CH02_DUNMERE_WATERWORKS", "required": ["BASE", "ACTIVE", "CLOSED", "CLEARED", "POST_STORY"]},
		"environment_sunken_archive.tres": {"id": "CH02_SUNKEN_ARCHIVE", "required": ["BASE", "ACTIVE", "OPEN", "POST_BOSS", "CLEARED"]},
		"environment_prisoner_transfer_service.tres": {"id": "CH02_PRISONER_TRANSFER_SERVICE", "required": ["BASE", "ACTIVE", "OPEN", "CLEARED", "POST_STORY"]},
		"environment_red_transfer_bastion.tres": {"id": "CH02_RED_TRANSFER_BASTION", "required": ["BASE", "ACTIVE", "INACTIVE", "POST_BOSS", "CLEARED"]},
		"environment_extraction_causeway.tres": {"id": "CH02_EXTRACTION_CAUSEWAY", "required": ["BASE", "ACTIVE", "OPEN", "CLEARED", "POST_STORY"]},
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

func _validate_encounter_boundaries() -> void:
	var s012 = load(PRESENTATION_DIR + "S012.tres")
	var s013 = load(PRESENTATION_DIR + "S013.tres")
	var s014 = load(PRESENTATION_DIR + "S014.tres")
	var s015 = load(PRESENTATION_DIR + "S015.tres")
	var s016 = load(PRESENTATION_DIR + "S016.tres")
	_expect(str(s012.encounter_mode) == "none" and s012.has_tag("NO_RANDOM"), "S012 must remain investigation-focused without random combat pressure")
	_expect(str(s013.encounter_mode) == "mixed", "S013 must support random Archive traversal plus authored encounters")
	_expect(str(s014.encounter_mode) == "mixed", "S014 must support random transfer traversal plus fixed gate combat")
	_expect(str(s015.encounter_mode) == "mixed", "S015 must support hostile Bastion traversal plus Rhazek")
	_expect(str(s016.encounter_mode) == "fixed_authored" and s016.has_tag("NO_RANDOM"), "S016 must suppress random encounters and retain Hold the Junction as the sole mandatory fight")

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
		print("Diyse Audit88 Chapter 2 HD-2D presentation resource validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
