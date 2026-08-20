extends Control

const BattleState = preload("res://game/combat/battle_state.gd")
const GeneratedBattleState = preload("res://game/combat/generated_encounter_battle_state.gd")
const ProofEnemyCombatData = preload("res://game/content/encounters/proof_enemy_combat_data.gd")
const FIELD_SCENE := "res://game/exploration/field_proof.tscn"

var battle
var title_label: Label
var party_status: RichTextLabel
var enemy_status: RichTextLabel
var prompt: Label
var command_box: HBoxContainer
var target_box: HBoxContainer
var confirm_button: Button
var next_round_button: Button
var return_button: Button
var flee_button: Button
var log_view: RichTextLabel
var command_buttons: Dictionary = {}
var _current_actor_index := -1
var _pending_command := ""
var _pending_content_id := ""
var _pending_prime_command_id := ""
var _generated_random_encounter := false
var _generated_reward_applied := false

func _ready() -> void:
	_build_ui()
	if not _setup_transient_random_battle():
		battle = BattleState.new()
		battle.setup_demo()
	_refresh_title()
	_refresh_all()
	_select_next_actor()

func _setup_transient_random_battle() -> bool:
	if not GameState.has_transient_random_encounter():
		return false
	var payload: Dictionary = GameState.transient_random_encounter_payload()
	var enemy_definitions: Array[Dictionary] = ProofEnemyCombatData.build_units(payload.get("enemies", []))
	if enemy_definitions.is_empty():
		GameState.clear_transient_encounter_state()
		return false
	var generated = GeneratedBattleState.new()
	if not generated.setup_generated_formation(
		enemy_definitions,
		int(payload.get("exp", 0)),
		0,
		str(payload.get("formation_id", ""))
	):
		GameState.clear_transient_encounter_state()
		return false
	battle = generated
	_generated_random_encounter = true
	return true

func _build_ui() -> void:
	var background := ColorRect.new()
	background.color = Color(0.045, 0.055, 0.07, 1.0)
	background.mouse_filter = Control.MOUSE_FILTER_IGNORE
	_place(background, 0.0, 0.0, 1.0, 1.0)
	add_child(background)

	title_label = Label.new()
	title_label.text = "Diyse 7B.5F — Prime Direct-Control Proof"
	title_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title_label.add_theme_font_size_override("font_size", 34)
	_place(title_label, 0.08, 0.025, 0.92, 0.085)
	add_child(title_label)

	party_status = RichTextLabel.new()
	party_status.bbcode_enabled = true
	party_status.fit_content = false
	party_status.add_theme_font_size_override("normal_font_size", 23)
	_place(party_status, 0.025, 0.10, 0.485, 0.32)
	add_child(party_status)

	enemy_status = RichTextLabel.new()
	enemy_status.bbcode_enabled = true
	enemy_status.fit_content = false
	enemy_status.add_theme_font_size_override("normal_font_size", 23)
	_place(enemy_status, 0.515, 0.10, 0.975, 0.32)
	add_child(enemy_status)

	prompt = Label.new()
	prompt.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	prompt.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	prompt.add_theme_font_size_override("font_size", 27)
	_place(prompt, 0.04, 0.32, 0.96, 0.385)
	add_child(prompt)

	command_box = HBoxContainer.new()
	command_box.alignment = BoxContainer.ALIGNMENT_CENTER
	command_box.add_theme_constant_override("separation", 14)
	_place(command_box, 0.06, 0.39, 0.94, 0.47)
	add_child(command_box)

	for command in ["Attack", "Ability", "Card", "Item", "Defend"]:
		var button := Button.new()
		button.text = command
		button.custom_minimum_size = Vector2(205, 72)
		button.focus_mode = Control.FOCUS_NONE
		button.add_theme_font_size_override("font_size", 27)
		button.pressed.connect(_on_command_pressed.bind(command))
		command_box.add_child(button)
		command_buttons[command] = button

	target_box = HBoxContainer.new()
	target_box.alignment = BoxContainer.ALIGNMENT_CENTER
	target_box.add_theme_constant_override("separation", 10)
	_place(target_box, 0.025, 0.485, 0.975, 0.575)
	add_child(target_box)

	confirm_button = Button.new()
	confirm_button.text = "CONFIRM ROUND"
	confirm_button.focus_mode = Control.FOCUS_NONE
	confirm_button.add_theme_font_size_override("font_size", 28)
	confirm_button.pressed.connect(_on_confirm_round)
	_place(confirm_button, 0.38, 0.585, 0.62, 0.655)
	add_child(confirm_button)

	next_round_button = Button.new()
	next_round_button.text = "NEXT ROUND"
	next_round_button.focus_mode = Control.FOCUS_NONE
	next_round_button.add_theme_font_size_override("font_size", 28)
	next_round_button.pressed.connect(_on_next_round)
	_place(next_round_button, 0.38, 0.585, 0.62, 0.655)
	add_child(next_round_button)

	return_button = Button.new()
	return_button.text = "RETURN TO FIELD"
	return_button.focus_mode = Control.FOCUS_NONE
	return_button.add_theme_font_size_override("font_size", 28)
	return_button.pressed.connect(_return_to_field)
	_place(return_button, 0.38, 0.585, 0.62, 0.655)
	add_child(return_button)

	flee_button = Button.new()
	flee_button.text = "PROOF FLEE SUCCESS"
	flee_button.focus_mode = Control.FOCUS_NONE
	flee_button.add_theme_font_size_override("font_size", 22)
	flee_button.pressed.connect(_on_proof_flee_success)
	_place(flee_button, 0.66, 0.585, 0.86, 0.655)
	add_child(flee_button)

	log_view = RichTextLabel.new()
	log_view.bbcode_enabled = true
	log_view.scroll_active = true
	log_view.add_theme_font_size_override("normal_font_size", 21)
	_place(log_view, 0.045, 0.67, 0.955, 0.965)
	add_child(log_view)

