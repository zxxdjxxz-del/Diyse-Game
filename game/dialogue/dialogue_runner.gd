extends Control

signal conversation_finished
signal scene_started(scene_id: String, presentation: Dictionary)
signal scene_finished(scene_id: String)
signal beat_presented(scene_id: String, beat_id: String, cues: Dictionary)

@onready var left_portrait: TextureRect = $Panel/LeftPortrait
@onready var right_portrait: TextureRect = $Panel/RightPortrait
@onready var speaker_label: Label = $Panel/Speaker
@onready var body_label: Label = $Panel/Body
@onready var continue_button: Button = $Panel/Continue
@onready var beat_label: Label = $Panel/BeatHint

var _beats: Array = []
var _index := -1
var _running := false
var _scene_id := ""
var _scene_presentation: Dictionary = {}

func _ready() -> void:
	visible = false
	continue_button.pressed.connect(_advance)

func is_running() -> bool:
	return _running

func current_scene_presentation() -> Dictionary:
	return _scene_presentation.duplicate(true)

func start_scene(scene_definition: DiyseDialogueSceneDefinition, registry: DiyseDialoguePortraitRegistry) -> bool:
	if scene_definition == null or registry == null:
		return false
	var failures := scene_definition.validate_schema(registry)
	if not failures.is_empty():
		for failure in failures:
			push_error("Dialogue scene validation failed: %s" % failure)
		return false
	var runner_beats := scene_definition.to_runner_beats(registry)
	if runner_beats.is_empty():
		return false
	_scene_id = scene_definition.scene_id
	_scene_presentation = scene_definition.presentation_metadata()
	scene_started.emit(_scene_id, _scene_presentation.duplicate(true))
	start_conversation(runner_beats)
	return true

func start_conversation(beats: Array) -> void:
	if beats.is_empty():
		return
	_beats = beats.duplicate(true)
	_index = -1
	_running = true
	visible = true
	_advance()

func _advance() -> void:
	if not _running:
		return

	_index += 1
	if _index >= _beats.size():
		_finish()
		return

	_apply_beat(_beats[_index])

func _apply_beat(beat: Dictionary) -> void:
	var speaker := str(beat.get("speaker", ""))
	var text := str(beat.get("text", ""))
	var left_path := str(beat.get("left_portrait", ""))
	var right_path := str(beat.get("right_portrait", ""))
	var active_side := str(beat.get("active_side", "none"))
	var beat_id := str(beat.get("beat_id", ""))
	var cues_value = beat.get("cues", {})
	var cues: Dictionary = cues_value.duplicate(true) if cues_value is Dictionary else {}

	speaker_label.text = speaker
	body_label.text = text
	beat_label.text = "Silent reaction — tap NEXT" if speaker.is_empty() and text.is_empty() else ""

	_set_portrait(left_portrait, left_path)
	_set_portrait(right_portrait, right_path)

	left_portrait.modulate.a = 1.0 if active_side == "left" or active_side == "none" else 0.55
	right_portrait.modulate.a = 1.0 if active_side == "right" or active_side == "none" else 0.55
	beat_presented.emit(_scene_id, beat_id, cues)

func _set_portrait(target: TextureRect, resource_path: String) -> void:
	if resource_path.is_empty():
		target.texture = null
		target.visible = false
		return

	var loaded := load(resource_path) as Texture2D
	target.texture = loaded
	target.visible = loaded != null

func _finish() -> void:
	var finished_scene_id := _scene_id
	_running = false
	visible = false
	_beats.clear()
	_index = -1
	_scene_id = ""
	_scene_presentation.clear()
	if not finished_scene_id.is_empty():
		scene_finished.emit(finished_scene_id)
	conversation_finished.emit()
