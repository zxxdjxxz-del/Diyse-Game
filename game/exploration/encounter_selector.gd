extends RefCounted
class_name DiyseEncounterSelector

const Balance = preload("res://game/exploration/encounter_balance.gd")
const Catalog = preload("res://game/content/encounters/chapter_01_04_formations.gd")

var _rng := RandomNumberGenerator.new()

func _init(seed_value: int = 0) -> void:
	if seed_value == 0:
		_rng.randomize()
	else:
		_rng.seed = seed_value

func supports_context(chapter: int, area_id: String) -> bool:
	return Catalog.chapter_for_area(area_id) == chapter

func choose(chapter: int, area_id: String, previous_formation_id: String = "") -> Dictionary:
	return choose_with_rolls(chapter, area_id, _rng.randf(), _rng.randf(), previous_formation_id)

func choose_with_rolls(
	chapter: int,
	area_id: String,
	tier_roll: float,
	formation_roll: float,
	previous_formation_id: String = ""
) -> Dictionary:
	if not supports_context(chapter, area_id):
		return {}
	var tier := Balance.tier_for_roll(chapter, tier_roll)
	if tier.is_empty():
		return {}
	var pool: Array = Catalog.formations_for_area_tier(area_id, tier)
	if pool.is_empty():
		return {}

	var candidates: Array = []
	for formation in pool:
		if pool.size() == 1 or str(formation.get("id", "")) != previous_formation_id:
			candidates.append(formation)
	if candidates.is_empty():
		candidates = pool

	var picked := _weighted_pick(candidates, formation_roll)
	if picked.is_empty():
		return {}
	picked["tier"] = tier
	return picked

static func _weighted_pick(candidates: Array, roll: float) -> Dictionary:
	var total_weight := 0.0
	for candidate in candidates:
		total_weight += maxf(float(candidate.get("weight", 0.0)), 0.0)
	if total_weight <= 0.0:
		return {}
	var target := clampf(roll, 0.0, 0.999999) * total_weight
	var cumulative := 0.0
	for candidate in candidates:
		cumulative += maxf(float(candidate.get("weight", 0.0)), 0.0)
		if target < cumulative:
			return candidate.duplicate(true)
	return candidates.back().duplicate(true)
