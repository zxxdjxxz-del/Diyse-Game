extends "res://game/characters/presentation/rig_preview/ilyra_production_v06_preview.gd"

# v0.7 keeps the v0.6 UAL + spring architecture and swaps in the seam-repaired
# replacement mesh. Flexible lowerarm->hand and calf->foot underlayers fill the
# large animated gaps exposed by the v0.6 deformation contact sheet.

const CHARACTER_V07_PATH := "res://asset_sources/animation/ual/Ilyra_ProductionMesh_v07_UAL_SpringReady.glb"

func _missing_assets() -> Array[String]:
	var missing: Array[String] = []
	for path in [CHARACTER_V07_PATH, UAL1_PATH, UAL2_PATH]:
		if not ResourceLoader.exists(path):
			missing.append(path)
	return missing

func _spawn_actor() -> void:
	var packed := load(CHARACTER_V07_PATH) as PackedScene
	actor = packed.instantiate() as Node3D
	actor.name = "Ilyra_ProductionMesh_v07"
	add_child(actor)
	animation_player = AnimationPlayer.new()
	animation_player.name = "UALAnimationPlayer"
	actor.add_child(animation_player)
	animation_player.root_node = NodePath("..")
	skeleton = _find_skeleton(actor)
	if skeleton == null:
		push_error("Ilyra v0.7 preview: Skeleton3D not found.")
		return
	if skeleton.get_bone_count() != 100:
		push_warning("Ilyra v0.7 expected 100 runtime bones; found %d." % skeleton.get_bone_count())
	_build_spring_simulator()
	_build_spring_debug()

func _update_hud() -> void:
	if info_label == null:
		return
	var label := "Ready"
	var clip := "none"
	if _clip_index >= 0 and _clip_index < STRESS_CLIPS.size():
		label = str(STRESS_CLIPS[_clip_index]["label"])
		clip = str(STRESS_CLIPS[_clip_index]["name"])
	info_label.text = "Diyse — Ilyra Production Mesh v0.7 / UAL live deformation proof\n%s  [%s]\nSEAM-REPAIRED replacement shell | 65 UAL core + 35 spring bones | %s | %s\nSPACE next   P pause   M springs   F wind   N spring bones   Q/E rotate   T turntable   R restart   ESC quit" % [label, clip, "SPRINGS ON" if _springs_enabled else "SPRINGS OFF", "WIND ON" if _wind_enabled else "WIND OFF"]
