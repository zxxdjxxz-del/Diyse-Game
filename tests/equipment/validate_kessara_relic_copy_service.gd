extends SceneTree

const GameStateScript = preload("res://game/core/state/game_state.gd")
const KessaraServiceScript = preload("res://game/equipment/kessara_relic_copy_service.gd")

var failures: Array[String] = []

func _initialize() -> void:
	_test_original_and_matching_component_are_required()
	_test_successful_copy_preserves_single_relic_identity()
	_test_wrong_face_component_cannot_be_consumed()
	_test_individual_relic_copy_limit()
	_test_face_component_and_copy_limits()
	_test_legacy_registration_is_rejected()
	_finish()

func _test_original_and_matching_component_are_required() -> void:
	var state = GameStateScript.new()
	var service = KessaraServiceScript.new()
	var missing := service.evaluate(state, "RELIC_PROOF_MIGHT")
	_expect(not bool(missing.get("ok", false)), "Unobtained Relic must not be copyable")
	_expect(str(missing.get("code", "")) == KessaraServiceScript.RESULT_RELIC_NOT_OBTAINED, "Unobtained Relic should return the explicit ownership failure")

	_expect(state.register_relic_original("RELIC_PROOF_MIGHT", "might"), "Relic original should register with canonicalized Face")
	_expect(state.relic_face("RELIC_PROOF_MIGHT") == "Might", "Relic Face should canonicalize to Might")
	var no_component := service.evaluate(state, "RELIC_PROOF_MIGHT")
	_expect(str(no_component.get("code", "")) == KessaraServiceScript.RESULT_NO_MATCHING_COMPONENT, "Obtained Relic without matching copy component must be rejected")

func _test_successful_copy_preserves_single_relic_identity() -> void:
	var state = GameStateScript.new()
	var service = KessaraServiceScript.new()
	_expect(state.register_relic_original("RELIC_PROOF_FIRST_MEASURE", "Might"), "Proof Relic should register")
	_expect(state.register_relic_copy_component("FORGE_PROOF_GRACE_COPY_1", "Grace"), "Nonmatching proof component should register independently")
	_expect(state.register_relic_copy_component("FORGE_PROOF_MIGHT_COPY_1", "Might"), "Matching proof component should register")

	var result := service.forge_copy(state, "RELIC_PROOF_FIRST_MEASURE")
	_expect(bool(result.get("ok", false)), "Kessara should forge a copy when original and matching component exist")
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
	_expect(not state.commit_relic_copy("RELIC_PROOF_GRACE", "FORGE_PROOF_MIGHT_ONLY"), "Direct commit must reject a wrong-Face component")
	_expect(state.relic_quantity("RELIC_PROOF_GRACE") == 1, "Wrong-Face commit must not change Relic quantity")
	_expect(not bool(state.forge_components["FORGE_PROOF_MIGHT_ONLY"].get("consumed", false)), "Wrong-Face component must not be consumed")

func _test_individual_relic_copy_limit() -> void:
	var state = GameStateScript.new()
	var service = KessaraServiceScript.new()
	_expect(state.register_relic_original("RELIC_PROOF_CHANGE", "Change"), "Change Relic should register")
	_expect(state.register_relic_copy_component("FORGE_PROOF_CHANGE_1", "Change"), "First Change component should register")
	_expect(state.register_relic_copy_component("FORGE_PROOF_CHANGE_2", "Change"), "Second Change component should register")
	_expect(bool(service.forge_copy(state, "RELIC_PROOF_CHANGE").get("ok", false)), "First copy should succeed")
	var second_attempt := service.forge_copy(state, "RELIC_PROOF_CHANGE")
	_expect(not bool(second_attempt.get("ok", false)), "Same Relic must not be copied twice")
	_expect(str(second_attempt.get("code", "")) == KessaraServiceScript.RESULT_ALREADY_COPIED, "Second copy attempt should report individual Relic limit")
	_expect(state.relic_quantity("RELIC_PROOF_CHANGE") == 2, "Individual Relic quantity must remain capped at two")
	_expect(state.available_relic_copy_component_for_face("Change") == "FORGE_PROOF_CHANGE_2", "Unused same-Face component must remain available for another Relic")

func _test_face_component_and_copy_limits() -> void:
	var state = GameStateScript.new()
	var service = KessaraServiceScript.new()
	for index in range(1, 5):
		_expect(state.register_relic_original("RELIC_PROOF_ACUITY_%d" % index, "Acuity"), "Acuity proof Relic %d should register" % index)
	for index in range(1, 4):
		_expect(state.register_relic_copy_component("FORGE_PROOF_ACUITY_%d" % index, "Acuity"), "Acuity copy component %d should register" % index)
	_expect(not state.register_relic_copy_component("FORGE_PROOF_ACUITY_4", "Acuity"), "A fourth Relic-copy component for one Face must be rejected")
	for index in range(1, 4):
		_expect(bool(service.forge_copy(state, "RELIC_PROOF_ACUITY_%d" % index).get("ok", false)), "Acuity Relic %d should consume one of the three Face copy opportunities" % index)
	var fourth := service.evaluate(state, "RELIC_PROOF_ACUITY_4")
	_expect(not bool(fourth.get("ok", false)), "A fourth forged Relic from one Face must be rejected")
	_expect(str(fourth.get("code", "")) == KessaraServiceScript.RESULT_FACE_COPY_LIMIT, "Fourth same-Face Relic copy should report Face-wide limit")
	_expect(state.forged_relic_count_for_face("Acuity") == 3, "Exactly three Relics may be forged for one Face")

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
		print("Diyse Kessara Relic-copy service validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
