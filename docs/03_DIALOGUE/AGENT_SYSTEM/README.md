# Diyse Dialogue Engine — Agent System

**Status:** ACTIVE DIALOGUE-ENGINE ARCHITECTURE  
**Domain:** `03_DIALOGUE`  
**Purpose:** define how persistent character agents consume current Diyse canon without creating a second canon library.

The Dialogue Engine writes all current spoken scenes under the global regeneration rule in `../README.md`.

## Core authoring contract

The Dialogue Engine does **not** write dialogue in isolation from the game around it.

Every authored scene is built from the full Diyse scene stack:

> **Talk like people. React like anime characters. Time jokes like a comedy. Structure important scenes like a great RPG. Remember they are living through a war. And occasionally let them argue about absolutely nothing.**

That craft layer is combined with:
- current story/canon/reveal authority;
- persistent character brains and relationship state;
- lived-world, lived-magic/Card, and lived-economy context;
- the actual map cell / area phase / traversal state in which the scene occurs;
- recent combat pressure, recovery, fatigue, and what the player has just physically done;
- the current HD-2D visual/staging grammar and production budget;
- dialogue UI and runtime capabilities.

The detailed integration contract is:
> `SCENE_CONSTRUCTION_STACK.md`

The dialogue-facing map/traversal interface is:
> `../../13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/AREA_TRAVERSAL_AUTHORING_INTERFACE.md`

## Architecture

The intended authoring flow is:

1. **Dialogue Director** — assembles the complete scene job: story position, purpose, participants, location, sub-area/cell, area phase, observable state, recent player pressure/recovery, required/forbidden information, relationship state, pacing need, traversal mode, world/economy pressures, staging resources, and production budget.
2. **Persistent Person Agents** — one agent per relevant character reasons from that character's current identity, knowledge, relationships, memories, state, and observable scene information.
3. **Dialogue Editor** — shapes the combined output for spoken rhythm, selective participation, comedic/dramatic timing, subtext, scene economy, cinematic/anime expressiveness, map compatibility, staging compatibility, and naturalism without flattening individual voices.
4. **Canon Checker** — validates story/reveal timing, current terminology, knowledge firewalls, character authority, map/traversal compatibility, gameplay legality, production/staging rules, and cross-domain authority before story-continuity memory is committed.

The system may also run sandbox/open-conversation modes, but sandbox interaction must never silently rewrite story continuity.

## One-canon rule

Agent files are **runtime synthesis**, not independent authority.

Canonical routing:
- character identity, biography, personality, values, relationship logic, life habits → `../../01_CHARACTERS/`
- story position, required events, reveal timing, who is present/knows what → `../../02_STORY/`
- spoken-dialogue craft, exact line anchors, scene outputs → `../`
- geography, world history, modern-knowledge firewall, lived-world pressure, and lived magic/Card normality → `../../04_WORLD_AND_LORE/`
- class/Ability expertise boundaries → `../../06_CLASSES_AND_ABILITIES/`
- Cards/Primes/Faces → `../../07_CARDS/`
- equipment identity → `../../08_ITEMS_AND_EQUIPMENT/`
- encounter pressure / battle legality → `../../05_BATTLE_SYSTEM/` and `../../09_ENEMIES_AND_ENCOUNTERS/`
- economy/prices/commerce and lived economic context → `../../12_ECONOMY_AND_REWARDS/`
- map/traversal/dialogue implementation interface → `../../13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/AREA_TRAVERSAL_AUTHORING_INTERFACE.md`
- dialogue presentation/runtime → `../../13_UI_AND_IMPLEMENTATION/DIALOGUE_UI.md`
- active HD-2D style/staging authority → `../../14_ART_AND_VISUALS/`
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
- location and specific sub-area/cell;
- who is present;
- what has been said/done;
- physical activity;
- current task;
- area phase / route state;
- time/rest/travel conditions when provided;
- recent combat and recovery state;
- relevant world-life pressure;
- relevant local economic/supply context;
- what environmental information is visible before anyone explains it.

### 6. Scene-construction context
Agents and the Director must know what kind of scene they are inside:
- full stop-and-talk authored scene;
- short post-battle reaction;
- walking/traversal exchange;
- optional NPC interaction;
- camp/hub Character-Life scene;
- pre-boss or post-boss scene;
- investigation / inspection exchange;
- battle-story pause or transformation handoff.

The scene type changes acceptable line density, body movement, interruption risk, pacing, and staging cost.

## Information firewall

Agents must never use:
- future story reveals;
- author-only Story-Prime association before the character legitimately learns it;
- player/system Prime mechanics as character knowledge before story-earned discovery;
- another character's private memory;
- author-only truth not yet discovered;
- subclass expertise before the current story unlock allows it;
- a repository balance/calibration number as in-world knowledge unless separately established;
- stale names/Face/class/currency terminology from historical sources.

