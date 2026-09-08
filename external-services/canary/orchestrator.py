from __future__ import annotations

import asyncio
import json
import os
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

CANONICAL_CHARACTER_IDS = {
    "cyanis",
    "ilyra",
    "torren",
    "nimera",
    "vaelira",
    "seyrik",
}

BASE_DIR = Path(__file__).parent
CONTEXT_DIR = BASE_DIR / "context"


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
        for character_id, value in parsed.items():
            cid = str(character_id).strip().lower()
            if cid in CANONICAL_CHARACTER_IDS and value:
                result[cid] = str(value).rstrip("/")

    for character_id in CANONICAL_CHARACTER_IDS:
        env_name = f"{character_id.upper()}_AGENT_URL"
        value = os.getenv(env_name)
        if value:
            result[character_id] = value.rstrip("/")
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


async def agent_post(character_id: str, path: str, payload: dict[str, Any]) -> dict[str, Any]:
    url = AGENT_URLS.get(character_id)
    if not url:
        raise HTTPException(503, f"No agent URL configured for {character_id}.")
    headers = {}
    if AGENT_AUTH_TOKEN:
        headers["Authorization"] = f"Bearer {AGENT_AUTH_TOKEN}"
    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.post(f"{url}{path}", headers=headers, json=payload)
    if response.status_code >= 400:
        detail: Any
        try:
            detail = response.json()
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
You are the Diyse Dialogue Director.

Build a beat plan, not final prose. You must synthesize all supplied inputs at once:
character participation, relationship/knowledge limits, current story purpose, recent gameplay,
physical map/cell role, encounter pressure, lived-world/economic pressure, and current economical
HD-2D staging grammar.

Diyse scene rule:
Talk like mature adults. Use cinematic subtext. Time comedy like comedy. Allow anime-readable
expression and physical reaction without stock anime behavior. Respect JRPG gameplay pacing and
map traversal. Economical staging means intentional use of existing field space, rigged B00 models,
portraits, small gestures, camera, light, sound, props and environmental state before bespoke animation.

Hard rules:
- No player dialogue choices.
- Do not turn all participants into a roll call.
- Silence and nonparticipation are valid.
- Do not create author-only or future knowledge.
- Do not invent local shortages, route states, prices, wages, preferences, or lore facts.
- Required story comprehension cannot depend only on optional side-path dialogue.
- RED dialogue readiness means ordinary long conversation is inappropriate.
- Preserve encounter pressure; do not erase gameplay pressure merely to make dialogue convenient.
- Exact-line anchors marked required must be planned for verbatim use by the named speaker.
- Current authority_packet beats general genre expectation.

