extends Node
class_name DiyseDialogueScenePreviewController

## Controlled bridge from an external Scene Orchestrator build to a temporary Godot
## Dialogue Resource for authoring preview.
##
## This controller deliberately does NOT:
## - save the generated Resource into production content;
## - start the DialogueRunner automatically;
## - mark wording approved/canon;
## - call /v1/scene/commit.

signal preview_scene_ready(scene: DiyseDialogueSceneDefinition, build_response: Dictionary)
signal preview_build_rejected(build_response: Dictionary)
signal preview_failed(error: Dictionary)

var _client: DiyseDialogueOrchestratorClient
var _registry: DiyseDialoguePortraitRegistry
var _importer := DiyseDialogueScenePacketImporter.new()
var _pending_metadata: Dictionary = {}
var _pending_scene_id := ""
var _pending_request_id := ""

func bind(
	client: DiyseDialogueOrchestratorClient,
	registry: DiyseDialoguePortraitRegistry
) -> Array[String]:
	unbind()
	var failures: Array[String] = []
	if client == null:
		failures.append("Dialogue preview requires a Dialogue Orchestrator client")
	if registry == null:
		failures.append("Dialogue preview requires a portrait registry")
	if not failures.is_empty():
		return failures
	_client = client
	_registry = registry
	_client.scene_build_completed.connect(_on_scene_build_completed)
	_client.scene_build_failed.connect(_on_scene_build_failed)
	return []

func unbind() -> void:
	_clear_pending()
	if _client != null:
		if _client.scene_build_completed.is_connected(_on_scene_build_completed):
			_client.scene_build_completed.disconnect(_on_scene_build_completed)
		if _client.scene_build_failed.is_connected(_on_scene_build_failed):
			_client.scene_build_failed.disconnect(_on_scene_build_failed)
	_client = null
	_registry = null

func request_preview(
	assembled_request: Dictionary,
	authoring_metadata: Dictionary
) -> bool:
	if _client == null or _registry == null:
		_emit_failure({
			"kind": "preview_not_bound",
			"message": "Dialogue preview controller is not bound to a client and registry.",
		})
		return false
	if not _pending_scene_id.is_empty():
		_emit_failure({
			"kind": "preview_busy",
			"message": "A Dialogue Engine preview build is already pending.",
		})
		return false

	var metadata_failures := validate_preview_metadata(assembled_request, authoring_metadata)
	if not metadata_failures.is_empty():
		_emit_failure({
			"kind": "preview_metadata_validation",
			"message": "Dialogue preview authoring metadata failed validation.",
			"failures": metadata_failures,
		})
		return false

	_pending_scene_id = str(assembled_request.get("scene_id", ""))
	_pending_request_id = str(assembled_request.get("request_id", ""))
	_pending_metadata = authoring_metadata.duplicate(true)
	if not _client.request_scene_build(assembled_request):
		_clear_pending()
		return false
	return true

func validate_preview_metadata(
	assembled_request: Dictionary,
	authoring_metadata: Dictionary
) -> Array[String]:
	var failures := _importer.validate_authoring_metadata(authoring_metadata)
	var scene_id := str(assembled_request.get("scene_id", ""))
	if scene_id.is_empty():
		failures.append("assembled_request.scene_id is required")
	var metadata_scene_id := str(authoring_metadata.get("scene_id", ""))
	if not metadata_scene_id.is_empty() and metadata_scene_id != scene_id:
		failures.append("Preview authoring metadata scene_id does not match assembled request")

	var request_participants_value = assembled_request.get("participants", [])
	var metadata_participants_value = authoring_metadata.get("participants", [])
	if request_participants_value is Array and metadata_participants_value is Array:
		var request_participants := _normalized_string_set(request_participants_value)
		var metadata_participants := _normalized_string_set(metadata_participants_value)
		if request_participants != metadata_participants:
			failures.append("Preview authoring metadata participants do not match assembled request")
	else:
		failures.append("Preview request/metadata participants must be Arrays")
	return failures

