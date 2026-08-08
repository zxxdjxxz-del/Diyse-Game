extends RefCounted
class_name DiyseRoundResolver

const ITEM_PRIORITY := 0
const DEFEND_PRIORITY := 1
const ORDINARY_PRIORITY := 2

static func priority_for(command: String) -> int:
	match command:
		"Item":
			return ITEM_PRIORITY
		"Defend":
			return DEFEND_PRIORITY
		_:
			return ORDINARY_PRIORITY

static func order_actions(actions: Array) -> Array:
	var ordered := actions.duplicate(true)
	ordered.sort_custom(_comes_before)
	return ordered

static func _comes_before(a: Dictionary, b: Dictionary) -> bool:
	var a_priority := priority_for(str(a.get("command", "Attack")))
	var b_priority := priority_for(str(b.get("command", "Attack")))
	if a_priority != b_priority:
		return a_priority < b_priority

	var a_speed := int(a.get("speed", 0))
	var b_speed := int(b.get("speed", 0))
	if a_speed != b_speed:
		return a_speed > b_speed

	var a_side := str(a.get("side", "enemy"))
	var b_side := str(b.get("side", "enemy"))
	if a_side != b_side:
		return a_side == "party"

	if a_side == "party":
		return int(a.get("tie_order", 0)) < int(b.get("tie_order", 0))

	return int(a.get("stable_order", 0)) < int(b.get("stable_order", 0))
