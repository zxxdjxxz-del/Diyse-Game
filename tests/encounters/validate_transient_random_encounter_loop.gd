extends SceneTree

const GameStateScript = preload("res://game/core/state/game_state.gd")
const FieldEncounterController = preload("res://game/exploration/field_encounter_controller.gd")
const GeneratedBattleState = preload("res://game/combat/generated_encounter_battle_state.gd")
const ProofEnemyCombatData = preload("res://game/content/encounters/proof_enemy_combat_data.gd")

func _initialize() -> void:
	var failures: Array[String] = []
	_validate_victory_round_trip(failures)
	_validate_flee_round_trip(failures)
	_validate_invalid_transient_payloads(failures)
	_finish(failures)

func _validate_victory_round_trip(failures: Array[String]) -> void:
	var state = GameStateScript.new()
	var field = FieldEncounterController.new(9801)
	get_root().add_child(field)
	if not field.configure_context(1, "ch01_greenhollow", 20.0):
		failures.append("Victory round-trip could not configure Greenhollow field context")
		field.queue_free()
		return

	var payload: Dictionary = field.advance_eligible_distance(7.0, [0.0], 0.0, 0.0)
	if payload.is_empty():
		failures.append("Victory round-trip did not generate a deterministic 0.35S random payload")
		field.queue_free()
		return
	if not state.queue_transient_random_encounter(payload):
		failures.append("GameState rejected a valid generated random payload")
		field.queue_free()
		return

	var definitions: Array[Dictionary] = ProofEnemyCombatData.build_units(payload.get("enemies", []))
	var battle = GeneratedBattleState.new()
	if not battle.setup_generated_formation(definitions, int(payload.get("exp", 0)), 0, str(payload.get("formation_id", ""))):
		failures.append("Generated battle state rejected the transient Greenhollow payload")
		field.queue_free()
		return

	for enemy in battle.enemies:
		enemy["hp"] = 0
	if not battle._check_end_state() or battle.phase != "victory":
		failures.append("Generated transient battle did not resolve to victory")
		field.queue_free()
		return
	if int(battle.rewards.get("xp", -1)) != int(payload.get("exp", -2)):
		failures.append("Generated transient victory did not preserve formation EXP")

	var reward_payload: Dictionary = battle.rewards.duplicate(true)
	state.rewards["xp"] = int(state.rewards.get("xp", 0)) + int(reward_payload.get("xp", 0))
	if not state.complete_transient_random_encounter("victory", reward_payload):
		failures.append("GameState could not complete transient victory")
	var returned: Dictionary = state.consume_transient_encounter_return()
	if str(returned.get("outcome", "")) != "victory":
		failures.append("Transient victory return outcome was lost")
	if str(returned.get("formation_id", "")) != str(payload.get("formation_id", "")):
		failures.append("Transient victory return lost formation anti-repeat identity")
	if int(state.rewards.get("xp", -1)) != int(payload.get("exp", -2)):
		failures.append("Transient victory reward was not applied exactly once in proof state")

	var returned_field = FieldEncounterController.new(9801)
	get_root().add_child(returned_field)
	if not returned_field.configure_context(1, "ch01_greenhollow", 20.0):
		failures.append("Returned field could not configure Greenhollow context")
	elif not returned_field.restore_after_scene_return(
		str(returned.get("outcome", "")),
		str(returned.get("formation_id", ""))
	):
		failures.append("Returned field rejected a valid victory return state")
	else:
		if absf(returned_field.pressure_fraction_s()) > 0.0001:
			failures.append("Victory scene return must reset encounter pressure")
		if returned_field.last_formation_id != str(payload.get("formation_id", "")):
			failures.append("Victory scene return must preserve immediate anti-repeat formation identity")

	returned_field.queue_free()
	field.queue_free()

func _validate_flee_round_trip(failures: Array[String]) -> void:
	var state = GameStateScript.new()
	var payload := {
		"kind": "random",
		"chapter": 1,
		"area_id": "ch01_greenhollow",
		"formation_id": "ch01_greenhollow_s01",
		"tier": "standard",
		"enemies": ["Greenhollow Stalker", "Briar Boar", "Thornvine Creeper"],
		"exp": 55
	}
	if not state.queue_transient_random_encounter(payload):
		failures.append("Flee round-trip could not queue a valid random payload")
		return
	if not state.complete_transient_random_encounter("successful_flee"):
		failures.append("Flee round-trip could not record successful flee")
		return
	var returned := state.consume_transient_encounter_return()
	var field = FieldEncounterController.new(1234)
	get_root().add_child(field)
	if not field.configure_context(1, "ch01_greenhollow", 20.0):
		failures.append("Flee round-trip could not configure returned field")
	elif not field.restore_after_scene_return(
		str(returned.get("outcome", "")),
		str(returned.get("formation_id", ""))
	):
		failures.append("Returned field rejected successful-flee state")
	else:
		if absf(field.pressure_fraction_s() - 0.65) > 0.0001:
			failures.append("Successful flee scene return must resume near 0.65S pressure")
		if not field.advance_eligible_distance(4.0, [0.0], 0.0, 0.0).is_empty():
			failures.append("Successful flee scene return did not preserve the 0.20S grace period")
		var after_grace: Dictionary = field.advance_eligible_distance(0.01, [0.0], 0.0, 0.0)
		if after_grace.is_empty():
			failures.append("Successful flee scene return did not resume checks after grace")
		elif str(after_grace.get("formation_id", "")) == str(payload.get("formation_id", "")):
			failures.append("Successful flee scene return allowed an immediate exact formation repeat")
	field.queue_free()

func _validate_invalid_transient_payloads(failures: Array[String]) -> void:
	var state = GameStateScript.new()
	if state.queue_transient_random_encounter({"kind": "authored", "formation_id": "bad", "enemies": ["x"]}):
		failures.append("Transient handoff accepted a non-random payload")
	if state.queue_transient_random_encounter({"kind": "random", "formation_id": "", "enemies": ["x"]}):
		failures.append("Transient handoff accepted an empty formation ID")
	if state.queue_transient_random_encounter({"kind": "random", "formation_id": "bad", "enemies": []}):
		failures.append("Transient handoff accepted an empty enemy list")
	if state.complete_transient_random_encounter("victory"):
		failures.append("Transient handoff completed a battle when none was queued")

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Audit98 transient field-combat-field random encounter loop validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
