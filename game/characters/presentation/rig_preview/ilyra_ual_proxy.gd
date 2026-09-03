extends "res://game/characters/presentation/rig_preview/ual_rig_preview.gd"

# Motion-only Ilyra proxy: real UAL female skeleton + abstract Ilyra palette/silhouette cues.
# This is not her final 3D model; her locked B00 image remains the appearance authority.

var _proxy_skeleton: Skeleton3D
var _cape_panels: Array[Node3D] = []
var _hair_strands: Array[Node3D] = []
var _proxy_time := 0.0

func _ready() -> void:
	super._ready()
	_proxy_skeleton = _find_skeleton(actor)
	_apply_proxy_style()

func _process(delta: float) -> void:
	super._process(delta)
	if _paused:
		return
	_proxy_time += delta
	_update_secondary_motion()

func _find_skeleton(node: Node) -> Skeleton3D:
	if node is Skeleton3D:
		return node as Skeleton3D
	for child in node.get_children():
		var found := _find_skeleton(child)
		if found != null:
			return found
	return null

func _apply_proxy_style() -> void:
	var body := _material(Color(0.78, 0.86, 0.93), 0.72, 0.0)
	var silver := _material(Color(0.63, 0.68, 0.74), 0.28, 0.52)
	_apply_surface_materials(actor, body, silver)
	if _proxy_skeleton == null:
		push_warning("Ilyra proxy: no Skeleton3D found.")
		return
	_add_hair()
	_add_cape()
	_add_utility_belt()

func _apply_surface_materials(node: Node, body: Material, silver: Material) -> void:
	if node is MeshInstance3D:
		var mesh_instance := node as MeshInstance3D
		if mesh_instance.mesh != null:
			for surface_index in range(mesh_instance.mesh.get_surface_count()):
				mesh_instance.set_surface_override_material(surface_index, body if surface_index == 0 else silver)
	for child in node.get_children():
		_apply_surface_materials(child, body, silver)

func _add_hair() -> void:
	var blonde := _material(Color(0.93, 0.78, 0.41), 0.58, 0.02)
	var attach := _bone_attachment("IlyraHair", "Head")
	if attach == null:
		return
	var cap := MeshInstance3D.new()
	var sphere := SphereMesh.new()
	sphere.radius = 0.13
	sphere.height = 0.26
	cap.mesh = sphere
	cap.material_override = blonde
	cap.position = Vector3(0.0, 0.035, -0.018)
	cap.scale = Vector3(1.02, 1.08, 0.88)
	attach.add_child(cap)
	for x in [-0.075, 0.0, 0.075]:
		var pivot := Node3D.new()
		pivot.position = Vector3(x, -0.10, -0.075)
		attach.add_child(pivot)
		var strand := MeshInstance3D.new()
		var capsule := CapsuleMesh.new()
		capsule.radius = 0.037
		capsule.height = 0.42
		strand.mesh = capsule
		strand.material_override = blonde
		strand.position = Vector3(0.0, -0.16, 0.0)
		pivot.add_child(strand)
		_hair_strands.append(pivot)

func _add_cape() -> void:
	var blue := _material(Color(0.50, 0.73, 0.88), 0.80, 0.0)
	var attach := _bone_attachment("IlyraCape", "spine_03")
	if attach == null:
		return
	var widths := [0.40, 0.36, 0.31]
	var heights := [0.31, 0.33, 0.35]
	var ys := [-0.17, -0.44, -0.72]
	for i in range(3):
		var pivot := Node3D.new()
		pivot.position = Vector3(0.0, ys[i], -0.105 - float(i) * 0.012)
		attach.add_child(pivot)
		var panel := MeshInstance3D.new()
		var box := BoxMesh.new()
		box.size = Vector3(widths[i], heights[i], 0.018)
		panel.mesh = box
		panel.material_override = blue
		panel.position = Vector3(0.0, -heights[i] * 0.48, 0.0)
		pivot.add_child(panel)
		_cape_panels.append(pivot)

func _add_utility_belt() -> void:
	var leather := _material(Color(0.24, 0.13, 0.075), 0.92, 0.0)
	var attach := _bone_attachment("IlyraUtility", "pelvis")
	if attach == null:
		return
	var belt := MeshInstance3D.new()
	var belt_mesh := BoxMesh.new()
	belt_mesh.size = Vector3(0.34, 0.045, 0.17)
	belt.mesh = belt_mesh
	belt.material_override = leather
	belt.position = Vector3(0.0, 0.02, 0.0)
	attach.add_child(belt)
	for x in [-0.19, 0.19]:
		var pouch := MeshInstance3D.new()
		var pouch_mesh := BoxMesh.new()
		pouch_mesh.size = Vector3(0.085, 0.11, 0.075)
		pouch.mesh = pouch_mesh
		pouch.material_override = leather
		pouch.position = Vector3(x, -0.055, 0.0)
		attach.add_child(pouch)

func _bone_attachment(node_name: String, bone_name: String) -> BoneAttachment3D:
	if _proxy_skeleton.find_bone(bone_name) < 0:
		push_warning("Ilyra proxy: missing bone %s" % bone_name)
		return null
	var attachment := BoneAttachment3D.new()
	attachment.name = node_name
	attachment.bone_name = bone_name
	_proxy_skeleton.add_child(attachment)
	return attachment

func _update_secondary_motion() -> void:
	var speed := 1.65 if animation_player.current_animation in [&"Walk_Loop", &"Jog_Fwd_Loop"] else 1.0
	for i in range(_cape_panels.size()):
		var phase := _proxy_time * (2.0 + 0.22 * i) * speed + float(i) * 0.55
		_cape_panels[i].rotation.x = deg_to_rad(7.0 + sin(phase) * (2.2 + i * 1.1))
		_cape_panels[i].rotation.z = deg_to_rad(sin(phase * 0.71) * (0.7 + i * 0.35))
	for i in range(_hair_strands.size()):
		var phase := _proxy_time * 2.35 * speed + float(i) * 0.9
		_hair_strands[i].rotation.x = deg_to_rad(4.0 + sin(phase) * 2.2)
		_hair_strands[i].rotation.z = deg_to_rad(sin(phase * 0.82) * 1.4)

func _material(color: Color, roughness: float, metallic: float) -> StandardMaterial3D:
	var material := StandardMaterial3D.new()
	material.albedo_color = color
	material.roughness = roughness
	material.metallic = metallic
	return material

func _update_hud(display_name: String, clip_name: String) -> void:
	if info_label == null:
		return
	info_label.text = "Diyse — Ilyra UAL motion proxy\n%s  [%s]\nUAL mannequin + Ilyra palette/silhouette cues only\nSPACE next   P pause   R restart   ESC quit" % [display_name, clip_name]
