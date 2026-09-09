extends RefCounted
class_name DiyseDialogueRuntimeContextBuilder

## Curated boundary between live Godot state and the external Dialogue Engine.
##
## This class deliberately does NOT serialize GameState wholesale. The current proof
## GameState still contains implementation-era/stale fields, so dialogue receives only
## the small observable subset explicitly captured here plus whitelisted scene context.

const RUNTIME_CONTEXT_SCHEMA := "diyse_dialogue_runtime_context_v1"
const ALLOWED_DIALOGUE_READINESS := ["GREEN", "AMBER", "RED"]
const ALLOWED_MAP_CONTEXT_STATUS := [
	"current_runtime",
	"provisional_runtime",
	"observed_runtime",
	"unknown_runtime",
]

const ALLOWED_RUNTIME_INPUT_KEYS := [
	"map_context",
	"recent_gameplay",
	"interaction_context",
]

const ALLOWED_MAP_KEYS := [
	"cell_id",
	"area_phase",
	"dialogue_readiness",
	"location_name",
	"visible_facts",
	"route_state",
	"time_context",
	"context_status",
]

const ALLOWED_RECENT_GAMEPLAY_KEYS := [
	"recent_events",
	"recent_combat_summary",
	"recovery_state",
	"fatigue_context",
	"current_task",
]

const ALLOWED_INTERACTION_KEYS := [
	"movement_enabled",
	"input_locked",
	"interaction_id",
	"interaction_kind",
]

# Raw proof/state-container fields are never valid inside the curated runtime payload.
# This blocks accidental "just pass GameState.to_save_dict()" integrations.
const FORBIDDEN_RAW_STATE_KEYS := [
	"inventory",
	"equipment",
	"standard_cards",
	"primes",
	"relic_inventory",
	"forge_components",
	"flags",
	"rewards",
	"gold",
	"bearer",
	"progression_state",
	"available_battle_use_baseline",
]

const PROTECTED_REQUEST_KEYS := [
	"request_id",
	"scene_id",
	"continuity_namespace",
	"story_position",
	"canon_snapshot_id",
	"participants",
	"participant_profiles",
	"scene_purpose",
	"authority_packet",
	"allowed_information_transfers",
	"exact_line_anchors",
	"max_beats",
	"production_cost_ceiling",
]

func build_request(
	request_seed: Dictionary,
	expected_canon_snapshot_id: String,
	runtime_input: Dictionary = {},
	game_state: Node = null,
	encounter_controller: Node = null
) -> Dictionary:
	var failures := validate_request_seed(request_seed, expected_canon_snapshot_id)
	failures.append_array(validate_runtime_input(runtime_input))
	if not failures.is_empty():
		return {"request": {}, "failures": failures}

	var request := request_seed.duplicate(true)
	var original_protected := _protected_snapshot(request_seed)

	var scene_context_value = request.get("scene_context", {})
	if not (scene_context_value is Dictionary):
		return {
			"request": {},
			"failures": ["request_seed.scene_context must be a Dictionary"],
		}
	var scene_context: Dictionary = scene_context_value.duplicate(true)
	if scene_context.has("runtime_observable"):
		return {
			"request": {},
			"failures": [
				"request_seed.scene_context.runtime_observable is runtime-owned and may not be pre-populated"
			],
		}

	var runtime_observable := {
		"schema": RUNTIME_CONTEXT_SCHEMA,
		"provenance": {
			"kind": "live_game_runtime",
			"authority": "observable_context_not_canon_authority",
			"note": "Current owning repository authority remains in authority_packet. Runtime observations may be provisional and must not rewrite canon.",
		},
	}

	var game_capture := _capture_safe_game_state(game_state)
	if not game_capture.is_empty():
		runtime_observable["field"] = game_capture

	var map_context_value = runtime_input.get("map_context", {})
	if map_context_value is Dictionary and not map_context_value.is_empty():
		var map_context: Dictionary = map_context_value.duplicate(true)
		var status := str(map_context.get("context_status", "unknown_runtime"))
		map_context["context_status"] = status
		map_context["authority"] = "runtime_observation_not_story_authority"
		# If current area is available from GameState, it is the runtime area identity.
		# The authored map descriptor may add a cell but cannot spoof a second area ID.
		if runtime_observable.has("field"):
			map_context["area_id"] = str(runtime_observable["field"].get("area_id", ""))
		runtime_observable["map"] = map_context

	var recent_value = runtime_input.get("recent_gameplay", {})
	if recent_value is Dictionary and not recent_value.is_empty():
		runtime_observable["recent_gameplay"] = recent_value.duplicate(true)

	var interaction_value = runtime_input.get("interaction_context", {})
	if interaction_value is Dictionary and not interaction_value.is_empty():
		runtime_observable["interaction"] = interaction_value.duplicate(true)

	var encounter_capture := _capture_safe_encounter_state(encounter_controller)
	if not encounter_capture.is_empty():
		runtime_observable["encounter"] = encounter_capture

	scene_context["runtime_observable"] = runtime_observable
	request["scene_context"] = scene_context

	# current_floor_state remains whatever the authority compiler / explicit caller supplied.
	# This builder never copies GameState.flags or other raw state containers into it.

	var after_protected := _protected_snapshot(request)
	if after_protected != original_protected:
		return {
			"request": {},
			"failures": ["Runtime merge modified a protected compiled request field"],
		}

	return {"request": request, "failures": []}

