extends "res://game/characters/presentation/rig_preview/ilyra_production_preview_base.gd"

# Current v0.7 regression wrapper. Shared UAL/spring/stress-loop behavior lives
# in ilyra_production_preview_base.gd; this file supplies only the v0.7 mesh and
# current HUD identity.

const CHARACTER_V07_PATH := "res://asset_sources/animation/ual/Ilyra_ProductionMesh_v07_UAL_SpringReady.glb"

func _character_path() -> String:
	return CHARACTER_V07_PATH

func _actor_name() -> String:
	return "Ilyra_ProductionMesh_v07"

func _preview_title() -> String:
	return "Diyse — Ilyra Production Mesh v0.7 / UAL live deformation proof"

func _shell_description() -> String:
	return "SEAM-REPAIRED replacement shell"
