extends "res://game/characters/presentation/rig_preview/ilyra_deformation_aware.gd"

# Stage 7: broader production-topology surfaces on the unchanged UAL skeleton.
# Still a deformation/topology proof; Ilyra's approved B00 remains appearance authority.

const PRODUCTION_TEST_CLIPS := [
	{"name": &"A_TPose", "hold": 2.2, "label": "Topology / T-pose"},
	{"name": &"Idle_Loop", "hold": 2.2, "label": "Neutral silhouette"},
	{"name": &"Walk_Loop", "hold": 2.3, "label": "Walk / shoulder + hip blend"},
	{"name": &"Jog_Fwd_Loop", "hold": 2.1, "label": "Jog / continuous shell"},
	{"name": &"Crouch_Fwd_Loop", "hold": 2.1, "label": "Crouch / hip compression"},
	{"name": &"ClimbUp_1m", "hold": 0.0, "label": "Climb / shoulder stress"},
	{"name": &"Roll", "hold": 0.0, "label": "Roll / whole-shell stress"},
	{"name": &"Shield_Dash", "hold": 0.0, "label": "Shield advance / cape root"},
	{"name": &"Spell_Simple_Shoot", "hold": 0.0, "label": "Warden cast / clavicle blend"},
	{"name": &"Hit_Knockback", "hold": 0.0, "label": "Knockback / recovery"},
]

var stage6_meshes: Array[MeshInstance3D] = []
var production_meshes: Array[MeshInstance3D] = []
var _debug_attachments: Array[BoneAttachment3D] = []
var _use_production_topology := true
var _show_bone_debug := false

func _apply_proxy_style() -> void:
	super._apply_proxy_style()
	if _proxy_skeleton == null or deformation_skin == null:
		return
	stage6_meshes.assign(deformation_meshes)
	_build_production_torso()
	_build_production_sleeves()
	_build_production_hip_drape()
	_build_production_hair()
	_build_production_cape()
	_build_debug_markers()
	_apply_deformation_mode_visibility()

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo:
		if event.keycode == KEY_L:
			_use_production_topology = not _use_production_topology
			_apply_deformation_mode_visibility()
			_update_hud(_current_label(), _current_clip_name())
			return
		if event.keycode == KEY_B:
			_show_bone_debug = not _show_bone_debug
			_update_debug_visibility()
			_update_hud(_current_label(), _current_clip_name())
			return
	super._unhandled_input(event)
	if event is InputEventKey and event.pressed and not event.echo and event.keycode in [KEY_V, KEY_K]:
		_apply_deformation_mode_visibility()
		_update_hud(_current_label(), _current_clip_name())

func _play_next_clip() -> void:
	if animation_player == null:
		return
	_clip_index = (_clip_index + 1) % PRODUCTION_TEST_CLIPS.size()
	var entry: Dictionary = PRODUCTION_TEST_CLIPS[_clip_index]
	var clip_name: StringName = entry["name"]
	if not animation_player.has_animation(clip_name):
		push_warning("Ilyra Stage 7: missing animation %s" % clip_name)
		_clip_time_left = 0.05
		return
	animation_player.play(clip_name, 0.18)
	var animation := animation_player.get_animation(clip_name)
	var hold := float(entry["hold"])
	_clip_time_left = hold if hold > 0.0 else max(animation.length + 0.35, 0.8)
	_update_hud(str(entry["label"]), str(clip_name))

func _current_label() -> String:
	return "Ready" if _clip_index < 0 or _clip_index >= PRODUCTION_TEST_CLIPS.size() else str(PRODUCTION_TEST_CLIPS[_clip_index]["label"])

func _current_clip_name() -> String:
	return "none" if _clip_index < 0 or _clip_index >= PRODUCTION_TEST_CLIPS.size() else str(PRODUCTION_TEST_CLIPS[_clip_index]["name"])

func _apply_deformation_mode_visibility() -> void:
	if _use_production_topology:
		if deformation_root != null:
			deformation_root.visible = _authored_visible
		for mesh in stage6_meshes:
			if is_instance_valid(mesh): mesh.visible = false
		for mesh in production_meshes:
			if is_instance_valid(mesh): mesh.visible = _authored_visible
		for node in rigid_deformation_nodes:
			if is_instance_valid(node): node.visible = false
	else:
		for mesh in production_meshes:
			if is_instance_valid(mesh): mesh.visible = false
		super._apply_deformation_mode_visibility()
	_update_debug_visibility()

