extends "res://game/characters/presentation/rig_preview/ilyra_modular_blockout.gd"

# Stage 5: authored-geometry character proof on the exact UAL animation foundation.
# The skinned Ilyra_AnimeBody_UAL body remains underneath for deformation.
# These custom meshes are still a production-direction prototype; the approved B00 image remains visual authority.

var authored_geometry_root: Node3D
var authored_cape_pivots: Array[Node3D] = []
var authored_hair_pivots: Array[Node3D] = []
var authored_tabard_pivots: Array[Node3D] = []
var _auto_turntable := false

func _build_modular_ilyra() -> void:
	if skeleton == null:
		return
	authored_geometry_root = Node3D.new()
	authored_geometry_root.name = "Ilyra_Authored_Geometry"
	modular_root.add_child(authored_geometry_root)
	_build_authored_head()
	_build_authored_hair()
	_build_authored_torso()
	_build_authored_waist_and_tabards()
	_build_arm_gear()
	_build_leg_gear()
	_build_authored_cape()
	_build_authored_wardrod()
	_build_authored_shield()

func _process(delta: float) -> void:
	super._process(delta)
	if _auto_turntable and actor != null and not _paused:
		actor.rotate_y(deg_to_rad(18.0 * delta))

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo and event.keycode == KEY_T:
		_auto_turntable = not _auto_turntable
		_update_hud(str(DEMO_CLIPS[_clip_index]["label"]), str(DEMO_CLIPS[_clip_index]["name"]))
		return
	super._unhandled_input(event)

func _build_authored_head() -> void:
	var head := _authored_bone_attachment("Ilyra_Head_Authored", "Head")
	if head == null:
		return

	var face := MeshInstance3D.new()
	face.name = "AnimeFaceMesh"
	face.mesh = _anime_head_mesh()
	face.material_override = mat_skin
	face.position = Vector3(0.0, 0.016, 0.010)
	head.add_child(face)

	var eye_white_material := _make_material(Color(0.97, 0.97, 0.95, 1.0), 0.52, 0.0)
	for x in [-0.037, 0.037]:
		var eye := _tapered_prism("EyeWhite", Vector3(x, 0.041, 0.111), 0.040, 0.034, 0.017, 0.007, eye_white_material)
		head.add_child(eye)
		var iris := _sphere("JadeIris", Vector3(x, 0.041, 0.118), Vector3(0.0105, 0.0115, 0.0045), mat_jade)
		head.add_child(iris)

	head.add_child(_tapered_prism("NoseBridge", Vector3(0.0, 0.005, 0.119), 0.016, 0.010, 0.050, 0.010, mat_skin))
	head.add_child(_tapered_prism("LowerLip", Vector3(0.0, -0.044, 0.115), 0.032, 0.024, 0.008, 0.008, _make_material(Color(0.58, 0.28, 0.26, 1.0), 0.68, 0.0)))

