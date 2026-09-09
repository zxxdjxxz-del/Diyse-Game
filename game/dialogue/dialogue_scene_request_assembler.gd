extends RefCounted
class_name DiyseDialogueSceneRequestAssembler

## Production-facing assembly boundary:
## compiled current authority seed + current map provider + safe live runtime capture.

var _runtime_builder := DiyseDialogueRuntimeContextBuilder.new()

func assemble(
	request_seed: Dictionary,
	expected_canon_snapshot_id: String,
	map_context_provider: Node = null,
	recent_gameplay: Dictionary = {},
	interaction_context: Dictionary = {},
	game_state: Node = null,
	encounter_controller: Node = null
) -> Dictionary:
	var runtime_input: Dictionary = {}

	if map_context_provider != null:
		if not map_context_provider.has_method("dialogue_runtime_map_context"):
			return {
				"request": {},
				"failures": [
					"Map context provider must expose dialogue_runtime_map_context()"
				],
			}
		var map_context_value = map_context_provider.call("dialogue_runtime_map_context")
		if not (map_context_value is Dictionary):
			return {
				"request": {},
				"failures": [
					"dialogue_runtime_map_context() must return a Dictionary"
				],
			}
		var map_context: Dictionary = map_context_value
		if not map_context.is_empty():
			runtime_input["map_context"] = map_context.duplicate(true)

	if not recent_gameplay.is_empty():
		runtime_input["recent_gameplay"] = recent_gameplay.duplicate(true)
	if not interaction_context.is_empty():
		runtime_input["interaction_context"] = interaction_context.duplicate(true)

	return _runtime_builder.build_request(
		request_seed,
		expected_canon_snapshot_id,
		runtime_input,
		game_state,
		encounter_controller
	)
