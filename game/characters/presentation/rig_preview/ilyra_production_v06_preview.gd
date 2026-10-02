extends "res://game/characters/presentation/rig_preview/ilyra_production_preview_base.gd"

# Historical v0.6 regression wrapper. Shared production-preview behavior lives in
# ilyra_production_preview_base.gd so the current v0.7 preview does not inherit
# implementation through an obsolete-version script.

const CHARACTER_V06_PATH := "res://asset_sources/animation/ual/Ilyra_ProductionMesh_v06_UAL_SpringReady.glb"

func _character_path() -> String:
	return CHARACTER_V06_PATH

func _actor_name() -> String:
	return "Ilyra_ProductionMesh_v06"

func _preview_title() -> String:
	return "Diyse — Ilyra Production Mesh v0.6 / UAL live deformation proof"

func _shell_description() -> String:
	return "ACTUAL replacement shell"
