extends Node3D

## Chapter 1 provisional spatial graybox — first playable slice only.
##
## Current slice:
## Brackenwall seam -> Upper Briar -> Greenhollow seam
##
## Source layout authority:
## docs/90_WORKING/AREA_LAYOUTS/BLUEPRINT_002_CH01_BRIAR_HOLLOW_WATCH_WAYFINDER.md
##
## This is test geometry, not final environment art or locked L3 topology.

@onready var player: CharacterBody3D = $Cyanis
@onready var camera: Camera3D = $Cyanis/Camera3D
@onready var location_label: Label = $HUD/LocationLabel
@onready var camera_label: Label = $HUD/CameraLabel
@onready var debug_label: Label = $HUD/DebugLabel
@onready var story_label: Label = $HUD/StoryLabel

var _road_material: StandardMaterial3D
var _optional_material: StandardMaterial3D
var _boundary_material: StandardMaterial3D
var _marker_material: StandardMaterial3D
var _seam_material: StandardMaterial3D

var _distance_moved := 0.0
var _slice_start_ms := 0
var _current_encounter_state := "SAFE — Brackenwall seam"
var _triggered_story_sockets: Dictionary = {}
var _last_safe_position := Vector3(-258.0, 0.9, 10.0)

const PLAYER_START := Vector3(-258.0, 0.9, 10.0)

func _ready() -> void:
	_build_materials()
	_build_graybox()
	_connect_ui()
	player.eligible_distance_moved.connect(_on_distance_moved)
	_slice_start_ms = Time.get_ticks_msec()
	_set_camera_variant(1)
	_update_debug_hud()

func _process(_delta: float) -> void:
	_update_debug_hud()

	# Keep a nearby recovery point so an accidental graybox fall does not force
	# the tester to restart the whole slice.
	if player.is_on_floor() and player.global_position.y > -0.2:
		_last_safe_position = player.global_position

	if player.global_position.y < -0.5:
		_recover_from_fall()

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo:
		match event.keycode:
			KEY_1:
				_set_camera_variant(0)
			KEY_2:
				_set_camera_variant(1)
			KEY_3:
				_set_camera_variant(2)
			KEY_R:
				_reset_player()

func _connect_ui() -> void:
	$HUD/CameraA.pressed.connect(_set_camera_variant.bind(0))
	$HUD/CameraB.pressed.connect(_set_camera_variant.bind(1))
	$HUD/CameraC.pressed.connect(_set_camera_variant.bind(2))
	$HUD/Reset.pressed.connect(_reset_player)

func _build_materials() -> void:
	_road_material = _make_material(Color(0.34, 0.28, 0.18, 1.0))
	_optional_material = _make_material(Color(0.29, 0.34, 0.20, 1.0))
	_boundary_material = _make_material(Color(0.12, 0.20, 0.12, 1.0))
	_marker_material = _make_material(Color(0.78, 0.60, 0.18, 1.0))
	_seam_material = _make_material(Color(0.55, 0.64, 0.75, 1.0))

func _make_material(color: Color) -> StandardMaterial3D:
	var material := StandardMaterial3D.new()
	material.albedo_color = color
	material.roughness = 0.95
	return material

func _build_graybox() -> void:
	_build_upper_briar()
	_build_boundaries()
	_build_debug_zones()
	_build_story_sockets()
	_build_markers()

