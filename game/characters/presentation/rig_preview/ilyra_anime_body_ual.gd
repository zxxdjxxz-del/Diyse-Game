extends "res://game/characters/presentation/rig_preview/ilyra_ual_proxy.gd"

# Next-stage Ilyra motion/proportion proof.
# This keeps the UAL skeleton and animation libraries, but uses a conservatively
# reshaped skinned body mesh when that generated GLB is present.
# It is NOT Ilyra visual canon. Her exact B00 remains authoritative.

const ANIME_BODY_PATH := "res://asset_sources/animation/ual/Ilyra_AnimeBody_UAL.glb"

const ILYRA_DEMO_CLIPS := [
	{"name": &"Idle_Loop", "hold": 2.6, "label": "Neutral idle"},
	{"name": &"Walk_Loop", "hold": 2.4, "label": "Walk"},
	{"name": &"Jog_Fwd_Loop", "hold": 2.2, "label": "Jog"},
	{"name": &"Idle_Shield_Loop", "hold": 2.5, "label": "Blue Warden guard idle"},
	{"name": &"Shield_OneShot", "hold": 0.0, "label": "Shield action"},
	{"name": &"Shield_Dash", "hold": 0.0, "label": "Shield advance"},
	{"name": &"Sword_Attack", "hold": 0.0, "label": "Wardrod strike motion donor"},
	{"name": &"Spell_Simple_Shoot", "hold": 0.0, "label": "Warden spell"},
	{"name": &"Hit_Chest", "hold": 0.0, "label": "Hit reaction"},
]

func _spawn_actor() -> void:
	if not ResourceLoader.exists(ANIME_BODY_PATH):
		push_warning("Ilyra anime-body GLB is missing; falling back to the stock UAL female mannequin.")
		super._spawn_actor()
		return

	var body_scene := load(ANIME_BODY_PATH) as PackedScene
	actor = body_scene.instantiate() as Node3D
	actor.name = "Ilyra_AnimeBody_UAL_Proof"
	add_child(actor)

	animation_player = AnimationPlayer.new()
	animation_player.name = "UALAnimationPlayer"
	actor.add_child(animation_player)
	animation_player.root_node = NodePath("..")

	skeleton = _find_skeleton(actor)
	if skeleton == null:
		push_error("Ilyra anime-body UAL proof: no Skeleton3D found.")

func _apply_ilyra_proxy_style() -> void:
	super._apply_ilyra_proxy_style()
	if skeleton == null:
		return
	_add_wardrod_proxy()
	_add_shield_proxy()

func _add_wardrod_proxy() -> void:
	var hand := _bone_attachment("IlyraWardrod", "hand_r")
	if hand == null:
		return
	var silver := _make_material(Color(0.70, 0.76, 0.83, 1.0), 0.30, 0.55)
	var blue := _make_material(Color(0.30, 0.66, 0.90, 1.0), 0.26, 0.18)

	var rod := MeshInstance3D.new()
	var rod_mesh := CylinderMesh.new()
	rod_mesh.top_radius = 0.018
	rod_mesh.bottom_radius = 0.022
	rod_mesh.height = 0.72
	rod.mesh = rod_mesh
	rod.material_override = silver
	rod.position = Vector3(0.0, -0.24, 0.015)
	rod.rotation_degrees = Vector3(0.0, 0.0, 7.0)
	hand.add_child(rod)

	var focus := MeshInstance3D.new()
	var focus_mesh := SphereMesh.new()
	focus_mesh.radius = 0.045
	focus_mesh.height = 0.09
	focus.mesh = focus_mesh
	focus.material_override = blue
	focus.position = Vector3(0.0, -0.60, 0.015)
	hand.add_child(focus)

func _add_shield_proxy() -> void:
	var hand := _bone_attachment("IlyraShield", "hand_l")
	if hand == null:
		return
	var silver := _make_material(Color(0.69, 0.75, 0.82, 1.0), 0.27, 0.62)
	var pale_blue := _make_material(Color(0.48, 0.73, 0.90, 1.0), 0.34, 0.20)

	var shield := MeshInstance3D.new()
	var shield_mesh := CylinderMesh.new()
	shield_mesh.top_radius = 0.22
	shield_mesh.bottom_radius = 0.22
	shield_mesh.height = 0.035
	shield.mesh = shield_mesh
	shield.material_override = silver
	shield.position = Vector3(-0.035, -0.03, 0.11)
	shield.rotation_degrees = Vector3(90.0, 0.0, 0.0)
	hand.add_child(shield)

	var boss := MeshInstance3D.new()
	var boss_mesh := CylinderMesh.new()
	boss_mesh.top_radius = 0.075
	boss_mesh.bottom_radius = 0.075
	boss_mesh.height = 0.045
	boss.mesh = boss_mesh
	boss.material_override = pale_blue
	boss.position = Vector3(-0.035, -0.03, 0.137)
	boss.rotation_degrees = Vector3(90.0, 0.0, 0.0)
	hand.add_child(boss)

func _play_next_clip() -> void:
	if animation_player == null:
		return
	_clip_index = (_clip_index + 1) % ILYRA_DEMO_CLIPS.size()
	var entry: Dictionary = ILYRA_DEMO_CLIPS[_clip_index]
	var clip_name: StringName = entry["name"]
	if not animation_player.has_animation(clip_name):
		push_warning("Ilyra anime-body proof: missing animation %s" % clip_name)
		_clip_time_left = 0.05
		return
	animation_player.play(clip_name, 0.18)
	var animation := animation_player.get_animation(clip_name)
	var requested_hold := float(entry["hold"])
	_clip_time_left = requested_hold if requested_hold > 0.0 else max(animation.length + 0.35, 0.8)
	_update_hud(str(entry["label"]), str(clip_name))

func _update_hud(display_name: String, clip_name: String) -> void:
	if info_label == null:
		return
	info_label.text = "Diyse — Ilyra anime-body / UAL proof\n%s  [%s]\nWardrod + shield are canonical-equipment proxies; body remains prototype\nSPACE next   P pause   R restart   ESC quit" % [display_name, clip_name]
