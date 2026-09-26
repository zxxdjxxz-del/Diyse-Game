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
		"F01_Breather1",
		"F01_Encounter2",
		"F01_Breather2",
		"F01_Encounter3",
		"F02_Basin",
		"F02_MixedPressure",
		"F02_StoneLineBreather",
		"F02_SurvivorRouteHound",
		"F02_EvacuationEvidence",
		"F03_RecoveryRoad_00",
		"F03_RelayYard",
		"F03_Decision",
		"F04_CampBase",
		"F04_Wounded",
		"F04_Supplies",
		"F04_Pursuer",
		"F04_FinalBoss",
		"F04_EastCut",
		"F03R_SurvivorSweep_00",
		"F03R_Tracks",
		"F03R_WreckMarkerLimit",
		"F03R_BrackenwallHandoff",
	]:
		_expect(instance.get_node_or_null(required_node) != null, "Graybox missing required generated node %s" % required_node)

	for marker in [
		"Marker_P01_Combat_1_—_Raider_+_Crossbowman",
		"Marker_P01_Breather_1_—_survivor_movement",
		"Marker_P01_Combat_2_—_Raider_+_Shieldbearer",
		"Marker_P01_Breather_2_—_wreckage_read",
		"Marker_P01_Combat_3_—_Hound_Rush",
		"Marker_P01_Late-road_breathing",
		"Marker_P02_Combat_4_—_Crossbowman_+_Hound",
		"Marker_P02_Breather_—_lower_stone_line",
		"Marker_P02_Combat_5_—_Survivor-Route_Hound",
		"Marker_North_Withdrawal_Sightline",
		"Marker_P03_Decision",
		"Marker_Wounded___NO_COMBAT",
		"Marker_P04_Ilyra",
		"Marker_P05_Concealed_Seyrik",
		"Marker_P05-P06_Noncombat_Reset",
		"Marker_P06_Riftmaw_+_War-Sorcerer",
		"Marker_P06_East_Cut",
		"Marker_P07_Sweep_Start",
		"Marker_P07_Tracks_South_of_Wagon_Line",
		"Marker_P07_Wreck_Marker_Limit",
		"Marker_TO_BRACKENWALL",
	]:
		_expect(instance.get_node_or_null(marker) != null, "Graybox missing authored spatial marker %s" % marker)

	var p05_marker = instance.get_node_or_null("Marker_P05_Concealed_Seyrik")
	var p06_marker = instance.get_node_or_null("Marker_P06_Riftmaw_+_War-Sorcerer")
	var east_cut = instance.get_node_or_null("Marker_P06_East_Cut")
	if p05_marker != null and p06_marker != null and east_cut != null:
		_expect(east_cut.position.x > p05_marker.position.x, "P06 east cut must remain east of the concealed-Seyrik pressure pocket")
		_expect(p06_marker.position.x <= east_cut.position.x, "Combined final boss pocket must remain inside the defended camp before the east cut")

	var sweep_start = instance.get_node_or_null("Marker_P07_Sweep_Start")
	var sweep_limit = instance.get_node_or_null("Marker_P07_Wreck_Marker_Limit")
	var brackenwall = instance.get_node_or_null("Marker_TO_BRACKENWALL")
	if sweep_start != null and sweep_limit != null and brackenwall != null:
		_expect(sweep_limit.position.z < sweep_start.position.z, "P07 bounded sweep must proceed outward from the camp")
		_expect(brackenwall.position.z < sweep_start.position.z, "Brackenwall handoff must occur after the bounded P07 sweep")

	var player = instance.get_node_or_null("Cyanis")
	if player != null:
		_expect(player.position.is_equal_approx(Vector3(0, 0.9, 108)), "Graybox player start must remain at the Convoy Road opening")

	var camera = instance.get_node_or_null("Cyanis/Camera3D")
	if camera != null:
		_expect(camera.position.is_equal_approx(Vector3(0, 6.5, 8.5)), "Default graybox camera must start on Camera B test framing")
		_expect(is_equal_approx(camera.fov, 56.0), "Default graybox camera FOV must remain 56 for Camera B")

	instance.queue_free()

func _validate_chapter_00_spatial_presentation_alignment() -> void:
	var b05 = load(PRESENTATION_DIR + "B05.tres")
	var b06 = load(PRESENTATION_DIR + "B06.tres")
	var b07 = load(PRESENTATION_DIR + "B07.tres")
	_expect(b05 != null, "B05 presentation sidecar must load")
	_expect(b06 != null, "B06 presentation sidecar must load")
	_expect(b07 != null, "B07 presentation sidecar must load")
	if b05 != null:
		_expect(str(b05.environment_family) == "CH00_TRIAGE_SAFE_CAMP", "B05 concealed Vanguard encounter must use the defended triage-camp environment")
		_expect(b05.has_tag("NONCOMBAT_RESET_AFTER"), "B05 must preserve the real noncombat perimeter reset before B06")
	if b06 != null:
		_expect(str(b06.environment_family) == "CH00_TRIAGE_SAFE_CAMP", "B06 final boss must use Field Triage Camp environment authority")
		_expect(str(b06.battle_background_family) == "CH00_TRIAGE_SAFE_CAMP", "B06 battle background must use the camp-perimeter environment family")
		_expect(b06.has_tag("RIFTMAW_WAR_SORCERER_COMBINED_BOSS"), "B06 must retain the combined Riftmaw + War-Sorcerer boss presentation")
	if b07 != null:
		_expect(str(b07.environment_family) == "CH00_RECOVERY_LINE", "B07 survivor recovery must continue using Recovery Line environment authority")
		_expect(b07.has_tag("BOUNDED_SURVIVOR_SWEEP"), "B07 must retain the bounded survivor-sweep intent")

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
