extends SceneTree

const Controller = preload("res://game/exploration/field_encounter_controller.gd")

var emitted_payloads: Array[Dictionary] = []

func _initialize() -> void:
	var failures: Array[String] = []
	var controller = Controller.new(24680)
	get_root().add_child(controller)
	controller.battle_requested.connect(_on_battle_requested)

	_validate_configuration(controller, failures)
	_validate_trigger_and_payload(controller, failures)
	_validate_battle_return_states(controller, failures)
	_validate_pause_transition_and_safe_room(controller, failures)

	controller.queue_free()
	_finish(failures)

func _validate_configuration(controller, failures: Array[String]) -> void:
	if controller.configure_context(1, "ch01_greenhollow", 0.0):
		failures.append("Field encounter controller accepted a zero S-distance scale")
	if controller.configure_context(2, "ch01_greenhollow", 10.0):
		failures.append("Field encounter controller accepted an area under the wrong chapter")
	if not controller.configure_context(1, "ch01_greenhollow", 10.0):
		failures.append("Field encounter controller rejected a valid Chapter 1 random context")
	if not controller.enabled:
		failures.append("Valid encounter context must enable the controller")

func _validate_trigger_and_payload(controller, failures: Array[String]) -> void:
	emitted_payloads.clear()
	var before := controller.advance_eligible_distance(3.4, [0.0], 0.0, 0.0)
	if not before.is_empty():
		failures.append("Field controller triggered before 0.35S")
	if absf(controller.pressure_fraction_s() - 0.34) > 0.0001:
		failures.append("Field controller did not convert world distance into normalized S distance")

	var payload: Dictionary = controller.advance_eligible_distance(0.1, [0.0], 0.0, 0.0)
	if payload.is_empty():
		failures.append("Field controller did not request a battle at deterministic 0.35S trigger")
		return
	if str(payload.get("kind", "")) != "random":
		failures.append("Field battle payload must identify random encounter kind")
	if int(payload.get("chapter", 0)) != 1 or str(payload.get("area_id", "")) != "ch01_greenhollow":
		failures.append("Field battle payload lost chapter/area context")
	if str(payload.get("tier", "")) != "light":
		failures.append("Forced Light tier did not survive controller payload construction")
	if str(payload.get("formation_id", "")) != "ch01_greenhollow_l01":
		failures.append("Deterministic first Greenhollow Light formation was not selected")
	if int(payload.get("exp", 0)) != 45:
		failures.append("Chapter 1 Light payload must preserve the 45 EXP formation reward")
	var enemies: Array = payload.get("enemies", [])
	if enemies.size() != 2:
		failures.append("Expected two enemies in deterministic Greenhollow Light payload")
	if emitted_payloads.size() != 1:
		failures.append("Battle request signal must emit exactly once for one pressure trigger")
	if not controller.has_pending_battle():
		failures.append("Controller must remain battle-active after emitting a request")
	if controller.configure_context(1, "ch01_brackenwall", 10.0):
		failures.append("Controller allowed area context to change while a battle was active")
	if controller.area_id != "ch01_greenhollow":
		failures.append("Rejected in-battle context change still mutated the active area")

	var pressure_before_block := controller.pressure_fraction_s()
	if not controller.advance_eligible_distance(20.0, [0.0], 0.0, 0.0).is_empty():
		failures.append("Eligible movement must not spawn another encounter while battle is active")
	if absf(controller.pressure_fraction_s() - pressure_before_block) > 0.0001:
		failures.append("Encounter pressure advanced while battle was active")

func _validate_battle_return_states(controller, failures: Array[String]) -> void:
	if not controller.report_failed_flee_attempt():
		failures.append("Failed flee callback was rejected during an active battle")
	if not controller.battle_active:
		failures.append("Failed flee must keep the same battle active")
	if controller.pressure.encounter_pending:
		failures.append("Failed flee callback must clear only the pending pressure latch")

	if not controller.report_victory():
		failures.append("Victory callback was rejected during an active battle")
	if controller.has_pending_battle():
		failures.append("Victory must clear pending battle state")
	if absf(controller.pressure_fraction_s()) > 0.0001:
		failures.append("Victory must reset encounter pressure")

	var second: Dictionary = controller.advance_eligible_distance(3.5, [0.0], 0.0, 0.0)
	if second.is_empty():
		failures.append("Second deterministic encounter did not trigger")
		return
	if str(second.get("formation_id", "")) != "ch01_greenhollow_l02":
		failures.append("Immediate exact formation repeat was not suppressed after victory")

	if not controller.report_successful_flee():
		failures.append("Successful flee callback was rejected during an active battle")
	if absf(controller.pressure_fraction_s() - 0.65) > 0.0001:
		failures.append("Successful flee did not resume at approximately 0.65S pressure")
	if not controller.advance_eligible_distance(2.0, [0.0], 0.0, 0.0).is_empty():
		failures.append("Successful-flee 0.20S grace was not honored by field controller")
	var after_grace: Dictionary = controller.advance_eligible_distance(0.01, [0.0], 0.0, 0.0)
	if after_grace.is_empty():
		failures.append("Encounter pressure did not resume after successful-flee grace")
	elif str(after_grace.get("formation_id", "")) != "ch01_greenhollow_l01":
		failures.append("Post-flee encounter did not suppress the immediately previous exact formation")

	if not controller.cancel_battle_request_without_reset():
		failures.append("Controller could not cancel a pending battle request without pressure reset")
	if controller.battle_active or controller.pressure.encounter_pending:
		failures.append("Cancelled battle request left controller latched in battle state")

func _validate_pause_transition_and_safe_room(controller, failures: Array[String]) -> void:
	var before_pause := controller.pressure_fraction_s()
	controller.set_authored_paused(true)
	controller.advance_eligible_distance(50.0, [0.0], 0.0, 0.0)
	if absf(controller.pressure_fraction_s() - before_pause) > 0.0001:
		failures.append("Authored pause allowed encounter pressure to advance")
	controller.set_authored_paused(false)

	var before_transition := controller.pressure_fraction_s()
	if not controller.configure_context(1, "ch01_brackenwall", 10.0):
		failures.append("Controller rejected a valid same-chapter area transition")
	if absf(controller.pressure_fraction_s() - before_transition) > 0.0001:
		failures.append("Area context transition reset pressure instead of preserving it")

	if not controller.reset_for_safe_room():
		failures.append("Safe-room reset was rejected outside battle")
	if absf(controller.pressure_fraction_s()) > 0.0001:
		failures.append("Safe-room reset did not clear encounter pressure")
	if not controller.last_formation_id.is_empty():
		failures.append("Safe-room reset must clear anti-repeat formation history")

	controller.set_enabled(false)
	controller.advance_eligible_distance(20.0, [0.0], 0.0, 0.0)
	if absf(controller.pressure_fraction_s()) > 0.0001:
		failures.append("Disabled controller allowed encounter pressure to advance")
	controller.set_enabled(true)

func _on_battle_requested(payload: Dictionary) -> void:
	emitted_payloads.append(payload.duplicate(true))

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Audit98 reusable field encounter controller validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
