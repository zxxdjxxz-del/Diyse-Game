extends "res://game/characters/presentation/rig_preview/ilyra_authored_geometry.gd"

# Stage 6: deformation-aware authored geometry on the unchanged 65-bone UAL skeleton.
# Long hair, fitted torso cloth, cape and tabards use actual ArrayMesh bone weights
# across multiple existing UAL bones. Rigid equipment stays bone-attached intentionally.

const DEFORMATION_TEST_CLIPS := [
	{"name": &"Idle_Loop", "hold": 2.4, "label": "Neutral / bind-pose read"},
	{"name": &"Walk_Loop", "hold": 2.3, "label": "Walk / weighted cloth"},
	{"name": &"Jog_Fwd_Loop", "hold": 2.1, "label": "Jog / torso + cape bend"},
	{"name": &"Crouch_Fwd_Loop", "hold": 2.2, "label": "Crouch / tabard compression"},
	{"name": &"Roll", "hold": 0.0, "label": "Roll / deformation stress"},
	{"name": &"Idle_Shield_Loop", "hold": 2.3, "label": "Blue Warden guard"},
	{"name": &"Shield_Dash", "hold": 0.0, "label": "Shield advance / cape stress"},
	{"name": &"Spell_Simple_Shoot", "hold": 0.0, "label": "Warden cast / upper-body bend"},
	{"name": &"Hit_Chest", "hold": 0.0, "label": "Hit / weighted recovery"},
]

var deformation_root: Node3D
var deformation_skin: Skin
var deformation_meshes: Array[MeshInstance3D] = []
var rigid_deformation_nodes: Array[Node3D] = []
var _use_weighted_deformation := true

func _apply_proxy_style() -> void:
	super._apply_proxy_style()
	if _proxy_skeleton == null:
		return
	_collect_rigid_deformation_nodes()
	deformation_root = Node3D.new()
	deformation_root.name = "Ilyra_DeformationAware_Root"
	_proxy_skeleton.add_child(deformation_root)
	deformation_skin = _proxy_skeleton.create_skin_from_rest_transforms()
	if deformation_skin == null:
		push_error("Ilyra Stage 6: failed to create Skin from UAL rest transforms.")
		return
	if deformation_skin.get_bind_count() != _proxy_skeleton.get_bone_count():
		push_warning("Ilyra Stage 6: skin bind count does not match skeleton bone count.")
	_build_weighted_torso()
	_build_weighted_hair()
	_build_weighted_cape()
	_build_weighted_tabards()
	_apply_deformation_mode_visibility()

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo:
		if event.keycode == KEY_K:
			_use_weighted_deformation = not _use_weighted_deformation
			_apply_deformation_mode_visibility()
			_update_hud(_current_label(), _current_clip_name())
			return
		if event.keycode == KEY_T:
			_auto_turntable = not _auto_turntable
			_update_hud(_current_label(), _current_clip_name())
			return
	super._unhandled_input(event)
	if event is InputEventKey and event.pressed and not event.echo and event.keycode == KEY_V:
		_apply_deformation_mode_visibility()
		_update_hud(_current_label(), _current_clip_name())

func _play_next_clip() -> void:
	if animation_player == null:
		return
	_clip_index = (_clip_index + 1) % DEFORMATION_TEST_CLIPS.size()
	var entry: Dictionary = DEFORMATION_TEST_CLIPS[_clip_index]
	var clip_name: StringName = entry["name"]
	if not animation_player.has_animation(clip_name):
		push_warning("Ilyra Stage 6: missing animation %s" % clip_name)
		_clip_time_left = 0.05
		return
	animation_player.play(clip_name, 0.18)
	var animation := animation_player.get_animation(clip_name)
	var requested_hold := float(entry["hold"])
	_clip_time_left = requested_hold if requested_hold > 0.0 else max(animation.length + 0.35, 0.8)
	_update_hud(str(entry["label"]), str(clip_name))

func _current_label() -> String:
	if _clip_index < 0 or _clip_index >= DEFORMATION_TEST_CLIPS.size():
		return "Ready"
	return str(DEFORMATION_TEST_CLIPS[_clip_index]["label"])

func _current_clip_name() -> String:
	if _clip_index < 0 or _clip_index >= DEFORMATION_TEST_CLIPS.size():
		return "none"
	return str(DEFORMATION_TEST_CLIPS[_clip_index]["name"])

