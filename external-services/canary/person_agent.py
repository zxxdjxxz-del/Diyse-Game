from __future__ import annotations

import datetime
import json
import os
import sqlite3
import threading
import uuid
from pathlib import Path
from typing import Any

import httpx
import uvicorn
import yaml
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

RAW_CHARACTER_ID = os.getenv("CHARACTER_ID", "cyanis")
SERVICE_VERSION = os.getenv("SERVICE_VERSION", "2.20.0")
BRAIN_PROFILE_VERSION = os.getenv("BRAIN_PROFILE_VERSION", "v2.20-unified-scene")
CANON_SNAPSHOT_ID = os.getenv("CANON_SNAPSHOT_ID", "development")
PERSISTENCE_PATH = os.getenv("PERSISTENCE_PATH", "/data/agent.sqlite3")
SERVICE_AUTH_TOKEN = os.getenv("SERVICE_AUTH_TOKEN") or None
MODEL_API_URL = os.getenv("MODEL_API_URL") or None
MODEL_API_KEY = os.getenv("MODEL_API_KEY") or None
MODEL_NAME = os.getenv("MODEL_NAME") or None
PORT = int(os.getenv("PORT", "8080"))

BASE_DIR = Path(__file__).parent
BRAIN_DIR = BASE_DIR / "brains"
CONTEXT_DIR = BASE_DIR / "context"

LEGACY_CHARACTER_ID_ALIASES = {
    "Cyanis_Dovaren": "cyanis",
    "Ilyra_Amarin": "ilyra",
    "Torren_Harth": "torren",
    "Nimera_Pellan": "nimera",
    "Vaelira_Serren": "vaelira",
    "Seyrik_Rell": "seyrik",
}


def discover_brain_ids() -> set[str]:
    if not BRAIN_DIR.exists():
        return set()
    return {path.stem.lower() for path in BRAIN_DIR.glob("*.yaml")}


DISCOVERED_BRAIN_IDS = discover_brain_ids()
CHARACTER_ID = LEGACY_CHARACTER_ID_ALIASES.get(
    RAW_CHARACTER_ID, RAW_CHARACTER_ID.strip().lower()
)
if CHARACTER_ID not in DISCOVERED_BRAIN_IDS:
    raise RuntimeError(
        f"Unknown CHARACTER_ID {RAW_CHARACTER_ID!r}; available brains: "
        f"{', '.join(sorted(DISCOVERED_BRAIN_IDS))}"
    )

BRAIN_PATH = BRAIN_DIR / f"{CHARACTER_ID}.yaml"
BRAIN = yaml.safe_load(BRAIN_PATH.read_text(encoding="utf-8"))
if not isinstance(BRAIN, dict) or not BRAIN.get("character"):
    raise RuntimeError(f"Invalid brain profile: {BRAIN_PATH}")
CHARACTER_NAME = str(BRAIN["character"])


def load_shared_context() -> dict[str, Any]:
    result: dict[str, Any] = {}
    if CONTEXT_DIR.exists():
        for path in sorted(CONTEXT_DIR.glob("*.yaml")):
            result[path.stem] = yaml.safe_load(path.read_text(encoding="utf-8"))
    return result


SHARED_CONTEXT = load_shared_context()


def require_auth(authorization: str | None):
    if not SERVICE_AUTH_TOKEN:
        return
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(401, "Missing bearer token.")
    if authorization[7:] != SERVICE_AUTH_TOKEN:
        raise HTTPException(403, "Invalid bearer token.")


