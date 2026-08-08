extends Node3D

const TALK_DISTANCE := 2.6

const CYANIS_NEUTRAL := "res://game/characters/placeholders/portraits/cyanis_neutral.svg"
const CYANIS_AMUSED := "res://game/characters/placeholders/portraits/cyanis_amused.svg"
const TORREN_NEUTRAL := "res://game/characters/placeholders/portraits/torren_neutral.svg"
const TORREN_DRY := "res://game/characters/placeholders/portraits/torren_dry.svg"

@onready var player = $Cyanis
@onready var torren = $Torren
@onready var touch_dpad: Control = $HUD/TouchDPad
@onready var talk_button: Button = $HUD/TalkButton
@onready var dialogue_runner: Control = $HUD/DialogueRunner

func _ready() -> void:
	talk_button.pressed.connect(_start_dialogue)
	dialogue_runner.conversation_finished.connect(_on_dialogue_finished)

func _process(_delta: float) -> void:
	if dialogue_runner.is_running():
		talk_button.visible = false
		return

	var nearby := player.global_position.distance_to(torren.global_position) <= TALK_DISTANCE
	talk_button.visible = nearby

	if nearby and Input.is_key_pressed(KEY_ENTER):
		_start_dialogue()

func _start_dialogue() -> void:
	if dialogue_runner.is_running():
		return
	if player.global_position.distance_to(torren.global_position) > TALK_DISTANCE:
		return

	player.set_movement_enabled(false)
	touch_dpad.visible = false
	talk_button.visible = false
	dialogue_runner.start_conversation(_proof_beats())

func _on_dialogue_finished() -> void:
	player.set_movement_enabled(true)
	touch_dpad.visible = true

func _proof_beats() -> Array:
	return [
		{
			"speaker": "Torren",
			"text": "You planning to stand there all afternoon?",
			"left_portrait": CYANIS_NEUTRAL,
			"right_portrait": TORREN_DRY,
			"active_side": "right"
		},
		{
			"speaker": "Cyanis",
			"text": "I was giving you time to improve the welcome.",
			"left_portrait": CYANIS_AMUSED,
			"right_portrait": TORREN_NEUTRAL,
			"active_side": "left"
		},
		{
			"speaker": "",
			"text": "",
			"left_portrait": CYANIS_AMUSED,
			"right_portrait": TORREN_DRY,
			"active_side": "right"
		},
		{
			"speaker": "Torren",
			"text": "No.",
			"left_portrait": CYANIS_AMUSED,
			"right_portrait": TORREN_DRY,
			"active_side": "right"
		}
	]