func _collect_rigid_deformation_nodes() -> void:
	for node in authored_hair_pivots:
		rigid_deformation_nodes.append(node)
	for node in authored_cape_pivots:
		rigid_deformation_nodes.append(node)
	for node in authored_tabard_pivots:
		rigid_deformation_nodes.append(node)
	_collect_named_nodes(_proxy_skeleton, ["IvoryWardenVest", "PaleBlueCenterPanel"])

func _collect_named_nodes(node: Node, wanted_names: Array) -> void:
	if node is Node3D and wanted_names.has(str(node.name)):
		rigid_deformation_nodes.append(node as Node3D)
	for child in node.get_children():
		_collect_named_nodes(child, wanted_names)

func _apply_deformation_mode_visibility() -> void:
	var weighted_visible := _authored_visible and _use_weighted_deformation
	if deformation_root != null:
		deformation_root.visible = weighted_visible
	for node in rigid_deformation_nodes:
		if is_instance_valid(node):
			node.visible = _authored_visible and not _use_weighted_deformation

func _update_secondary_motion() -> void:
	# Stage 6 weighted geometry follows the real skeleton. The Stage 5 procedural
	# follow-through is retained only when K selects the rigid comparison geometry.
	if not _use_weighted_deformation:
		super._update_secondary_motion()

func _build_weighted_torso() -> void:
	var rows := [
		{"center": _bone_origin("spine_03") + Vector3(0.0, 0.105, 0.030), "rx": 0.155, "rz": 0.078, "weights": _weights({"spine_03": 0.92, "spine_02": 0.08})},
		{"center": _bone_origin("spine_03") + Vector3(0.0, -0.030, 0.035), "rx": 0.165, "rz": 0.083, "weights": _weights({"spine_03": 0.72, "spine_02": 0.28})},
		{"center": _bone_origin("spine_02") + Vector3(0.0, -0.025, 0.042), "rx": 0.148, "rz": 0.078, "weights": _weights({"spine_02": 0.76, "spine_01": 0.24})},
		{"center": _bone_origin("spine_01") + Vector3(0.0, -0.028, 0.044), "rx": 0.132, "rz": 0.073, "weights": _weights({"spine_01": 0.68, "pelvis": 0.32})},
		{"center": _bone_origin("pelvis") + Vector3(0.0, 0.105, 0.042), "rx": 0.122, "rz": 0.069, "weights": _weights({"pelvis": 0.84, "spine_01": 0.16})},
	]
	var vertices: Array[Vector3] = []
	var influences: Array[Dictionary] = []
	var segments := 12
	for row in rows:
		for i in range(segments):
			var angle := TAU * float(i) / float(segments)
			var center: Vector3 = row["center"]
			vertices.append(center + Vector3(cos(angle) * float(row["rx"]), 0.0, sin(angle) * float(row["rz"])))
			influences.append(row["weights"])
	var indices: Array[int] = []
	for r in range(rows.size() - 1):
		for i in range(segments):
			var next := (i + 1) % segments
			var a := r * segments + i
			var b := r * segments + next
			var c := (r + 1) * segments + next
			var d := (r + 1) * segments + i
			indices.append_array([a, b, c, a, c, d])
	_add_weighted_mesh("WeightedWardenVest", vertices, indices, influences, _ivory, true)
	var panel_vertices: Array[Vector3] = []
	var panel_influences: Array[Dictionary] = []
	for row in rows:
		var center: Vector3 = row["center"]
		var front_z := center.z + float(row["rz"]) + 0.006
		panel_vertices.append(Vector3(-0.035, center.y, front_z))
		panel_vertices.append(Vector3(0.035, center.y, front_z))
		panel_influences.append(row["weights"])
		panel_influences.append(row["weights"])
	_add_weighted_mesh("WeightedBlueCenterPanel", panel_vertices, _strip_indices(rows.size(), 2), panel_influences, _pale_blue, true)

