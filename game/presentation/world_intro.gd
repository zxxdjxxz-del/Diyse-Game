extends Control

const INTRO_DATA_PATH := "res://game/content/presentation/player_facing_world_intro.json"
const NEXT_SCENE_PATH := "res://game/exploration/field_proof.tscn"

@onready var title_label: Label = $Background/Page/Content/Title
@onready var body_label: RichTextLabel = $Background/Page/Content/Body
@onready var continue_button: Button = $Background/Page/Content/Continue

func _ready() -> void:
	continue_button.pressed.connect(_continue_to_game)
	_load_intro()
	continue_button.grab_focus()

func _load_intro() -> void:
	var raw := FileAccess.get_file_as_string(INTRO_DATA_PATH)
	if raw.is_empty():
		push_error("Player-facing world intro runtime data is missing: %s" % INTRO_DATA_PATH)
		title_label.text = "The World of Diyse"
		body_label.text = "The opening introduction could not be loaded."
		return

	var parsed = JSON.parse_string(raw)
	if not (parsed is Dictionary):
		push_error("Player-facing world intro runtime data is invalid JSON")
		return

	var data := parsed as Dictionary
	title_label.text = str(data.get("title", "The World of Diyse"))
	var paragraph_value = data.get("paragraphs", [])
	if not (paragraph_value is Array):
		push_error("Player-facing world intro has no paragraph array")
		return

	var paragraphs: Array[String] = []
	for value in paragraph_value:
		paragraphs.append(str(value))
	body_label.text = "\n\n".join(paragraphs)
	body_label.scroll_to_line(0)

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("ui_accept"):
		_continue_to_game()
		get_viewport().set_input_as_handled()

func _continue_to_game() -> void:
	if ResourceLoader.exists(NEXT_SCENE_PATH):
		get_tree().change_scene_to_file(NEXT_SCENE_PATH)
	else:
		push_error("World intro handoff scene is missing: %s" % NEXT_SCENE_PATH)
