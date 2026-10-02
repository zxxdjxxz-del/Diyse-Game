extends SceneTree

# Runtime-structure regression only.
# This suite intentionally does not certify encounter rosters, formation composition,
# EXP/CEXP totals, chapter encounter counts, or Chapter 3/4 content authority.
# Current encounter content remains owned by docs/09 and progression values by docs/10.

const Balance = preload("res://game/exploration/encounter_balance.gd")
const Pressure = preload("res://game/exploration/encounter_pressure.gd")
const Selector = preload("res://game/exploration/encounter_selector.gd")
const Catalog = preload("res://game/content/encounters/chapter_01_04_formations.gd")

func _initialize() -> void:
	var failures: Array[String] = []
	_validate_balance_profile_structure(failures)
	_validate_catalog_structure(failures)
	_validate_pressure_state_machine(failures)
	_validate_selector_contract(failures)
	_finish(failures)

func _validate_balance_profile_structure(failures: Array[String]) -> void:
	if Balance.CHAPTER_PROFILES.is_empty():
		failures.append("Encounter balance must expose at least one runtime chapter profile")
		return
	for chapter_value in Balance.CHAPTER_PROFILES.keys():
		var chapter := int(chapter_value)
		for failure in Balance.validate_profile(chapter):
			failures.append("Chapter %d profile: %s" % [chapter, str(failure)])
		var profile: Dictionary = Balance.profile_for_chapter(chapter)
		if profile.is_empty():
			failures.append("Chapter %d profile could not be read back" % chapter)
			continue
		for tier in Catalog.TIER_NAMES:
			if not profile.get("tier_weights", {}).has(tier):
				failures.append("Chapter %d profile is missing tier weight %s" % [chapter, tier])
			if not profile.get("exp_anchors", {}).has(tier):
				failures.append("Chapter %d profile is missing runtime EXP anchor %s" % [chapter, tier])

func _validate_catalog_structure(failures: Array[String]) -> void:
	var seen_ids := {}
	var area_ids := Catalog.area_ids()
	if area_ids.is_empty():
		failures.append("Encounter catalog must expose at least one runtime area")
		return

	for area_id in area_ids:
		var chapter := Catalog.chapter_for_area(area_id)
		if chapter <= 0:
			failures.append("%s has no valid chapter owner" % area_id)
		var max_enemies := Catalog.max_enemies_for_area(area_id)
		if max_enemies <= 0 or max_enemies > Balance.MAX_ACTIVE_ENEMIES:
			failures.append("%s has invalid runtime enemy cap %d" % [area_id, max_enemies])

		for tier in Catalog.TIER_NAMES:
			var formations: Array = Catalog.formations_for_area_tier(area_id, tier)
			if formations.is_empty():
				failures.append("%s %s pool is empty" % [area_id, tier])
				continue

			var total_weight := 0.0
			for formation in formations:
				var formation_id := str(formation.get("id", ""))
				if formation_id.is_empty():
					failures.append("%s %s contains a formation without an ID" % [area_id, tier])
				elif seen_ids.has(formation_id):
					failures.append("Duplicate runtime formation ID: %s" % formation_id)
				else:
					seen_ids[formation_id] = true

				var weight := float(formation.get("weight", 0.0))
				if weight <= 0.0:
					failures.append("%s must have positive selection weight" % formation_id)
				total_weight += maxf(weight, 0.0)

				var enemies: Array = formation.get("enemies", [])
				if enemies.is_empty():
					failures.append("%s must contain at least one runtime enemy" % formation_id)
				elif enemies.size() > max_enemies:
					failures.append("%s exceeds the area runtime enemy cap" % formation_id)

				var subareas: Array = formation.get("subareas", [])
				if subareas.is_empty():
					failures.append("%s must identify at least one runtime subarea" % formation_id)

				if int(formation.get("exp", -1)) < 0:
					failures.append("%s exposes an invalid negative runtime EXP value" % formation_id)

			if absf(total_weight - 100.0) > 0.001:
				failures.append("%s %s selection weights must total 100" % [area_id, tier])

func _validate_pressure_state_machine(failures: Array[String]) -> void:
	var before_threshold = Pressure.new(1101)
	var subthreshold := maxf(Pressure.MIN_TRIGGER_S - 0.01, 0.0)
	if before_threshold.advance(subthreshold, [0.0]):
		failures.append("Encounter pressure triggered before its configured minimum threshold")

	var pressure = Pressure.new(1102)
	if not pressure.advance(Pressure.MIN_TRIGGER_S, [0.0]):
		failures.append("Encounter pressure failed a deterministic trigger at its configured minimum threshold")
	pressure.reset_after_victory()
	if pressure.encounter_pending or absf(pressure.distance_s) > Pressure.EPSILON:
		failures.append("Victory reset did not clear encounter pressure state")

	pressure.resume_after_successful_flee()
	if absf(pressure.distance_s - Pressure.FLEE_RESUME_S) > Pressure.EPSILON:
		failures.append("Successful flee did not restore the configured resume pressure")
	if pressure.grace_remaining_s <= 0.0:
		failures.append("Successful flee did not apply a positive grace window")

	pressure.reset_after_victory()
	pressure.set_paused(true)
	if pressure.advance(Pressure.MIN_TRIGGER_S * 2.0, [0.0]):
		failures.append("Paused encounter pressure generated an encounter")
	if absf(pressure.distance_s) > Pressure.EPSILON:
		failures.append("Paused encounter pressure accumulated movement")

func _validate_selector_contract(failures: Array[String]) -> void:
	var selector = Selector.new(2201)
	var found_multi_pool := false

	for area_id in Catalog.area_ids():
		var chapter := Catalog.chapter_for_area(area_id)
		var tier := Balance.tier_for_roll(chapter, 0.0)
		if tier.is_empty():
			continue
		var pool: Array = Catalog.formations_for_area_tier(area_id, tier)
		if pool.size() < 2:
			continue

		found_multi_pool = true
		var previous_id := str(pool[0].get("id", ""))
		var selected: Dictionary = selector.choose_with_rolls(chapter, area_id, 0.0, 0.0, previous_id)
		if selected.is_empty():
			failures.append("Encounter selector failed to return a legal formation for %s" % area_id)
			break
		if str(selected.get("tier", "")) != tier:
			failures.append("Encounter selector changed the selected tier for %s" % area_id)
		if str(selected.get("id", "")) == previous_id:
			failures.append("Encounter selector repeated the previous formation despite alternatives in %s" % area_id)

		var legal_ids: Array[String] = []
		for formation in pool:
			legal_ids.append(str(formation.get("id", "")))
		if str(selected.get("id", "")) not in legal_ids:
			failures.append("Encounter selector returned a formation outside the selected pool for %s" % area_id)

		if not selector.choose_with_rolls(chapter + 100, area_id, 0.0, 0.0).is_empty():
			failures.append("Encounter selector accepted an area under the wrong chapter")
		break

	if not found_multi_pool:
		failures.append("Encounter catalog exposes no multi-formation pool for selector repeat-avoidance validation")

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Encounter runtime structural contract validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