func _build_weighted_hair() -> void:
	var head := _bone_origin("Head")
	var spine_03 := _bone_origin("spine_03")
	var lock_specs := [
		{"x": -0.105, "drift": -0.080, "z": -0.090, "width": 0.047},
		{"x": -0.040, "drift": -0.030, "z": -0.115, "width": 0.052},
		{"x": 0.025, "drift": 0.050, "z": -0.118, "width": 0.052},
		{"x": 0.092, "drift": 0.115, "z": -0.085, "width": 0.045},
	]
	var y_values := [head.y + 0.035, head.y - 0.100, head.y - 0.245, head.y - 0.405, spine_03.y - 0.220]
	var row_weights := [
		_weights({"Head": 1.0}),
		_weights({"Head": 0.78, "neck_01": 0.22}),
		_weights({"Head": 0.36, "neck_01": 0.54, "spine_03": 0.10}),
		_weights({"neck_01": 0.32, "spine_03": 0.68}),
		_weights({"spine_03": 0.82, "spine_02": 0.18}),
	]
	for lock_i in range(lock_specs.size()):
		var spec: Dictionary = lock_specs[lock_i]
		var vertices: Array[Vector3] = []
		var influences: Array[Dictionary] = []
		for row_i in range(y_values.size()):
			var t := float(row_i) / float(y_values.size() - 1)
			var center_x := lerp(float(spec["x"]), float(spec["drift"]), t)
			var center_z := float(spec["z"]) + sin(t * PI) * -0.018
			var half_width := lerp(float(spec["width"]), 0.010, t)
			vertices.append(Vector3(center_x - half_width, float(y_values[row_i]), center_z))
			vertices.append(Vector3(center_x + half_width, float(y_values[row_i]), center_z))
			influences.append(row_weights[row_i])
			influences.append(row_weights[row_i])
		_add_weighted_mesh("WeightedHairLock_%02d" % lock_i, vertices, _strip_indices(y_values.size(), 2), influences, _authored_hair, true)

func _build_weighted_cape() -> void:
	var spine_03 := _bone_origin("spine_03")
	var spine_02 := _bone_origin("spine_02")
	var spine_01 := _bone_origin("spine_01")
	var pelvis := _bone_origin("pelvis")
	var row_specs := [
		{"y": spine_03.y + 0.030, "x": 0.000, "z": -0.145, "half": 0.225, "weights": _weights({"spine_03": 1.0})},
		{"y": spine_02.y + 0.010, "x": 0.000, "z": -0.150, "half": 0.235, "weights": _weights({"spine_03": 0.46, "spine_02": 0.54})},
		{"y": spine_01.y - 0.035, "x": -0.006, "z": -0.145, "half": 0.228, "weights": _weights({"spine_02": 0.46, "spine_01": 0.44, "pelvis": 0.10})},
		{"y": pelvis.y - 0.105, "x": -0.018, "z": -0.135, "half": 0.205, "weights": _weights({"spine_01": 0.34, "pelvis": 0.66})},
		{"y": pelvis.y - 0.365, "x": -0.042, "z": -0.115, "half": 0.165, "weights": _weights({"pelvis": 1.0})},
		{"y": pelvis.y - 0.575, "x": -0.075, "z": -0.085, "half": 0.075, "weights": _weights({"pelvis": 1.0})},
	]
	var columns := 7
	var vertices: Array[Vector3] = []
	var influences: Array[Dictionary] = []
	for row in row_specs:
		for c in range(columns):
			var u := float(c) / float(columns - 1)
			var x := float(row["x"]) + lerp(-float(row["half"]), float(row["half"]), u)
			var z := float(row["z"]) - sin(u * PI) * 0.018
			vertices.append(Vector3(x, float(row["y"]), z))
			influences.append(row["weights"])
	_add_weighted_mesh("WeightedPaleBlueCape", vertices, _strip_indices(row_specs.size(), columns), influences, _pale_blue, true)

