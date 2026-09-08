extends SceneTree

const BridgeScript = preload("res://game/dialogue/dialogue_field_bridge.gd")

class FakeRunner:
	extends Node
	signal scene_started(scene_id: String, presentation: Dictionary)
	signal scene_finished(scene_id: String)

class FakePlayer:
	extends Node
	var enabled := true
	func set_movement_enabled(value: bool) -> void:
		enabled = value
	func movement_enabled() -> bool:
		return enabled

var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run")

func _run() -> void:
	var runner := FakeRunner.new()
	var player := FakePlayer.new()
	var encounters := DiyseFieldEncounterController.new(777)
	var bridge = BridgeScript.new()

	root.add_child(runner)
	root.add_child(player)
	root.add_child(encounters)
	root.add_child(bridge)
	bridge.bind(runner, player, encounters)

	encounters.pressure.distance_s = 0.72
	encounters.pressure.next_check_s = 0.75
	var before_distance := float(encounters.pressure.distance_s)
	var before_next_check := float(encounters.pressure.next_check_s)

	var stop_metadata := {
		"scene_mode": "full_authored_stop_scene",
		"movement_lock": true,
		"dialogue_readiness": "GREEN",
		"encounter_policy": {
			"during_scene": "temporarily_suppress_trigger",
			"after_scene": "restore_prior_pressure",
		},
	}
	runner.scene_started.emit("TEST_STOP", stop_metadata)
	_expect(not player.movement_enabled(), "Stop scene must lock movement when movement_lock=true")
	_expect(encounters.authored_paused, "Authored dialogue suppression must pause encounter triggering")
	_expect(_near(float(encounters.pressure.distance_s), before_distance), "Starting dialogue must not reset accumulated encounter pressure")
	_expect(_near(float(encounters.pressure.next_check_s), before_next_check), "Starting dialogue must not move the next encounter check")
	_expect(bridge.active_scene_id() == "TEST_STOP", "Bridge must retain active scene identity")

	runner.scene_finished.emit("TEST_STOP")
	_expect(player.movement_enabled(), "Finishing stop scene must restore prior movement state")
	_expect(not encounters.authored_paused, "Finishing stop scene must restore prior authored-pause state")
	_expect(_near(float(encounters.pressure.distance_s), before_distance), "Finishing dialogue must preserve accumulated encounter pressure")
	_expect(_near(float(encounters.pressure.next_check_s), before_next_check), "Finishing dialogue must preserve next encounter check")

	var walking_metadata := {
		"scene_mode": "walking_or_traversal_dialogue",
		"movement_lock": false,
		"dialogue_readiness": "AMBER",
		"encounter_policy": {
			"during_scene": "temporarily_suppress_trigger",
			"after_scene": "restore_prior_pressure",
		},
	}
	runner.scene_started.emit("TEST_WALK", walking_metadata)
	_expect(player.movement_enabled(), "Walking dialogue must preserve movement when movement_lock=false")
	_expect(encounters.authored_paused, "Walking dialogue may suppress encounter triggering without stopping traversal")
	runner.scene_finished.emit("TEST_WALK")
	_expect(player.movement_enabled(), "Walking-dialogue finish must keep prior enabled movement state")
	_expect(not encounters.authored_paused, "Walking-dialogue finish must restore encounter pause state")
	_expect(_near(float(encounters.pressure.distance_s), before_distance), "Walking dialogue suppression must preserve pressure rather than safe-reset it")

	# Existing outer authored locks must survive a nested dialogue policy application.
	player.set_movement_enabled(false)
	encounters.set_authored_paused(true)
	runner.scene_started.emit("TEST_PRELOCKED", stop_metadata)
	_expect(not player.movement_enabled(), "Pre-existing movement lock must remain locked during dialogue")
	_expect(encounters.authored_paused, "Pre-existing authored encounter pause must remain paused during dialogue")
	runner.scene_finished.emit("TEST_PRELOCKED")
	_expect(not player.movement_enabled(), "Dialogue finish must restore a pre-existing movement lock")
	_expect(encounters.authored_paused, "Dialogue finish must restore a pre-existing authored encounter pause")

	var invalid_metadata := {
		"scene_mode": "full_authored_stop_scene",
		"movement_lock": true,
		"dialogue_readiness": "GREEN",
		"encounter_policy": {
			"during_scene": "reset_everything",
			"after_scene": "restore_prior_pressure",
		},
	}
	var validation: Array[String] = bridge.validate_metadata(invalid_metadata)
	_expect(not validation.is_empty(), "Unsupported encounter policies must be rejected")

	bridge.unbind()
	_finish()

func _near(a: float, b: float) -> bool:
	return absf(a - b) < 0.00001

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse dialogue field bridge validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
