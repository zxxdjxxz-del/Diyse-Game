extends SceneTree

const GRAYBOX_SCENE := "res://game/exploration/maps/chapter_00/chapter_00_graybox.tscn"
const PRESENTATION_DIR := "res://game/content/presentation/chapter_00/"

var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	await _validate_graybox_scene()
	_validate_chapter_00_spatial_presentation_alignment()
	_finish()

func _validate_graybox_scene() -> void:
	var packed = load(GRAYBOX_SCENE)
	_expect(packed is PackedScene, "Chapter 0 graybox scene must load as PackedScene")
	if not (packed is PackedScene):
		return

	var instance = packed.instantiate()
	get_root().add_child(instance)

	# SceneTree test scripts begin before the first normal process frame. The
	# graybox constructs its route dynamically in the root scene's _ready(), so
	# wait one frame after attachment before asserting generated geometry.
	await process_frame

	_expect(instance.get_node_or_null("Cyanis") != null, "Graybox must include a controllable Cyanis proof actor")
	_expect(instance.get_node_or_null("Cyanis/Camera3D") != null, "Graybox must include the camera-variant test camera")
	_expect(instance.get_node_or_null("HUD/TouchDPad") != null, "Graybox must preserve Android touch-D-pad testing")
	_expect(instance.get_node_or_null("HUD/CameraA") != null, "Graybox must expose Camera A")
	_expect(instance.get_node_or_null("HUD/CameraB") != null, "Graybox must expose Camera B")
	_expect(instance.get_node_or_null("HUD/CameraC") != null, "Graybox must expose Camera C")

	for required_node in [
		"F01_Road_00",
		"F01_Encounter1",
		"F01_Encounter2",
		"F01_Pursuer",
		"F01_Riftmaw",
		"F02_Basin",
		"F02_EvacuationEvidence",
		"F03_RecoveryRoad_00",
		"F03_RelayYard",
		"F03_Decision",
		"F04_CampBase",
		"F04_Wounded",
		"F04_Supplies",
		"F04_Perimeter",
		"F04_EastCut",
		"F03R_SurvivorSweep_00",
		"F03R_Tracks",
		"F03R_WreckMarkerLimit",
		"F03R_BrackenwallHandoff",
	]:
		_expect(instance.get_node_or_null(required_node) != null, "Graybox missing required generated node %s" % required_node)

	for marker in [
		"Marker_S001-1",
		"Marker_S001-2",
		"Marker_S001-3_Pursuer",
		"Marker_S001-4_Riftmaw",
		"Marker_S002_Hound",
		"Marker_North_Withdrawal_Sightline",
		"Marker_S003_Decision",
		"Marker_Wounded___NO_COMBAT",
		"Marker_S004_Ilyra",
		"Marker_S005_Final_Confrontation",
		"Marker_S005_East_Cut",
		"Marker_Soldier_Withdraws_East",
		"Marker_S006_Sweep_Start",
		"Marker_S006_Tracks_South_of_Wagon_Line",
		"Marker_S006_Wreck_Marker_Limit",
		"Marker_TO_BRACKENWALL",
	]:
		_expect(instance.get_node_or_null(marker) != null, "Graybox missing authored spatial marker %s" % marker)

	var s005_marker = instance.get_node_or_null("Marker_S005_Final_Confrontation")
	var east_cut = instance.get_node_or_null("Marker_S005_East_Cut")
	var soldier_exit = instance.get_node_or_null("Marker_Soldier_Withdraws_East")
	if s005_marker != null and east_cut != null and soldier_exit != null:
		_expect(east_cut.position.x > s005_marker.position.x, "S005 enemy east cut must be east of the defensive confrontation pocket")
		_expect(soldier_exit.position.x >= east_cut.position.x, "Surviving S005 Soldier withdrawal must continue through the east cut")

	var sweep_start = instance.get_node_or_null("Marker_S006_Sweep_Start")
	var sweep_limit = instance.get_node_or_null("Marker_S006_Wreck_Marker_Limit")
	var brackenwall = instance.get_node_or_null("Marker_TO_BRACKENWALL")
	if sweep_start != null and sweep_limit != null and brackenwall != null:
		_expect(sweep_limit.position.z < sweep_start.position.z, "S006 bounded sweep must proceed outward from the camp")
		_expect(brackenwall.position.z < sweep_start.position.z, "Brackenwall handoff must occur after the bounded S006 sweep")

	var player = instance.get_node_or_null("Cyanis")
	if player != null:
		_expect(player.position.is_equal_approx(Vector3(0, 0.9, 108)), "Graybox player start must remain at the Convoy Road opening")

	var camera = instance.get_node_or_null("Cyanis/Camera3D")
	if camera != null:
		_expect(camera.position.is_equal_approx(Vector3(0, 6.5, 8.5)), "Default graybox camera must start on Camera B test framing")
		_expect(is_equal_approx(camera.fov, 56.0), "Default graybox camera FOV must remain 56 for Camera B")

	instance.queue_free()

func _validate_chapter_00_spatial_presentation_alignment() -> void:
	var s005 = load(PRESENTATION_DIR + "S005.tres")
	var s006 = load(PRESENTATION_DIR + "S006.tres")
	_expect(s005 != null, "S005 presentation sidecar must load")
	_expect(s006 != null, "S006 presentation sidecar must load")
	if s005 != null:
		_expect(str(s005.environment_family) == "CH00_TRIAGE_SAFE_CAMP", "S005 must use Field Triage Camp environment authority")
		_expect(str(s005.battle_background_family) == "CH00_TRIAGE_SAFE_CAMP", "S005 battle background must use the camp-perimeter environment family")
		_expect(s005.has_tag("CAMP_PERIMETER_DEFENSE"), "S005 must retain the camp-perimeter defense presentation tag")
	if s006 != null:
		_expect(str(s006.environment_family) == "CH00_RECOVERY_LINE", "S006 player-controlled survivor sweep must continue using Recovery Line environment family")
		_expect(s006.has_tag("PLAYER_CONTROLLED_SURVIVOR_SWEEP"), "S006 must retain player-controlled survivor-sweep intent")

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Chapter 0 graybox structure validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
