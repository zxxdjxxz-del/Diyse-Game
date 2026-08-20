extends Resource
class_name DiyseScenePresentationDefinition

const ALLOWED_ENCOUNTER_MODES := ["none", "fixed_authored", "random_allowed", "mixed"]

@export var scene_id: String = ""
@export var chapter_id: String = ""
@export var environment_family: String = ""
@export var battle_background_family: String = ""
@export var cutscene_tier: String = "C0"
@export var vfx_tier: String = "V1"
@export var encounter_mode: String = "none"
@export var presentation_tags: Array[String] = []

# This is intentionally a presentation sidecar. It does not own enemy identities,
# Elite identities, encounter tables, combat stats, dialogue text, or final assets.

func validate_schema() -> Array[String]:
	var failures: Array[String] = []
	if scene_id.is_empty():
		failures.append("scene_id is required")
	if chapter_id.is_empty():
		failures.append("chapter_id is required")
	if environment_family.is_empty():
		failures.append("environment_family is required")
	if not DiyseHd2dRuntime.is_valid_cutscene_tier(cutscene_tier):
		failures.append("Unsupported cutscene_tier: %s" % cutscene_tier)
	if not DiyseHd2dRuntime.is_valid_vfx_tier(vfx_tier):
		failures.append("Unsupported vfx_tier: %s" % vfx_tier)
	if encounter_mode not in ALLOWED_ENCOUNTER_MODES:
		failures.append("Unsupported encounter_mode: %s" % encounter_mode)
	return failures

func has_tag(tag: String) -> bool:
	return tag in presentation_tags
