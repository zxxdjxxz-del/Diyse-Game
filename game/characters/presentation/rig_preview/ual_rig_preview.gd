extends Node3D

const MANNEQUIN_PATH := "res://asset_sources/animation/ual/Mannequin_F.glb"
const UAL1_PATH := "res://asset_sources/animation/ual/UAL1_Standard.glb"
const UAL2_PATH := "res://asset_sources/animation/ual/UAL2_Standard.glb"

const DEMO_CLIPS := [
	{"name": &"Idle_Loop", "hold": 2.7, "label": "Idle"},
	{"name": &"Walk_Loop", "hold": 2.4, "label": "Walk"},
	{"name": &"Jog_Fwd_Loop", "hold": 2.2, "label": "Jog"},
	{"name": &"Sword_Idle", "hold": 2.0, "label": "Sword idle"},
	{"name": &"Sword_Regular_Combo", "hold": 0.0, "label": "Sword regular combo"},
	{"name": &"Sword_Block", "hold": 0.0, "label": "Sword block"},
	{"name": &"Hit_Chest", "hold": 0.0, "label": "Hit reaction"},
	{"name": &"Spell_Simple_Shoot", "hold": 0.0, "label": "Simple spell"},
]

var actor: Node3D
var animation_player: AnimationPlayer
var info_label: Label
var _clip_index := -1
var _clip_time_left := 0.0
var _paused := false

func _ready() -> void:
	_setup_world()
	_setup_hud()
	var missing := _missing_assets()
	if not missing.is_empty():
		info_label.text = "UAL rig preview is ready.\nMissing GLBs:\n" + "\n".join(missing)
		push_warning("UAL rig preview missing assets: %s" % missing)
		return
	_spawn_actor()
	_build_animation_library()
	_play_next_clip()

func _process(delta: float) -> void:
	if animation_player == null or _paused:
		return
	_clip_time_left -= delta
	if _clip_time_left <= 0.0:
		_play_next_clip()

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo and animation_player != null:
		match event.keycode:
			KEY_SPACE:
				_play_next_clip()
			KEY_P:
				_paused = not _paused
				if _paused:
					animation_player.pause()
				else:
					animation_player.play()
			KEY_R:
				_clip_index = -1
				_play_next_clip()

func _missing_assets() -> Array[String]:
	var missing: Array[String] = []
	for path in [MANNEQUIN_PATH, UAL1_PATH, UAL2_PATH]:
		if not ResourceLoader.exists(path):
			missing.append(path)
	return missing

func _spawn_actor() -> void:
	var mannequin_scene := load(MANNEQUIN_PATH) as PackedScene
	actor = mannequin_scene.instantiate() as Node3D
	actor.name = "Ilyra_UAL_Female_Test"
	add_child(actor)
	animation_player = AnimationPlayer.new()
	animation_player.name = "UALAnimationPlayer"
	actor.add_child(animation_player)
	animation_player.root_node = NodePath("..")

func _build_animation_library() -> void:
	var merged := AnimationLibrary.new()
	_copy_animations_from(load(UAL1_PATH) as PackedScene, merged)
	_copy_animations_from(load(UAL2_PATH) as PackedScene, merged)
	animation_player.add_animation_library(&"", merged)
	print("UAL rig preview loaded %d animations." % merged.get_animation_list().size())

func _copy_animations_from(source_scene: PackedScene, destination: AnimationLibrary) -> void:
	var source_root := source_scene.instantiate()
	var source_player := _find_animation_player(source_root)
	if source_player == null:
		push_error("UAL rig preview: no AnimationPlayer found in %s" % source_scene.resource_path)
		source_root.free()
		return
	for library_name in source_player.get_animation_library_list():
		var library := source_player.get_animation_library(library_name)
		for animation_name in library.get_animation_list():
			if destination.has_animation(animation_name):
				continue
			var copied := library.get_animation(animation_name).duplicate(true) as Animation
			destination.add_animation(animation_name, copied)
	source_root.free()

func _find_animation_player(node: Node) -> AnimationPlayer:
	if node is AnimationPlayer:
		return node as AnimationPlayer
	for child in node.get_children():
		var found := _find_animation_player(child)
		if found != null:
			return found
	return null

func _play_next_clip() -> void:
	_clip_index = (_clip_index + 1) % DEMO_CLIPS.size()
	var entry: Dictionary = DEMO_CLIPS[_clip_index]
	var clip_name: StringName = entry["name"]
	if not animation_player.has_animation(clip_name):
		push_warning("UAL rig preview: missing animation %s" % clip_name)
		_clip_time_left = 0.05
		return
	animation_player.play(clip_name, 0.18)
	var animation := animation_player.get_animation(clip_name)
	var requested_hold := float(entry["hold"])
	_clip_time_left = requested_hold if requested_hold > 0.0 else max(animation.length + 0.35, 0.8)
	info_label.text = "Diyse — UAL female rig proof\nNow: %s  [%s]\nSPACE next   P pause   R restart" % [entry["label"], clip_name]

func _setup_world() -> void:
	var environment := WorldEnvironment.new()
	var env := Environment.new()
	env.background_mode = Environment.BG_COLOR
	env.background_color = Color(0.055, 0.065, 0.085, 1.0)
	env.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	env.ambient_light_color = Color(0.62, 0.67, 0.78, 1.0)
	env.ambient_light_energy = 0.85
	environment.environment = env
	add_child(environment)
	var key_light := DirectionalLight3D.new()
	key_light.rotation_degrees = Vector3(-38.0, -28.0, 0.0)
	key_light.light_energy = 1.35
	key_light.shadow_enabled = true
	add_child(key_light)
	var fill_light := OmniLight3D.new()
	fill_light.position = Vector3(-1.8, 1.7, 2.2)
	fill_light.omni_range = 6.0
	fill_light.light_energy = 2.0
	add_child(fill_light)
	var ground := MeshInstance3D.new()
	var plane := PlaneMesh.new()
	plane.size = Vector2(6.0, 6.0)
	ground.mesh = plane
	var ground_material := StandardMaterial3D.new()
	ground_material.albedo_color = Color(0.13, 0.145, 0.17, 1.0)
	ground_material.roughness = 0.92
	ground.material_override = ground_material
	add_child(ground)
	var camera := Camera3D.new()
	camera.position = Vector3(0.0, 1.15, 3.45)
	camera.fov = 38.0
	camera.look_at_from_position(camera.position, Vector3(0.0, 0.95, 0.0), Vector3.UP)
	add_child(camera)

func _setup_hud() -> void:
	var canvas := CanvasLayer.new()
	add_child(canvas)
	var panel := ColorRect.new()
	panel.position = Vector2(18.0, 18.0)
	panel.size = Vector2(540.0, 135.0)
	panel.color = Color(0.02, 0.025, 0.035, 0.82)
	canvas.add_child(panel)
	info_label = Label.new()
	info_label.position = Vector2(34.0, 31.0)
	info_label.size = Vector2(510.0, 115.0)
	info_label.add_theme_font_size_override("font_size", 18)
	canvas.add_child(info_label)
