extends RefCounted
class_name DiyseEncounterBalance

const MAX_ACTIVE_ENEMIES := 8

const CHAPTER_PROFILES := {
	1: {
		"expected_encounters": 18,
		"tier_weights": {"light": 25.0, "standard": 55.0, "heavy": 20.0},
		"exp_anchors": {"light": 45, "standard": 55, "heavy": 70},
		"expected_ordinary_exp_pool": 1000,
		"typical_min": 2,
		"typical_max": 3,
		"max_enemies": 4,
	},
	2: {
		"expected_encounters": 19,
		"tier_weights": {"light": 25.0, "standard": 55.0, "heavy": 20.0},
		"exp_anchors": {"light": 130, "standard": 165, "heavy": 200},
		"expected_ordinary_exp_pool": 3100,
		"typical_min": 3,
		"typical_max": 4,
		"max_enemies": 4,
	},
	3: {
		"expected_encounters": 19,
		"tier_weights": {"light": 22.0, "standard": 55.0, "heavy": 23.0},
		"exp_anchors": {"light": 215, "standard": 280, "heavy": 315},
		"expected_ordinary_exp_pool": 5200,
		"typical_min": 3,
		"typical_max": 4,
		"max_enemies": 5,
	},
	4: {
		"expected_encounters": 19,
		"tier_weights": {"light": 20.0, "standard": 55.0, "heavy": 25.0},
		"exp_anchors": {"light": 315, "standard": 375, "heavy": 460},
		"expected_ordinary_exp_pool": 7300,
		"typical_min": 4,
		"typical_max": 5,
		"max_enemies": 6,
	},
	5: {
		"expected_encounters": 20,
		"tier_weights": {"light": 18.0, "standard": 55.0, "heavy": 27.0},
		"exp_anchors": {"light": 460, "standard": 610, "heavy": 710},
		"expected_ordinary_exp_pool": 12200,
		"typical_min": 5,
		"typical_max": 6,
		"max_enemies": 7,
	},
	6: {
		"expected_encounters": 19,
		"tier_weights": {"light": 18.0, "standard": 55.0, "heavy": 27.0},
		"exp_anchors": {"light": 650, "standard": 850, "heavy": 995},
		"expected_ordinary_exp_pool": 16200,
		"typical_min": 5,
		"typical_max": 7,
		"max_enemies": 8,
	},
	7: {
		"expected_encounters": 19,
		"tier_weights": {"light": 17.0, "standard": 55.0, "heavy": 28.0},
		"exp_anchors": {"light": 830, "standard": 1050, "heavy": 1250},
		"expected_ordinary_exp_pool": 20300,
		"typical_min": 6,
		"typical_max": 7,
		"max_enemies": 8,
	},
	8: {
		"expected_encounters": 18,
		"tier_weights": {"light": 17.0, "standard": 55.0, "heavy": 28.0},
		"exp_anchors": {"light": 1070, "standard": 1360, "heavy": 1600},
		"expected_ordinary_exp_pool": 24800,
		"typical_min": 6,
		"typical_max": 8,
		"max_enemies": 8,
	},
	9: {
		"expected_encounters": 16,
		"tier_weights": {"light": 22.0, "standard": 55.0, "heavy": 23.0},
		"exp_anchors": {"light": 1480, "standard": 1825, "heavy": 2265},
		"expected_ordinary_exp_pool": 29600,
		"typical_min": 6,
		"typical_max": 8,
		"max_enemies": 8,
	},
	10: {
		"expected_encounters": 17,
		"tier_weights": {"light": 19.0, "standard": 55.0, "heavy": 26.0},
		"exp_anchors": {"light": 1835, "standard": 2300, "heavy": 2640},
		"expected_ordinary_exp_pool": 39100,
		"typical_min": 6,
		"typical_max": 8,
		"max_enemies": 8,
	},
	11: {
		"expected_encounters": 18,
		"tier_weights": {"light": 22.0, "standard": 55.0, "heavy": 23.0},
		"exp_anchors": {"light": 2075, "standard": 2600, "heavy": 3100},
		"expected_ordinary_exp_pool": 46800,
		"typical_min": 6,
		"typical_max": 8,
		"max_enemies": 8,
	},
	12: {
		"expected_encounters": 8,
		"tier_weights": {"light": 22.5, "standard": 55.0, "heavy": 22.5},
		"exp_anchors": {"light": 2080, "standard": 2600, "heavy": 3120},
		"expected_ordinary_exp_pool": 20800,
		"typical_min": 5,
		"typical_max": 8,
		"max_enemies": 8,
	},
}

static func profile_for_chapter(chapter: int) -> Dictionary:
	if not CHAPTER_PROFILES.has(chapter):
		return {}
	return CHAPTER_PROFILES[chapter].duplicate(true)

static func tier_for_roll(chapter: int, roll: float) -> String:
	var profile := profile_for_chapter(chapter)
	if profile.is_empty():
		return ""
	var weights: Dictionary = profile["tier_weights"]
	var normalized := clampf(roll, 0.0, 0.999999)
	var light_cutoff := float(weights["light"]) / 100.0
	var standard_cutoff := light_cutoff + float(weights["standard"]) / 100.0
	if normalized < light_cutoff:
		return "light"
	if normalized < standard_cutoff:
		return "standard"
	return "heavy"

static func exp_anchor(chapter: int, tier: String) -> int:
	var profile := profile_for_chapter(chapter)
	if profile.is_empty():
		return 0
	var anchors: Dictionary = profile["exp_anchors"]
	return int(anchors.get(tier, 0))

static func expected_campaign_encounters() -> int:
	var total := 0
	for chapter in CHAPTER_PROFILES.keys():
		total += int(CHAPTER_PROFILES[chapter]["expected_encounters"])
	return total

static func validate_profile(chapter: int) -> Array[String]:
	var failures: Array[String] = []
	var profile := profile_for_chapter(chapter)
	if profile.is_empty():
		failures.append("Missing chapter profile: %d" % chapter)
		return failures
	var weights: Dictionary = profile["tier_weights"]
	var weight_total := float(weights["light"]) + float(weights["standard"]) + float(weights["heavy"])
	if absf(weight_total - 100.0) > 0.001:
		failures.append("Chapter %d tier weights must total 100" % chapter)
	var max_enemies := int(profile["max_enemies"])
	if max_enemies > MAX_ACTIVE_ENEMIES:
		failures.append("Chapter %d exceeds the 8-active-enemy cap" % chapter)
	if int(profile["typical_min"]) > int(profile["typical_max"]):
		failures.append("Chapter %d typical formation range is inverted" % chapter)
	if int(profile["typical_max"]) > max_enemies:
		failures.append("Chapter %d typical formation range exceeds its maximum" % chapter)
	return failures
