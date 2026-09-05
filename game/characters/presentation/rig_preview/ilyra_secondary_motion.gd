extends "res://game/characters/presentation/rig_preview/ilyra_production_topology.gd"

# Stage 8: dedicated spring-bone secondary motion for Ilyra's long hair and cape.
# The 65 imported UAL bones are preserved in their original order. This scene appends
# auxiliary bones only after the UAL core, then lets SpringBoneSimulator3D modify those
# extra chains after animation playback. Ilyra's approved B00 remains visual authority.

const UAL_CORE_BONE_COUNT := 65
const HAIR_CHAIN_COUNT := 5
const HAIR_BONES_PER_CHAIN := 4
const CAPE_CHAIN_COUNT := 3
const CAPE_BONES_PER_CHAIN := 5
const EXPECTED_SECONDARY_BONES := HAIR_CHAIN_COUNT * HAIR_BONES_PER_CHAIN + CAPE_CHAIN_COUNT * CAPE_BONES_PER_CHAIN

const SECONDARY_TEST_CLIPS := [
	{"name": &"A_TPose", "hold": 2.0, "label": "Secondary rig / rest inspection"},
	{"name": &"Walk_Loop", "hold": 2.4, "label": "Walk / hair + cape lag"},
	{"name": &"Jog_Fwd_Loop", "hold": 2.2, "label": "Jog / recovery"},
	{"name": &"Sprint_Loop", "hold": 2.0, "label": "Sprint / sustained trailing"},
	{"name": &"Jump_Start", "hold": 0.0, "label": "Jump start / upward inertia"},
	{"name": &"Jump_Land", "hold": 0.0, "label": "Landing / settle"},
	{"name": &"Roll", "hold": 0.0, "label": "Roll / secondary stress"},
	{"name": &"Shield_Dash", "hold": 0.0, "label": "Shield dash / cape kick"},
	{"name": &"Spell_Simple_Shoot", "hold": 0.0, "label": "Warden cast / shoulder follow-through"},
	{"name": &"Hit_Knockback", "hold": 0.0, "label": "Knockback / overshoot + recovery"},
]

var secondary_root: Node3D
var secondary_skin: Skin
var secondary_meshes: Array[MeshInstance3D] = []
var stage7_secondary_meshes: Array[MeshInstance3D] = []
var spring_simulator: SpringBoneSimulator3D
var secondary_debug_root: Node3D
var secondary_debug_attachments: Array[BoneAttachment3D] = []
var hair_chains: Array = []
var cape_chains: Array = []
var _use_secondary_motion := true
var _show_secondary_debug := false
var _wind_enabled := false
var _secondary_bone_count_at_build := 0

func _apply_proxy_style() -> void:
	super._apply_proxy_style()
	if _proxy_skeleton == null:
		return

	if _proxy_skeleton.get_bone_count() != UAL_CORE_BONE_COUNT:
		push_warning("Ilyra Stage 8 expected %d UAL core bones before secondary append; found %d." % [UAL_CORE_BONE_COUNT, _proxy_skeleton.get_bone_count()])

	_collect_stage7_secondary_meshes()
	_append_secondary_chains()
	_secondary_bone_count_at_build = _proxy_skeleton.get_bone_count()
	if _secondary_bone_count_at_build != UAL_CORE_BONE_COUNT + EXPECTED_SECONDARY_BONES:
		push_warning("Ilyra Stage 8 expected %d runtime bones after append; found %d." % [UAL_CORE_BONE_COUNT + EXPECTED_SECONDARY_BONES, _secondary_bone_count_at_build])

	_proxy_skeleton.force_update_all_bone_transforms()
	secondary_skin = _proxy_skeleton.create_skin_from_rest_transforms()
	if secondary_skin == null:
		push_error("Ilyra Stage 8: failed to create secondary Skin after appending spring bones.")
		return
	if secondary_skin.get_bind_count() != _proxy_skeleton.get_bone_count():
		push_warning("Ilyra Stage 8: secondary skin bind count does not match runtime skeleton bone count.")

	secondary_root = Node3D.new()
	secondary_root.name = "Ilyra_SecondaryMotion_Root"
	_proxy_skeleton.add_child(secondary_root)

	_build_secondary_hair_geometry()
	_build_secondary_cape_geometry()
	_build_spring_simulator()
	_build_secondary_debug_markers()
	_apply_deformation_mode_visibility()

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo:
		if event.keycode == KEY_M:
			_use_secondary_motion = not _use_secondary_motion
			_apply_deformation_mode_visibility()
			_reset_springs()
			_update_hud(_current_label(), _current_clip_name())
			return
		if event.keycode == KEY_N:
			_show_secondary_debug = not _show_secondary_debug
			_update_secondary_debug_visibility()
			_update_hud(_current_label(), _current_clip_name())
			return
		if event.keycode == KEY_F:
			_wind_enabled = not _wind_enabled
			_apply_wind_state()
			_update_hud(_current_label(), _current_clip_name())
			return

	super._unhandled_input(event)
	if event is InputEventKey and event.pressed and not event.echo and event.keycode in [KEY_V, KEY_K, KEY_L]:
		_apply_deformation_mode_visibility()
		_update_hud(_current_label(), _current_clip_name())