func validate_request_seed(
	request_seed: Dictionary,
	expected_canon_snapshot_id: String
) -> Array[String]:
	var failures: Array[String] = []
	if expected_canon_snapshot_id.strip_edges().is_empty():
		failures.append("expected_canon_snapshot_id is required")
	if str(request_seed.get("scene_id", "")).is_empty():
		failures.append("request_seed.scene_id is required")
	if str(request_seed.get("story_position", "")).is_empty():
		failures.append("request_seed.story_position is required")
	if str(request_seed.get("scene_purpose", "")).is_empty():
		failures.append("request_seed.scene_purpose is required")

	var snapshot := str(request_seed.get("canon_snapshot_id", ""))
	if snapshot.is_empty():
		failures.append("request_seed.canon_snapshot_id is required")
	elif not expected_canon_snapshot_id.is_empty() and snapshot != expected_canon_snapshot_id:
		failures.append(
			"Canon snapshot mismatch: compiled=%s runtime=%s" % [
				snapshot,
				expected_canon_snapshot_id,
			]
		)

	var authority_packet = request_seed.get("authority_packet", {})
	if not (authority_packet is Dictionary):
		failures.append("request_seed.authority_packet must be a Dictionary")
	else:
		var packet: Dictionary = authority_packet
		if str(packet.get("schema", "")) != "diyse_scene_authority_packet_v1":
			failures.append("request_seed.authority_packet has unsupported schema")
		if str(packet.get("canon_snapshot_id", "")) != snapshot:
			failures.append("authority_packet canon snapshot does not match request seed")

	var participants = request_seed.get("participants", [])
	if not (participants is Array) or participants.is_empty():
		failures.append("request_seed.participants must be a non-empty Array")
	if not (request_seed.get("participant_profiles", {}) is Dictionary):
		failures.append("request_seed.participant_profiles must be a Dictionary")
	if not (request_seed.get("scene_context", {}) is Dictionary):
		failures.append("request_seed.scene_context must be a Dictionary")
	if not (request_seed.get("current_floor_state", {}) is Dictionary):
		failures.append("request_seed.current_floor_state must be a Dictionary")
	return failures

func validate_runtime_input(runtime_input: Dictionary) -> Array[String]:
	var failures: Array[String] = []
	for raw_key in runtime_input.keys():
		var key := str(raw_key)
		if key not in ALLOWED_RUNTIME_INPUT_KEYS:
			failures.append("Unsupported runtime_input field: %s" % key)

	_validate_curated_section(
		runtime_input.get("map_context", {}),
		"runtime_input.map_context",
		ALLOWED_MAP_KEYS,
		failures
	)
	_validate_curated_section(
		runtime_input.get("recent_gameplay", {}),
		"runtime_input.recent_gameplay",
		ALLOWED_RECENT_GAMEPLAY_KEYS,
		failures
	)
	_validate_curated_section(
		runtime_input.get("interaction_context", {}),
		"runtime_input.interaction_context",
		ALLOWED_INTERACTION_KEYS,
		failures
	)

	var map_context = runtime_input.get("map_context", {})
	if map_context is Dictionary:
		var readiness := str(map_context.get("dialogue_readiness", ""))
		if not readiness.is_empty() and readiness not in ALLOWED_DIALOGUE_READINESS:
			failures.append("Unsupported runtime map dialogue_readiness: %s" % readiness)
		var status := str(map_context.get("context_status", "unknown_runtime"))
		if status not in ALLOWED_MAP_CONTEXT_STATUS:
			failures.append("Unsupported runtime map context_status: %s" % status)

	if not _is_json_safe(runtime_input):
		failures.append("runtime_input must contain JSON-safe values only")
	_find_forbidden_raw_keys(runtime_input, "runtime_input", failures)
	return failures

