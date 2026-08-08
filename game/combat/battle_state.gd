extends RefCounted
class_name DiyseBattleState

const Resolver = preload("res://game/combat/round_resolver.gd")

const PARTY_ATTACK_DAMAGE := 12
const PARTY_ABILITY_DAMAGE := 20
const PARTY_ABILITY_MP_COST := 3
const ENEMY_ATTACK_DAMAGE := 9
const ITEM_HEAL := 18

var party: Array = []
var enemies: Array = []
var inventory := {"Potion": 3}
var round_number := 0
var phase := "idle"
var enemy_actions: Array = []
var party_actions: Array = []
var last_resolution_order: Array = []
var log: Array[String] = []
var rewards := {"xp": 0, "gold": 0}
var _party_tie_counter := 0

func setup_demo() -> void:
	party = [
		_unit("Cyanis", "party", 46, 12, 10, 0),
		_unit("Ilyra", "party", 40, 18, 9, 1),
		_unit("Torren", "party", 44, 10, 8, 2),
		_unit("Nimera", "party", 38, 16, 7, 3)
	]
	enemies = [
		_unit("Raider A", "enemy", 34, 0, 11, 0),
		_unit("Raider B", "enemy", 34, 0, 9, 1),
		_unit("Raider C", "enemy", 34, 0, 6, 2)
	]
	inventory = {"Potion": 3}
	round_number = 0
	phase = "idle"
	enemy_actions.clear()
	party_actions.clear()
	last_resolution_order.clear()
	log.clear()
	rewards = {"xp": 0, "gold": 0}
	begin_round()

func _unit(name: String, side: String, hp: int, mp: int, speed: int, stable_order: int) -> Dictionary:
	return {
		"name": name,
		"side": side,
		"hp": hp,
		"max_hp": hp,
		"mp": mp,
		"max_mp": mp,
		"speed": speed,
		"stable_order": stable_order,
		"defending": false
	}

func begin_round() -> void:
	if phase == "victory" or phase == "defeat":
		return
	for unit in party:
		unit["defending"] = false
	for unit in enemies:
		unit["defending"] = false
	round_number += 1
	party_actions.clear()
	_party_tie_counter = 0
	enemy_actions = _lock_enemy_actions()
	phase = "selecting"
	log.append("Round %d begins. Enemy actions locked before player confirmation." % round_number)

func _lock_enemy_actions() -> Array:
	var locked: Array = []
	var living_party := _living_indices(party)
	if living_party.is_empty():
		return locked
	for enemy_index in range(enemies.size()):
		var enemy: Dictionary = enemies[enemy_index]
		if int(enemy["hp"]) <= 0:
			continue
		var target_slot := (round_number + int(enemy["stable_order"]) - 1) % living_party.size()
		var target_index: int = living_party[target_slot]
		locked.append({
			"actor_index": enemy_index,
			"actor_name": str(enemy["name"]),
			"side": "enemy",
			"command": "Attack",
			"target_side": "party",
			"target_index": target_index,
			"speed": int(enemy["speed"]),
			"stable_order": int(enemy["stable_order"]),
			"tie_order": 0
		})
	return locked

func queue_party_action(actor_index: int, command: String, target_index: int = -1) -> bool:
	if phase != "selecting":
		return false
	if actor_index < 0 or actor_index >= party.size():
		return false
	var actor: Dictionary = party[actor_index]
	if int(actor["hp"]) <= 0:
		return false
	if command not in ["Attack", "Ability", "Item", "Defend"]:
		return false
	if command == "Ability" and int(actor["mp"]) < PARTY_ABILITY_MP_COST:
		return false
	if command == "Item" and int(inventory.get("Potion", 0)) <= 0:
		return false
	if command in ["Attack", "Ability"]:
		if target_index < 0 or target_index >= enemies.size() or int(enemies[target_index]["hp"]) <= 0:
			return false
	if command == "Item":
		if target_index < 0 or target_index >= party.size() or int(party[target_index]["hp"]) <= 0:
			return false
	if command == "Defend":
		target_index = actor_index

	for i in range(party_actions.size()):
		if int(party_actions[i]["actor_index"]) == actor_index:
			party_actions.remove_at(i)
			break

	party_actions.append({
		"actor_index": actor_index,
		"actor_name": str(actor["name"]),
		"side": "party",
		"command": command,
		"target_side": "party" if command in ["Item", "Defend"] else "enemy",
		"target_index": target_index,
		"speed": int(actor["speed"]),
		"stable_order": actor_index,
		"tie_order": _party_tie_counter
	})
	_party_tie_counter += 1
	return true

