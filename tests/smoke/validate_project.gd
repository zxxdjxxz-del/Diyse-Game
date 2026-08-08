extends SceneTree

const FIELD_SCENE := "res://game/exploration/field_proof.tscn"
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
	if field.get_node_or_null("FieldBoundary/North") == null:
		failures.append("Field perimeter is missing North collision")
	if field.get_node_or_null("FieldBoundary/South") == null:
		failures.append("Field perimeter is missing South collision")
	if field.get_node_or_null("FieldBoundary/West") == null:
		failures.append("Field perimeter is missing West collision")
	if field.get_node_or_null("FieldBoundary/East") == null:
		failures.append("Field perimeter is missing East collision")
	if field.get_node_or_null("Obstacle") == null:
		failures.append("Field proof is missing collision Obstacle")
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
	if field.get_node_or_null("HUD/TouchDPad/Up") == null:
		failures.append("Touch D-pad is missing Up button")
	if field.get_node_or_null("HUD/TouchDPad/Down") == null:
		failures.append("Touch D-pad is missing Down button")
	if field.get_node_or_null("HUD/TouchDPad/Left") == null:
		failures.append("Touch D-pad is missing Left button")
	if field.get_node_or_null("HUD/TouchDPad/Right") == null:
		failures.append("Touch D-pad is missing Right button")

	var talk_button := field.get_node_or_null("HUD/TalkButton") as Button
	if talk_button == null:
		failures.append("Dialogue proof is missing proximity TALK button")
	else:
		if talk_button.anchor_left < 0.99 or talk_button.anchor_top < 0.99:
			failures.append("TALK button is not viewport-anchored to bottom-right")

	var dialogue_runner := field.get_node_or_null("HUD/DialogueRunner")
	if dialogue_runner == null:
		failures.append("Dialogue proof is missing DialogueRunner")
	else:
		if not dialogue_runner.has_method("start_conversation"):
			failures.append("DialogueRunner cannot start authored conversations")
		if dialogue_runner.get_node_or_null("Panel/LeftPortrait") == null:
			failures.append("DialogueRunner is missing left portrait slot")
		if dialogue_runner.get_node_or_null("Panel/RightPortrait") == null:
			failures.append("DialogueRunner is missing right portrait slot")
		if dialogue_runner.get_node_or_null("Panel/Speaker") == null:
			failures.append("DialogueRunner is missing speaker label")
		if dialogue_runner.get_node_or_null("Panel/Body") == null:
			failures.append("DialogueRunner is missing body text")
		if dialogue_runner.get_node_or_null("Panel/Continue") == null:
			failures.append("DialogueRunner is missing authored NEXT control")

	var player := field.get_node_or_null("Cyanis")
	var torren := field.get_node_or_null("Torren")
	if player != null and not player.has_method("set_movement_enabled"):
		failures.append("Cyanis controller cannot pause/resume movement for dialogue")

	if player != null and torren != null and talk_button != null:
		player.global_position = torren.global_position + Vector3(0.0, 0.0, 1.5)
		field.call("_refresh_interaction_state")
		if not talk_button.visible:
			failures.append("TALK button does not become visible when Cyanis is in Torren interaction range")
		player.global_position = torren.global_position + Vector3(0.0, 0.0, 6.0)
		field.call("_refresh_interaction_state")
		if talk_button.visible:
			failures.append("TALK button remains visible when Cyanis leaves Torren interaction range")

	for portrait_path in PORTRAIT_PATHS:
		if load(portrait_path) == null:
			failures.append("Could not load dialogue portrait: %s" % portrait_path)

	field.queue_free()
	_finish(failures)

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Diyse 7B.5C functional dialogue interaction validation passed.")
		quit(0)
		return

	for failure in failures:
		push_error(failure)
	quit(1)
