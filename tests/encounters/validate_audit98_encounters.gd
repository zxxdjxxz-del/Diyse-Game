extends SceneTree

const Balance = preload("res://game/exploration/encounter_balance.gd")
const Pressure = preload("res://game/exploration/encounter_pressure.gd")
const Selector = preload("res://game/exploration/encounter_selector.gd")
const Catalog = preload("res://game/content/encounters/chapter_01_04_formations.gd")
const LevelCurve = preload("res://game/core/progression/level_curve.gd")

const ALLOWED_BY_AREA := {
	"ch01_brackenwall": ["Black Host Raider", "Black Host Crossbowman", "Ruin Shieldbearer", "Brackenwall Reaver"],
	"ch01_greenhollow": ["Greenhollow Stalker", "Thornvine Creeper", "Briar Boar"],
	"ch01_hollow_watch": ["Hollow Watch Sentry", "Hollow Watch Ballista"],
	"ch02_dunmere_waterworks": ["Redwater Initiate", "Bogshell", "Cistern Leech"],
	"ch02_sunken_archive": ["Archive Current", "Memory Scribe", "Vault Sentinel", "Drowned Archive Maw"],
	"ch02_red_transfer_bastion": ["Bastion Shield Guard", "Bastion Crossbow Guard", "Transfer Adept", "Black Host Raider", "Beast Handler", "Rift Hound"],
	"ch03_way_fort": ["Way-Fort Marauder", "Rift Boltman", "Black Host Ward-Sorcerer"],
	"ch03_suppressed_archives": ["Archive Scribe Engine", "Judgment Frame", "Erasure Wisp"],
	"ch03_command_station": ["Command-Station Sentry", "Authority Lens", "Command Ring Drone"],
	"ch04_reaction_annex": ["Reaction Node", "Composite Elemental", "Reaction Hound", "Element Mirror", "Annex Crucible Guard"],
}

const EXP_MILESTONES := {
	17: 25600,
	22: 44400,
	23: 48900,
	27: 69300,
	32: 100600,
	37: 138800,
	42: 184300,
	47: 237600,
	50: 273500,
	53: 312400,
	54: 326000,
	55: 340000,
	56: 354400,
	57: 369100,
	58: 384200,
	59: 399600,
	60: 415400,
}

func _initialize() -> void:
	var failures: Array[String] = []
	_validate_balance_profiles(failures)
	_validate_level_curve(failures)
	_validate_pressure(failures)
	_validate_chapter_01_04_catalog(failures)
	_validate_selector(failures)
	_finish(failures)

func _validate_balance_profiles(failures: Array[String]) -> void:
	if Balance.MAX_ACTIVE_ENEMIES != 8:
		failures.append("Audit98 maximum active enemy count must be 8")
	if Balance.expected_campaign_encounters() != 210:
		failures.append("Audit98 campaign encounter center must total 210")
	for chapter in range(1, 13):
		for failure in Balance.validate_profile(chapter):
			failures.append(failure)

	for chapter in range(1, 5):
		var profile: Dictionary = Balance.profile_for_chapter(chapter)
		var weights: Dictionary = profile["tier_weights"]
		var anchors: Dictionary = profile["exp_anchors"]
		var weighted_mean := (
			float(weights["light"]) * float(anchors["light"]) +
			float(weights["standard"]) * float(anchors["standard"]) +
			float(weights["heavy"]) * float(anchors["heavy"])
		) / 100.0
		var projected_pool := weighted_mean * float(profile["expected_encounters"])
		if absf(projected_pool - float(profile["expected_ordinary_exp_pool"])) > 2.0:
			failures.append("Chapter %d weighted formation anchors drift from Audit98 ordinary EXP pool" % chapter)

	if Balance.tier_for_roll(1, 0.249999) != "light":
		failures.append("Chapter 1 light-tier cutoff is incorrect")
	if Balance.tier_for_roll(1, 0.25) != "standard":
		failures.append("Chapter 1 standard-tier cutoff is incorrect")
	if Balance.tier_for_roll(1, 0.80) != "heavy":
		failures.append("Chapter 1 heavy-tier cutoff is incorrect")

func _validate_level_curve(failures: Array[String]) -> void:
	for level in EXP_MILESTONES.keys():
		var expected := int(EXP_MILESTONES[level])
		var actual := LevelCurve.cumulative_exp_for_level(int(level))
		if actual != expected:
			failures.append("Level %d cumulative EXP expected %d, got %d" % [level, expected, actual])
	if LevelCurve.cumulative_exp_for_level(1) != 0:
		failures.append("Level 1 must begin at 0 EXP")
	if LevelCurve.level_for_exp(312399) != 52:
		failures.append("312,399 EXP must remain Level 52")
	if LevelCurve.level_for_exp(312400) != 53:
		failures.append("312,400 EXP must be Level 53")
	if LevelCurve.level_for_exp(9999999) != 60:
		failures.append("Level curve must clamp at Level 60")
	if LevelCurve.exp_to_next_level(415400) != 0:
		failures.append("Level 60 must not expose overflow level progression")

