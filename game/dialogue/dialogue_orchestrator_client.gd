extends Node
class_name DiyseDialogueOrchestratorClient

## Build-only Godot transport for the external Dialogue Scene Orchestrator.
##
## This client intentionally does not expose /v1/scene/commit. Story-memory commit remains
## an authoring action gated by explicit approval outside normal gameplay runtime.

signal scene_build_completed(response: Dictionary)
signal scene_build_failed(error: Dictionary)

const BUILD_PATH := "/v1/scene/build"
const EXPECTED_HANDOFF_SCHEMA := "diyse_dialogue_scene_packet_v1"

var _base_url := ""
var _auth_token := ""
var _canon_snapshot_id := ""
var _http: HTTPRequest
var _in_flight := false
var _in_flight_request_id := ""
var _in_flight_scene_id := ""
var _validator := DiyseDialogueRuntimeContextBuilder.new()

func configure(
	base_url: String,
	auth_token: String,
	canon_snapshot_id: String
) -> Array[String]:
	var failures: Array[String] = []
	var normalized_url := base_url.strip_edges().trim_suffix("/")
	if normalized_url.is_empty():
		failures.append("Dialogue Orchestrator base URL is required")
	elif not _is_allowed_base_url(normalized_url):
		failures.append("Dialogue Orchestrator URL must use HTTPS (localhost HTTP is allowed for development)")
	if canon_snapshot_id.strip_edges().is_empty():
		failures.append("Dialogue Orchestrator canon snapshot ID is required")
	if not failures.is_empty():
		return failures

	_base_url = normalized_url
	_auth_token = auth_token
	_canon_snapshot_id = canon_snapshot_id.strip_edges()
	return []

func is_configured() -> bool:
	return not _base_url.is_empty() and not _canon_snapshot_id.is_empty()

func is_build_in_flight() -> bool:
	return _in_flight

func prepare_build_transport(request_payload: Dictionary) -> Dictionary:
	var failures: Array[String] = []
	if not is_configured():
		failures.append("Dialogue Orchestrator client is not configured")
	else:
		failures.append_array(
			_validator.validate_request_seed(request_payload, _canon_snapshot_id)
		)

	var scene_context_value = request_payload.get("scene_context", {})
	if scene_context_value is Dictionary:
		var runtime_value = scene_context_value.get("runtime_observable", {})
		if runtime_value is Dictionary and not runtime_value.is_empty():
			if str(runtime_value.get("schema", "")) != DiyseDialogueRuntimeContextBuilder.RUNTIME_CONTEXT_SCHEMA:
				failures.append("Unsupported scene_context.runtime_observable schema")

	if not failures.is_empty():
		return {
			"url": "",
			"headers": PackedStringArray(),
			"body": "",
			"failures": failures,
		}

	var headers := PackedStringArray(["Content-Type: application/json"])
	if not _auth_token.is_empty():
		headers.append("Authorization: Bearer %s" % _auth_token)
	return {
		"url": _base_url + BUILD_PATH,
		"headers": headers,
		"body": JSON.stringify(request_payload),
		"failures": [],
	}

func request_scene_build(request_payload: Dictionary) -> bool:
	if _in_flight:
		_emit_failure({
			"kind": "client_busy",
			"message": "A Dialogue Engine scene build is already in flight.",
		})
		return false

	var transport := prepare_build_transport(request_payload)
	var failures_value = transport.get("failures", [])
	var failures: Array = failures_value if failures_value is Array else []
	if not failures.is_empty():
		_emit_failure({
			"kind": "request_validation",
			"message": "Dialogue Engine build request failed local validation.",
			"failures": failures.duplicate(true),
		})
		return false

	if not is_inside_tree():
		_emit_failure({
			"kind": "client_not_in_tree",
			"message": "Dialogue Orchestrator client must be inside the SceneTree before sending a request.",
		})
		return false

	_ensure_http()
	_in_flight = true
	_in_flight_request_id = str(request_payload.get("request_id", ""))
	_in_flight_scene_id = str(request_payload.get("scene_id", ""))
	var error := _http.request(
		str(transport.get("url", "")),
		transport.get("headers", PackedStringArray()),
		HTTPClient.METHOD_POST,
		str(transport.get("body", ""))
	)
	if error != OK:
		_clear_in_flight()
		_emit_failure({
			"kind": "request_start_failed",
			"message": "Dialogue Orchestrator HTTP request could not start.",
			"error_code": int(error),
		})
		return false
	return true

