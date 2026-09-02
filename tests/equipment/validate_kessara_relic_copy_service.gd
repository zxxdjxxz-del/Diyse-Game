extends SceneTree

const GameStateScript = preload("res://game/core/state/game_state.gd")
const KessaraServiceScript = preload("res://game/equipment/kessara_relic_copy_service.gd")

var failures: Array[String] = []

func _initialize() -> void:
	_test_original_and_matching_component_are_required()
	_test_insufficient_g_is_nonmutating()
	_test_successful_copy_preserves_identity_and_charges_exact_fee()
	_test_wrong_face_component_cannot_be_consumed()
	_test_individual_relic_copy_limit()
	_test_face_component_and_copy_limits()
	_test_retired_face_aliases_migrate_to_current()
	_test_legacy_registration_is_rejected()
	_finish()

func _fund_for_copies(state, copy_count: int) -> void:
	_expect(state.credit_g(KessaraServiceScript.SERVICE_FEE_G * maxi(copy_count, 0)), "Test wallet funding should succeed")

func _test_original_and_matching_component_are_required() -> void:
	var state = GameStateScript.new()
	var service = KessaraServiceScript.new()
	var missing := service.evaluate(state, "RELIC_PROOF_MIGHT")
	_expect(not bool(missing.get("ok", false)), "Unobtained Relic must not be copyable")
	_expect(str(missing.get("code", "")) == KessaraServiceScript.RESULT_RELIC_NOT_OBTAINED, "Unobtained Relic should return the explicit ownership failure")

	_expect(state.register_relic_original("RELIC_PROOF_MIGHT", "might"), "Relic original should register with canonicalized Face")
	_expect(state.relic_face("RELIC_PROOF_MIGHT") == "Might", "Relic Face should canonicalize to Might")
	var no_component := service.evaluate(state, "RELIC_PROOF_MIGHT")
	_expect(str(no_component.get("code", "")) == KessaraServiceScript.RESULT_NO_MATCHING_COMPONENT, "Obtained Relic without matching copy component must be rejected before wallet eligibility")

func _test_insufficient_g_is_nonmutating() -> void:
	var state = GameStateScript.new()
	var service = KessaraServiceScript.new()
	_expect(state.wallet_balance_g() == GameStateScript.STARTING_WALLET_G, "New game wallet must begin at the current 2,500 G authority")
	_expect(state.register_relic_original("RELIC_PROOF_UNFUNDED", "Might"), "Unfunded test Relic should register")
	_expect(state.register_relic_copy_component("FORGE_PROOF_UNFUNDED", "Might"), "Unfunded matching component should register")
	var wallet_before := state.wallet_balance_g()
	var result := service.forge_copy(state, "RELIC_PROOF_UNFUNDED")
	_expect(not bool(result.get("ok", false)), "Relic copy must fail when the wallet cannot cover 6,000 G")
	_expect(str(result.get("code", "")) == KessaraServiceScript.RESULT_INSUFFICIENT_G, "Insufficient wallet must return explicit insufficient_g failure")
	_expect(state.wallet_balance_g() == wallet_before, "Failed Relic copy must charge 0 G")
	_expect(state.relic_quantity("RELIC_PROOF_UNFUNDED") == 1, "Failed Relic copy must not create a duplicate")
	_expect(not bool(state.forge_components["FORGE_PROOF_UNFUNDED"].get("consumed", false)), "Failed Relic copy must not consume the component")

func _test_successful_copy_preserves_identity_and_charges_exact_fee() -> void:
	var state = GameStateScript.new()
	var service = KessaraServiceScript.new()
	_fund_for_copies(state, 1)
	_expect(state.register_relic_original("RELIC_PROOF_FIRST_MEASURE", "Might"), "Proof Relic should register")
	_expect(state.register_relic_copy_component("FORGE_PROOF_GRACE_COPY_1", "Grace"), "Nonmatching proof component should register independently")
	_expect(state.register_relic_copy_component("FORGE_PROOF_MIGHT_COPY_1", "Might"), "Matching proof component should register")
	var wallet_before := state.wallet_balance_g()

	var result := service.forge_copy(state, "RELIC_PROOF_FIRST_MEASURE")
	_expect(bool(result.get("ok", false)), "Kessara should forge a copy when original, matching component, and sufficient G exist")
	_expect(int(result.get("fee_g", -1)) == 6000, "Successful result must report the exact 6,000 G fee")
	_expect(state.wallet_balance_g() == wallet_before - 6000, "Successful forge must deduct exactly 6,000 G")
	_expect(str(result.get("component_id", "")) == "FORGE_PROOF_MIGHT_COPY_1", "Kessara must consume the matching-Face component, not another Face")
	_expect(state.relic_quantity("RELIC_PROOF_FIRST_MEASURE") == 2, "Forged Relic maximum quantity should become exactly two")
	_expect(state.has_forged_relic_copy("RELIC_PROOF_FIRST_MEASURE"), "Relic record should mark the forged copy")
	_expect(state.relic_inventory.size() == 1, "Forging must not create a second Relic definition or copy ID")
	_expect(bool(state.forge_components["FORGE_PROOF_MIGHT_COPY_1"].get("consumed", false)), "Matching copy component must be consumed")
	_expect(not bool(state.forge_components["FORGE_PROOF_GRACE_COPY_1"].get("consumed", false)), "Nonmatching Face component must remain untouched")

