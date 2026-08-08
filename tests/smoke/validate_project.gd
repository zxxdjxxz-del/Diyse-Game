extends SceneTree

const FIELD_SCENE := "res://game/exploration/field_proof.tscn"
const COMBAT_SCENE := "res://game/combat/combat_proof.tscn"
const PORTRAIT_PATHS := [
	"res://game/characters/placeholders/portraits/cyanis_neutral.svg",
	"res://game/characters/placeholders/portraits/cyanis_amused.svg",
	"res://game/characters/placeholders/portraits/torren_neutral.svg",
	"res://game/characters/placeholders/portraits/torren_dry.svg"
]

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var failures: Array[String] = []
	GameState.reset_defaults()
	var packed_scene := load(FIELD_SCENE) as PackedScene

	if packed_scene == null:
		failures.append("Could not load %s" % FIELD_SCENE)
		_finish(failures)
		return

	var field := packed_scene.instantiate()
	if field == null:
		failures.append("Could not instantiate field proof scene")
		_finish(failures)
		return

	get_root().add_child(field)
	await process_frame

	if field.get_node_or_null("Ground") == null:
		failures.append("Field proof is missing Ground")
	if field.get_node_or_null("FieldBoundary") == null:
		failures.append("Field proof is missing perimeter collision body")
	for side in ["North", "South", "West", "East"]:
		if field.get_node_or_null("FieldBoundary/%s" % side) == null:
			failures.append("Field perimeter is missing %s collision" % side)
	if field.get_node_or_null("Obstacle") == null:
		failures.append("Field proof is missing collision Obstacle")
	if field.get_node_or_null("ProofChest") == null:
		failures.append("Persistence proof is missing ProofChest interactable")
	if field.get_node_or_null("ProofChest/MeshInstance3D") == null:
		failures.append("ProofChest is missing visible mesh state")
	if field.get_node_or_null("Torren") == null:
		failures.append("Field proof is missing Torren dialogue-test NPC")
	if field.get_node_or_null("Torren/Sprite3D") == null:
		failures.append("Torren is missing 2.5D Sprite3D presentation")
	if field.get_node_or_null("Torren/InteractionArea") == null:
		failures.append("Torren is missing Area3D interaction zone")
	if field.get_node_or_null("Torren/InteractionArea/CollisionShape3D") == null:
		failures.append("Torren interaction zone is missing collision shape")
	if field.get_node_or_null("Cyanis") == null:
		failures.append("Field proof is missing Cyanis CharacterBody3D")
	if field.get_node_or_null("Cyanis/Sprite3D") == null:
		failures.append("Cyanis is missing 2.5D Sprite3D presentation")
	if field.get_node_or_null("Cyanis/Camera3D") == null:
		failures.append("Cyanis is missing follow Camera3D")
	if field.get_node_or_null("Cyanis/CollisionShape3D") == null:
		failures.append("Cyanis is missing collision shape")
	if field.get_node_or_null("HUD/TouchDPad") == null:
		failures.append("Field proof is missing temporary touch D-pad")
	for direction in ["Up", "Down", "Left", "Right"]:
		if field.get_node_or_null("HUD/TouchDPad/%s" % direction) == null:
			failures.append("Touch D-pad is missing %s button" % direction)

	var combat_button := field.get_node_or_null("HUD/CombatTestButton") as Button
	if combat_button == null:
		failures.append("Field is missing COMBAT TEST entry button")
	elif combat_button.anchor_left < 0.99:
		failures.append("COMBAT TEST button is not anchored to the right side of the viewport")

	var save_button := field.get_node_or_null("HUD/SaveButton") as Button
	var load_button := field.get_node_or_null("HUD/LoadButton") as Button
	var chest_button := field.get_node_or_null("HUD/ChestButton") as Button
	var torren_state_button := field.get_node_or_null("HUD/TorrenStateButton") as Button
	if save_button == null or load_button == null:
		failures.append("Persistence proof must expose SAVE and LOAD controls")
	if chest_button == null:
		failures.append("Persistence proof is missing chest interaction control")
	if torren_state_button == null:
		failures.append("Persistence proof is missing Torren state control")
	if field.get_node_or_null("HUD/PersistenceStatus") == null:
		failures.append("Persistence proof is missing visible status feedback")

	var talk_button := field.get_node_or_null("HUD/TalkButton") as Button
	if talk_button == null:
		failures.append("Dialogue proof is missing proximity TALK button")
	elif talk_button.anchor_left < 0.99 or talk_button.anchor_top < 0.99:
		failures.append("TALK button is not viewport-anchored to bottom-right")

	var dialogue_runner := field.get_node_or_null("HUD/DialogueRunner")
	if dialogue_runner == null:
		failures.append("Dialogue proof is missing DialogueRunner")
	else:
		if not dialogue_runner.has_method("start_conversation"):
			failures.append("DialogueRunner cannot start authored conversations")
		for child_name in ["LeftPortrait", "RightPortrait", "Speaker", "Body", "Continue"]:
			if dialogue_runner.get_node_or_null("Panel/%s" % child_name) == null:
				failures.append("DialogueRunner is missing %s" % child_name)

	var player := field.get_node_or_null("Cyanis")
	var torren := field.get_node_or_null("Torren")
	var chest := field.get_node_or_null("ProofChest")
	if player != null and not player.has_method("set_movement_enabled"):
		failures.append("Cyanis controller cannot pause/resume movement for dialogue")
	if player != null and torren != null and talk_button != null:
		player.global_position = torren.global_position + Vector3(0.0, 0.0, 1.5)
		field.call("_refresh_interaction_state")
		if not talk_button.visible:
			failures.append("TALK button does not become visible when Cyanis is in Torren interaction range")
		if torren_state_button != null and not torren_state_button.visible:
			failures.append("Torren state control does not become visible in NPC interaction range")
		player.global_position = torren.global_position + Vector3(0.0, 0.0, 6.0)
		field.call("_refresh_interaction_state")
		if talk_button.visible:
			failures.append("TALK button remains visible when Cyanis leaves Torren interaction range")
	if player != null and chest != null and chest_button != null:
		player.global_position = chest.global_position + Vector3(0.0, 0.5, 1.0)
		field.call("_refresh_interaction_state")
		if not chest_button.visible:
			failures.append("Chest interaction control does not appear near ProofChest")

	for portrait_path in PORTRAIT_PATHS:
		if load(portrait_path) == null:
			failures.append("Could not load dialogue portrait: %s" % portrait_path)

	field.queue_free()
	await process_frame
	GameState.reset_defaults()

	var combat_packed := load(COMBAT_SCENE) as PackedScene
	if combat_packed == null:
		failures.append("Could not load %s" % COMBAT_SCENE)
	else:
		var combat := combat_packed.instantiate()
		get_root().add_child(combat)
		await process_frame
		var battle_state = combat.get("battle")
		if battle_state == null:
			failures.append("Combat proof did not initialize its battle state")
		else:
			if battle_state.party.size() != 4:
				failures.append("Combat proof must initialize exactly four active party members")
			if battle_state.enemies.size() != 3:
				failures.append("Combat proof must initialize three test enemies")
			if battle_state.phase != "selecting":
				failures.append("Combat proof must begin in command-selection phase")
			if battle_state.available_standard_cards().size() != 1:
				failures.append("7B.5G must preserve exactly one placeholder Standard Card")
			if battle_state.available_prime_cards_for_actor(0).size() != 1:
				failures.append("Cyanis must initialize with bearer-locked First Champion available")
			if not battle_state.available_prime_cards_for_actor(1).is_empty():
				failures.append("First Champion must not appear for a non-bearer")
		var commands = combat.get("command_buttons")
		var required_commands := ["Attack", "Ability", "Card", "Item", "Defend"]
		if not (commands is Dictionary) or commands.size() != 5:
			failures.append("Combat proof must expose exactly five permanent commands")
		else:
			for command in required_commands:
				if not commands.has(command):
					failures.append("Combat proof is missing command: %s" % command)
		if combat.get("confirm_button") == null:
			failures.append("Combat proof is missing CONFIRM ROUND control")
		combat.queue_free()

	_finish(failures)

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Diyse 7B.5G integrated exploration/dialogue/combat/Card/Prime/persistence smoke validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
