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
BRAIN_PROFILE_VERSION = os.getenv("BRAIN_PROFILE_VERSION", "v2.20-lived-world")
CANON_SNAPSHOT_ID = os.getenv("CANON_SNAPSHOT_ID", "development")
PERSISTENCE_PATH = os.getenv("PERSISTENCE_PATH", "/data/agent.sqlite3")
SERVICE_AUTH_TOKEN = os.getenv("SERVICE_AUTH_TOKEN") or None
MODEL_API_URL = os.getenv("MODEL_API_URL") or None
MODEL_API_KEY = os.getenv("MODEL_API_KEY") or None
MODEL_NAME = os.getenv("MODEL_NAME") or None
PORT = int(os.getenv("PORT", "8080"))

CANONICAL_CHARACTER_IDS = {
    "cyanis", "ilyra", "torren", "nimera", "vaelira", "seyrik",
}
LEGACY_CHARACTER_ID_ALIASES = {
    "Cyanis_Dovaren": "cyanis",
    "Ilyra_Amarin": "ilyra",
    "Torren_Harth": "torren",
    "Nimera_Pellan": "nimera",
    "Vaelira_Serren": "vaelira",
    "Seyrik_Rell": "seyrik",
}

CHARACTER_ID = LEGACY_CHARACTER_ID_ALIASES.get(
    RAW_CHARACTER_ID, RAW_CHARACTER_ID.strip().lower()
)
if CHARACTER_ID not in CANONICAL_CHARACTER_IDS:
    raise RuntimeError(f"Unknown CHARACTER_ID: {RAW_CHARACTER_ID}")

BASE_DIR = Path(__file__).parent
BRAIN_PATH = BASE_DIR / "brains" / f"{CHARACTER_ID}.yaml"
CONTEXT_DIR = BASE_DIR / "context"

if not BRAIN_PATH.exists():
    raise RuntimeError(f"Missing brain profile: {BRAIN_PATH}")
BRAIN = yaml.safe_load(BRAIN_PATH.read_text(encoding="utf-8"))
CHARACTER_NAME = BRAIN["character"]