func _build_authored_hair() -> void:
	var head := _authored_bone_attachment("Ilyra_Hair_Authored", "Head")
	if head == null:
		return

	var cap := MeshInstance3D.new()
	cap.name = "HairCapMesh"
	cap.mesh = _hair_cap_mesh()
	cap.material_override = mat_hair
	cap.position = Vector3(0.0, 0.030, -0.020)
	head.add_child(cap)

	var lock_specs := [
		{"points": [Vector3(-0.105, -0.015, -0.030), Vector3(-0.130, -0.135, -0.050), Vector3(-0.155, -0.285, -0.060), Vector3(-0.185, -0.455, -0.050)], "widths": [0.046, 0.044, 0.035, 0.012]},
		{"points": [Vector3(-0.055, -0.030, -0.085), Vector3(-0.065, -0.170, -0.105), Vector3(-0.085, -0.355, -0.115), Vector3(-0.115, -0.565, -0.090)], "widths": [0.052, 0.050, 0.038, 0.013]},
		{"points": [Vector3(0.005, -0.035, -0.105), Vector3(0.015, -0.185, -0.125), Vector3(0.035, -0.385, -0.130), Vector3(0.085, -0.600, -0.095)], "widths": [0.052, 0.050, 0.038, 0.013]},
		{"points": [Vector3(0.075, -0.020, -0.075), Vector3(0.110, -0.150, -0.080), Vector3(0.155, -0.300, -0.065), Vector3(0.210, -0.455, -0.025)], "widths": [0.046, 0.042, 0.032, 0.011]},
		{"points": [Vector3(-0.115, 0.010, 0.035), Vector3(-0.135, -0.085, 0.040), Vector3(-0.145, -0.205, 0.025)], "widths": [0.032, 0.026, 0.008]},
		{"points": [Vector3(0.115, 0.010, 0.035), Vector3(0.140, -0.080, 0.045), Vector3(0.155, -0.195, 0.030)], "widths": [0.032, 0.026, 0.008]},
	]
	for i in range(lock_specs.size()):
		var spec: Dictionary = lock_specs[i]
		var pivot := Node3D.new()
		pivot.name = "HairLockPivot_%02d" % i
		head.add_child(pivot)
		var lock := MeshInstance3D.new()
		lock.name = "WindsweptHairLock_%02d" % i
		lock.mesh = _ribbon_mesh(spec["points"], spec["widths"], 0.012)
		lock.material_override = mat_hair
		pivot.add_child(lock)
		authored_hair_pivots.append(pivot)

func _build_authored_torso() -> void:
	var chest := _authored_bone_attachment("Ilyra_Torso_Authored", "spine_03")
	if chest == null:
		return

	chest.add_child(_tapered_prism("IvoryWardenVest", Vector3(0.0, -0.105, 0.052), 0.315, 0.255, 0.355, 0.130, mat_ivory))
	chest.add_child(_tapered_prism("PaleBlueCenterPanel", Vector3(0.0, -0.105, 0.121), 0.080, 0.065, 0.300, 0.014, mat_blue))
	chest.add_child(_tapered_prism("HighBlueCollar", Vector3(0.0, 0.090, 0.048), 0.205, 0.170, 0.085, 0.125, mat_blue_dark))

	for x in [-0.118, 0.118]:
		var trim := _tapered_prism("AntiqueGoldEdge", Vector3(x, -0.105, 0.132), 0.012, 0.010, 0.285, 0.009, mat_gold)
		chest.add_child(trim)
	chest.add_child(_sphere("CapeClasp", Vector3(0.0, 0.030, 0.139), Vector3(0.029, 0.029, 0.014), mat_silver))
	chest.add_child(_tapered_prism("BluePendant", Vector3(0.0, -0.010, 0.148), 0.026, 0.012, 0.050, 0.012, mat_blue))

func _build_authored_waist_and_tabards() -> void:
	var pelvis := _authored_bone_attachment("Ilyra_Waist_Authored", "pelvis")
	if pelvis == null:
		return

	pelvis.add_child(_tapered_prism("LeatherBelt", Vector3(0.0, 0.020, 0.015), 0.385, 0.370, 0.055, 0.175, mat_leather))
	pelvis.add_child(_tapered_prism("SilverBuckle", Vector3(0.0, 0.020, 0.112), 0.065, 0.055, 0.052, 0.016, mat_silver))
	pelvis.add_child(_tapered_prism("LeftPouch", Vector3(-0.205, -0.050, 0.020), 0.105, 0.090, 0.130, 0.080, mat_leather))
	pelvis.add_child(_tapered_prism("RightUtility", Vector3(0.205, -0.065, -0.002), 0.078, 0.065, 0.105, 0.065, mat_leather))

	var panels := [
		{"name": "FrontIvoryTabard", "pos": Vector3(0.0, -0.105, 0.115), "top": 0.145, "bottom": 0.075, "height": 0.43, "mat": mat_ivory},
		{"name": "FrontBlueInset", "pos": Vector3(0.0, -0.100, 0.128), "top": 0.066, "bottom": 0.032, "height": 0.365, "mat": mat_blue},
		{"name": "LeftLayer", "pos": Vector3(-0.137, -0.095, 0.030), "top": 0.120, "bottom": 0.070, "height": 0.335, "mat": mat_ivory},
		{"name": "RightLayer", "pos": Vector3(0.137, -0.095, 0.028), "top": 0.120, "bottom": 0.070, "height": 0.335, "mat": mat_blue},
	]
	for spec in panels:
		var pivot := Node3D.new()
		pivot.name = str(spec["name"]) + "Pivot"
		pivot.position = spec["pos"]
		pelvis.add_child(pivot)
		var panel := _tapered_prism(str(spec["name"]), Vector3(0.0, -float(spec["height"]) * 0.43, 0.0), float(spec["top"]), float(spec["bottom"]), float(spec["height"]), 0.018, spec["mat"])
		pivot.add_child(panel)
		authored_tabard_pivots.append(pivot)

