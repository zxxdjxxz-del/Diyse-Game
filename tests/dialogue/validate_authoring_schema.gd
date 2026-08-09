extends SceneTree

const REGISTRY_PATH := "res://game/content/dialogue/proof/proof_portrait_registry.tres"
const SCENE_PATH := "res://game/content/dialogue/proof/PROOF_SCHEMA.tres"

var failures: Array[String] = []

func _initialize() -> void:
	var registry = load(REGISTRY_PATH)
	var scene = load(SCENE_PATH)
	_expect(registry != null, "Portrait registry fixture must load")
	_expect(scene != null, "Production dialogue schema fixture must load")
	if registry == null or scene == null:
		_finish()
		return

	_test_valid_fixture(scene, registry)
	_test_runner_adapter(scene, registry)
	_test_choice_fields_are_rejected(scene, registry)
	_test_duplicate_beat_ids_are_rejected(scene, registry)
	_test_unknown_expression_is_rejected(scene, registry)
	_finish()

func _test_valid_fixture(scene, registry) -> void:
	var schema_failures: Array[String] = scene.validate_schema(registry)
	_expect(schema_failures.is_empty(), "Valid non-canon production dialogue fixture must pass schema validation: %s" % str(schema_failures))
	_expect(str(scene.scene_id) == "PROOF_SCHEMA", "Proof scene must use a non-production PROOF_ scene ID")
	_expect(str(scene.completion_flag) == "scene.proof_schema.complete", "Scene completion flag must be explicit data")
	_expect(str(scene.trigger_id) == "trigger.proof.schema", "Scene trigger ID must be explicit data")
	_expect(scene.participants == ["cyanis", "torren"], "Participant IDs must remain stable lowercase IDs")
	_expect(scene.beats.size() == 3, "Proof fixture should contain three beats including one silent reaction")
	for beat in scene.beats:
		for forbidden in scene.FORBIDDEN_BRANCH_KEYS:
			_expect(not beat.has(forbidden), "Valid authored beats must contain no choice/response/branch key: %s" % forbidden)

func _test_runner_adapter(scene, registry) -> void:
	var beats: Array[Dictionary] = scene.to_runner_beats(registry)
	_expect(beats.size() == 3, "Scene adapter must emit one runner beat per authored beat")
	if beats.size() < 3:
		return
	_expect(str(beats[0].get("speaker", "")) == "Torren", "Stable speaker_id must resolve through the registry to display name")
	_expect(str(beats[0].get("right_portrait", "")).ends_with("torren_dry.svg"), "Portrait expression ID must resolve through registry indirection")
	_expect(str(beats[1].get("left_portrait", "")).ends_with("cyanis_amused.svg"), "Cyanis expression ID must resolve without embedding an asset path in scene data")
	_expect(str(beats[2].get("speaker", "")).is_empty() and str(beats[2].get("text", "")).is_empty(), "Silent reaction beat must survive adaptation with no spoken line")
	var cues: Dictionary = beats[2].get("cues", {})
	_expect("SILENT_REACTION" in cues.get("implementation_flags", []), "Opaque implementation cue metadata must survive adaptation")

func _test_choice_fields_are_rejected(scene, registry) -> void:
	var invalid = scene.duplicate(true)
	invalid.beats = scene.beats.duplicate(true)
	invalid.beats[0]["choices"] = [{"text": "Forbidden"}]
	var found := false
	for message in invalid.validate_schema(registry):
		if "forbidden dialogue-choice field" in message:
			found = true
	_expect(found, "Schema must reject dialogue choices rather than silently accepting branching player responses")

func _test_duplicate_beat_ids_are_rejected(scene, registry) -> void:
	var invalid = scene.duplicate(true)
	invalid.beats = scene.beats.duplicate(true)
	invalid.beats[1]["beat_id"] = str(invalid.beats[0]["beat_id"])
	var found := false
	for message in invalid.validate_schema(registry):
		if "Duplicate beat_id" in message:
			found = true
	_expect(found, "Schema must reject duplicate stable beat IDs")

func _test_unknown_expression_is_rejected(scene, registry) -> void:
	var invalid = scene.duplicate(true)
	invalid.beats = scene.beats.duplicate(true)
	var left: Dictionary = invalid.beats[0]["left"].duplicate(true)
	left["expression_id"] = "invented_expression"
	invalid.beats[0]["left"] = left
	var found := false
	for message in invalid.validate_schema(registry):
		if "unknown expression_id" in message:
			found = true
	_expect(found, "Schema must reject unregistered expression IDs instead of inventing portrait assets")

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse 7B.6 production dialogue authoring schema validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
