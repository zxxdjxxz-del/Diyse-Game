extends SceneTree

const GameStateScript = preload("res://game/core/state/game_state.gd")
const SaveManagerScript = preload("res://game/core/save/save_manager.gd")
const TEST_PATH := "user://diyse_7b5g_test_save.json"

var failures: Array[String] = []

func _initialize() -> void:
	_test_missing_save_is_safe()
	_test_full_state_round_trip()
	_test_pre_kessara_schema_v1_save_is_compatible()
	_test_invalid_json_is_safe()
	_test_future_schema_is_rejected()
	_cleanup()
	_finish()

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _cleanup() -> void:
	if FileAccess.file_exists(TEST_PATH):
		DirAccess.remove_absolute(ProjectSettings.globalize_path(TEST_PATH))

func _test_missing_save_is_safe() -> void:
	_cleanup()
	var manager = SaveManagerScript.new()
	var state = GameStateScript.new()
	var result: Dictionary = manager.load_state(state, TEST_PATH)
	_expect(not bool(result.get("ok", false)), "Missing save must return a safe failure")
	_expect("No save file" in str(result.get("message", "")), "Missing save failure should explain that no save exists")

func _test_full_state_round_trip() -> void:
	_cleanup()
	var manager = SaveManagerScript.new()
	var source = GameStateScript.new()
	source.current_area = "field_proof"
	source.field_position = Vector3(6.25, 0.9, -3.5)
	source.party[0]["hp"] = 31
	source.party[0]["mp"] = 7
	source.party[1]["hp"] = 22
	source.inventory["Potion"] = 1
	source.standard_cards = ["proof_might_strike", "proof_second_card"]
	source.primes["first_champion"]["progression_state"] = "Awakened"
	source.primes["first_champion"]["available_battle_use_baseline"] = 1
	source.equipment["Cyanis"]["weapon"] = "Saved Proof Blade"
	_expect(source.register_relic_original("RELIC_SAVE_PROOF_MIGHT", "Might"), "Save test Relic should register")
	_expect(source.register_relic_copy_component("FORGE_SAVE_PROOF_MIGHT_1", "Might"), "Save test matching copy component should register")
	_expect(source.register_relic_copy_component("FORGE_SAVE_PROOF_GRACE_1", "Grace"), "Save test unused copy component should register")
	_expect(source.commit_relic_copy("RELIC_SAVE_PROOF_MIGHT", "FORGE_SAVE_PROOF_MIGHT_1"), "Save test Relic copy should commit before serialization")
	source.flags["proof_story_flag"] = true
	source.flags["proof_chest_opened"] = true
	source.flags["torren_state"] = "prepared"
	source.rewards = {"xp": 123, "gold": 456}
	_expect(source.queue_transient_random_encounter({
		"kind": "random",
		"chapter": 1,
		"area_id": "ch01_greenhollow",
		"formation_id": "save_exclusion_test",
		"tier": "light",
		"enemies": ["Greenhollow Stalker"],
		"exp": 45
	}), "Transient random encounter should queue for save-exclusion test")

	var save_result: Dictionary = manager.save_state(source, TEST_PATH)
	_expect(bool(save_result.get("ok", false)), "Versioned save must write successfully")
	_expect(FileAccess.file_exists(TEST_PATH), "Save manager must create the user:// JSON file")
	var raw_saved: Dictionary = manager.read_save_data(TEST_PATH).get("data", {})
	_expect(not raw_saved.has("transient_encounter"), "Runtime random encounter payload must not be serialized")
	_expect(not raw_saved.has("transient_encounter_return"), "Runtime encounter return state must not be serialized")
	_expect(raw_saved.has("relic_inventory") and raw_saved.has("forge_components"), "Relic and Forge-component ownership must be serialized")

	var fresh_manager = SaveManagerScript.new()
	var restored = GameStateScript.new()
	_expect(restored.queue_transient_random_encounter({
		"kind": "random",
		"formation_id": "stale_before_load",
		"enemies": ["Greenhollow Stalker"]
	}), "Restored-state stale transient setup should succeed before load")
	var load_result: Dictionary = fresh_manager.load_state(restored, TEST_PATH)
	_expect(bool(load_result.get("ok", false)), "A fresh save-manager instance must reload the saved file")
	_expect(restored.current_area == source.current_area, "Current area must round-trip")
	_expect(restored.field_position.is_equal_approx(source.field_position), "Vector3 field position must round-trip exactly enough for field restoration")
	_expect(int(restored.party[0]["hp"]) == 31 and int(restored.party[0]["mp"]) == 7, "Party HP/MP must round-trip")
	_expect(int(restored.party[1]["hp"]) == 22, "Multiple party records must round-trip")
	_expect(int(restored.inventory.get("Potion", -1)) == 1, "Inventory must round-trip")
	_expect(restored.standard_cards == ["proof_might_strike", "proof_second_card"], "Standard Card acquisition list must round-trip")
	_expect(str(restored.primes["first_champion"]["progression_state"]) == "Awakened", "Prime ownership/progression state must round-trip")
	_expect(str(restored.equipment["Cyanis"]["weapon"]) == "Saved Proof Blade", "Equipment placeholders must round-trip")
	_expect(restored.relic_quantity("RELIC_SAVE_PROOF_MIGHT") == 2, "Forged Relic quantity must round-trip")
	_expect(restored.has_forged_relic_copy("RELIC_SAVE_PROOF_MIGHT"), "Forged-copy marker must round-trip")
	_expect(bool(restored.forge_components["FORGE_SAVE_PROOF_MIGHT_1"].get("consumed", false)), "Consumed Relic-copy component must round-trip")
	_expect(not bool(restored.forge_components["FORGE_SAVE_PROOF_GRACE_1"].get("consumed", false)), "Unused Relic-copy component must remain unused after load")
	_expect(bool(restored.flags.get("proof_story_flag", false)), "Story flag must round-trip")
	_expect(bool(restored.flags.get("proof_chest_opened", false)), "Opened interactable flag must round-trip")
	_expect(str(restored.flags.get("torren_state", "")) == "prepared", "NPC state must round-trip")
	_expect(int(restored.rewards.get("xp", -1)) == 123 and int(restored.rewards.get("gold", -1)) == 456, "Rewards/currency must round-trip")
	_expect(not restored.has_transient_random_encounter(), "Loading a disk save must clear stale transient encounter state")
	_expect(restored.transient_encounter_return.is_empty(), "Loading a disk save must clear stale transient encounter-return state")
	var data: Dictionary = load_result.get("data", {})
	_expect(int(data.get("schema_version", -1)) == SaveManagerScript.SCHEMA_VERSION, "Save data must carry the current schema version")