func _build_authored_cape() -> void:
	var chest := _authored_bone_attachment("Ilyra_Cape_Authored", "spine_03")
	if chest == null:
		return

	chest.add_child(_tapered_prism("CapeShoulderMantle", Vector3(0.0, 0.020, -0.120), 0.455, 0.395, 0.145, 0.050, mat_blue))
	var cape_specs := [
		{"points": [Vector3(0.0, 0.0, 0.0), Vector3(0.0, -0.22, -0.012), Vector3(0.012, -0.47, -0.022)], "widths": [0.205, 0.215, 0.180]},
		{"points": [Vector3(0.0, -0.42, -0.010), Vector3(-0.012, -0.63, -0.020), Vector3(-0.030, -0.84, -0.012)], "widths": [0.185, 0.165, 0.115]},
		{"points": [Vector3(-0.025, -0.78, -0.008), Vector3(-0.050, -0.96, 0.005), Vector3(-0.085, -1.12, 0.030)], "widths": [0.120, 0.095, 0.025]},
	]
	for i in range(cape_specs.size()):
		var spec: Dictionary = cape_specs[i]
		var pivot := Node3D.new()
		pivot.name = "CapeAuthoredPivot_%02d" % i
		pivot.position = Vector3(0.0, -0.08 if i == 0 else 0.0, -0.145 - 0.006 * i)
		chest.add_child(pivot)
		var panel := MeshInstance3D.new()
		panel.name = "CapeCloth_%02d" % i
		panel.mesh = _ribbon_mesh(spec["points"], spec["widths"], 0.014)
		panel.material_override = mat_blue
		pivot.add_child(panel)
		authored_cape_pivots.append(pivot)

func _build_authored_wardrod() -> void:
	var hand := _authored_bone_attachment("Ilyra_Wardrod_Authored", "hand_r")
	if hand == null:
		return
	var root := Node3D.new()
	root.name = "WardrodRoot"
	root.position = Vector3(0.0, -0.075, 0.020)
	root.rotation_degrees.z = 7.0
	hand.add_child(root)

	root.add_child(_radial_prism_y("WardrodSilverShaft", Vector3(0.0, -0.275, 0.0), 0.018, 0.017, 0.64, 8, mat_silver))
	root.add_child(_radial_prism_y("WardrodLeatherGrip", Vector3(0.0, -0.085, 0.0), 0.026, 0.024, 0.17, 8, mat_leather))
	root.add_child(_radial_prism_y("WardrodGoldPommel", Vector3(0.0, 0.062, 0.0), 0.031, 0.024, 0.052, 8, mat_gold))

	var focus := _extruded_polygon("WardrodFocus", Vector3(0.0, -0.605, 0.0), [Vector2(0.0, 0.075), Vector2(0.050, 0.0), Vector2(0.0, -0.075), Vector2(-0.050, 0.0)], 0.030, mat_blue)
	root.add_child(focus)
	root.add_child(_radial_prism_y("WardrodFocusCollar", Vector3(0.0, -0.530, 0.0), 0.038, 0.030, 0.040, 8, mat_gold))

