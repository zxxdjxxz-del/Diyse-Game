extends RefCounted
class_name DiyseElementalPresentationRuntime

const ELEMENTS := ["fire", "ice", "lightning", "earth"]

const PAYLOAD_KEYS := {
	"fire": ["heat_distortion", "embers", "scorch_overlay"],
	"ice": ["frost_mask", "cold_mist"],
	"lightning": ["electric_arc", "static_overlay"],
	"earth": ["crack_overlay", "dust", "material_shift"],
}

static func is_element(element_id: String) -> bool:
	return element_id.to_lower() in ELEMENTS

static func payload_keys(element_id: String) -> Array:
	var normalized := element_id.to_lower()
	if not is_element(normalized):
		return []
	return PAYLOAD_KEYS[normalized].duplicate()

static func active_module_mask(element_ids: Array[String]) -> Dictionary:
	var normalized_ids: Array[String] = []
	for element_id in element_ids:
		normalized_ids.append(element_id.to_lower())
	var result := {}
	for element_id in ELEMENTS:
		result[element_id] = element_id in normalized_ids
	return result

static func validate_element_ids(element_ids: Array[String]) -> Array[String]:
	var failures: Array[String] = []
	var seen := {}
	for element_id in element_ids:
		var normalized := element_id.to_lower()
		if normalized == "seventh" or normalized == "seventh_reaction":
			failures.append("Seventh Reaction is a system consequence, not an element")
		elif not is_element(normalized):
			failures.append("Unsupported element presentation ID: %s" % element_id)
		elif seen.has(normalized):
			failures.append("Duplicate element presentation ID: %s" % normalized)
		else:
			seen[normalized] = true
	return failures
