# Diyse Dialogue Engine — Agent System

**Status:** ACTIVE DIALOGUE-ENGINE ARCHITECTURE  
**Domain:** `03_DIALOGUE`  
**Purpose:** define how persistent character agents consume current Diyse canon without creating a second canon library.

The Dialogue Engine writes all current spoken scenes under the global regeneration rule in `../README.md`.

## Architecture

The intended authoring flow is:

1. **Dialogue Director** — assembles the scene job: story position, purpose, participants, location, observable state, required/forbidden information, relationship state, and pacing needs.
2. **Persistent Person Agents** — one agent per permanent character reasons from that character's current identity, knowledge, relationships, memories, state, and observable scene information.
3. **Dialogue Editor** — shapes the combined output for spoken rhythm, selective participation, scene economy, staging compatibility, and naturalism without flattening individual voices.
4. **Canon Checker** — validates story/reveal timing, current terminology, knowledge firewalls, character authority, and cross-domain rules before story-continuity memory is committed.

The system may also run sandbox/open-conversation modes, but sandbox interaction must never silently rewrite story continuity.

## One-canon rule

Agent files are **runtime synthesis**, not independent authority.

Canonical routing:
- character identity, biography, personality, values, relationship logic, life habits → `../../01_CHARACTERS/`
- story position, required events, reveal timing, who is present/knows what → `../../02_STORY/`
- spoken-dialogue craft, exact line anchors, scene outputs → `../`
- geography, world history, modern-knowledge firewall, lived-world pressure → `../../04_WORLD_AND_LORE/`
- class/Ability expertise boundaries → `../../06_CLASSES_AND_ABILITIES/`
- Cards/Primes/Faces → `../../07_CARDS/`
- equipment identity → `../../08_ITEMS_AND_EQUIPMENT/`
- economy/prices/commerce and lived economic context → `../../12_ECONOMY_AND_REWARDS/`
- runtime/implementation precedence → `../../13_UI_AND_IMPLEMENTATION/`

When a runtime profile conflicts with an owning current domain, the owning domain wins and the runtime profile must be regenerated/fixed.

## Person Agent context stack

Each character turn should be grounded in:

### 1. Immutable/current character authority
- identity and role;
- current class/Face labels as references, not duplicated mechanics;
- values, contradictions, fears, habits, humor, social behavior;
- ordinary-life interests/preferences only where actually established;
- relationship interpretation patterns;
- knowledge/expertise boundaries;
- anti-patterns.

### 2. Story-position knowledge
- current chapter/scene position;
- what this character has personally observed;
- legitimate information transfers;
- facts learned in prior committed scenes;
- explicit unknown/forbidden future information.

A character does not know a fact merely because it exists in repository canon.

### 3. Persistent personal memory
Useful memory categories include:
- promises;
- conflicts;
- injuries/care received or refused;
- practical favors;
- jokes/callbacks;
- mistakes and corrections;
- people who followed through;
- relationship-specific language;
- unresolved misunderstandings;
- mundane continuity that was actually established.

Memory is character-local unless an allowed information transfer makes it shared.

### 4. Current state
State may influence behavior without replacing personality:
- fatigue;
- stress;
- anger;
- fear;
- guilt;
- injury/discomfort where observable/known;
- affection/trust;
- social posture;
- immediate task pressure.

### 5. Observable scene context
- location;
- who is present;
- what has been said/done;
- physical activity;
- current task;
- time/rest/travel conditions when provided;
- relevant world-life pressure;
- relevant local economic/supply context.

## Information firewall

Agents must never use:
- future story reveals;
- another character's private memory;
- author-only truth not yet discovered;
- subclass expertise before the current story unlock allows it;
- a repository balance/calibration number as in-world knowledge unless separately established;
- stale names/Face/class/currency terminology from historical sources.

Agents may be wrong when a wrong belief is plausible from their evidence.

## Lived-world requirement

The Dialogue Engine must not generate plot-only people.

Character agents are allowed to notice and discuss ordinary things. NPCs are allowed to have work, families, complaints, hobbies, rumors, schedules, and absences. Fatigue, shortages, watches, wounds, routes, evacuations, displaced civilians, missing people, food, weather, repairs, sleep, and interrupted routine may shape scenes when current location/story context supports them.

See:
- `../../04_WORLD_AND_LORE/LIVED_WORLD_SOCIAL_CONTEXT.md`
- `../../12_ECONOMY_AND_REWARDS/LIVED_ECONOMY_CONTEXT.md`

## Dialogue-naturalism contract

- Characters do not know they are in a story.
- Not every conversation must accomplish plot or arc work.
- Humor comes from personality and relationship rather than a designated funny character.
- Important dialogue earns eloquence; ordinary speech should usually remain ordinary.
- Silence is participation.
- Selective participation is preferred to six-person roll call.
- Interruptions, false starts, partial answers, misunderstanding, dead ends, subject changes, failed jokes, and unresolved conversations are available but should not become a checklist.
- Surface subject may carry hidden emotional meaning without the characters naming the hidden subject.
- A character may refuse, defer, joke, become formal, leave, say "not tonight," or answer only the practical part.
- The cast does not possess writer-level psychological insight into one another.
- Relationship progression should become audible through shorthand, callbacks, teasing, borrowed language, fast coordination, and comfortable silence.

## Runtime service

The current external service lives at:
> `external-services/canary/`

Its `brains/` and shared `context/` files are deployment/runtime synthesis only. They should identify their source-authority paths so stale runtime data can be audited quickly.

The service should receive shared world/economy/dialogue-life context in addition to the character brain, personal memory/state, and observable scene payload.

## Commit rule

Only a Canon Checker **PASS** may commit generated story memory/state to persistent story continuity.

Open-conversation/sandbox memories remain separate from authored story continuity unless explicitly promoted through the normal authoring/canon process.