func _build_authored_shield() -> void:
	var hand := _authored_bone_attachment("Ilyra_Shield_Authored", "hand_l")
	if hand == null:
		return
	var root := Node3D.new()
	root.name = "ShieldRoot"
	root.position = Vector3(-0.035, -0.020, 0.135)
	hand.add_child(root)

	var outline := [
		Vector2(0.0, 0.255), Vector2(0.165, 0.175), Vector2(0.205, 0.015),
		Vector2(0.135, -0.175), Vector2(0.0, -0.255), Vector2(-0.135, -0.175),
		Vector2(-0.205, 0.015), Vector2(-0.165, 0.175)
	]
	root.add_child(_extruded_polygon("WardenShieldSilver", Vector3.ZERO, outline, 0.034, mat_silver))
	var inset: Array[Vector2] = []
	for point in outline:
		inset.append(point * 0.78)
	root.add_child(_extruded_polygon("WardenShieldBlueInset", Vector3(0.0, 0.0, 0.021), inset, 0.010, mat_blue))
	root.add_child(_radial_prism_z("ShieldBoss", Vector3(0.0, 0.0, 0.036), 0.064, 0.052, 0.035, 10, mat_silver))

func _authored_bone_attachment(node_name: String, bone_name: String) -> BoneAttachment3D:
	return _bone_attachment(node_name, bone_name)

func _anime_head_mesh() -> ArrayMesh:
	var rings := [
		{"y": -0.135, "rx": 0.050, "rz": 0.060, "z": 0.000},
		{"y": -0.095, "rx": 0.082, "rz": 0.080, "z": 0.008},
		{"y": -0.035, "rx": 0.108, "rz": 0.098, "z": 0.012},
		{"y": 0.035, "rx": 0.124, "rz": 0.106, "z": 0.006},
		{"y": 0.105, "rx": 0.108, "rz": 0.102, "z": -0.002},
		{"y": 0.155, "rx": 0.072, "rz": 0.082, "z": -0.010},
	]
	return _ring_surface_mesh(rings, 12, 1.0)

func _hair_cap_mesh() -> ArrayMesh:
	var rings := [
		{"y": -0.090, "rx": 0.125, "rz": 0.112, "z": -0.012},
		{"y": -0.010, "rx": 0.145, "rz": 0.132, "z": -0.022},
		{"y": 0.085, "rx": 0.148, "rz": 0.137, "z": -0.028},
		{"y": 0.165, "rx": 0.095, "rz": 0.105, "z": -0.035},
	]
	return _ring_surface_mesh(rings, 14, 0.78)

func _ring_surface_mesh(rings: Array, segments: int, front_scale: float) -> ArrayMesh:
	var vertices: Array[Vector3] = []
	for ring in rings:
		for i in range(segments):
			var angle := TAU * float(i) / float(segments)
			var x := cos(angle) * float(ring["rx"])
			var z_radius := float(ring["rz"])
			var z := sin(angle) * z_radius
			if z > 0.0:
				z *= front_scale
			vertices.append(Vector3(x, float(ring["y"]), z + float(ring["z"])))
	var indices: Array[int] = []
	for r in range(rings.size() - 1):
		for i in range(segments):
			var next := (i + 1) % segments
			var a := r * segments + i
			var b := r * segments + next
			var c := (r + 1) * segments + next
			var d := (r + 1) * segments + i
			indices.append_array([a, b, c, a, c, d])
	return _surface_mesh(vertices, indices)

func _tapered_prism(node_name: String, position: Vector3, top_width: float, bottom_width: float, height: float, depth: float, material: Material) -> MeshInstance3D:
	var top_y := height * 0.5
	var bottom_y := -height * 0.5
	var td := depth * 0.5
	var bd := depth * 0.5
	var vertices: Array[Vector3] = [
		Vector3(-top_width * 0.5, top_y, td), Vector3(top_width * 0.5, top_y, td),
		Vector3(top_width * 0.5, top_y, -td), Vector3(-top_width * 0.5, top_y, -td),
		Vector3(-bottom_width * 0.5, bottom_y, bd), Vector3(bottom_width * 0.5, bottom_y, bd),
		Vector3(bottom_width * 0.5, bottom_y, -bd), Vector3(-bottom_width * 0.5, bottom_y, -bd),
	]
	var indices: Array[int] = [
		0, 1, 5, 0, 5, 4,
		1, 2, 6, 1, 6, 5,
		2, 3, 7, 2, 7, 6,
		3, 0, 4, 3, 4, 7,
		0, 3, 2, 0, 2, 1,
		4, 5, 6, 4, 6, 7,
	]
	var node := MeshInstance3D.new()
	node.name = node_name
	node.mesh = _surface_mesh(vertices, indices)
	node.material_override = material
	node.position = position
	return node