func _add_stage7_mesh(name: String, vertices: Array[Vector3], indices: Array[int], influences: Array[Dictionary], material: Material, double_sided := true) -> void:
	var mesh := _add_weighted_mesh(name, vertices, indices, influences, material, double_sided)
	if mesh != null:
		production_meshes.append(mesh)

func _build_production_torso() -> void:
	var rows := [
		{"y": _bone_origin("spine_03").y + 0.120, "rx": 0.176, "rz": 0.088, "zone": 0.00},
		{"y": _bone_origin("spine_03").y + 0.045, "rx": 0.184, "rz": 0.091, "zone": 0.10},
		{"y": _bone_origin("spine_03").y - 0.040, "rx": 0.176, "rz": 0.089, "zone": 0.22},
		{"y": _bone_origin("spine_02").y - 0.015, "rx": 0.161, "rz": 0.082, "zone": 0.38},
		{"y": _bone_origin("spine_01").y - 0.015, "rx": 0.139, "rz": 0.075, "zone": 0.56},
		{"y": _bone_origin("pelvis").y + 0.105, "rx": 0.132, "rz": 0.074, "zone": 0.70},
		{"y": _bone_origin("pelvis").y + 0.045, "rx": 0.151, "rz": 0.079, "zone": 0.84},
		{"y": _bone_origin("pelvis").y - 0.010, "rx": 0.168, "rz": 0.083, "zone": 1.00},
	]
	var vertices: Array[Vector3] = []
	var influences: Array[Dictionary] = []
	var segments := 20
	for row in rows:
		for i in range(segments):
			var angle := TAU * float(i) / float(segments)
			var x := cos(angle) * float(row["rx"])
			vertices.append(Vector3(x, float(row["y"]), sin(angle) * float(row["rz"]) + 0.020))
			influences.append(_torso_weights(float(row["zone"]), x, float(row["rx"])))
	_add_stage7_mesh("ProductionWardenTorsoShell", vertices, _closed_indices(rows.size(), segments), influences, _ivory, false)
	var panel_v: Array[Vector3] = []
	var panel_w: Array[Dictionary] = []
	for row in rows:
		var zone := float(row["zone"])
		var width := lerp(0.040, 0.030, zone)
		for x in [-width, width]:
			panel_v.append(Vector3(x, float(row["y"]), float(row["rz"]) + 0.027))
			panel_w.append(_torso_weights(zone, x, float(row["rx"])))
	_add_stage7_mesh("ProductionBlueCenterPanel", panel_v, _strip_indices(rows.size(), 2), panel_w, _pale_blue)

func _torso_weights(zone: float, x: float, rx: float) -> Dictionary:
	var named: Dictionary = {}
	if zone < 0.18:
		named = {"spine_03": 0.72, "spine_02": 0.16}
		var side := clamp((abs(x) / max(rx, 0.001) - 0.45) / 0.55, 0.0, 1.0)
		if side > 0.0:
			var clavicle := "clavicle_l" if x > 0.0 else "clavicle_r"
			var arm := "upperarm_l" if x > 0.0 else "upperarm_r"
			named[clavicle] = 0.10 + 0.16 * side
			named[arm] = 0.02 + 0.08 * side
			named["spine_03"] = max(0.40, 0.72 - 0.20 * side)
	elif zone < 0.42:
		named = {"spine_03": 0.58, "spine_02": 0.42}
	elif zone < 0.62:
		named = {"spine_02": 0.55, "spine_01": 0.45}
	elif zone < 0.82:
		named = {"spine_01": 0.50, "pelvis": 0.50}
	else:
		var thigh := "thigh_l" if x > 0.0 else "thigh_r"
		named = {"pelvis": 0.74, "spine_01": 0.10}
		named[thigh] = 0.16 * clamp(abs(x) / max(rx, 0.001), 0.0, 1.0)
	return _weights(named)

func _build_production_sleeves() -> void:
	for side in ["l", "r"]:
		var clavicle := "clavicle_%s" % side
		var upper := "upperarm_%s" % side
		var lower := "lowerarm_%s" % side
		var start := _bone_origin(upper)
		var finish := _bone_origin(lower)
		var axis := (finish - start).normalized()
		var up := Vector3.UP
		var across := axis.cross(up).normalized()
		up = across.cross(axis).normalized()
		var vertices: Array[Vector3] = []
		var influences: Array[Dictionary] = []
		var rings := 6
		var segments := 10
		for r in range(rings):
			var t := float(r) / float(rings - 1)
			var center := start.lerp(finish, t)
			var radius := lerp(0.071, 0.056, t)
			var named: Dictionary = {}
			if t < 0.20:
				named[clavicle] = 0.22 * (1.0 - t / 0.20)
				named[upper] = 0.78 + 0.22 * (t / 0.20)
			elif t < 0.72:
				named[upper] = 1.0
			else:
				var et := (t - 0.72) / 0.28
				named[upper] = 1.0 - 0.42 * et
				named[lower] = 0.42 * et
			var influence := _weights(named)
			for s in range(segments):
				var angle := TAU * float(s) / float(segments)
				vertices.append(center + up * cos(angle) * radius + across * sin(angle) * radius)
				influences.append(influence)
		_add_stage7_mesh("ProductionUpperSleeve_%s" % side.to_upper(), vertices, _closed_indices(rings, segments), influences, _ivory, false)

