extends "res://game/characters/presentation/rig_preview/ilyra_anime_body_ual.gd"

# Modular costume/detail blockout layered onto the reshaped UAL-skinned Ilyra proof.
# Non-canon 3D prototype. The exact approved B00 remains visual authority.

var _detail_visible := true
var _detail_attachments: Array[BoneAttachment3D] = []
var _tabard_pivots: Array[Node3D] = []
var _detail_time := 0.0

var _ivory: StandardMaterial3D
var _pale_blue: StandardMaterial3D
var _deep_blue: StandardMaterial3D
var _silver: StandardMaterial3D
var _leather: StandardMaterial3D
var _gold: StandardMaterial3D
var _skin: StandardMaterial3D
var _jade: StandardMaterial3D

func _apply_proxy_style() -> void:
	super._apply_proxy_style()
	if _proxy_skeleton == null:
		return
	_build_detail_materials()
	_build_modular_details()

func _process(delta: float) -> void:
	super._process(delta)
	if _paused:
		return
	_detail_time += delta
	for i in range(_tabard_pivots.size()):
		var speed := 1.65 if animation_player.current_animation in [&"Walk_Loop", &"Jog_Fwd_Loop", &"Shield_Dash"] else 1.0
		var phase := _detail_time * 2.0 * speed + float(i) * 0.55
		_tabard_pivots[i].rotation.x = deg_to_rad(2.0 + sin(phase) * 1.0)

func _unhandled_input(event: InputEvent) -> void:
	super._unhandled_input(event)
	if event is InputEventKey and event.pressed and not event.echo:
		match event.keycode:
			KEY_V:
				if animation_player == null:
					return
				_detail_visible = not _detail_visible
				for attachment in _detail_attachments:
					attachment.visible = _detail_visible
				_update_hud(_current_label(), str(animation_player.current_animation))
			KEY_Q:
				if actor != null:
					actor.rotate_y(deg_to_rad(15.0))
			KEY_E:
				if actor != null:
					actor.rotate_y(deg_to_rad(-15.0))
			KEY_ESCAPE:
				get_tree().quit()

func _build_detail_materials() -> void:
	_ivory = _material(Color(0.91, 0.91, 0.87), 0.76, 0.02)
	_pale_blue = _material(Color(0.54, 0.76, 0.90), 0.78, 0.0)
	_deep_blue = _material(Color(0.27, 0.43, 0.55), 0.82, 0.0)
	_silver = _material(Color(0.71, 0.76, 0.81), 0.28, 0.64)
	_leather = _material(Color(0.27, 0.15, 0.085), 0.92, 0.0)
	_gold = _material(Color(0.72, 0.60, 0.32), 0.40, 0.48)
	_skin = _material(Color(0.93, 0.79, 0.68), 0.82, 0.0)
	_jade = _material(Color(0.18, 0.88, 0.54), 0.22, 0.06)
	_jade.emission_enabled = true
	_jade.emission = Color(0.06, 0.24, 0.13)
	_jade.emission_energy_multiplier = 0.42

func _build_modular_details() -> void:
	_add_face_read()
	_add_torso_layers()
	_add_waist_layers()
	_add_arm_layers()
	_add_leg_layers()
	_add_cape_mantle()
	_add_extra_hair_locks()

func _add_face_read() -> void:
	var head := _detail_attachment("IlyraFaceDetail", "Head")
	if head == null:
		return
	head.add_child(_sphere("FaceShell", Vector3(0.0, 0.010, 0.012), Vector3(0.123, 0.141, 0.108), _skin))
	for x in [-0.038, 0.038]:
		head.add_child(_sphere("EyeWhite", Vector3(x, 0.035, 0.105), Vector3(0.024, 0.013, 0.009), _ivory))
		head.add_child(_sphere("JadeIris", Vector3(x, 0.035, 0.114), Vector3(0.010, 0.010, 0.006), _jade))

