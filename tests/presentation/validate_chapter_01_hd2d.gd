extends SceneTree

const PRESENTATION_DIR := "res://game/content/presentation/chapter_01/"
const DIALOGUE_DIR := "res://game/content/dialogue/current/chapter_01/"
const ScenePresentationDefinition = preload("res://game/presentation/scene_presentation_definition.gd")

var failures: Array[String] = []

const EXPECTED := {
	"B01": {"environment": "CH01_BRACKENWALL", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B02": {"environment": "CH01_BRIAR_PASSAGE", "background": "CH01_BRIAR_PASSAGE", "cutscene": "C1", "vfx": "V1", "encounter": "random_allowed"},
	"B03": {"environment": "CH01_GREENHOLLOW", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B04": {"environment": "CH01_HOLLOW_WATCH", "background": "CH01_HOLLOW_WATCH", "cutscene": "C1", "vfx": "V1", "encounter": "random_allowed"},
	"B05": {"environment": "CH01_HOLLOW_WATCH", "background": "CH01_HOLLOW_WATCH", "cutscene": "C1", "vfx": "V1", "encounter": "random_allowed"},
	"B06": {"environment": "CH01_HOLLOW_WATCH", "background": "CH01_HOLLOW_WATCH", "cutscene": "C1", "vfx": "V1", "encounter": "mixed"},
	"B07": {"environment": "CH01_HOLLOW_WATCH", "background": "", "cutscene": "C2", "vfx": "V1", "encounter": "none"},
	"B08": {"environment": "CH01_GREENHOLLOW", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B09": {"environment": "CH01_BRIAR_PASSAGE", "background": "CH01_BRIAR_PASSAGE", "cutscene": "C1", "vfx": "V1", "encounter": "random_allowed"},
	"B10": {"environment": "CH01_BRIAR_PASSAGE", "background": "CH01_BRIAR_PASSAGE", "cutscene": "C2", "vfx": "V2", "encounter": "fixed_authored"},
	"B11": {"environment": "CH01_JUNCTION", "background": "", "cutscene": "C2", "vfx": "V1", "encounter": "none"},
	"B12": {"environment": "CH01_JUNCTION", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"C02": {"environment": "CH01_JUNCTION", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
	"C03": {"environment": "CH01_JUNCTION", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
	"C04": {"environment": "CH01_JUNCTION", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
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
		_expect(str(presentation.chapter_id) == "chapter_01", "%s sidecar chapter mismatch" % scene_id)
		_expect(str(dialogue.chapter_id) == "chapter_01", "%s current dialogue chapter mismatch" % scene_id)
		_expect(str(dialogue.scene_id).begins_with("CH01_%s_" % scene_id), "%s presentation must pair with the current canonical dialogue scene" % scene_id)
		_expect(str(presentation.environment_family) == str(expected["environment"]), "%s environment family mismatch" % scene_id)
		_expect(str(presentation.battle_background_family) == str(expected["background"]), "%s battle-background family mismatch" % scene_id)
		_expect(str(presentation.cutscene_tier) == str(expected["cutscene"]), "%s cutscene tier mismatch" % scene_id)
		_expect(str(presentation.vfx_tier) == str(expected["vfx"]), "%s VFX tier mismatch" % scene_id)
		_expect(str(presentation.encounter_mode) == str(expected["encounter"]), "%s encounter-mode mismatch" % scene_id)
		_expect(presentation.has_tag("HD2D"), "%s must be marked HD2D" % scene_id)
		for tag in presentation.presentation_tags:
			_expect("ELITE" not in str(tag).to_upper(), "%s sidecar must not encode Elite placement: %s" % [scene_id, tag])
			_expect("BRIARHIDE" not in str(tag).to_upper(), "%s must not restore retired Briarhide naming: %s" % [scene_id, tag])
			_expect("CASTELLAN_SAME_BODY_SAME_HP" not in str(tag).to_upper(), "%s must not restore retired Castellan presentation: %s" % [scene_id, tag])

func _validate_environment_states() -> void:
	var expected_states := {
		"environment_brackenwall.tres": {"id": "CH01_BRACKENWALL", "required": ["BASE", "ACTIVE", "POST_STORY"]},
		"environment_briar_passage.tres": {"id": "CH01_BRIAR_PASSAGE", "required": ["BASE", "ACTIVE", "CLEARED", "POST_STORY"]},
		"environment_greenhollow.tres": {"id": "CH01_GREENHOLLOW", "required": ["BASE", "ACTIVE", "POST_STORY"]},
		"environment_hollow_watch.tres": {"id": "CH01_HOLLOW_WATCH", "required": ["BASE", "ACTIVE", "OPEN", "CLEARED", "POST_STORY"]},
		"environment_junction.tres": {"id": "CH01_JUNCTION", "required": ["BASE", "ACTIVE", "OPEN", "POST_STORY"]},
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
	var b02 = load(PRESENTATION_DIR + "B02.tres")
	var b06 = load(PRESENTATION_DIR + "B06.tres")
	var b07 = load(PRESENTATION_DIR + "B07.tres")
	var b09 = load(PRESENTATION_DIR + "B09.tres")
	var b10 = load(PRESENTATION_DIR + "B10.tres")
	var b11 = load(PRESENTATION_DIR + "B11.tres")
	var b12 = load(PRESENTATION_DIR + "B12.tres")
	var c02 = load(PRESENTATION_DIR + "C02.tres")
	var c03 = load(PRESENTATION_DIR + "C03.tres")
	var c04 = load(PRESENTATION_DIR + "C04.tres")
	_expect(b02.has_tag("NO_WALKING_DIALOGUE"), "B02 must preserve the authored-stop/no-walking-dialogue rule")
	_expect(str(b06.encounter_mode) == "mixed", "B06 must support Construct randoms plus the fixed Shield Construct")
	_expect(b06.has_tag("CONSTRUCT_ONLY_UNDERGROUND") and b06.has_tag("NO_BLACK_HOST_UNDERGROUND"), "B06 must keep the excavation Construct-only")
	_expect(b06.has_tag("SHIELD_CONSTRUCT_FIXED_NOT_MINIBOSS"), "B06 Shield Construct must remain fixed authored combat without miniboss framing")
	_expect(b06.has_tag("NO_CASTELLAN"), "B06 must preserve the retired Castellan boundary")
	_expect(b07.has_tag("LANDSCAPE_DEPICTION") and b07.has_tag("NO_HIDDEN_NETWORK_REVEAL"), "B07 must preserve the current landscape-depiction reveal boundary")
	_expect(b09.has_tag("THORNHIDE_SIGNS_ONLY") and b09.has_tag("NO_THORNHIDE_CLEAR_SIGHTING"), "B09 must not reveal Thornhide before the boss beat")
	_expect(str(b10.encounter_mode) == "fixed_authored" and b10.has_tag("THORNHIDE_BOSS"), "B10 must present Thornhide as the Chapter-1 boss")
	_expect(b10.has_tag("NORMAL_LETHAL_BOSS") and b10.has_tag("NO_NONLETHAL_RETREAT"), "B10 must not restore the old nonlethal Briarhide resolution")
	_expect(b11.has_tag("WESTERN_ANCIENT_DIYSE_MAP") and b11.has_tag("CAELORA_AREA_BREAK"), "B11 must preserve the current Wayfinder scale and damaged Caelora cluster")
	_expect(b11.has_tag("SIX_FACE_MARKINGS") and b11.has_tag("NO_HIDDEN_NETWORK_REVEAL"), "B11 may show all six Face markings without revealing their hidden network function")
	_expect(str(b12.encounter_mode) == "none" and b12.has_tag("CLEANUP_WINDOW"), "B12 must remain the safe Chapter-1 cleanup window")
	for scene in [c02, c03, c04]:
		_expect(str(scene.environment_family) == "CH01_JUNCTION" and scene.has_tag("JUNCTION_CAMP"), "Chapter-1 Character-Life scenes must live in the Junction camp cleanup window")

func _validate_legacy_layer_removed() -> void:
	for legacy_scene in ["S007", "S008", "S009", "S010", "S011", "C05"]:
		_expect(not ResourceLoader.exists(PRESENTATION_DIR + legacy_scene + ".tres"), "Legacy Chapter-1 presentation sidecar must be removed: %s" % legacy_scene)
	for legacy_environment in [
		"environment_edgelands_settlement.tres",
		"environment_wooded_route.tres",
		"environment_ancient_route_wayfinder.tres",
	]:
		_expect(not ResourceLoader.exists(PRESENTATION_DIR + legacy_environment), "Retired Chapter-1 environment presentation must be removed: %s" % legacy_environment)

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
		print("Diyse Chapter 1 current B01-B12 HD-2D presentation validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