def load_shared_context() -> dict[str, Any]:
    result: dict[str, Any] = {}
    if not CONTEXT_DIR.exists():
        return result
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
            con.executescript("""
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
            """)
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
                "SELECT content_json FROM memories WHERE namespace=? "
                "ORDER BY created_at DESC LIMIT ?",
                (namespace, limit),
            ).fetchall()
            return [json.loads(r["content_json"]) for r in rows]

    def state(self) -> dict[str, Any]:
        with self.connect() as con:
            row = con.execute(
                "SELECT data_json FROM current_state WHERE singleton=1"
            ).fetchone()
            return json.loads(row["data_json"]) if row else {
                "social_posture": "neutral", "stress": 0, "fatigue": 0
            }

    def add_memory(self, con, namespace: str, memory_type: str,
                   scope_id: str, content: dict[str, Any]) -> bool:
        mid = content.get("memory_id") or str(uuid.uuid4())
        before = con.total_changes
        con.execute(
            "INSERT OR IGNORE INTO memories("
            "memory_id,namespace,memory_type,scope_id,content_json,created_at"
            ") VALUES(?,?,?,?,?,?)",
            (
                mid, namespace, memory_type, scope_id,
                json.dumps(content, ensure_ascii=False),
                datetime.datetime.now(datetime.timezone.utc).isoformat(),
            ),
        )
        return con.total_changes > before

    def commit_story(self, request_id: str, expected_revision: str, ledger: dict) -> dict:
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
            for mem in ledger.get("memories", []):
                if self.add_memory(
                    con, "story", mem.get("memory_type", "observed_event"),
                    ledger.get("scene_id", ""), mem
                ):
                    created += 1

            if ledger.get("state") is not None:
                row = con.execute(
                    "SELECT revision FROM current_state WHERE singleton=1"
                ).fetchone()
                srev = (row["revision"] + 1) if row else 1
                con.execute(
                    "INSERT INTO current_state(singleton,data_json,revision) VALUES(1,?,?) "
                    "ON CONFLICT(singleton) DO UPDATE SET "
                    "data_json=excluded.data_json, revision=excluded.revision",
                    (json.dumps(ledger["state"], ensure_ascii=False), srev),
                )

            new_rev = str(int(current) + 1)
            con.execute(
                "UPDATE metadata SET value=? WHERE key='story_revision'", (new_rev,)
            )
            response = {
                "committed": True,
                "new_revision": new_rev,
                "memories_created": created,
                "state_updated": ledger.get("state") is not None,
            }
            con.execute(
                "INSERT INTO processed_commits(request_id,response_json,created_at) VALUES(?,?,?)",
                (
                    request_id, json.dumps(response),
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
            rev = (row["revision"] + 1) if row else 1
            now = datetime.datetime.now(datetime.timezone.utc).isoformat()
            con.execute(
                "INSERT INTO conversations(conversation_id,revision,updated_at) VALUES(?,?,?) "
                "ON CONFLICT(conversation_id) DO UPDATE SET "
                "revision=excluded.revision, updated_at=excluded.updated_at",
                (conversation_id, rev, now),
            )
            self.add_memory(
                con, f"user_chat:{conversation_id}", "user_conversation",
                conversation_id,
                {
                    "content_summary": {
                        "user_message": user_message,
                        "character_response": response,
                    }
                },
            )
            con.commit()
            return str(rev)


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
        resp = await client.post(
            MODEL_API_URL,
            headers={"Authorization": f"Bearer {MODEL_API_KEY}"},
            json=body,
        )
        resp.raise_for_status()
        data = resp.json()
    content = data["choices"][0]["message"]["content"]
    return content if isinstance(content, dict) else json.loads(content)


def compact_brain() -> dict:
    keys = [
        "character", "identity", "core_person", "values", "drives", "defenses",
        "interests", "knowledge_model", "relationship_models", "memory_model",
        "state_model", "conversation_model", "decision_model", "chronology_gates",
        "anti_patterns",
    ]
    return {k: BRAIN[k] for k in keys if k in BRAIN}


TURN_PROMPT = f"""
You are the persistent external Diyse Person Agent for {CHARACTER_NAME}.
Use only your supplied Agent Brain, shared Diyse lived-world/economy/dialogue context,
your own memories/state, and observable scene information.
Shared context is runtime synthesis, not permission to invent local conditions or private facts.
The current story position and observable scene payload control what is actually true here.
Never use another character's private memory, author-only balance totals, or future story knowledge.
Never invent a fixed character preference, civilian wage, price, shortage, route condition, or local fact
when the supplied context says it requires current authority or scene evidence.
You may speak, act, interrupt, ask, misunderstand, be wrong, be bored, decline, or remain silent.
Prefer the shortest natural expression that accomplishes the intent.
Do not reveal hidden chain-of-thought.
Return only JSON with:
wants_to_speak, urgency, intent, emotional_posture, knowledge_basis, memory_refs,
observable_candidate {{speech, action, silence}}, claimed_facts, state_delta_proposal.
""".strip()

CHAT_PROMPT = f"""
You are {CHARACTER_NAME}, simulated through the Diyse Person Agent system.
Stay grounded in your Agent Brain, shared Diyse lived-world/economy/dialogue context,
personal continuity, knowledge boundaries, and observable context.
Shared context is not omniscience: do not invent local conditions, future story facts,
author-only balance information, or fixed preferences that have not been established.
You can say you don't know, ask questions, disagree, joke, change your mind, or let a subject drop.
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
        "shared_context_sections": sorted(SHARED_CONTEXT.keys()),
    }


@app.get("/v1/identity")
def identity():
    return {
        "character_id": CHARACTER_ID,
        "requested_character_id": RAW_CHARACTER_ID,
        "character_name": CHARACTER_NAME,
        "service_version": SERVICE_VERSION,
    }


@app.post("/v1/turn")
async def turn(req: TurnRequest, authorization: str | None = Header(default=None)):
    require_auth(authorization)
    if req.continuity_namespace not in {"story", "sandbox"}:
        raise HTTPException(400, "Invalid continuity namespace.")
    if req.continuity_namespace == "story" and req.canon_snapshot_id != CANON_SNAPSHOT_ID:
        raise HTTPException(409, "Canon snapshot mismatch.")
    result = await model_json(
        TURN_PROMPT,
        {
            "brain": compact_brain(),
            "shared_context": SHARED_CONTEXT,
            "memories": STORE.memories("story"),
            "current_state": STORE.state(),
            "request": req.model_dump(),
        },
    )
    result["request_id"] = req.request_id
    result["character_id"] = CHARACTER_ID
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
            req.request_id, req.expected_previous_revision,
            req.filtered_event_ledger
        )
    except RevisionConflict as e:
        raise HTTPException(
            409, detail={"error": "revision_conflict",
                         "current": e.current, "expected": e.expected}
        )


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
            "user_message": req.user_message,
            "observable_context": req.observable_context,
            "Diyse_native_mode": req.Diyse_native_mode,
        },
    )
    response = str(result["character_response"])
    revision = STORE.record_chat(req.conversation_id, req.user_message, response)
    return {"character_response": response, "conversation_revision": revision}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