func _play_next_clip() -> void:
	if animation_player == null:
		return
	_clip_index = (_clip_index + 1) % SECONDARY_TEST_CLIPS.size()
	var entry: Dictionary = SECONDARY_TEST_CLIPS[_clip_index]
	var clip_name: StringName = entry["name"]
	if not animation_player.has_animation(clip_name):
		push_warning("Ilyra Stage 8: missing animation %s" % clip_name)
		_clip_time_left = 0.05
		return
	animation_player.play(clip_name, 0.18)
	var animation := animation_player.get_animation(clip_name)
	var requested_hold := float(entry["hold"])
	_clip_time_left = requested_hold if requested_hold > 0.0 else max(animation.length + 0.45, 0.9)
	_reset_springs()
	_update_hud(str(entry["label"]), str(clip_name))

func _current_label() -> String:
	if _clip_index < 0 or _clip_index >= SECONDARY_TEST_CLIPS.size():
		return "Ready"
	return str(SECONDARY_TEST_CLIPS[_clip_index]["label"])

func _current_clip_name() -> String:
	if _clip_index < 0 or _clip_index >= SECONDARY_TEST_CLIPS.size():
		return "none"
	return str(SECONDARY_TEST_CLIPS[_clip_index]["name"])

func _collect_stage7_secondary_meshes() -> void:
	stage7_secondary_meshes.clear()
	for mesh in production_meshes:
		if not is_instance_valid(mesh):
			continue
		var mesh_name := str(mesh.name)
		if mesh_name == "ProductionBackHairMass" or mesh_name == "ProductionPaleBlueCape":
			stage7_secondary_meshes.append(mesh)

