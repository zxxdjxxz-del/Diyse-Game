extends Node
class_name DiyseDialogueFieldBridge

signal scene_policy_applied(scene_id: String, metadata: Dictionary)
signal scene_policy_restored(scene_id: String)

# DialogueRunner currently has no class_name, so keep this as Node and validate the
# expected scene_started/scene_finished signals at bind time rather than inventing
# a second runtime class identity.
var dialogue_runner: Node
var player_controller: Node
var encounter_controller: DiyseFieldEncounterController

var _active_scene_id := ""
var _active_metadata: Dictionary = {}
var _movement_state_captured := false
var _previous_movement_enabled := true
var _encounter_pause_state_captured := false
var _previous_authored_paused := false

func bind(
	runner: Node,
	player: Node = null,
	encounters: DiyseFieldEncounterController = null
) -> void:
	unbind()
	dialogue_runner = runner
	player_controller = player
	encounter_controller = encounters
	if dialogue_runner != null:
		if not dialogue_runner.has_signal("scene_started") or not dialogue_runner.has_signal("scene_finished"):
			push_error("Dialogue field bridge requires scene_started and scene_finished signals")
			dialogue_runner = null
			return
		dialogue_runner.scene_started.connect(_on_scene_started)
		dialogue_runner.scene_finished.connect(_on_scene_finished)

func unbind() -> void:
	_restore_active_policy()
	if dialogue_runner != null:
		if dialogue_runner.scene_started.is_connected(_on_scene_started):
			dialogue_runner.scene_started.disconnect(_on_scene_started)
		if dialogue_runner.scene_finished.is_connected(_on_scene_finished):
			dialogue_runner.scene_finished.disconnect(_on_scene_finished)
	dialogue_runner = null
	player_controller = null
	encounter_controller = null

func apply_scene_metadata(scene_id: String, metadata: Dictionary) -> Array[String]:
	var failures := validate_metadata(metadata)
	if not failures.is_empty():
		return failures

	if not _active_scene_id.is_empty():
		_restore_active_policy()

	_active_scene_id = scene_id
	_active_metadata = metadata.duplicate(true)

	var movement_lock := bool(metadata.get("movement_lock", true))
	if movement_lock and player_controller != null and player_controller.has_method("movement_enabled") and player_controller.has_method("set_movement_enabled"):
		_previous_movement_enabled = bool(player_controller.call("movement_enabled"))
		_movement_state_captured = true
		player_controller.call("set_movement_enabled", false)

	var encounter_policy_value = metadata.get("encounter_policy", {})
	var encounter_policy: Dictionary = encounter_policy_value if encounter_policy_value is Dictionary else {}
	var during_scene := str(encounter_policy.get("during_scene", "not_applicable"))
	if during_scene == "temporarily_suppress_trigger" and encounter_controller != null:
		_previous_authored_paused = encounter_controller.authored_paused
		_encounter_pause_state_captured = true
		# This pauses pressure advancement; it does not reset distance_s or apply safe-room grace.
		encounter_controller.set_authored_paused(true)

	scene_policy_applied.emit(scene_id, _active_metadata.duplicate(true))
	return []

func finish_active_scene(scene_id: String = "") -> void:
	if _active_scene_id.is_empty():
		return
	if not scene_id.is_empty() and scene_id != _active_scene_id:
		return
	var finished_id := _active_scene_id
	_restore_active_policy()
	scene_policy_restored.emit(finished_id)

func active_scene_id() -> String:
	return _active_scene_id

func active_metadata() -> Dictionary:
	return _active_metadata.duplicate(true)

func validate_metadata(metadata: Dictionary) -> Array[String]:
	var failures: Array[String] = []
	var scene_mode := str(metadata.get("scene_mode", "full_authored_stop_scene"))
	if scene_mode not in DiyseDialogueSceneDefinition.ALLOWED_SCENE_MODES:
		failures.append("Unsupported dialogue scene_mode: %s" % scene_mode)
	var readiness := str(metadata.get("dialogue_readiness", "GREEN"))
	if readiness not in DiyseDialogueSceneDefinition.ALLOWED_DIALOGUE_READINESS:
		failures.append("Unsupported dialogue_readiness: %s" % readiness)

	var encounter_policy_value = metadata.get("encounter_policy", {})
	if not (encounter_policy_value is Dictionary):
		failures.append("encounter_policy must be a Dictionary")
	else:
		var policy: Dictionary = encounter_policy_value
		if not policy.is_empty():
			var during_scene := str(policy.get("during_scene", ""))
			var after_scene := str(policy.get("after_scene", ""))
			if during_scene not in DiyseDialogueSceneDefinition.ALLOWED_ENCOUNTER_DURING:
				failures.append("Unsupported encounter_policy.during_scene: %s" % during_scene)
			if after_scene not in DiyseDialogueSceneDefinition.ALLOWED_ENCOUNTER_AFTER:
				failures.append("Unsupported encounter_policy.after_scene: %s" % after_scene)
	return failures

func _on_scene_started(scene_id: String, metadata: Dictionary) -> void:
	var failures := apply_scene_metadata(scene_id, metadata)
	for failure in failures:
		push_error("Dialogue field policy rejected: %s" % failure)

func _on_scene_finished(scene_id: String) -> void:
	finish_active_scene(scene_id)

func _restore_active_policy() -> void:
	if _movement_state_captured and player_controller != null and player_controller.has_method("set_movement_enabled"):
		player_controller.call("set_movement_enabled", _previous_movement_enabled)
	if _encounter_pause_state_captured and encounter_controller != null:
		encounter_controller.set_authored_paused(_previous_authored_paused)

	_active_scene_id = ""
	_active_metadata.clear()
	_movement_state_captured = false
	_previous_movement_enabled = true
	_encounter_pause_state_captured = false
	_previous_authored_paused = false
