extends RefCounted
class_name DiyseLevelCurve

const MIN_LEVEL := 1
const MAX_LEVEL := 60
const RAMP_START_LEVEL := 17
const RAMP_END_LEVEL := 59
const RAMP_GAIN := 0.35
const ROUND_EPSILON := 0.000001

static func level_up_cost(current_level: int) -> int:
	if current_level < MIN_LEVEL or current_level >= MAX_LEVEL:
		return 0
	var base_cost := 100 * (2 * current_level - 1)
	if current_level < RAMP_START_LEVEL:
		return base_cost
	var multiplier := 1.0 + RAMP_GAIN * float(current_level - RAMP_START_LEVEL) / float(RAMP_END_LEVEL - RAMP_START_LEVEL)
	return _round_to_nearest_hundred_half_even(float(base_cost) * multiplier)

static func cumulative_exp_for_level(level: int) -> int:
	var clamped_level := clampi(level, MIN_LEVEL, MAX_LEVEL)
	if clamped_level <= RAMP_START_LEVEL:
		return 100 * (clamped_level - 1) * (clamped_level - 1)
	var total := 100 * (RAMP_START_LEVEL - 1) * (RAMP_START_LEVEL - 1)
	for current_level in range(RAMP_START_LEVEL, clamped_level):
		total += level_up_cost(current_level)
	return total

static func level_for_exp(exp_total: int) -> int:
	var safe_exp := maxi(exp_total, 0)
	for level in range(MAX_LEVEL, MIN_LEVEL - 1, -1):
		if safe_exp >= cumulative_exp_for_level(level):
			return level
	return MIN_LEVEL

static func exp_to_next_level(exp_total: int) -> int:
	var level := level_for_exp(exp_total)
	if level >= MAX_LEVEL:
		return 0
	return maxi(cumulative_exp_for_level(level + 1) - maxi(exp_total, 0), 0)

# Audit98 publishes exact cumulative milestones. Godot's built-in round() uses a
# different .5 tie rule than the validation model that produced those locked
# milestones, so make the tie behavior explicit and platform-independent.
static func _round_to_nearest_hundred_half_even(value: float) -> int:
	var scaled := value / 100.0
	var lower := floori(scaled)
	var fraction := scaled - float(lower)
	if fraction < 0.5 - ROUND_EPSILON:
		return lower * 100
	if fraction > 0.5 + ROUND_EPSILON:
		return (lower + 1) * 100
	if lower % 2 == 0:
		return lower * 100
	return (lower + 1) * 100
