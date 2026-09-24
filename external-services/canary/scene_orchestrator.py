from __future__ import annotations

import asyncio
import json
import os
import re
import uuid
from pathlib import Path
from typing import Any

import httpx
import uvicorn
import yaml
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

SERVICE_VERSION = os.getenv("SERVICE_VERSION", "2.20.0")
CANON_SNAPSHOT_ID = os.getenv("CANON_SNAPSHOT_ID", "development")
MODEL_API_URL = os.getenv("MODEL_API_URL") or None
MODEL_API_KEY = os.getenv("MODEL_API_KEY") or None
MODEL_NAME = os.getenv("MODEL_NAME") or None
ORCHESTRATOR_AUTH_TOKEN = os.getenv("ORCHESTRATOR_AUTH_TOKEN") or None
AGENT_AUTH_TOKEN = os.getenv("AGENT_AUTH_TOKEN") or None
PORT = int(os.getenv("PORT", "8090"))

BASE_DIR = Path(__file__).parent
CONTEXT_DIR = BASE_DIR / "context"
SAFE_ID = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")


def normalize_id(value: str) -> str:
    result = value.strip().lower().replace(" ", "_")
    if not SAFE_ID.fullmatch(result):
        raise HTTPException(400, f"Invalid character ID: {value!r}")
    return result


def load_shared_context() -> dict[str, Any]:
    result: dict[str, Any] = {}
    if CONTEXT_DIR.exists():
        for path in sorted(CONTEXT_DIR.glob("*.yaml")):
            result[path.stem] = yaml.safe_load(path.read_text(encoding="utf-8"))
    return result


SHARED_CONTEXT = load_shared_context()


def load_agent_urls() -> dict[str, str]:
    result: dict[str, str] = {}
    raw = os.getenv("AGENT_URLS_JSON")
    if raw:
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise RuntimeError("AGENT_URLS_JSON is not valid JSON") from exc
        if not isinstance(parsed, dict):
            raise RuntimeError("AGENT_URLS_JSON must be an object")
        for key, value in parsed.items():
            cid = str(key).strip().lower().replace(" ", "_")
            if SAFE_ID.fullmatch(cid) and value:
                result[cid] = str(value).rstrip("/")

    # Convenience env vars for the initial permanent-six deployments.
    for cid in ("cyanis", "ilyra", "torren", "nimera", "vaelira", "seyrik"):
        value = os.getenv(f"{cid.upper()}_AGENT_URL")
        if value:
            result[cid] = value.rstrip("/")
    return result


AGENT_URLS = load_agent_urls()


def require_auth(authorization: str | None):
    if not ORCHESTRATOR_AUTH_TOKEN:
        return
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(401, "Missing bearer token.")
    if authorization[7:] != ORCHESTRATOR_AUTH_TOKEN:
        raise HTTPException(403, "Invalid bearer token.")


def model_configured() -> bool:
    return bool(MODEL_API_URL and MODEL_API_KEY and MODEL_NAME)


async def model_json(system_prompt: str, payload: dict[str, Any]) -> dict[str, Any]:
    if not model_configured():
        raise HTTPException(
            503, "MODEL_API_URL, MODEL_API_KEY, and MODEL_NAME are not configured."
        )
    body = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
        ],
        "response_format": {"type": "json_object"},
    }
    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.post(
            MODEL_API_URL,
            headers={"Authorization": f"Bearer {MODEL_API_KEY}"},
            json=body,
        )
        response.raise_for_status()
        data = response.json()
    content = data["choices"][0]["message"]["content"]
    return content if isinstance(content, dict) else json.loads(content)