Agents may be wrong when a wrong belief is plausible from their evidence.

## Character-local speech / narrator firewall

Every Person Agent is a **person in the scene**, not a narrator, canon checker, continuity reconciler, exposition router, or audience-recap device.

Character knowledge determines what a person **may know**. It does not create an obligation to say everything they know.

Do not assign a line to any character merely to:
- restate a fact another character just established;
- repeat the current objective, location, relationship state, reveal, rule, or chronology for player clarity;
- summarize the preceding exchange;
- reconcile canon or continuity aloud;
- confirm that another character's accurate statement is accurate;
- finish another person's exposition;
- state the thematic meaning of the scene;
- translate author-only knowledge into dialogue;
- explain visible staging that already communicates the point;
- provide a tidy verbal conclusion after the dramatic/emotional point already landed.

A character should speak because that **person has a reason to speak**: a new observation, inference, objection, question, decision, action, joke, misunderstanding, emotional reaction, relationship impulse, professional need, or personal interest.

If the point is already established and the character has no new local motive, **silence is valid and usually preferable to repetition**.

Global line test:
> **Would this character still say this if no player needed the information repeated?**

If not, the line probably belongs to narration, UI, staging, another speaker with a genuine motive, or nowhere.

Characters are allowed to:
- misunderstand;
- remember imperfectly where current canon permits;
- focus on the wrong detail;
- draw plausible incomplete conclusions;
- decide a distinction is not worth correcting;
- know an answer and choose not to speak;
- react emotionally instead of supplying the clean explanatory line.

### Canon Checker separation
The **Canon Checker is invisible to the fiction**.

Its job is to validate, reject, or require revision of generated material. It must **never** be simulated through a character's dialogue.

When a generated line is inaccurate or confusing:
- fix, replace, or remove the line at the authoring/editor/checker layer;
- do not make another character recite the correct canon solely to repair it;
- do not add a "Yes, exactly" / "To be clear" / recap line merely to prove the scene is canon-compliant.

Canon correctness is an authoring property, not an in-world conversational role.

## Lived magic / Card requirement

The Agent Brain must inhabit the magical baseline of the setting rather than merely know its mechanics.

Hard runtime assumptions:
- ordinary trained Abilities are natural personal magic and should feel normal to modern people;
- Standard Cards are familiar Ancient Diysean artifacts that grant their holder/user access to the preserved ancient ability;
- ordinary Standard Card ownership/use is not chosen-one behavior and does not automatically create mystery;
- unusual Card behavior should be recognized as a violation of familiar Card expectations;
- Prime Cards are the exception: no known modern person has knowingly possessed or used one, surviving late-Diysean references are extremely sparse, their reality is uncertain to most people, and their actual function is unknown;
- operational Prime mechanics and Story-Prime bearer assignments are author/game-system truth until story evidence reveals them.

The runtime service therefore redacts author-only Prime-association metadata from character-facing Person-Agent inputs.

See:
- `../../04_WORLD_AND_LORE/LIVED_MAGIC_AND_CARD_CONTEXT.md`
- `../../04_WORLD_AND_LORE/MODERN_KNOWLEDGE_FIREWALL.md`
- `../../06_CLASSES_AND_ABILITIES/ABILITY_RULES.md`
- `../../07_CARDS/CARD_SYSTEM_MASTER.md`

## Lived-world requirement

The Dialogue Engine must not generate plot-only people.

Character agents are allowed to notice and discuss ordinary things. NPCs are allowed to have work, families, complaints, hobbies, rumors, schedules, and absences. Fatigue, shortages, watches, wounds, routes, evacuations, displaced civilians, missing people, food, weather, repairs, sleep, and interrupted routine may shape scenes when current location/story context supports them.

See:
- `../../04_WORLD_AND_LORE/LIVED_WORLD_SOCIAL_CONTEXT.md`
- `../../12_ECONOMY_AND_REWARDS/LIVED_ECONOMY_CONTEXT.md`

## Dialogue-naturalism and performance contract

### Talk like mature people
- Characters do not know they are in a story.
- Most speech should sound spoken rather than written.
- Adults may interrupt, swear, trail off, answer the wrong part, misunderstand, change subject, get petty, be bored, or simply not know what to say.
- Important dialogue earns eloquence; ordinary dialogue is allowed to be ordinary.
- The cast does not possess writer-level psychological insight into one another.

### React with anime expressiveness
Anime influence means readable emotional performance and tonal elasticity, not stock anime behavior.

