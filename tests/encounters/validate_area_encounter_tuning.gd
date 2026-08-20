extends SceneTree

const Controller = preload("res://game/exploration/field_encounter_controller.gd")
const Tuning = preload("res://game/exploration/area_encounter_tuning.gd")
const PROOF_TUNING_PATH := "res://game/content/encounters/tuning/proof_field_greenhollow.tres"

func _initialize() -> void:
	var failures: Array[String] = []
	_validate_proof_tuning(failures)
	_validate_schema_guards(failures)
	_validate_transition_semantics(failures)
	_finish(failures)

func _validate_proof_tuning(failures: Array[String]) -> void:
	var proof = load(PROOF_TUNING_PATH)
	if proof == null:
		failures.append("Could not load engineering Greenhollow area encounter tuning")
		return
	var schema_failures: Array = proof.validate_schema()
	if not schema_failures.is_empty():
		failures.append("Engineering Greenhollow tuning failed its schema: %s" % str(schema_failures))
	if str(proof.tuning_id) != "proof_field_greenhollow":
		failures.append("Proof tuning ID changed unexpectedly")
	if int(proof.chapter) != 1 or str(proof.random_area_id) != "ch01_greenhollow":
		failures.append("Proof tuning must target the existing Chapter 1 Greenhollow random pool")
	if absf(float(proof.world_units_per_s) - 20.0) > 0.0001:
		failures.append("Proof tuning temporary world-units-per-S value changed unexpectedly")
	if not bool(proof.random_encounters_enabled):
		failures.append("Proof tuning must enable random encounters")
	if str(proof.transition_mode_on_entry) != Tuning.TRANSITION_SAME_ECOLOGY:
		failures.append("Proof tuning must enter as same-ecology engineering context")
	if not proof.is_engineering_only() or proof.is_production_calibrated():
		failures.append("20-world-unit proof tuning must remain explicitly engineering-only")

	var controller = Controller.new(1001)
	get_root().add_child(controller)
	if not controller.configure_tuning(proof):
		failures.append("Reusable field controller rejected valid proof tuning resource")
	else:
		if int(controller.chapter) != 1 or str(controller.area_id) != "ch01_greenhollow":
			failures.append("Controller lost chapter/area fields while configuring from tuning resource")
		if absf(float(controller.world_units_per_s) - 20.0) > 0.0001:
			failures.append("Controller lost S-distance scale while configuring from tuning resource")
	controller.queue_free()

func _validate_schema_guards(failures: Array[String]) -> void:
	var awaiting = Tuning.new()
	awaiting.tuning_id = "uncalibrated_enabled_area"
	awaiting.chapter = 1
	awaiting.random_area_id = "ch01_greenhollow"
	awaiting.world_units_per_s = 10.0
	awaiting.random_encounters_enabled = true
	awaiting.calibration_state = Tuning.CALIBRATION_AWAITING_GEOMETRY
	if awaiting.validate_schema().is_empty():
		failures.append("Awaiting-geometry tuning must not be allowed to enable random encounters")

	var zero_scale = Tuning.new()
	zero_scale.tuning_id = "zero_scale_enabled_area"
	zero_scale.chapter = 1
	zero_scale.random_area_id = "ch01_greenhollow"
	zero_scale.world_units_per_s = 0.0
	zero_scale.random_encounters_enabled = true
	zero_scale.calibration_state = Tuning.CALIBRATION_ENGINEERING_ONLY
	if zero_scale.validate_schema().is_empty():
		failures.append("Enabled tuning must reject zero world-units-per-S scale")

	var invalid_transition = Tuning.new()
	invalid_transition.tuning_id = "invalid_transition"
	invalid_transition.random_encounters_enabled = false
	invalid_transition.transition_mode_on_entry = "doorway_rng_reset"
	if invalid_transition.validate_schema().is_empty():
		failures.append("Area tuning accepted an unsupported transition mode")

