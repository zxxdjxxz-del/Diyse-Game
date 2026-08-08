extends SceneTree

const FIELD_SCENE := "res://game/exploration/field_proof.tscn"
const OUTPUT_DIR := "res://artifacts"
const OUTPUT_FILE := "res://artifacts/dialogue_proof.png"

func _initialize() -> void:
	call_deferred("_capture")

func _capture() -> void:
	var packed_scene := load(FIELD_SCENE) as PackedScene
	if packed_scene == null:
		push_error("Could not load %s" % FIELD_SCENE)
		quit(1)
		return

	var field := packed_scene.instantiate()
	get_root().add_child(field)
	await process_frame

	var player := field.get_node("Cyanis") as Node3D
	var torren := field.get_node("Torren") as Node3D
	player.global_position = torren.global_position + Vector3(0.0, 0.0, 1.5)
	field.call("_start_dialogue")

	await process_frame
	await process_frame
	await RenderingServer.frame_post_draw

	var dialogue_runner := field.get_node("HUD/DialogueRunner") as Control
	if not dialogue_runner.visible:
		push_error("Dialogue runner did not become visible for visual proof")
		quit(1)
		return

	var body := dialogue_runner.get_node("Panel/Body") as Label
	if body.text.is_empty():
		push_error("Dialogue visual proof opened without authored text")
		quit(1)
		return

	var absolute_dir := ProjectSettings.globalize_path(OUTPUT_DIR)
	var absolute_file := ProjectSettings.globalize_path(OUTPUT_FILE)
	var mkdir_error := DirAccess.make_dir_recursive_absolute(absolute_dir)
	if mkdir_error != OK and mkdir_error != ERR_ALREADY_EXISTS:
		push_error("Could not create screenshot artifact directory: %s" % mkdir_error)
		quit(1)
		return

	var image := get_root().get_texture().get_image()
	if image == null or image.is_empty():
		push_error("Dialogue viewport capture returned an empty image")
		quit(1)
		return

	var save_error := image.save_png(absolute_file)
	if save_error != OK:
		push_error("Could not save dialogue proof screenshot: %s" % save_error)
		quit(1)
		return

	print("Saved 7B.5C dialogue proof screenshot to %s" % absolute_file)
	quit(0)
