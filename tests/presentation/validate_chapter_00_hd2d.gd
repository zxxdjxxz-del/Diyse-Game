extends SceneTree

const PRESENTATION_DIR := "res://game/content/presentation/chapter_00/"
const DIALOGUE_DIR := "res://game/content/dialogue/chapter_00/"
const ScenePresentationDefinition = preload("res://game/presentation/scene_presentation_definition.gd")

var failures: Array[String] = []

const EXPECTED := {
	"S001": {"environment": "CH00_CONVOY_ROAD", "background": "CH00_CONVOY_ROAD", "cutscene": "C1", "vfx": "V1", "encounter": "fixed_authored"},
	"S002": {"environment": "CH00_WRECK_FIELD", "background": "CH00_WRECK_FIELD", "cutscene": "C1", "vfx": "V1", "encounter": "fixed_authored"},
	"S003": {"environment": "CH00_RECOVERY_LINE", "background": "CH00_RECOVERY_LINE", "cutscene": "C1", "vfx": "V1", "encounter": "fixed_authored"},
	"S004": {"environment": "CH00_TRIAGE_SAFE_CAMP", "background": "", "cutscene": "C2", "vfx": "V2", "encounter": "none"},
	"S005": {"environment": "CH00_RECOVERY_LINE", "background": "CH00_RECOVERY_LINE", "cutscene": "C2", "vfx": "V2", "encounter": "fixed_authored"},
	"S006": {"environment": "CH00_RECOVERY_LINE", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"C01": {"environment": "CH00_TRIAGE_SAFE_CAMP", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
	"C02": {"environment": "CH00_TRIAGE_SAFE_CAMP", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
}

func _initialize() -> void:
	_validate_scene_sidecars()
	_validate_environment_states()
	_validate_no_enemy_or_elite_placement_fields()
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
		_expect(schema_failures.is_empty(), "%s presentation sidecar must pass schema validation: %s" % [scene_id, str(schema_failures)])
		_expect(str(presentation.scene_id) == scene_id, "%s presentation sidecar must target the matching closed scene" % scene_id)
		_expect(str(presentation.chapter_id) == "chapter_00", "%s sidecar must remain in Chapter 0" % scene_id)
		var expected: Dictionary = EXPECTED[scene_id]
		_expect(str(presentation.environment_family) == str(expected["environment"]), "%s environment family mismatch" % scene_id)
		_expect(str(presentation.battle_background_family) == str(expected["background"]), "%s battle-background family mismatch" % scene_id)
		_expect(str(presentation.cutscene_tier) == str(expected["cutscene"]), "%s cutscene tier mismatch" % scene_id)
		_expect(str(presentation.vfx_tier) == str(expected["vfx"]), "%s VFX tier mismatch" % scene_id)
		_expect(str(presentation.encounter_mode) == str(expected["encounter"]), "%s encounter-mode mismatch" % scene_id)
		_expect(presentation.has_tag("HD2D"), "%s must be explicitly marked as HD-2D presentation authority" % scene_id)
		_expect(presentation.has_tag("NO_RANDOM"), "%s must preserve Chapter 0's no-random-encounter rule" % scene_id)

func _validate_environment_states() -> void:
	var expected_states := {
		"environment_convoy_road.tres": {"id": "CH00_CONVOY_ROAD", "initial": "BASE", "required": ["BASE", "DAMAGED", "POST_STORY"]},
		"environment_wreck_field.tres": {"id": "CH00_WRECK_FIELD", "initial": "DAMAGED", "required": ["BASE", "DAMAGED", "CLEARED", "POST_STORY"]},
		"environment_recovery_line.tres": {"id": "CH00_RECOVERY_LINE", "initial": "DAMAGED", "required": ["BASE", "DAMAGED", "POST_BOSS", "CLEARED"]},
		"environment_triage_safe_camp.tres": {"id": "CH00_TRIAGE_SAFE_CAMP", "initial": "ACTIVE", "required": ["BASE", "ACTIVE", "POST_STORY"]},
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
		_expect(str(definition.initial_state) == str(expected["initial"]), "%s initial environment state mismatch" % filename)
		for required_state in expected["required"]:
			_expect(definition.allows_state(str(required_state)), "%s must expose authored state %s" % [filename, required_state])

func _validate_no_enemy_or_elite_placement_fields() -> void:
	var definition = ScenePresentationDefinition.new()
	var property_names: Array[String] = []
	for property in definition.get_property_list():
		property_names.append(str(property.get("name", "")))
	for forbidden in ["enemy_id", "enemy_ids", "elite_id", "elite_ids", "encounter_table", "enemy_roster", "enemy_placement"]:
		_expect(forbidden not in property_names, "Scene presentation sidecars must not lock enemy/Elite placement field: %s" % forbidden)

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Audit88 Chapter 0 HD-2D presentation resource validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