func _add_torso_layers() -> void:
	var chest := _detail_attachment("IlyraTorsoDetail", "spine_03")
	if chest == null:
		return
	chest.add_child(_box("FittedIvoryVest", Vector3(0.0, -0.105, 0.005), Vector3(0.34, 0.36, 0.19), _ivory))
	chest.add_child(_box("PaleBlueCenterPanel", Vector3(0.0, -0.11, 0.104), Vector3(0.075, 0.31, 0.014), _pale_blue))
	chest.add_child(_box("HighCollar", Vector3(0.0, 0.078, 0.015), Vector3(0.22, 0.085, 0.18), _deep_blue))
	chest.add_child(_box("GoldTrimL", Vector3(-0.115, -0.105, 0.108), Vector3(0.012, 0.29, 0.012), _gold))
	chest.add_child(_box("GoldTrimR", Vector3(0.115, -0.105, 0.108), Vector3(0.012, 0.29, 0.012), _gold))
	chest.add_child(_sphere("CapeClasp", Vector3(0.0, 0.025, 0.122), Vector3(0.032, 0.032, 0.016), _silver))
	chest.add_child(_sphere("BluePendant", Vector3(0.0, -0.045, 0.125), Vector3(0.018, 0.028, 0.012), _pale_blue))

func _add_waist_layers() -> void:
	var pelvis := _detail_attachment("IlyraWaistDetail", "pelvis")
	if pelvis == null:
		return
	pelvis.add_child(_box("BeltBuckle", Vector3(0.0, 0.018, 0.104), Vector3(0.065, 0.052, 0.018), _silver))
	pelvis.add_child(_box("LeftUtilityPouch", Vector3(-0.215, -0.050, 0.015), Vector3(0.105, 0.135, 0.085), _leather))
	pelvis.add_child(_box("RightUtilityPouch", Vector3(0.205, -0.070, -0.005), Vector3(0.075, 0.105, 0.070), _leather))
	_add_tabard(pelvis, "FrontTabard", Vector3(0.0, -0.17, 0.095), Vector3(0.16, 0.38, 0.018), _ivory)
	_add_tabard(pelvis, "FrontBlueInset", Vector3(0.0, -0.17, 0.108), Vector3(0.075, 0.32, 0.012), _pale_blue)
	_add_tabard(pelvis, "LeftSkirtPanel", Vector3(-0.145, -0.15, 0.015), Vector3(0.13, 0.31, 0.018), _ivory)
	_add_tabard(pelvis, "RightSkirtPanel", Vector3(0.145, -0.15, 0.015), Vector3(0.13, 0.31, 0.018), _pale_blue)

func _add_tabard(parent: Node3D, node_name: String, position: Vector3, size: Vector3, material: Material) -> void:
	var pivot := Node3D.new()
	pivot.name = node_name + "Pivot"
	pivot.position = position
	parent.add_child(pivot)
	pivot.add_child(_box(node_name, Vector3(0.0, -size.y * 0.48, 0.0), size, material))
	_tabard_pivots.append(pivot)

func _add_arm_layers() -> void:
	for side in ["l", "r"]:
		var forearm := _detail_attachment("IlyraBracer_%s" % side.to_upper(), "lowerarm_%s" % side)
		if forearm != null:
			forearm.add_child(_cylinder("SilverBracer", Vector3(0.0, -0.12, 0.0), 0.050, 0.22, _silver))
			forearm.add_child(_box("LeatherBracerStrap", Vector3(0.0, -0.17, 0.045), Vector3(0.105, 0.035, 0.020), _leather))
		var hand := _detail_attachment("IlyraGlove_%s" % side.to_upper(), "hand_%s" % side)
		if hand != null:
			hand.add_child(_box("FingerlessGlove", Vector3(0.0, -0.025, 0.0), Vector3(0.10, 0.10, 0.075), _leather))