func _build_upper_briar() -> void:
	# Android v0.3 collision pass: the first slice is intentionally flat.
	# Independent sloped BoxShape3D segments created tiny step lips at joins,
	# which CharacterBody3D could not step over reliably. Elevation returns only
	# after route scale is approved and the floor is rebuilt as continuous terrain.
	# All route branches now attach at explicit nodes. Visible edge guards are
	# generated along the walkable paths, with short gaps at nodes so junctions
	# remain traversable.
	var main_points: Array[Vector3] = [
		Vector3(-260, 0, 10),
		Vector3(-190, 0, 20),
		Vector3(-145, 0, 12.1), # shallow-loop junction
		Vector3(-105, 0, 5),
		Vector3(-18, 0, 15.8), # shallow-loop reconnect
		Vector3(0, 0, 18),
		Vector3(95, 0, 5),
		Vector3(108, 0, 3), # Pocket U2 junction
		Vector3(185, 0, -8),
		Vector3(260, 0, 0),
	]
	_add_guarded_path("BP_A_Main", main_points, 7.0, _road_material)

	var shallow_loop: Array[Vector3] = [
		Vector3(-145, 0, 12.1),
		Vector3(-125, 0, -24), # Pocket U1 junction
		Vector3(-78, 0, -34),
		Vector3(-32, 0, -4),
		Vector3(-18, 0, 15.8),
	]
	_add_guarded_path("BP_A_ShallowLoop", shallow_loop, 5.2, _optional_material)

	var pocket_u1: Array[Vector3] = [
		Vector3(-125, 0, -24),
		Vector3(-150, 0, -42),
	]
	_add_guarded_path("BP_A_PocketU1_Path", pocket_u1, 4.2, _optional_material)
	_add_pad("BP_A_PocketU1", Vector3(-154, 0, -45), Vector2(14, 12), _optional_material)

	var pocket_u2: Array[Vector3] = [
		Vector3(108, 0, 3),
		Vector3(130, 0, 28),
	]
	_add_guarded_path("BP_A_PocketU2_Path", pocket_u2, 4.2, _optional_material)
	_add_pad("BP_A_PocketU2", Vector3(134, 0, 32), Vector2(14, 12), _optional_material)

	_add_pad("BP_A_HalfwayPocket", Vector3(0, 0, 18), Vector2(30, 20), _road_material)
	_add_pad_side_guard("BP_A_HalfwayNorth", Vector3(0, 0, 26.4), Vector3(18, 2.4, 0.8))
	_add_pad_side_guard("BP_A_HalfwaySouth", Vector3(0, 0, 9.6), Vector3(18, 2.4, 0.8))

	_add_pad("BP_A_BrackenwallSeam", Vector3(-266, 0, 10), Vector2(16, 14), _seam_material)
	_add_pad("BP_A_GreenhollowSeam", Vector3(266, 0, 0), Vector2(16, 14), _seam_material)

func _build_boundaries() -> void:
	# v0.2 removes the oversized rectangular forest collision volumes that could
	# be hit from the wrong direction on Android. Route-edge briar banks now do
	# the actual fall prevention. Only visible end caps remain.
	_add_boundary_box("BP_A_WestCap", Vector3(-292, 3.0, 8), Vector3(10, 6, 130))
	_add_boundary_box("BP_A_EastCap", Vector3(292, 3.0, 0), Vector3(10, 6, 130))

func _build_debug_zones() -> void:
	# Encounter-state areas are deliberately broad. They exist to test pacing,
	# not to define final encounter math.
	_add_state_zone(
		"Zone_BrackenwallSafe",
		Vector3(-252, 3, 10),
		Vector3(32, 12, 55),
		"SAFE — Brackenwall seam"
	)
	_add_state_zone(
		"Zone_EncounterWest",
		Vector3(-125, 4, 5),
		Vector3(210, 18, 125),
		"ACTIVE — Upper Briar west"
	)
	_add_state_zone(
		"Zone_HalfwaySafe",
		Vector3(0, 0, 18),
		Vector3(44, 18, 70),
		"SAFE — Beat 2 halfway buffer"
	)
	_add_state_zone(
		"Zone_EncounterEast",
		Vector3(135, 3, 2),
		Vector3(220, 12, 125),
		"ACTIVE — Upper Briar east"
	)
	_add_state_zone(
		"Zone_GreenhollowSafe",
		Vector3(252, 3, 0),
		Vector3(34, 12, 60),
		"SAFE — Greenhollow seam"
	)

func _build_story_sockets() -> void:
	_add_story_trigger(
		"Beat02_HalfwayStop",
		Vector3(0, 0, 18),
		Vector3(16, 8, 18),
		"BEAT 2 — HALFWAY STOP\nOne brief natural route break; no guided traversal."
	)

func _build_markers() -> void:
	_add_marker("BRACKENWALL SEAM", Vector3(-258, 0, 10))
	_add_marker("U1", Vector3(-190, 0, 20))
	_add_marker("U2 / LOOP", Vector3(-105, 0, 5))
	_add_marker("POCKET U1", Vector3(-154, 0, -45))
	_add_marker("BEAT 2 HALFWAY", Vector3(0, 0, 18))
	_add_marker("U3", Vector3(95, 0, 5))
	_add_marker("POCKET U2", Vector3(134, 7, 32))
	_add_marker("U4", Vector3(185, 0, -8))
	_add_marker("GREENHOLLOW SEAM", Vector3(258, 5, 0))

