extends Node
class_name DiyseFieldEncounterController

signal battle_requested(payload: Dictionary)

const Pressure = preload("res://game/exploration/encounter_pressure.gd")

const TRANSITION_SAME_ECOLOGY := "same_ecology"
const TRANSITION_NEW_ECOLOGY := "new_ecology"
const TRANSITION_SAFE_RESET := "safe_reset"
const ALLOWED_TRANSITION_MODES := [
	TRANSITION_SAME_ECOLOGY,
	TRANSITION_NEW_ECOLOGY,
	TRANSITION_SAFE_RESET,
]

const Selector = preload("res://game/exploration/encounter_selector.gd")

var pressure
var selector

var chapter := 0
var area_id := ""
var world_units_per_s := 0.0
var enabled := false
var authored_paused := false
var battle_active := false
var last_formation_id := ""
var pending_battle: Dictionary = {}
var context_configured := false
var transition_mode_on_entry := TRANSITION_SAME_ECOLOGY

func _init(seed_value: int = 0) -> void:
	pressure = Pressure.new(seed_value)
	var selector_seed := 0 if seed_value == 0 else seed_value + 1
	selector = Selector.new(selector_seed)

func configure_context(
	new_chapter: int,
	new_area_id: String,
	new_world_units_per_s: float,
	transition_mode: String = TRANSITION_SAME_ECOLOGY
) -> bool:
	if battle_active:
		return false
	if transition_mode not in ALLOWED_TRANSITION_MODES:
		return false
	if new_world_units_per_s <= 0.0:
		return false
	if not selector.supports_context(new_chapter, new_area_id):
		return false

	var context_changed := context_configured and (
		chapter != new_chapter or area_id != new_area_id
	)
	if context_configured:
		if transition_mode == TRANSITION_SAFE_RESET:
			pressure.reset_for_safe_room()
			last_formation_id = ""
		elif transition_mode == TRANSITION_NEW_ECOLOGY and context_changed:
			pressure.apply_transition_grace()

	chapter = new_chapter
	area_id = new_area_id
	world_units_per_s = new_world_units_per_s
	transition_mode_on_entry = transition_mode
	context_configured = true
	enabled = true
	_apply_pause_state()
	return true

func configure_tuning(tuning) -> bool:
	if tuning == null or not tuning.has_method("validate_schema"):
		return false
	var failures: Array = tuning.validate_schema()
	if not failures.is_empty():
		return false

	var transition_mode := str(tuning.get("transition_mode_on_entry"))
	var tuning_enabled := bool(tuning.get("random_encounters_enabled"))
	if tuning_enabled:
		return configure_context(
			int(tuning.get("chapter")),
			str(tuning.get("random_area_id")),
			float(tuning.get("world_units_per_s")),
			transition_mode
		)

	if battle_active:
		return false
	if transition_mode == TRANSITION_SAFE_RESET:
		pressure.reset_for_safe_room()
		last_formation_id = ""
		chapter = 0
		area_id = ""
		world_units_per_s = 0.0
		context_configured = false
	transition_mode_on_entry = transition_mode
	enabled = false
	_apply_pause_state()
	return true

func set_enabled(value: bool) -> void:
	enabled = value
	_apply_pause_state()

func set_authored_paused(value: bool) -> void:
	authored_paused = value
	_apply_pause_state()

func advance_eligible_distance(
	world_distance: float,
	forced_pressure_rolls: Array = [],
	forced_tier_roll: float = -1.0,
	forced_formation_roll: float = -1.0
) -> Dictionary:
	if not enabled or authored_paused or battle_active:
		return {}
	if world_distance <= 0.0 or world_units_per_s <= 0.0:
		return {}

	var normalized_distance := world_distance / world_units_per_s
	if not pressure.advance(normalized_distance, forced_pressure_rolls):
		return {}

	var formation: Dictionary
	if forced_tier_roll >= 0.0 and forced_formation_roll >= 0.0:
		formation = selector.choose_with_rolls(
			chapter,
			area_id,
			forced_tier_roll,
			forced_formation_roll,
			last_formation_id
		)
	else:
		formation = selector.choose(chapter, area_id, last_formation_id)

	if formation.is_empty():
		pressure.cancel_pending_encounter()
		return {}

	pending_battle = _build_battle_payload(formation)
	battle_active = true
	last_formation_id = str(formation.get("id", ""))
	_apply_pause_state()
	battle_requested.emit(pending_battle.duplicate(true))
	return pending_battle.duplicate(true)

func report_victory() -> bool:
	if not battle_active:
		return false
	_finish_battle_state()
	pressure.reset_after_victory()
	_apply_pause_state()
	return true

func report_successful_flee() -> bool:
	if not battle_active:
		return false
	_finish_battle_state()
	pressure.resume_after_successful_flee()
	_apply_pause_state()
	return true

func report_failed_flee_attempt() -> bool:
	if not battle_active:
		return false
	pressure.resume_after_failed_flee()
	return true

func cancel_battle_request_without_reset() -> bool:
	if not battle_active:
		return false
	_finish_battle_state()
	pressure.cancel_pending_encounter()
	_apply_pause_state()
	return true

func restore_after_scene_return(outcome: String, formation_id: String) -> bool:
	if battle_active:
		return false
	if not formation_id.is_empty():
		last_formation_id = formation_id
	match outcome:
		"victory":
			pressure.reset_after_victory()
		"successful_flee":
			pressure.resume_after_successful_flee()
		"defeat":
			# Engineering proof return only. Production defeat flow is still separate.
			pressure.reset_after_victory()
		_:
			return false
	_apply_pause_state()
	return true

func reset_for_safe_room() -> bool:
	if battle_active:
		return false
	pressure.reset_for_safe_room()
	last_formation_id = ""
	_apply_pause_state()
	return true

func pressure_fraction_s() -> float:
	return float(pressure.distance_s)

func transition_grace_fraction_s() -> float:
	return float(pressure.grace_remaining_s)

func has_pending_battle() -> bool:
	return battle_active and not pending_battle.is_empty()

func _build_battle_payload(formation: Dictionary) -> Dictionary:
	return {
		"kind": "random",
		"chapter": chapter,
		"area_id": area_id,
		"formation_id": str(formation.get("id", "")),
		"tier": str(formation.get("tier", "")),
		"enemies": formation.get("enemies", []).duplicate(true),
		"exp": int(formation.get("exp", 0)),
	}

func _finish_battle_state() -> void:
	battle_active = false
	pending_battle.clear()

func _apply_pause_state() -> void:
	pressure.set_paused(not enabled or authored_paused or battle_active)
