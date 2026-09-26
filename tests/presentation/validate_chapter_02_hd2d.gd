extends SceneTree

const PRESENTATION_DIR := "res://game/content/presentation/chapter_02/"
const DIALOGUE_DIR := "res://game/content/dialogue/current/chapter_02/"
const ScenePresentationDefinition = preload("res://game/presentation/scene_presentation_definition.gd")

var failures: Array[String] = []

const EXPECTED := {
	"B01": {"environment": "CH02_DUNMERE_APPROACH", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
	"B02": {"environment": "CH02_DUNMERE", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B03": {"environment": "CH02_DUNMERE", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B04": {"environment": "CH02_OLD_WATERWORKS", "background": "CH02_OLD_WATERWORKS", "cutscene": "C1", "vfx": "V1", "encounter": "random_allowed"},
	"B05": {"environment": "CH02_SUNKEN_ARCHIVE", "background": "CH02_SUNKEN_ARCHIVE", "cutscene": "C1", "vfx": "V1", "encounter": "random_allowed"},
	"B06": {"environment": "CH02_SUNKEN_ARCHIVE", "background": "CH02_SUNKEN_ARCHIVE", "cutscene": "C1", "vfx": "V1", "encounter": "random_allowed"},
	"B07": {"environment": "CH02_SUNKEN_ARCHIVE", "background": "CH02_SUNKEN_ARCHIVE", "cutscene": "C2", "vfx": "V2", "encounter": "fixed_authored"},
	"B08": {"environment": "CH02_SUNKEN_ARCHIVE", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B09": {"environment": "CH02_PRISONER_GALLERIES", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B10": {"environment": "CH02_PRISONER_GALLERIES", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B11": {"environment": "CH02_OLD_BASTION", "background": "CH02_OLD_BASTION", "cutscene": "C1", "vfx": "V1", "encounter": "random_allowed"},
	"B12": {"environment": "CH02_OLD_BASTION", "background": "", "cutscene": "C2", "vfx": "V1", "encounter": "none"},
	"B13": {"environment": "CH02_OLD_BASTION", "background": "CH02_OLD_BASTION", "cutscene": "C2", "vfx": "V2", "encounter": "fixed_authored"},
	"B14": {"environment": "CH02_PRISONER_GALLERIES", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B15": {"environment": "CH02_DUNMERE", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"C05": {"environment": "CH02_DUNMERE", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
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
		_expect(str(presentation.chapter_id) == "chapter_02", "%s sidecar chapter mismatch" % scene_id)
		_expect(str(dialogue.chapter_id) == "chapter_02", "%s current dialogue chapter mismatch" % scene_id)
		_expect(str(dialogue.scene_id).begins_with("CH02_%s_" % scene_id), "%s presentation must pair with the current canonical dialogue scene" % scene_id)
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
		"environment_dunmere_approach.tres": {"id": "CH02_DUNMERE_APPROACH", "required": ["BASE", "ACTIVE", "POST_STORY"]},
		"environment_dunmere.tres": {"id": "CH02_DUNMERE", "required": ["BASE", "ACTIVE", "POST_STORY"]},
		"environment_old_waterworks.tres": {"id": "CH02_OLD_WATERWORKS", "required": ["BASE", "ACTIVE", "CLEARED", "POST_STORY"]},
		"environment_sunken_archive.tres": {"id": "CH02_SUNKEN_ARCHIVE", "required": ["BASE", "ACTIVE", "OPEN", "POST_BOSS", "CLEARED"]},
		"environment_prisoner_galleries.tres": {"id": "CH02_PRISONER_GALLERIES", "required": ["BASE", "ACTIVE", "OPEN", "CLEARED", "POST_STORY"]},
		"environment_old_bastion.tres": {"id": "CH02_OLD_BASTION", "required": ["BASE", "ACTIVE", "INACTIVE", "POST_BOSS", "CLEARED"]},
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
	var b04 = load(PRESENTATION_DIR + "B04.tres")
	var b07 = load(PRESENTATION_DIR + "B07.tres")
	var b08 = load(PRESENTATION_DIR + "B08.tres")
	var b10 = load(PRESENTATION_DIR + "B10.tres")
	var b11 = load(PRESENTATION_DIR + "B11.tres")
	var b12 = load(PRESENTATION_DIR + "B12.tres")
	var b13 = load(PRESENTATION_DIR + "B13.tres")
	var b14 = load(PRESENTATION_DIR + "B14.tres")
	var b15 = load(PRESENTATION_DIR + "B15.tres")
	_expect(b04.has_tag("NO_BLACK_HOST_RANDOMS"), "B04 Old Waterworks must remain covert with no routine Black Host randoms")
	_expect(str(b07.encounter_mode) == "fixed_authored" and b07.has_tag("ARCHIVE_LEVIATHAN_AUTHORED"), "B07 must present the authored Archive Leviathan climax")
	_expect(b07.has_tag("MAEVRA_NONCOMBAT"), "B07 must preserve Maevra as noncombat")
	_expect(b08.has_tag("NO_TRANSFER_RECORDS_BEAT"), "B08 must not restore the retired transfer-records beat")
	_expect(b10.has_tag("NO_ESCORT_BATTLE"), "B10 must not create prisoner-escort combat")
	_expect(str(b11.encounter_mode) == "random_allowed" and b11.has_tag("FUNCTIONING_BLACK_HOST_BASE"), "B11 must preserve hostile traversal through a functioning Old Bastion")
	_expect(b12.has_tag("MASKED_OFFICER_UNNAMED") and b12.has_tag("SEYRIK_IDENTITY_FIREWALL"), "B12 must preserve the masked-officer identity firewall")
	_expect(str(b13.encounter_mode) == "fixed_authored" and b13.has_tag("RHAZEK_SURVIVES_WITHDRAWAL"), "B13 must preserve the authored Rhazek climax and credible withdrawal")
	_expect(b14.has_tag("NO_ESCORT_BEAT"), "B14 must return to the prisoners without restoring a dedicated escort beat")
	_expect(b15.has_tag("ROAD_REOPENED") and b15.has_tag("NO_AUTOMATIC_CH3"), "B15 must preserve Dunmere cleanup and explicit Chapter-3 advance")

func _validate_legacy_layer_removed() -> void:
	for legacy_scene in ["S012", "S013", "S014", "S015", "S016", "C06", "C07"]:
		_expect(not ResourceLoader.exists(PRESENTATION_DIR + legacy_scene + ".tres"), "Legacy Chapter-2 presentation sidecar must be removed: %s" % legacy_scene)
	for legacy_environment in [
		"environment_dunmere_waterworks.tres",
		"environment_prisoner_transfer_service.tres",
		"environment_extraction_causeway.tres",
	]:
		_expect(not ResourceLoader.exists(PRESENTATION_DIR + legacy_environment), "Retired Chapter-2 environment presentation must be removed: %s" % legacy_environment)

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
		print("Diyse Chapter 2 current B01-B15 HD-2D presentation validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