func _refresh_title() -> void:
	if _generated_random_encounter:
		title_label.text = "Diyse Audit98 — Generated Random Encounter Proof"
	else:
		title_label.text = "Diyse 7B.5F — Prime Direct-Control Proof"

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
	next_round_button.visible = battle.phase in ["round_complete", "prime_returned"]
	return_button.visible = battle.phase in ["victory", "defeat"]
	flee_button.visible = _generated_random_encounter and battle.phase == "selecting"
	command_box.visible = battle.phase == "selecting" and not battle.all_living_party_have_actions()
	if battle.phase == "prime_selecting":
		_show_prime_command_choices()
	elif battle.phase != "selecting":
		_clear_targets()

func _refresh_status() -> void:
	var party_text := "[b]PARTY[/b]\n"
	for unit in battle.party:
		var suffix := ""
		if battle.party_suspended:
			suffix = "  [SUSPENDED]"
		elif bool(unit["defending"]):
			suffix = "  [DEFENDING]"
		if int(unit.get("return_defense_bonus", 0)) > 0:
			suffix += "  [RETURN +%d DEF]" % int(unit["return_defense_bonus"])
		party_text += "%s  HP %d/%d  MP %d/%d  SPD %d%s\n" % [
			str(unit["name"]), int(unit["hp"]), int(unit["max_hp"]), int(unit["mp"]), int(unit["max_mp"]), int(unit["speed"]), suffix
		]
	if battle.party_suspended and not battle.active_prime.is_empty():
		party_text += "\n[b]ACTIVE PRIME[/b]\n%s  HP %d/%d  SPD %d  Rounds %d" % [
			str(battle.active_prime["name"]), int(battle.active_prime["hp"]), int(battle.active_prime["max_hp"]), int(battle.active_prime["speed"]), int(battle.active_prime["rounds_remaining"])
		]
	else:
		party_text += "\nPotions: %d  |  First Champion uses: %d" % [int(battle.inventory.get("Potion", 0)), battle.prime_use_remaining("first_champion")]
	party_status.text = party_text

	var enemy_text := "[b]ENEMIES[/b]\n"
	for unit in battle.enemies:
		enemy_text += "%s  HP %d/%d  SPD %d%s\n" % [
			str(unit["name"]), int(unit["hp"]), int(unit["max_hp"]), int(unit["speed"]), "  [KO]" if int(unit["hp"]) <= 0 else ""
		]
	enemy_status.text = enemy_text

