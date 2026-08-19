extends SceneTree

const Hd2dRuntime = preload("res://game/presentation/hd2d_runtime.gd")
const EnvironmentStateDefinition = preload("res://game/presentation/environment_state_definition.gd")
const EncounterPresentationDefinition = preload("res://game/presentation/encounter_presentation_definition.gd")
const DialogueSceneDefinition = preload("res://game/dialogue/dialogue_scene_definition.gd")

var failures: Array[String] = []

func _initialize() -> void:
	_test_reference_targets()
	_test_battle_layout()
	_test_quality_scaling()
	_test_environment_states()
	_test_encounter_presentation_without_enemy_placement()
	_test_dialogue_presentation_metadata()
	_finish()

func _test_reference_targets() -> void:
	_expect(is_equal_approx(Hd2dRuntime.FIELD_CHARACTER_TARGET_PX, 80.0), "Field character target must remain approximately 80 px")
	_expect(is_equal_approx(Hd2dRuntime.BATTLE_CHARACTER_TARGET_PX, 200.0), "Battle character target must remain approximately 200 px")
	_expect(Hd2dRuntime.REFERENCE_SIZE == Vector2(1920.0, 1080.0), "Reference composition must remain 1920x1080")
	_expect(is_equal_approx(Hd2dRuntime.field_sprite_scale_for_texture(160.0), 0.5), "Field sprite scale helper must target 80 px")
	_expect(is_equal_approx(Hd2dRuntime.battle_sprite_scale_for_texture(400.0), 0.5), "Battle sprite scale helper must target 200 px")

func _test_battle_layout() -> void:
	var lane: Rect2 = Hd2dRuntime.action_lane(Vector2.ONE)
	_expect(lane.position.x >= 0.30 and lane.end.x <= 0.70, "Action lane must remain protected near the screen center")
	for i in range(4):
		var anchor := Hd2dRuntime.party_anchor(i, Vector2.ONE)
		_expect(anchor.x >= 0.0 and anchor.x < lane.position.x, "Party slot %d must remain left of the action lane" % i)
	for i in range(Hd2dRuntime.ENEMY_ANCHORS_NORMALIZED.size()):
		var anchor := Hd2dRuntime.enemy_anchor(i, Vector2.ONE)
		_expect(anchor.x > lane.end.x, "Enemy slot %d must remain right of the action lane" % i)
	_expect(Hd2dRuntime.party_anchor(-1) == Vector2(-1.0, -1.0), "Invalid party slots must not silently map onto a legal anchor")
	_expect(Hd2dRuntime.enemy_anchor(999) == Vector2(-1.0, -1.0), "Invalid enemy slots must not silently map onto a legal anchor")

func _test_quality_scaling() -> void:
	var low := Hd2dRuntime.decorative_quality_profile(0)
	var high := Hd2dRuntime.decorative_quality_profile(2)
	_expect(float(low.get("particle_multiplier", 1.0)) < float(high.get("particle_multiplier", 0.0)), "Low quality may reduce decorative particle density")
	_expect(not bool(low.get("decorative_dynamic_lights", true)), "Low quality should disable decorative dynamic lights")
	_expect(bool(high.get("secondary_motion", false)), "High quality should retain secondary decorative motion")

func _test_environment_states() -> void:
	var definition = EnvironmentStateDefinition.new()
	definition.environment_id = "proof_environment"
	definition.initial_state = "BASE"
	definition.available_states = ["BASE", "DAMAGED", "POST_BOSS"]
	definition.persistent_flag_prefix = "environment.proof"
	_expect(definition.validate_schema().is_empty(), "Valid authored environment states must pass validation")
	_expect(definition.allows_state("POST_BOSS"), "Authored post-boss state must be selectable")
	_expect(definition.persistent_flag_for("POST_BOSS") == "environment.proof.post_boss", "Environment persistence flag must be deterministic")

	var invalid = EnvironmentStateDefinition.new()
	invalid.environment_id = "bad_environment"
	invalid.initial_state = "OPEN"
	invalid.available_states = ["BASE"]
	_expect(not invalid.validate_schema().is_empty(), "Initial state outside available_states must be rejected")

func _test_encounter_presentation_without_enemy_placement() -> void:
	var definition = EncounterPresentationDefinition.new()
	definition.presentation_id = "elite_ready_not_assigned"
	definition.encounter_kind = "elite"
	definition.battle_background_family = "placeholder_family"
	definition.cutscene_tier = "C1"
	definition.vfx_tier = "V2"
	definition.form_mode = "same_body_same_hp"
	_expect(definition.validate_schema().is_empty(), "Generic Elite-capable presentation definition must validate without placing an Elite")

	var property_names: Array[String] = []
	for property in definition.get_property_list():
		property_names.append(str(property.get("name", "")))
	for forbidden in ["enemy_id", "enemy_ids", "elite_id", "chapter_id", "location_id", "encounter_table"]:
		_expect(forbidden not in property_names, "Presentation contract must not lock enemy/Elite placement field: %s" % forbidden)

func _test_dialogue_presentation_metadata() -> void:
	var scene = DialogueSceneDefinition.new()
	scene.scene_id = "PROOF_HD2D"
	scene.chapter_id = "proof"
	scene.scene_kind = "proof"
	scene.location_id = "proof_location"
	scene.trigger_id = "trigger.proof.hd2d"
	scene.completion_flag = "scene.proof_hd2d.complete"
	scene.cutscene_tier = "C2"
	scene.vfx_tier = "V3"
	scene.presentation_tags = ["HD2D_TEST"]
	scene.battle_background_family = "proof_background"
	scene.beats = [{
		"beat_id": "PROOF_HD2D_B001",
		"speaker_id": "",
		"text": "",
		"left": {},
		"right": {},
		"active_side": "none",
		"advance_mode": "manual",
		"cues": {},
	}]
	_expect(scene.validate_schema().is_empty(), "Valid HD-2D dialogue presentation metadata must remain backward-compatible with schema v1")
	var metadata := scene.presentation_metadata()
	_expect(str(metadata.get("cutscene_tier", "")) == "C2", "Dialogue presentation metadata must expose cutscene tier")
	_expect(str(metadata.get("vfx_tier", "")) == "V3", "Dialogue presentation metadata must expose VFX tier")
	_expect(str(metadata.get("battle_background_family", "")) == "proof_background", "Dialogue presentation metadata must expose optional battle-background family")

	var invalid = scene.duplicate(true)
	invalid.cutscene_tier = "S2"
	var saw_invalid_tier := false
	for message in invalid.validate_schema():
		if "Unsupported cutscene_tier" in message:
			saw_invalid_tier = true
	_expect(saw_invalid_tier, "Legacy S-tier shorthand must not be accepted as active Audit88 presentation metadata")

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Audit88 HD-2D runtime contract validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
