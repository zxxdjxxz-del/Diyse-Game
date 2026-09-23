extends SceneTree

const INTRO_SCENE := "res://game/presentation/world_intro.tscn"
const INTRO_DATA := "res://game/content/presentation/player_facing_world_intro.json"
const EXPECTED_MAIN_SCENE := "res://game/presentation/world_intro.tscn"
const EXPECTED_FINAL_LINE := "Mostly not metaphorically."

func _initialize() -> void:
	call_deferred("_run_validation")

func _run_validation() -> void:
	var failures: Array[String] = []

	var configured_main := str(ProjectSettings.get_setting("application/run/main_scene", ""))
	if configured_main != EXPECTED_MAIN_SCENE:
		failures.append("Game main scene must launch through the player-facing world intro")

	var raw := FileAccess.get_file_as_string(INTRO_DATA)
	if raw.is_empty():
		failures.append("Player-facing world intro JSON is missing")
	else:
		var parsed = JSON.parse_string(raw)
		if not (parsed is Dictionary):
			failures.append("Player-facing world intro JSON is invalid")
		else:
			var data := parsed as Dictionary
			if str(data.get("speaker_name", "")) != "Nimera Pellan":
				failures.append("World intro speaker must be Nimera Pellan")
			if str(data.get("present_year", "")) != "713 YF":
				failures.append("World intro present year must be 713 YF")
			if str(data.get("awakening_period", "")) != "around 200 YF":
				failures.append("World intro Awakening anchor must be around 200 YF")
			var paragraphs_value = data.get("paragraphs", [])
			if not (paragraphs_value is Array) or paragraphs_value.is_empty():
				failures.append("World intro paragraphs are missing")
			else:
				var paragraphs := paragraphs_value as Array
				if str(paragraphs[-1]) != EXPECTED_FINAL_LINE:
					failures.append("World intro must preserve Nimera's approved sign-off")
				if not paragraphs.has("Slept with people they probably shouldn't have."):
					failures.append("World intro lost the approved Diysean-humanity line")
				if not paragraphs.has("If somebody can throw fire today?"):
					failures.append("World intro lost the modern/ancient magic comparison")
				if not paragraphs.has("The Black Host is not a species. Not a curse. Not a horde of mindless things crawling out of a ruin."):
					failures.append("World intro lost the player-facing Black Host identity")
				if not paragraphs.has("At the center of it is Emperor Vaelkor Draeven."):
					failures.append("World intro lost Vaelkor's player-facing introduction")
				if not paragraphs.has("His exact age is unknown. The exact beginning of his reign is unknown. Reliable records agree that he has lived far beyond a normal human lifespan, and that is about where agreement starts falling apart."):
					failures.append("World intro lost Vaelkor's unknown-age boundary")

	var packed := load(INTRO_SCENE) as PackedScene
	if packed == null:
		failures.append("Could not load world intro scene")
	else:
		var intro := packed.instantiate()
		get_root().add_child(intro)
		await process_frame
		var title := intro.get_node_or_null("Background/Page/Content/Title") as Label
		var body := intro.get_node_or_null("Background/Page/Content/Body") as RichTextLabel
		var continue_button := intro.get_node_or_null("Background/Page/Content/Continue") as Button
		if title == null or title.text != "The World of Diyse":
			failures.append("World intro title is missing")
		if body == null or not body.text.contains("713 YF") or not body.text.contains("Nimera Pellan"):
			failures.append("World intro scene did not load the approved runtime text")
		if continue_button == null:
			failures.append("World intro scene is missing its Continue control")
		intro.queue_free()
		await process_frame

	_finish(failures)

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Player-facing Nimera world intro validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
