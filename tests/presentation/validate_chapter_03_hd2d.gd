extends SceneTree

const PRESENTATION_DIR := "res://game/content/presentation/chapter_03/"
const DIALOGUE_DIR := "res://game/content/dialogue/chapter_03/"
const ScenePresentationDefinition = preload("res://game/presentation/scene_presentation_definition.gd")

var failures: Array[String] = []

const EXPECTED := {
	"S017": {"environment": "CH03_CAELORA_CIVIC_JUDICIAL", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"S018": {"environment": "CH03_CAELORA_CIVIC_JUDICIAL", "background": "CH03_JUDICIAL_CAUSEWAY", "cutscene": "C1", "vfx": "V1", "encounter": "fixed_authored"},
	"S019": {"environment": "CH03_OLD_CITY_SUPPRESSED_ARCHIVES", "background": "CH03_SUPPRESSED_ARCHIVE", "cutscene": "C2", "vfx": "V2", "encounter": "mixed"},
	"S020": {"environment": "CH03_DEEP_COMMAND_STATION", "background": "CH03_FIRST_COMMAND_WARDEN", "cutscene": "C2", "vfx": "V3", "encounter": "mixed"},
	"S021": {"environment": "CH03_CRESTHAVEN_STATE_1", "background": "", "cutscene": "C2", "vfx": "V1", "encounter": "none"},
	"H01": {"environment": "CH03_CRESTHAVEN_STATE_1", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
	"H02": {"environment": "CH03_CRESTHAVEN_STATE_1", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
	"H03": {"environment": "CH03_CRESTHAVEN_STATE_1", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
	"H04": {"environment": "CH03_CRESTHAVEN_STATE_1", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
}

func _initialize() -> void:
	_validate_scene_sidecars()
	_validate_environment_states()
	_validate_chapter_03_firewalls()
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
		_expect(str(presentation.chapter_id) == "chapter_03", "%s sidecar chapter mismatch" % scene_id)
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
		"environment_caelora_civic_judicial.tres": {"id": "CH03_CAELORA_CIVIC_JUDICIAL", "required": ["BASE", "ACTIVE", "POST_STORY"]},
		"environment_old_city_suppressed_archives.tres": {"id": "CH03_OLD_CITY_SUPPRESSED_ARCHIVES", "required": ["BASE", "ACTIVE", "OPEN", "CLEARED", "POST_STORY"]},
		"environment_deep_command_station.tres": {"id": "CH03_DEEP_COMMAND_STATION", "required": ["BASE", "ACTIVE", "OPEN", "POST_BOSS", "CLEARED"]},
		"environment_cresthaven_state_1.tres": {"id": "CH03_CRESTHAVEN_STATE_1", "required": ["BASE", "ESTABLISHMENT", "ACTIVE", "POST_STORY"]},
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

func _validate_chapter_03_firewalls() -> void:
	var s017 = load(PRESENTATION_DIR + "S017.tres")
	var s018 = load(PRESENTATION_DIR + "S018.tres")
	var s019 = load(PRESENTATION_DIR + "S019.tres")
	var s020 = load(PRESENTATION_DIR + "S020.tres")
	var s021 = load(PRESENTATION_DIR + "S021.tres")
	var h04 = load(PRESENTATION_DIR + "H04.tres")
	_expect(str(s017.encounter_mode) == "none" and s017.has_tag("NO_RANDOM"), "S017 must remain civic/procedural with no random combat")
	_expect(str(s018.encounter_mode) == "fixed_authored" and s018.has_tag("EXACTLY_TWO_AUTHORITY_ENCOUNTERS"), "S018 must preserve exactly two authored authority encounters")
	_expect(s018.has_tag("NONLETHAL_AUTHORITY_RESOLUTION"), "S018 authority combat must use nonlethal presentation")
	_expect(str(s019.encounter_mode) == "mixed" and s019.has_tag("CHOOSE_FOUR_UNLOCK"), "S019 must support Archive traversal and Nimera choose-four recruitment")
	_expect(s019.has_tag("NO_RUBY_PRIME_NETWORK_LEAK"), "S019 must preserve the early knowledge firewall")
	_expect(s020.has_tag("WARDEN_ONE_HP_TWO_STATES"), "S020 First Command Warden must remain one HP bar / two states")
	_expect(s020.has_tag("NO_PRIME_MANIFESTATION"), "S020 must not manifest Last Sentinel")
	_expect(s021.has_tag("LAST_SENTINEL_IDENTIFIED_UNLOCKED") and s021.has_tag("NO_PRIME_MANIFESTATION"), "S021 must identify/unlock Last Sentinel without manifestation")
	_expect(h04.has_tag("LAST_SENTINEL_CASE_INERT") and h04.has_tag("NO_RUBY_CHANGE"), "H04 Last Sentinel case must remain completely inert")

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
		print("Diyse Audit88 Chapter 3 HD-2D presentation resource validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
