extends SceneTree

const Resolver = preload("res://game/combat/round_resolver.gd")
const BattleState = preload("res://game/combat/battle_state.gd")

var failures: Array[String] = []

func _initialize() -> void:
	_test_item_and_defend_priority()
	_test_speed_order()
	_test_party_enemy_tie()
	_test_tied_party_selection_order()
	_test_tied_enemy_stable_order()
	_test_enemy_actions_lock_before_player_commands()
	_test_one_party_action_per_actor()
	_test_defend_applies_before_enemy_attack()
	_test_hostile_action_retargets_after_enemy_ko()
	_test_hostile_retarget_wraps_to_first_living_enemy()
	_finish()

func _action(name: String, command: String, side: String, speed: int, tie_order: int = 0, stable_order: int = 0) -> Dictionary:
	return {
		"actor_name": name,
		"command": command,
		"side": side,
		"speed": speed,
		"tie_order": tie_order,
		"stable_order": stable_order
	}

func _names(actions: Array) -> Array[String]:
	var result: Array[String] = []
	for action in actions:
		result.append(str(action["actor_name"]))
	return result

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _test_item_and_defend_priority() -> void:
	var ordered := Resolver.order_actions([
		_action("FastEnemy", "Attack", "enemy", 99),
		_action("Defender", "Defend", "party", 5),
		_action("ItemUser", "Item", "party", 2)
	])
	_expect(_names(ordered) == ["ItemUser", "Defender", "FastEnemy"], "Item must resolve before Defend, and Defend before faster ordinary actions")

func _test_speed_order() -> void:
	var ordered := Resolver.order_actions([
		_action("Slow", "Attack", "party", 5),
		_action("Fast", "Attack", "party", 12),
		_action("Middle", "Attack", "enemy", 8)
	])
	_expect(_names(ordered) == ["Fast", "Middle", "Slow"], "Ordinary actions must resolve by descending Speed")

func _test_party_enemy_tie() -> void:
	var ordered := Resolver.order_actions([
		_action("Enemy9", "Attack", "enemy", 9, 0, 0),
		_action("Party9", "Attack", "party", 9, 0, 0)
	])
	_expect(_names(ordered) == ["Party9", "Enemy9"], "Party must win an exact Speed tie against an enemy")

func _test_tied_party_selection_order() -> void:
	var ordered := Resolver.order_actions([
		_action("SelectedSecond", "Attack", "party", 10, 1),
		_action("SelectedFirst", "Attack", "party", 10, 0)
	])
	_expect(_names(ordered) == ["SelectedFirst", "SelectedSecond"], "Tied party members must follow player-selected tie order")

func _test_tied_enemy_stable_order() -> void:
	var ordered := Resolver.order_actions([
		_action("EnemyB", "Attack", "enemy", 10, 0, 1),
		_action("EnemyA", "Attack", "enemy", 10, 0, 0)
	])
	_expect(_names(ordered) == ["EnemyA", "EnemyB"], "Tied enemies must use stable deterministic order")

func _test_enemy_actions_lock_before_player_commands() -> void:
	var battle = BattleState.new()
	battle.setup_demo()
	_expect(battle.phase == "selecting", "Demo battle must begin in selecting phase")
	_expect(battle.enemy_actions.size() == 3, "All three living enemies must lock actions at round start")
	_expect(battle.party_actions.is_empty(), "Enemy actions must be locked before any player action exists")
	var locked_before: Array = battle.enemy_actions.duplicate(true)
	battle.queue_party_action(0, "Attack", 0)
	_expect(battle.enemy_actions == locked_before, "Enemy locks must not change after seeing a player command")

func _test_one_party_action_per_actor() -> void:
	var battle = BattleState.new()
	battle.setup_demo()
	battle.queue_party_action(0, "Attack", 0)
	battle.queue_party_action(0, "Attack", 1)
	_expect(battle.party_actions.size() == 1, "A party actor may have no more than one selected ordinary action in a round")
	_expect(int(battle.party_actions[0]["target_index"]) == 1, "Replacing an unconfirmed action should update rather than duplicate the actor command")

func _test_defend_applies_before_enemy_attack() -> void:
	var battle = BattleState.new()
	battle.setup_demo()
	var cyanis_start := int(battle.party[0]["hp"])
	battle.queue_party_action(0, "Defend", 0)
	battle.queue_party_action(1, "Attack", 0)
	battle.queue_party_action(2, "Attack", 0)
	battle.queue_party_action(3, "Attack", 0)
	_expect(battle.confirm_round(), "A complete four-character command set must confirm")
	_expect(int(battle.party[0]["hp"]) == cyanis_start - 5, "Defend must resolve before Raider A's faster ordinary attack and halve 9 damage to 5")
	_expect(battle.phase == "round_complete", "Non-terminal resolved round must end in round_complete phase")

func _test_hostile_action_retargets_after_enemy_ko() -> void:
	var battle = BattleState.new()
	battle.setup_demo()
	battle.enemies[0]["hp"] = 12
	battle.queue_party_action(0, "Attack", 0)
	battle.queue_party_action(1, "Attack", 0)
	battle.queue_party_action(2, "Defend", 2)
	battle.queue_party_action(3, "Defend", 3)
	_expect(battle.confirm_round(), "Retarget test round must confirm")
	_expect(int(battle.enemies[0]["hp"]) == 0, "Cyanis should defeat the originally targeted Raider A")
	_expect(int(battle.enemies[1]["hp"]) == 22, "Ilyra's queued attack on defeated Raider A must retarget to next living Raider B")
	var saw_retarget := false
	for line in battle.log:
		if "Ilyra retargets from Raider A to Raider B." in line:
			saw_retarget = true
	_expect(saw_retarget, "Combat log must expose automatic retargeting")

func _test_hostile_retarget_wraps_to_first_living_enemy() -> void:
	var battle = BattleState.new()
	battle.setup_demo()
	battle.enemies[2]["hp"] = 12
	battle.queue_party_action(0, "Attack", 2)
	battle.queue_party_action(1, "Attack", 2)
	battle.queue_party_action(2, "Defend", 2)
	battle.queue_party_action(3, "Defend", 3)
	_expect(battle.confirm_round(), "Wraparound retarget test round must confirm")
	_expect(int(battle.enemies[2]["hp"]) == 0, "Cyanis should defeat the originally targeted Raider C")
	_expect(int(battle.enemies[0]["hp"]) == 22, "Ilyra's queued attack on defeated Raider C must wrap to first living Raider A")

func _finish() -> void:
	if failures.is_empty():
		print("Diyse deterministic round combat validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
