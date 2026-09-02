extends Node3D

## Provisional Chapter-0 spatial graybox.
##
## Source layout authority:
## docs/90_WORKING/AREA_LAYOUTS/BLUEPRINT_001_CH00_CONVOY_WRECK_ROUTE.md
##
## This is a test blockout, not final environment art or locked L3 topology.

@onready var player: CharacterBody3D = $Cyanis
@onready var camera: Camera3D = $Cyanis/Camera3D
@onready var location_label: Label = $HUD/LocationLabel
@onready var camera_label: Label = $HUD/CameraLabel

var _road_material: StandardMaterial3D
var _wreck_material: StandardMaterial3D
var _recovery_material: StandardMaterial3D
var _camp_material: StandardMaterial3D
var _marker_material: StandardMaterial3D
var _boundary_material: StandardMaterial3D

const F02_OFFSET_Z := -175.0
const F03_OFFSET_Z := -325.0
const F04_OFFSET_Z := -450.0
const PLAYER_START := Vector3(0.0, 0.9, 108.0)

func _ready() -> void:
	_build_materials()
	_build_graybox()
	_connect_ui()
	_set_camera_variant(1)
	_update_location_label()

func _process(_delta: float) -> void:
	_update_location_label()
	if player.global_position.y < -8.0:
		_reset_player()

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
	_road_material = _make_material(Color(0.34, 0.27, 0.18, 1.0))
	_wreck_material = _make_material(Color(0.31, 0.30, 0.28, 1.0))
	_recovery_material = _make_material(Color(0.36, 0.33, 0.24, 1.0))
	_camp_material = _make_material(Color(0.24, 0.32, 0.23, 1.0))
	_marker_material = _make_material(Color(0.72, 0.54, 0.16, 1.0))
	_boundary_material = _make_material(Color(0.17, 0.20, 0.16, 1.0))

func _make_material(color: Color) -> StandardMaterial3D:
	var material := StandardMaterial3D.new()
	material.albedo_color = color
	material.roughness = 0.95
	return material

func _build_graybox() -> void:
	_build_convoy_road()
	_build_wreck_field()
	_build_recovery_line()
	_build_triage_camp()
	_build_recovery_sweep()
	_build_chunk_seams()

func _build_convoy_road() -> void:
	var points: Array[Vector3] = [
		Vector3(0, 0, 112),
		Vector3(0, 0, 95),
		Vector3(-8, 0, 55),
		Vector3(18, 0, 20),
		Vector3(10, 0, -15),
		Vector3(-20, 0, -48),
		Vector3(-5, 0, -82),
		Vector3(0, 0, -105),
	]
	_add_path("F01_Road", points, 9.0, _road_material)
	_add_pad("F01_Encounter1", Vector3(-8, 0, 55), Vector2(24, 22), _road_material)
	_add_pad("F01_Encounter2", Vector3(10, 0, -15), Vector2(24, 22), _road_material)
	_add_pad("F01_Pursuer", Vector3(-20, 0, -48), Vector2(25, 22), _road_material)
	_add_pad("F01_Riftmaw", Vector3(-5, 0, -82), Vector2(28, 24), _road_material)
	_add_boundary_box("F01_WestRidge", Vector3(-43, 1.5, 8), Vector3(24, 3, 205))
	_add_boundary_box("F01_EastRidge", Vector3(48, 1.5, 0), Vector3(26, 3, 210))
	_add_marker("F01 Start", Vector3(0, 0, 103))
	_add_marker("S001-1", Vector3(-8, 0, 55))
	_add_marker("S001-2", Vector3(10, 0, -15))
	_add_marker("S001-3 Pursuer", Vector3(-20, 0, -48))
	_add_marker("S001-4 Riftmaw", Vector3(-5, 0, -82))

func _build_wreck_field() -> void:
	var o := Vector3(0, 0, F02_OFFSET_Z)
	_add_pad("F02_Basin", o + Vector3(0, 0, -2), Vector2(150, 136), _wreck_material)
	_add_pad("F02_SurvivorLobe", o + Vector3(-45, 0, 20), Vector2(42, 34), _wreck_material)
	_add_pad("F02_DamagedConvoy", o + Vector3(38, 0, 12), Vector2(44, 36), _wreck_material)
	_add_pad("F02_EvacuationEvidence", o + Vector3(-28, 0, -42), Vector2(38, 32), _wreck_material)
	_add_boundary_box("F02_WestEdge", o + Vector3(-84, 1.2, -2), Vector3(18, 2.4, 145))
	_add_boundary_box("F02_EastEdge", o + Vector3(84, 1.2, -2), Vector3(18, 2.4, 145))
	_add_marker("F02 Entry", o + Vector3(0, 0, 60))
	_add_marker("Survivors", o + Vector3(-45, 0, 20))
	_add_marker("S002 Hound", o + Vector3(5, 0, -10))
	_add_marker("Damaged Convoy", o + Vector3(38, 0, 12))
	_add_marker("Evacuation Evidence", o + Vector3(-28, 0, -42))
	_add_marker("North Withdrawal Sightline", o + Vector3(30, 0, -62))
	_add_marker("F02 Exit", o + Vector3(0, 0, -70))