async def agent_request(
    character_id: str,
    method: str,
    path: str,
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    url = AGENT_URLS.get(character_id)
    if not url:
        raise HTTPException(503, f"No persistent agent URL configured for {character_id}.")
    headers = {}
    if AGENT_AUTH_TOKEN:
        headers["Authorization"] = f"Bearer {AGENT_AUTH_TOKEN}"
    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.request(
            method,
            f"{url}{path}",
            headers=headers,
            json=payload,
        )
    if response.status_code >= 400:
        try:
            detail: Any = response.json()
        except Exception:
            detail = response.text
        raise HTTPException(
            502,
            detail={
                "error": "agent_call_failed",
                "character_id": character_id,
                "status_code": response.status_code,
                "agent_detail": detail,
            },
        )
    return response.json()


class ExactLineAnchor(BaseModel):
    speaker_id: str
    text: str
    required: bool = True
    note: str | None = None


class SceneBuildRequest(BaseModel):
    request_id: str
    scene_id: str
    continuity_namespace: str = "story"
    story_position: str
    canon_snapshot_id: str
    participants: list[str]
    participant_profiles: dict[str, dict[str, Any]] = Field(default_factory=dict)
    scene_purpose: str
    authority_packet: dict[str, Any] = Field(default_factory=dict)
    scene_context: dict[str, Any] = Field(default_factory=dict)
    current_floor_state: dict[str, Any] = Field(default_factory=dict)
    allowed_information_transfers: list[Any] = Field(default_factory=list)
    exact_line_anchors: list[ExactLineAnchor] = Field(default_factory=list)
    max_beats: int = Field(default=18, ge=1, le=32)
    production_cost_ceiling: str = "economical"


class SceneCommitRequest(BaseModel):
    request_id: str
    scene_id: str
    canon_snapshot_id: str
    author_approved: bool
    canon_check_status: str
    per_character_event_ledgers: dict[str, dict[str, Any]]
    expected_previous_revisions: dict[str, str]


DIRECTOR_PROMPT = """
You are the Diyse Dialogue Director. Build a beat plan, not final prose.

Synthesize simultaneously:
- current story authority and reveal timing;
- the actual people present, their relationships and knowledge limits;
- committed personal continuity when supplied by persistent agents;
- recent gameplay and encounter pressure;
- physical location, sub-area and map-cell role;
- lived-world/economic pressure that is actually established;
- the scene's purpose;
- current economical HD-2D staging and production cost.

Diyse authoring mnemonic:
Talk like people. React like anime characters. Time jokes like a comedy. Structure important scenes
like a great RPG. Remember they are living through a war. Let ordinary life exist when the context earns it.

Hard rules:
- no player dialogue choices;
- no six-person or whole-room roll call merely because people are present;
- silence/nonparticipation are valid;
- no future, author-only, private-memory, or unsupported local knowledge;
- do not invent prices, wages, shortages, route states, preferences or lore facts;
- RED dialogue readiness does not support an ordinary long scene;
- preserve gameplay/encounter pressure rather than resetting it for convenience;
- no dialogue while player-controlled traversal is active; route dialogue requires an authored stop with movement locked;
- no dialogue during active combat; battle-related dialogue belongs before combat begins or after combat fully ends;
- required story comprehension does not live only in optional side-path dialogue;
- exact-line anchors marked required must be planned verbatim for the named speaker;
- current authority_packet outranks generic genre expectation.

Return JSON only:
{
  "scene_mode": "full_authored_stop_scene|post_battle_reaction|story_bearing_cell|character_life_hub_camp|boss_threshold|microbeat_or_defer",
  "dialogue_readiness": "GREEN|AMBER|RED",
  "production_cost_tier": "economical|moderate|bespoke",
  "movement_lock": true,
  "encounter_policy": {
    "during_scene": "preserve|temporarily_suppress_trigger|not_applicable",
    "after_scene": "restore_prior_pressure|continue_existing_state|not_applicable"
  },
  "director_notes": [],
  "beat_plan": [
    {
      "beat_id": "b01",
      "purpose": "short purpose",
      "eligible_speakers": ["character_id"],
      "allow_silence": true,
      "must_land": [],
      "must_avoid": [],
      "exact_line_anchor": null,
      "staging_intent": "short staging intention",
      "target_energy": "quiet|ordinary|comic|tense|urgent|grief|intimate|revelatory"
    }
  ],
  "return_to_gameplay": {
    "control_mode": "exploration|combat|cutscene_chain|hub",
    "handoff_note": "short note"
  }
}

Plan no more beats than requested. Prefer fewer beats when the point can land cleanly.
""".strip()


PROFILE_AGENT_PROMPT = """
You are a scene-bound Diyse Person Agent for the named character.

The supplied participant_profile is current character authority for this scene. Treat it as a person,
not a list of traits to recite. Use only that profile, supplied authority/story position, shared Diyse
world/economy/dialogue/scene context, allowed information transfers, and observable scene history.

Performance:
- mature adult speech appropriate to the specific person;
- cinematic subtext rather than therapy-summary dialogue;
- anime-readable action/reaction without stock anime behavior;
- relationship-specific humor/timing when supported;
- silence/nonparticipation are valid;
- do not become omniscient because the author profile contains information the character could not know here;
- ordinary trained Abilities and Standard Cards are familiar modern magic, not automatic mysteries;
- Prime Cards are disputed late-Diysean history with no verified modern holder/use; never invent operational Prime knowledge or personal Prime association.

This is a nonpersistent fallback profile. Do not fabricate previous private memories. Do not invent local
facts, prices, wages, shortages, route states, preferences, or future story knowledge.

Return JSON only with:
wants_to_speak, urgency, intent, emotional_posture, knowledge_basis, memory_refs,
observable_candidate {speech, action, silence}, claimed_facts, state_delta_proposal.
""".strip()


BEAT_EDITOR_PROMPT = """
You are the Diyse Dialogue Editor working one beat at a time.

Choose the most truthful Person-Agent candidate for the Director's beat target, or choose silence/action.
You may lightly edit the selected candidate's spoken wording for rhythm, clarity, interruption, naturalism
and comedy timing, but may not invent substantive facts, motives, memories, preferences, relationship
states, knowledge, or actions unsupported by the selected candidate and authority packet.

Craft contract:
- mature adult spoken language, not wiki prose;
- cinematic subtext rather than explicit emotional diagnosis;
- anime-readable expression/body language without stock reaction spam;
- comedy timing comes from the specific people and relationship;
- selective participation beats roll call;
- once the point lands, get out;
- visual/environmental information does not need full verbal description;
- economical HD-2D staging uses existing field models, portraits, facing, small gestures, camera, light,
  sound, props, background motion and state swaps before expensive one-use animation.

If an exact_line_anchor is supplied, use that text verbatim and the named speaker.
No player dialogue choices.

Return JSON only:
{
  "beat_id": "b01",
  "selected_speaker_id": "character_id|null",
  "text": "spoken text or empty string",
  "action": "visible action or empty string",
  "silence": false,
  "expression_id": null,
  "portrait_side": "left|right|none",
  "staging_cues": [],
  "claimed_facts": [],
  "source_candidate_character_ids": ["character_id"],
  "editor_note": "short rationale"
}
""".strip()


CANON_CHECKER_PROMPT = """
You are the Diyse Canon Checker.

Audit the complete drafted scene against the supplied current authority packet, story position,
knowledge firewall, participants/profiles, exact-line anchors, map/gameplay state, lived-world/economy
rules, candidate provenance, and Dialogue Engine craft rules.

PASS requires:
- no future/author-only knowledge leak;
- no private memory transfer without authorization;
- no stale/conflicting terminology when current authority is supplied;
- no invented fixed local facts, prices, wages, route conditions, shortages, preferences or lore;
- required exact-line anchors appear verbatim from the required speaker;
- mandatory story facts land and forbidden reveals remain absent;
- valid participant/speaker identity;
- no dialogue during player-controlled traversal;
- no dialogue during active combat;
- no player dialogue choices;
- staging implies no illegal gameplay action;
- traversal/encounter pressure is respected;
- pacing matches map-cell role/dialogue readiness;
- voices remain adult, specific, and not flattened into one party voice;
- staging fits the production cost ceiling.

Do not silently rewrite a failed scene. Report failure for regeneration.

For PASS, produce conservative durable-memory ledgers only for the persistent_agent_ids supplied.
A character only receives memories they could plausibly observe/learn. Do not store every line.
Profile-only participants may receive memory proposals separately, but they are not automatically committed.
Do not propose whole-state replacement.

Return JSON only:
{
  "status": "PASS|FAIL",
  "violations": [],
  "warnings": [],
  "knowledge_firewall_checks": [],
  "story_requirement_checks": [],
  "map_gameplay_checks": [],
  "performance_checks": [],
  "per_character_event_ledgers": {},
  "profile_only_memory_proposals": {},
  "state_delta_proposals": {}
}
""".strip()


def normalized_participants(req: SceneBuildRequest) -> tuple[list[str], dict[str, dict[str, Any]]]:
    participants: list[str] = []
    seen: set[str] = set()
    for raw in req.participants:
        cid = normalize_id(raw)
        if cid not in seen:
            participants.append(cid)
            seen.add(cid)

    if not participants:
        raise HTTPException(400, "At least one participant is required.")

    profiles: dict[str, dict[str, Any]] = {}
    for raw_id, profile in req.participant_profiles.items():
        cid = normalize_id(raw_id)
        profiles[cid] = profile

    missing = [cid for cid in participants if cid not in AGENT_URLS and cid not in profiles]
    if missing:
        raise HTTPException(
            400,
            detail={
                "error": "participant_has_no_person_source",
                "character_ids": missing,
                "fix": "configure a persistent agent URL or supply participant_profiles for these people",
            },
        )
    return participants, profiles


def profile_person_view(profile: dict[str, Any]) -> dict[str, Any]:
    """Return character-facing profile data with author-only Prime assignment removed."""
    result = dict(profile)

    # Scene-authority compiler profiles carry the complete character Markdown in
    # authority_text. Story Prime assignment is author metadata, not pre-reveal
    # character knowledge.
    authority_text = result.get("authority_text")
    if isinstance(authority_text, str):
        result["authority_text"] = "\n".join(
            line
            for line in authority_text.splitlines()
            if not re.match(r"^\s*-\s*Story Prime\s*:", line, flags=re.IGNORECASE)
        )

    for key in list(result.keys()):
        normalized = str(key).strip().lower().replace("-", "_").replace(" ", "_")
        if normalized in {"prime", "story_prime", "prime_card", "story_prime_association"}:
            result.pop(key, None)

    return result


def validate_anchors(anchors: list[ExactLineAnchor], participants: list[str]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for anchor in anchors:
        speaker_id = normalize_id(anchor.speaker_id)
        if speaker_id not in participants:
            raise HTTPException(
                400,
                f"Exact-line anchor speaker {speaker_id} is not a scene participant.",
            )
        item = anchor.model_dump()
        item["speaker_id"] = speaker_id
        result.append(item)
    return result


def validate_director_plan(plan: dict[str, Any], participants: list[str], max_beats: int):
    allowed_scene_modes = {
        "full_authored_stop_scene",
        "post_battle_reaction",
        "story_bearing_cell",
        "character_life_hub_camp",
        "boss_threshold",
        "microbeat_or_defer",
    }
    scene_mode = plan.get("scene_mode")
    if scene_mode not in allowed_scene_modes:
        raise HTTPException(502, f"Dialogue Director returned unsupported scene_mode: {scene_mode}")
    if scene_mode != "microbeat_or_defer" and not bool(plan.get("movement_lock", True)):
        raise HTTPException(502, "Dialogue scenes require movement_lock; walking/traversal dialogue is not supported.")

    beats = plan.get("beat_plan")
    if not isinstance(beats, list):
        raise HTTPException(502, "Dialogue Director did not return beat_plan as a list.")
    if len(beats) > max_beats:
        del beats[max_beats:]

    for index, beat in enumerate(beats, start=1):
        if not isinstance(beat, dict):
            raise HTTPException(502, "Dialogue Director returned an invalid beat entry.")
        beat.setdefault("beat_id", f"b{index:02d}")
        eligible: list[str] = []
        for raw in beat.get("eligible_speakers", []):
            try:
                cid = normalize_id(str(raw))
            except HTTPException:
                continue
            if cid in participants and cid not in eligible:
                eligible.append(cid)
        beat["eligible_speakers"] = eligible
        if not eligible:
            beat["allow_silence"] = True


def local_scene_checks(
    anchors: list[dict[str, Any]],
    participants: list[str],
    scene_beats: list[dict[str, Any]],
) -> list[str]:
    violations: list[str] = []
    for anchor in anchors:
        if not anchor.get("required", True):
            continue
        matched = any(
            beat.get("selected_speaker_id") == anchor["speaker_id"]
            and beat.get("text") == anchor["text"]
            for beat in scene_beats
        )
        if not matched:
            violations.append(
                f"Required exact-line anchor missing or altered for {anchor['speaker_id']}: {anchor['text']}"
            )

    for beat in scene_beats:
        speaker = beat.get("selected_speaker_id")
        if speaker not in (None, "null") and speaker not in participants:
            violations.append(f"Beat {beat.get('beat_id')} uses nonparticipant speaker {speaker}.")
        if "choices" in beat:
            violations.append(f"Beat {beat.get('beat_id')} contains player dialogue choices.")
    return violations


def make_godot_packet(
    req: SceneBuildRequest,
    director_plan: dict[str, Any],
    scene_beats: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "schema": "diyse_dialogue_scene_packet_v1",
        "scene_id": req.scene_id,
        "story_position": req.story_position,
        "scene_mode": director_plan.get("scene_mode"),
        "movement_lock": bool(director_plan.get("movement_lock", True)),
        "dialogue_readiness": director_plan.get("dialogue_readiness"),
        "production_cost_tier": director_plan.get("production_cost_tier"),
        "encounter_policy": director_plan.get("encounter_policy", {}),
        "beats": [
            {
                "beat_id": beat.get("beat_id"),
                "speaker_id": None
                if beat.get("selected_speaker_id") in (None, "null")
                else beat.get("selected_speaker_id"),
                "body_text": beat.get("text", ""),
                "silent": bool(beat.get("silence", False)),
                "action": beat.get("action", ""),
                "expression_id": beat.get("expression_id"),
                "portrait_side": beat.get("portrait_side", "none"),
                "cues": beat.get("staging_cues", []),
            }
            for beat in scene_beats
        ],
        "return_to_gameplay": director_plan.get("return_to_gameplay", {}),
    }


app = FastAPI(title="Diyse Dialogue Scene Orchestrator", version=SERVICE_VERSION)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service_version": SERVICE_VERSION,
        "canon_snapshot_id": CANON_SNAPSHOT_ID,
        "model_configured": model_configured(),
        "persistent_agent_ids": sorted(AGENT_URLS.keys()),
        "shared_context_sections": sorted(SHARED_CONTEXT.keys()),
    }


@app.post("/v1/scene/build")
async def build_scene(
    req: SceneBuildRequest,
    authorization: str | None = Header(default=None),
):
    require_auth(authorization)
    if req.continuity_namespace not in {"story", "sandbox"}:
        raise HTTPException(400, "Invalid continuity namespace.")
    if req.continuity_namespace == "story" and req.canon_snapshot_id != CANON_SNAPSHOT_ID:
        raise HTTPException(409, "Canon snapshot mismatch.")

    participants, profiles = normalized_participants(req)
    anchors = validate_anchors(req.exact_line_anchors, participants)
    persistent_ids = [cid for cid in participants if cid in AGENT_URLS]
    profile_only_ids = [cid for cid in participants if cid not in AGENT_URLS]

    async def get_snapshot(cid: str) -> tuple[str, dict[str, Any]]:
        return cid, await agent_request(cid, "GET", "/v1/context-snapshot")

    snapshot_pairs = await asyncio.gather(*(get_snapshot(cid) for cid in persistent_ids))
    agent_snapshots = {cid: snapshot for cid, snapshot in snapshot_pairs}

    director_payload = {
        **req.model_dump(),
        "participants": participants,
        "participant_profiles": profiles,
        "persistent_agent_ids": persistent_ids,
        "profile_only_ids": profile_only_ids,
        "exact_line_anchors": anchors,
        "agent_public_state_snapshots": agent_snapshots,
        "shared_context": SHARED_CONTEXT,
    }
    director_plan = await model_json(DIRECTOR_PROMPT, director_payload)
    validate_director_plan(director_plan, participants, req.max_beats)

    scene_beats: list[dict[str, Any]] = []
    candidate_audit: list[dict[str, Any]] = []

    for beat_index, beat_target in enumerate(director_plan.get("beat_plan", []), start=1):
        eligible = list(beat_target.get("eligible_speakers", []))
        anchor = beat_target.get("exact_line_anchor")
        if isinstance(anchor, dict) and anchor.get("speaker_id"):
            anchor_id = normalize_id(str(anchor["speaker_id"]))
            if anchor_id in participants:
                eligible = [anchor_id]

        observable_scene = [
            {
                "beat_id": beat.get("beat_id"),
                "speaker_id": beat.get("selected_speaker_id"),
                "speech": beat.get("text", ""),
                "action": beat.get("action", ""),
                "silence": beat.get("silence", False),
            }
            for beat in scene_beats
        ]

        if not eligible and beat_target.get("allow_silence", False):
            scene_beats.append(
                {
                    "beat_id": beat_target.get("beat_id", f"b{beat_index:02d}"),
                    "selected_speaker_id": None,
                    "text": "",
                    "action": "",
                    "silence": True,
                    "expression_id": None,
                    "portrait_side": "none",
                    "staging_cues": [beat_target.get("staging_intent", "hold")],
                    "claimed_facts": [],
                    "source_candidate_character_ids": [],
                    "editor_note": "Director-authored silent beat.",
                }
            )
            continue

        async def fetch_candidate(cid: str) -> tuple[str, str, dict[str, Any]]:
            scene_context = {
                **req.scene_context,
                "scene_purpose": req.scene_purpose,
                "authority_packet": req.authority_packet,
                "director_scene_mode": director_plan.get("scene_mode"),
                "dialogue_readiness": director_plan.get("dialogue_readiness"),
                "beat_target": beat_target,
                "production_cost_ceiling": req.production_cost_ceiling,
            }
            if cid in AGENT_URLS:
                payload = {
                    "request_id": f"{req.request_id}:{beat_target.get('beat_id', beat_index)}:{cid}",
                    "scene_id": req.scene_id,
                    "continuity_namespace": req.continuity_namespace,
                    "story_position": req.story_position,
                    "canon_snapshot_id": req.canon_snapshot_id,
                    "observable_scene_so_far": observable_scene,
                    "scene_context": scene_context,
                    "current_floor_state": req.current_floor_state,
                    "allowed_information_transfers": req.allowed_information_transfers,
                }
                return cid, "persistent", await agent_request(cid, "POST", "/v1/turn", payload)

            profile_payload = {
                "character_id": cid,
                "participant_profile": profile_person_view(profiles[cid]),
                "story_position": req.story_position,
                "authority_packet": req.authority_packet,
                "observable_scene_so_far": observable_scene,
                "scene_context": scene_context,
                "current_floor_state": req.current_floor_state,
                "allowed_information_transfers": req.allowed_information_transfers,
                "shared_context": SHARED_CONTEXT,
            }
            return cid, "profile", await model_json(PROFILE_AGENT_PROMPT, profile_payload)

        candidate_rows = await asyncio.gather(*(fetch_candidate(cid) for cid in eligible))
        candidates = [
            {"character_id": cid, "source": source, "candidate": candidate}
            for cid, source, candidate in candidate_rows
        ]
        candidate_audit.append(
            {
                "beat_id": beat_target.get("beat_id"),
                "eligible_speakers": eligible,
                "candidates": candidates,
            }
        )

        editor_payload = {
            "scene_id": req.scene_id,
            "story_position": req.story_position,
            "scene_purpose": req.scene_purpose,
            "authority_packet": req.authority_packet,
            "participants": participants,
            "participant_profiles": profiles,
            "scene_context": req.scene_context,
            "director_plan": director_plan,
            "beat_target": beat_target,
            "observable_scene_so_far": observable_scene,
            "agent_candidates": candidates,
            "exact_line_anchors": anchors,
            "shared_context": SHARED_CONTEXT,
            "production_cost_ceiling": req.production_cost_ceiling,
        }
        edited = await model_json(BEAT_EDITOR_PROMPT, editor_payload)
        edited.setdefault("beat_id", beat_target.get("beat_id", f"b{beat_index:02d}"))
        scene_beats.append(edited)

    local_violations = local_scene_checks(anchors, participants, scene_beats)
    checker_payload = {
        "scene_id": req.scene_id,
        "story_position": req.story_position,
        "scene_purpose": req.scene_purpose,
        "canon_snapshot_id": req.canon_snapshot_id,
        "authority_packet": req.authority_packet,
        "participants": participants,
        "participant_profiles": profiles,
        "persistent_agent_ids": persistent_ids,
        "profile_only_ids": profile_only_ids,
        "allowed_information_transfers": req.allowed_information_transfers,
        "exact_line_anchors": anchors,
        "scene_context": req.scene_context,
        "current_floor_state": req.current_floor_state,
        "director_plan": director_plan,
        "draft_scene_beats": scene_beats,
        "candidate_audit": candidate_audit,
        "local_violations": local_violations,
        "shared_context": SHARED_CONTEXT,
        "production_cost_ceiling": req.production_cost_ceiling,
    }
    canon_check = await model_json(CANON_CHECKER_PROMPT, checker_payload)

    if local_violations:
        canon_check["status"] = "FAIL"
        merged = list(canon_check.get("violations", []))
        for violation in local_violations:
            if violation not in merged:
                merged.append(violation)
        canon_check["violations"] = merged

    if canon_check.get("status") != "PASS":
        canon_check["per_character_event_ledgers"] = {}

    # Never expose a profile-only character as automatically committable.
    persistent_ledgers = {
        cid: ledger
        for cid, ledger in canon_check.get("per_character_event_ledgers", {}).items()
        if cid in persistent_ids
    }
    canon_check["per_character_event_ledgers"] = persistent_ledgers

    return {
        "draft_id": str(uuid.uuid4()),
        "request_id": req.request_id,
        "scene_id": req.scene_id,
        "canon_snapshot_id": req.canon_snapshot_id,
        "participant_sources": {
            cid: "persistent" if cid in persistent_ids else "profile"
            for cid in participants
        },
        "agent_snapshots": agent_snapshots,
        "expected_previous_revisions": {
            cid: str(snapshot.get("story_revision", "0"))
            for cid, snapshot in agent_snapshots.items()
        },
        "director_plan": director_plan,
        "scene_beats": scene_beats,
        "canon_check": canon_check,
        "commit_ready": canon_check.get("status") == "PASS",
        "commit_bundle": {
            "canon_check_status": canon_check.get("status"),
            "per_character_event_ledgers": persistent_ledgers,
            "profile_only_memory_proposals": canon_check.get(
                "profile_only_memory_proposals", {}
            ),
            "state_delta_proposals": canon_check.get("state_delta_proposals", {}),
        },
        "godot_handoff": make_godot_packet(req, director_plan, scene_beats),
        "candidate_audit": candidate_audit,
    }


@app.post("/v1/scene/commit")
async def commit_scene(
    req: SceneCommitRequest,
    authorization: str | None = Header(default=None),
):
    require_auth(authorization)
    if not req.author_approved:
        raise HTTPException(400, "Story scene commit requires explicit author approval.")
    if req.canon_check_status != "PASS":
        raise HTTPException(400, "Only a Canon Checker PASS may be committed.")
    if req.canon_snapshot_id != CANON_SNAPSHOT_ID:
        raise HTTPException(409, "Canon snapshot mismatch.")

    character_ids = sorted(req.per_character_event_ledgers.keys())
    for cid in character_ids:
        normalized = normalize_id(cid)
        if normalized != cid:
            raise HTTPException(400, f"Commit character ID must be normalized: {cid}")
        if cid not in AGENT_URLS:
            raise HTTPException(400, f"Cannot commit profile-only character {cid}.")
        if cid not in req.expected_previous_revisions:
            raise HTTPException(400, f"Missing expected revision for {cid}.")

    async def commit_one(cid: str) -> tuple[str, dict[str, Any]]:
        ledger = dict(req.per_character_event_ledgers[cid])
        ledger.setdefault("scene_id", req.scene_id)
        payload = {
            "request_id": f"{req.request_id}:commit:{cid}",
            "scene_id": req.scene_id,
            "canon_snapshot_id": req.canon_snapshot_id,
            "canon_check_status": "PASS",
            "filtered_event_ledger": ledger,
            "expected_previous_revision": req.expected_previous_revisions[cid],
        }
        return cid, await agent_request(cid, "POST", "/v1/commit", payload)

    results = await asyncio.gather(*(commit_one(cid) for cid in character_ids))
    return {
        "committed": True,
        "scene_id": req.scene_id,
        "character_results": {cid: result for cid, result in results},
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
