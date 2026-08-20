extends RefCounted
class_name DiyseEncounterPressure

const MIN_TRIGGER_S := 0.35
const CHECK_INTERVAL_S := 0.10
const FLEE_GRACE_S := 0.20
const FLEE_RESUME_S := 0.65
const ECOLOGY_TRANSITION_GRACE_S := 0.10
const EPSILON := 0.00001

const TRIGGER_CURVE := [
	{"at_s": 0.35, "chance": 0.03},
	{"at_s": 0.45, "chance": 0.04},
	{"at_s": 0.55, "chance": 0.06},
	{"at_s": 0.65, "chance": 0.08},
	{"at_s": 0.75, "chance": 0.10},
	{"at_s": 0.85, "chance": 0.13},
	{"at_s": 0.95, "chance": 0.17},
	{"at_s": 1.05, "chance": 0.22},
	{"at_s": 1.15, "chance": 0.28},
	{"at_s": 1.25, "chance": 0.36},
	{"at_s": 1.35, "chance": 0.46},
	{"at_s": 1.45, "chance": 0.58},
	{"at_s": 1.55, "chance": 0.70},
	{"at_s": 1.65, "chance": 0.80},
]

var distance_s := 0.0
var next_check_s := MIN_TRIGGER_S
var grace_remaining_s := 0.0
var paused := false
var encounter_pending := false

var _rng := RandomNumberGenerator.new()

func _init(seed_value: int = 0) -> void:
	if seed_value == 0:
		_rng.randomize()
	else:
		_rng.seed = seed_value

static func chance_for_spacing(spacing_s: float) -> float:
	if spacing_s + EPSILON < MIN_TRIGGER_S:
		return 0.0
	var result := 0.80
	for point in TRIGGER_CURVE:
		if spacing_s <= float(point["at_s"]) + EPSILON:
			result = float(point["chance"])
			break
	return result

func set_paused(value: bool) -> void:
	paused = value

func advance(normalized_distance: float, forced_rolls: Array = []) -> bool:
	if normalized_distance <= 0.0 or paused or encounter_pending:
		return false

	var remaining := normalized_distance
	if grace_remaining_s > 0.0:
		var consumed := minf(grace_remaining_s, remaining)
		grace_remaining_s -= consumed
		remaining -= consumed
		if remaining <= EPSILON:
			return false

	distance_s += remaining
	var roll_index := 0
	while distance_s + EPSILON >= next_check_s:
		var chance := chance_for_spacing(next_check_s)
		var roll := _rng.randf()
		if roll_index < forced_rolls.size():
			roll = clampf(float(forced_rolls[roll_index]), 0.0, 1.0)
		roll_index += 1
		next_check_s += CHECK_INTERVAL_S
		if roll < chance:
			encounter_pending = true
			return true
	return false

func apply_transition_grace(grace_s: float = ECOLOGY_TRANSITION_GRACE_S) -> void:
	if grace_s <= 0.0:
		return
	grace_remaining_s = maxf(grace_remaining_s, grace_s)

func reset_after_victory() -> void:
	distance_s = 0.0
	next_check_s = MIN_TRIGGER_S
	grace_remaining_s = 0.0
	encounter_pending = false

func reset_for_safe_room() -> void:
	reset_after_victory()

func resume_after_successful_flee() -> void:
	distance_s = FLEE_RESUME_S
	next_check_s = FLEE_RESUME_S
	grace_remaining_s = FLEE_GRACE_S
	encounter_pending = false

func resume_after_failed_flee() -> void:
	encounter_pending = false

func cancel_pending_encounter() -> void:
	encounter_pending = false
