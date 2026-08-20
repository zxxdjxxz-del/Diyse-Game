extends Node3D

const FieldEncounterController = preload("res://game/exploration/field_encounter_controller.gd")

const AREA_ID := "field_proof"
const TALK_DISTANCE_FALLBACK := 3.0
const CHEST_DISTANCE := 2.35
const COMBAT_SCENE := "res://game/combat/combat_proof.tscn"

# Engineering proof tuning only. This is not production map calibration or canon.
const ENCOUNTER_PROOF_CHAPTER := 1
const ENCOUNTER_PROOF_AREA_ID := "ch01_greenhollow"
const ENCOUNTER_PROOF_WORLD_UNITS_PER_S := 20.0
const ENCOUNTER_PROOF_SEED := 9801

const CYANIS_NEUTRAL := "res://game/characters/placeholders/portraits/cyanis_neutral.svg"
const CYANIS_AMUSED := "res://game/characters/placeholders/portraits/cyanis_amused.svg"
const TORREN_NEUTRAL := "res://game/characters/placeholders/portraits/torren_neutral.svg"
const TORREN_DRY := "res://game/characters/placeholders/portraits/torren_dry.svg"

@onready var player = $Cyanis
@onready var torren = $Torren
@onready var torren_sprite: Sprite3D = $Torren/Sprite3D
@onready var interaction_area: Area3D = $Torren/InteractionArea
@onready var chest: StaticBody3D = $ProofChest
@onready var chest_mesh: MeshInstance3D = $ProofChest/MeshInstance3D
@onready var touch_dpad: Control = $HUD/TouchDPad
@onready var talk_button: Button = $HUD/TalkButton
@onready var combat_button: Button = $HUD/CombatTestButton
@onready var save_button: Button = $HUD/SaveButton
@onready var load_button: Button = $HUD/LoadButton
@onready var chest_button: Button = $HUD/ChestButton
@onready var torren_state_button: Button = $HUD/TorrenStateButton
@onready var persistence_status: Label = $HUD/PersistenceStatus
@onready var dialogue_runner: Control = $HUD/DialogueRunner

var encounter_controller
var _player_in_talk_range := false
var _encounter_proof_message := "Encounter proof armed: resolved movement feeds Audit98 pressure."

func _ready() -> void:
	talk_button.pressed.connect(_start_dialogue)
	combat_button.pressed.connect(_start_combat)
	save_button.pressed.connect(_save_game)
	load_button.pressed.connect(_load_game)
	chest_button.pressed.connect(_open_proof_chest)
	torren_state_button.pressed.connect(_toggle_torren_state)
	dialogue_runner.conversation_finished.connect(_on_dialogue_finished)
	interaction_area.body_entered.connect(_on_interaction_body_entered)
	interaction_area.body_exited.connect(_on_interaction_body_exited)
	_setup_encounter_proof()
	_apply_game_state_to_field()
	_consume_transient_encounter_return()
	call_deferred("_refresh_interaction_state")
	_refresh_persistence_visuals(_encounter_proof_message)

func _setup_encounter_proof() -> void:
	encounter_controller = FieldEncounterController.new(ENCOUNTER_PROOF_SEED)
	encounter_controller.name = "EncounterProofController"
	add_child(encounter_controller)
	if not encounter_controller.configure_context(
		ENCOUNTER_PROOF_CHAPTER,
		ENCOUNTER_PROOF_AREA_ID,
		ENCOUNTER_PROOF_WORLD_UNITS_PER_S
	):
		_encounter_proof_message = "Encounter proof unavailable: invalid test context."
		return
	player.eligible_distance_moved.connect(_on_player_eligible_distance_moved)
	encounter_controller.battle_requested.connect(_on_random_battle_requested)

func _consume_transient_encounter_return() -> void:
	var result: Dictionary = GameState.consume_transient_encounter_return()
	if result.is_empty() or encounter_controller == null:
		return
	var outcome := str(result.get("outcome", ""))
	var formation_id := str(result.get("formation_id", ""))
	if not encounter_controller.restore_after_scene_return(outcome, formation_id):
		_encounter_proof_message = "Random encounter return could not restore pressure state."
		return
	match outcome:
		"victory":
			_encounter_proof_message = "Random victory return: %s. Pressure reset; anti-repeat retained." % formation_id
		"successful_flee":
			_encounter_proof_message = "Random flee return: %s. Pressure resumed near 0.65S with 0.20S grace." % formation_id
		"defeat":
			_encounter_proof_message = "Random defeat proof return: %s. Pressure reset for engineering restart." % formation_id

