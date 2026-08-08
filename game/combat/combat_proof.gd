extends Control

const BattleState = preload("res://game/combat/battle_state.gd")
const FIELD_SCENE := "res://game/exploration/field_proof.tscn"

var battle
var party_status: RichTextLabel
var enemy_status: RichTextLabel
var prompt: Label
var command_box: HBoxContainer
var target_box: HBoxContainer
var confirm_button: Button
var next_round_button: Button
var return_button: Button
var log_view: RichTextLabel
var command_buttons: Dictionary = {}
var _current_actor_index := -1
var _pending_command := ""

func _ready() -> void:
	_build_ui()
	battle = BattleState.new()
	battle.setup_demo()
	_refresh_all()
	_select_next_actor()

func _build_ui() -> void:
	var background := ColorRect.new()
	background.color = Color(0.045, 0.055, 0.07, 1.0)
	background.mouse_filter = Control.MOUSE_FILTER_IGNORE
	_place(background, 0.0, 0.0, 1.0, 1.0)
	add_child(background)

	var title := Label.new()
	title.text = "Diyse 7B.5D — Round-Based Combat Proof"
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", 34)
	_place(title, 0.12, 0.025, 0.88, 0.085)
	add_child(title)

	party_status = RichTextLabel.new()
	party_status.bbcode_enabled = true
	party_status.fit_content = false
	party_status.add_theme_font_size_override("normal_font_size", 24)
	_place(party_status, 0.035, 0.10, 0.47, 0.32)
	add_child(party_status)

	enemy_status = RichTextLabel.new()
	enemy_status.bbcode_enabled = true
	enemy_status.fit_content = false
	enemy_status.add_theme_font_size_override("normal_font_size", 24)
	_place(enemy_status, 0.53, 0.10, 0.965, 0.32)
	add_child(enemy_status)

	prompt = Label.new()
	prompt.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	prompt.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	prompt.add_theme_font_size_override("font_size", 28)
	_place(prompt, 0.08, 0.32, 0.92, 0.385)
	add_child(prompt)

	command_box = HBoxContainer.new()
	command_box.alignment = BoxContainer.ALIGNMENT_CENTER
	command_box.add_theme_constant_override("separation", 18)
	_place(command_box, 0.13, 0.39, 0.87, 0.47)
	add_child(command_box)

	for command in ["Attack", "Ability", "Item", "Defend"]:
		var button := Button.new()
		button.text = command
		button.custom_minimum_size = Vector2(220, 72)
		button.focus_mode = Control.FOCUS_NONE
		button.add_theme_font_size_override("font_size", 27)
		button.pressed.connect(_on_command_pressed.bind(command))
		command_box.add_child(button)
		command_buttons[command] = button

	target_box = HBoxContainer.new()
	target_box.alignment = BoxContainer.ALIGNMENT_CENTER
	target_box.add_theme_constant_override("separation", 12)
	_place(target_box, 0.07, 0.485, 0.93, 0.565)
	add_child(target_box)

	confirm_button = Button.new()
	confirm_button.text = "CONFIRM ROUND"
	confirm_button.focus_mode = Control.FOCUS_NONE
	confirm_button.add_theme_font_size_override("font_size", 28)
	confirm_button.pressed.connect(_on_confirm_round)
	_place(confirm_button, 0.38, 0.575, 0.62, 0.645)
	add_child(confirm_button)

	next_round_button = Button.new()
	next_round_button.text = "NEXT ROUND"
	next_round_button.focus_mode = Control.FOCUS_NONE
	next_round_button.add_theme_font_size_override("font_size", 28)
	next_round_button.pressed.connect(_on_next_round)
	_place(next_round_button, 0.38, 0.575, 0.62, 0.645)
	add_child(next_round_button)

	return_button = Button.new()
	return_button.text = "RETURN TO FIELD"
	return_button.focus_mode = Control.FOCUS_NONE
	return_button.add_theme_font_size_override("font_size", 28)
	return_button.pressed.connect(_return_to_field)
	_place(return_button, 0.38, 0.575, 0.62, 0.645)
	add_child(return_button)

	log_view = RichTextLabel.new()
	log_view.bbcode_enabled = true
	log_view.scroll_active = true
	log_view.add_theme_font_size_override("normal_font_size", 22)
	_place(log_view, 0.055, 0.665, 0.945, 0.965)
	add_child(log_view)

func _place(control: Control, left: float, top: float, right: float, bottom: float) -> void:
	control.set_anchors_preset(Control.PRESET_FULL_RECT)
	control.anchor_left = left
	control.anchor_top = top
	control.anchor_right = right
	control.anchor_bottom = bottom
	control.offset_left = 0
	control.offset_top = 0
	control.offset_right = 0
	control.offset_bottom = 0

