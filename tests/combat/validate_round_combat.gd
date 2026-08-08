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
	_test_standard_card_is_data_driven_unlimited_and_ordinary()
	_test_standard_card_retargets_after_enemy_ko()
	_test_prime_is_bearer_locked_and_spent_only_on_manifestation()
	_test_prime_activation_suspends_party_after_ordinary_round()
	_test_prime_direct_control_two_rounds_and_normal_return()
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

func _test_standard_card_is_data_driven_unlimited_and_ordinary() -> void:
	var battle = BattleState.new()
	battle.setup_demo()
	var cards: Array = battle.available_standard_cards()
	_expect(cards.size() == 1, "7B.5F must preserve exactly one placeholder Standard Card")
	if cards.is_empty():
		return
	var card = cards[0]
	_expect(str(card.card_id) == "proof_might_strike", "Placeholder Standard Card must come from its data resource")
	_expect(Resolver.priority_for("Card") == Resolver.ORDINARY_PRIORITY, "Card command must use the ordinary Speed-ordered action tier")
	var property_names: Array[String] = []
	for property in card.get_property_list():
		property_names.append(str(property["name"]))
	for forbidden in ["charges", "essence", "rank", "refresh_counter", "use_counter"]:
		_expect(not property_names.has(forbidden), "Standard Card data must not contain obsolete usage state: %s" % forbidden)

	battle.queue_party_action(0, "Card", 0, str(card.card_id))
	battle.queue_party_action(1, "Defend", 1)
	battle.queue_party_action(2, "Defend", 2)
	battle.queue_party_action(3, "Defend", 3)
	_expect(battle.confirm_round(), "First Standard Card round must confirm")
	_expect(int(battle.enemies[0]["hp"]) == 19, "Proof Strike should deal its data-defined 15 damage")
	battle.begin_round()
	battle.queue_party_action(0, "Card", 0, str(card.card_id))
	battle.queue_party_action(1, "Defend", 1)
	battle.queue_party_action(2, "Defend", 2)
	battle.queue_party_action(3, "Defend", 3)
	_expect(battle.confirm_round(), "Second Standard Card round must confirm without refresh or replenishment")
	_expect(int(battle.enemies[0]["hp"]) == 4, "The same Standard Card must remain reusable")

func _test_standard_card_retargets_after_enemy_ko() -> void:
	var battle = BattleState.new()
	battle.setup_demo()
	var card = battle.available_standard_cards()[0]
	battle.enemies[0]["hp"] = 12
	battle.queue_party_action(0, "Attack", 0)
	battle.queue_party_action(1, "Card", 0, str(card.card_id))
	battle.queue_party_action(2, "Defend", 2)
	battle.queue_party_action(3, "Defend", 3)
	_expect(battle.confirm_round(), "Card retarget test round must confirm")
	_expect(int(battle.enemies[0]["hp"]) == 0, "Cyanis should defeat Raider A before Ilyra's Card resolves")
	_expect(int(battle.enemies[1]["hp"]) == 19, "Ilyra's queued Standard Card must retarget to Raider B and deal 15 damage")

func _test_prime_is_bearer_locked_and_spent_only_on_manifestation() -> void:
	var battle = BattleState.new()
	battle.setup_demo()
	_expect(battle.available_prime_cards_for_actor(0).size() == 1, "Cyanis must have access to bearer-locked First Champion")
	_expect(battle.available_prime_cards_for_actor(1).is_empty(), "Ilyra must not have access to Cyanis's story Prime")
	_expect(not battle.queue_party_action(1, "Card", -1, "first_champion"), "Non-bearer must not queue First Champion")
	_expect(battle.prime_use_remaining("first_champion") == 1, "Prime use begins available")
	_expect(battle.queue_party_action(0, "Card", -1, "first_champion"), "Cyanis must be able to queue First Champion through Card")
	_expect(battle.prime_use_remaining("first_champion") == 1, "Queueing alone must not spend the Prime use")
	battle.queue_party_action(1, "Defend", 1)
	battle.queue_party_action(2, "Defend", 2)
	battle.queue_party_action(3, "Defend", 3)
	_expect(battle.confirm_round(), "Prime activation round must confirm")
	_expect(battle.prime_use_remaining("first_champion") == 0, "Successful manifestation must spend the one Prime use")

