extends Node2D
class_name DiyseBattlePresentationController

signal layout_applied(party_count: int, enemy_count: int, viewport_size: Vector2)
signal prime_presentation_started(prime_id: String)
signal prime_presentation_finished(prime_id: String)

var _party_nodes: Array[Node2D] = []
var _enemy_nodes: Array[Node2D] = []
var _prime_node: Node2D = null
var _active_prime_id := ""

func bind_party_nodes(nodes: Array[Node2D]) -> void:
	_party_nodes = nodes.duplicate()

func bind_enemy_nodes(nodes: Array[Node2D]) -> void:
	_enemy_nodes = nodes.duplicate()

func apply_layout(viewport_size: Vector2 = Vector2.ZERO) -> void:
	var size := viewport_size
	if size.x <= 0.0 or size.y <= 0.0:
		size = get_viewport_rect().size
	if size.x <= 0.0 or size.y <= 0.0:
		size = DiyseHd2dRuntime.REFERENCE_SIZE

	for i in range(_party_nodes.size()):
		var node := _party_nodes[i]
		if node == null:
			continue
		var anchor := DiyseHd2dRuntime.party_anchor(i, size)
		if anchor.x >= 0.0:
			node.position = anchor

	for i in range(_enemy_nodes.size()):
		var node := _enemy_nodes[i]
		if node == null:
			continue
		var anchor := DiyseHd2dRuntime.enemy_anchor(i, size)
		if anchor.x >= 0.0:
			node.position = anchor

	layout_applied.emit(_party_nodes.size(), _enemy_nodes.size(), size)

func bind_and_layout(party_nodes: Array[Node2D], enemy_nodes: Array[Node2D], viewport_size: Vector2 = Vector2.ZERO) -> void:
	bind_party_nodes(party_nodes)
	bind_enemy_nodes(enemy_nodes)
	apply_layout(viewport_size)

func begin_prime_presentation(prime_id: String, prime_node: Node2D) -> bool:
	if prime_id.is_empty() or prime_node == null or not _active_prime_id.is_empty():
		return false
	_active_prime_id = prime_id
	_prime_node = prime_node
	for node in _party_nodes:
		if node != null:
			node.visible = false
	prime_node.visible = true
	prime_presentation_started.emit(prime_id)
	return true

func finish_prime_presentation() -> bool:
	if _active_prime_id.is_empty():
		return false
	var finished_prime_id := _active_prime_id
	if _prime_node != null:
		_prime_node.visible = false
	for node in _party_nodes:
		if node != null:
			node.visible = true
	_prime_node = null
	_active_prime_id = ""
	prime_presentation_finished.emit(finished_prime_id)
	return true

func active_prime_id() -> String:
	return _active_prime_id

func party_nodes() -> Array[Node2D]:
	return _party_nodes.duplicate()

func enemy_nodes() -> Array[Node2D]:
	return _enemy_nodes.duplicate()
