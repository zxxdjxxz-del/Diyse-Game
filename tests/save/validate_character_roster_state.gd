extends SceneTree

const GameStateScript = preload("res://game/core/state/game_state.gd")

var failures: Array[String] = []

func _initialize() -> void:
	_test_default_permanent_roster()
	_test_recruitment_and_active_party_rules()
	_test_proof_party_is_not_roster_authority()
	_finish()

func _test_default_permanent_roster() -> void:
	var state = GameStateScript.new()
	var expected_ids := ["cyanis", "ilyra", "torren", "nimera", "vaelira", "seyrik"]
	_expect(GameStateScript.PERMANENT_CHARACTER_IDS == expected_ids, "Permanent character stable-ID set/order must match the current six")
	_expect(state.character_roster.size() == 6, "Production roster must contain exactly the six permanent character records")
	_expect(state.recruited_character_ids() == ["cyanis"], "New production roster must begin with Cyanis as the only recruited permanent character")
	_expect(state.active_party_character_ids() == ["cyanis"], "New production active party must begin with Cyanis only")

	var expected_names := {
		"cyanis": "Cyanis",
		"ilyra": "Ilyra",
		"torren": "Torren",
		"nimera": "Nimera",
		"vaelira": "Vaelira",
		"seyrik": "Seyrik"
	}
	for character_id in expected_ids:
		_expect(state.is_permanent_character_id(character_id), "%s must be recognized as a permanent character ID" % character_id)
		var record := state.character_record(character_id)
		_expect(str(record.get("character_id", "")) == character_id, "%s record must retain its stable character ID" % character_id)
		_expect(str(record.get("display_name", "")) == str(expected_names[character_id]), "%s display identity must use the current first-name-only name" % character_id)
		_expect(record.get("persistent_state", null) is Dictionary, "%s must expose the reserved persistent-state envelope" % character_id)

	_expect(not state.is_permanent_character_id("maevra"), "Maevra must not be added to the permanent six by the roster model")
	_expect(not state.is_permanent_character_id("kessara"), "Kessara must not be added to the permanent six by the roster model")
	_expect(state.character_record("unknown").is_empty(), "Unknown character IDs must not create roster records")

func _test_recruitment_and_active_party_rules() -> void:
	var state = GameStateScript.new()
	_expect(not state.set_active_party(["cyanis", "ilyra"]), "An unrecruited character must not enter the active party")
	_expect(state.active_party_character_ids() == ["cyanis"], "Rejected active-party changes must leave the prior formation intact")

	for character_id in ["ilyra", "torren", "nimera"]:
		_expect(state.recruit_character(character_id), "%s should be recruitable into the permanent roster" % character_id)
	_expect(state.recruited_character_ids() == ["cyanis", "ilyra", "torren", "nimera"], "Recruitment order must follow stable permanent-character order")
	_expect(not state.recruit_character("nimera"), "Recruiting an already recruited character must be a no-op failure")
	_expect(state.set_active_party(["cyanis", "ilyra", "torren", "nimera"]), "Four recruited permanent characters must form a legal active party")
	_expect(state.active_party_character_ids() == ["cyanis", "ilyra", "torren", "nimera"], "Legal four-character active party must be retained")

	_expect(not state.set_active_party(["cyanis", "cyanis"]), "Duplicate stable character IDs must be rejected")
	_expect(state.active_party_character_ids() == ["cyanis", "ilyra", "torren", "nimera"], "Duplicate rejection must not mutate the current party")
	_expect(not state.set_active_party(["cyanis", "ilyra", "torren", "nimera", "vaelira"]), "Active party must never exceed four")
	_expect(not state.set_active_party([]), "Persistent active party must not be empty")
	_expect(not state.set_active_party(["cyanis", "unknown"]), "Unknown IDs must be rejected from active party")
	_expect(not state.set_active_party(["cyanis", "vaelira"]), "Unrecruited Vaelira must remain ineligible for active party")

	_expect(state.recruit_character("vaelira"), "Vaelira should become eligible after recruitment")
	_expect(state.recruit_character("seyrik"), "Seyrik should become eligible after recruitment")
	_expect(state.set_active_party(["vaelira", "seyrik", "cyanis", "nimera"]), "Any four recruited permanent characters must be a legal active party")
	_expect(state.active_party_character_ids() == ["vaelira", "seyrik", "cyanis", "nimera"], "Active-party order must preserve the caller-selected formation order")

func _test_proof_party_is_not_roster_authority() -> void:
	var state = GameStateScript.new()
	_expect(state.party.size() == 4, "Legacy proof battle fixture must remain intact during the roster migration")
	_expect(state.character_roster.size() == 6, "Production roster must exist independently of the four-member proof fixture")
	_expect(state.recruited_character_ids() == ["cyanis"], "Proof fixture membership must not imply production recruitment")
	state.party[0]["name"] = "Proof Fixture Mutation"
	_expect(state.character_display_name("cyanis") == "Cyanis", "Mutating proof-party display data must not alter production character identity")

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _finish() -> void:
	if failures.is_empty():
		print("Diyse production permanent-roster and active-party state validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