func _process(_delta: float) -> void:
	GameState.current_area = AREA_ID
	GameState.field_position = player.global_position

	var dialogue_active: bool = bool(dialogue_runner.is_running())
	if encounter_controller != null:
		encounter_controller.set_authored_paused(dialogue_active)
	save_button.disabled = dialogue_active
	load_button.disabled = dialogue_active
	if dialogue_active:
		talk_button.visible = false
		combat_button.visible = false
		chest_button.visible = false
		torren_state_button.visible = false
		return

	combat_button.visible = true
	var near_torren := _is_player_in_talk_range()
	talk_button.visible = near_torren
	torren_state_button.visible = near_torren
	chest_button.visible = _is_player_near_chest()
	_update_context_button_text()

	if near_torren and Input.is_key_pressed(KEY_ENTER):
		_start_dialogue()

func _on_player_eligible_distance_moved(distance: float) -> void:
	if encounter_controller == null:
		return
	encounter_controller.advance_eligible_distance(distance)

func _on_random_battle_requested(payload: Dictionary) -> void:
	if not GameState.queue_transient_random_encounter(payload):
		encounter_controller.cancel_battle_request_without_reset()
		_encounter_proof_message = "Random encounter handoff rejected an invalid payload."
		_refresh_persistence_visuals(_encounter_proof_message)
		return
	encounter_controller.set_authored_paused(true)
	GameState.current_area = AREA_ID
	GameState.field_position = player.global_position
	_encounter_proof_message = "Random battle handoff: %s | %s | %d EXP." % [
		str(payload.get("formation_id", "unknown")),
		str(payload.get("tier", "unknown")).to_upper(),
		int(payload.get("exp", 0))
	]
	get_tree().change_scene_to_file(COMBAT_SCENE)

func _on_interaction_body_entered(body: Node3D) -> void:
	if body == player:
		_player_in_talk_range = true
		if not dialogue_runner.is_running():
			talk_button.visible = true
			torren_state_button.visible = true

func _on_interaction_body_exited(body: Node3D) -> void:
	if body == player:
		_player_in_talk_range = false
		if not dialogue_runner.is_running():
			talk_button.visible = false
			torren_state_button.visible = false

func _refresh_interaction_state() -> void:
	_player_in_talk_range = interaction_area.get_overlapping_bodies().has(player)
	if not _player_in_talk_range:
		_player_in_talk_range = player.global_position.distance_to(torren.global_position) <= TALK_DISTANCE_FALLBACK
	if not dialogue_runner.is_running():
		talk_button.visible = _player_in_talk_range
		torren_state_button.visible = _player_in_talk_range
		chest_button.visible = _is_player_near_chest()
		combat_button.visible = true
	_update_context_button_text()

func _is_player_in_talk_range() -> bool:
	if _player_in_talk_range:
		return true
	if interaction_area.get_overlapping_bodies().has(player):
		return true
	return player.global_position.distance_to(torren.global_position) <= TALK_DISTANCE_FALLBACK

func _is_player_near_chest() -> bool:
	return player.global_position.distance_to(chest.global_position) <= CHEST_DISTANCE

func _start_dialogue() -> void:
	if dialogue_runner.is_running() or not _is_player_in_talk_range():
		return
	if encounter_controller != null:
		encounter_controller.set_authored_paused(true)
	player.set_movement_enabled(false)
	touch_dpad.visible = false
	talk_button.visible = false
	combat_button.visible = false
	chest_button.visible = false
	torren_state_button.visible = false
	dialogue_runner.start_conversation(_proof_beats())

func _on_dialogue_finished() -> void:
	if encounter_controller != null:
		encounter_controller.set_authored_paused(false)
	player.set_movement_enabled(true)
	touch_dpad.visible = true
	combat_button.visible = true
	_refresh_interaction_state()

