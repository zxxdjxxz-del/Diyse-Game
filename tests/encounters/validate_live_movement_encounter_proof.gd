extends SceneTree

const FIELD_SCENE := "res://game/exploration/field_proof.tscn"

var moved_distances: Array[float] = []

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var failures: Array[String] = []
	var packed := load(FIELD_SCENE) as PackedScene
	if packed == null:
		failures.append("Could not load field proof for live movement encounter validation")
		_finish(failures)
		return

	var field = packed.instantiate()
	get_root().add_child(field)
	await process_frame

	var player = field.get_node_or_null("Cyanis")
	var encounter_controller = field.get("encounter_controller")
	if player == null:
		failures.append("Field proof is missing Cyanis movement source")
	elif not player.has_signal("eligible_distance_moved"):
		failures.append("Player controller must expose eligible_distance_moved signal")
	if encounter_controller == null:
		failures.append("Field proof did not create the reusable encounter controller")
	else:
		if int(encounter_controller.chapter) != 1:
			failures.append("Field encounter proof must use Chapter 1 test context")
		if str(encounter_controller.area_id) != "ch01_greenhollow":
			failures.append("Field encounter proof must use the existing Greenhollow test pool")
		if absf(float(encounter_controller.world_units_per_s) - 20.0) > 0.0001:
			failures.append("Field encounter proof temporary world-units-per-S value changed unexpectedly")

	if player != null and encounter_controller != null:
		player.eligible_distance_moved.connect(_on_eligible_distance_moved)
		moved_distances.clear()
		var pressure_before: float = encounter_controller.pressure_fraction_s()
		var resolved: float = player.call(
			"_emit_resolved_eligible_distance",
			Vector3(1.0, 0.0, 2.0),
			Vector3(3.0, 7.0, 2.0)
		)
		if absf(resolved - 2.0) > 0.0001:
			failures.append("Player eligible distance must use resolved horizontal displacement only")
		if moved_distances.size() != 1 or absf(moved_distances[0] - 2.0) > 0.0001:
			failures.append("Resolved movement did not emit exactly one eligible-distance signal")
		var expected_pressure := pressure_before + 0.10
		if absf(encounter_controller.pressure_fraction_s() - expected_pressure) > 0.0001:
			failures.append("Field proof did not feed resolved player distance into normalized encounter pressure")

		var pressure_before_vertical: float = encounter_controller.pressure_fraction_s()
		var emitted_count_before_vertical := moved_distances.size()
		var vertical_only: float = player.call(
			"_emit_resolved_eligible_distance",
			Vector3(3.0, 0.0, 2.0),
			Vector3(3.0, 5.0, 2.0)
		)
		if vertical_only != 0.0:
			failures.append("Vertical displacement must not count toward random encounter pressure")
		if moved_distances.size() != emitted_count_before_vertical:
			failures.append("Vertical-only movement emitted eligible encounter distance")
		if absf(encounter_controller.pressure_fraction_s() - pressure_before_vertical) > 0.0001:
			failures.append("Vertical-only movement advanced encounter pressure")

		var pressure_before_zero: float = encounter_controller.pressure_fraction_s()
		var emitted_count_before_zero := moved_distances.size()
		var zero_resolved: float = player.call(
			"_emit_resolved_eligible_distance",
			Vector3(3.0, 0.0, 2.0),
			Vector3(3.0, 0.0, 2.0)
		)
		if zero_resolved != 0.0:
			failures.append("Zero resolved displacement must report zero eligible distance")
		if moved_distances.size() != emitted_count_before_zero:
			failures.append("Zero resolved displacement emitted encounter distance")
		if absf(encounter_controller.pressure_fraction_s() - pressure_before_zero) > 0.0001:
			failures.append("Zero resolved displacement advanced encounter pressure; wall-pushing must not inflate pressure")

		player.set_movement_enabled(false)
		var pressure_before_disabled: float = encounter_controller.pressure_fraction_s()
		var disabled_distance: float = player.call(
			"_emit_resolved_eligible_distance",
			Vector3(3.0, 0.0, 2.0),
			Vector3(7.0, 0.0, 2.0)
		)
		if disabled_distance != 0.0:
			failures.append("Movement-disabled player must not report eligible encounter distance")
		if absf(encounter_controller.pressure_fraction_s() - pressure_before_disabled) > 0.0001:
			failures.append("Movement-disabled displacement advanced encounter pressure")
		player.set_movement_enabled(true)

		encounter_controller.set_authored_paused(true)
		var pressure_before_pause: float = encounter_controller.pressure_fraction_s()
		player.call(
			"_emit_resolved_eligible_distance",
			Vector3(7.0, 0.0, 2.0),
			Vector3(9.0, 0.0, 2.0)
		)
		if absf(encounter_controller.pressure_fraction_s() - pressure_before_pause) > 0.0001:
			failures.append("Authored pause failed to suppress live field encounter pressure")
		encounter_controller.set_authored_paused(false)

		field.call("_on_random_battle_requested", {
			"formation_id": "ch01_greenhollow_l01",
			"tier": "light",
			"exp": 45,
		})
		if encounter_controller.enabled:
			failures.append("Field proof must pause encounter generation after proving a battle request")
		var status = field.get_node_or_null("HUD/PersistenceStatus") as Label
		if status == null or "ch01_greenhollow_l01" not in status.text:
			failures.append("Field proof did not expose the generated encounter request in visible status feedback")

	field.queue_free()
	await process_frame
	_finish(failures)

func _on_eligible_distance_moved(distance: float) -> void:
	moved_distances.append(distance)

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Audit98 live resolved-movement encounter proof validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
