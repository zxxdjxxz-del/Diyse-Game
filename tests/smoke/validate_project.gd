extends SceneTree

const FIELD_SCENE := "res://game/exploration/field_proof.tscn"

func _initialize() -> void:
	var failures: Array[String] = []
	var packed_scene := load(FIELD_SCENE) as PackedScene

	if packed_scene == null:
		failures.append("Could not load %s" % FIELD_SCENE)
		_finish(failures)
		return

	var field := packed_scene.instantiate()
	if field == null:
		failures.append("Could not instantiate field proof scene")
		_finish(failures)
		return

	if field.get_node_or_null("Ground") == null:
		failures.append("Field proof is missing Ground")
	if field.get_node_or_null("Obstacle") == null:
		failures.append("Field proof is missing collision Obstacle")
	if field.get_node_or_null("Cyanis") == null:
		failures.append("Field proof is missing Cyanis CharacterBody3D")
	if field.get_node_or_null("Cyanis/Sprite3D") == null:
		failures.append("Cyanis is missing 2.5D Sprite3D presentation")
	if field.get_node_or_null("Cyanis/Camera3D") == null:
		failures.append("Cyanis is missing follow Camera3D")
	if field.get_node_or_null("Cyanis/CollisionShape3D") == null:
		failures.append("Cyanis is missing collision shape")
	if field.get_node_or_null("HUD/TouchDPad") == null:
		failures.append("Field proof is missing temporary touch D-pad")
	if field.get_node_or_null("HUD/TouchDPad/Up") == null:
		failures.append("Touch D-pad is missing Up button")
	if field.get_node_or_null("HUD/TouchDPad/Down") == null:
		failures.append("Touch D-pad is missing Down button")
	if field.get_node_or_null("HUD/TouchDPad/Left") == null:
		failures.append("Touch D-pad is missing Left button")
	if field.get_node_or_null("HUD/TouchDPad/Right") == null:
		failures.append("Touch D-pad is missing Right button")

	field.queue_free()
	_finish(failures)

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Diyse 7B.5B smoke validation passed.")
		quit(0)
		return

	for failure in failures:
		push_error(failure)
	quit(1)