func _refresh_all() -> void:
	_refresh_status()
	_refresh_log()
	confirm_button.visible = battle.phase == "selecting" and battle.all_living_party_have_actions()
	next_round_button.visible = battle.phase == "round_complete"
	return_button.visible = battle.phase in ["victory", "defeat"]
	command_box.visible = battle.phase == "selecting" and not battle.all_living_party_have_actions()
	if battle.phase != "selecting":
		_clear_targets()

func _refresh_status() -> void:
	var party_text := "[b]PARTY[/b]\n"
	for unit in battle.party:
		party_text += "%s  HP %d/%d  MP %d/%d  SPD %d%s\n" % [
			str(unit["name"]), int(unit["hp"]), int(unit["max_hp"]), int(unit["mp"]), int(unit["max_mp"]), int(unit["speed"]),
			"  [DEFENDING]" if bool(unit["defending"]) else ""
		]
	party_text += "Potions: %d" % int(battle.inventory.get("Potion", 0))
	party_status.text = party_text

	var enemy_text := "[b]ENEMIES[/b]\n"
	for unit in battle.enemies:
		enemy_text += "%s  HP %d/%d  SPD %d%s\n" % [
			str(unit["name"]), int(unit["hp"]), int(unit["max_hp"]), int(unit["speed"]), "  [KO]" if int(unit["hp"]) <= 0 else ""
		]
	enemy_status.text = enemy_text

func _refresh_log() -> void:
	var start := maxi(0, battle.log.size() - 12)
	var lines: Array[String] = []
	for i in range(start, battle.log.size()):
		lines.append(battle.log[i])
	log_view.text = "[b]COMBAT LOG[/b]\n" + "\n".join(lines)
	log_view.scroll_to_line(maxi(0, lines.size() - 1))

func _select_next_actor() -> void:
	if battle.phase != "selecting":
		_refresh_all()
		return
	var selected: Dictionary = {}
	for action in battle.party_actions:
		selected[int(action["actor_index"])] = true
	_current_actor_index = -1
	for i in range(battle.party.size()):
		if int(battle.party[i]["hp"]) > 0 and not selected.has(i):
			_current_actor_index = i
			break
	if _current_actor_index == -1:
		prompt.text = "All conscious party actions selected. Confirm the round."
		_clear_targets()
		_refresh_all()
		return
	var actor: Dictionary = battle.party[_current_actor_index]
	prompt.text = "Select %s's action" % str(actor["name"])
	_pending_command = ""
	_clear_targets()
	command_buttons["Ability"].disabled = int(actor["mp"]) < BattleState.PARTY_ABILITY_MP_COST
	command_buttons["Item"].disabled = int(battle.inventory.get("Potion", 0)) <= 0
	_refresh_all()

func _on_command_pressed(command: String) -> void:
	if battle.phase != "selecting" or _current_actor_index < 0:
		return
	_pending_command = command
	if command == "Defend":
		if battle.queue_party_action(_current_actor_index, command, _current_actor_index):
			_select_next_actor()
		return
	if command in ["Attack", "Ability"]:
		prompt.text = "%s: choose an enemy target" % command
		_show_targets("enemy")
	elif command == "Item":
		prompt.text = "Potion: choose a living party target"
		_show_targets("party")

func _show_targets(side: String) -> void:
	_clear_targets()
	var units: Array = battle.enemies if side == "enemy" else battle.party
	for i in range(units.size()):
		if int(units[i]["hp"]) <= 0:
			continue
		var button := Button.new()
		button.text = "%s\nHP %d/%d" % [str(units[i]["name"]), int(units[i]["hp"]), int(units[i]["max_hp"])]
		button.custom_minimum_size = Vector2(230, 76)
		button.focus_mode = Control.FOCUS_NONE
		button.add_theme_font_size_override("font_size", 21)
		button.pressed.connect(_on_target_pressed.bind(i))
		target_box.add_child(button)

func _clear_targets() -> void:
	for child in target_box.get_children():
		child.queue_free()

func _on_target_pressed(target_index: int) -> void:
	if _pending_command.is_empty() or _current_actor_index < 0:
		return
	if battle.queue_party_action(_current_actor_index, _pending_command, target_index):
		_select_next_actor()

func _on_confirm_round() -> void:
	if not battle.confirm_round():
		return
	if battle.phase == "victory":
		prompt.text = "Victory — 30 XP and 42 gold awarded."
	elif battle.phase == "defeat":
		prompt.text = "Defeat — return to the field to restart the proof."
	else:
		prompt.text = "Round resolved. Review the log, then continue."
	_refresh_all()

func _on_next_round() -> void:
	battle.begin_round()
	_refresh_all()
	_select_next_actor()

func _return_to_field() -> void:
	get_tree().change_scene_to_file(FIELD_SCENE)