func _ribbon_mesh(points: Array, widths: Array, depth: float) -> ArrayMesh:
	var vertices: Array[Vector3] = []
	for side_z in [depth * 0.5, -depth * 0.5]:
		for i in range(points.size()):
			var p: Vector3 = points[i]
			var half_w := float(widths[i])
			vertices.append(Vector3(p.x - half_w, p.y, p.z + side_z))
			vertices.append(Vector3(p.x + half_w, p.y, p.z + side_z))
	var row_count := points.size()
	var front_offset := 0
	var back_offset := row_count * 2
	var indices: Array[int] = []
	for i in range(row_count - 1):
		var f0 := front_offset + i * 2
		var f1 := f0 + 1
		var f2 := f0 + 2
		var f3 := f0 + 3
		indices.append_array([f0, f1, f3, f0, f3, f2])
		var b0 := back_offset + i * 2
		var b1 := b0 + 1
		var b2 := b0 + 2
		var b3 := b0 + 3
		indices.append_array([b0, b3, b1, b0, b2, b3])
		indices.append_array([f0, f2, b2, f0, b2, b0])
		indices.append_array([f1, b1, b3, f1, b3, f3])
	indices.append_array([0, back_offset, back_offset + 1, 0, back_offset + 1, 1])
	var last_front := (row_count - 1) * 2
	var last_back := back_offset + last_front
	indices.append_array([last_front, last_front + 1, last_back + 1, last_front, last_back + 1, last_back])
	return _surface_mesh(vertices, indices)

func _extruded_polygon(node_name: String, position: Vector3, outline: Array, depth: float, material: Material) -> MeshInstance3D:
	var vertices: Array[Vector3] = []
	var front_z := depth * 0.5
	var back_z := -depth * 0.5
	for p in outline:
		vertices.append(Vector3(float(p.x), float(p.y), front_z))
	for p in outline:
		vertices.append(Vector3(float(p.x), float(p.y), back_z))
	var n := outline.size()
	var indices: Array[int] = []
	for i in range(1, n - 1):
		indices.append_array([0, i, i + 1])
		indices.append_array([n, n + i + 1, n + i])
	for i in range(n):
		var next := (i + 1) % n
		indices.append_array([i, n + i, n + next, i, n + next, next])
	var node := MeshInstance3D.new()
	node.name = node_name
	node.mesh = _surface_mesh(vertices, indices)
	node.material_override = material
	node.position = position
	return node

func _radial_prism_y(node_name: String, position: Vector3, top_radius: float, bottom_radius: float, height: float, segments: int, material: Material) -> MeshInstance3D:
	var vertices: Array[Vector3] = []
	var top_y := height * 0.5
	var bottom_y := -height * 0.5
	for y_and_radius in [[top_y, top_radius], [bottom_y, bottom_radius]]:
		for i in range(segments):
			var angle := TAU * float(i) / float(segments)
			vertices.append(Vector3(cos(angle) * float(y_and_radius[1]), float(y_and_radius[0]), sin(angle) * float(y_and_radius[1])))
	var indices: Array[int] = []
	for i in range(segments):
		var next := (i + 1) % segments
		indices.append_array([i, segments + i, segments + next, i, segments + next, next])
	for i in range(1, segments - 1):
		indices.append_array([0, i + 1, i])
		indices.append_array([segments, segments + i, segments + i + 1])
	var node := MeshInstance3D.new()
	node.name = node_name
	node.mesh = _surface_mesh(vertices, indices)
	node.material_override = material
	node.position = position
	return node

