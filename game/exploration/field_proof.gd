extends Node3D

const TALK_DISTANCE_FALLBACK := 3.0
const COMBAT_SCENE := "res://game/combat/combat_proof.tscn"

const CYANIS_NEUTRAL := "res://game/characters/placeholders/portraits/cyanis_neutral.svg"
const CYANIS_AMUSED := "res://game/characters/placeholders/portraits/cyanis_amused.svg"
const TORREN_NEUTRAL := "res://game/characters/placeholders/portraits/torren_neutral.svg"
const TORREN_DRY := "res://game/characters/placeholders/portraits/torren_dry.svg"

@onready var player = $Cyanis
@onready var torren = $Torren
@onready var interaction_area: Area3D = $Torren/InteractionArea
@onready var touch_dpad: Control = $HUD/TouchDPad
@onready var talk_button: Button = $HUD/TalkButton
@onready var combat_button: Button = $HUD/CombatTestButton
@onready var dialogue_runner: Control = $HUD/DialogueRunner

var _player_in_talk_range := false

func _ready() -> void:
	talk_button.pressed.connect(_start_dialogue)
	combat_button.pressed.connect(_start_combat)
	dialogue_runner.conversation_finished.connect(_on_dialogue_finished)
	interaction_area.body_entered.connect(_on_interaction_body_entered)
	interaction_area.body_exited.connect(_on_interaction_body_exited)
	call_deferred("_refresh_interaction_state")

func _process(_delta: float) -> void:
	if dialogue_runner.is_running():
		talk_button.visible = false
		combat_button.visible = false
		return

	combat_button.visible = true
	var nearby := _is_player_in_talk_range()
	talk_button.visible = nearby

	if nearby and Input.is_key_pressed(KEY_ENTER):
		_start_dialogue()

func _on_interaction_body_entered(body: Node3D) -> void:
	if body == player:
		_player_in_talk_range = true
		if not dialogue_runner.is_running():
			talk_button.visible = true

func _on_interaction_body_exited(body: Node3D) -> void:
	if body == player:
		_player_in_talk_range = false
		if not dialogue_runner.is_running():
			talk_button.visible = false

func _refresh_interaction_state() -> void:
	_player_in_talk_range = interaction_area.get_overlapping_bodies().has(player)
	if not _player_in_talk_range:
		_player_in_talk_range = player.global_position.distance_to(torren.global_position) <= TALK_DISTANCE_FALLBACK
	if not dialogue_runner.is_running():
		talk_button.visible = _player_in_talk_range
		combat_button.visible = true

func _is_player_in_talk_range() -> bool:
	if _player_in_talk_range:
		return true
	if interaction_area.get_overlapping_bodies().has(player):
		return true
	return player.global_position.distance_to(torren.global_position) <= TALK_DISTANCE_FALLBACK

func _start_dialogue() -> void:
	if dialogue_runner.is_running():
		return
	if not _is_player_in_talk_range():
		return

	player.set_movement_enabled(false)
	touch_dpad.visible = false
	talk_button.visible = false
	combat_button.visible = false
	dialogue_runner.start_conversation(_proof_beats())

func _on_dialogue_finished() -> void:
	player.set_movement_enabled(true)
	touch_dpad.visible = true
	combat_button.visible = true
	_refresh_interaction_state()

func _start_combat() -> void:
	if dialogue_runner.is_running():
		return
	get_tree().change_scene_to_file(COMBAT_SCENE)

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