func _build_production_hip_drape() -> void:
	var pelvis := _bone_origin("pelvis")
	var rows := 5
	var columns := 13
	var vertices: Array[Vector3] = []
	var influences: Array[Dictionary] = []
	for r in range(rows):
		var t := float(r) / float(rows - 1)
		var rx := lerp(0.176, 0.208, t)
		var rz := lerp(0.090, 0.108, t)
		for c in range(columns):
			var u := float(c) / float(columns - 1)
			var angle := lerp(0.04 * PI, 0.96 * PI, u)
			var x := cos(angle) * rx
			vertices.append(Vector3(x, pelvis.y + lerp(0.035, -0.315, t), sin(angle) * rz + 0.018))
			var thigh := "thigh_l" if x > 0.0 else "thigh_r"
			var tw := t * lerp(0.36, 0.18, 1.0 - clamp(abs(x) / rx, 0.0, 1.0))
			var named: Dictionary = {"pelvis": 1.0 - tw}
			named[thigh] = tw
			influences.append(_weights(named))
	_add_stage7_mesh("ProductionHipDrape", vertices, _strip_indices(rows, columns), influences, _pale_blue)
	var tab_v: Array[Vector3] = []
	var tab_w: Array[Dictionary] = []
	for r in range(6):
		var t := float(r) / 5.0
		var half := lerp(0.132, 0.062, t)
		for c in range(5):
			var x := lerp(-half, half, float(c) / 4.0)
			tab_v.append(Vector3(x, pelvis.y + lerp(0.020, -0.470, t), 0.124))
			tab_w.append(_weights({"pelvis": max(0.14, 1.0 - t * 0.86), "thigh_l": t * 0.43, "thigh_r": t * 0.43}))
	_add_stage7_mesh("ProductionFrontTabard", tab_v, _strip_indices(6, 5), tab_w, _ivory)

func _build_production_hair() -> void:
	var head := _bone_origin("Head")
	var s3 := _bone_origin("spine_03")
	var s2 := _bone_origin("spine_02")
	var rows := [
		{"y": head.y + 0.120, "half": 0.095, "z": -0.070, "w": _weights({"Head": 1.0})},
		{"y": head.y + 0.035, "half": 0.142, "z": -0.105, "w": _weights({"Head": 0.92, "neck_01": 0.08})},
		{"y": head.y - 0.095, "half": 0.158, "z": -0.120, "w": _weights({"Head": 0.66, "neck_01": 0.34})},
		{"y": head.y - 0.235, "half": 0.172, "z": -0.125, "w": _weights({"Head": 0.24, "neck_01": 0.52, "spine_03": 0.24})},
		{"y": s3.y - 0.135, "half": 0.164, "z": -0.118, "w": _weights({"neck_01": 0.24, "spine_03": 0.66, "spine_02": 0.10})},
		{"y": s2.y - 0.135, "half": 0.128, "z": -0.103, "w": _weights({"spine_03": 0.46, "spine_02": 0.54})},
		{"y": s2.y - 0.285, "half": 0.064, "z": -0.080, "w": _weights({"spine_02": 0.86, "spine_01": 0.14})},
	]
	var vertices: Array[Vector3] = []
	var influences: Array[Dictionary] = []
	for r in range(rows.size()):
		var row: Dictionary = rows[r]
		for c in range(9):
			var u := float(c) / 8.0
			var x := lerp(-float(row["half"]), float(row["half"]), u) + (u - 0.5) * 0.030 * float(r) / 6.0
			vertices.append(Vector3(x, float(row["y"]), float(row["z"]) - sin(u * PI) * 0.018))
			influences.append(row["w"])
	_add_stage7_mesh("ProductionBackHairMass", vertices, _strip_indices(rows.size(), 9), influences, _authored_hair)

