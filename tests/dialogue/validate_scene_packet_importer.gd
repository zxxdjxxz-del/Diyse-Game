extends SceneTree

const PacketImporter = preload("res://game/dialogue/dialogue_scene_packet_importer.gd")

var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run")

func _run() -> void:
	var importer = PacketImporter.new()
	var packet := {
		"schema": "diyse_dialogue_scene_packet_v1",
		"scene_id": "TEST_ORCH_001",
		"story_position": "chapter_03_after_route_recovery",
		"scene_mode": "full_authored_stop_scene",
		"movement_lock": true,
		"dialogue_readiness": "GREEN",
		"production_cost_tier": "economical",
		"encounter_policy": {
			"during_scene": "temporarily_suppress_trigger",
			"after_scene": "restore_prior_pressure",
		},
		"beats": [
			{
				"beat_id": "b01",
				"speaker_id": "torren",
				"body_text": "Road's quieter than it should be.",
				"silent": false,
				"action": "Torren looks back toward the bend.",
				"expression_id": "dry",
				"portrait_side": "right",
				"cues": ["hold_field_camera", "wind_continues"],
			},
			{
				"beat_id": "b02",
				"speaker_id": "cyanis",
				"body_text": "You say that like quiet has personally offended you.",
				"silent": false,
				"action": "",
				"expression_id": "amused",
				"portrait_side": "left",
				"cues": [],
			},
			{
				"beat_id": "b03",
				"speaker_id": null,
				"body_text": "",
				"silent": true,
				"action": "Torren gives him a flat look.",
				"expression_id": null,
				"portrait_side": "right",
				"cues": ["deadpan_hold"],
			},
		],
		"return_to_gameplay": {
			"control_mode": "exploration",
			"handoff_note": "Resume the preserved route pressure after the authored buffer.",
		},
	}
	var metadata := {
		"scene_id": "TEST_ORCH_001",
		"chapter_id": "chapter_03",
		"scene_kind": "banter",
		"location_id": "test_route",
		"trigger_id": "test_orchestrated_trigger",
		"completion_flag": "test_orchestrated_scene_seen",
		"participants": ["cyanis", "torren"],
		"cutscene_tier": "C0",
		"vfx_tier": "V1",
		"presentation_tags": ["field_models", "portrait_optional", "economical"],
		"battle_background_family": "",
		"authoring_notes": "Test fixture for Dialogue Engine packet bridge.",
	}

	var result: Dictionary = importer.build_scene(packet, metadata)
	var import_failures: Array = result.get("failures", [])
	_expect(import_failures.is_empty(), "Valid orchestrator packet must import without failures: %s" % str(import_failures))
	var scene = result.get("scene") as DiyseDialogueSceneDefinition
	_expect(scene != null, "Importer must return a DiyseDialogueSceneDefinition")
	if scene == null:
		_finish()
		return

	_expect(scene.scene_id == "TEST_ORCH_001", "scene_id must survive packet import")
	_expect(scene.chapter_id == "chapter_03", "chapter_id must come from authored metadata")
	_expect(scene.scene_mode == "full_authored_stop_scene", "scene_mode must survive packet import")
	_expect(scene.movement_lock, "movement_lock must survive packet import")
	_expect(scene.dialogue_readiness == "GREEN", "dialogue readiness must survive packet import")
	_expect(scene.production_cost_tier == "economical", "production cost tier must survive packet import")
	_expect(str(scene.encounter_policy.get("during_scene", "")) == "temporarily_suppress_trigger", "encounter policy must survive packet import")
	_expect(str(scene.return_to_gameplay.get("control_mode", "")) == "exploration", "return-to-gameplay mode must survive packet import")
	_expect(scene.beats.size() == 3, "All packet beats must import")

	if scene.beats.size() == 3:
		var first: Dictionary = scene.beats[0]
		var second: Dictionary = scene.beats[1]
		var third: Dictionary = scene.beats[2]
		_expect(str(first.get("speaker_id", "")) == "torren", "First speaker ID must import")
		_expect(str(first.get("text", "")) == "Road's quieter than it should be.", "body_text must map to Resource text")
		_expect(str(first.get("active_side", "")) == "right", "First active portrait side must be right")
		_expect(str((first.get("right", {}) as Dictionary).get("expression_id", "")) == "dry", "First right expression must import")

		_expect(str(second.get("active_side", "")) == "left", "Second active portrait side must be left")
		_expect(str((second.get("left", {}) as Dictionary).get("character_id", "")) == "cyanis", "Second beat must place Cyanis on left")
		_expect(str((second.get("right", {}) as Dictionary).get("character_id", "")) == "torren", "Portrait state must carry Torren forward")

		_expect(str(third.get("speaker_id", "")) == "", "Silent beat must not acquire a speaker")
		_expect(str(third.get("text", "")) == "", "Silent beat must not acquire text")
		_expect(str(third.get("active_side", "")) == "right", "Silent reaction may keep the right portrait active")
		var third_cues: Dictionary = third.get("cues", {})
		_expect(bool(third_cues.get("silent", false)), "Silent packet beat must become a silent cue")
		_expect(str(third_cues.get("action", "")) == "Torren gives him a flat look.", "Packet action must survive inside cues")
		_expect(third_cues.get("staging", []) is Array, "Packet staging list must survive inside cue dictionary")

	var presentation := scene.presentation_metadata()
	_expect(str(presentation.get("scene_mode", "")) == "full_authored_stop_scene", "Runner presentation metadata must expose scene mode")
	_expect(bool(presentation.get("movement_lock", false)), "Runner presentation metadata must expose movement lock")
	_expect(str((presentation.get("encounter_policy", {}) as Dictionary).get("after_scene", "")) == "restore_prior_pressure", "Runner presentation metadata must expose encounter restore behavior")

	var bad_packet := packet.duplicate(true)
	bad_packet["scene_id"] = "TEST_BAD_PACKET"
	bad_packet["beats"] = [
		{
			"beat_id": "b01",
			"speaker_id": null,
			"body_text": "This must fail because text has no speaker.",
			"silent": false,
			"portrait_side": "none",
			"cues": [],
		}
	]
	var bad_metadata := metadata.duplicate(true)
	bad_metadata["scene_id"] = "TEST_BAD_PACKET"
	var bad_result: Dictionary = importer.build_scene(bad_packet, bad_metadata)
	_expect(not (bad_result.get("failures", []) as Array).is_empty(), "Malformed packet must be rejected")

	_finish()

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Dialogue Engine scene-packet importer validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
