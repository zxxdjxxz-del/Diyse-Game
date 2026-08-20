extends Resource
class_name DiyseAreaEncounterTuning

const TRANSITION_SAME_ECOLOGY := "same_ecology"
const TRANSITION_NEW_ECOLOGY := "new_ecology"
const TRANSITION_SAFE_RESET := "safe_reset"
const ALLOWED_TRANSITION_MODES := [
	TRANSITION_SAME_ECOLOGY,
	TRANSITION_NEW_ECOLOGY,
	TRANSITION_SAFE_RESET,
]

const CALIBRATION_ENGINEERING_ONLY := "engineering_only"
const CALIBRATION_AWAITING_GEOMETRY := "awaiting_geometry"
const CALIBRATION_PRODUCTION := "production_calibrated"
const ALLOWED_CALIBRATION_STATES := [
	CALIBRATION_ENGINEERING_ONLY,
	CALIBRATION_AWAITING_GEOMETRY,
	CALIBRATION_PRODUCTION,
]

@export var tuning_id: String = ""
@export var chapter: int = 0
@export var random_area_id: String = ""
@export var world_units_per_s: float = 0.0
@export var random_encounters_enabled: bool = true
@export var transition_mode_on_entry: String = TRANSITION_SAME_ECOLOGY
@export var calibration_state: String = CALIBRATION_AWAITING_GEOMETRY

func validate_schema() -> Array[String]:
	var failures: Array[String] = []
	if tuning_id.is_empty():
		failures.append("tuning_id is required")
	if chapter < 0 or chapter > 12:
		failures.append("chapter must be between 0 and 12")
	if transition_mode_on_entry not in ALLOWED_TRANSITION_MODES:
		failures.append("Unsupported transition_mode_on_entry: %s" % transition_mode_on_entry)
	if calibration_state not in ALLOWED_CALIBRATION_STATES:
		failures.append("Unsupported calibration_state: %s" % calibration_state)
	if world_units_per_s < 0.0:
		failures.append("world_units_per_s cannot be negative")

	if random_encounters_enabled:
		if chapter < 1 or chapter > 12:
			failures.append("Enabled random encounter tuning requires chapter 1 through 12")
		if random_area_id.is_empty():
			failures.append("Enabled random encounter tuning requires random_area_id")
		if world_units_per_s <= 0.0:
			failures.append("Enabled random encounter tuning requires world_units_per_s > 0")
		if calibration_state == CALIBRATION_AWAITING_GEOMETRY:
			failures.append("Uncalibrated area tuning cannot enable random encounters")
	return failures

func is_engineering_only() -> bool:
	return calibration_state == CALIBRATION_ENGINEERING_ONLY

func is_production_calibrated() -> bool:
	return calibration_state == CALIBRATION_PRODUCTION