func _start_combat() -> void:
	if dialogue_runner.is_running():
		return
	if encounter_controller != null:
		encounter_controller.set_authored_paused(true)
	GameState.clear_transient_encounter_state()
	GameState.current_area = AREA_ID
	GameState.field_position = player.global_position
	get_tree().change_scene_to_file(COMBAT_SCENE)

func _save_game() -> void:
	GameState.current_area = AREA_ID
	GameState.field_position = player.global_position
	var result: Dictionary = SaveManager.save_state(GameState)
	_refresh_persistence_visuals(str(result.get("message", "Save failed.")))

func _load_game() -> void:
	var result: Dictionary = SaveManager.load_state(GameState)
	if bool(result.get("ok", false)):
		if encounter_controller != null:
			encounter_controller.reset_for_safe_room()
		_apply_game_state_to_field()
		call_deferred("_refresh_interaction_state")
	_refresh_persistence_visuals(str(result.get("message", "Load failed.")))

func _apply_game_state_to_field() -> void:
	if GameState.current_area == AREA_ID:
		player.global_position = GameState.field_position
	_apply_chest_visual()
	_apply_torren_visual()

func _open_proof_chest() -> void:
	if not _is_player_near_chest():
		return
	if bool(GameState.flags.get("proof_chest_opened", false)):
		_refresh_persistence_visuals("Proof chest is already open.")
		return
	GameState.flags["proof_chest_opened"] = true
	GameState.flags["proof_story_flag"] = true
	GameState.rewards["gold"] = int(GameState.rewards.get("gold", 0)) + 25
	GameState.rewards["xp"] = int(GameState.rewards.get("xp", 0)) + 10
	_apply_chest_visual()
	_refresh_persistence_visuals("Proof chest opened: +25 gold, +10 XP; story flag set.")

func _toggle_torren_state() -> void:
	if not _is_player_in_talk_range():
		return
	var current := str(GameState.flags.get("torren_state", "normal"))
	GameState.flags["torren_state"] = "prepared" if current == "normal" else "normal"
	_apply_torren_visual()
	_update_context_button_text()
	_refresh_persistence_visuals("Torren proof state changed to %s." % str(GameState.flags["torren_state"]))

func _apply_chest_visual() -> void:
	var opened := bool(GameState.flags.get("proof_chest_opened", false))
	var material := StandardMaterial3D.new()
	material.roughness = 0.72
	material.albedo_color = Color(0.62, 0.48, 0.16, 1.0) if opened else Color(0.38, 0.23, 0.10, 1.0)
	chest_mesh.material_override = material
	chest_mesh.scale = Vector3(1.0, 0.58, 1.0) if opened else Vector3.ONE

func _apply_torren_visual() -> void:
	var prepared := str(GameState.flags.get("torren_state", "normal")) == "prepared"
	torren_sprite.modulate = Color(1.0, 0.88, 0.68, 1.0) if prepared else Color.WHITE

func _update_context_button_text() -> void:
	chest_button.text = "CHEST OPEN" if bool(GameState.flags.get("proof_chest_opened", false)) else "OPEN CHEST"
	chest_button.disabled = bool(GameState.flags.get("proof_chest_opened", false))
	var torren_state := str(GameState.flags.get("torren_state", "normal"))
	torren_state_button.text = "TORREN: %s" % torren_state.to_upper()

func _refresh_persistence_visuals(message: String = "") -> void:
	_apply_chest_visual()
	_apply_torren_visual()
	_update_context_button_text()
	var chest_state := "OPEN" if bool(GameState.flags.get("proof_chest_opened", false)) else "CLOSED"
	var story_state := "SET" if bool(GameState.flags.get("proof_story_flag", false)) else "UNSET"
	var save_state := "FOUND" if SaveManager.has_save() else "NONE"
	var pressure_text := "OFF"
	if encounter_controller != null:
		pressure_text = "%.3fS" % encounter_controller.pressure_fraction_s()
	persistence_status.text = "%s\nSave: %s | Chest: %s | Torren: %s | Story flag: %s | XP: %d | Gold: %d\nEncounter proof pressure: %s" % [
		message,
		save_state,
		chest_state,
		str(GameState.flags.get("torren_state", "normal")),
		story_state,
		int(GameState.rewards.get("xp", 0)),
		int(GameState.rewards.get("gold", 0)),
		pressure_text
	]

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
