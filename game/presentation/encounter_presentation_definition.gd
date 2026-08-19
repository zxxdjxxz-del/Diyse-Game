extends Resource
class_name DiyseEncounterPresentationDefinition

const ALLOWED_ENCOUNTER_KINDS := ["random", "fixed", "boss", "hunt", "elite"]
const ALLOWED_RESOLUTION_MODES := [
	"standard",
	"nonlethal_retreat",
	"nonlethal_stabilize",
	"nonlethal_deescalate",
]
const ALLOWED_FORM_MODES := [
	"none",
	"same_body_same_hp",
	"genuine_new_form",
	"prime_scale",
]

@export var presentation_id: String = ""
@export var encounter_kind: String = "fixed"
@export var battle_background_family: String = ""
@export var cutscene_tier: String = "C0"
@export var vfx_tier: String = "V1"
@export var resolution_mode: String = "standard"
@export var form_mode: String = "none"
@export var suppress_victory_pose: bool = false
@export var suppress_generic_loot_show: bool = false

# Intentionally absent: enemy IDs, chapter placement, map placement, Elite IDs,
# encounter tables, final stats, or final visual assets. This resource describes
# presentation behavior only and cannot assign an Elite or ordinary enemy to a scene.

func validate_schema() -> Array[String]:
	var failures: Array[String] = []
	if presentation_id.is_empty():
		failures.append("presentation_id is required")
	if encounter_kind not in ALLOWED_ENCOUNTER_KINDS:
		failures.append("Unsupported encounter_kind: %s" % encounter_kind)
	if not DiyseHd2dRuntime.is_valid_cutscene_tier(cutscene_tier):
		failures.append("Unsupported cutscene_tier: %s" % cutscene_tier)
	if not DiyseHd2dRuntime.is_valid_vfx_tier(vfx_tier):
		failures.append("Unsupported vfx_tier: %s" % vfx_tier)
	if resolution_mode not in ALLOWED_RESOLUTION_MODES:
		failures.append("Unsupported resolution_mode: %s" % resolution_mode)
	if form_mode not in ALLOWED_FORM_MODES:
		failures.append("Unsupported form_mode: %s" % form_mode)
	return failures

func is_nonlethal() -> bool:
	return resolution_mode != "standard"

func uses_genuine_new_form() -> bool:
	return form_mode == "genuine_new_form"