func _validate_pressure(failures: Array[String]) -> void:
	if Pressure.chance_for_spacing(0.34) != 0.0:
		failures.append("Encounter pressure must not trigger before 0.35S")
	if absf(Pressure.chance_for_spacing(0.35) - 0.03) > 0.0001:
		failures.append("0.35S trigger chance must be 3%")
	if absf(Pressure.chance_for_spacing(1.65) - 0.80) > 0.0001:
		failures.append("1.65S+ trigger chance must be 80%")

	var pressure = Pressure.new(12345)
	if pressure.advance(0.0, [0.0]):
		failures.append("Standing still must not create encounters")
	if pressure.advance(0.34, [0.0]):
		failures.append("Encounter fired before 0.35S")
	if not pressure.advance(0.01, [0.0]):
		failures.append("Deterministic low roll did not trigger at 0.35S")
	pressure.reset_after_victory()
	if pressure.distance_s != 0.0 or pressure.encounter_pending:
		failures.append("Victory must reset encounter pressure")

	var high_rolls: Array = []
	for _index in range(20):
		high_rolls.append(0.99)
	if pressure.advance(1.65, high_rolls):
		failures.append("A 0.99 roll must survive the pressure curve without a forced encounter")

	pressure.resume_after_successful_flee()
	if absf(pressure.distance_s - 0.65) > 0.0001:
		failures.append("Successful flee must resume near 0.65S effective pressure")
	if pressure.advance(0.20, [0.0]):
		failures.append("Successful flee 0.20S grace was not honored")
	if not pressure.advance(0.001, [0.0]):
		failures.append("Pressure did not resume after successful-flee grace")

	pressure.reset_after_victory()
	pressure.set_paused(true)
	if pressure.advance(1.0, [0.0]) or pressure.distance_s != 0.0:
		failures.append("Paused encounter pressure must ignore movement")
	pressure.set_paused(false)

func _validate_chapter_01_04_catalog(failures: Array[String]) -> void:
	var area_ids := Catalog.area_ids()
	if area_ids.size() != ALLOWED_BY_AREA.size():
		failures.append("Chapter 1-4 catalog must contain exactly the approved first-pass area tables")
	if Catalog.has_area("ch03_caelora"):
		failures.append("Caelora lawful personnel must not receive an ordinary random-farm table")

	var seen_ids := {}
	for area_id in area_ids:
		if not ALLOWED_BY_AREA.has(area_id):
			failures.append("Unexpected Chapter 1-4 random area: %s" % area_id)
			continue
		var chapter := Catalog.chapter_for_area(area_id)
		var profile: Dictionary = Balance.profile_for_chapter(chapter)
		var max_enemies := int(profile["max_enemies"])
		for tier in Catalog.TIER_NAMES:
			var formations: Array = Catalog.formations_for_area_tier(area_id, tier)
			if formations.size() < 2:
				failures.append("%s %s tier needs at least two formations for anti-repeat selection" % [area_id, tier])
			var total_weight := 0.0
			for formation in formations:
				var formation_id := str(formation.get("id", ""))
				if formation_id.is_empty():
					failures.append("%s %s contains a formation without an ID" % [area_id, tier])
				elif seen_ids.has(formation_id):
					failures.append("Duplicate formation ID: %s" % formation_id)
				else:
					seen_ids[formation_id] = true
				total_weight += float(formation.get("weight", 0.0))
				if int(formation.get("exp", 0)) != Balance.exp_anchor(chapter, tier):
					failures.append("%s must use Chapter %d %s Audit98 EXP anchor" % [formation_id, chapter, tier])
				var enemies: Array = formation.get("enemies", [])
				if enemies.is_empty() or enemies.size() > max_enemies:
					failures.append("%s violates Chapter %d enemy-count limits" % [formation_id, chapter])
				for enemy_name in enemies:
					if str(enemy_name) not in ALLOWED_BY_AREA[area_id]:
						failures.append("%s uses non-approved random enemy %s in %s" % [formation_id, enemy_name, area_id])
			if absf(total_weight - 100.0) > 0.001:
				failures.append("%s %s formation weights must total 100" % [area_id, tier])

func _validate_selector(failures: Array[String]) -> void:
	var selector = Selector.new(9876)
	var light_pool: Array = Catalog.formations_for_area_tier("ch01_greenhollow", "light")
	var previous_id := str(light_pool[0]["id"])
	var selected: Dictionary = selector.choose_with_rolls(1, "ch01_greenhollow", 0.0, 0.0, previous_id)
	if selected.is_empty():
		failures.append("Encounter selector failed to return a legal formation")
	elif str(selected.get("id", "")) == previous_id:
		failures.append("Encounter selector repeated the same formation despite an available alternative")
	if str(selected.get("tier", "")) != "light":
		failures.append("Encounter selector did not preserve the Light tier roll")
	if not selector.choose_with_rolls(3, "ch01_greenhollow", 0.0, 0.0).is_empty():
		failures.append("Encounter selector accepted an area under the wrong chapter")

func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Audit98 encounter pressure, level curve, balance profiles, and Chapter 1-4 formation validation passed.")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	quit(1)