func _validate_curated_section(
	value: Variant,
	label: String,
	allowed_keys: Array,
	failures: Array[String]
) -> void:
	if value == null:
		return
	if not (value is Dictionary):
		failures.append("%s must be a Dictionary" % label)
		return
	var section: Dictionary = value
	for raw_key in section.keys():
		var key := str(raw_key)
		if key not in allowed_keys:
			failures.append("Unsupported %s field: %s" % [label, key])

func _capture_safe_game_state(game_state: Node) -> Dictionary:
	if game_state == null:
		return {}
	var result: Dictionary = {}
	if _has_property(game_state, "current_area"):
		var area_id := str(game_state.get("current_area"))
		if not area_id.is_empty():
			result["area_id"] = area_id
	if _has_property(game_state, "field_position"):
		var position = game_state.get("field_position")
		if position is Vector3:
			result["field_position"] = {
				"x": float(position.x),
				"y": float(position.y),
				"z": float(position.z),
			}
	return result

func _capture_safe_encounter_state(encounter_controller: Node) -> Dictionary:
	if encounter_controller == null:
		return {}
	var result: Dictionary = {}
	for key in ["enabled", "authored_paused", "battle_active", "context_configured", "area_id"]:
		if _has_property(encounter_controller, key):
			var value = encounter_controller.get(key)
			if key == "area_id":
				result[key] = str(value)
			else:
				result[key] = bool(value)
	if encounter_controller.has_method("pressure_fraction_s"):
		result["pressure_fraction_s"] = float(encounter_controller.call("pressure_fraction_s"))
	if encounter_controller.has_method("transition_grace_fraction_s"):
		result["transition_grace_fraction_s"] = float(
			encounter_controller.call("transition_grace_fraction_s")
		)
	if encounter_controller.has_method("has_pending_battle"):
		result["encounter_pending"] = bool(encounter_controller.call("has_pending_battle"))
	return result

func _protected_snapshot(request: Dictionary) -> Dictionary:
	var result: Dictionary = {}
	for key in PROTECTED_REQUEST_KEYS:
		if request.has(key):
			result[key] = request[key]
	return result.duplicate(true)

func _find_forbidden_raw_keys(value: Variant, path: String, failures: Array[String]) -> void:
	if value is Dictionary:
		for raw_key in value.keys():
			var key := str(raw_key)
			if key in FORBIDDEN_RAW_STATE_KEYS:
				failures.append("Raw proof/state field is forbidden in dialogue runtime context: %s.%s" % [path, key])
			_find_forbidden_raw_keys(value[raw_key], "%s.%s" % [path, key], failures)
	elif value is Array:
		for index in range(value.size()):
			_find_forbidden_raw_keys(value[index], "%s[%d]" % [path, index], failures)

func _is_json_safe(value: Variant) -> bool:
	var value_type := typeof(value)
	if value_type in [TYPE_NIL, TYPE_BOOL, TYPE_INT, TYPE_FLOAT, TYPE_STRING]:
		return true
	if value is Array:
		for entry in value:
			if not _is_json_safe(entry):
				return false
		return true
	if value is Dictionary:
		for raw_key in value.keys():
			if typeof(raw_key) != TYPE_STRING:
				return false
			if not _is_json_safe(value[raw_key]):
				return false
		return true
	return false

func _has_property(object: Object, property_name: String) -> bool:
	for property in object.get_property_list():
		if str(property.get("name", "")) == property_name:
			return true
	return false