func prepare_preview_scene(
	build_response: Dictionary,
	authoring_metadata: Dictionary,
	registry: DiyseDialoguePortraitRegistry
) -> Dictionary:
	var canon_check_value = build_response.get("canon_check", {})
	if not (canon_check_value is Dictionary):
		return {
			"scene": null,
			"rejected": false,
			"failures": ["Build response canon_check must be a Dictionary"],
		}
	var canon_check: Dictionary = canon_check_value
	var status := str(canon_check.get("status", ""))
	if status == "FAIL":
		return {
			"scene": null,
			"rejected": true,
			"violations": (canon_check.get("violations", []) as Array).duplicate(true) if canon_check.get("violations", []) is Array else [],
			"failures": [],
		}
	if status != "PASS":
		return {
			"scene": null,
			"rejected": false,
			"failures": ["Build response canon_check.status must be PASS or FAIL"],
		}

	var packet_value = build_response.get("godot_handoff", {})
	if not (packet_value is Dictionary):
		return {
			"scene": null,
			"rejected": false,
			"failures": ["Build response godot_handoff must be a Dictionary"],
		}
	var packet: Dictionary = packet_value
	var scene_id := str(build_response.get("scene_id", ""))
	if str(packet.get("scene_id", "")) != scene_id:
		return {
			"scene": null,
			"rejected": false,
			"failures": ["Build response and Godot handoff scene IDs do not match"],
		}

	var metadata := authoring_metadata.duplicate(true)
	metadata["scene_id"] = scene_id
	var imported := _importer.build_scene(packet, metadata, registry)
	return {
		"scene": imported.get("scene"),
		"rejected": false,
		"failures": (imported.get("failures", []) as Array).duplicate(true) if imported.get("failures", []) is Array else [],
	}

func _on_scene_build_completed(response: Dictionary) -> void:
	if _pending_scene_id.is_empty():
		return
	if str(response.get("scene_id", "")) != _pending_scene_id or str(response.get("request_id", "")) != _pending_request_id:
		var expected_scene := _pending_scene_id
		_clear_pending()
		_emit_failure({
			"kind": "preview_response_mismatch",
			"message": "Dialogue preview response does not match the pending request.",
			"expected_scene_id": expected_scene,
		})
		return

	var metadata := _pending_metadata.duplicate(true)
	_clear_pending()
	var prepared := prepare_preview_scene(response, metadata, _registry)
	if bool(prepared.get("rejected", false)):
		preview_build_rejected.emit(response.duplicate(true))
		return
	var failures_value = prepared.get("failures", [])
	var failures: Array = failures_value if failures_value is Array else []
	if not failures.is_empty():
		_emit_failure({
			"kind": "preview_import_validation",
			"message": "Dialogue preview packet could not be imported into the current Godot dialogue schema.",
			"failures": failures.duplicate(true),
		})
		return
	var scene = prepared.get("scene")
	if not (scene is DiyseDialogueSceneDefinition):
		_emit_failure({
			"kind": "preview_scene_missing",
			"message": "Dialogue preview import returned no scene Resource.",
		})
		return
	preview_scene_ready.emit(scene, response.duplicate(true))

func _on_scene_build_failed(error: Dictionary) -> void:
	if _pending_scene_id.is_empty():
		return
	_clear_pending()
	_emit_failure(error)

func _clear_pending() -> void:
	_pending_metadata.clear()
	_pending_scene_id = ""
	_pending_request_id = ""

func _emit_failure(error: Dictionary) -> void:
	preview_failed.emit(error.duplicate(true))

func _normalized_string_set(value: Array) -> Array[String]:
	var result: Array[String] = []
	for entry in value:
		var normalized := str(entry).strip_edges().to_lower()
		if not normalized.is_empty() and normalized not in result:
			result.append(normalized)
	result.sort()
	return result
