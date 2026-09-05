extends "res://game/characters/presentation/rig_preview/ual_rig_preview.gd"

# First live preview of the actual Ilyra replacement shell rather than the older
# mannequin/proxy visual construction. Binary GLB is generated externally and copied to
# asset_sources/animation/ual/. Approved cleaned B00 remains exact visual authority.

const CHARACTER_PATH := "res://asset_sources/animation/ual/Ilyra_ProductionMesh_v06_UAL_SpringReady.glb"

const STRESS_CLIPS := [
	{"name": &"A_TPose", "hold": 2.0, "label": "Rest / spring rig"},
	{"name": &"Walk_Loop", "hold": 2.4, "label": "Walk"},
	{"name": &"Jog_Fwd_Loop", "hold": 2.2, "label": "Jog"},
	{"name": &"Sprint_Loop", "hold": 2.0, "label": "Sprint"},
	{"name": &"Crouch_Fwd_Loop", "hold": 2.2, "label": "Crouch"},
	{"name": &"Jump_Start", "hold": 0.0, "label": "Jump start"},
	{"name": &"Jump_Land", "hold": 0.0, "label": "Jump land"},
	{"name": &"Roll", "hold": 0.0, "label": "Roll"},
	{"name": &"Shield_Dash", "hold": 0.0, "label": "Shield dash"},
	{"name": &"Spell_Simple_Shoot", "hold": 0.0, "label": "Warden cast"},
	{"name": &"Hit_Knockback", "hold": 0.0, "label": "Knockback"},
]

var skeleton: Skeleton3D
var spring_simulator: SpringBoneSimulator3D
var _springs_enabled := true
var _wind_enabled := false
var _spring_debug_enabled := false
var _turntable := false
var _spring_debug_attachments: Array[BoneAttachment3D] = []

func _missing_assets() -> Array[String]:
	var missing: Array[String] = []
	for path in [CHARACTER_PATH, UAL1_PATH, UAL2_PATH]:
		if not ResourceLoader.exists(path):
			missing.append(path)
	return missing

func _spawn_actor() -> void:
	var packed := load(CHARACTER_PATH) as PackedScene
	actor = packed.instantiate() as Node3D
	actor.name = "Ilyra_ProductionMesh_v06"
	add_child(actor)
	animation_player = AnimationPlayer.new()
	animation_player.name = "UALAnimationPlayer"
	actor.add_child(animation_player)
	animation_player.root_node = NodePath("..")
	skeleton = _find_skeleton(actor)
	if skeleton == null:
		push_error("Ilyra v0.6 preview: Skeleton3D not found.")
		return
	if skeleton.get_bone_count() != 100:
		push_warning("Ilyra v0.6 expected 100 runtime bones; found %d." % skeleton.get_bone_count())
	_build_spring_simulator()
	_build_spring_debug()

func _process(delta: float) -> void:
	super._process(delta)
	if _turntable and actor != null and not _paused:
		actor.rotate_y(deg_to_rad(18.0 * delta))

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo:
		match event.keycode:
			KEY_M:
				_springs_enabled = not _springs_enabled
				_apply_spring_state()
				_update_hud()
				return
			KEY_F:
				_wind_enabled = not _wind_enabled
				_apply_wind_state()
				_update_hud()
				return
			KEY_N:
				_spring_debug_enabled = not _spring_debug_enabled
				_update_spring_debug_visibility()
				_update_hud()
				return
			KEY_Q:
				if actor != null: actor.rotate_y(deg_to_rad(15.0))
				return
			KEY_E:
				if actor != null: actor.rotate_y(deg_to_rad(-15.0))
				return
			KEY_T:
				_turntable = not _turntable
				_update_hud()
				return
			KEY_ESCAPE:
				get_tree().quit()
				return
	super._unhandled_input(event)

func _find_skeleton(node: Node) -> Skeleton3D:
	if node is Skeleton3D:
		return node as Skeleton3D
	for child in node.get_children():
		var found := _find_skeleton(child)
		if found != null:
			return found
	return null

func _play_next_clip() -> void:
	if animation_player == null:
		return
	_clip_index = (_clip_index + 1) % STRESS_CLIPS.size()
	var entry: Dictionary = STRESS_CLIPS[_clip_index]
	var clip_name: StringName = entry["name"]
	if not animation_player.has_animation(clip_name):
		push_warning("Ilyra v0.6 preview: missing UAL clip %s." % clip_name)
		_clip_time_left = 0.05
		return
	if spring_simulator != null:
		spring_simulator.reset()
	animation_player.play(clip_name, 0.18)
	var animation := animation_player.get_animation(clip_name)
	var hold := float(entry["hold"])
	_clip_time_left = hold if hold > 0.0 else max(animation.length + 0.35, 0.8)
	_update_hud()

