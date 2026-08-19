extends Resource
class_name DiyseEnvironmentStateDefinition

const STANDARD_STATE_IDS := [
	"BASE",
	"DAMAGED",
	"CLEARED",
	"OPEN",
	"CLOSED",
	"ACTIVE",
	"INACTIVE",
	"POST_BOSS",
	"POST_STORY",
]

@export var environment_id: String = ""
@export var initial_state: String = "BASE"
@export var available_states: Array[String] = ["BASE"]
@export var persistent_flag_prefix: String = ""

func validate_schema() -> Array[String]:
	var failures: Array[String] = []
	if environment_id.is_empty():
		failures.append("environment_id is required")
	if available_states.is_empty():
		failures.append("available_states must contain at least one authored state")
	if initial_state not in available_states:
		failures.append("initial_state must be present in available_states")
	var seen: Dictionary = {}
	for state_id in available_states:
		if state_id.is_empty():
			failures.append("environment state IDs cannot be empty")
		elif seen.has(state_id):
			failures.append("Duplicate environment state ID: %s" % state_id)
		else:
			seen[state_id] = true
	return failures

func allows_state(state_id: String) -> bool:
	return state_id in available_states

func persistent_flag_for(state_id: String) -> String:
	if persistent_flag_prefix.is_empty() or not allows_state(state_id):
		return ""
	return "%s.%s" % [persistent_flag_prefix, state_id.to_lower()]
