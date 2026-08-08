extends Control

@export var player_path: NodePath

@onready var player := get_node(player_path)

var _left := false
var _right := false
var _up := false
var _down := false

func _ready() -> void:
	$Left.button_down.connect(_on_left_down)
	$Left.button_up.connect(_on_left_up)
	$Right.button_down.connect(_on_right_down)
	$Right.button_up.connect(_on_right_up)
	$Up.button_down.connect(_on_up_down)
	$Up.button_up.connect(_on_up_up)
	$Down.button_down.connect(_on_down_down)
	$Down.button_up.connect(_on_down_up)

func _process(_delta: float) -> void:
	if player == null or not player.has_method("set_touch_input"):
		return

	var x := (1.0 if _right else 0.0) - (1.0 if _left else 0.0)
	var y := (1.0 if _down else 0.0) - (1.0 if _up else 0.0)
	player.set_touch_input(Vector2(x, y).limit_length(1.0))

func _exit_tree() -> void:
	if player != null and player.has_method("set_touch_input"):
		player.set_touch_input(Vector2.ZERO)

func _on_left_down() -> void:
	_left = true

func _on_left_up() -> void:
	_left = false

func _on_right_down() -> void:
	_right = true

func _on_right_up() -> void:
	_right = false

func _on_up_down() -> void:
	_up = true

func _on_up_up() -> void:
	_up = false

func _on_down_down() -> void:
	_down = true

func _on_down_up() -> void:
	_down = false
