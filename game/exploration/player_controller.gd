extends CharacterBody3D

signal eligible_distance_moved(distance: float)

@export var move_speed: float = 5.0
@export var acceleration: float = 20.0
@export var gravity: float = 24.0
@export var movement_camera_path: NodePath

@onready var sprite: Sprite3D = $Sprite3D
@onready var movement_camera: Camera3D = (
	get_node_or_null(movement_camera_path) as Camera3D
	if not movement_camera_path.is_empty()
	else null
)

var _touch_input := Vector2.ZERO
var _movement_enabled := true

func set_touch_input(value: Vector2) -> void:
	_touch_input = value.limit_length(1.0)

func set_movement_enabled(value: bool) -> void:
	_movement_enabled = value
	if not value:
		_touch_input = Vector2.ZERO

func movement_enabled() -> bool:
	return _movement_enabled

func _physics_process(delta: float) -> void:
	var keyboard_input := Vector2.ZERO

	if _movement_enabled:
		if Input.is_key_pressed(KEY_A) or Input.is_key_pressed(KEY_LEFT):
			keyboard_input.x -= 1.0
		if Input.is_key_pressed(KEY_D) or Input.is_key_pressed(KEY_RIGHT):
			keyboard_input.x += 1.0
		if Input.is_key_pressed(KEY_W) or Input.is_key_pressed(KEY_UP):
			keyboard_input.y -= 1.0
		if Input.is_key_pressed(KEY_S) or Input.is_key_pressed(KEY_DOWN):
			keyboard_input.y += 1.0

	var input_vector := Vector2.ZERO
	if _movement_enabled:
		input_vector = (keyboard_input + _touch_input).limit_length(1.0)

	var move_direction := Vector3(input_vector.x, 0.0, input_vector.y)
	if movement_camera != null:
		var camera_right := movement_camera.global_basis.x
		camera_right.y = 0.0
		camera_right = camera_right.normalized()

		var camera_forward := -movement_camera.global_basis.z
		camera_forward.y = 0.0
		camera_forward = camera_forward.normalized()

		# Touch/keyboard "up" is input_vector.y == -1, so negate Y here.
		move_direction = (
			camera_right * input_vector.x
			+ camera_forward * -input_vector.y
		).limit_length(1.0)

	var desired_velocity := move_direction * move_speed

	velocity.x = move_toward(velocity.x, desired_velocity.x, acceleration * delta)
	velocity.z = move_toward(velocity.z, desired_velocity.z, acceleration * delta)

	if is_on_floor():
		if velocity.y < 0.0:
			velocity.y = -0.1
	else:
		velocity.y -= gravity * delta

	if absf(input_vector.x) > 0.01:
		sprite.flip_h = input_vector.x < 0.0

	var before_position := global_position
	move_and_slide()
	_emit_resolved_eligible_distance(before_position, global_position)

func _emit_resolved_eligible_distance(before_position: Vector3, after_position: Vector3) -> float:
	if not _movement_enabled:
		return 0.0
	var horizontal_delta := Vector2(
		after_position.x - before_position.x,
		after_position.z - before_position.z
	)
	var distance := horizontal_delta.length()
	if distance > 0.00001:
		eligible_distance_moved.emit(distance)
	return distance