func _build_spring_simulator() -> void:
	spring_simulator = SpringBoneSimulator3D.new()
	spring_simulator.name = "IlyraProductionSpringSimulator"
	skeleton.add_child(spring_simulator)
	spring_simulator.mutable_bone_axes = false
	spring_simulator.set_setting_count(8)
	var setting := 0
	for i in range(5):
		_configure_spring(setting, "IlyraHairSpring_%d_0" % i, "IlyraHairSpring_%d_3" % i, 0.68, 0.20, 0.16, 0.018)
		setting += 1
	for i in range(3):
		_configure_spring(setting, "IlyraCapeSpring_%d_0" % i, "IlyraCapeSpring_%d_4" % i, 0.44, 0.30, 0.32, 0.026)
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
	for i in range(8):
		spring_simulator.set_enable_all_child_collisions(i, true)
	_apply_spring_state()
	_apply_wind_state()

func _configure_spring(index: int, root_name: String, end_name: String, stiffness: float, drag: float, gravity: float, radius: float) -> void:
	if skeleton.find_bone(root_name) < 0 or skeleton.find_bone(end_name) < 0:
		push_error("Ilyra v0.6 missing spring chain %s -> %s." % [root_name, end_name])
		return
	spring_simulator.set_root_bone_name(index, root_name)
	spring_simulator.set_end_bone_name(index, end_name)
	spring_simulator.set_stiffness(index, stiffness)
	spring_simulator.set_drag(index, drag)
	spring_simulator.set_gravity(index, gravity)
	spring_simulator.set_gravity_direction(index, Vector3.DOWN)
	spring_simulator.set_radius(index, radius)
	spring_simulator.set_extend_end_bone(index, true)
	spring_simulator.set_end_bone_length(index, 0.10)

func _apply_spring_state() -> void:
	if spring_simulator == null:
		return
	spring_simulator.active = _springs_enabled
	if not _springs_enabled:
		spring_simulator.reset()

func _apply_wind_state() -> void:
	if spring_simulator == null:
		return
	spring_simulator.external_force = Vector3(0.55, 0.0, 0.10) if _wind_enabled else Vector3.ZERO

func _build_spring_debug() -> void:
	var hair_mat := _debug_material(Color(0.96, 0.78, 0.20))
	var cape_mat := _debug_material(Color(0.25, 0.78, 0.98))
	for i in range(5):
		for k in range(4):
			_add_spring_debug_marker("IlyraHairSpring_%d_%d" % [i, k], hair_mat)
	for i in range(3):
		for k in range(5):
			_add_spring_debug_marker("IlyraCapeSpring_%d_%d" % [i, k], cape_mat)
	_update_spring_debug_visibility()

func _add_spring_debug_marker(bone_name: String, material: Material) -> void:
	if skeleton.find_bone(bone_name) < 0:
		return
	var attachment := BoneAttachment3D.new()
	attachment.bone_name = bone_name
	skeleton.add_child(attachment)
	var marker := MeshInstance3D.new()
	var sphere := SphereMesh.new()
	sphere.radius = 0.012
	sphere.height = 0.024
	marker.mesh = sphere
	marker.material_override = material
	attachment.add_child(marker)
	_spring_debug_attachments.append(attachment)

func _update_spring_debug_visibility() -> void:
	for attachment in _spring_debug_attachments:
		attachment.visible = _spring_debug_enabled

func _debug_material(color: Color) -> StandardMaterial3D:
	var material := StandardMaterial3D.new()
	material.albedo_color = color
	material.roughness = 0.55
	return material

func _update_hud() -> void:
	if info_label == null:
		return
	var label := "Ready"
	var clip := "none"
	if _clip_index >= 0 and _clip_index < STRESS_CLIPS.size():
		label = str(STRESS_CLIPS[_clip_index]["label"])
		clip = str(STRESS_CLIPS[_clip_index]["name"])
	info_label.text = "Diyse — Ilyra Production Mesh v0.6 / UAL live deformation proof\n%s  [%s]\nACTUAL replacement shell | 65 UAL core + 35 spring bones | %s | %s\nSPACE next   P pause   M springs   F wind   N spring bones   Q/E rotate   T turntable   R restart   ESC quit" % [label, clip, "SPRINGS ON" if _springs_enabled else "SPRINGS OFF", "WIND ON" if _wind_enabled else "WIND OFF"]
