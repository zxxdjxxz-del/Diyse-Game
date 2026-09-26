"""Deterministic, read-only construction of scene-local Person contexts.

No semantic search, model calls, wall-clock ordering, or personality inference here.
The compiler and both services use this module; SQLite remains person-local.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
from typing import Any

SCHEMA = "diyse_person_context_construction_v1"
EPISTEMIC_STATES = {
    "known_fact", "direct_observation", "trusted_report", "heard_claim",
    "inference", "suspicion", "assumption", "misunderstanding", "unknown",
    "forbidden_future",
}
RELATIONSHIP_DIMENSIONS = (
    "chronology_stage", "trust", "familiarity", "conflict_safety",
    "disagreement_tolerance", "teasing_permission", "profanity_vulgar_banter_permission",
    "affectionate_insult_permission", "physical_care_touch_permission_when_relevant",
    "favor_asking_comfort", "refusal_safety", "willingness_to_ask_preference",
    "willingness_to_state_preference", "ordinary_company_comfort", "silence_comfort",
    "disclosure_comfort", "shared_jokes_callbacks", "borrowed_language",
    "unresolved_friction", "recent_rupture", "recent_repair", "asymmetry_between_people",
)
LOCAL_KEYS = {
    "immediate_wants", "immediate_avoidances", "current_task", "physical_activity",
    "attention_target", "willing_to_discuss", "unwilling_to_discuss",
    "current_desire_to_speak", "interruption_trigger", "privacy_preference",
    "participation", "private_appraisal", "visible_behavior", "spoken_expression",
    "withheld_content",
}
HARD_KEYS = {
    "recruitment_status", "unlock_state", "equipment_restrictions", "knowledge_gates",
    "relationship_chronology_gate", "location_name", "area_phase", "party_state",
}


class ContextError(ValueError):
    pass


def fingerprint(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     separators=(",", ":")).encode()).hexdigest()


def clock(value: Any) -> tuple[int, int] | None:
    if not isinstance(value, dict):
        return None
    chapter, sequence = value.get("chapter"), value.get("sequence")
    if type(chapter) is int and 0 <= chapter <= 13 and type(sequence) is int and sequence >= 0:
        return chapter, sequence
    return None


def validate_plan(plan: dict[str, Any], participants: list[str]) -> None:
    if not isinstance(plan, dict) or plan.get("schema") != SCHEMA:
        raise ContextError("Unsupported context_construction schema")
    position = plan.get("story_clock", {})
    if not isinstance(position, dict):
        raise ContextError("story_clock must be an object")
    if not isinstance(plan.get("forward_only", False), bool):
        raise ContextError("forward_only must be boolean")
    reveals = plan.get("forbidden_reveals", [])
    if not isinstance(reveals, list) or any(not isinstance(x, str) for x in reveals):
        raise ContextError("forbidden_reveals must be a list of topic IDs")
    if position and clock(position) is None:
        raise ContextError("story_clock requires integer chapter (0..13) and sequence (>=0)")
    chapter_id = plan.get("chapter_id")
    if chapter_id is not None:
        if not isinstance(chapter_id, str) or not re.fullmatch(r"chapter_(0[0-9]|1[0-3])", chapter_id):
            raise ContextError("Invalid context chapter_id")
        if position and position["chapter"] != int(chapter_id[-2:]):
            raise ContextError("Context chapter_id and story_clock disagree")
    policies = plan.get("memory_policies", {})
    if not isinstance(policies, dict) or set(policies) - set(participants):
        raise ContextError("memory_policies must name only scene participants")
    for policy in [plan.get("continuity_policy", {"mode": "none"}), *policies.values()]:
        if not isinstance(policy, dict) or policy.get("mode") not in {
            "none", "explicit_ids", "scene_ids", "all_committed_story"}:
            raise ContextError("Invalid continuity authorization mode")
        for key in ("authorized_memory_ids", "authorized_scene_ids", "prior_scene_ids"):
            if key in policy and (not isinstance(policy[key], list) or
                                 any(not isinstance(x, str) or not x for x in policy[key])):
                raise ContextError(f"{key} must be a list of nonempty IDs")
        if policy.get("mode") == "all_committed_story" and (
                plan.get("forward_only") is not True or clock(position) is None):
            raise ContextError("all_committed_story requires forward_only and an exact story_clock")
    assertions = plan.get("assertions", [])
    if not isinstance(assertions, list):
        raise ContextError("assertions must be a list")
    ids: set[str] = set()
    for assertion in assertions:
        validate_effect(assertion)
        if assertion.get("owner_id") not in participants:
            raise ContextError("Assertion owner must be present")
        aid = assertion.get("id")
        if not isinstance(aid, str) or not aid or aid in ids:
            raise ContextError("Assertions require unique IDs")
        ids.add(aid)


def validate_request_authority(request: dict[str, Any]) -> None:
    packet = request.get("authority_packet", {})
    plan = request.get("context_construction", {"schema": SCHEMA})
    for key, value in plan.get("scene_identity", {}).items():
        if key not in {"scene_id", "story_position", "participants"} or request.get(key) != value:
            raise ContextError("Request differs from compiled scene identity")
    if packet:
        for key in ("scene_id", "canon_snapshot_id"):
            if packet.get(key) != request.get(key):
                raise ContextError(f"Authority packet {key} mismatch")
        if "context_construction" in packet and packet["context_construction"] != plan:
            raise ContextError("Context construction differs from compiled authority")
        if "bundle_sha256" in packet and fingerprint({key: value for key, value in packet.items()
                                                       if key != "bundle_sha256"}) != packet["bundle_sha256"]:
            raise ContextError("Authority bundle fingerprint mismatch")
        for cid, expected in packet.get("participant_profile_sources", {}).items():
            profile = request.get("participant_profiles", {}).get(cid, {})
            digest = hashlib.sha256(profile.get("authority_text", "").encode()).hexdigest()
            if digest != expected.get("file_sha256") or profile.get("source_path") != expected.get("source_path"):
                raise ContextError(f"Participant authority fingerprint mismatch: {cid}")


def validate_effect(effect: Any) -> None:
    if not isinstance(effect, dict):
        raise ContextError("Context effects must be objects")
    kind, key = effect.get("kind"), effect.get("key")
    if kind not in {"hard", "relationship", "epistemic", "thread", "local", "physical", "emotional"}:
        raise ContextError("Unsupported context effect kind")
    if not isinstance(key, str) or not key or "value" not in effect:
        raise ContextError("Context effects require key and value")
    if kind == "relationship" and (key not in RELATIONSHIP_DIMENSIONS or
                                    not isinstance(effect.get("target_id"), str)):
        raise ContextError("Relationship effect requires a supported dimension and target_id")
    if kind == "epistemic" and effect.get("status") not in EPISTEMIC_STATES:
        raise ContextError("Epistemic effect requires an explicit epistemic status")
    if kind == "hard" and key not in HARD_KEYS:
        raise ContextError("Unsupported hard context key")
    if kind == "local" and key not in LOCAL_KEYS:
        raise ContextError("Unsupported scene-local key")
    if kind == "local" and key == "participation" and effect["value"] not in ("optional", "silent", "nonparticipating"):
        raise ContextError("Unsupported participation state")
    if "applies_to_scene_ids" in effect and (not isinstance(effect["applies_to_scene_ids"], list) or
                                             any(not isinstance(x, str) for x in effect["applies_to_scene_ids"])):
        raise ContextError("applies_to_scene_ids must be a list of IDs")
    if kind == "thread" and effect.get("status") not in {"open", "resolved"}:
        raise ContextError("Thread effects require open or resolved status")


def authorize_memories(records: list[dict[str, Any]], request: dict[str, Any],
                       cid: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Intersect policy, ownership, visibility, provenance, version and chronology.

    Missing legacy metadata is not evidence of access. Rejected contents never leave
    this function. Every record is considered BEFORE any retrieval budget is applied.
    """
    plan = request.get("context_construction", {})
    policy = plan.get("memory_policies", {}).get(cid, plan.get("continuity_policy", {"mode": "none"}))
    mode = policy.get("mode", "none")
    now = clock(plan.get("story_clock"))
    chapter_id = plan.get("chapter_id", "")
    chapter = int(chapter_id[-2:]) if re.fullmatch(r"chapter_(0[0-9]|1[0-3])", chapter_id) else None
    prior = set(policy.get("prior_scene_ids", []))
    forbidden = {a["key"] for a in plan.get("assertions", [])
                 if a.get("owner_id") == cid and a.get("status") == "forbidden_future"}
    accepted = []
    denied: dict[str, int] = {}
    for record in records:
        reason = None
        mid = record.get("memory_id")
        scene = record.get("source_scene_id")
        then = clock(record.get("source_story_clock"))
        visibility = record.get("privacy_visibility_scope")
        visible = visibility == "private" or (
            isinstance(visibility, dict) and visibility.get("kind") in {"private", "shared"}
            and isinstance(visibility.get("allowed_character_ids"), list)
            and cid in visibility["allowed_character_ids"])
        if request.get("continuity_namespace", "story") != "story" or mode == "none":
            reason = "not_authorized"
        elif not mid or record.get("owner_id") != cid or not visible:
            reason = "ownership_or_privacy"
        elif (record.get("canon_snapshot_id") != request.get("canon_snapshot_id") or
              record.get("commit_provenance") != {"canon_check_status": "PASS", "author_approved": True}):
            reason = "unverified_or_stale"
        elif (scene == request.get("scene_id") or
              (chapter is not None and then is not None and then[0] > chapter) or
              (now is not None and then is not None and then >= now)):
            reason = "not_prior"
        elif not (now is not None and then is not None) and scene not in prior:
            reason = "unknown_chronology"
        elif (record.get("epistemic_status_at_acquisition") == "forbidden_future" or
              any(e.get("status") == "forbidden_future" or e.get("key") in forbidden
                  for e in record.get("context_effects", []) if isinstance(e, dict))):
            reason = "forbidden_knowledge"
        elif mode == "explicit_ids" and mid not in policy.get("authorized_memory_ids", []):
            reason = "not_authorized"
        elif mode == "scene_ids" and scene not in policy.get("authorized_scene_ids", []):
            reason = "not_authorized"
        elif mode == "all_committed_story" and (plan.get("forward_only") is not True or not now or not then):
            reason = "unsafe_forward_mode"
        elif mode not in {"explicit_ids", "scene_ids", "all_committed_story"}:
            reason = "not_authorized"
        if reason:
            denied[reason] = denied.get(reason, 0) + 1
        else:
            accepted.append(copy.deepcopy(record))
    accepted.sort(key=lambda row: (clock(row.get("source_story_clock")) or (-1, -1), row["memory_id"]))
    return accepted, {"mode": mode, "candidate_count": len(records),
                      "authorized_count": len(accepted), "denied_counts": denied,
                      "authorized_memory_ids": [row["memory_id"] for row in accepted]}