func _refresh_log() -> void:
	var start := maxi(0, battle.log.size() - 13)
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
	_pending_content_id = ""
	_pending_prime_command_id = ""
	_clear_targets()
	command_buttons["Ability"].disabled = int(actor["mp"]) < BattleState.PARTY_ABILITY_MP_COST
	command_buttons["Item"].disabled = int(battle.inventory.get("Potion", 0)) <= 0
	command_buttons["Card"].disabled = battle.available_standard_cards().is_empty() and battle.available_prime_cards_for_actor(_current_actor_index).is_empty()
	_refresh_all()

func _on_command_pressed(command: String) -> void:
	if battle.phase != "selecting" or _current_actor_index < 0:
		return
	_pending_command = command
	_pending_content_id = ""
	if command == "Defend":
		if battle.queue_party_action(_current_actor_index, command, _current_actor_index):
			_select_next_actor()
		return
	if command in ["Attack", "Ability"]:
		prompt.text = "%s: choose an enemy target" % command
		_show_targets("enemy")
	elif command == "Card":
		prompt.text = "Choose a Card"
		_show_card_choices()
	elif command == "Item":
		prompt.text = "Potion: choose a living party target"
		_show_targets("party")

func _show_card_choices() -> void:
	_clear_targets()
	for card in battle.available_standard_cards():
		var button := Button.new()
		button.text = "%s [Standard]\n%s — Power %d" % [str(card.display_name), str(card.face), int(card.power)]
		button.custom_minimum_size = Vector2(360, 82)
		button.focus_mode = Control.FOCUS_NONE
		button.add_theme_font_size_override("font_size", 19)
		button.pressed.connect(_on_standard_card_selected.bind(str(card.card_id), str(card.target_side), str(card.display_name)))
		target_box.add_child(button)
	for prime in battle.available_prime_cards_for_actor(_current_actor_index):
		var prime_button := Button.new()
		prime_button.text = "%s [Prime]\n%s — Recovered — 1 use/battle" % [str(prime.display_name), str(prime.face)]
		prime_button.custom_minimum_size = Vector2(390, 82)
		prime_button.focus_mode = Control.FOCUS_NONE
		prime_button.add_theme_font_size_override("font_size", 19)
		prime_button.pressed.connect(_on_prime_card_selected.bind(str(prime.prime_id)))
		target_box.add_child(prime_button)

func _on_standard_card_selected(card_id: String, target_side: String, card_name: String) -> void:
	_pending_content_id = card_id
	prompt.text = "%s: choose a %s target" % [card_name, target_side]
	_show_targets(target_side)

func _on_prime_card_selected(prime_id: String) -> void:
	if battle.queue_party_action(_current_actor_index, "Card", -1, prime_id):
		_select_next_actor()

func _show_targets(side: String) -> void:
	_clear_targets()
	var units: Array = battle.enemies if side == "enemy" else battle.party
	for i in range(units.size()):
		if int(units[i]["hp"]) <= 0:
			continue
		var button := Button.new()
		button.text = "%s\nHP %d/%d" % [str(units[i]["name"]), int(units[i]["hp"]), int(units[i]["max_hp"])]
		button.custom_minimum_size = Vector2(220, 74)
		button.focus_mode = Control.FOCUS_NONE
		button.add_theme_font_size_override("font_size", 20)
		button.pressed.connect(_on_target_pressed.bind(i))
		target_box.add_child(button)

func _show_prime_command_choices() -> void:
	_clear_targets()
	_pending_prime_command_id = ""
	prompt.text = "%s: select exactly one Prime command" % str(battle.active_prime.get("name", "Prime"))
	for command in battle.available_prime_commands():
		var button := Button.new()
		button.text = "%s\n%s" % [str(command.get("display_name", "Prime Command")), _prime_command_summary(command)]
		button.custom_minimum_size = Vector2(330, 82)
		button.focus_mode = Control.FOCUS_NONE
		button.add_theme_font_size_override("font_size", 18)
		button.pressed.connect(_on_prime_command_selected.bind(str(command.get("command_id", "")), str(command.get("target_mode", "one"))))
		target_box.add_child(button)

func _prime_command_summary(command: Dictionary) -> String:
	match str(command.get("command_id", "")):
		"champion_edge":
			return "One enemy — 22 proof damage"
		"shieldbreak_arc":
			return "All enemies — 15 proof damage each"
		"stand_between":
			return "Self protection + return DEF marker"
	return str(command.get("description", ""))

