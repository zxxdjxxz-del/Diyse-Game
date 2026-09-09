extends SceneTree

var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run")

func _run() -> void:
	var client := DiyseDialogueOrchestratorClient.new()
	get_root().add_child(client)

	var bad_url := client.configure("http://example.com", "secret", "v2.20-Audit135")
	_expect(not bad_url.is_empty(), "non-local HTTP Orchestrator endpoint must be rejected")

	var config_failures := client.configure(
		"https://dialogue.example.test/",
		"test-token-do-not-log",
		"v2.20-Audit135"
	)
	_expect(config_failures.is_empty(), "valid HTTPS Orchestrator configuration must pass")
	_expect(client.is_configured(), "client should report configured")
	_expect(not client.has_method("commit_scene"), "game client must not expose a story-memory commit helper")

	var request := _request_payload()
	var transport := client.prepare_build_transport(request)
	_expect((transport.get("failures", []) as Array).is_empty(), "valid assembled request must prepare for transport")
	_expect(transport.get("url") == "https://dialogue.example.test/v1/scene/build", "build endpoint URL is wrong")

	var headers_value = transport.get("headers", PackedStringArray())
	var headers: PackedStringArray = headers_value if headers_value is PackedStringArray else PackedStringArray()
	_expect(headers.has("Content-Type: application/json"), "JSON content type header missing")
	_expect(headers.has("Authorization: Bearer test-token-do-not-log"), "Bearer authorization header missing")

	var body := str(transport.get("body", ""))
	_expect(body.find("test-token-do-not-log") == -1, "auth token must never be serialized into request body")
	var parsed_body = JSON.parse_string(body)
	_expect(parsed_body is Dictionary, "prepared request body must be JSON object")
	if parsed_body is Dictionary:
		_expect(parsed_body.get("scene_id") == "PROOF_CLIENT", "transport body changed scene ID")
		_expect(parsed_body.get("canon_snapshot_id") == "v2.20-Audit135", "transport body changed snapshot")

	var wrong_snapshot := request.duplicate(true)
	wrong_snapshot["canon_snapshot_id"] = "v2.19-Audit134"
	var wrong_snapshot_transport := client.prepare_build_transport(wrong_snapshot)
	_expect(not (wrong_snapshot_transport.get("failures", []) as Array).is_empty(), "mismatched request snapshot must be rejected before HTTP")

	var wrong_runtime_schema := request.duplicate(true)
	wrong_runtime_schema["scene_context"]["runtime_observable"]["schema"] = "stale_runtime_schema"
	var wrong_runtime_transport := client.prepare_build_transport(wrong_runtime_schema)
	_expect(not (wrong_runtime_transport.get("failures", []) as Array).is_empty(), "stale runtime context schema must be rejected before HTTP")

	var good_response := _response_payload("PASS")
	var response_failures := client.validate_build_response(good_response, "proof-client-request", "PROOF_CLIENT")
	_expect(response_failures.is_empty(), "valid Orchestrator build response must pass local validation")

	var valid_fail_response := _response_payload("FAIL")
	var fail_response_validation := client.validate_build_response(valid_fail_response, "proof-client-request", "PROOF_CLIENT")
	_expect(fail_response_validation.is_empty(), "Canon Checker FAIL is a valid build response, not a transport failure")

	var wrong_response_scene := _response_payload("PASS")
	wrong_response_scene["godot_handoff"]["scene_id"] = "OTHER_SCENE"
	var wrong_response_failures := client.validate_build_response(wrong_response_scene, "proof-client-request", "PROOF_CLIENT")
	_expect(not wrong_response_failures.is_empty(), "mismatched handoff scene ID must be rejected")

	var wrong_response_snapshot := _response_payload("PASS")
	wrong_response_snapshot["canon_snapshot_id"] = "v2.19-Audit134"
	var wrong_snapshot_failures := client.validate_build_response(wrong_response_snapshot, "proof-client-request", "PROOF_CLIENT")
	_expect(not wrong_snapshot_failures.is_empty(), "mismatched response snapshot must be rejected")

	client.queue_free()
	await process_frame
	_finish()

func _request_payload() -> Dictionary:
	return {
		"request_id": "proof-client-request",
		"scene_id": "PROOF_CLIENT",
		"continuity_namespace": "story",
		"story_position": "Dialogue Orchestrator client transport proof",
		"canon_snapshot_id": "v2.20-Audit135",
		"participants": ["cyanis", "ilyra"],
		"participant_profiles": {
			"cyanis": {"source_path": "docs/01_CHARACTERS/PLAYABLE/Cyanis.md"},
			"ilyra": {"source_path": "docs/01_CHARACTERS/PLAYABLE/Ilyra.md"},
		},
		"scene_purpose": "Validate build-only Godot transport into the external Scene Orchestrator.",
		"authority_packet": {
			"schema": "diyse_scene_authority_packet_v1",
			"canon_snapshot_id": "v2.20-Audit135",
			"bundle_sha256": "proof",
		},
		"scene_context": {
			"runtime_observable": {
				"schema": "diyse_dialogue_runtime_context_v1",
				"provenance": {
					"authority": "observable_context_not_canon_authority",
				},
			},
		},
		"current_floor_state": {},
		"allowed_information_transfers": [],
		"exact_line_anchors": [],
		"max_beats": 10,
		"production_cost_ceiling": "economical",
	}

func _response_payload(status: String) -> Dictionary:
	return {
		"draft_id": "draft-proof-001",
		"request_id": "proof-client-request",
		"scene_id": "PROOF_CLIENT",
		"canon_snapshot_id": "v2.20-Audit135",
		"participant_sources": {"cyanis": "profile", "ilyra": "profile"},
		"agent_snapshots": {},
		"expected_previous_revisions": {},
		"director_plan": {},
		"scene_beats": [],
		"canon_check": {
			"status": status,
			"violations": [],
		},
		"commit_ready": status == "PASS",
		"commit_bundle": {},
		"godot_handoff": {
			"schema": "diyse_dialogue_scene_packet_v1",
			"scene_id": "PROOF_CLIENT",
			"story_position": "Dialogue Orchestrator client transport proof",
			"scene_mode": "full_authored_stop_scene",
			"movement_lock": true,
			"dialogue_readiness": "GREEN",
			"production_cost_tier": "economical",
			"encounter_policy": {},
			"beats": [],
			"return_to_gameplay": {},
		},
		"candidate_audit": [],
	}

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Dialogue Engine Godot Orchestrator client validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
