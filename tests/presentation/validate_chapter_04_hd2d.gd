extends SceneTree

const PRESENTATION_DIR := "res://game/content/presentation/chapter_04/"
const ScenePresentationDefinition = preload("res://game/presentation/scene_presentation_definition.gd")
const ElementalRuntime = preload("res://game/presentation/elemental_presentation_runtime.gd")

var failures: Array[String] = []

const EXPECTED := {
	"B01": {"environment": "CH03_CRESTHAVEN", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B02": {"environment": "CH04_THORNHIDE_TERRITORY", "background": "CH04_THORNHIDE_TERRITORY", "cutscene": "C3", "vfx": "V4", "encounter": "fixed_authored"},
	"B03": {"environment": "CH04_THORNHIDE_TERRITORY", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B04": {"environment": "CH04_FOREST_CROWN_ROUTE", "background": "CH04_FOREST_ROUTE", "cutscene": "C1", "vfx": "V1", "encounter": "random_allowed"},
	"B05": {"environment": "CH04_IVORYBRIDGE", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B06": {"environment": "CH04_REACTION_ANNEX", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B07": {"environment": "CH04_REACTION_ANNEX", "background": "CH04_REACTION_ANNEX", "cutscene": "C1", "vfx": "V2", "encounter": "random_allowed"},
	"B08": {"environment": "CH04_REACTION_ANNEX", "background": "CH04_REACTION_ANNEX", "cutscene": "C2", "vfx": "V2", "encounter": "mixed"},
	"B09": {"environment": "CH04_CENTRAL_REGULATION", "background": "CH04_CENTRAL_REGULATION", "cutscene": "C3", "vfx": "V3", "encounter": "mixed"},
	"B10": {"environment": "CH04_CENTRAL_REGULATION", "background": "CH04_CENTRAL_REGULATION", "cutscene": "C3", "vfx": "V3", "encounter": "fixed_authored"},
	"B11": {"environment": "CH04_REACTION_ANNEX", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"B12": {"environment": "CH04_IVORYBRIDGE", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
}

func _initialize() -> void:
	_validate_scene_sidecars()
	_validate_pre_dialogue_boundary()
	_validate_environment_states()
	_validate_prime_and_recruitment_timing()
	_validate_annex_scientific_boundaries()
	_validate_elemental_runtime()
	_validate_legacy_layer_removed()
	_validate_no_enemy_or_elite_placement()
	_finish()

func _validate_scene_sidecars() -> void:
	for scene_id in EXPECTED.keys():
		var presentation = load(PRESENTATION_DIR + scene_id + ".tres")
		_expect(presentation != null, "%s Chapter-4 structural presentation sidecar must load" % scene_id)
		if presentation == null:
			continue
		var schema_failures: Array[String] = presentation.validate_schema()
		_expect(schema_failures.is_empty(), "%s sidecar must validate: %s" % [scene_id, str(schema_failures)])
		var expected: Dictionary = EXPECTED[scene_id]
		_expect(str(presentation.scene_id) == scene_id, "%s presentation slot ID mismatch" % scene_id)
		_expect(str(presentation.chapter_id) == "chapter_04", "%s sidecar chapter mismatch" % scene_id)
		_expect(str(presentation.environment_family) == str(expected["environment"]), "%s environment mismatch" % scene_id)
		_expect(str(presentation.battle_background_family) == str(expected["background"]), "%s battle background mismatch" % scene_id)
		_expect(str(presentation.cutscene_tier) == str(expected["cutscene"]), "%s cutscene tier mismatch" % scene_id)
		_expect(str(presentation.vfx_tier) == str(expected["vfx"]), "%s VFX tier mismatch" % scene_id)
		_expect(str(presentation.encounter_mode) == str(expected["encounter"]), "%s encounter mode mismatch" % scene_id)
		_expect(presentation.has_tag("HD2D"), "%s must be HD2D" % scene_id)
		_expect(presentation.has_tag("PRE_DIALOGUE_STRUCTURE"), "%s must be marked pre-dialogue structural presentation" % scene_id)

func _validate_pre_dialogue_boundary() -> void:
	for scene_id in EXPECTED.keys():
		var current_dialogue_path := "res://game/content/dialogue/current/chapter_04/%s.tres" % scene_id
		_expect(not ResourceLoader.exists(current_dialogue_path), "%s must not have fabricated current runtime dialogue before approved exact dialogue exists" % scene_id)

func _validate_environment_states() -> void:
	var expected_states := {
		"environment_thornhide_territory.tres": {"id": "CH04_THORNHIDE_TERRITORY", "required": ["BASE", "ACTIVE", "RETREAT", "POST_STORY"]},
		"environment_forest_crown_route.tres": {"id": "CH04_FOREST_CROWN_ROUTE", "required": ["BASE", "ACTIVE", "CROWN_ROAD_REACHED", "POST_STORY"]},
		"environment_ivorybridge.tres": {"id": "CH04_IVORYBRIDGE", "required": ["BASE", "ACTIVE", "POST_ANNEX", "POST_STORY"]},
		"environment_reaction_annex.tres": {"id": "CH04_REACTION_ANNEX", "required": ["BASE", "ACTIVE", "CRISIS", "POST_CRISIS", "CLEARED", "POST_STORY"]},
		"environment_central_regulation.tres": {"id": "CH04_CENTRAL_REGULATION", "required": ["BASE", "ACTIVE", "FORM_I", "FORM_II", "POST_BOSS", "CLEARED"]},
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

	var cresthaven = load("res://game/content/presentation/chapter_03/environment_cresthaven.tres")
	_expect(cresthaven != null, "Chapter 4 B01 must reuse the current Chapter-3 Cresthaven environment family")
	_expect(str(cresthaven.environment_id) == "CH03_CRESTHAVEN", "Inherited Cresthaven environment ID must remain current")

func _validate_prime_and_recruitment_timing() -> void:
	var b01 = load(PRESENTATION_DIR + "B01.tres")
	var b02 = load(PRESENTATION_DIR + "B02.tres")
	var b05 = load(PRESENTATION_DIR + "B05.tres")
	var b12 = load(PRESENTATION_DIR + "B12.tres")
	_expect(b01.has_tag("NO_PRIME_THEORY_AT_WAKEUP"), "B01 must not raise Prime/Last Sentinel theory during the wake-up disturbance")
	_expect(b02.has_tag("FIRST_VERIFIED_MODERN_MANIFESTATION"), "B02 must own Last Sentinel's first verified modern manifestation")
	_expect(b02.has_tag("LAST_SENTINEL_RECOVERED_TRANSITION"), "B02 must own the Recovered transition/acquisition event")
	_expect(b02.has_tag("LAST_SENTINEL_NOT_AWAKENED"), "Last Sentinel must not Awaken in Chapter 4 B02")
	_expect(b02.has_tag("ELDER_THORNHIDE_RETREATS_ALIVE") and b02.has_tag("NONLETHAL_DRIVE_OFF"), "Elder Thornhide must survive and retreat")
	_expect(b02.has_tag("VAELIRA_NOT_PRESENT"), "Vaelira must not be present for the Elder Thornhide event")
	_expect(b05.has_tag("VAELIRA_PERMANENT_RECRUIT"), "Vaelira must join permanently in B05 Ivorybridge")
	_expect(b12.has_tag("LAST_SENTINEL_RECOVERED"), "Chapter 4 end state must retain Last Sentinel as Recovered")

func _validate_annex_scientific_boundaries() -> void:
	var b05 = load(PRESENTATION_DIR + "B05.tres")
	var b07 = load(PRESENTATION_DIR + "B07.tres")
	var b08 = load(PRESENTATION_DIR + "B08.tres")
	var b09 = load(PRESENTATION_DIR + "B09.tres")
	var b10 = load(PRESENTATION_DIR + "B10.tres")
	var b11 = load(PRESENTATION_DIR + "B11.tres")
	_expect(b05.has_tag("WAYFINDER_PATTERN_RESEMBLANCE_ONLY") and b05.has_tag("NO_FACE_INTERACTION_IDENTIFICATION"), "B05 must preserve the Wayfinder interpretation firewall")
	_expect(b07.has_tag("FOUR_ELEMENTS_ONLY") and b07.has_tag("BRANCH_MODELS_VALIDATE"), "B07 must validate the four individual branch models")
	_expect(b08.has_tag("SIX_PAIR_TESTS_VALIDATE") and b08.has_tag("REACTION_CONDUIT_NONLETHAL"), "B08 must validate all six pairs and resolve Reaction Conduit nonlethally")
	_expect(b08.has_tag("RESEARCHER_SURVIVES") and b08.has_tag("NO_SEVENTH_ELEMENT"), "B08 must preserve researcher survival and the four-element boundary")
	_expect(b09.has_tag("REGULATION_CRUCIBLE_FORM_I") and b09.has_tag("TWO_CHAMBERS_ACTIVE"), "B09 must own Regulation Crucible Form I")
	_expect(b10.has_tag("REGULATION_CRUCIBLE_FORM_II") and b10.has_tag("FORM2_FRESH_HP_MP"), "B10 must own the fresh-HP/MP Form-II transition")
	_expect(b10.has_tag("PRIME_REFRESH_FRESH_HP_FORM"), "B10 genuine fresh-HP form must refresh Prime availability")
	_expect(b10.has_tag("SEVENTH_REACTION_NOT_ELEMENT") and b10.has_tag("NO_THIRD_FORM"), "B10 must preserve Seventh Reaction as emergent behavior, not a new element or third form")
	_expect(b11.has_tag("MODEL_REVISION") and b11.has_tag("WAYFINDER_UNRESOLVED"), "B11 must revise the model without solving the Wayfinder")

func _validate_elemental_runtime() -> void:
	_expect(ElementalRuntime.ELEMENTS.size() == 4, "Elemental presentation runtime must expose exactly four elements")
	for element_id in ["fire", "ice", "lightning", "earth"]:
		_expect(ElementalRuntime.is_element(element_id), "Expected element missing from modular presentation runtime: %s" % element_id)
		_expect(not ElementalRuntime.payload_keys(element_id).is_empty(), "Element payload module list must exist for %s" % element_id)
	for retired_element_id in ["wind", "water"]:
		_expect(not ElementalRuntime.is_element(retired_element_id), "Retired element must not remain active in presentation runtime: %s" % retired_element_id)
		_expect(ElementalRuntime.payload_keys(retired_element_id).is_empty(), "Retired element must not expose payload modules: %s" % retired_element_id)
	_expect(not ElementalRuntime.is_element("seventh_reaction"), "Seventh Reaction must never validate as an element")

func _validate_legacy_layer_removed() -> void:
	for legacy_scene in ["S022", "S023", "S024", "S025", "S026", "H05", "C08", "C09", "HUNT_04_CROWN_PROTOTYPE"]:
		_expect(not ResourceLoader.exists(PRESENTATION_DIR + legacy_scene + ".tres"), "Retired Chapter-4 presentation sidecar must be removed: %s" % legacy_scene)
	for legacy_environment in [
		"environment_cresthaven_lower_grounds.tres",
		"environment_annex_approach_regulation.tres",
		"environment_regulation_core.tres",
		"environment_sixfold_annex.tres",
		"environment_southhold_roadside.tres",
	]:
		_expect(not ResourceLoader.exists(PRESENTATION_DIR + legacy_environment), "Retired Chapter-4 environment presentation must be removed: %s" % legacy_environment)

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
		print("Diyse Chapter 4 current B01-B12 pre-dialogue HD-2D presentation validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