func validate_build_response(response: Dictionary, expected_request_id: String, expected_scene_id: String) -> Array[String]:
	var failures: Array[String] = []
	if str(response.get("request_id", "")) != expected_request_id:
		failures.append("Dialogue Orchestrator response request_id mismatch")
	if str(response.get("scene_id", "")) != expected_scene_id:
		failures.append("Dialogue Orchestrator response scene_id mismatch")
	if str(response.get("canon_snapshot_id", "")) != _canon_snapshot_id:
		failures.append("Dialogue Orchestrator response canon snapshot mismatch")
	if str(response.get("draft_id", "")).is_empty():
		failures.append("Dialogue Orchestrator response draft_id is required")

	var canon_check = response.get("canon_check", {})
	if not (canon_check is Dictionary):
		failures.append("Dialogue Orchestrator response canon_check must be a Dictionary")
	else:
		var status := str(canon_check.get("status", ""))
		if status not in ["PASS", "FAIL"]:
			failures.append("Dialogue Orchestrator canon_check.status must be PASS or FAIL")

	var handoff = response.get("godot_handoff", {})
	if not (handoff is Dictionary):
		failures.append("Dialogue Orchestrator response godot_handoff must be a Dictionary")
	else:
		if str(handoff.get("schema", "")) != EXPECTED_HANDOFF_SCHEMA:
			failures.append("Dialogue Orchestrator response has unsupported Godot handoff schema")
		if str(handoff.get("scene_id", "")) != expected_scene_id:
			failures.append("Dialogue Orchestrator Godot handoff scene_id mismatch")
	return failures

func _ensure_http() -> void:
	if _http != null and is_instance_valid(_http):
		return
	_http = HTTPRequest.new()
	_http.name = "DialogueOrchestratorHttp"
	add_child(_http)
	_http.request_completed.connect(_on_request_completed)

func _on_request_completed(
	result: int,
	response_code: int,
	_headers: PackedStringArray,
	body: PackedByteArray
) -> void:
	var expected_request_id := _in_flight_request_id
	var expected_scene_id := _in_flight_scene_id
	_clear_in_flight()

	if result != HTTPRequest.RESULT_SUCCESS:
		_emit_failure({
			"kind": "transport_failure",
			"message": "Dialogue Orchestrator transport failed.",
			"result": result,
			"response_code": response_code,
		})
		return
	if response_code < 200 or response_code >= 300:
		_emit_failure({
			"kind": "http_failure",
			"message": "Dialogue Orchestrator returned a non-success HTTP status.",
			"response_code": response_code,
			"body": _safe_error_body(body),
		})
		return

	var body_text := body.get_string_from_utf8()
	var parsed = JSON.parse_string(body_text)
	if not (parsed is Dictionary):
		_emit_failure({
			"kind": "invalid_json_response",
			"message": "Dialogue Orchestrator returned invalid or non-object JSON.",
		})
		return
	var response: Dictionary = parsed
	var failures := validate_build_response(response, expected_request_id, expected_scene_id)
	if not failures.is_empty():
		_emit_failure({
			"kind": "response_validation",
			"message": "Dialogue Orchestrator response failed local validation.",
			"failures": failures,
		})
		return
	scene_build_completed.emit(response.duplicate(true))

func _clear_in_flight() -> void:
	_in_flight = false
	_in_flight_request_id = ""
	_in_flight_scene_id = ""

func _emit_failure(error: Dictionary) -> void:
	scene_build_failed.emit(error.duplicate(true))

func _safe_error_body(body: PackedByteArray) -> String:
	var text := body.get_string_from_utf8()
	if text.length() > 1000:
		return text.left(1000)
	return text

func _is_allowed_base_url(url: String) -> bool:
	if url.find("?") >= 0 or url.find("#") >= 0:
		return false
	if url.begins_with("https://"):
		return true
	return (
		url.begins_with("http://127.0.0.1")
		or url.begins_with("http://localhost")
		or url.begins_with("http://[::1]")
	)