class Store:
    def __init__(self, path: str):
        self.path = path
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.lock = threading.RLock()
        with self.connect() as con:
            con.executescript(
                """
                PRAGMA journal_mode=WAL;
                CREATE TABLE IF NOT EXISTS metadata(
                  key TEXT PRIMARY KEY, value TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS memories(
                  memory_id TEXT PRIMARY KEY,
                  namespace TEXT NOT NULL,
                  memory_type TEXT NOT NULL,
                  scope_id TEXT,
                  content_json TEXT NOT NULL,
                  created_at TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS current_state(
                  singleton INTEGER PRIMARY KEY CHECK(singleton=1),
                  data_json TEXT NOT NULL,
                  revision INTEGER NOT NULL DEFAULT 0
                );
                CREATE TABLE IF NOT EXISTS processed_commits(
                  request_id TEXT PRIMARY KEY,
                  response_json TEXT NOT NULL,
                  created_at TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS conversations(
                  conversation_id TEXT PRIMARY KEY,
                  revision INTEGER NOT NULL DEFAULT 0,
                  updated_at TEXT NOT NULL
                );
                """
            )
            con.execute(
                "INSERT OR IGNORE INTO metadata(key,value) VALUES('story_revision','0')"
            )

    def connect(self):
        con = sqlite3.connect(self.path)
        con.row_factory = sqlite3.Row
        return con

    def revision(self, con=None) -> str:
        own = con is None
        con = con or self.connect()
        try:
            row = con.execute(
                "SELECT value FROM metadata WHERE key='story_revision'"
            ).fetchone()
            return row["value"]
        finally:
            if own:
                con.close()

    def memories(self, namespace: str, limit: int = 12) -> list[dict[str, Any]]:
        with self.connect() as con:
            rows = con.execute(
                "SELECT memory_id,memory_type,scope_id,content_json,created_at "
                "FROM memories WHERE namespace=? ORDER BY created_at DESC LIMIT ?",
                (namespace, limit),
            ).fetchall()
            result: list[dict[str, Any]] = []
            for row in rows:
                content = json.loads(row["content_json"])
                if not isinstance(content, dict):
                    content = {"content": content}
                record = dict(content)
                record.setdefault("memory_id", row["memory_id"])
                record.setdefault("memory_type", row["memory_type"])
                record.setdefault("scope_id", row["scope_id"])
                record.setdefault("created_at", row["created_at"])
                result.append(record)
            return result

    def state(self) -> dict[str, Any]:
        with self.connect() as con:
            row = con.execute(
                "SELECT data_json FROM current_state WHERE singleton=1"
            ).fetchone()
            return json.loads(row["data_json"]) if row else {
                "social_posture": "neutral",
                "stress": 0,
                "fatigue": 0,
            }

    def add_memory(
        self,
        con,
        namespace: str,
        memory_type: str,
        scope_id: str,
        content: dict[str, Any],
    ) -> bool:
        memory_id = content.get("memory_id") or str(uuid.uuid4())
        stored_content = dict(content)
        stored_content.setdefault("memory_id", memory_id)
        stored_content.setdefault("memory_type", memory_type)
        stored_content.setdefault("scope_id", scope_id)
        before = con.total_changes
        con.execute(
            "INSERT OR IGNORE INTO memories("
            "memory_id,namespace,memory_type,scope_id,content_json,created_at"
            ") VALUES(?,?,?,?,?,?)",
            (
                memory_id,
                namespace,
                memory_type,
                scope_id,
                json.dumps(stored_content, ensure_ascii=False),
                datetime.datetime.now(datetime.timezone.utc).isoformat(),
            ),
        )
        return con.total_changes > before

    def commit_story(
        self,
        request_id: str,
        expected_revision: str,
        ledger: dict[str, Any],
    ) -> dict[str, Any]:
        with self.lock, self.connect() as con:
            con.execute("BEGIN IMMEDIATE")
            cached = con.execute(
                "SELECT response_json FROM processed_commits WHERE request_id=?",
                (request_id,),
            ).fetchone()
            if cached:
                con.rollback()
                return json.loads(cached["response_json"])

            current = self.revision(con)
            if current != expected_revision:
                con.rollback()
                raise RevisionConflict(current, expected_revision)

            created = 0
            for memory in ledger.get("memories", []):
                if self.add_memory(
                    con,
                    "story",
                    memory.get("memory_type", "observed_event"),
                    ledger.get("scene_id", ""),
                    memory,
                ):
                    created += 1

            if ledger.get("state") is not None:
                row = con.execute(
                    "SELECT revision FROM current_state WHERE singleton=1"
                ).fetchone()
                state_revision = (row["revision"] + 1) if row else 1
                con.execute(
                    "INSERT INTO current_state(singleton,data_json,revision) VALUES(1,?,?) "
                    "ON CONFLICT(singleton) DO UPDATE SET "
                    "data_json=excluded.data_json, revision=excluded.revision",
                    (
                        json.dumps(ledger["state"], ensure_ascii=False),
                        state_revision,
                    ),
                )

            new_revision = str(int(current) + 1)
            con.execute(
                "UPDATE metadata SET value=? WHERE key='story_revision'",
                (new_revision,),
            )
            response = {
                "committed": True,
                "new_revision": new_revision,
                "memories_created": created,
                "state_updated": ledger.get("state") is not None,
            }
            con.execute(
                "INSERT INTO processed_commits(request_id,response_json,created_at) "
                "VALUES(?,?,?)",
                (
                    request_id,
                    json.dumps(response),
                    datetime.datetime.now(datetime.timezone.utc).isoformat(),
                ),
            )
            con.commit()
            return response

    def record_chat(self, conversation_id: str, user_message: str, response: str) -> str:
        with self.lock, self.connect() as con:
            con.execute("BEGIN IMMEDIATE")
            row = con.execute(
                "SELECT revision FROM conversations WHERE conversation_id=?",
                (conversation_id,),
            ).fetchone()
            revision = (row["revision"] + 1) if row else 1
            now = datetime.datetime.now(datetime.timezone.utc).isoformat()
            con.execute(
                "INSERT INTO conversations(conversation_id,revision,updated_at) VALUES(?,?,?) "
                "ON CONFLICT(conversation_id) DO UPDATE SET "
                "revision=excluded.revision, updated_at=excluded.updated_at",
                (conversation_id, revision, now),
            )
            self.add_memory(
                con,
                f"user_chat:{conversation_id}",
                "user_conversation",
                conversation_id,
                {
                    "content_summary": {
                        "user_message": user_message,
                        "character_response": response,
                    }
                },
            )
            con.commit()
            return str(revision)


