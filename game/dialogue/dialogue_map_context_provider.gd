extends Node
class_name DiyseDialogueMapContextProvider

## Small map-facing adapter for Dialogue Engine runtime observations.
##
## A field/map controller may update this provider as the player moves between authored
## cells/phases. The provider never turns map data into canon; it only exposes a current
## observable snapshot through dialogue_runtime_map_context().

signal context_changed(context: Dictionary)

var _context: Dictionary = {}
var _validator := DiyseDialogueRuntimeContextBuilder.new()

func set_context(context: Dictionary) -> Array[String]:
	var failures := _validator.validate_runtime_input({"map_context": context})
	if not failures.is_empty():
		return failures
	_context = context.duplicate(true)
	context_changed.emit(_context.duplicate(true))
	return []

func clear_context() -> void:
	if _context.is_empty():
		return
	_context.clear()
	context_changed.emit({})

func has_context() -> bool:
	return not _context.is_empty()

func dialogue_runtime_map_context() -> Dictionary:
	return _context.duplicate(true)