def identity_from_profile(profile: dict[str, Any]) -> dict[str, str]:
    """Only unambiguous stable identity bullets; no join/unlock/Prime projection."""
    text = profile.get("authority_text", "")
    result = {}
    for label, key in (("Full name", "full_name"), ("Age", "age"), ("Face", "face")):
        matches = re.findall(r"^- " + re.escape(label) + r":\s*(.+)$", text, re.M)
        if len(matches) == 1:
            result[key] = matches[0].replace("**", "").strip()
    return result


def hard_profile_rules(profile: dict[str, Any]) -> dict[str, Any]:
    text = profile.get("authority_text", "")
    labels = re.findall(r"^- Base / Subclass:\s*(.+)$", text, re.M)
    result: dict[str, Any] = {"class_labels_reference_only": labels[0].replace("**", "") if len(labels) == 1 else "unknown"}
    # Exact named restriction section; no NLP extraction from life/arc prose.
    match = re.search(r"^## Visual / combat identity firewall\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if match:
        result["equipment_identity_firewall"] = match.group(1).strip()
    return result


def build_person_context(request: dict[str, Any], cid: str,
                         records: list[dict[str, Any]] | None = None,
                         revision: str | None = None) -> dict[str, Any]:
    participants = request["participants"]
    if cid not in participants:
        raise ContextError("Cannot build context for a nonparticipant")
    validate_request_authority(request)
    plan = request.get("context_construction", {"schema": SCHEMA})
    validate_plan(plan, participants)
    memories, audit = authorize_memories(records or [], request, cid)
    profile = request.get("participant_profiles", {}).get(cid, {})
    hard = {"scene_id": request["scene_id"], "story_position": request["story_position"],
            "canon_snapshot_id": request["canon_snapshot_id"], "participant_id": cid,
            "participants": list(participants), "story_clock": plan.get("story_clock", {}),
            "forbidden_reveals": copy.deepcopy(plan.get("forbidden_reveals", [])),
            "identity": identity_from_profile(profile),
            "authority_bundle_sha256": request.get("authority_packet", {}).get("bundle_sha256"),
            "profile_source": {k: profile[k] for k in ("source_path", "file_sha256") if k in profile}}
    hard.update(hard_profile_rules(profile))
    hard.update({key: "unknown" for key in HARD_KEYS})
    scene = request.get("scene_context", {})
    observable = scene.get("runtime_observable", {})
    hard["runtime_observations"] = {key: copy.deepcopy(observable[key]) for key in (
        "field", "map", "recent_gameplay", "interaction", "encounter") if key in observable}
    for key in ("location_name", "area_phase"):
        if key in scene:
            hard[key] = copy.deepcopy(scene[key])
    context: dict[str, Any] = {
        "schema": SCHEMA, "hard_context": hard,
        "relationship_runtime_state": {other: {key: "unknown" for key in RELATIONSHIP_DIMENSIONS}
                                       for other in participants if other != cid},
        "epistemic_state": {}, "belief_history": {}, "open_threads": [],
        "default_epistemic_status": "unknown",
        "forbidden_scope": ["unauthorized_memory", "other_person_private_state", "future_reveals", "author_only_truth"],
        "scene_local_state": {"immediate_wants": [], "immediate_avoidances": [],
                              "attention_candidates": [], "current_desire_to_speak": "undecided",
                              "participation": "optional", "motive_candidates": [],
                              "motive_resolution": "open", "private_appraisal": "unknown",
                              "visible_behavior": "open", "spoken_expression": "open",
                              "withheld_content": []},
        "physical_state": {}, "emotional_state": {}, "forbidden_topics": [],
        "memory_authorization": ({"mode": "explicit_ids", "authorized_memory_ids": audit["authorized_memory_ids"]}
                                 if audit["mode"] != "none" else {"mode": "none"}),
        "memory_authorization_audit": audit, "provenance": {}, "unresolved_dependencies": [],
        "continuity_revision": revision,
    }
    # Index every legal effect before choosing salient recollections. Corrections,
    # boundaries, and thread closures must never be dropped by a retrieval budget.
    grouped: dict[tuple[str, str, str], list[dict[str, Any]]] = {}
    for memory in memories:
        for effect in memory.get("context_effects", []):
            try:
                validate_effect(effect)
            except ContextError:
                continue
            if effect["kind"] == "hard":
                continue  # Persistent memory cannot overwrite injected hard canon.
            if effect["kind"] in {"local", "physical", "emotional"} and request["scene_id"] not in effect.get("applies_to_scene_ids", []):
                continue  # Transient state does not silently survive rest/scene changes.
            entry = dict(effect, evidence_id=memory["memory_id"],
                         order=clock(memory.get("source_story_clock")), origin="memory")
            grouped.setdefault((effect["kind"], effect.get("target_id", ""), effect["key"]), []).append(entry)
    for assertion in plan.get("assertions", []):
        if assertion["owner_id"] != cid:
            continue
        entry = dict(assertion, evidence_id=assertion["id"], order=(99, 0), origin="scene_authority")
        grouped.setdefault((entry["kind"], entry.get("target_id", ""), entry["key"]), []).append(entry)

    for (kind, target, key), entries in sorted(grouped.items()):
        path = f"{kind}.{target + '.' if target else ''}{key}"
        current = [entry for entry in entries if entry["origin"] == "scene_authority"]
        pool = current or entries
        # An explicit prior-scene list proves access but does not sort those scenes.
        # Conflicting unordered values remain open, never ordered by insertion time.
        orders = [entry["order"] for entry in pool]
        latest = [entry for entry in pool if entry["order"] == max(orders)] if all(orders) else pool
        signatures = {fingerprint([entry["value"], entry.get("status")]) for entry in latest}
        conflict = len(signatures) > 1
        chosen = latest[-1]
        value = "unknown" if conflict else copy.deepcopy(chosen["value"])
        context["provenance"][path] = [entry["evidence_id"] for entry in latest]
        if conflict:
            context["unresolved_dependencies"].append(f"conflicting_evidence:{path}")
        if kind == "hard":
            hard[key] = value
        elif kind == "relationship" and target in context["relationship_runtime_state"]:
            context["relationship_runtime_state"][target][key] = value
        elif kind == "epistemic":
            status = "unknown" if conflict else chosen["status"]
            # Never pass future/unknown answer text to the person, even as a warning.
            context["epistemic_state"][key] = {"status": status,
                "value": None if status in {"unknown", "forbidden_future"} else value}
            if status == "forbidden_future":
                context["forbidden_topics"].append(key)
            context["belief_history"][key] = [
                {"evidence_id": entry["evidence_id"], "status": entry["status"],
                 "value": entry["value"] if entry["status"] not in {"unknown", "forbidden_future"} else None}
                for entry in entries if entry not in latest]
        elif kind == "thread" and (conflict or chosen["status"] == "open"):
            context["open_threads"].append({"thread_id": key, "value": value,
                                             "status": "unknown" if conflict else "open"})
        elif kind == "local":
            context["scene_local_state"][key] = value
        elif kind in {"physical", "emotional"}:
            context[f"{kind}_state"][key] = value

    local = context["scene_local_state"]
    for fact in observable.get("map", {}).get("visible_facts", []):
        local["attention_candidates"].append({"target": copy.deepcopy(fact), "basis": "direct_observation",
                                               "obligation_to_speak": False})
    if local.get("current_task") not in (None, "unknown", ""):
        local["motive_candidates"].append({"want": "address_current_task", "task": local["current_task"],
                                           "status": "inference", "persistent": False})
        local["attention_candidates"].append({"target": local["current_task"], "basis": "assigned_task"})
    for thread in context["open_threads"]:
        local["attention_candidates"].append({"target": thread["thread_id"], "basis": "open_thread",
                                              "obligation_to_speak": False})
    if local.get("participation") in {"silent", "nonparticipating"}:
        local["current_desire_to_speak"] = False
        local["spoken_expression"] = "none"
    for key in HARD_KEYS:
        if hard[key] == "unknown":
            context["unresolved_dependencies"].append(f"hard_context.{key}")
    if not hard["identity"]:
        context["unresolved_dependencies"].append("hard_context.identity")
    if hard["class_labels_reference_only"] == "unknown":
        context["unresolved_dependencies"].append("hard_context.class_labels_reference_only")
    for field in ("physical_state", "emotional_state"):
        if not context[field]:
            context["unresolved_dependencies"].append(field)
    context["context_sha256"] = fingerprint(context)
    return context


def select_salient_memories(memories: list[dict[str, Any]], limit: int = 12) -> list[dict[str, Any]]:
    """A deliberately simple ranking, only called on the fully authorized set."""
    def score(record: dict[str, Any]) -> float:
        values = [record.get(key, 0) for key in ("emotional_salience", "practical_salience")]
        return sum(float(value) for value in values if type(value) in (int, float))
    return sorted(memories, key=lambda row: (-score(row), row["memory_id"]))[:limit]


def memory_person_view(record: dict[str, Any], context: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(record)
    # A stored "current" label is current at acquisition, not at every later rewrite.
    result.pop("current_epistemic_status", None)
    result["as_of_epistemic_state"] = {effect["key"]: context["epistemic_state"][effect["key"]]
        for effect in record.get("context_effects", []) if effect.get("kind") == "epistemic"
        and effect.get("key") in context["epistemic_state"]}
    result["interpretation_rule"] = "historical_evidence_not_automatic_current_truth"
    return result


def person_request_view(request: dict[str, Any], cid: str, context: dict[str, Any]) -> dict[str, Any]:
    """Keep author-only source documents, other people's state and directives out.

    A Person receives explicit local evidence; the Director/Checker retain the full
    authority bundle. Adding a field to the author request never implicitly exposes it.
    """
    floor = request.get("current_floor_state", {})
    safe_floor = {}
    if floor.get("floor_owner") in context["hard_context"]["participants"]:
        safe_floor["floor_owner"] = floor["floor_owner"]
    if floor.get("interruption_window") in {"closed", "natural", "strong"}:
        safe_floor["interruption_window"] = floor["interruption_window"]
    return {key: copy.deepcopy(request[key]) for key in (
        "request_id", "scene_id", "continuity_namespace", "story_position", "canon_snapshot_id",
        "observable_scene_so_far") if key in request} | {
        "person_runtime_context": context,
        "current_floor_state": safe_floor,
    }