func _radial_prism_z(node_name: String, position: Vector3, front_radius: float, back_radius: float, depth: float, segments: int, material: Material) -> MeshInstance3D:
	var vertices: Array[Vector3] = []
	var front_z := depth * 0.5
	var back_z := -depth * 0.5
	for z_and_radius in [[front_z, front_radius], [back_z, back_radius]]:
		for i in range(segments):
			var angle := TAU * float(i) / float(segments)
			vertices.append(Vector3(cos(angle) * float(z_and_radius[1]), sin(angle) * float(z_and_radius[1]), float(z_and_radius[0])))
	var indices: Array[int] = []
	for i in range(segments):
		var next := (i + 1) % segments
		indices.append_array([i, next, segments + next, i, segments + next, segments + i])
	for i in range(1, segments - 1):
		indices.append_array([0, i, i + 1])
		indices.append_array([segments, segments + i + 1, segments + i])
	var node := MeshInstance3D.new()
	node.name = node_name
	node.mesh = _surface_mesh(vertices, indices)
	node.material_override = material
	node.position = position
	return node

func _surface_mesh(vertices: Array[Vector3], indices: Array[int]) -> ArrayMesh:
	var surface_tool := SurfaceTool.new()
	surface_tool.begin(Mesh.PRIMITIVE_TRIANGLES)
	for i in range(0, indices.size(), 3):
		var a := vertices[indices[i]]
		var b := vertices[indices[i + 1]]
		var c := vertices[indices[i + 2]]
		# Helper index lists are authored clockwise from the visible exterior.
		# Flip B/C at commit time so Godot receives outward-facing CCW triangles.
		var normal := (c - a).cross(b - a).normalized()
		surface_tool.set_normal(normal)
		surface_tool.add_vertex(a)
		surface_tool.set_normal(normal)
		surface_tool.add_vertex(c)
		surface_tool.set_normal(normal)
		surface_tool.add_vertex(b)
	return surface_tool.commit() as ArrayMesh

func _update_secondary_motion() -> void:
	var speed_scale := 1.0
	if animation_player != null and animation_player.current_animation in [&"Walk_Loop", &"Jog_Fwd_Loop", &"Shield_Dash"]:
		speed_scale = 1.75
	for i in range(authored_cape_pivots.size()):
		var phase := _motion_time * (1.8 + i * 0.18) * speed_scale + i * 0.55
		authored_cape_pivots[i].rotation.x = deg_to_rad(5.0 + sin(phase) * (2.4 + i * 1.0))
		authored_cape_pivots[i].rotation.z = deg_to_rad(sin(phase * 0.68) * (0.9 + i * 0.45))
	for i in range(authored_hair_pivots.size()):
		var phase := _motion_time * (2.05 + i * 0.04) * speed_scale + i * 0.63
		authored_hair_pivots[i].rotation.x = deg_to_rad(2.0 + sin(phase) * 2.1)
		authored_hair_pivots[i].rotation.z = deg_to_rad(sin(phase * 0.72) * 1.25)
	for i in range(authored_tabard_pivots.size()):
		var phase := _motion_time * 1.85 * speed_scale + i * 0.60
		authored_tabard_pivots[i].rotation.x = deg_to_rad(1.5 + sin(phase) * 1.3)

func _update_hud(display_name: String, clip_name: String) -> void:
	if info_label == null:
		return
	var layer_state := "AUTHORED GEOMETRY ON" if _show_modular else "SKINNED UAL BODY ONLY"
	var turn_state := "AUTO TURN ON" if _auto_turntable else "AUTO TURN OFF"
	info_label.text = "Diyse — Ilyra authored-geometry / UAL proof\n%s  [%s]\n%s | %s | B00 remains exact visual authority\nSPACE next   P pause   V compare   Q/E rotate   T turntable   R restart   ESC quit" % [display_name, clip_name, layer_state, turn_state]