func _append_secondary_chains() -> void:
	hair_chains.clear()
	cape_chains.clear()

	var hair_specs := [
		{"label": "OuterL", "root": Vector3(-0.125, 0.020, -0.090), "drift": -0.050},
		{"label": "InnerL", "root": Vector3(-0.065, 0.025, -0.110), "drift": -0.025},
		{"label": "Center", "root": Vector3(0.000, 0.030, -0.120), "drift": 0.010},
		{"label": "InnerR", "root": Vector3(0.065, 0.025, -0.110), "drift": 0.030},
		{"label": "OuterR", "root": Vector3(0.125, 0.020, -0.090), "drift": 0.055},
	]
	var head_idx := _proxy_skeleton.find_bone("Head")
	for spec in hair_specs:
		var chain: Array = []
		var previous_parent := head_idx
		for segment in range(HAIR_BONES_PER_CHAIN):
			var bone_name := "IlyraHairSpring_%s_%02d" % [str(spec["label"]), segment]
			var offset: Vector3
			if segment == 0:
				offset = spec["root"]
			else:
				var t := float(segment) / float(HAIR_BONES_PER_CHAIN - 1)
				offset = Vector3(float(spec["drift"]) * t, -0.155 - 0.012 * float(segment), 0.006 + 0.008 * t)
			var bone_idx := _append_secondary_bone(bone_name, previous_parent, offset)
			chain.append(bone_name)
			previous_parent = bone_idx
		hair_chains.append(chain)

	var cape_specs := [
		{"label": "L", "root": Vector3(-0.185, 0.055, -0.155), "drift": -0.018},
		{"label": "C", "root": Vector3(0.000, 0.060, -0.165), "drift": -0.008},
		{"label": "R", "root": Vector3(0.185, 0.055, -0.155), "drift": 0.010},
	]
	var spine_idx := _proxy_skeleton.find_bone("spine_03")
	for spec in cape_specs:
		var chain: Array = []
		var previous_parent := spine_idx
		for segment in range(CAPE_BONES_PER_CHAIN):
			var bone_name := "IlyraCapeSpring_%s_%02d" % [str(spec["label"]), segment]
			var offset: Vector3
			if segment == 0:
				offset = spec["root"]
			else:
				var t := float(segment) / float(CAPE_BONES_PER_CHAIN - 1)
				offset = Vector3(float(spec["drift"]) * t, -0.205 - 0.012 * float(segment), 0.010 + 0.010 * t)
			var bone_idx := _append_secondary_bone(bone_name, previous_parent, offset)
			chain.append(bone_name)
			previous_parent = bone_idx
		cape_chains.append(chain)

func _append_secondary_bone(bone_name: String, parent_idx: int, local_offset: Vector3) -> int:
	var existing := _proxy_skeleton.find_bone(bone_name)
	if existing >= 0:
		return existing
	var bone_idx := _proxy_skeleton.add_bone(bone_name)
	if bone_idx < 0:
		push_error("Ilyra Stage 8: failed to append secondary bone %s." % bone_name)
		return max(parent_idx, 0)
	_proxy_skeleton.set_bone_parent(bone_idx, parent_idx)
	_proxy_skeleton.set_bone_rest(bone_idx, Transform3D(Basis.IDENTITY, local_offset))
	_proxy_skeleton.set_bone_pose(bone_idx, Transform3D.IDENTITY)
	return bone_idx

func _build_secondary_hair_geometry() -> void:
	var widths := [0.052, 0.048, 0.034, 0.010]
	for chain_i in range(hair_chains.size()):
		var chain: Array = hair_chains[chain_i]
		var vertices: Array[Vector3] = []
		var influences: Array[Dictionary] = []
		for row_i in range(chain.size()):
			var bone_name := str(chain[row_i])
			var center := _bone_origin(bone_name)
			var width := widths[min(row_i, widths.size() - 1)]
			vertices.append(center + Vector3(-width, 0.0, 0.0))
			vertices.append(center + Vector3(width, 0.0, 0.0))
			var influence := _weights({bone_name: 1.0})
			influences.append(influence)
			influences.append(influence)
		_add_secondary_weighted_mesh("SpringHairRibbon_%02d" % chain_i, vertices, _strip_indices(chain.size(), 2), influences, _authored_hair, true)

func _build_secondary_cape_geometry() -> void:
	if cape_chains.size() != 3:
		push_error("Ilyra Stage 8: cape secondary geometry expects exactly three spring chains.")
		return
	var rows := CAPE_BONES_PER_CHAIN
	var columns := 9
	var vertices: Array[Vector3] = []
	var influences: Array[Dictionary] = []
	for row_i in range(rows):
		var left_name := str(cape_chains[0][row_i])
		var center_name := str(cape_chains[1][row_i])
		var right_name := str(cape_chains[2][row_i])
		var left := _bone_origin(left_name)
		var center := _bone_origin(center_name)
		var right := _bone_origin(right_name)
		for column in range(columns):
			var u := float(column) / float(columns - 1)
			var position: Vector3
			var named_weights: Dictionary = {}
			if u <= 0.5:
				var local_u := u / 0.5
				position = left.lerp(center, local_u)
				named_weights[left_name] = 1.0 - local_u
				named_weights[center_name] = local_u
			else:
				var local_u := (u - 0.5) / 0.5
				position = center.lerp(right, local_u)
				named_weights[center_name] = 1.0 - local_u
				named_weights[right_name] = local_u
			position.z -= sin(u * PI) * 0.018
			vertices.append(position)
			influences.append(_weights(named_weights))
	_add_secondary_weighted_mesh("SpringPaleBlueCape", vertices, _strip_indices(rows, columns), influences, _pale_blue, true)

