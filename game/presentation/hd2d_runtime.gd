extends RefCounted
class_name DiyseHd2dRuntime

const REFERENCE_SIZE := Vector2(1920.0, 1080.0)
const FIELD_CHARACTER_TARGET_PX := 80.0
const BATTLE_CHARACTER_TARGET_PX := 200.0

const CUTSCENE_TIERS := ["C0", "C1", "C2", "C3"]
const VFX_TIERS := ["V1", "V2", "V3", "V4"]

# Permanent four-slot party grammar. Early 1–3 person parties occupy these same
# legal homes rather than being recentered. All anchors stay left of the action lane.
const PARTY_ANCHORS_NORMALIZED := [
	Vector2(0.18, 0.68),
	Vector2(0.25, 0.58),
	Vector2(0.16, 0.48),
	Vector2(0.28, 0.40),
]

# Generic enemy-side homes. Encounter data may choose how many are used, but
# presentation code keeps them right of the protected center action lane.
const ENEMY_ANCHORS_NORMALIZED := [
	Vector2(0.78, 0.60),
	Vector2(0.86, 0.48),
	Vector2(0.73, 0.40),
	Vector2(0.88, 0.68),
	Vector2(0.76, 0.76),
	Vector2(0.90, 0.32),
]

const ACTION_LANE_NORMALIZED := Rect2(0.32, 0.20, 0.36, 0.64)

static func is_valid_cutscene_tier(value: String) -> bool:
	return value in CUTSCENE_TIERS

static func is_valid_vfx_tier(value: String) -> bool:
	return value in VFX_TIERS

static func party_anchor(slot_index: int, viewport_size: Vector2 = REFERENCE_SIZE) -> Vector2:
	if slot_index < 0 or slot_index >= PARTY_ANCHORS_NORMALIZED.size():
		return Vector2(-1.0, -1.0)
	return _to_pixels(PARTY_ANCHORS_NORMALIZED[slot_index], viewport_size)

static func enemy_anchor(slot_index: int, viewport_size: Vector2 = REFERENCE_SIZE) -> Vector2:
	if slot_index < 0 or slot_index >= ENEMY_ANCHORS_NORMALIZED.size():
		return Vector2(-1.0, -1.0)
	return _to_pixels(ENEMY_ANCHORS_NORMALIZED[slot_index], viewport_size)

static func action_lane(viewport_size: Vector2 = REFERENCE_SIZE) -> Rect2:
	return Rect2(
		Vector2(
			ACTION_LANE_NORMALIZED.position.x * viewport_size.x,
			ACTION_LANE_NORMALIZED.position.y * viewport_size.y
		),
		Vector2(
			ACTION_LANE_NORMALIZED.size.x * viewport_size.x,
			ACTION_LANE_NORMALIZED.size.y * viewport_size.y
		)
	)

static func field_sprite_scale_for_texture(texture_height_px: float) -> float:
	if texture_height_px <= 0.0:
		return 1.0
	return FIELD_CHARACTER_TARGET_PX / texture_height_px

static func battle_sprite_scale_for_texture(texture_height_px: float) -> float:
	if texture_height_px <= 0.0:
		return 1.0
	return BATTLE_CHARACTER_TARGET_PX / texture_height_px

static func decorative_quality_profile(level: int) -> Dictionary:
	# 0 = low, 1 = medium, 2 = high. Gameplay-critical readability is deliberately
	# absent from this profile and must never be quality-scaled away.
	match clampi(level, 0, 2):
		0:
			return {
				"particle_multiplier": 0.45,
				"reflection_scale": 0.50,
				"secondary_motion": false,
				"weather_multiplier": 0.55,
				"decorative_dynamic_lights": false,
			}
		1:
			return {
				"particle_multiplier": 0.75,
				"reflection_scale": 0.75,
				"secondary_motion": true,
				"weather_multiplier": 0.80,
				"decorative_dynamic_lights": false,
			}
		_:
			return {
				"particle_multiplier": 1.0,
				"reflection_scale": 1.0,
				"secondary_motion": true,
				"weather_multiplier": 1.0,
				"decorative_dynamic_lights": true,
			}

static func _to_pixels(normalized: Vector2, viewport_size: Vector2) -> Vector2:
	return Vector2(normalized.x * viewport_size.x, normalized.y * viewport_size.y)