func _build_weighted_tabards() -> void:
	var pelvis := _bone_origin("pelvis")
	var thigh_l := _bone_origin("thigh_l")
	var thigh_r := _bone_origin("thigh_r")
	var y_values := [pelvis.y + 0.020, pelvis.y - 0.095, pelvis.y - 0.205, pelvis.y - 0.320, pelvis.y - 0.435]
	var row_weights := [
		_weights({"pelvis": 1.0}),
		_weights({"pelvis": 0.82, "thigh_l": 0.09, "thigh_r": 0.09}),
		_weights({"pelvis": 0.62, "thigh_l": 0.19, "thigh_r": 0.19}),
		_weights({"pelvis": 0.38, "thigh_l": 0.31, "thigh_r": 0.31}),
		_weights({"pelvis": 0.18, "thigh_l": 0.41, "thigh_r": 0.41}),
	]
	var front_vertices: Array[Vector3] = []
	var front_influences: Array[Dictionary] = []
	var columns := 3
	for row_i in range(y_values.size()):
		var width := lerp(0.145, 0.075, float(row_i) / float(y_values.size() - 1))
		for c in range(columns):
			var u := float(c) / float(columns - 1)
			front_vertices.append(Vector3(lerp(-width, width, u), float(y_values[row_i]), 0.112))
			front_influences.append(row_weights[row_i])
	_add_weighted_mesh("WeightedFrontIvoryTabard", front_vertices, _strip_indices(y_values.size(), columns), front_influences, _ivory, true)
	var inset_vertices: Array[Vector3] = []
	var inset_influences: Array[Dictionary] = []
	for row_i in range(y_values.size()):
		var width := lerp(0.050, 0.023, float(row_i) / float(y_values.size() - 1))
		inset_vertices.append(Vector3(-width, float(y_values[row_i]) + 0.006, 0.119))
		inset_vertices.append(Vector3(width, float(y_values[row_i]) + 0.006, 0.119))
		inset_influences.append(row_weights[row_i])
		inset_influences.append(row_weights[row_i])
	_add_weighted_mesh("WeightedFrontBlueInset", inset_vertices, _strip_indices(y_values.size(), 2), inset_influences, _pale_blue, true)
	_build_weighted_side_tabard("WeightedLeftSideTabard", 0.145, thigh_l, "thigh_l", _ivory)
	_build_weighted_side_tabard("WeightedRightSideTabard", -0.145, thigh_r, "thigh_r", _pale_blue)

func _build_weighted_side_tabard(node_name: String, x: float, thigh_origin: Vector3, thigh_bone: String, material: Material) -> void:
	var pelvis := _bone_origin("pelvis")
	var rows := 4
	var vertices: Array[Vector3] = []
	var influences: Array[Dictionary] = []
	for row_i in range(rows):
		var t := float(row_i) / float(rows - 1)
		var y := lerp(pelvis.y - 0.015, thigh_origin.y - 0.345, t)
		var center_x := lerp(x, x * 1.05, t)
		var half_width := lerp(0.062, 0.035, t)
		vertices.append(Vector3(center_x - half_width, y, 0.035))
		vertices.append(Vector3(center_x + half_width, y, 0.035))
		var named_weights: Dictionary = {"pelvis": 1.0 - t * 0.82}
		named_weights[thigh_bone] = t * 0.82
		var influence := _weights(named_weights)
		influences.append(influence)
		influences.append(influence)
	_add_weighted_mesh(node_name, vertices, _strip_indices(rows, 2), influences, material, true)

func _strip_indices(rows: int, columns: int) -> Array[int]:
	var indices: Array[int] = []
	for r in range(rows - 1):
		for c in range(columns - 1):
			var a := r * columns + c
			var b := a + 1
			var d := (r + 1) * columns + c
			var e := d + 1
			indices.append_array([a, b, e, a, e, d])
	return indices

func _weights(named_weights: Dictionary) -> Dictionary:
	var result: Dictionary = {}
	var total := 0.0
	for bone_name in named_weights:
		var bone_idx := _proxy_skeleton.find_bone(str(bone_name))
		if bone_idx < 0:
			push_error("Ilyra Stage 6: missing required bone '%s'." % str(bone_name))
			continue
		var weight := float(named_weights[bone_name])
		if weight <= 0.0:
			continue
		result[bone_idx] = weight
		total += weight
	if total <= 0.0:
		return {0: 1.0}
	for bone_idx in result.keys():
		result[bone_idx] = float(result[bone_idx]) / total
	return result

func _bone_origin(bone_name: String) -> Vector3:
	var bone_idx := _proxy_skeleton.find_bone(bone_name)
	if bone_idx < 0:
		push_error("Ilyra Stage 6: missing required bone '%s'." % bone_name)
		return Vector3.ZERO
	return _proxy_skeleton.get_bone_global_rest(bone_idx).origin