func _on_prime_command_selected(prime_id: String) -> void:
	if battle.queue_party_action(_current_actor_index, "Card", -1, prime_id):
		_select_next_actor()

func _on_prime_command_selected_unused() -> void:
	pass

func _on_prime_card_selected_unused() -> void:
	pass

func _on_prime_command_selected(command_id: String, target_mode: String) -> void:
	_pending_prime_command_id = command_id
	if target_mode == "one":
		prompt.text = "Choose an enemy target for the Prime command"
		_show_prime_targets()
	else:
		_resolve_prime_command(command_id, -1)

func _show_prime_targets() -> void:
	_clear_targets()
	for i in range(battle.enemies.size()):
		if int(battle.enemies[i]["hp"]) <= 0:
			continue
		var enemy: Dictionary = battle.enemies[i]
		var button := Button.new()
		button.text = "%s\nHP %d/%d" % [str(enemy["name"]), int(enemy["hp"]), int(enemy["max_hp"])]
		button.custom_minimum_size = Vector2(220, 74)
		button.focus_mode = Control.FOCUS_NONE
		button.add_theme_font_size_override("font_size", 20)
		button.pressed.connect(_on_prime_target_pressed.bind(i))
		target_box.add_child(button)

func _on_prime_target_pressed(target_index: int) -> void:
	if not _pending_prime_command_id.is_empty():
		_resolve_prime_command(_pending_prime_command_id, target_index)

func _resolve_prime_command(command_id: String, target_index: int) -> void:
	if not battle.resolve_prime_command(command_id, target_index):
		return
	_pending_prime_command_id = ""
	if battle.phase == "prime_selecting":
		prompt.text = "Prime round resolved. Select the next direct-control command."
	elif battle.phase == "prime_returned":
		prompt.text = "First Champion completed its two Recovered Prime rounds. Party returned."
	elif battle.phase == "victory":
		_finalize_generated_victory_once()
		prompt.text = _victory_prompt()
	_refresh_all()

func _clear_targets() -> void:
	for child in target_box.get_children():
		child.queue_free()

func _on_target_pressed(target_index: int) -> void:
	if _pending_command.is_empty() or _current_actor_index < 0:
		return
	if battle.queue_party_action(_current_actor_index, _pending_command, target_index, _pending_content_id):
		_select_next_actor()

func _on_confirm_round() -> void:
	if not battle.confirm_round():
		return
	if battle.phase == "victory":
		_finalize_generated_victory_once()
		prompt.text = _victory_prompt()
	elif battle.phase == "defeat":
		prompt.text = "Defeat — return to the field to restart the proof."
	elif battle.phase == "prime_selecting":
		prompt.text = "Activation round complete. Party suspended; First Champion entered."
	else:
		prompt.text = "Round resolved. Review the log, then continue."
	_refresh_all()

func _victory_prompt() -> String:
	return "Victory — %d XP and %d gold awarded." % [int(battle.rewards.get("xp", 0)), int(battle.rewards.get("gold", 0))]

func _finalize_generated_victory_once() -> void:
	if not _generated_random_encounter or _generated_reward_applied or battle.phase != "victory":
		return
	var reward_payload: Dictionary = battle.rewards.duplicate(true)
	GameState.rewards["xp"] = int(GameState.rewards.get("xp", 0)) + int(reward_payload.get("xp", 0))
	GameState.rewards["gold"] = int(GameState.rewards.get("gold", 0)) + int(reward_payload.get("gold", 0))
	if GameState.complete_transient_random_encounter("victory", reward_payload):
		_generated_reward_applied = true

func _on_proof_flee_success() -> void:
	# Engineering-only control. This proves the scene-return pressure contract;
	# it is not the final flee-success formula or player-facing UI.
	if not _generated_random_encounter or battle.phase != "selecting":
		return
	if not GameState.complete_transient_random_encounter("successful_flee"):
		return
	get_tree().change_scene_to_file(FIELD_SCENE)

func _on_next_round() -> void:
	battle.begin_round()
	_refresh_all()
	_select_next_actor()

func _return_to_field() -> void:
	if _generated_random_encounter:
		if battle.phase == "victory":
			_finalize_generated_victory_once()
		elif battle.phase == "defeat" and GameState.has_transient_random_encounter():
			GameState.complete_transient_random_encounter("defeat")
	get_tree().change_scene_to_file(FIELD_SCENE)
