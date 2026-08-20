extends SceneTree

const BaseBattleState = preload("res://game/combat/battle_state.gd")
const GeneratedBattleState = preload("res://game/combat/generated_encounter_battle_state.gd")
const ProofEnemyData = preload("res://game/content/encounters/proof_enemy_combat_data.gd")
const Catalog = preload("res://game/content/encounters/chapter_01_04_formations.gd")

func _initialize() -> void:
	var failures: Array[String] = []
	_validate_greenhollow_coverage(failures)
	_validate_generated_setup_and_rewards(failures)
	_validate_enemy_cap_and_invalid_data(failures)
	_validate_base_demo_regression(failures)
	_finish(failures)

func _validate_greenhollow_coverage(failures: Array[String]) -> void:
	for tier in ["light", "standard", "heavy"]:
		var formations: Array = Catalog.formations_for_area_tier("ch01_greenhollow", tier)
		if formations.is_empty():
			failures.append("Greenhollow %s formation pool is unexpectedly empty" % tier)
			continue
		for formation in formations:
			var units := ProofEnemyData.build_units(formation.get("enemies", []))
			if units.size() != formation.get("enemies", []).size():
				failures.append("Proof combat data does not cover %s" % str(formation.get("id", "unknown")))

	if not ProofEnemyData.definition_for("Definitely Not An Enemy").is_empty():
		failures.append("Proof combat data accepted an unknown enemy identity")
	if not ProofEnemyData.build_units(["Greenhollow Stalker", "Definitely Not An Enemy"]).is_empty():
		failures.append("Proof combat data returned a partial unit list for an unsupported formation")

func _validate_generated_setup_and_rewards(failures: Array[String]) -> void:
	var formation: Dictionary = Catalog.formations_for_area_tier("ch01_greenhollow", "heavy")[0]
	var units := ProofEnemyData.build_units(formation.get("enemies", []))
	var battle = GeneratedBattleState.new()
	if not battle.setup_generated_formation(units, int(formation.get("exp", 0)), 0, str(formation.get("id", ""))):
		failures.append("Generated battle state rejected a valid Greenhollow Heavy formation")
		return
	if battle.party.size() != 4:
		failures.append("Generated setup did not preserve the accepted four-member proof party")
	if battle.enemies.size() != formation.get("enemies", []).size():
		failures.append("Generated setup changed the formation enemy count")
	if battle.enemies.size() > 8:
		failures.append("Generated setup exceeded the Audit98 eight-active-enemy cap")
	if battle.phase != "selecting":
		failures.append("Generated setup did not enter the normal round-selection phase")
	if int(battle.rewards.get("xp", -1)) != 0:
		failures.append("Generated encounter paid rewards before victory")
	if str(battle.generated_encounter_id) != str(formation.get("id", "")):
		failures.append("Generated encounter ID was not retained")

	for enemy in battle.enemies:
		enemy["hp"] = 0
	if not battle._check_end_state():
		failures.append("Generated battle did not recognize all-enemies-defeated victory")
	if battle.phase != "victory":
		failures.append("Generated battle did not enter victory phase")
	if int(battle.rewards.get("xp", 0)) != int(formation.get("exp", 0)):
		failures.append("Generated battle did not preserve the formation EXP reward")
	if int(battle.rewards.get("gold", -1)) != 0:
		failures.append("Generated proof encounter invented a gold reward")

func _validate_enemy_cap_and_invalid_data(failures: Array[String]) -> void:
	var base_def := ProofEnemyData.definition_for("Thornvine Creeper")
	var eight: Array[Dictionary] = []
	for _i in range(8):
		eight.append(base_def.duplicate(true))
	var battle = GeneratedBattleState.new()
	if not battle.setup_generated_formation(eight, 1, 0, "eight_enemy_cap_proof"):
		failures.append("Generated battle rejected exactly eight active enemies")
	if battle.enemies.size() != 8:
		failures.append("Generated battle did not preserve exactly eight active enemies")

	var nine: Array[Dictionary] = eight.duplicate(true)
	nine.append(base_def.duplicate(true))
	var over_cap = GeneratedBattleState.new()
	if over_cap.setup_generated_formation(nine, 1):
		failures.append("Generated battle accepted more than eight active enemies")

	var invalid = GeneratedBattleState.new()
	if invalid.setup_generated_formation([{"display_name": "Broken", "hp": 0, "speed": 1}], 1):
		failures.append("Generated battle accepted a nonpositive-HP enemy definition")

func _validate_base_demo_regression(failures: Array[String]) -> void:
	var battle = BaseBattleState.new()
	battle.setup_demo()
	if battle.enemies.size() != 3:
		failures.append("Existing setup_demo regression path no longer has its three proof enemies")
	for enemy in battle.enemies:
		enemy["hp"] = 0
	if not battle._check_end_state():
		failures.append("Existing setup_demo path no longer resolves victory")
	if int(battle.rewards.get("xp", 0)) != 30 or int(battle.rewards.get("gold", 0)) != 42:
		failures.append("Existing setup_demo 30 XP / 42 gold regression reward changed")

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Audit98 generated random-encounter battle-state validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