func _validate_transition_semantics(failures: Array[String]) -> void:
	var controller = Controller.new(2002)
	get_root().add_child(controller)
	if not controller.configure_context(1, "ch01_greenhollow", 10.0):
		failures.append("Transition test could not configure initial Greenhollow context")
		controller.queue_free()
		return

	controller.advance_eligible_distance(3.0, [1.0], 0.0, 0.0)
	if absf(controller.pressure_fraction_s() - 0.30) > 0.0001:
		failures.append("Transition test failed to establish 0.30S carried pressure")

	if not controller.configure_context(
		1,
		"ch01_brackenwall",
		10.0,
		Controller.TRANSITION_NEW_ECOLOGY
	):
		failures.append("Controller rejected valid new-ecology transition")
	else:
		if absf(controller.pressure_fraction_s() - 0.30) > 0.0001:
			failures.append("New ecology transition reset pressure instead of carrying it")
		if absf(controller.transition_grace_fraction_s() - 0.10) > 0.0001:
			failures.append("New ecology transition did not add exactly 0.10S grace")

	controller.advance_eligible_distance(1.0, [1.0], 0.0, 0.0)
	if absf(controller.pressure_fraction_s() - 0.30) > 0.0001:
		failures.append("Ecology transition grace did not consume eligible distance before pressure")
	if controller.transition_grace_fraction_s() > 0.0001:
		failures.append("Ecology transition grace remained after consuming 0.10S")

	var post_grace := controller.advance_eligible_distance(1.0, [1.0], 0.0, 0.0)
	if not post_grace.is_empty():
		failures.append("High deterministic roll should suppress encounter while verifying post-grace pressure")
	if absf(controller.pressure_fraction_s() - 0.40) > 0.0001:
		failures.append("Pressure did not resume after ecology transition grace")

	if not controller.configure_context(
		1,
		"ch01_greenhollow",
		10.0,
		Controller.TRANSITION_SAME_ECOLOGY
	):
		failures.append("Controller rejected valid same-ecology transition")
	else:
		if absf(controller.pressure_fraction_s() - 0.40) > 0.0001:
			failures.append("Same-ecology transition did not preserve pressure")
		if controller.transition_grace_fraction_s() > 0.0001:
			failures.append("Same-ecology transition added grace when it should preserve continuously")

	controller.last_formation_id = "ch01_greenhollow_s01"
	if not controller.configure_context(
		1,
		"ch01_hollow_watch",
		10.0,
		Controller.TRANSITION_SAFE_RESET
	):
		failures.append("Controller rejected valid safe-reset transition")
	else:
		if absf(controller.pressure_fraction_s()) > 0.0001:
			failures.append("Safe-reset transition did not clear encounter pressure")
		if not controller.last_formation_id.is_empty():
			failures.append("Safe-reset transition did not clear anti-repeat history")

	controller.advance_eligible_distance(2.0, [1.0], 0.0, 0.0)
	controller.last_formation_id = "ch01_hollow_watch_l01"
	var disabled_safe = Tuning.new()
	disabled_safe.tuning_id = "safe_space_without_randoms"
	disabled_safe.random_encounters_enabled = false
	disabled_safe.transition_mode_on_entry = Tuning.TRANSITION_SAFE_RESET
	disabled_safe.calibration_state = Tuning.CALIBRATION_AWAITING_GEOMETRY
	if not controller.configure_tuning(disabled_safe):
		failures.append("Controller rejected valid disabled safe-space tuning")
	else:
		if controller.enabled:
			failures.append("Disabled safe-space tuning left random encounters enabled")
		if absf(controller.pressure_fraction_s()) > 0.0001:
			failures.append("Disabled safe-space tuning did not reset carried pressure")
		if not controller.last_formation_id.is_empty():
			failures.append("Disabled safe-space tuning did not clear anti-repeat history")
		if controller.context_configured or not controller.area_id.is_empty():
			failures.append("Safe-space tuning retained stale random-area context")

	controller.queue_free()

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Audit98 area encounter tuning and ecology transition validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