func _add_guarded_path(name_prefix: String, points: Array[Vector3], width: float, material: StandardMaterial3D) -> void:
	for index in range(points.size() - 1):
		var a := points[index]
		var b := points[index + 1]
		_add_path_segment("%s_%02d" % [name_prefix, index], a, b, width, material)
		_add_edge_guard("%s_L_%02d" % [name_prefix, index], a, b, width, 1.0)
		_add_edge_guard("%s_R_%02d" % [name_prefix, index], a, b, width, -1.0)

func _add_edge_guard(name: String, a: Vector3, b: Vector3, path_width: float, side: float) -> void:
	var delta := b - a
	var horizontal := Vector3(delta.x, 0.0, delta.z)
	var horizontal_length := horizontal.length()
	if horizontal_length <= 4.5:
		return

	var horizontal_dir := horizontal / horizontal_length
	var margin := minf(2.0, horizontal_length * 0.2)
	var start := a + horizontal_dir * margin
	var finish := b - horizontal_dir * margin

	var normal := Vector3(-horizontal_dir.z, 0.0, horizontal_dir.x)
	var offset := normal * side * (path_width * 0.5 + 0.55)
	start += offset
	finish += offset

	var guard_delta := finish - start
	var guard_horizontal_length := Vector2(guard_delta.x, guard_delta.z).length()
	if guard_horizontal_length <= 0.2:
		return

	var body := StaticBody3D.new()
	body.name = name
	body.position = (start + finish) * 0.5 + Vector3(0, 0.9, 0)
	body.rotation.y = atan2(guard_delta.x, guard_delta.z)
	add_child(body)

	var mesh := BoxMesh.new()
	mesh.size = Vector3(0.9, 2.2, guard_horizontal_length)
	mesh.material = _boundary_material
	var mesh_instance := MeshInstance3D.new()
	mesh_instance.mesh = mesh
	body.add_child(mesh_instance)

	var shape := BoxShape3D.new()
	shape.size = Vector3(0.9, 2.2, guard_horizontal_length)
	var collision := CollisionShape3D.new()
	collision.shape = shape
	body.add_child(collision)

func _add_pad_side_guard(name: String, ground_center: Vector3, size: Vector3) -> void:
	_add_boundary_box(name, ground_center + Vector3(0, size.y * 0.5 - 0.1, 0), size)

func _add_path(name_prefix: String, points: Array[Vector3], width: float, material: StandardMaterial3D) -> void:
	for index in range(points.size() - 1):
		_add_path_segment("%s_%02d" % [name_prefix, index], points[index], points[index + 1], width, material)

func _add_path_segment(name: String, a: Vector3, b: Vector3, width: float, material: StandardMaterial3D) -> void:
	var delta := b - a
	var horizontal_length := Vector2(delta.x, delta.z).length()
	if horizontal_length <= 0.001:
		return

	var body := StaticBody3D.new()
	body.name = name
	body.position = (a + b) * 0.5

	var yaw := atan2(delta.x, delta.z)
	var pitch := -atan2(delta.y, horizontal_length)
	body.basis = Basis(Vector3.UP, yaw) * Basis(Vector3.RIGHT, pitch)
	add_child(body)

	var segment_length := delta.length() + 1.0
	var mesh := BoxMesh.new()
	mesh.size = Vector3(width, 0.22, segment_length)
	mesh.material = material

	var mesh_instance := MeshInstance3D.new()
	mesh_instance.mesh = mesh
	mesh_instance.position.y = -0.11
	body.add_child(mesh_instance)

	var shape := BoxShape3D.new()
	shape.size = Vector3(width, 0.22, segment_length)
	var collision := CollisionShape3D.new()
	collision.shape = shape
	collision.position.y = -0.11
	body.add_child(collision)

func _add_pad(name: String, center: Vector3, size_xz: Vector2, material: StandardMaterial3D) -> void:
	var body := StaticBody3D.new()
	body.name = name
	body.position = center + Vector3(0, -0.11, 0)
	add_child(body)

	var mesh := BoxMesh.new()
	mesh.size = Vector3(size_xz.x, 0.22, size_xz.y)
	mesh.material = material
	var mesh_instance := MeshInstance3D.new()
	mesh_instance.mesh = mesh
	body.add_child(mesh_instance)

	var shape := BoxShape3D.new()
	shape.size = Vector3(size_xz.x, 0.22, size_xz.y)
	var collision := CollisionShape3D.new()
	collision.shape = shape
	body.add_child(collision)