func _add_weighted_mesh(node_name: String, vertices: Array[Vector3], indices: Array[int], influences: Array[Dictionary], material: Material, double_sided: bool) -> MeshInstance3D:
	if vertices.size() != influences.size():
		push_error("Ilyra Stage 6: vertex/influence count mismatch for %s." % node_name)
		return null
	var normals := _calculate_normals(vertices, indices)
	var packed_vertices := PackedVector3Array()
	var packed_normals := PackedVector3Array()
	var packed_indices := PackedInt32Array()
	var packed_bones := PackedInt32Array()
	var packed_weights := PackedFloat32Array()
	for vertex in vertices:
		packed_vertices.append(vertex)
	for normal in normals:
		packed_normals.append(normal)
	for index in indices:
		packed_indices.append(index)
	for influence in influences:
		_pack_four_influences(influence, packed_bones, packed_weights)
	var arrays := []
	arrays.resize(Mesh.ARRAY_MAX)
	arrays[Mesh.ARRAY_VERTEX] = packed_vertices
	arrays[Mesh.ARRAY_NORMAL] = packed_normals
	arrays[Mesh.ARRAY_BONES] = packed_bones
	arrays[Mesh.ARRAY_WEIGHTS] = packed_weights
	arrays[Mesh.ARRAY_INDEX] = packed_indices
	var array_mesh := ArrayMesh.new()
	array_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arrays)
	var mesh_instance := MeshInstance3D.new()
	mesh_instance.name = node_name
	mesh_instance.mesh = array_mesh
	var active_material := material
	if double_sided:
		active_material = material.duplicate() as Material
		if active_material is BaseMaterial3D:
			(active_material as BaseMaterial3D).cull_mode = BaseMaterial3D.CULL_DISABLED
	mesh_instance.material_override = active_material
	deformation_root.add_child(mesh_instance)
	mesh_instance.skin = deformation_skin
	mesh_instance.skeleton = mesh_instance.get_path_to(_proxy_skeleton)
	deformation_meshes.append(mesh_instance)
	return mesh_instance

func _pack_four_influences(influence: Dictionary, packed_bones: PackedInt32Array, packed_weights: PackedFloat32Array) -> void:
	var bone_slots: Array[int] = []
	var weight_slots: Array[float] = []
	for bone_idx in influence.keys():
		if bone_slots.size() >= 4:
			break
		bone_slots.append(int(bone_idx))
		weight_slots.append(float(influence[bone_idx]))
	while bone_slots.size() < 4:
		bone_slots.append(0)
		weight_slots.append(0.0)
	for i in range(4):
		packed_bones.append(bone_slots[i])
		packed_weights.append(weight_slots[i])

func _calculate_normals(vertices: Array[Vector3], indices: Array[int]) -> Array[Vector3]:
	var normals: Array[Vector3] = []
	normals.resize(vertices.size())
	for i in range(normals.size()):
		normals[i] = Vector3.ZERO
	for i in range(0, indices.size(), 3):
		var ia := indices[i]
		var ib := indices[i + 1]
		var ic := indices[i + 2]
		var a := vertices[ia]
		var b := vertices[ib]
		var c := vertices[ic]
		var face_normal := (b - a).cross(c - a)
		if face_normal.length_squared() > 0.0000001:
			face_normal = face_normal.normalized()
			normals[ia] += face_normal
			normals[ib] += face_normal
			normals[ic] += face_normal
	for i in range(normals.size()):
		if normals[i].length_squared() <= 0.0000001:
			normals[i] = Vector3.FORWARD
		else:
			normals[i] = normals[i].normalized()
	return normals

func _update_hud(display_name: String, clip_name: String) -> void:
	if info_label == null:
		return
	var character_state := "CHARACTER ON" if _authored_visible else "UAL BODY ONLY"
	var deformation_state := "MULTI-BONE SKINNING" if _use_weighted_deformation else "STAGE 5 RIGID COMPARISON"
	var turn_state := "AUTO TURN ON" if _auto_turntable else "AUTO TURN OFF"
	info_label.text = "Diyse — Ilyra Stage 6 deformation-aware / UAL proof\n%s  [%s]\n%s | %s | %s\n65-bone UAL core unchanged; B00 remains visual authority\nSPACE next   P pause   V character/body   K weighted/rigid   Q/E rotate   T turntable   R restart" % [display_name, clip_name, character_state, deformation_state, turn_state]