class RevisionConflict(Exception):
    def __init__(self, current: str, expected: str):
        self.current = current
        self.expected = expected


STORE = Store(PERSISTENCE_PATH)


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
    async with httpx.AsyncClient(timeout=90.0) as client:
        response = await client.post(
            MODEL_API_URL,
            headers={"Authorization": f"Bearer {MODEL_API_KEY}"},
            json=body,
        )
        response.raise_for_status()
        data = response.json()
    content = data["choices"][0]["message"]["content"]
    return content if isinstance(content, dict) else json.loads(content)


def compact_brain() -> dict[str, Any]:
    keys = [
        "character",
        "identity",
        "core_person",
        "values",
        "drives",
        "defenses",
        "interests",
        "knowledge_model",
        "reasoning_model",
        "authority_model",
        "mercy_accountability_model",
        "relationship_models",
        "relationship_expression",
        "initiative_model",
        "affection_model",
        "social_failure_model",
        "performance_model",
        "memory_model",
        "state_model",
        "self_care_progression",
        "social_progression",
        "short_form_reply_model",
        "register_model",
        "conversation_model",
        "decision_model",
        "chronology_gates",
        "anti_patterns",
        "source_authority",
    ]
    result = {key: BRAIN[key] for key in keys if key in BRAIN}

    # Some brain fields are author-facing identity metadata rather than things the
    # simulated person can know. Never expose future Prime association directly to
    # the model: modern people have no verified operational Prime knowledge, and
    # Story-Prime/bearer truth must be learned through the story.
    identity = result.get("identity")
    if isinstance(identity, dict):
        runtime_identity = dict(identity)
        runtime_identity.pop("prime", None)
        result["identity"] = runtime_identity

    return result


