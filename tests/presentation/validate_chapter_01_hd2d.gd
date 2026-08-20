extends SceneTree

const PRESENTATION_DIR := "res://game/content/presentation/chapter_01/"
const DIALOGUE_DIR := "res://game/content/dialogue/chapter_01/"
const ScenePresentationDefinition = preload("res://game/presentation/scene_presentation_definition.gd")

var failures: Array[String] = []

const EXPECTED := {
	"S007": {"environment": "CH01_EDGELANDS_SETTLEMENT", "background": "CH01_WOODED_EDGELANDS_ROAD", "cutscene": "C1", "vfx": "V1", "encounter": "random_allowed"},
	"S008": {"environment": "CH01_HOLLOW_WATCH", "background": "CH01_HOLLOW_WATCH", "cutscene": "C2", "vfx": "V2", "encounter": "mixed"},
	"S009": {"environment": "CH01_EDGELANDS_SETTLEMENT", "background": "CH01_LOWER_WOODS", "cutscene": "C1", "vfx": "V1", "encounter": "mixed"},
	"S010": {"environment": "CH01_WOODED_ROUTE", "background": "CH01_BRIAR_PASSAGE", "cutscene": "C1", "vfx": "V1", "encounter": "random_allowed"},
	"S011": {"environment": "CH01_ANCIENT_ROUTE_WAYFINDER", "background": "", "cutscene": "C2", "vfx": "V1", "encounter": "none"},
	"C03": {"environment": "CH01_WOODED_ROUTE", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
	"C04": {"environment": "CH01_EDGELANDS_SETTLEMENT", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
	"C05": {"environment": "CH01_EDGELANDS_SETTLEMENT", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
}

func _initialize() -> void:
	_validate_scene_sidecars()
	_validate_environment_states()
	_validate_random_encounter_boundary()
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
		_expect(str(presentation.chapter_id) == "chapter_01", "%s sidecar chapter mismatch" % scene_id)
		_expect(str(presentation.environment_family) == str(expected["environment"]), "%s environment family mismatch" % scene_id)
		_expect(str(presentation.battle_background_family) == str(expected["background"]), "%s battle-background family mismatch" % scene_id)
		_expect(str(presentation.cutscene_tier) == str(expected["cutscene"]), "%s cutscene tier mismatch" % scene_id)
		_expect(str(presentation.vfx_tier) == str(expected["vfx"]), "%s VFX tier mismatch" % scene_id)
		_expect(str(presentation.encounter_mode) == str(expected["encounter"]), "%s encounter-mode mismatch" % scene_id)
		_expect(presentation.has_tag("HD2D"), "%s must be marked HD2D" % scene_id)
		for tag in presentation.presentation_tags:
			_expect("ELITE" not in str(tag).to_upper(), "%s sidecar must not encode Elite placement through presentation tags: %s" % [scene_id, tag])

func _validate_environment_states() -> void:
	var expected_states := {
		"environment_edgelands_settlement.tres": {"id": "CH01_EDGELANDS_SETTLEMENT", "required": ["BASE", "ACTIVE", "POST_STORY"]},
		"environment_wooded_route.tres": {"id": "CH01_WOODED_ROUTE", "required": ["BASE", "ACTIVE", "CLEARED", "POST_STORY"]},
		"environment_hollow_watch.tres": {"id": "CH01_HOLLOW_WATCH", "required": ["BASE", "ACTIVE", "OPEN", "POST_BOSS", "CLEARED"]},
		"environment_ancient_route_wayfinder.tres": {"id": "CH01_ANCIENT_ROUTE_WAYFINDER", "required": ["BASE", "ACTIVE", "POST_STORY"]},
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

func _validate_random_encounter_boundary() -> void:
	var s007 = load(PRESENTATION_DIR + "S007.tres")
	var s008 = load(PRESENTATION_DIR + "S008.tres")
	var s009 = load(PRESENTATION_DIR + "S009.tres")
	var s010 = load(PRESENTATION_DIR + "S010.tres")
	var s011 = load(PRESENTATION_DIR + "S011.tres")
	_expect(s007.has_tag("RANDOM_START_AFTER_EAST_GATE"), "S007 must establish normal random encounters only after Brackenwall east gate")
	_expect(str(s008.encounter_mode) == "mixed", "S008 must support hostile random traversal plus authored Castellan combat")
	_expect(str(s009.encounter_mode) == "mixed", "S009 must support random Lower Woods traversal plus authored nonlethal Briarhide encounter")
	_expect(str(s010.encounter_mode) == "random_allowed", "S010 must retain random hostile Briar Passage traversal")
	_expect(str(s011.encounter_mode) == "none" and s011.has_tag("NO_RANDOM"), "Wayfinder story pocket must suppress random encounters")

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
		print("Diyse Audit88 Chapter 1 HD-2D presentation resource validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
