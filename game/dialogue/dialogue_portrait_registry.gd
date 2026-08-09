extends Resource
class_name DiyseDialoguePortraitRegistry

@export var entries: Array[Dictionary] = []

func has_character(character_id: String) -> bool:
	return not _entry_for(character_id).is_empty()

func display_name(character_id: String) -> String:
	if character_id.is_empty():
		return ""
	var entry := _entry_for(character_id)
	return str(entry.get("display_name", character_id))

func has_expression(character_id: String, expression_id: String) -> bool:
	if character_id.is_empty() and expression_id.is_empty():
		return true
	var entry := _entry_for(character_id)
	if entry.is_empty():
		return false
	var portraits = entry.get("portraits", {})
	return portraits is Dictionary and portraits.has(expression_id)

func resolve_portrait(character_id: String, expression_id: String) -> String:
	if character_id.is_empty() or expression_id.is_empty():
		return ""
	var entry := _entry_for(character_id)
	if entry.is_empty():
		return ""
	var portraits = entry.get("portraits", {})
	if not (portraits is Dictionary):
		return ""
	return str(portraits.get(expression_id, ""))

func _entry_for(character_id: String) -> Dictionary:
	for entry in entries:
		if str(entry.get("character_id", "")) == character_id:
			return entry
	return {}
