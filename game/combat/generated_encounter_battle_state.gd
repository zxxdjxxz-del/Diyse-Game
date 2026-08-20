extends "res://game/combat/battle_state.gd"
class_name DiyseGeneratedEncounterBattleState

const MAX_ACTIVE_ENEMIES := 8

var generated_encounter_id := ""
var generated_reward_xp := 0
var generated_reward_gold := 0
var generated_encounter_active := false

func setup_generated_formation(
	enemy_definitions: Array,
	xp_reward: int,
	gold_reward: int = 0,
	encounter_id: String = ""
) -> bool:
	if enemy_definitions.is_empty() or enemy_definitions.size() > MAX_ACTIVE_ENEMIES:
		return false
	for entry in enemy_definitions:
		if not (entry is Dictionary):
			return false
		if str(entry.get("display_name", "")).is_empty():
			return false
		if int(entry.get("hp", 0)) <= 0 or int(entry.get("speed", -1)) < 0:
			return false

	# Preserve the accepted proof party/Card/Prime regression setup, then replace
	# only the enemy side and encounter reward contract.
	super.setup_demo()
	enemies.clear()
	var seen_names: Dictionary = {}
	for i in range(enemy_definitions.size()):
		var definition: Dictionary = enemy_definitions[i]
		var base_name := str(definition.get("display_name", "Enemy"))
		var count := int(seen_names.get(base_name, 0)) + 1
		seen_names[base_name] = count
		var combat_name := base_name if count == 1 else "%s %d" % [base_name, count]
		enemies.append(_generated_enemy_unit(
			combat_name,
			int(definition.get("hp", 1)),
			int(definition.get("mp", 0)),
			int(definition.get("speed", 0)),
			i
		))

	generated_encounter_id = encounter_id
	generated_reward_xp = maxi(0, xp_reward)
	generated_reward_gold = maxi(0, gold_reward)
	generated_encounter_active = true

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
	log.append("Generated random encounter initialized: %s (%d enemies)." % [
		generated_encounter_id if not generated_encounter_id.is_empty() else "unnamed",
		enemies.size()
	])
	return true

func _generated_enemy_unit(name: String, hp: int, mp: int, speed: int, stable_order: int) -> Dictionary:
	return {
		"name": name,
		"side": "enemy",
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

func _check_end_state() -> bool:
	if generated_encounter_active and _living_indices(enemies).is_empty():
		phase = "victory"
		_apply_generated_victory_rewards()
		return true
	return super._check_end_state()

func resolve_prime_command(command_id: String, target_index: int = -1) -> bool:
	var result := super.resolve_prime_command(command_id, target_index)
	if result and generated_encounter_active and phase == "victory":
		if not log.is_empty() and str(log.back()).begins_with("Victory. Rewards:"):
			log.pop_back()
		_apply_generated_victory_rewards()
	return result

func _apply_generated_victory_rewards() -> void:
	rewards = {"xp": generated_reward_xp, "gold": generated_reward_gold}
	log.append("Victory. Rewards: %d XP, %d gold." % [generated_reward_xp, generated_reward_gold])
