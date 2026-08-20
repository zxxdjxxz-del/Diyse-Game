extends SceneTree

const PRESENTATION_DIR := "res://game/content/presentation/chapter_04/"
const DIALOGUE_DIR := "res://game/content/dialogue/chapter_04/"
const ScenePresentationDefinition = preload("res://game/presentation/scene_presentation_definition.gd")
const ElementalRuntime = preload("res://game/presentation/elemental_presentation_runtime.gd")

var failures: Array[String] = []

const EXPECTED := {
	"S022": {"environment": "CH04_CRESTHAVEN_LOWER_GROUNDS", "background": "CH04_LOWER_CRESTHAVEN_GROUNDS", "cutscene": "C3", "vfx": "V4", "encounter": "fixed_authored"},
	"S023": {"environment": "CH04_SIXFOLD_ANNEX", "background": "CH04_SIXFOLD_ANNEX", "cutscene": "C2", "vfx": "V3", "encounter": "mixed"},
	"S024": {"environment": "CH04_REGULATION_CORE", "background": "CH04_REGULATION_CORE", "cutscene": "C3", "vfx": "V3", "encounter": "mixed"},
	"S025": {"environment": "CH04_SIXFOLD_ANNEX", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"S026": {"environment": "CH04_IVORYBRIDGE", "background": "", "cutscene": "C1", "vfx": "V1", "encounter": "none"},
	"C08": {"environment": "CH04_SOUTHHOLD_ROADSIDE", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
	"C09": {"environment": "CH04_IVORYBRIDGE", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
	"H05": {"environment": "CH03_CRESTHAVEN_STATE_1", "background": "", "cutscene": "C0", "vfx": "V1", "encounter": "none"},
	"HUNT_04_CROWN_PROTOTYPE": {"environment": "CH04_SIXFOLD_ANNEX", "background": "CH04_ANNEX_PROTOTYPE_BRANCH", "cutscene": "C1", "vfx": "V2", "encounter": "fixed_authored"},
}

func _initialize() -> void:
	_validate_scene_sidecars()
	_validate_environment_states()
	_validate_prime_and_crucible_rules()
	_validate_elemental_runtime()
	_validate_hunt_vs_elite_boundary()
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
		_expect(str(presentation.chapter_id) == "chapter_04", "%s sidecar chapter mismatch" % scene_id)
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
		"environment_cresthaven_lower_grounds.tres": {"id": "CH04_CRESTHAVEN_LOWER_GROUNDS", "required": ["BASE", "ACTIVE", "CLEARED", "POST_STORY"]},
		"environment_ivorybridge.tres": {"id": "CH04_IVORYBRIDGE", "required": ["BASE", "ACTIVE", "POST_STORY"]},
		"environment_annex_approach_regulation.tres": {"id": "CH04_ANNEX_APPROACH_REGULATION", "required": ["BASE", "ACTIVE", "CLEARED", "POST_STORY"]},
		"environment_sixfold_annex.tres": {"id": "CH04_SIXFOLD_ANNEX", "required": ["BASE", "ACTIVE", "CLOSED", "CLEARED", "POST_STORY"]},
		"environment_regulation_core.tres": {"id": "CH04_REGULATION_CORE", "required": ["BASE", "ACTIVE", "POST_BOSS", "CLEARED"]},
		"environment_southhold_roadside.tres": {"id": "CH04_SOUTHHOLD_ROADSIDE", "required": ["BASE", "ACTIVE", "POST_STORY"]},
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

	var inherited_cresthaven = load("res://game/content/presentation/chapter_03/environment_cresthaven_state_1.tres")
	_expect(inherited_cresthaven != null, "Chapter 4 H05 must reuse the Chapter 3 Cresthaven State 1 environment resource")

func _validate_prime_and_crucible_rules() -> void:
	var s022 = load(PRESENTATION_DIR + "S022.tres")
	var s023 = load(PRESENTATION_DIR + "S023.tres")
	var s024 = load(PRESENTATION_DIR + "S024.tres")
	_expect(s022.has_tag("FIRST_VERIFIED_PRIME_MANIFESTATION"), "S022 must remain the first verified modern Prime manifestation")
	_expect(s022.has_tag("LAST_SENTINEL_ROUND4_ONLY") and s022.has_tag("PRIME_PIPELINE"), "S022 must route Last Sentinel through the approved Round-4 Prime pipeline")
	_expect(str(s022.vfx_tier) == "V4", "S022 Last Sentinel manifestation must remain the first early-game V4 event")
	_expect(s022.has_tag("ELDER_BRIARHIDE_RETREATS_ALIVE"), "Elder Briarhide must retreat alive after the first manifestation")
	_expect(s023.has_tag("HEXARCH_LIVING_RESEARCHER") and s023.has_tag("HEXARCH_NONLETHAL_STABILIZATION"), "Hexarch must remain a living researcher resolved nonlethally")
	_expect(s023.has_tag("NO_SEVENTH_ELEMENT"), "S023 must not present the out-of-loop reaction as a seventh element")
	_expect(s024.has_tag("SEVENTH_REACTION_NOT_ELEMENT"), "S024 must preserve Seventh Reaction as a system consequence")
	_expect(s024.has_tag("CRUCIBLE_GENUINE_TWO_FORM") and s024.has_tag("FORM2_FRESH_HP_MP"), "Sixfold Crucible must remain a genuine fresh-HP/MP Form-II transition")
	_expect(s024.has_tag("NO_PRIME_REFRESH"), "Sixfold Crucible transformation must not refresh Prime availability")

func _validate_elemental_runtime() -> void:
	_expect(ElementalRuntime.ELEMENTS.size() == 6, "Elemental presentation runtime must expose exactly six elements")
	for element_id in ["fire", "ice", "lightning", "wind", "earth", "water"]:
		_expect(ElementalRuntime.is_element(element_id), "Expected element missing from modular presentation runtime: %s" % element_id)
		_expect(not ElementalRuntime.payload_keys(element_id).is_empty(), "Element payload module list must exist for %s" % element_id)
	_expect(not ElementalRuntime.is_element("seventh_reaction"), "Seventh Reaction must never validate as an element")
	_expect(not ElementalRuntime.validate_element_ids(["seventh_reaction"]).is_empty(), "Element validation must reject Seventh Reaction")

func _validate_hunt_vs_elite_boundary() -> void:
	var hunt = load(PRESENTATION_DIR + "HUNT_04_CROWN_PROTOTYPE.tres")
	_expect(hunt.has_tag("HUNT"), "Crown Prototype sidecar may identify its already-canon Hunt category")
	_expect(hunt.has_tag("ONE_BODY_ONE_HP") and hunt.has_tag("NO_TRANSFORMATION"), "Crown Prototype Hunt must remain one body / one HP bar / no transformation")
	_expect(hunt.has_tag("PRE_EXISTING_RELENTLESS_FLURRY"), "Crown Prototype must expose a pre-existing Card rather than create one")
	for tag in hunt.presentation_tags:
		_expect("ELITE" not in str(tag).to_upper(), "Hunt category must remain separate from Elite placement: %s" % tag)

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
		print("Diyse Audit88 Chapter 4 HD-2D presentation resource validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