Use when appropriate:
- expression changes;
- posture shifts;
- sudden embarrassment or irritation;
- disbelief;
- visible enthusiasm;
- emotional snap changes;
- fast movement between comedy, calm, danger, and grief.

Avoid:
- constant screaming;
- generic catchphrases;
- sexualized gag reactions;
- announcing visible emotions;
- friendship speeches;
- making competent people stupid when comedy starts.

### Time jokes like comedy
Comedy should arise from the people and their relationship. Available structures include:
- setup → beat → reaction;
- deadpan hold;
- escalation;
- callback;
- misunderstanding;
- awkward silence;
- overconfidence;
- committing harder to a stupid position;
- somebody refusing to give the expected reaction.

Do not insert jokes merely because a scene has been serious for a while.

### Use cinematic subtext
Emotion may live in:
- a pause;
- a look;
- someone turning away;
- a field-model gesture;
- a portrait-expression change;
- somebody beginning to answer and stopping;
- one person noticing something and choosing not to say it;
- a prop or ordinary task continuing through the conversation;
- silence after a line rather than another explanatory line.

Dialogue is not required to verbalize what staging can communicate.

## Ensemble rules

- Not every conversation must accomplish plot or arc work.
- Humor comes from personality and relationship rather than a designated funny character.
- Silence is participation.
- Selective participation is preferred to six-person roll call.
- Interruptions, false starts, partial answers, misunderstanding, dead ends, subject changes, failed jokes, and unresolved conversations are available but should not become a checklist.
- Surface subject may carry hidden emotional meaning without the characters naming the hidden subject.
- A character may refuse, defer, joke, become formal, leave, say "not tonight," or answer only the practical part.
- Relationship progression should become audible through shorthand, callbacks, teasing, borrowed language, fast coordination, and comfortable silence.
- Once the point has landed, get out. Do not add a line from every present party member merely to acknowledge presence.
- Do not make any participant function as the scene's narrator, recap voice, canon checker, or continuity verifier.
- Correct canon at the authoring/checker layer rather than inserting in-character confirmation dialogue.

## Gameplay / traversal integration

Dialogue placement must respect what the player is doing.

- Normal exploration remains gameplay; it is not merely a hallway between cutscenes.
- Long dialogue requires a breathable authored context: a settlement, camp, secured room, recovery point, story-bearing cell, safe pocket, or explicitly protected traversal window.
- Short post-battle reaction is naturally suited to post-battle grace.
- Mandatory walking dialogue may use encounter suppression only for the authored exchange and short buffer; local encounter pressure is preserved rather than reset.
- Do not place a long mandatory conversation inside a corridor whose intended identity is pursuit or sustained high pressure; move the processing scene to the next credible safe threshold.
- Boss aftermaths, recruitment handoffs, major revelations, Prime awakenings, surrender/capture beats, and genuine transformations deserve an authored breath before normal hostile pressure resumes.
- Important spatial discoveries should receive a clean visual read before portraits/text obscure them.

Exact map-size or minute targets from ongoing area research are not silently promoted to canon. The Director uses the research as an authoring interface and must obey any later current area-specific authority.

## HD-2D scene integration

Current visual authority is **Seinen HD-2D Fantasy with Chaotic Variable Line Weight + Graphic Anime-Stylized Rendering**.

For dialogue scenes:
- the actual field environment is the physical stage;
- current B00 rigged 3D field characters carry body placement, facing, movement, and broad gesture;
- high-resolution illustrated portraits carry close facial/emotional performance where used;
- authored camera framing, lighting, sound, props, foreground/midground/background activity, and world-state changes carry cinematic meaning;
- use selective depth geometry and expensive bespoke animation only when traversal, elevation, occlusion, perspective, spectacle, or a major emotional beat genuinely earns them;
- scale may be sold through composition, sound, lighting, background activity, layered depth, and state changes rather than fully simulating everything;
- intimate scenes may be carried by props, lighting, posture, portraits, ordinary tasks, and silence rather than expensive animation;
- presentation may never create illegal combat actions or story facts.

The production goal is not "cheap-looking HD-2D." It is **economical HD-2D that spends complexity where the player sees and feels it**.

## Runtime service

The current external service lives at:
> `external-services/canary/`

Its `brains/` and shared `context/` files are deployment/runtime synthesis only. They should identify their source-authority paths so stale runtime data can be audited quickly.

The service should receive shared world/magic-and-Cards/economy/dialogue-life/scene-construction context in addition to the character brain, personal memory/state, and observable scene payload.

## Commit rule

Only a Canon Checker **PASS** may commit generated story memory/state to persistent story continuity.

Open-conversation/sandbox memories remain separate from authored story continuity unless explicitly promoted through the normal authoring/canon process.