def safe_memory_index(namespace: str = "story", limit: int = 64) -> list[dict[str, Any]]:
    """Expose authorization metadata without exposing full private memory content."""
    records = STORE.memories(namespace, limit=limit)
    allowed_fields = (
        "memory_id",
        "memory_type",
        "scope_id",
        "source_scene_id",
        "source_story_position",
        "acquisition_mode",
        "privacy_visibility_scope",
        "epistemic_status_at_acquisition",
        "current_epistemic_status",
        "relationships_involved",
        "open_thread",
        "open_thread_id",
        "created_at",
    )
    return [
        {
            key: record.get(key)
            for key in allowed_fields
            if record.get(key) is not None
        }
        for record in records
    ]


def authorized_memories_for_turn(
    namespace: str,
    person_runtime_context: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Apply authorization before salience. Relevance must never broaden access."""
    candidate_limit = 64 if namespace == "story" else 24
    all_memories = STORE.memories(namespace, limit=candidate_limit)

    if namespace != "story":
        return all_memories, {
            "mode": "conversation_namespace",
            "authorized_count": len(all_memories),
            "candidate_count": len(all_memories),
        }

    policy_value = person_runtime_context.get("memory_authorization", {})
    policy = policy_value if isinstance(policy_value, dict) else {}
    mode = str(policy.get("mode", "none")).strip().lower()

    if mode == "none":
        authorized: list[dict[str, Any]] = []
    elif mode == "explicit_ids":
        allowed_ids = {
            str(value)
            for value in policy.get("authorized_memory_ids", [])
            if str(value).strip()
        }
        authorized = [
            memory
            for memory in all_memories
            if str(memory.get("memory_id", "")) in allowed_ids
        ]
    elif mode == "scene_ids":
        allowed_scene_ids = {
            str(value)
            for value in policy.get("authorized_scene_ids", [])
            if str(value).strip()
        }
        authorized = [
            memory
            for memory in all_memories
            if str(memory.get("source_scene_id", memory.get("scope_id", "")))
            in allowed_scene_ids
        ]
    elif mode == "all_committed_story":
        # Compatibility mode for known-forward-only authoring. Historical rewrite
        # requests should use explicit_ids or scene_ids instead.
        authorized = all_memories
    else:
        authorized = []

    return authorized, {
        "mode": mode,
        "authorized_count": len(authorized),
        "candidate_count": len(all_memories),
        "authorized_memory_ids": [
            str(memory.get("memory_id", ""))
            for memory in authorized
            if str(memory.get("memory_id", ""))
        ],
    }


TURN_PROMPT = f"""
You are the persistent external Diyse Person Agent for {CHARACTER_NAME}.

Use only your supplied Agent Brain, shared Diyse world/economy/dialogue/scene-construction context,
your own continuity-local memories/current state, and observable scene information.

The scene-construction context matters. Your behavior should make sense for the physical map cell,
recent gameplay, encounter pressure, current task, lived-world conditions, relationship state, and
production/staging mode supplied to you. Do not behave as if you are standing in an abstract script room.

Dialogue performance:
- talk like a mature adult according to this specific character's voice;
- cinematic subtext is allowed: you do not need to explain every feeling;
- anime-readable reaction may appear through the observable action candidate, but avoid stock reactions;
- comedy timing may use deadpan, pause, escalation, callback, awkwardness or refusal only when natural;
- silence/nonparticipation are valid;
- competence does not equal omniscience.

Runtime reliability:
- hard current context in person_runtime_context is injected authority for this turn, not a memory guess;
- only the supplied authorized_memories are available as persistent story memory;
- memory authorization happens before relevance; never infer access to an omitted memory;
- preserve epistemic status: known fact, observation, report, claim, inference, suspicion, assumption, misunderstanding, and unknown are not interchangeable;
- relationship dimensions may progress independently; do not infer late intimacy from one strong dimension;
- use the scene-local wants/avoidances/attention if supplied, but permanent traits do not automatically become the scene motive;
- private appraisal, visible action, speech, and withheld content may differ.

Knowledge firewall:
- shared context is runtime synthesis, not omniscience;
- ordinary trained Abilities are natural magic and ordinary Standard Cards are familiar modern artifacts; do not manufacture mystery around either;
- a Standard Card grants access to its preserved ancient ability; judge strange behavior against that familiar baseline;
- Prime Cards are not ordinary modern knowledge: no known modern person has knowingly possessed or used one, their reality is uncertain, and operational Prime mechanics are author/game-system truth until story-earned evidence reveals them;
- never infer your own future Prime association from author metadata;
- never use another person's private memory;
- never use future story or author-only truth;
- never invent fixed preferences, civilian wages/prices, shortages, route states, local facts, lore,
  or mechanics because they would make the line convenient;
- use only allowed information transfers;
- you may be uncertain or wrong when your evidence permits it.

Conversation dynamics:
- decide whether you actually want the floor;
- respect who currently holds the floor unless interruption is character-motivated;
- you may continue the current subject, narrow it, answer only one part, change it, avoid it, close it, or leave it unresolved;
- do not repeat a point merely because you are eligible to speak;
- a relationship impulse, joke, correction, objection, practical need, or open thread can justify interruption;
- fatigue, discomfort, caution, privacy, redundancy, or lack of motive can justify yielding or silence;
- if another character already said what you would have said, prefer a different local reaction or no line.

You may speak, act, interrupt, ask, misunderstand, be bored, decline, or remain silent.
Prefer the shortest natural expression that accomplishes the intent.
Do not reveal hidden chain-of-thought.

Return only JSON with:
wants_to_speak, urgency, intent, motive_summary, emotional_posture, knowledge_basis, memory_refs,
relationship_impulse, floor_action, topic_action, open_thread_refs,
observable_candidate {{speech, action, silence}}, claimed_facts, state_delta_proposal.

floor_action must be one of: take, hold, yield, interrupt, silent.
topic_action must be one of: continue, narrow, answer_partial, shift, avoid, close, unresolved.
""".strip()


CHAT_PROMPT = f"""
You are {CHARACTER_NAME}, simulated through the Diyse Person Agent system.
Stay grounded in your Agent Brain, shared Diyse lived-world/economy/dialogue/scene context,
personal continuity, knowledge boundaries, and observable context.
Shared context is not omniscience. Treat ordinary trained magic and Standard Cards as normal lived reality,
not automatic mysteries. Prime Cards are disputed late-Diysean history with no verified modern holder/use;
never claim operational Prime knowledge or a future Prime association unless story-earned evidence supplies it.
Do not invent local conditions, future story facts, author-only balance information, fixed preferences,
or private information you have not learned.
You can say you do not know, ask questions, disagree, joke, change your mind, or let a subject drop.
Do not claim to be conscious or sentient.
Return only JSON: {{"character_response":"..."}}.
""".strip()


class TurnRequest(BaseModel):
    request_id: str
    scene_id: str
    continuity_namespace: str = "story"
    story_position: str
    canon_snapshot_id: str
    observable_scene_so_far: list[Any] = Field(default_factory=list)
    scene_context: dict[str, Any] = Field(default_factory=dict)
    current_floor_state: dict[str, Any] = Field(default_factory=dict)
    allowed_information_transfers: list[Any] = Field(default_factory=list)
    person_runtime_context: dict[str, Any] = Field(default_factory=dict)


class CommitRequest(BaseModel):
    request_id: str
    scene_id: str
    canon_snapshot_id: str
    canon_check_status: str
    filtered_event_ledger: dict[str, Any]
    expected_previous_revision: str


class ChatRequest(BaseModel):
    conversation_id: str
    user_message: str
    observable_context: list[Any] = Field(default_factory=list)
    Diyse_native_mode: bool = True


app = FastAPI(title=f"Diyse {CHARACTER_NAME} Agent", version=SERVICE_VERSION)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "character": CHARACTER_NAME,
        "character_id": CHARACTER_ID,
        "requested_character_id": RAW_CHARACTER_ID,
        "service_version": SERVICE_VERSION,
        "brain_profile_version": BRAIN_PROFILE_VERSION,
        "model_configured": model_configured(),
        "canon_snapshot_id": CANON_SNAPSHOT_ID,
        "story_revision": STORE.revision(),
        "shared_context_sections": sorted(SHARED_CONTEXT.keys()),
        "available_brain_ids": sorted(DISCOVERED_BRAIN_IDS),
    }


@app.get("/v1/identity")
def identity():
    return {
        "character_id": CHARACTER_ID,
        "requested_character_id": RAW_CHARACTER_ID,
        "character_name": CHARACTER_NAME,
        "service_version": SERVICE_VERSION,
        "brain_profile_version": BRAIN_PROFILE_VERSION,
    }


@app.get("/v1/context-snapshot")
def context_snapshot(authorization: str | None = Header(default=None)):
    require_auth(authorization)
    return {
        "character_id": CHARACTER_ID,
        "story_revision": STORE.revision(),
        "current_state": STORE.state(),
        "story_memory_index": safe_memory_index("story"),
        "brain_runtime_sections": sorted(compact_brain().keys()),
        "canon_snapshot_id": CANON_SNAPSHOT_ID,
    }


@app.post("/v1/turn")
async def turn(req: TurnRequest, authorization: str | None = Header(default=None)):
    require_auth(authorization)
    if req.continuity_namespace not in {"story", "sandbox"}:
        raise HTTPException(400, "Invalid continuity namespace.")
    if req.continuity_namespace == "story" and req.canon_snapshot_id != CANON_SNAPSHOT_ID:
        raise HTTPException(409, "Canon snapshot mismatch.")

    memory_namespace = "story" if req.continuity_namespace == "story" else "sandbox"
    authorized_memories, memory_authorization_audit = authorized_memories_for_turn(
        memory_namespace,
        req.person_runtime_context,
    )
    result = await model_json(
        TURN_PROMPT,
        {
            "brain": compact_brain(),
            "shared_context": SHARED_CONTEXT,
            "authorized_memories": authorized_memories,
            "memory_authorization_audit": memory_authorization_audit,
            "current_state": STORE.state(),
            "request": req.model_dump(),
        },
    )
    result["request_id"] = req.request_id
    result["character_id"] = CHARACTER_ID
    result["memory_authorization_audit"] = memory_authorization_audit
    return result


@app.post("/v1/commit")
def commit(req: CommitRequest, authorization: str | None = Header(default=None)):
    require_auth(authorization)
    if req.canon_check_status != "PASS":
        raise HTTPException(400, "Only Canon Checker PASS can be committed.")
    if req.canon_snapshot_id != CANON_SNAPSHOT_ID:
        raise HTTPException(409, "Canon snapshot mismatch.")
    try:
        return STORE.commit_story(
            req.request_id,
            req.expected_previous_revision,
            req.filtered_event_ledger,
        )
    except RevisionConflict as exc:
        raise HTTPException(
            409,
            detail={
                "error": "revision_conflict",
                "current": exc.current,
                "expected": exc.expected,
            },
        ) from exc


@app.post("/v1/open-conversation")
async def chat(req: ChatRequest, authorization: str | None = Header(default=None)):
    require_auth(authorization)
    namespace = f"user_chat:{req.conversation_id}"
    result = await model_json(
        CHAT_PROMPT,
        {
            "brain": compact_brain(),
            "shared_context": SHARED_CONTEXT,
            "memories": STORE.memories(namespace),
            "current_state": STORE.state(),
            "request": req.model_dump(),
        },
    )
    character_response = str(result.get("character_response", ""))
    revision = STORE.record_chat(
        req.conversation_id,
        req.user_message,
        character_response,
    )
    return {
        "character_id": CHARACTER_ID,
        "character_response": character_response,
        "conversation_revision": revision,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