func _add_leg_layers() -> void:
	for side in ["l", "r"]:
		var calf := _detail_attachment("IlyraGreave_%s" % side.to_upper(), "calf_%s" % side)
		if calf != null:
			calf.add_child(_box("SilverGreave", Vector3(0.0, -0.18, 0.025), Vector3(0.115, 0.31, 0.075), _silver))
			calf.add_child(_box("GreaveStrap", Vector3(0.0, -0.24, -0.020), Vector3(0.13, 0.035, 0.085), _leather))
		var foot := _detail_attachment("IlyraBoot_%s" % side.to_upper(), "foot_%s" % side)
		if foot != null:
			foot.add_child(_box("LeatherBoot", Vector3(0.0, -0.03, 0.075), Vector3(0.13, 0.13, 0.26), _leather))

func _add_cape_mantle() -> void:
	var chest := _detail_attachment("IlyraCapeMantle", "spine_03")
	if chest != null:
		chest.add_child(_box("PaleBlueShoulderMantle", Vector3(0.0, 0.015, -0.105), Vector3(0.44, 0.13, 0.045), _pale_blue))

func _add_extra_hair_locks() -> void:
	var head := _detail_attachment("IlyraHairDetail", "Head")
	if head == null:
		return
	var blonde := _material(Color(0.93, 0.79, 0.43), 0.58, 0.0)
	for x in [-0.125, 0.125]:
		var lock := MeshInstance3D.new()
		var mesh := CapsuleMesh.new()
		mesh.radius = 0.026
		mesh.height = 0.36
		lock.mesh = mesh
		lock.material_override = blonde
		lock.position = Vector3(x, -0.15, 0.02)
		lock.rotation_degrees.z = -13.0 if x < 0.0 else 13.0
		head.add_child(lock)

func _detail_attachment(node_name: String, bone_name: String) -> BoneAttachment3D:
	if _proxy_skeleton == null or _proxy_skeleton.find_bone(bone_name) < 0:
		push_warning("Ilyra modular detail: missing bone %s" % bone_name)
		return null
	var attachment := BoneAttachment3D.new()
	attachment.name = node_name
	attachment.bone_name = bone_name
	_proxy_skeleton.add_child(attachment)
	_detail_attachments.append(attachment)
	return attachment

func _box(node_name: String, position: Vector3, size: Vector3, material: Material) -> MeshInstance3D:
	var node := MeshInstance3D.new()
	node.name = node_name
	var mesh := BoxMesh.new()
	mesh.size = size
	node.mesh = mesh
	node.material_override = material
	node.position = position
	return node

func _sphere(node_name: String, position: Vector3, scale_value: Vector3, material: Material) -> MeshInstance3D:
	var node := MeshInstance3D.new()
	node.name = node_name
	var mesh := SphereMesh.new()
	mesh.radius = 1.0
	mesh.height = 2.0
	node.mesh = mesh
	node.material_override = material
	node.position = position
	node.scale = scale_value
	return node

func _cylinder(node_name: String, position: Vector3, radius: float, height: float, material: Material) -> MeshInstance3D:
	var node := MeshInstance3D.new()
	node.name = node_name
	var mesh := CylinderMesh.new()
	mesh.top_radius = radius
	mesh.bottom_radius = radius
	mesh.height = height
	node.mesh = mesh
	node.material_override = material
	node.position = position
	return node

func _current_label() -> String:
	if _clip_index < 0 or _clip_index >= ILYRA_DEMO_CLIPS.size():
		return "Ready"
	return str(ILYRA_DEMO_CLIPS[_clip_index]["label"])

func _update_hud(display_name: String, clip_name: String) -> void:
	if info_label == null:
		return
	var details := "DETAIL LAYERS ON" if _detail_visible else "DETAIL LAYERS OFF"
	info_label.text = "Diyse — Ilyra modular UAL blockout\n%s  [%s]\n%s | reshaped UAL body + B00-guided construction\nSPACE next   P pause   V detail compare   Q/E rotate   R restart   ESC quit" % [display_name, clip_name, details]
