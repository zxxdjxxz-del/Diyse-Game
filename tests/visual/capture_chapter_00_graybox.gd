extends SceneTree

const GRAYBOX_SCENE := "res://game/exploration/maps/chapter_00/chapter_00_graybox.tscn"
const OUTPUT_DIR := "res://artifacts/chapter_00_graybox"

var graybox: Node3D
var player: CharacterBody3D

func _initialize() -> void:
	call_deferred("_capture_all")

func _capture_all() -> void:
	var packed_scene := load(GRAYBOX_SCENE) as PackedScene
	if packed_scene == null:
		push_error("Could not load %s" % GRAYBOX_SCENE)
		quit(1)
		return

	graybox = packed_scene.instantiate()
	get_root().add_child(graybox)
	await process_frame
	await process_frame

	player = graybox.get_node_or_null("Cyanis") as CharacterBody3D
	if player == null:
		push_error("Chapter 0 graybox is missing Cyanis")
		quit(1)
		return

	var absolute_dir := ProjectSettings.globalize_path(OUTPUT_DIR)
	var mkdir_error := DirAccess.make_dir_recursive_absolute(absolute_dir)
	if mkdir_error != OK and mkdir_error != ERR_ALREADY_EXISTS:
		push_error("Could not create Chapter 0 graybox artifact directory: %s" % mkdir_error)
		quit(1)
		return

	# Camera B route checkpoints.
	await _capture_checkpoint("01_convoy_road_cam_b", Vector3(0, 0.9, 55), 1)
	await _capture_checkpoint("02_wreck_field_cam_b", Vector3(5, 0.9, -185), 1)
	await _capture_checkpoint("03_recovery_line_cam_b", Vector3(14, 0.9, -355), 1)
	await _capture_checkpoint("04_triage_camp_cam_b", Vector3(0, 0.9, -460), 1)
	await _capture_checkpoint("05_s006_sweep_cam_b", Vector3(-34, 0.9, -536), 1)

	# Same Wreck Field viewpoint for direct camera comparison.
	await _capture_checkpoint("06_wreck_field_cam_a", Vector3(5, 0.9, -185), 0)
	await _capture_checkpoint("07_wreck_field_cam_b_compare", Vector3(5, 0.9, -185), 1)
	await _capture_checkpoint("08_wreck_field_cam_c", Vector3(5, 0.9, -185), 2)

	print("Saved Chapter 0 graybox screenshots to %s" % ProjectSettings.globalize_path(OUTPUT_DIR))
	quit(0)

func _capture_checkpoint(filename: String, position: Vector3, camera_variant: int) -> void:
	player.global_position = position
	player.velocity = Vector3.ZERO
	graybox.call("_set_camera_variant", camera_variant)

	await process_frame
	await process_frame
	await RenderingServer.frame_post_draw

	var image := get_root().get_texture().get_image()
	if image == null or image.is_empty():
		push_error("Viewport capture returned an empty image for %s" % filename)
		quit(1)
		return

	var absolute_file := ProjectSettings.globalize_path("%s/%s.png" % [OUTPUT_DIR, filename])
	var save_error := image.save_png(absolute_file)
	if save_error != OK:
		push_error("Could not save Chapter 0 graybox screenshot %s: %s" % [filename, save_error])
		quit(1)
		return