func _add_secondary_weighted_mesh(node_name: String, vertices: Array[Vector3], indices: Array[int], influences: Array[Dictionary], material: Material, double_sided: bool) -> MeshInstance3D:
	if vertices.size() != influences.size():
		push_error("Ilyra Stage 8: vertex/influence mismatch for %s." % node_name)
		return null
	var normals := _calculate_normals(vertices, indices)
	var packed_vertices := PackedVector3Array(vertices)
	var packed_normals := PackedVector3Array(normals)
	var packed_indices := PackedInt32Array(indices)
	var packed_bones := PackedInt32Array()
	var packed_weights := PackedFloat32Array()
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
	secondary_root.add_child(mesh_instance)
	mesh_instance.skin = secondary_skin
	mesh_instance.skeleton = mesh_instance.get_path_to(_proxy_skeleton)
	secondary_meshes.append(mesh_instance)
	return mesh_instance

func _build_spring_simulator() -> void:
	spring_simulator = SpringBoneSimulator3D.new()
	spring_simulator.name = "IlyraSecondarySpringSimulator"
	_proxy_skeleton.add_child(spring_simulator)
	spring_simulator.mutable_bone_axes = false
	spring_simulator.set_setting_count(hair_chains.size() + cape_chains.size())

	var setting := 0
	for chain in hair_chains:
		_configure_spring_setting(setting, str(chain[0]), str(chain[chain.size() - 1]), 0.68, 0.20, 0.16, 0.018)
		setting += 1
	for chain in cape_chains:
		_configure_spring_setting(setting, str(chain[0]), str(chain[chain.size() - 1]), 0.44, 0.30, 0.32, 0.026)
		setting += 1

	var head_collision := SpringBoneCollisionSphere3D.new()
	head_collision.name = "HeadCollision"
	head_collision.bone_name = "Head"
	head_collision.position_offset = Vector3(0.0, 0.0, -0.010)
	head_collision.radius = 0.145
	spring_simulator.add_child(head_collision)

	var torso_collision := SpringBoneCollisionCapsule3D.new()
	torso_collision.name = "UpperTorsoCollision"
	torso_collision.bone_name = "spine_03"
	torso_collision.position_offset = Vector3(0.0, -0.165, -0.005)
	torso_collision.radius = 0.145
	torso_collision.height = 0.46
	spring_simulator.add_child(torso_collision)

	var hip_collision := SpringBoneCollisionSphere3D.new()
	hip_collision.name = "HipCollision"
	hip_collision.bone_name = "pelvis"
	hip_collision.position_offset = Vector3(0.0, -0.045, -0.020)
	hip_collision.radius = 0.165
	spring_simulator.add_child(hip_collision)

	for i in range(hair_chains.size() + cape_chains.size()):
		spring_simulator.set_enable_all_child_collisions(i, true)
	_apply_wind_state()

func _configure_spring_setting(index: int, root_name: String, end_name: String, stiffness: float, drag: float, gravity: float, radius: float) -> void:
	spring_simulator.set_root_bone_name(index, root_name)
	spring_simulator.set_end_bone_name(index, end_name)
	spring_simulator.set_stiffness(index, stiffness)
	spring_simulator.set_drag(index, drag)
	spring_simulator.set_gravity(index, gravity)
	spring_simulator.set_gravity_direction(index, Vector3.DOWN)
	spring_simulator.set_radius(index, radius)
	spring_simulator.set_extend_end_bone(index, true)
	spring_simulator.set_end_bone_length(index, 0.10)

