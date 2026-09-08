extends RefCounted
class_name DiyseDialogueScenePacketImporter

const PACKET_SCHEMA := "diyse_dialogue_scene_packet_v1"
const ALLOWED_PORTRAIT_SIDES := ["left", "right", "none"]

func validate_packet(packet: Dictionary) -> Array[String]:
	var failures: Array[String] = []
	if str(packet.get("schema", "")) != PACKET_SCHEMA:
		failures.append("Unsupported Dialogue Engine packet schema: %s" % str(packet.get("schema", "")))
	if str(packet.get("scene_id", "")).is_empty():
		failures.append("packet.scene_id is required")
	if str(packet.get("story_position", "")).is_empty():
		failures.append("packet.story_position is required")

	var scene_mode := str(packet.get("scene_mode", ""))
	if scene_mode not in DiyseDialogueSceneDefinition.ALLOWED_SCENE_MODES:
		failures.append("Unsupported packet.scene_mode: %s" % scene_mode)
	var readiness := str(packet.get("dialogue_readiness", ""))
	if readiness not in DiyseDialogueSceneDefinition.ALLOWED_DIALOGUE_READINESS:
		failures.append("Unsupported packet.dialogue_readiness: %s" % readiness)
	var cost_tier := str(packet.get("production_cost_tier", ""))
	if cost_tier not in DiyseDialogueSceneDefinition.ALLOWED_PRODUCTION_COST_TIERS:
		failures.append("Unsupported packet.production_cost_tier: %s" % cost_tier)

	if not packet.has("movement_lock") or not (packet.get("movement_lock") is bool):
		failures.append("packet.movement_lock must be a bool")
	if not (packet.get("encounter_policy", {}) is Dictionary):
		failures.append("packet.encounter_policy must be a Dictionary")
	if not (packet.get("return_to_gameplay", {}) is Dictionary):
		failures.append("packet.return_to_gameplay must be a Dictionary")

	var beats_value = packet.get("beats", [])
	if not (beats_value is Array):
		failures.append("packet.beats must be an Array")
		return failures
	var beats: Array = beats_value
	if beats.is_empty():
		failures.append("packet.beats must contain at least one beat")
		return failures

	var seen_ids: Dictionary = {}
	for i in range(beats.size()):
		var value = beats[i]
		var prefix := "packet.beats[%d]" % i
		if not (value is Dictionary):
			failures.append("%s must be a Dictionary" % prefix)
			continue
		var beat: Dictionary = value
		var beat_id := str(beat.get("beat_id", ""))
		if beat_id.is_empty():
			failures.append("%s.beat_id is required" % prefix)
		elif seen_ids.has(beat_id):
			failures.append("Duplicate packet beat_id: %s" % beat_id)
		else:
			seen_ids[beat_id] = true

		var speaker_id := _string_or_empty(beat.get("speaker_id", null))
		var body_text := str(beat.get("body_text", ""))
		var silent := bool(beat.get("silent", false))
		if speaker_id.is_empty() and not body_text.is_empty():
			failures.append("%s has body_text but no speaker_id" % prefix)
		if silent and (not speaker_id.is_empty() or not body_text.is_empty()):
			failures.append("%s is marked silent but also contains speaker/text" % prefix)

		var portrait_side := str(beat.get("portrait_side", "none"))
		if portrait_side not in ALLOWED_PORTRAIT_SIDES:
			failures.append("%s has unsupported portrait_side: %s" % [prefix, portrait_side])
		var cues = beat.get("cues", [])
		if not (cues is Array) and not (cues is Dictionary):
			failures.append("%s.cues must be an Array or Dictionary" % prefix)
	return failures

func validate_authoring_metadata(metadata: Dictionary) -> Array[String]:
	var failures: Array[String] = []
	var required_string_keys := [
		"chapter_id",
		"scene_kind",
		"completion_flag",
		"cutscene_tier",
		"vfx_tier",
	]
	for key in required_string_keys:
		if str(metadata.get(key, "")).is_empty():
			failures.append("authoring metadata.%s is required" % key)
	if not (metadata.get("participants", []) is Array):
		failures.append("authoring metadata.participants must be an Array")
	elif (metadata.get("participants", []) as Array).is_empty():
		failures.append("authoring metadata.participants must not be empty")
	return failures

