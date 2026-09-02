extends RefCounted
class_name DiyseKessaraRelicCopyService

const MAX_RELIC_COPIES_PER_FACE := 3
const SERVICE_FEE_G := 6000

const RESULT_OK := "ok"
const RESULT_INVALID_STATE := "invalid_state"
const RESULT_RELIC_NOT_OBTAINED := "relic_not_obtained"
const RESULT_ALREADY_COPIED := "already_copied"
const RESULT_FACE_COPY_LIMIT := "face_copy_limit"
const RESULT_NO_MATCHING_COMPONENT := "no_matching_component"
const RESULT_INSUFFICIENT_G := "insufficient_g"
const RESULT_COMMIT_FAILED := "commit_failed"

func evaluate(state, relic_id: String) -> Dictionary:
	if state == null:
		return _failure(RESULT_INVALID_STATE, "Kessara's Relic-copy service requires a valid game state.")
	for required_method in [
		"has_relic_original",
		"has_forged_relic_copy",
		"relic_face",
		"relic_quantity",
		"forged_relic_count_for_face",
		"available_relic_copy_component_for_face",
		"wallet_balance_g",
		"can_afford_g"
	]:
		if not state.has_method(required_method):
			return _failure(RESULT_INVALID_STATE, "Game state does not expose the Relic-copy ownership/economy contract.")

	var normalized_id := relic_id.strip_edges()
	if normalized_id.is_empty() or not bool(state.call("has_relic_original", normalized_id)):
		return _failure(RESULT_RELIC_NOT_OBTAINED, "The original Relic must already be obtained before Kessara can copy it.")
	if bool(state.call("has_forged_relic_copy", normalized_id)) or int(state.call("relic_quantity", normalized_id)) >= 2:
		return _failure(RESULT_ALREADY_COPIED, "An individual Relic may be forged only once.")

	var face := str(state.call("relic_face", normalized_id))
	if int(state.call("forged_relic_count_for_face", face)) >= MAX_RELIC_COPIES_PER_FACE:
		return _failure(RESULT_FACE_COPY_LIMIT, "All three Relic-copy opportunities for this Face have already been used.")

	var component_id := str(state.call("available_relic_copy_component_for_face", face))
	if component_id.is_empty():
		return _failure(RESULT_NO_MATCHING_COMPONENT, "A matching-Face Relic-copy Forge Component is required.")
	if not bool(state.call("can_afford_g", SERVICE_FEE_G)):
		return _failure(RESULT_INSUFFICIENT_G, "Kessara's Relic-copy service costs 6,000 G.")

	var wallet_before := int(state.call("wallet_balance_g"))
	return {
		"ok": true,
		"code": RESULT_OK,
		"relic_id": normalized_id,
		"face": face,
		"component_id": component_id,
		"quantity_before": int(state.call("relic_quantity", normalized_id)),
		"quantity_after": 2,
		"fee_g": SERVICE_FEE_G,
		"wallet_before_g": wallet_before,
		"wallet_after_g": wallet_before - SERVICE_FEE_G
	}

func forge_copy(state, relic_id: String) -> Dictionary:
	var evaluation := evaluate(state, relic_id)
	if not bool(evaluation.get("ok", false)):
		return evaluation
	if not state.has_method("commit_relic_copy_with_g_fee"):
		return _failure(RESULT_INVALID_STATE, "Game state cannot commit the Relic copy and G fee atomically.")

	var normalized_id := str(evaluation.get("relic_id", ""))
	var component_id := str(evaluation.get("component_id", ""))
	if not bool(state.call("commit_relic_copy_with_g_fee", normalized_id, component_id, SERVICE_FEE_G)):
		return _failure(RESULT_COMMIT_FAILED, "Relic-copy state or available G changed before the forge could be committed.")

	return {
		"ok": true,
		"code": RESULT_OK,
		"relic_id": normalized_id,
		"face": str(evaluation.get("face", "")),
		"component_id": component_id,
		"quantity": int(state.call("relic_quantity", normalized_id)),
		"forged_copy": true,
		"fee_g": SERVICE_FEE_G,
		"wallet_g": int(state.call("wallet_balance_g"))
	}

func _failure(code: String, message: String) -> Dictionary:
	return {"ok": false, "code": code, "message": message}