func _apply_wind_state() -> void:
	if spring_simulator == null:
		return
	spring_simulator.external_force = Vector3(0.55, 0.0, 0.10) if _wind_enabled else Vector3.ZERO

func _reset_springs() -> void:
	if spring_simulator != null:
		spring_simulator.reset()

func _build_secondary_debug_markers() -> void:
	secondary_debug_root = Node3D.new()
	secondary_debug_root.name = "Stage8_SecondaryBoneDebug"
	_proxy_skeleton.add_child(secondary_debug_root)
	var hair_mat := _material(Color(0.96, 0.78, 0.20), 0.50, 0.0)
	var cape_mat := _material(Color(0.25, 0.78, 0.98), 0.50, 0.0)
	for chain in hair_chains:
		for bone_name in chain:
			_add_secondary_debug_marker(str(bone_name), hair_mat)
	for chain in cape_chains:
		for bone_name in chain:
			_add_secondary_debug_marker(str(bone_name), cape_mat)
	_update_secondary_debug_visibility()

func _add_secondary_debug_marker(bone_name: String, material: Material) -> void:
	var attachment := BoneAttachment3D.new()
	attachment.name = "SecondaryDebug_%s" % bone_name
	attachment.bone_name = bone_name
	_proxy_skeleton.add_child(attachment)
	var marker := MeshInstance3D.new()
	var sphere := SphereMesh.new()
	sphere.radius = 0.012
	sphere.height = 0.024
	marker.mesh = sphere
	marker.material_override = material
	attachment.add_child(marker)
	secondary_debug_attachments.append(attachment)

func _apply_deformation_mode_visibility() -> void:
	# Preserve all Stage 7/6/5 comparison behavior first, then replace only the
	# Stage 7 back-hair mass and cape when spring mode is active.
	super._apply_deformation_mode_visibility()
	var stage8_active := _authored_visible and _use_production_topology and _use_secondary_motion
	if secondary_root != null:
		secondary_root.visible = stage8_active
	if spring_simulator != null:
		spring_simulator.active = stage8_active
	for mesh in stage7_secondary_meshes:
		if is_instance_valid(mesh):
			mesh.visible = _authored_visible and _use_production_topology and not _use_secondary_motion
	_update_secondary_debug_visibility()

func _update_secondary_debug_visibility() -> void:
	var visible_now := _authored_visible and _use_production_topology and _use_secondary_motion and _show_secondary_debug
	for attachment in secondary_debug_attachments:
		if is_instance_valid(attachment):
			attachment.visible = visible_now

func _update_hud(display_name: String, clip_name: String) -> void:
	if info_label == null:
		return
	var character_state := "CHARACTER ON" if _authored_visible else "UAL BODY ONLY"
	var topology_state := "STAGE 7 CONTINUOUS TOPOLOGY" if _use_production_topology else ("STAGE 6 MULTI-BONE" if _use_weighted_deformation else "STAGE 5 RIGID")
	var secondary_state := "SPRING HAIR/CAPE" if _use_secondary_motion and _use_production_topology else "STAGE 7 WEIGHTED HAIR/CAPE"
	var wind_state := "WIND ON" if _wind_enabled else "WIND OFF"
	var debug_state := "SPRING BONES ON" if _show_secondary_debug else "SPRING BONES OFF"
	info_label.text = "Diyse — Ilyra Stage 8 secondary-motion / UAL proof\n%s  [%s]\n%s | %s | %s\n%s | %s | %d UAL core + %d auxiliary spring bones\nSPACE next   P pause   V character/body   L Stage7/Stage6   K Stage6 weighted/rigid\nM spring/weighted hair+cape   F wind   N spring debug   B core debug   Q/E rotate   T turntable   R restart" % [display_name, clip_name, character_state, topology_state, secondary_state, wind_state, debug_state, UAL_CORE_BONE_COUNT, EXPECTED_SECONDARY_BONES]