func _test_wrong_face_component_cannot_be_consumed() -> void:
	var state = GameStateScript.new()
	_expect(state.register_relic_original("RELIC_PROOF_GRACE", "Grace"), "Grace Relic should register")
	_expect(state.register_relic_copy_component("FORGE_PROOF_MIGHT_ONLY", "Might"), "Might component should register")
	_expect(not state.commit_relic_copy("RELIC_PROOF_GRACE", "FORGE_PROOF_MIGHT_ONLY"), "Low-level ownership commit must reject a wrong-Face component")
	_expect(state.relic_quantity("RELIC_PROOF_GRACE") == 1, "Wrong-Face commit must not change Relic quantity")
	_expect(not bool(state.forge_components["FORGE_PROOF_MIGHT_ONLY"].get("consumed", false)), "Wrong-Face component must not be consumed")

func _test_individual_relic_copy_limit() -> void:
	var state = GameStateScript.new()
	var service = KessaraServiceScript.new()
	_fund_for_copies(state, 1)
	_expect(state.register_relic_original("RELIC_PROOF_MEMORY", "Memory"), "Memory Relic should register")
	_expect(state.register_relic_copy_component("FORGE_PROOF_MEMORY_1", "Memory"), "First Memory component should register")
	_expect(state.register_relic_copy_component("FORGE_PROOF_MEMORY_2", "Memory"), "Second Memory component should register")
	_expect(bool(service.forge_copy(state, "RELIC_PROOF_MEMORY").get("ok", false)), "First copy should succeed")
	var wallet_after_first := state.wallet_balance_g()
	var second_attempt := service.forge_copy(state, "RELIC_PROOF_MEMORY")
	_expect(not bool(second_attempt.get("ok", false)), "Same Relic must not be copied twice")
	_expect(str(second_attempt.get("code", "")) == KessaraServiceScript.RESULT_ALREADY_COPIED, "Second copy attempt should report individual Relic limit before any new fee")
	_expect(state.wallet_balance_g() == wallet_after_first, "Invalid second copy attempt must charge 0 G")
	_expect(state.relic_quantity("RELIC_PROOF_MEMORY") == 2, "Individual Relic quantity must remain capped at two")
	_expect(state.available_relic_copy_component_for_face("Memory") == "FORGE_PROOF_MEMORY_2", "Unused same-Face component must remain available for another Relic")

func _test_face_component_and_copy_limits() -> void:
	var state = GameStateScript.new()
	var service = KessaraServiceScript.new()
	_fund_for_copies(state, 3)
	for index in range(1, 5):
		_expect(state.register_relic_original("RELIC_PROOF_PERCEPTION_%d" % index, "Perception"), "Perception proof Relic %d should register" % index)
	for index in range(1, 4):
		_expect(state.register_relic_copy_component("FORGE_PROOF_PERCEPTION_%d" % index, "Perception"), "Perception copy component %d should register" % index)
	_expect(not state.register_relic_copy_component("FORGE_PROOF_PERCEPTION_4", "Perception"), "A fourth Relic-copy component for one Face must be rejected")
	for index in range(1, 4):
		_expect(bool(service.forge_copy(state, "RELIC_PROOF_PERCEPTION_%d" % index).get("ok", false)), "Perception Relic %d should consume one of the three Face copy opportunities" % index)
	var wallet_after_three := state.wallet_balance_g()
	var fourth := service.evaluate(state, "RELIC_PROOF_PERCEPTION_4")
	_expect(not bool(fourth.get("ok", false)), "A fourth forged Relic from one Face must be rejected")
	_expect(str(fourth.get("code", "")) == KessaraServiceScript.RESULT_FACE_COPY_LIMIT, "Fourth same-Face Relic copy should report Face-wide limit")
	_expect(state.wallet_balance_g() == wallet_after_three, "Face-limit rejection must not charge additional G")
	_expect(state.forged_relic_count_for_face("Perception") == 3, "Exactly three Relics may be forged for one Face")

func _test_retired_face_aliases_migrate_to_current() -> void:
	var state = GameStateScript.new()
	_expect(state.register_relic_original("RELIC_LEGACY_FACE_CHANGE", "Change"), "Retired Change label should remain load/data compatible")
	_expect(state.relic_face("RELIC_LEGACY_FACE_CHANGE") == "Memory", "Retired Change Face must canonicalize to Memory")
	_expect(state.register_relic_original("RELIC_LEGACY_FACE_ACUITY", "Acuity"), "Retired Acuity label should remain load/data compatible")
	_expect(state.relic_face("RELIC_LEGACY_FACE_ACUITY") == "Perception", "Retired Acuity Face must canonicalize to Perception")
	_expect(state.register_relic_original("RELIC_LEGACY_FACE_RESOURCE", "Resource"), "Retired Resource label should remain load/data compatible")
	_expect(state.relic_face("RELIC_LEGACY_FACE_RESOURCE") == "Perception", "Retired Resource Face must canonicalize to Perception")

func _test_legacy_registration_is_rejected() -> void:
	var state = GameStateScript.new()
	var service = KessaraServiceScript.new()
	_expect(not state.register_relic_original("LEGACY_PROOF_WEAPON", "Might"), "Legacy-prefixed equipment must not enter the Relic registration path")
	var result := service.evaluate(state, "LEGACY_PROOF_WEAPON")
	_expect(str(result.get("code", "")) == KessaraServiceScript.RESULT_RELIC_NOT_OBTAINED, "Kessara must not copy a Legacy through the Relic service")

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse Kessara Relic-copy service + 6,000 G transaction validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
