extends SceneTree

const REGISTRY_PATH := "res://game/content/dialogue/proof/proof_portrait_registry.tres"

var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run")

func _run() -> void:
	var registry = load(REGISTRY_PATH) as DiyseDialoguePortraitRegistry
	_expect(registry != null, "proof portrait registry must load")
	if registry == null:
		_finish()
		return

	var controller := DiyseDialogueScenePreviewController.new()
	get_root().add_child(controller)
	_expect(not controller.has_method("commit_scene"), "preview controller must not expose story-memory commit")

	var assembled_request := _assembled_request()
	var metadata := _authoring_metadata()
	var metadata_failures := controller.validate_preview_metadata(assembled_request, metadata)
	_expect(metadata_failures.is_empty(), "matching preview metadata must pass")

	var mismatched_metadata := metadata.duplicate(true)
	mismatched_metadata["participants"] = ["cyanis"]
	var mismatch_failures := controller.validate_preview_metadata(assembled_request, mismatched_metadata)
	_expect(not mismatch_failures.is_empty(), "preview participant mismatch must fail")

	var pass_response := _build_response("PASS")
	var prepared := controller.prepare_preview_scene(pass_response, metadata, registry)
	_expect(not bool(prepared.get("rejected", true)), "Canon Checker PASS must not be marked rejected")
	_expect((prepared.get("failures", []) as Array).is_empty(), "valid PASS packet must import for preview")
	var scene = prepared.get("scene")
	_expect(scene is DiyseDialogueSceneDefinition, "PASS preview must produce a temporary Dialogue Resource")
	if scene is DiyseDialogueSceneDefinition:
		_expect(scene.scene_id == "PROOF_PREVIEW", "preview scene ID changed")
		_expect(scene.chapter_id == "chapter_00", "explicit authoring chapter metadata was not applied")
		_expect(scene.cutscene_tier == "C1", "preview importer must preserve explicit C-tier")
		_expect(scene.vfx_tier == "V1", "preview importer must preserve explicit V-tier")
		_expect(scene.production_cost_tier == "economical", "qualitative production tier was not preserved")
		_expect(scene.beats.size() == 2, "preview scene beat count is wrong")
		_expect(scene.beats[0].get("speaker_id") == "cyanis", "preview first speaker changed")
		_expect(scene.beats[1].get("speaker_id") == "torren", "preview second speaker changed")

	var fail_response := _build_response("FAIL")
	fail_response["canon_check"]["violations"] = ["knowledge firewall violation"]
	var rejected := controller.prepare_preview_scene(fail_response, metadata, registry)
	_expect(bool(rejected.get("rejected", false)), "Canon Checker FAIL must be a preview rejection")
	_expect(rejected.get("scene") == null, "Canon Checker FAIL must not produce a preview Resource")
	_expect((rejected.get("failures", []) as Array).is_empty(), "Canon Checker FAIL is not an importer failure")
	_expect((rejected.get("violations", []) as Array).size() == 1, "Canon Checker violations must survive preview rejection")

	var malformed := _build_response("PASS")
	malformed["godot_handoff"]["scene_id"] = "WRONG_SCENE"
	var malformed_result := controller.prepare_preview_scene(malformed, metadata, registry)
	_expect(not (malformed_result.get("failures", []) as Array).is_empty(), "mismatched build/handoff scene IDs must fail preview")
	_expect(malformed_result.get("scene") == null, "malformed build must not produce preview Resource")

	var branch_packet := _build_response("PASS")
	branch_packet["godot_handoff"]["beats"][0]["choices"] = ["illegal"]
	var branch_result := controller.prepare_preview_scene(branch_packet, metadata, registry)
	_expect(not (branch_result.get("failures", []) as Array).is_empty(), "preview gate must retain no-dialogue-choice packet validation")

	controller.queue_free()
	await process_frame
	_finish()

func _assembled_request() -> Dictionary:
	return {
		"request_id": "proof-preview-request",
		"scene_id": "PROOF_PREVIEW",
		"continuity_namespace": "story",
		"story_position": "Chapter 0 preview gate proof",
		"canon_snapshot_id": "v2.20-Audit135",
		"participants": ["cyanis", "torren"],
		"participant_profiles": {},
		"scene_purpose": "Validate controlled authoring preview import.",
		"authority_packet": {
			"schema": "diyse_scene_authority_packet_v1",
			"canon_snapshot_id": "v2.20-Audit135",
		},
		"scene_context": {},
		"current_floor_state": {},
		"allowed_information_transfers": [],
		"exact_line_anchors": [],
		"max_beats": 8,
		"production_cost_ceiling": "economical",
	}

func _authoring_metadata() -> Dictionary:
	return {
		"scene_id": "PROOF_PREVIEW",
		"chapter_id": "chapter_00",
		"scene_kind": "proof",
		"location_id": "proof_field",
		"trigger_id": "preview_gate_test",
		"completion_flag": "proof_preview_complete",
		"participants": ["cyanis", "torren"],
		"cutscene_tier": "C1",
		"vfx_tier": "V1",
		"presentation_tags": ["dialogue_engine_preview"],
		"authoring_notes": "Temporary preview only; not production approval.",
	}

func _build_response(status: String) -> Dictionary:
	return {
		"draft_id": "preview-draft-001",
		"request_id": "proof-preview-request",
		"scene_id": "PROOF_PREVIEW",
		"canon_snapshot_id": "v2.20-Audit135",
		"canon_check": {
			"status": status,
			"violations": [],
		},
		"godot_handoff": {
			"schema": "diyse_dialogue_scene_packet_v1",
			"scene_id": "PROOF_PREVIEW",
			"story_position": "Chapter 0 preview gate proof",
			"scene_mode": "full_authored_stop_scene",
			"movement_lock": true,
			"dialogue_readiness": "GREEN",
			"production_cost_tier": "economical",
			"encounter_policy": {
				"during_scene": "not_applicable",
				"after_scene": "not_applicable",
			},
			"beats": [
				{
					"beat_id": "p01",
					"speaker_id": "cyanis",
					"body_text": "We check the road first.",
					"silent": false,
					"action": "glances toward the road",
					"expression_id": "neutral",
					"portrait_side": "left",
					"cues": [],
				},
				{
					"beat_id": "p02",
					"speaker_id": "torren",
					"body_text": "Then stop staring at it.",
					"silent": false,
					"action": "starts walking",
					"expression_id": "dry",
					"portrait_side": "right",
					"cues": [],
				},
			],
			"return_to_gameplay": {
				"control_mode": "exploration",
			},
		},
	}

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Dialogue Engine controlled preview-gate validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
