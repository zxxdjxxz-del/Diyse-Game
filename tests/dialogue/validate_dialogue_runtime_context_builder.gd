extends SceneTree

var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run")

func _run() -> void:
	GameState.reset_defaults()
	GameState.current_area = "chapter_00_graybox"
	GameState.field_position = Vector3(12.5, 0.9, -172.0)

	var encounters := DiyseFieldEncounterController.new(7001)
	encounters.enabled = true
	encounters.authored_paused = false
	encounters.battle_active = false
	encounters.context_configured = true
	encounters.area_id = "chapter_00_graybox"
	encounters.pressure.distance_s = 0.74
	encounters.pressure.grace_remaining_s = 0.08
	get_root().add_child(encounters)

	var seed := _request_seed()
	var original_seed := seed.duplicate(true)
	var runtime_input := {
		"map_context": {
			"cell_id": "CH00_F02",
			"area_phase": "wreck_field_recovery",
			"dialogue_readiness": "AMBER",
			"location_name": "Wreck Field",
			"visible_facts": [
				"damaged convoy remains are visible",
				"survivors are present in the recovery area",
			],
			"route_state": "player-controlled recovery traversal",
			"context_status": "provisional_runtime",
		},
		"recent_gameplay": {
			"recent_events": ["player crossed from the convoy road into the wreck field"],
			"recent_combat_summary": "combat occurred before this recovery pocket",
			"recovery_state": "brief recovery window",
			"fatigue_context": "not authoritatively quantified",
			"current_task": "inspect the wreck field and survivors",
		},
		"interaction_context": {
			"movement_enabled": true,
			"input_locked": false,
			"interaction_id": "proof_runtime_context",
			"interaction_kind": "field_story_beat",
		},
	}

	var builder := DiyseDialogueRuntimeContextBuilder.new()
	var result := builder.build_request(
		seed,
		"v2.20-Audit135",
		runtime_input,
		GameState,
		encounters
	)
	_expect((result.get("failures", []) as Array).is_empty(), "valid curated runtime merge must pass")
	var request_value = result.get("request", {})
	_expect(request_value is Dictionary, "valid merge must return a request Dictionary")
	var request: Dictionary = request_value if request_value is Dictionary else {}

	_expect(request.get("scene_id") == original_seed.get("scene_id"), "runtime merge changed scene_id")
	_expect(request.get("canon_snapshot_id") == original_seed.get("canon_snapshot_id"), "runtime merge changed canon_snapshot_id")
	_expect(request.get("participants") == original_seed.get("participants"), "runtime merge changed participants")
	_expect(request.get("authority_packet") == original_seed.get("authority_packet"), "runtime merge changed authority_packet")
	_expect(request.get("exact_line_anchors") == original_seed.get("exact_line_anchors"), "runtime merge changed exact-line anchors")
	_expect(request.get("current_floor_state") == original_seed.get("current_floor_state"), "runtime merge changed current_floor_state")

	var scene_context_value = request.get("scene_context", {})
	var scene_context: Dictionary = scene_context_value if scene_context_value is Dictionary else {}
	_expect(scene_context.get("static_seed_note") == "compiled authority-side seed", "static scene context was lost")
	var runtime_value = scene_context.get("runtime_observable", {})
	var runtime: Dictionary = runtime_value if runtime_value is Dictionary else {}
	_expect(runtime.get("schema") == "diyse_dialogue_runtime_context_v1", "runtime schema missing")

	var provenance_value = runtime.get("provenance", {})
	var provenance: Dictionary = provenance_value if provenance_value is Dictionary else {}
	_expect(provenance.get("authority") == "observable_context_not_canon_authority", "runtime provenance must not claim canon authority")

	var field_value = runtime.get("field", {})
	var field: Dictionary = field_value if field_value is Dictionary else {}
	_expect(field.get("area_id") == "chapter_00_graybox", "safe GameState area was not captured")
	var position_value = field.get("field_position", {})
	var position: Dictionary = position_value if position_value is Dictionary else {}
	_expect(is_equal_approx(float(position.get("x", 0.0)), 12.5), "safe field X position was not captured")
	_expect(is_equal_approx(float(position.get("z", 0.0)), -172.0), "safe field Z position was not captured")

	var map_value = runtime.get("map", {})
	var map_context: Dictionary = map_value if map_value is Dictionary else {}
	_expect(map_context.get("cell_id") == "CH00_F02", "map cell was not merged")
	_expect(map_context.get("context_status") == "provisional_runtime", "provisional map status was not retained")
	_expect(map_context.get("authority") == "runtime_observation_not_story_authority", "map context must be labeled non-authoritative")
	_expect(map_context.get("area_id") == "chapter_00_graybox", "runtime area identity should come from safe GameState capture")

	var encounter_value = runtime.get("encounter", {})
	var encounter: Dictionary = encounter_value if encounter_value is Dictionary else {}
	_expect(bool(encounter.get("enabled", false)), "encounter enabled state was not captured")
	_expect(not bool(encounter.get("authored_paused", true)), "encounter authored pause state was not captured")
	_expect(is_equal_approx(float(encounter.get("pressure_fraction_s", 0.0)), 0.74), "encounter pressure was not captured")
	_expect(is_equal_approx(float(encounter.get("transition_grace_fraction_s", 0.0)), 0.08), "encounter grace was not captured")
	_expect(not bool(encounter.get("encounter_pending", true)), "unexpected pending encounter")

	# The proof GameState currently contains stale/internal fields. They must never be serialized
	# merely because GameState was supplied to this builder.
	var runtime_json := JSON.stringify(runtime)
	for forbidden in [
		"Acuity",
		"Change",
		"Auren",
		"Proof Warden Blade",
		"Proof Sword",
		"first_champion",
		"\"gold\"",
		"\"inventory\"",
		"\"equipment\"",
		"\"primes\"",
		"\"flags\"",
	]:
		_expect(runtime_json.find(forbidden) == -1, "raw/stale GameState data leaked into runtime context: %s" % forbidden)

	# Unknown top-level fields cannot use the runtime merge as an authority override channel.
	var protected_injection := runtime_input.duplicate(true)
	protected_injection["authority_packet"] = {"fake": true}
	var protected_result := builder.build_request(seed, "v2.20-Audit135", protected_injection, GameState, encounters)
	_expect(not (protected_result.get("failures", []) as Array).is_empty(), "runtime authority_packet injection must fail")

	# Raw state-container/economy keys are rejected even when nested under an otherwise legal section.
	var raw_state_injection := runtime_input.duplicate(true)
	raw_state_injection["recent_gameplay"] = {
		"recent_events": [],
		"gold": 999,
		"inventory": {"Potion": 99},
	}
	var raw_state_result := builder.build_request(seed, "v2.20-Audit135", raw_state_injection, GameState, encounters)
	_expect(not (raw_state_result.get("failures", []) as Array).is_empty(), "raw proof GameState fields must fail runtime validation")

	var stale_snapshot_result := builder.build_request(seed, "v2.21-Audit999", runtime_input, GameState, encounters)
	_expect(not (stale_snapshot_result.get("failures", []) as Array).is_empty(), "canon snapshot mismatch must fail")

	var collision_seed := seed.duplicate(true)
	collision_seed["scene_context"]["runtime_observable"] = {"spoof": true}
	var collision_result := builder.build_request(collision_seed, "v2.20-Audit135", runtime_input, GameState, encounters)
	_expect(not (collision_result.get("failures", []) as Array).is_empty(), "compiled seed may not pre-populate runtime_observable")

	encounters.queue_free()
	await process_frame
	_finish()

