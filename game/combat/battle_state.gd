extends RefCounted
class_name DiyseBattleState

const Resolver = preload("res://game/combat/round_resolver.gd")
const PROOF_STANDARD_CARD = preload("res://game/content/cards/proof_standard_card.tres")
const FIRST_CHAMPION = preload("res://game/content/cards/first_champion_recovered.tres")

const PARTY_ATTACK_DAMAGE := 12
const PARTY_ABILITY_DAMAGE := 20
const PARTY_ABILITY_MP_COST := 3
const ENEMY_ATTACK_DAMAGE := 9
const ITEM_HEAL := 18
const RECOVERED_PRIME_HP_FACTOR := 0.70
const PRIME_DEFEAT_BACKLASH_FACTOR := 0.15

var party: Array = []
var enemies: Array = []
var inventory := {"Potion": 3}
var standard_cards: Array = []
var prime_cards: Array = []
var prime_uses: Dictionary = {}
var round_number := 0
var phase := "idle"
var enemy_actions: Array = []
var party_actions: Array = []
var last_resolution_order: Array = []
var log: Array[String] = []
var rewards := {"xp": 0, "gold": 0}
var party_suspended := false
var pending_prime_id := ""
var active_prime: Dictionary = {}
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
	standard_cards = [PROOF_STANDARD_CARD]
	prime_cards = [FIRST_CHAMPION]
	prime_uses = {str(FIRST_CHAMPION.prime_id): 1}
	round_number = 0
	phase = "idle"
	enemy_actions.clear()
	party_actions.clear()
	last_resolution_order.clear()
	log.clear()
	rewards = {"xp": 0, "gold": 0}
	party_suspended = false
	pending_prime_id = ""
	active_prime.clear()
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
		"defending": false,
		"return_defense_bonus": 0,
		"return_defense_rounds": 0
	}

func begin_round() -> void:
	if phase in ["victory", "defeat"] or party_suspended:
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
			"tie_order": 0,
			"content_id": "",
			"content_kind": ""
		})
	return locked

func _lock_enemy_actions_against_prime() -> Array:
	var locked: Array = []
	for enemy_index in range(enemies.size()):
		var enemy: Dictionary = enemies[enemy_index]
		if int(enemy["hp"]) <= 0:
			continue
		locked.append({
			"actor_index": enemy_index,
			"actor_name": str(enemy["name"]),
			"side": "enemy",
			"command": "Attack",
			"target_side": "prime",
			"target_index": 0,
			"speed": int(enemy["speed"]),
			"stable_order": int(enemy["stable_order"]),
			"tie_order": 0,
			"content_id": "",
			"content_kind": ""
		})
	return locked

func available_standard_cards() -> Array:
	return standard_cards.duplicate()

func available_prime_cards_for_actor(actor_index: int) -> Array:
	var result: Array = []
	if phase != "selecting" or actor_index < 0 or actor_index >= party.size():
		return result
	var actor_name := str(party[actor_index]["name"])
	for prime in prime_cards:
		if str(prime.bearer_name) != actor_name:
			continue
		if int(prime_uses.get(str(prime.prime_id), 0)) <= 0:
			continue
		result.append(prime)
	return result

func prime_use_remaining(prime_id: String) -> int:
	return int(prime_uses.get(prime_id, 0))

func available_prime_commands() -> Array[Dictionary]:
	var result: Array[Dictionary] = []
	if not party_suspended or active_prime.is_empty():
		return result
	var definition = _prime_card_by_id(str(active_prime.get("prime_id", "")))
	if definition == null:
		return result
	for command in definition.commands:
		result.append(command.duplicate(true))
	return result