func _build_production_cape() -> void:
	var s3 := _bone_origin("spine_03")
	var s2 := _bone_origin("spine_02")
	var s1 := _bone_origin("spine_01")
	var pelvis := _bone_origin("pelvis")
	var rows := [
		{"y": s3.y + 0.095, "half": 0.238, "x": 0.000, "z": -0.150, "zone": 0.00},
		{"y": s3.y + 0.005, "half": 0.246, "x": 0.000, "z": -0.158, "zone": 0.14},
		{"y": s2.y - 0.035, "half": 0.240, "x": -0.004, "z": -0.157, "zone": 0.30},
		{"y": s1.y - 0.065, "half": 0.226, "x": -0.012, "z": -0.150, "zone": 0.48},
		{"y": pelvis.y - 0.145, "half": 0.205, "x": -0.025, "z": -0.137, "zone": 0.66},
		{"y": pelvis.y - 0.405, "half": 0.164, "x": -0.050, "z": -0.112, "zone": 0.84},
		{"y": pelvis.y - 0.620, "half": 0.085, "x": -0.090, "z": -0.080, "zone": 1.00},
	]
	var vertices: Array[Vector3] = []
	var influences: Array[Dictionary] = []
	for row in rows:
		for c in range(9):
			var u := float(c) / 8.0
			var x := float(row["x"]) + lerp(-float(row["half"]), float(row["half"]), u)
			vertices.append(Vector3(x, float(row["y"]), float(row["z"]) - sin(u * PI) * 0.022))
			influences.append(_cape_weights(float(row["zone"]), x, float(row["half"])))
	_add_stage7_mesh("ProductionPaleBlueCape", vertices, _strip_indices(rows.size(), 9), influences, _pale_blue)

func _cape_weights(zone: float, x: float, half: float) -> Dictionary:
	if zone < 0.18:
		var side := clamp(abs(x) / max(half, 0.001), 0.0, 1.0)
		var clavicle := "clavicle_l" if x > 0.0 else "clavicle_r"
		var named: Dictionary = {"spine_03": 0.78 - 0.24 * side, "spine_02": 0.12}
		named[clavicle] = 0.10 + 0.24 * side
		return _weights(named)
	if zone < 0.38: return _weights({"spine_03": 0.54, "spine_02": 0.46})
	if zone < 0.58: return _weights({"spine_02": 0.48, "spine_01": 0.42, "pelvis": 0.10})
	if zone < 0.80: return _weights({"spine_01": 0.38, "pelvis": 0.62})
	return _weights({"pelvis": 1.0})

func _closed_indices(rows: int, columns: int) -> Array[int]:
	var indices: Array[int] = []
	for r in range(rows - 1):
		for c in range(columns):
			var n := (c + 1) % columns
			var a := r * columns + c
			var b := r * columns + n
			var d := (r + 1) * columns + c
			var e := (r + 1) * columns + n
			indices.append_array([a, b, e, a, e, d])
	return indices

func _build_debug_markers() -> void:
	var mat := _material(Color(0.96, 0.26, 0.22), 0.55, 0.0)
	for bone_name in ["clavicle_l", "clavicle_r", "spine_03", "spine_01", "pelvis", "thigh_l", "thigh_r"]:
		var a := BoneAttachment3D.new()
		a.name = "Stage7Debug_%s" % bone_name
		a.bone_name = bone_name
		_proxy_skeleton.add_child(a)
		var marker := MeshInstance3D.new()
		var sphere := SphereMesh.new()
		sphere.radius = 0.020
		sphere.height = 0.040
		marker.mesh = sphere
		marker.material_override = mat
		a.add_child(marker)
		_debug_attachments.append(a)
	_update_debug_visibility()

func _update_debug_visibility() -> void:
	for a in _debug_attachments:
		if is_instance_valid(a): a.visible = _authored_visible and _show_bone_debug

func _update_hud(display_name: String, clip_name: String) -> void:
	if info_label == null:
		return
	var state := "STAGE 7 CONTINUOUS TOPOLOGY" if _use_production_topology else ("STAGE 6 MULTI-BONE" if _use_weighted_deformation else "STAGE 5 RIGID")
	info_label.text = "Diyse — Ilyra Stage 7 production-topology / UAL proof\n%s  [%s]\n%s | %s | B00 remains visual authority\nSPACE next   P pause   V character/body   L Stage7/Stage6   K Stage6 weighted/rigid   B bones   Q/E rotate   T turntable   R restart" % [display_name, clip_name, state, "BONES ON" if _show_bone_debug else "BONES OFF"]