func _add_boundary_box(name: String, center: Vector3, size: Vector3) -> void:
	var body := StaticBody3D.new()
	body.name = name
	body.position = center
	add_child(body)

	var mesh := BoxMesh.new()
	mesh.size = size
	mesh.material = _boundary_material
	var mesh_instance := MeshInstance3D.new()
	mesh_instance.mesh = mesh
	body.add_child(mesh_instance)

	var shape := BoxShape3D.new()
	shape.size = size
	var collision := CollisionShape3D.new()
	collision.shape = shape
	body.add_child(collision)

func _add_state_zone(name: String, center: Vector3, size: Vector3, state_text: String) -> void:
	var area := Area3D.new()
	area.name = name
	area.position = center
	area.collision_layer = 0
	area.collision_mask = 1
	add_child(area)

	var shape := BoxShape3D.new()
	shape.size = size
	var collision := CollisionShape3D.new()
	collision.shape = shape
	area.add_child(collision)

	area.body_entered.connect(_on_state_zone_entered.bind(state_text))

func _add_story_trigger(name: String, center: Vector3, size: Vector3, text: String) -> void:
	var area := Area3D.new()
	area.name = name
	area.position = center
	area.collision_layer = 0
	area.collision_mask = 1
	add_child(area)

	var shape := BoxShape3D.new()
	shape.size = size
	var collision := CollisionShape3D.new()
	collision.shape = shape
	area.add_child(collision)

	area.body_entered.connect(_on_story_trigger_entered.bind(name, text))

func _add_marker(text: String, position: Vector3) -> void:
	var marker := Node3D.new()
	marker.name = "Marker_%s" % text.replace(" ", "_").replace("/", "_")
	marker.position = position
	add_child(marker)

	var mesh := CylinderMesh.new()
	mesh.top_radius = 0.20
	mesh.bottom_radius = 0.26
	mesh.height = 1.8
	mesh.material = _marker_material

	var pillar := MeshInstance3D.new()
	pillar.mesh = mesh
	pillar.position.y = 0.9
	marker.add_child(pillar)

	var label := Label3D.new()
	label.text = text
	label.font_size = 36
	label.outline_size = 8
	label.position = Vector3(0, 2.35, 0)
	label.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	marker.add_child(label)

func _on_state_zone_entered(body: Node3D, state_text: String) -> void:
	if body == player:
		_current_encounter_state = state_text

func _on_story_trigger_entered(body: Node3D, socket_id: String, text: String) -> void:
	if body != player:
		return
	story_label.text = text
	if not _triggered_story_sockets.has(socket_id):
		_triggered_story_sockets[socket_id] = true

func _on_distance_moved(distance: float) -> void:
	_distance_moved += distance

func _set_camera_variant(index: int) -> void:
	# Upper Briar progresses broadly west -> east, so these variants look east.
	match index:
		0:
			camera.position = Vector3(-7.5, 5.5, 0)
			camera.rotation_degrees = Vector3(-25, -90, 0)
			camera.fov = 60.0
			camera_label.text = "Camera A — proof-near / east-facing"
		1:
			camera.position = Vector3(-8.5, 6.5, 0)
			camera.rotation_degrees = Vector3(-30, -90, 0)
			camera.fov = 56.0
			camera_label.text = "Camera B — HD-2D test / east-facing"
		2:
			camera.position = Vector3(-9.5, 7.5, 0)
			camera.rotation_degrees = Vector3(-34, -90, 0)
			camera.fov = 54.0
			camera_label.text = "Camera C — broad readability / east-facing"

func _recover_from_fall() -> void:
	player.global_position = _last_safe_position + Vector3(0, 0.2, 0)
	player.velocity = Vector3.ZERO

func _reset_player() -> void:
	player.global_position = PLAYER_START
	player.velocity = Vector3.ZERO
	_distance_moved = 0.0
	_slice_start_ms = Time.get_ticks_msec()
	_current_encounter_state = "SAFE — Brackenwall seam"
	_last_safe_position = PLAYER_START
	_triggered_story_sockets.clear()
	story_label.text = "Story socket: none triggered"

func _update_debug_hud() -> void:
	location_label.text = "CH01_BP_A — Upper Briar / Brackenwall → Greenhollow"

	var elapsed_seconds := maxf(0.0, float(Time.get_ticks_msec() - _slice_start_ms) / 1000.0)
	var minutes := int(elapsed_seconds) / 60
	var seconds := int(elapsed_seconds) % 60

	debug_label.text = (
		"Time %02d:%02d   Distance %.0f m   Story sockets %d\nEncounter state: %s"
		% [minutes, seconds, _distance_moved, _triggered_story_sockets.size(), _current_encounter_state]
	)