func queue_party_action(actor_index: int, command: String, target_index: int = -1, content_id: String = "") -> bool:
	if phase != "selecting":
		return false
	if actor_index < 0 or actor_index >= party.size():
		return false
	var actor: Dictionary = party[actor_index]
	if int(actor["hp"]) <= 0:
		return false
	if command not in ["Attack", "Ability", "Card", "Item", "Defend"]:
		return false
	if command == "Ability" and int(actor["mp"]) < PARTY_ABILITY_MP_COST:
		return false
	if command == "Item" and int(inventory.get("Potion", 0)) <= 0:
		return false

	var target_side := "enemy"
	var content_kind := ""
	if command in ["Item", "Defend"]:
		target_side = "party"
	elif command == "Card":
		var standard = _standard_card_by_id(content_id)
		if standard != null:
			content_kind = "standard"
			target_side = str(standard.target_side)
		else:
			var prime = _prime_card_by_id(content_id)
			if prime == null:
				return false
			if str(prime.bearer_name) != str(actor["name"]):
				return false
			if int(prime_uses.get(content_id, 0)) <= 0:
				return false
			for existing in party_actions:
				if int(existing["actor_index"]) != actor_index and str(existing.get("content_kind", "")) == "prime":
					return false
			content_kind = "prime"
			target_side = "none"
			target_index = -1

	if target_side == "enemy":
		if target_index < 0 or target_index >= enemies.size() or int(enemies[target_index]["hp"]) <= 0:
			return false
	elif target_side == "party":
		if command == "Defend":
			target_index = actor_index
		elif target_index < 0 or target_index >= party.size() or int(party[target_index]["hp"]) <= 0:
			return false
	elif target_side != "none":
		return false

	for i in range(party_actions.size()):
		if int(party_actions[i]["actor_index"]) == actor_index:
			party_actions.remove_at(i)
			break

	party_actions.append({
		"actor_index": actor_index,
		"actor_name": str(actor["name"]),
		"side": "party",
		"command": command,
		"target_side": target_side,
		"target_index": target_index,
		"speed": int(actor["speed"]),
		"stable_order": actor_index,
		"tie_order": _party_tie_counter,
		"content_id": content_id,
		"content_kind": content_kind
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
		if not pending_prime_id.is_empty():
			_enter_pending_prime()
		else:
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
		"Card":
			if str(action.get("content_kind", "")) == "prime":
				_execute_prime_activation(actor, action)
			else:
				_execute_standard_card(actor, action)
		"Attack":
			_damage_target(actor, action, PARTY_ATTACK_DAMAGE if side == "party" else ENEMY_ATTACK_DAMAGE, "attacks")

func _execute_standard_card(actor: Dictionary, action: Dictionary) -> void:
	var card = _standard_card_by_id(str(action.get("content_id", "")))
	if card == null:
		log.append("%s's Card definition is unavailable." % str(actor["name"]))
		return
	match str(card.effect_kind):
		"damage":
			_damage_target(actor, action, int(card.power), "uses %s on" % str(card.display_name))
		_:
			log.append("%s's %s has an unsupported proof effect." % [str(actor["name"]), str(card.display_name)])

func _execute_prime_activation(actor: Dictionary, action: Dictionary) -> void:
	var prime_id := str(action.get("content_id", ""))
	var prime = _prime_card_by_id(prime_id)
	if prime == null or str(prime.bearer_name) != str(actor["name"]):
		log.append("%s cannot activate that Prime." % str(actor["name"]))
		return
	if int(prime_uses.get(prime_id, 0)) <= 0 or not pending_prime_id.is_empty():
		log.append("%s is unavailable." % str(prime.display_name))
		return
	prime_uses[prime_id] = int(prime_uses[prime_id]) - 1
	pending_prime_id = prime_id
	log.append("%s activates %s. Manifestation Pending established; the ordinary round continues." % [str(actor["name"]), str(prime.display_name)])

func _enter_pending_prime() -> void:
	var prime = _prime_card_by_id(pending_prime_id)
	if prime == null:
		pending_prime_id = ""
		phase = "round_complete"
		return
	var combined_max_hp := 0
	var bearer_speed := 0
	for unit in party:
		combined_max_hp += int(unit["max_hp"])
		if str(unit["name"]) == str(prime.bearer_name):
			bearer_speed = int(unit["speed"])
	var prime_max_hp := int(round(float(combined_max_hp) * RECOVERED_PRIME_HP_FACTOR))
	active_prime = {
		"prime_id": str(prime.prime_id),
		"name": str(prime.display_name),
		"hp": prime_max_hp,
		"max_hp": prime_max_hp,
		"speed": int(round(float(bearer_speed) * float(prime.speed_multiplier))),
		"rounds_remaining": int(prime.duration_rounds),
		"duration_total": int(prime.duration_rounds),
		"guard_reduction": 0.0,
		"return_defense_prepared": false
	}
	party_suspended = true
	pending_prime_id = ""
	party_actions.clear()
	log.append("The active party is Suspended. %s enters at %d/%d HP." % [str(active_prime["name"]), int(active_prime["hp"]), int(active_prime["max_hp"])])
	_begin_prime_round()

func _begin_prime_round() -> void:
	if not party_suspended or active_prime.is_empty():
		return
	round_number += 1
	enemy_actions = _lock_enemy_actions_against_prime()
	phase = "prime_selecting"
	log.append("Prime round %d begins. Select exactly one %s command." % [round_number, str(active_prime["name"])])

func resolve_prime_command(command_id: String, target_index: int = -1) -> bool:
	if phase != "prime_selecting" or not party_suspended or active_prime.is_empty():
		return false
	var command := _prime_command_by_id(command_id)
	if command.is_empty():
		return false
	var target_mode := str(command.get("target_mode", "one"))
	if target_mode == "one":
		if target_index < 0 or target_index >= enemies.size() or int(enemies[target_index]["hp"]) <= 0:
			return false
	else:
		target_index = -1

	var prime_action := {
		"actor_index": 0,
		"actor_name": str(active_prime["name"]),
		"side": "party",
		"command": "PrimeCommand",
		"target_side": str(command.get("target_side", "enemy")),
		"target_index": target_index,
		"speed": int(active_prime["speed"]),
		"stable_order": 0,
		"tie_order": 0,
		"content_id": command_id,
		"content_kind": "prime_command"
	}
	var combined: Array = [prime_action]
	combined.append_array(enemy_actions.duplicate(true))
	last_resolution_order = Resolver.order_actions(combined)
	phase = "prime_resolving"
	for action in last_resolution_order:
		if str(action.get("content_kind", "")) == "prime_command":
			_execute_prime_command(action)
		else:
			_execute_enemy_action_against_prime(action)
		if _living_indices(enemies).is_empty() or int(active_prime.get("hp", 0)) <= 0:
			break

	if _living_indices(enemies).is_empty():
		_normal_prime_return()
		phase = "victory"
		rewards = {"xp": 30, "gold": 42}
		log.append("Victory. Rewards: 30 XP, 42 gold.")
		return true
	if int(active_prime.get("hp", 0)) <= 0:
		_prime_defeat_return()
		return true

	active_prime["rounds_remaining"] = int(active_prime["rounds_remaining"]) - 1
	if int(active_prime["rounds_remaining"]) <= 0:
		_normal_prime_return()
		phase = "prime_returned"
	else:
		_begin_prime_round()
	return true

func _execute_prime_command(action: Dictionary) -> void:
	var command := _prime_command_by_id(str(action.get("content_id", "")))
	if command.is_empty():
		return
	if float(active_prime.get("guard_reduction", 0.0)) > 0.0:
		active_prime["guard_reduction"] = 0.0
	var command_id := str(command.get("command_id", ""))
	match command_id:
		"champion_edge":
			var target_index := _next_living_target_index(enemies, int(action.get("target_index", -1)))
			if target_index == -1:
				return
			var target: Dictionary = enemies[target_index]
			var damage := int(command.get("proof_damage", 22))
			target["hp"] = maxi(0, int(target["hp"]) - damage)
			log.append("%s uses Champion Edge on %s for %d proof damage." % [str(active_prime["name"]), str(target["name"]), damage])
			if int(target["hp"]) == 0:
				log.append("%s is KO." % str(target["name"]))
		"shieldbreak_arc":
			var damage := int(command.get("proof_damage", 15))
			for enemy in enemies:
				if int(enemy["hp"]) <= 0:
					continue
				enemy["hp"] = maxi(0, int(enemy["hp"]) - damage)
				log.append("%s hits %s with Shieldbreak Arc for %d proof damage." % [str(active_prime["name"]), str(enemy["name"]), damage])
				if int(enemy["hp"]) == 0:
					log.append("%s is KO." % str(enemy["name"]))
		"stand_between":
			active_prime["guard_reduction"] = 0.45
			active_prime["return_defense_prepared"] = true
			log.append("%s uses Stand Between: 45%% reduction until its next action; +25 Total Defense return marker prepared." % str(active_prime["name"]))

func _execute_enemy_action_against_prime(action: Dictionary) -> void:
	if active_prime.is_empty() or int(active_prime.get("hp", 0)) <= 0:
		return
	var enemy_index := int(action.get("actor_index", -1))
	if enemy_index < 0 or enemy_index >= enemies.size() or int(enemies[enemy_index]["hp"]) <= 0:
		return
	var damage := int(round(float(ENEMY_ATTACK_DAMAGE) * 0.85))
	var guard := float(active_prime.get("guard_reduction", 0.0))
	if guard > 0.0:
		damage = maxi(1, int(round(float(damage) * (1.0 - guard))))
	active_prime["hp"] = maxi(0, int(active_prime["hp"]) - damage)
	log.append("%s attacks %s for %d damage." % [str(enemies[enemy_index]["name"]), str(active_prime["name"]), damage])
	if int(active_prime["hp"]) == 0:
		log.append("%s is defeated." % str(active_prime["name"]))

func _normal_prime_return() -> void:
	if active_prime.is_empty():
		return
	var prime_name := str(active_prime["name"])
	if bool(active_prime.get("return_defense_prepared", false)):
		for unit in party:
			if int(unit["hp"]) > 0:
				unit["return_defense_bonus"] = 25
				unit["return_defense_rounds"] = 1
		log.append("Stand Between return effect applied: eligible party receives +25 Total Defense marker for the next round.")
	party_suspended = false
	active_prime.clear()
	enemy_actions.clear()
	log.append("%s exits normally. The suspended party returns with frozen HP/MP state restored." % prime_name)

func _prime_defeat_return() -> void:
	var prime_name := str(active_prime.get("name", "Prime"))
	party_suspended = false
	active_prime.clear()
	enemy_actions.clear()
	for unit in party:
		if int(unit["hp"]) <= 0:
			continue
		var backlash := int(round(float(unit["max_hp"]) * PRIME_DEFEAT_BACKLASH_FACTOR))
		unit["hp"] = maxi(1, int(unit["hp"]) - backlash)
	phase = "prime_returned"
	log.append("%s is defeated. Party returns under Resonance Backlash (15%% maximum HP, cannot reduce below 1 HP)." % prime_name)

func _standard_card_by_id(card_id: String):
	for card in standard_cards:
		if str(card.card_id) == card_id:
			return card
	return null

func _prime_card_by_id(prime_id: String):
	for prime in prime_cards:
		if str(prime.prime_id) == prime_id:
			return prime
	return null

func _prime_command_by_id(command_id: String) -> Dictionary:
	var definition = _prime_card_by_id(str(active_prime.get("prime_id", "")))
	if definition == null:
		return {}
	for command in definition.commands:
		if str(command.get("command_id", "")) == command_id:
			return command
	return {}

func _damage_target(actor: Dictionary, action: Dictionary, base_damage: int, verb: String) -> void:
	var target_side := str(action["target_side"])
	var target_array: Array = party if target_side == "party" else enemies
	var original_index := int(action["target_index"])
	var resolved_index := original_index

	if str(action["side"]) == "party" and target_side == "enemy":
		resolved_index = _next_living_target_index(target_array, original_index)
		if resolved_index == -1:
			log.append("%s's action has no living target." % str(actor["name"]))
			return
		if resolved_index != original_index:
			var original_name := "defeated target"
			if original_index >= 0 and original_index < target_array.size():
				original_name = str(target_array[original_index]["name"])
			log.append("%s retargets from %s to %s." % [str(actor["name"]), original_name, str(target_array[resolved_index]["name"])])

	var target := _target(target_array, resolved_index)
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

func _next_living_target_index(units: Array, original_index: int) -> int:
	if units.is_empty():
		return -1
	if original_index >= 0 and original_index < units.size() and int(units[original_index]["hp"]) > 0:
		return original_index
	for offset in range(1, units.size() + 1):
		var index := (original_index + offset) % units.size()
		if index >= 0 and int(units[index]["hp"]) > 0:
			return index
	return -1

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
	if not party_suspended and _living_indices(party).is_empty():
		phase = "defeat"
		log.append("Defeat.")
		return true
	return false