func build_scene(
	packet: Dictionary,
	metadata: Dictionary,
	registry: DiyseDialoguePortraitRegistry = null
) -> Dictionary:
	var failures := validate_packet(packet)
	failures.append_array(validate_authoring_metadata(metadata))
	if not failures.is_empty():
		return {"scene": null, "failures": failures}

	var scene := DiyseDialogueSceneDefinition.new()
	scene.scene_id = str(packet.get("scene_id", ""))
	if metadata.has("scene_id") and str(metadata.get("scene_id", "")) != scene.scene_id:
		failures.append("authoring metadata.scene_id does not match packet.scene_id")
		return {"scene": null, "failures": failures}

	scene.chapter_id = str(metadata.get("chapter_id", ""))
	scene.scene_kind = str(metadata.get("scene_kind", "mandatory"))
	scene.location_id = str(metadata.get("location_id", ""))
	scene.trigger_id = str(metadata.get("trigger_id", ""))
	scene.completion_flag = str(metadata.get("completion_flag", ""))
	scene.participants = _string_array(metadata.get("participants", []))
	scene.story_position = str(packet.get("story_position", ""))
	scene.scene_mode = str(packet.get("scene_mode", "full_authored_stop_scene"))
	scene.movement_lock = bool(packet.get("movement_lock", true))
	scene.dialogue_readiness = str(packet.get("dialogue_readiness", "GREEN"))
	scene.production_cost_tier = str(packet.get("production_cost_tier", "economical"))
	scene.encounter_policy = (packet.get("encounter_policy", {}) as Dictionary).duplicate(true)
	scene.return_to_gameplay = (packet.get("return_to_gameplay", {}) as Dictionary).duplicate(true)

	# These values come from current authored implementation/story metadata. The importer
	# deliberately does not derive them from production_cost_tier or scene_mode.
	scene.cutscene_tier = str(metadata.get("cutscene_tier", ""))
	scene.vfx_tier = str(metadata.get("vfx_tier", ""))
	scene.presentation_tags = _string_array(metadata.get("presentation_tags", []))
	scene.battle_background_family = str(metadata.get("battle_background_family", ""))
	scene.authoring_notes = str(metadata.get("authoring_notes", ""))

	var left_slot: Dictionary = {}
	var right_slot: Dictionary = {}
	var authored_beats: Array[Dictionary] = []
	var packet_beats: Array = packet.get("beats", [])
	for value in packet_beats:
		var incoming: Dictionary = value
		var speaker_id := _string_or_empty(incoming.get("speaker_id", null))
		var expression_id := _string_or_empty(incoming.get("expression_id", null))
		var portrait_side := str(incoming.get("portrait_side", "none"))

		# Portrait state persists from beat to beat, matching the existing Resource grammar.
		# A new expression updates the requested slot. If the Director gives portrait_side
		# "none", an already-visible slot for the same speaker may still update expression.
		if not speaker_id.is_empty() and not expression_id.is_empty():
			if portrait_side == "left":
				left_slot = {"character_id": speaker_id, "expression_id": expression_id}
			elif portrait_side == "right":
				right_slot = {"character_id": speaker_id, "expression_id": expression_id}
			elif str(left_slot.get("character_id", "")) == speaker_id:
				left_slot["expression_id"] = expression_id
			elif str(right_slot.get("character_id", "")) == speaker_id:
				right_slot["expression_id"] = expression_id

		var active_side := "none"
		if not speaker_id.is_empty():
			if str(left_slot.get("character_id", "")) == speaker_id:
				active_side = "left"
			elif str(right_slot.get("character_id", "")) == speaker_id:
				active_side = "right"
		elif portrait_side == "left" and not left_slot.is_empty():
			active_side = "left"
		elif portrait_side == "right" and not right_slot.is_empty():
			active_side = "right"

		var cues := _normalize_cues(incoming)
		authored_beats.append({
			"beat_id": str(incoming.get("beat_id", "")),
			"speaker_id": speaker_id,
			"text": str(incoming.get("body_text", "")),
			"left": left_slot.duplicate(true),
			"right": right_slot.duplicate(true),
			"active_side": active_side,
			"advance_mode": "manual",
			"cues": cues,
		})

	scene.beats = authored_beats
	failures.append_array(scene.validate_schema(registry))
	return {"scene": scene, "failures": failures}

func _normalize_cues(beat: Dictionary) -> Dictionary:
	var incoming = beat.get("cues", [])
	var result: Dictionary = {}
	if incoming is Dictionary:
		result = (incoming as Dictionary).duplicate(true)
	elif incoming is Array and not (incoming as Array).is_empty():
		result["staging"] = (incoming as Array).duplicate(true)

	var action := str(beat.get("action", ""))
	if not action.is_empty():
		result["action"] = action
	if bool(beat.get("silent", false)):
		result["silent"] = true
	result["source"] = PACKET_SCHEMA
	return result

func _string_array(value: Variant) -> Array[String]:
	var result: Array[String] = []
	if not (value is Array):
		return result
	for item in value:
		var text := str(item)
		if not text.is_empty():
			result.append(text)
	return result

func _string_or_empty(value: Variant) -> String:
	if value == null:
		return ""
	return str(value)
