extends Control

signal conversation_finished

@onready var left_portrait: TextureRect = $Panel/LeftPortrait
@onready var right_portrait: TextureRect = $Panel/RightPortrait
@onready var speaker_label: Label = $Panel/Speaker
@onready var body_label: Label = $Panel/Body
@onready var continue_button: Button = $Panel/Continue
@onready var beat_label: Label = $Panel/BeatHint

var _beats: Array = []
var _index := -1
var _running := false

func _ready() -> void:
	visible = false
	continue_button.pressed.connect(_advance)

func is_running() -> bool:
	return _running

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

	speaker_label.text = speaker
	body_label.text = text
	beat_label.text = "Silent reaction — tap NEXT" if speaker.is_empty() and text.is_empty() else ""

	_set_portrait(left_portrait, left_path)
	_set_portrait(right_portrait, right_path)

	left_portrait.modulate.a = 1.0 if active_side == "left" or active_side == "none" else 0.55
	right_portrait.modulate.a = 1.0 if active_side == "right" or active_side == "none" else 0.55

func _set_portrait(target: TextureRect, resource_path: String) -> void:
	if resource_path.is_empty():
		target.texture = null
		target.visible = false
		return

	var loaded := load(resource_path) as Texture2D
	target.texture = loaded
	target.visible = loaded != null

func _finish() -> void:
	_running = false
	visible = false
	_beats.clear()
	_index = -1
	conversation_finished.emit()