Return JSON only with this schema:
{
  "scene_mode": "full_authored_stop_scene|walking_or_traversal_dialogue|post_battle_reaction|story_bearing_cell|character_life_hub_camp|boss_threshold|story_combat_pause|microbeat_or_defer",
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
      "eligible_speakers": ["cyanis"],
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


BEAT_EDITOR_PROMPT = """
You are the Diyse Dialogue Editor working one beat at a time.

You receive a Director beat target plus candidate responses from persistent Person Agents.
Choose the most truthful candidate for the beat, or choose silence/action if that is better.
You may lightly edit spoken wording for rhythm, clarity, comedy timing, interruption, and natural speech,
but you may not invent a substantive fact, motive, memory, preference, relationship state, or knowledge
that the selected character candidate and authority packet do not support.

Performance contract:
- mature adult spoken language, not wiki prose;
- cinematic subtext instead of unnecessary emotional explanation;
- anime-readable expression/body language without stock reaction spam;
- comedy uses setup/beat/reaction, deadpan, escalation, callback, awkward hold, overcommitment, or refusal
  only when the people/scene support it;
- selective participation beats roll call;
- once the point lands, get out;
- environment/staging may carry information instead of dialogue;
- economical HD-2D staging should use existing field models, portraits, facing, small gestures, camera,
  light, sound, props, background motion and state swaps before expensive one-use animation.

If the Director supplies an exact_line_anchor, use that text verbatim and the named speaker.
Do not add player choices.

Return JSON only:
{
  "beat_id": "b01",
  "selected_speaker_id": "cyanis|null",
  "text": "spoken text or empty string",
  "action": "visible action or empty string",
  "silence": false,
  "expression_id": null,
  "portrait_side": "left|right|none",
  "staging_cues": [],
  "claimed_facts": [],
  "source_candidate_character_ids": ["cyanis"],
  "editor_note": "short rationale"
}
""".strip()


CANON_CHECKER_PROMPT = """
You are the Diyse Canon Checker.

Audit the complete drafted scene against the supplied current authority packet, story position,
knowledge firewall, participants, exact-line anchors, map/gameplay state, lived-world/economy rules,
and Dialogue Engine craft rules.

A PASS requires all of the following:
- no future or author-only knowledge leaks;
- no other character's private memory is used without an allowed transfer;
- no stale canon terminology supplied as retired/current-conflicting authority;
- no invented fixed local facts, prices, wages, route conditions, shortages, character preferences or lore;
- exact-line anchors marked required appear verbatim from the required speaker;
- mandatory story facts are present when required and forbidden reveals remain absent;
- participant presence and speaker identities are valid;
- no player dialogue choices;
- no illegal gameplay action is implied by staging;
- encounter/traversal pressure is respected;
- scene pacing is compatible with its map/cell role and dialogue readiness;
- character dialogue remains plausibly adult/natural and does not flatten everyone into one voice;
- HD-2D staging is compatible with the stated production cost ceiling.

Do not repair a failed scene by silently writing a new scene. Report the failure so the Director/editor
can regenerate the affected beat.

For a PASS, also build conservative per-character event ledgers containing only durable memories that
character could plausibly retain from this scene. Do not create a memory merely because a line occurred.
Do not place another person's private internal state into a character's memory. Do not propose full
state replacement; state changes remain proposals outside automatic commit.

Return JSON only:
{
  "status": "PASS|FAIL",
  "violations": [],
  "warnings": [],
  "knowledge_firewall_checks": [],
  "story_requirement_checks": [],
  "map_gameplay_checks": [],
  "performance_checks": [],
  "per_character_event_ledgers": {
    "cyanis": {
      "scene_id": "scene id",
      "memories": [
        {
          "memory_id": "stable unique string",
          "memory_type": "promise|conflict|care|favor|joke_callback|mistake_correction|follow_through|relationship_language|misunderstanding|mundane_continuity|observed_event",
          "content_summary": {},
          "importance": "low|medium|high"
        }
      ]
    }
  },
  "state_delta_proposals": {}
}
""".strip()


def normalize_participants(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        cid = value.strip().lower()
        if cid not in CANONICAL_CHARACTER_IDS:
            raise HTTPException(400, f"Unknown participant: {value}")
        if cid not in seen:
            result.append(cid)
            seen.add(cid)
    if not result:
        raise HTTPException(400, "At least one participant is required.")
    return result


def validate_anchor_inputs(anchors: list[ExactLineAnchor], participants: list[str]):
    for anchor in anchors:
        speaker_id = anchor.speaker_id.strip().lower()
        if speaker_id not in CANONICAL_CHARACTER_IDS:
            raise HTTPException(400, f"Unknown anchor speaker: {anchor.speaker_id}")
        if speaker_id not in participants:
            raise HTTPException(
                400, f"Exact-line anchor speaker {speaker_id} is not a scene participant."
            )


def validate_director_plan(plan: dict[str, Any], participants: list[str], max_beats: int):
    beats = plan.get("beat_plan")
    if not isinstance(beats, list):
        raise HTTPException(502, "Dialogue Director did not return a beat_plan list.")
    if len(beats) > max_beats:
        del beats[max_beats:]
    for index, beat in enumerate(beats, start=1):
        if not isinstance(beat, dict):
            raise HTTPException(502, "Dialogue Director returned an invalid beat entry.")
        beat.setdefault("beat_id", f"b{index:02d}")
        eligible = []
        for cid in beat.get("eligible_speakers", []):
            normalized = str(cid).strip().lower()
            if normalized in participants and normalized not in eligible:
                eligible.append(normalized)
        beat["eligible_speakers"] = eligible
        if not eligible and not beat.get("allow_silence", False):
            beat["allow_silence"] = True


def local_scene_checks(
    req: SceneBuildRequest,
    participants: list[str],
    scene_beats: list[dict[str, Any]],
) -> list[str]:
    violations: list[str] = []
    for anchor in req.exact_line_anchors:
        if not anchor.required:
            continue
        speaker_id = anchor.speaker_id.strip().lower()
        matched = any(
            beat.get("selected_speaker_id") == speaker_id
            and beat.get("text") == anchor.text
            for beat in scene_beats
        )
        if not matched:
            violations.append(
                f"Required exact-line anchor missing or altered for {speaker_id}: {anchor.text}"
            )

    for beat in scene_beats:
        speaker = beat.get("selected_speaker_id")
        if speaker not in (None, "null") and speaker not in participants:
            violations.append(f"Beat {beat.get('beat_id')} uses nonparticipant speaker {speaker}.")
        if "choices" in beat:
            violations.append(f"Beat {beat.get('beat_id')} contains player dialogue choices.")
    return violations


def godot_handoff(
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


app = FastAPI(title="Diyse Dialogue Orchestrator", version=SERVICE_VERSION)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service_version": SERVICE_VERSION,
        "canon_snapshot_id": CANON_SNAPSHOT_ID,
        "model_configured": model_configured(),
        "configured_agents": sorted(AGENT_URLS.keys()),
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

    participants = normalize_participants(req.participants)
    validate_anchor_inputs(req.exact_line_anchors, participants)

    missing_agents = [cid for cid in participants if cid not in AGENT_URLS]
    if missing_agents:
        raise HTTPException(
            503,
            detail={"error": "missing_agent_urls", "character_ids": missing_agents},
        )

    request_packet = req.model_dump()
    request_packet["participants"] = participants
    request_packet["shared_scene_construction_context"] = SHARED_CONTEXT.get(
        "scene_construction", {}
    )
    request_packet["shared_dialogue_life_context"] = SHARED_CONTEXT.get(
        "dialogue_life", {}
    )
    request_packet["shared_world_life_context"] = SHARED_CONTEXT.get("world_life", {})
    request_packet["shared_economy_context"] = SHARED_CONTEXT.get("economy", {})

    director_plan = await model_json(DIRECTOR_PROMPT, request_packet)
    validate_director_plan(director_plan, participants, req.max_beats)

    scene_beats: list[dict[str, Any]] = []
    candidate_audit: list[dict[str, Any]] = []

    for beat_index, beat_target in enumerate(director_plan.get("beat_plan", []), start=1):
        eligible = beat_target.get("eligible_speakers", [])
        anchor = beat_target.get("exact_line_anchor")
        if isinstance(anchor, dict) and anchor.get("speaker_id"):
            anchor_speaker = str(anchor["speaker_id"]).strip().lower()
            if anchor_speaker in participants:
                eligible = [anchor_speaker]

        if not eligible and beat_target.get("allow_silence", False):
            edited = {
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
                "editor_note": "Director-authored silent beat; no speaker candidates required.",
            }
            scene_beats.append(edited)
            continue

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

        async def fetch_candidate(character_id: str) -> tuple[str, dict[str, Any]]:
            payload = {
                "request_id": f"{req.request_id}:{beat_target.get('beat_id', beat_index)}:{character_id}",
                "scene_id": req.scene_id,
                "continuity_namespace": req.continuity_namespace,
                "story_position": req.story_position,
                "canon_snapshot_id": req.canon_snapshot_id,
                "observable_scene_so_far": observable_scene,
                "scene_context": {
                    **req.scene_context,
                    "scene_purpose": req.scene_purpose,
                    "authority_packet": req.authority_packet,
                    "director_scene_mode": director_plan.get("scene_mode"),
                    "dialogue_readiness": director_plan.get("dialogue_readiness"),
                    "beat_target": beat_target,
                    "production_cost_ceiling": req.production_cost_ceiling,
                },
                "current_floor_state": req.current_floor_state,
                "allowed_information_transfers": req.allowed_information_transfers,
            }
            return character_id, await agent_post(character_id, "/v1/turn", payload)

        candidate_pairs = await asyncio.gather(
            *(fetch_candidate(character_id) for character_id in eligible)
        )
        candidates = [
            {"character_id": character_id, "candidate": candidate}
            for character_id, candidate in candidate_pairs
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
            "scene_context": req.scene_context,
            "director_plan": director_plan,
            "beat_target": beat_target,
            "observable_scene_so_far": observable_scene,
            "agent_candidates": candidates,
            "exact_line_anchors": [anchor.model_dump() for anchor in req.exact_line_anchors],
            "shared_scene_construction_context": SHARED_CONTEXT.get("scene_construction", {}),
            "production_cost_ceiling": req.production_cost_ceiling,
        }
        edited = await model_json(BEAT_EDITOR_PROMPT, editor_payload)
        edited.setdefault("beat_id", beat_target.get("beat_id", f"b{beat_index:02d}"))
        scene_beats.append(edited)

    local_violations = local_scene_checks(req, participants, scene_beats)

    checker_payload = {
        "scene_id": req.scene_id,
        "story_position": req.story_position,
        "scene_purpose": req.scene_purpose,
        "canon_snapshot_id": req.canon_snapshot_id,
        "authority_packet": req.authority_packet,
        "participants": participants,
        "allowed_information_transfers": req.allowed_information_transfers,
        "exact_line_anchors": [anchor.model_dump() for anchor in req.exact_line_anchors],
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

    draft_id = str(uuid.uuid4())
    scene_packet = godot_handoff(req, director_plan, scene_beats)

    return {
        "draft_id": draft_id,
        "request_id": req.request_id,
        "scene_id": req.scene_id,
        "canon_snapshot_id": req.canon_snapshot_id,
        "director_plan": director_plan,
        "scene_beats": scene_beats,
        "canon_check": canon_check,
        "commit_ready": canon_check.get("status") == "PASS",
        "commit_bundle": {
            "canon_check_status": canon_check.get("status"),
            "per_character_event_ledgers": canon_check.get(
                "per_character_event_ledgers", {}
            ),
            "state_delta_proposals": canon_check.get("state_delta_proposals", {}),
        },
        "godot_handoff": scene_packet,
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
    for character_id in character_ids:
        if character_id not in CANONICAL_CHARACTER_IDS:
            raise HTTPException(400, f"Unknown commit character: {character_id}")
        if character_id not in AGENT_URLS:
            raise HTTPException(503, f"No agent URL configured for {character_id}.")
        if character_id not in req.expected_previous_revisions:
            raise HTTPException(
                400, f"Missing expected_previous_revision for {character_id}."
            )

    async def commit_one(character_id: str) -> tuple[str, dict[str, Any]]:
        ledger = dict(req.per_character_event_ledgers[character_id])
        ledger.setdefault("scene_id", req.scene_id)
        payload = {
            "request_id": f"{req.request_id}:commit:{character_id}",
            "scene_id": req.scene_id,
            "canon_snapshot_id": req.canon_snapshot_id,
            "canon_check_status": "PASS",
            "filtered_event_ledger": ledger,
            "expected_previous_revision": req.expected_previous_revisions[character_id],
        }
        return character_id, await agent_post(character_id, "/v1/commit", payload)

    results = await asyncio.gather(*(commit_one(cid) for cid in character_ids))
    return {
        "committed": True,
        "scene_id": req.scene_id,
        "character_results": {character_id: result for character_id, result in results},
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