func _build_recovery_line() -> void:
	var o := Vector3(0, 0, F03_OFFSET_Z)
	var points: Array[Vector3] = [
		o + Vector3(0, 0, 78),
		o + Vector3(8, 0, 35),
		o + Vector3(-12, 0, 0),
		o + Vector3(14, 0, -30),
		o + Vector3(0, 0, -60),
		o + Vector3(0, 0, -82),
	]
	_add_path("F03_RecoveryRoad", points, 8.0, _recovery_material)
	_add_pad("F03_RelayYard", o + Vector3(-12, 0, 0), Vector2(34, 30), _recovery_material)
	_add_pad("F03_Decision", o + Vector3(14, 0, -30), Vector2(24, 20), _recovery_material)
	_add_boundary_box("F03_WestBank", o + Vector3(-40, 1.2, 0), Vector3(18, 2.4, 168))
	_add_boundary_box("F03_EastBank", o + Vector3(42, 1.2, 0), Vector3(18, 2.4, 168))
	_add_marker("F03 Entry", o + Vector3(0, 0, 78))
	_add_marker("Damaged Recovery Line", o + Vector3(8, 0, 35))
	_add_marker("Relay Yard", o + Vector3(-12, 0, 0))
	_add_marker("S003 Decision", o + Vector3(14, 0, -30))
	_add_marker("F03 Exit", o + Vector3(0, 0, -82))

func _build_triage_camp() -> void:
	var o := Vector3(0, 0, F04_OFFSET_Z)
	_add_pad("F04_CampBase", o + Vector3(0, 0, -5), Vector2(108, 88), _camp_material)
	_add_pad("F04_ArrivalLane", o + Vector3(0, 0, 36), Vector2(26, 20), _camp_material)
	_add_pad("F04_Wounded", o + Vector3(-28, 0, 8), Vector2(34, 30), _camp_material)
	_add_pad("F04_Supplies", o + Vector3(24, 0, 5), Vector2(32, 28), _camp_material)
	_add_pad("F04_Ilyra", o + Vector3(0, 0, -10), Vector2(22, 20), _camp_material)
	_add_pad("F04_Perimeter", o + Vector3(8, 0, -38), Vector2(34, 24), _camp_material)
	_add_pad("F04_EastCut", o + Vector3(45, 0, -34), Vector2(18, 18), _camp_material)
	_add_boundary_box("F04_WestEdge", o + Vector3(-58, 1.2, -4), Vector3(10, 2.4, 96))
	_add_boundary_box("F04_EastEdgeNorth", o + Vector3(58, 1.2, 9), Vector3(10, 2.4, 62))
	_add_marker("F04 Entry", o + Vector3(0, 0, 40))
	_add_marker("Wounded / NO COMBAT", o + Vector3(-28, 0, 8))
	_add_marker("Supplies / NO COMBAT", o + Vector3(24, 0, 5))
	_add_marker("S004 Ilyra", o + Vector3(0, 0, -10))
	_add_marker("S005 Final Confrontation", o + Vector3(8, 0, -38))
	_add_marker("S005 East Cut", o + Vector3(45, 0, -34))
	_add_marker("Soldier Withdraws East", o + Vector3(50, 0, -40))
	_add_marker("S006 Sweep Start", o + Vector3(0, 0, -48))

