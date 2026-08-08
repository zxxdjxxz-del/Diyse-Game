extends CharacterBody3D

@export var move_speed: float = 5.0
@export var acceleration: float = 20.0
@export var gravity: float = 24.0

@onready var sprite: Sprite3D = $Sprite3D

func _physics_process(delta: float) -> void:
	var input_vector := Vector2.ZERO

	if Input.is_key_pressed(KEY_A) or Input.is_key_pressed(KEY_LEFT):
		input_vector.x -= 1.0
	if Input.is_key_pressed(KEY_D) or Input.is_key_pressed(KEY_RIGHT):
		input_vector.x += 1.0
	if Input.is_key_pressed(KEY_W) or Input.is_key_pressed(KEY_UP):
		input_vector.y -= 1.0
	if Input.is_key_pressed(KEY_S) or Input.is_key_pressed(KEY_DOWN):
		input_vector.y += 1.0

	input_vector = input_vector.normalized()
	var desired_velocity := Vector3(input_vector.x, 0.0, input_vector.y) * move_speed

	velocity.x = move_toward(velocity.x, desired_velocity.x, acceleration * delta)
	velocity.z = move_toward(velocity.z, desired_velocity.z, acceleration * delta)

	if is_on_floor():
		if velocity.y < 0.0:
			velocity.y = -0.1
	else:
		velocity.y -= gravity * delta

	if absf(input_vector.x) > 0.01:
		sprite.flip_h = input_vector.x < 0.0

	move_and_slide()
