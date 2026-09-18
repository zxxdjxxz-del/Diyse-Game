extends SceneTree

var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run")

func _run() -> void:
	var game_state := get_root().get_node_or_null("GameState")
	if game_state == null:
		failures.append("GameState autoload is unavailable")
		_finish()
		return
	game_state.call("reset_defaults")
	game_state.set("current_area", "chapter_00_graybox")
	game_state.set("field_position", Vector3(1.0, 0.9, -330.0))

	var provider := DiyseDialogueMapContextProvider.new()
	get_root().add_child(provider)
	var provider_failures := provider.set_context({
		"cell_id": "CH00_F03",
		"location_name": "Recovery Line",
		"area_phase": "recovery_line",
		"dialogue_readiness": "AMBER",
		"context_status": "provisional_runtime",
		"visible_facts": ["the damaged recovery route is visible"],
	})
	_expect(provider_failures.is_empty(), "valid map provider context must be accepted")
	_expect(provider.has_context(), "map provider must retain accepted context")

	var invalid_provider_failures := provider.set_context({
		"cell_id": "CH00_F03",
		"inventory": {"Potion": 99},
		"context_status": "provisional_runtime",
	})
	_expect(not invalid_provider_failures.is_empty(), "map provider must reject raw state fields")
	_expect(
		provider.dialogue_runtime_map_context().get("cell_id") == "CH00_F03",
		"rejected map update must not replace last valid context"
	)

	var encounters := DiyseFieldEncounterController.new(7010)
	encounters.enabled = true
	encounters.context_configured = true
	encounters.area_id = "chapter_00_graybox"
	encounters.pressure.distance_s = 0.52
	get_root().add_child(encounters)

	var assembler := DiyseDialogueSceneRequestAssembler.new()
	var assembled := assembler.assemble(
		_request_seed(),
		"v2.20-Audit135",
		provider,
		{
			"recent_events": ["the player entered the recovery line"],
			"current_task": "continue toward the relay yard",
		},
		{
			"movement_enabled": true,
			"input_locked": false,
			"interaction_kind": "field_story_beat",
		},
		game_state,
		encounters
	)
	_expect((assembled.get("failures", []) as Array).is_empty(), "valid assembled scene request must pass")

	var request_value = assembled.get("request", {})
	var request: Dictionary = request_value if request_value is Dictionary else {}
	var scene_context_value = request.get("scene_context", {})
	var scene_context: Dictionary = scene_context_value if scene_context_value is Dictionary else {}
	var runtime_value = scene_context.get("runtime_observable", {})
	var runtime: Dictionary = runtime_value if runtime_value is Dictionary else {}
	var map_value = runtime.get("map", {})
	var map_context: Dictionary = map_value if map_value is Dictionary else {}
	var encounter_value = runtime.get("encounter", {})
	var encounter: Dictionary = encounter_value if encounter_value is Dictionary else {}

	_expect(map_context.get("cell_id") == "CH00_F03", "assembler did not pull current map-provider cell")
	_expect(map_context.get("context_status") == "provisional_runtime", "assembler lost map provisional status")
	_expect(map_context.get("area_id") == "chapter_00_graybox", "safe live area was not merged")
	_expect(is_equal_approx(float(encounter.get("pressure_fraction_s", 0.0)), 0.52), "assembler did not merge encounter pressure")
	_expect(request.get("authority_packet") == _request_seed().get("authority_packet"), "assembler modified compiled authority")

	var no_map := assembler.assemble(
		_request_seed(),
		"v2.20-Audit135",
		null,
		{},
		{},
		game_state,
		encounters
	)
	_expect((no_map.get("failures", []) as Array).is_empty(), "map provider should be optional for non-map scenes")
	var no_map_request_value = no_map.get("request", {})
	var no_map_request: Dictionary = no_map_request_value if no_map_request_value is Dictionary else {}
	var no_map_scene_context_value = no_map_request.get("scene_context", {})
	var no_map_scene_context: Dictionary = no_map_scene_context_value if no_map_scene_context_value is Dictionary else {}
	var no_map_runtime_value = no_map_scene_context.get("runtime_observable", {})
	var no_map_runtime: Dictionary = no_map_runtime_value if no_map_runtime_value is Dictionary else {}
	_expect(not no_map_runtime.has("map"), "null map provider must not fabricate map context")

	var bad_provider := Node.new()
	get_root().add_child(bad_provider)
	var bad := assembler.assemble(
		_request_seed(),
		"v2.20-Audit135",
		bad_provider,
		{},
		{},
		game_state,
		encounters
	)
	_expect(not (bad.get("failures", []) as Array).is_empty(), "provider without contract method must fail")

	bad_provider.queue_free()
	provider.queue_free()
	encounters.queue_free()
	await process_frame
	_finish()

func _request_seed() -> Dictionary:
	return {
		"request_id": "authority:PROOF_ASSEMBLER:abcdef012345",
		"scene_id": "PROOF_ASSEMBLER",
		"continuity_namespace": "story",
		"story_position": "Chapter 0 request assembly proof",
		"canon_snapshot_id": "v2.20-Audit135",
		"participants": ["cyanis", "ilyra"],
		"participant_profiles": {
			"cyanis": {"source_path": "docs/01_CHARACTERS/PLAYABLE/Cyanis.md"},
			"ilyra": {"source_path": "docs/01_CHARACTERS/PLAYABLE/Ilyra.md"},
		},
		"scene_purpose": "Validate compiled authority plus live map/runtime assembly.",
		"authority_packet": {
			"schema": "diyse_scene_authority_packet_v1",
			"canon_snapshot_id": "v2.20-Audit135",
			"bundle_sha256": "proof",
		},
		"scene_context": {},
		"current_floor_state": {},
		"allowed_information_transfers": [],
		"exact_line_anchors": [],
		"max_beats": 10,
		"production_cost_ceiling": "economical",
	}

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Dialogue Engine map-provider request assembly validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