func _request_seed() -> Dictionary:
	return {
		"request_id": "authority:PROOF_RUNTIME_CONTEXT:123456789abc",
		"scene_id": "PROOF_RUNTIME_CONTEXT",
		"continuity_namespace": "story",
		"story_position": "Chapter 0 runtime merge proof",
		"canon_snapshot_id": "v2.20-Audit135",
		"participants": ["cyanis", "ilyra"],
		"participant_profiles": {
			"cyanis": {"source_path": "docs/01_CHARACTERS/PLAYABLE/Cyanis.md"},
			"ilyra": {"source_path": "docs/01_CHARACTERS/PLAYABLE/Ilyra.md"},
		},
		"scene_purpose": "Validate safe live runtime context merging without proof-state leakage.",
		"authority_packet": {
			"schema": "diyse_scene_authority_packet_v1",
			"canon_snapshot_id": "v2.20-Audit135",
			"bundle_sha256": "proof",
		},
		"scene_context": {
			"static_seed_note": "compiled authority-side seed",
		},
		"current_floor_state": {
			"static_authoring_state": "preserve",
		},
		"allowed_information_transfers": [],
		"exact_line_anchors": [],
		"max_beats": 12,
		"production_cost_ceiling": "economical",
	}

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Dialogue Engine curated runtime-context validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