func all_living_party_have_actions() -> bool:
	var needed := 0
	for unit in party:
		if int(unit["hp"]) > 0:
			needed += 1
	return party_actions.size() == needed

func confirm_round() -> bool:
	if phase != "selecting" or not all_living_party_have_actions():
		return false
	phase = "resolving"
	var combined := party_actions.duplicate(true)
	combined.append_array(enemy_actions.duplicate(true))
	last_resolution_order = Resolver.order_actions(combined)
	for action in last_resolution_order:
		_execute_action(action)
		if _check_end_state():
			break
	if phase == "resolving":
		phase = "round_complete"
	return true

func _execute_action(action: Dictionary) -> void:
	var side := str(action["side"])
	var actor_array: Array = party if side == "party" else enemies
	var actor_index := int(action["actor_index"])
	if actor_index < 0 or actor_index >= actor_array.size():
		return
	var actor: Dictionary = actor_array[actor_index]
	if int(actor["hp"]) <= 0:
		log.append("%s cannot act." % str(actor["name"]))
		return

	var command := str(action["command"])
	match command:
		"Defend":
			actor["defending"] = true
			log.append("%s defends." % str(actor["name"]))
		"Item":
			if int(inventory.get("Potion", 0)) <= 0:
				log.append("%s has no Potion remaining." % str(actor["name"]))
				return
			var target := _target(party, int(action["target_index"]))
			if target.is_empty() or int(target["hp"]) <= 0:
				log.append("%s's Item has no legal target." % str(actor["name"]))
				return
			inventory["Potion"] = int(inventory["Potion"]) - 1
			var before := int(target["hp"])
			target["hp"] = mini(int(target["max_hp"]), before + ITEM_HEAL)
			log.append("%s uses Potion on %s (+%d HP)." % [str(actor["name"]), str(target["name"]), int(target["hp"]) - before])
		"Ability":
			if int(actor["mp"]) < PARTY_ABILITY_MP_COST:
				log.append("%s lacks MP." % str(actor["name"]))
				return
			actor["mp"] = int(actor["mp"]) - PARTY_ABILITY_MP_COST
			_damage_target(actor, action, PARTY_ABILITY_DAMAGE, "uses Ability on")
		"Attack":
			_damage_target(actor, action, PARTY_ATTACK_DAMAGE if side == "party" else ENEMY_ATTACK_DAMAGE, "attacks")

func _damage_target(actor: Dictionary, action: Dictionary, base_damage: int, verb: String) -> void:
	var target_array: Array = party if str(action["target_side"]) == "party" else enemies
	var target := _target(target_array, int(action["target_index"]))
	if target.is_empty() or int(target["hp"]) <= 0:
		log.append("%s's action has no living target." % str(actor["name"]))
		return
	var damage := base_damage
	if bool(target.get("defending", false)):
		damage = int(ceil(float(damage) / 2.0))
	target["hp"] = maxi(0, int(target["hp"]) - damage)
	log.append("%s %s %s for %d damage." % [str(actor["name"]), verb, str(target["name"]), damage])
	if int(target["hp"]) == 0:
		log.append("%s is KO." % str(target["name"]))

func _target(units: Array, index: int) -> Dictionary:
	if index < 0 or index >= units.size():
		return {}
	return units[index]

func _living_indices(units: Array) -> Array[int]:
	var result: Array[int] = []
	for i in range(units.size()):
		if int(units[i]["hp"]) > 0:
			result.append(i)
	return result

func _check_end_state() -> bool:
	if _living_indices(enemies).is_empty():
		phase = "victory"
		rewards = {"xp": 30, "gold": 42}
		log.append("Victory. Rewards: 30 XP, 42 gold.")
		return true
	if _living_indices(party).is_empty():
		phase = "defeat"
		log.append("Defeat.")
		return true
	return false