func _test_prime_activation_suspends_party_after_ordinary_round() -> void:
	var battle = BattleState.new()
	battle.setup_demo()
	battle.queue_party_action(0, "Card", -1, "first_champion")
	battle.queue_party_action(1, "Defend", 1)
	battle.queue_party_action(2, "Defend", 2)
	battle.queue_party_action(3, "Defend", 3)
	_expect(battle.confirm_round(), "Prime activation proof round must confirm")
	_expect(battle.party_suspended, "Party must be suspended only after the activation round finishes")
	_expect(battle.phase == "prime_selecting", "First Prime action round must enter direct command selection")
	_expect(str(battle.active_prime.get("name", "")) == "First Champion", "First Champion must become the sole active player combatant")
	_expect(int(battle.active_prime.get("max_hp", 0)) == 118, "Recovered Prime HP must equal rounded 70% of combined four-party maximum HP")
	_expect(int(battle.active_prime.get("speed", 0)) == 10, "First Champion Speed must snapshot Cyanis at the 1.00 profile multiplier")
	_expect(int(battle.active_prime.get("rounds_remaining", 0)) == 2, "Recovered First Champion must begin with exactly two Prime action rounds")
	for action in battle.enemy_actions:
		_expect(str(action.get("target_side", "")) == "prime", "Hostile actions must target the active Prime while party is suspended")
	var commands := battle.available_prime_commands()
	_expect(commands.size() == 3, "Recovered First Champion must expose exactly its first three commands")
	var command_names: Array[String] = []
	for command in commands:
		command_names.append(str(command.get("display_name", "")))
	_expect(command_names == ["Champion Edge", "Shieldbreak Arc", "Stand Between"], "Prime command sheet must match Recovered First Champion")

func _test_prime_direct_control_two_rounds_and_normal_return() -> void:
	var battle = BattleState.new()
	battle.setup_demo()
	battle.queue_party_action(0, "Card", -1, "first_champion")
	battle.queue_party_action(1, "Defend", 1)
	battle.queue_party_action(2, "Defend", 2)
	battle.queue_party_action(3, "Defend", 3)
	battle.confirm_round()
	var frozen_hp: Array[int] = []
	var frozen_mp: Array[int] = []
	for unit in battle.party:
		frozen_hp.append(int(unit["hp"]))
		frozen_mp.append(int(unit["mp"]))
	_expect(battle.resolve_prime_command("champion_edge", 0), "Player must directly select Champion Edge for Prime round one")
	_expect(battle.phase == "prime_selecting", "After Prime round one, one Recovered Prime round must remain")
	_expect(int(battle.active_prime.get("rounds_remaining", 0)) == 1, "Prime duration must decrement after one completed Prime action round")
	for i in range(battle.party.size()):
		_expect(int(battle.party[i]["hp"]) == frozen_hp[i] and int(battle.party[i]["mp"]) == frozen_mp[i], "Suspended party HP/MP must remain frozen during Prime replacement")
	_expect(battle.resolve_prime_command("stand_between", -1), "Player must directly select Stand Between for Prime round two")
	_expect(battle.phase == "prime_returned", "Recovered Prime must return normally after exactly two action rounds")
	_expect(not battle.party_suspended and battle.active_prime.is_empty(), "Party must be restored and Prime removed after normal expiry")
	for i in range(battle.party.size()):
		_expect(int(battle.party[i]["hp"]) == frozen_hp[i] and int(battle.party[i]["mp"]) == frozen_mp[i], "Normal Prime return must restore frozen party HP/MP unchanged")
	_expect(int(battle.party[0]["return_defense_bonus"]) == 25, "Stand Between must deliver its +25 Total Defense return marker")
	battle.begin_round()
	_expect(battle.available_prime_cards_for_actor(0).is_empty(), "First Champion cannot be activated again in the same ordinary battle after its use is spent")

func _finish() -> void:
	if failures.is_empty():
		print("Diyse 7B.5F deterministic combat, Card, retarget, and Prime validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