func _test_pre_kessara_schema_v1_save_is_compatible() -> void:
	_cleanup()
	var legacy_data := {
		"schema_version": SaveManagerScript.SCHEMA_VERSION,
		"area": "field_proof",
		"field_position": {"x": 1.0, "y": 0.9, "z": 2.0},
		"party": [],
		"inventory": {"Potion": 2},
		"standard_cards": [],
		"primes": {},
		"equipment": {},
		"flags": {"legacy_schema_v1": true},
		"rewards": {"xp": 0, "gold": 0}
	}
	var file := FileAccess.open(TEST_PATH, FileAccess.WRITE)
	file.store_string(JSON.stringify(legacy_data))
	file.flush()
	var manager = SaveManagerScript.new()
	var state = GameStateScript.new()
	var result: Dictionary = manager.load_state(state, TEST_PATH)
	_expect(bool(result.get("ok", false)), "Schema-v1 save written before Kessara fields existed must remain loadable")
	_expect(state.relic_inventory.is_empty(), "Pre-Kessara schema-v1 save should default Relic ownership empty")
	_expect(state.forge_components.is_empty(), "Pre-Kessara schema-v1 save should default Forge-component ownership empty")
	_expect(bool(state.flags.get("legacy_schema_v1", false)), "Pre-Kessara schema-v1 save should preserve its existing state")

func _test_invalid_json_is_safe() -> void:
	var file := FileAccess.open(TEST_PATH, FileAccess.WRITE)
	file.store_string("{ this is deliberately invalid json")
	file.flush()
	var manager = SaveManagerScript.new()
	var state = GameStateScript.new()
	var result: Dictionary = manager.load_state(state, TEST_PATH)
	_expect(not bool(result.get("ok", false)), "Invalid JSON must fail safely")
	_expect("corrupt" in str(result.get("message", "")).to_lower(), "Invalid JSON should be identified as corrupt")

func _test_future_schema_is_rejected() -> void:
	var file := FileAccess.open(TEST_PATH, FileAccess.WRITE)
	file.store_string(JSON.stringify({"schema_version": SaveManagerScript.SCHEMA_VERSION + 99, "area": "field_proof", "field_position": {"x": 0, "y": 0.9, "z": 0}}))
	file.flush()
	var manager = SaveManagerScript.new()
	var state = GameStateScript.new()
	var result: Dictionary = manager.load_state(state, TEST_PATH)
	_expect(not bool(result.get("ok", false)), "Unsupported future schema must be rejected safely")
	_expect("Unsupported save schema" in str(result.get("message", "")), "Future schema rejection should be explicit")

func _finish() -> void:
	if failures.is_empty():
		print("Diyse 7B.5G versioned save/load persistence validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)