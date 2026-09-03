extends Resource
class_name DiyseDialogueSceneDefinition

const SCHEMA_VERSION := 1
const ALLOWED_SCENE_KINDS := ["mandatory", "character_life", "quest", "ambient", "banter", "battle", "proof"]
const ALLOWED_ACTIVE_SIDES := ["left", "right", "none"]
const ALLOWED_ADVANCE_MODES := ["manual"]
const FORBIDDEN_BRANCH_KEYS := ["choices", "responses", "branches", "dialogue_choices", "affinity_options", "tone_options"]

@export var schema_version: int = SCHEMA_VERSION
@export var scene_id: String = ""
@export var chapter_id: String = ""
@export var scene_kind: String = "mandatory"
@export var location_id: String = ""
@export var trigger_id: String = ""
@export var completion_flag: String = ""
@export var participants: Array[String] = []

# Audit88 presentation metadata is deliberately optional/backward-compatible.
# It describes how a closed scene should be staged without changing its dialogue.
@export var cutscene_tier: String = "C0"
@export var vfx_tier: String = "V1"
@export var presentation_tags: Array[String] = []
@export var battle_background_family: String = ""

@export_multiline var authoring_notes: String = ""
@export var beats: Array[Dictionary] = []

func validate_schema(registry: DiyseDialoguePortraitRegistry = null) -> Array[String]:
	var failures: Array[String] = []
	if schema_version != SCHEMA_VERSION:
		failures.append("Unsupported dialogue scene schema version: %d" % schema_version)
	if scene_id.is_empty():
		failures.append("scene_id is required")
	if chapter_id.is_empty():
		failures.append("chapter_id is required")
	if scene_kind not in ALLOWED_SCENE_KINDS:
		failures.append("Unsupported scene_kind: %s" % scene_kind)
	if completion_flag.is_empty():
		failures.append("completion_flag is required")
	if not DiyseHd2dRuntime.is_valid_cutscene_tier(cutscene_tier):
		failures.append("Unsupported cutscene_tier: %s" % cutscene_tier)
	if not DiyseHd2dRuntime.is_valid_vfx_tier(vfx_tier):
		failures.append("Unsupported vfx_tier: %s" % vfx_tier)
	if beats.is_empty():
		failures.append("At least one beat is required")

	var seen_beats: Dictionary = {}
	for i in range(beats.size()):
		var beat: Dictionary = beats[i]
		var prefix := "beat[%d]" % i
		for forbidden in FORBIDDEN_BRANCH_KEYS:
			if beat.has(forbidden):
				failures.append("%s contains forbidden dialogue-choice field: %s" % [prefix, forbidden])
		var beat_id := str(beat.get("beat_id", ""))
		if beat_id.is_empty():
			failures.append("%s beat_id is required" % prefix)
		elif seen_beats.has(beat_id):
			failures.append("Duplicate beat_id: %s" % beat_id)
		else:
			seen_beats[beat_id] = true
		var active_side := str(beat.get("active_side", "none"))
		if active_side not in ALLOWED_ACTIVE_SIDES:
			failures.append("%s has invalid active_side: %s" % [prefix, active_side])
		var advance_mode := str(beat.get("advance_mode", "manual"))
		if advance_mode not in ALLOWED_ADVANCE_MODES:
			failures.append("%s has unsupported advance_mode: %s" % [prefix, advance_mode])
		var speaker_id := str(beat.get("speaker_id", ""))
		var text := str(beat.get("text", ""))
		if speaker_id.is_empty() and not text.is_empty():
			failures.append("%s has text but no speaker_id" % prefix)
		if registry != null and not speaker_id.is_empty() and not registry.has_character(speaker_id):
			failures.append("%s references unknown speaker_id: %s" % [prefix, speaker_id])
		_validate_portrait_slot(beat.get("left", {}), "left", prefix, registry, failures)
		_validate_portrait_slot(beat.get("right", {}), "right", prefix, registry, failures)
		var cues = beat.get("cues", {})
		if not (cues is Dictionary):
			failures.append("%s cues must be a Dictionary" % prefix)
	return failures

func presentation_metadata() -> Dictionary:
	return {
		"scene_id": scene_id,
		"chapter_id": chapter_id,
		"location_id": location_id,
		"cutscene_tier": cutscene_tier,
		"vfx_tier": vfx_tier,
		"presentation_tags": presentation_tags.duplicate(),
		"battle_background_family": battle_background_family,
	}

func to_runner_beats(registry: DiyseDialoguePortraitRegistry) -> Array[Dictionary]:
	var result: Array[Dictionary] = []
	for beat in beats:
		var left_value = beat.get("left", {})
		var right_value = beat.get("right", {})
		var cues_value = beat.get("cues", {})
		var left: Dictionary = left_value if left_value is Dictionary else {}
		var right: Dictionary = right_value if right_value is Dictionary else {}
		var cues: Dictionary = cues_value if cues_value is Dictionary else {}
		var speaker_id := str(beat.get("speaker_id", ""))
		result.append({
			"scene_id": scene_id,
			"beat_id": str(beat.get("beat_id", "")),
			"speaker_id": speaker_id,
			"speaker": registry.display_name(speaker_id) if registry != null else speaker_id,
			"text": str(beat.get("text", "")),
			"left_portrait": registry.resolve_portrait(str(left.get("character_id", "")), str(left.get("expression_id", ""))) if registry != null else "",
			"right_portrait": registry.resolve_portrait(str(right.get("character_id", "")), str(right.get("expression_id", ""))) if registry != null else "",
			"active_side": str(beat.get("active_side", "none")),
			"advance_mode": str(beat.get("advance_mode", "manual")),
			"cues": cues.duplicate(true)
		})
	return result

func _validate_portrait_slot(value: Variant, slot_name: String, prefix: String, registry: DiyseDialoguePortraitRegistry, failures: Array[String]) -> void:
	if not (value is Dictionary):
		failures.append("%s %s portrait slot must be a Dictionary" % [prefix, slot_name])
		return
	var slot: Dictionary = value
	var character_id := str(slot.get("character_id", ""))
	var expression_id := str(slot.get("expression_id", ""))
	if character_id.is_empty() and expression_id.is_empty():
		return
	if character_id.is_empty() or expression_id.is_empty():
		failures.append("%s %s portrait slot requires both character_id and expression_id" % [prefix, slot_name])
		return
	if registry != null:
		if not registry.has_character(character_id):
			failures.append("%s %s portrait references unknown character_id: %s" % [prefix, slot_name, character_id])
		elif not registry.has_expression(character_id, expression_id):
			failures.append("%s %s portrait references unknown expression_id: %s/%s" % [prefix, slot_name, character_id, expression_id])
