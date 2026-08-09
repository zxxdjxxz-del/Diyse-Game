extends SceneTree

const FIELD_SCENE := "res://game/exploration/field_proof.tscn"
const REGISTRY_PATH := "res://game/content/dialogue/proof/proof_portrait_registry.tres"
const SCENE_PATH := "res://game/content/dialogue/proof/PROOF_SCHEMA.tres"

var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run")

func _run() -> void:
	var game_state := get_root().get_node_or_null("GameState")
	if game_state != null:
		game_state.call("reset_defaults")
	var packed := load(FIELD_SCENE) as PackedScene
	var registry = load(REGISTRY_PATH)
	var scene = load(SCENE_PATH)
	_expect(packed != null, "Field scene must load for dialogue runner integration validation")
	_expect(registry != null and scene != null, "7B.6 authored Resource fixtures must load")
	if packed == null or registry == null or scene == null:
		_finish()
		return

	var field := packed.instantiate()
	get_root().add_child(field)
	await process_frame
	var runner = field.get_node_or_null("HUD/DialogueRunner")
	_expect(runner != null, "Accepted DialogueRunner must remain present")
	if runner == null:
		field.queue_free()
		_finish()
		return
	_expect(runner.has_method("start_scene"), "DialogueRunner must expose the production Resource adapter")
	var started := bool(runner.call("start_scene", scene, registry))
	_expect(started, "Valid production scene Resource must start through the accepted DialogueRunner")
	_expect(bool(runner.call("is_running")), "DialogueRunner must enter running state for a Resource-backed scene")
	var speaker := runner.get_node("Panel/Speaker") as Label
	var body := runner.get_node("Panel/Body") as Label
	var hint := runner.get_node("Panel/BeatHint") as Label
	var left := runner.get_node("Panel/LeftPortrait") as TextureRect
	var right := runner.get_node("Panel/RightPortrait") as TextureRect
	_expect(speaker.text == "Torren", "First Resource-backed beat must resolve Torren's display name")
	_expect(not body.text.is_empty(), "First Resource-backed beat must present authored fixture text")
	_expect(left.texture != null and right.texture != null, "Registry-resolved portraits must reach the existing portrait slots")

	runner.call("_advance")
	_expect(speaker.text == "Cyanis", "Second Resource-backed beat must advance through the existing runner")
	runner.call("_advance")
	_expect(speaker.text.is_empty() and body.text.is_empty(), "Third Resource-backed beat must preserve a true silent reaction")
	_expect(not hint.text.is_empty(), "Existing silent-reaction presentation must remain active for Resource-backed data")
	runner.call("_advance")
	_expect(not bool(runner.call("is_running")), "Resource-backed scene must finish through the existing runner lifecycle")

	field.queue_free()
	await process_frame
	_finish()

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse 7B.6 production Resource -> DialogueRunner integration validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