func _build_recovery_sweep() -> void:
	var o := Vector3(0, 0, F04_OFFSET_Z)
	var points: Array[Vector3] = [
		o + Vector3(0, 0, -48),
		o + Vector3(-18, 0, -58),
		o + Vector3(-36, 0, -70),
		o + Vector3(-34, 0, -86),
		o + Vector3(-12, 0, -98),
		o + Vector3(0, 0, -108),
	]
	_add_path("F03R_SurvivorSweep", points, 7.0, _recovery_material)
	_add_pad("F03R_Tracks", o + Vector3(-36, 0, -70), Vector2(20, 18), _recovery_material)
	_add_pad("F03R_WreckMarkerLimit", o + Vector3(-34, 0, -86), Vector2(18, 16), _recovery_material)
	_add_pad("F03R_BrackenwallHandoff", o + Vector3(0, 0, -108), Vector2(18, 16), _recovery_material)
	_add_marker("S006 Tracks South of Wagon Line", o + Vector3(-36, 0, -70))
	_add_marker("S006 Wreck Marker Limit", o + Vector3(-34, 0, -86))
	_add_marker("S006 Sweep Complete", o + Vector3(-12, 0, -98))
	_add_marker("TO BRACKENWALL", o + Vector3(0, 0, -108))

func _build_chunk_seams() -> void:
	_add_path_segment("Seam_F01_F02", Vector3(0, 0, -105), Vector3(0, 0, -115), 8.0, _road_material)
	_add_path_segment("Seam_F02_F03", Vector3(0, 0, -245), Vector3(0, 0, -247), 8.0, _recovery_material)
	_add_path_segment("Seam_F03_F04", Vector3(0, 0, -407), Vector3(0, 0, -410), 8.0, _camp_material)

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
	body.position = (a + b) * 0.5 + Vector3(0, -0.1, 0)
	body.rotation.y = atan2(delta.x, delta.z)
	add_child(body)
	var mesh := BoxMesh.new()
	mesh.size = Vector3(width, 0.2, horizontal_length + 1.0)
	mesh.material = material
	var mesh_instance := MeshInstance3D.new()
	mesh_instance.mesh = mesh
	body.add_child(mesh_instance)
	var shape := BoxShape3D.new()
	shape.size = Vector3(width, 0.2, horizontal_length + 1.0)
	var collision := CollisionShape3D.new()
	collision.shape = shape
	body.add_child(collision)

func _add_pad(name: String, center: Vector3, size_xz: Vector2, material: StandardMaterial3D) -> void:
	var body := StaticBody3D.new()
	body.name = name
	body.position = center + Vector3(0, -0.1, 0)
	add_child(body)
	var mesh := BoxMesh.new()
	mesh.size = Vector3(size_xz.x, 0.2, size_xz.y)
	mesh.material = material
	var mesh_instance := MeshInstance3D.new()
	mesh_instance.mesh = mesh
	body.add_child(mesh_instance)
	var shape := BoxShape3D.new()
	shape.size = Vector3(size_xz.x, 0.2, size_xz.y)
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

func _add_marker(text: String, position: Vector3) -> void:
	var marker := Node3D.new()
	marker.name = "Marker_%s" % text.replace(" ", "_").replace("/", "_")
	marker.position = position
	add_child(marker)
	var mesh := CylinderMesh.new()
	mesh.top_radius = 0.22
	mesh.bottom_radius = 0.28
	mesh.height = 2.0
	mesh.material = _marker_material
	var pillar := MeshInstance3D.new()
	pillar.mesh = mesh
	pillar.position.y = 1.0
	marker.add_child(pillar)
	var label := Label3D.new()
	label.text = text
	label.font_size = 40
	label.outline_size = 8
	label.position = Vector3(0, 2.6, 0)
	marker.add_child(label)

func _set_camera_variant(index: int) -> void:
	match index:
		0:
			camera.position = Vector3(0, 5.5, 7.5)
			camera.rotation_degrees = Vector3(-25, 0, 0)
			camera.fov = 60.0
			camera_label.text = "Camera A — proof-near"
		1:
			camera.position = Vector3(0, 6.5, 8.5)
			camera.rotation_degrees = Vector3(-30, 0, 0)
			camera.fov = 56.0
			camera_label.text = "Camera B — HD-2D test"
		2:
			camera.position = Vector3(0, 7.5, 9.5)
			camera.rotation_degrees = Vector3(-34, 0, 0)
			camera.fov = 54.0
			camera_label.text = "Camera C — broad readability"

func _reset_player() -> void:
	player.global_position = PLAYER_START
	player.velocity = Vector3.ZERO

func _update_location_label() -> void:
	var z := player.global_position.z
	if z > -110.0:
		location_label.text = "CH00_F01 — Convoy Road"
	elif z > -246.0:
		location_label.text = "CH00_F02 — Wreck Field"
	elif z > -409.0:
		location_label.text = "CH00_F03 — Recovery Line"
	elif z > -500.0:
		location_label.text = "CH00_F04 — Field Triage Camp"
	else:
		location_label.text = "CH00_F03R — Survivor Recovery Sweep"
