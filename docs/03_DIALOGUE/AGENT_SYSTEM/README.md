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

The scene-construction contract is included in this file below.

The dialogue-facing map/traversal interface is:
> `../../13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/AREA_TRAVERSAL_AUTHORING_INTERFACE.md`

## Architecture

The intended authoring flow is:

1. **Dialogue Director** — assembles the complete scene job: story position, purpose, participants, location, sub-area/cell, area phase, observable state, recent player pressure/recovery, required/forbidden information, relationship state, pacing need, traversal mode, world/economy pressures, staging resources, and production budget.
2. **Persistent Person Agents** — one agent per relevant character reasons from that character's current identity, knowledge, relationships, memories, state, and observable scene information.
3. **Dialogue Editor** — shapes the combined output for spoken rhythm, selective participation, comedic/dramatic timing, subtext, scene economy, cinematic/anime expressiveness, map compatibility, staging compatibility, and naturalism without flattening individual voices.
4. **Canon Checker** — validates story/reveal timing, current terminology, knowledge firewalls, character authority, map/traversal compatibility, gameplay legality, production/staging rules, and cross-domain authority before story-continuity memory is committed.

The system may also run sandbox/open-conversation modes, but sandbox interaction must never silently rewrite story continuity.

## "Use the Agent Brain" contract

When an authoring request says **use the Agent Brain**, it means the **whole current Person-Agent stack**, not merely that character's runtime YAML.

Use together:
- current canonical character authority;
- runtime brain synthesis;
- current relationship state;
- story-position knowledge and chronology gates;
- established personal memory;
- current physical/emotional state;
- observable scene context;
- shared dialogue-system and scene-construction rules.

No new duplicate "master brain" file is required. The owning character file remains canon; YAML remains runtime synthesis.

Runtime combines the shared dialogue-life and scene-construction synthesis in `external-services/canary/context/dialogue_system.yaml`.

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
- authored route/traversal stop with player movement paused;
- short post-battle reaction after combat has fully ended;
- optional NPC interaction;
- camp/hub Character-Life scene;
- pre-boss or post-boss scene;
- investigation / inspection exchange.

The scene type changes acceptable line density, body movement, interruption risk, pacing, and staging cost.

## Runtime truth hierarchy

The Agent Brain must distinguish three kinds of information. They do **not** use the same retrieval rules.

### A. Hard current context — inject, do not retrieve

These facts must be supplied directly from current authority for the scene:

- chapter / sequence / exact story position;
- current participant list and party state;
- current location / sub-area / cell / area phase;
- current character identity, age, Face, Base/Subclass labels, and current unlock state;
- current equipment/weapon prohibitions or other hard identity restrictions that matter to the scene;
- current recruitment status;
- current reveal/knowledge gates;
- explicit forbidden future knowledge;
- current relationship chronology gate;
- current gameplay pressure / recovery state when narratively relevant;
- current world terminology and other hard naming corrections;
- current player-control/dialogue legality.

Hard context is **not optional memory**.

Examples:
- Vaelira's no-bow identity is not something the runtime "remembers if relevant";
- Seyrik's recruitment timing is not inferred from relationship warmth;
- a subclass ability is not available because an old scene happened to mention it;
- a future reveal cannot surface because semantic retrieval considered it relevant.

If hard context is missing, stale, contradictory, or unresolved, the runtime must **stop or mark the dependency open rather than guess**.

### B. Persistent personal memory — authorize, then retrieve selectively

Persistent memory contains things a specific character legitimately experienced, learned, was told, inferred, promised, shared, corrected, or established through prior committed scenes.

Memory may be selective and imperfect.

However:

> **Retrieval may fail. Authorization may not.**

A character may fail to remember an old joke in a specific moment. A character may **not** retrieve a private event they never witnessed or a fact they have not learned.

### C. Momentary cognition — intentionally variable

Momentary cognition includes:
- what catches attention first;
- which authorized memory comes to mind;
- current inference;
- current emotional appraisal;
- misunderstanding;
- competing wants;
- whether to speak;
- what to reveal;
- whether to stay silent.

This is where human variability belongs.

Hard canon should not drift in order to simulate human cognition.

## Epistemic-state contract

The runtime must not flatten all available information into "known."

Character-facing information should carry an epistemic status when the distinction matters:

- **known_fact** — directly established for this character;
- **direct_observation** — personally witnessed but still open to interpretation;
- **trusted_report** — reported by a source this character currently accepts;
- **heard_claim** — heard but not established;
- **inference** — conclusion drawn from evidence;
- **suspicion** — live possibility with insufficient support;
- **assumption** — currently treated as true without sufficient verification;
- **misunderstanding** — active incorrect model the character plausibly holds;
- **unknown** — not known;
- **forbidden_future** — author/runtime knows it exists but this character cannot access it.

Rules:
- confidence does not upgrade an inference into a fact;
- repetition does not upgrade a claim into a fact;
- another character knowing something does not make it shared;
- writer knowledge never enters the character-facing packet merely because it would produce cleaner exposition;
- corrections should update the belief/memory record rather than silently rewriting the character's past state;
- a character can remember **what they believed then** and **what they know now** as separate things.

## Persistent-memory record contract

Meaningful persistent memories should be attributable rather than stored as free-floating lore.

Where implementation supports it, a memory record should carry:

- memory ID;
- owner / character;
- source chapter / scene / event;
- acquisition mode: observed / told / inferred / participated / promised / corrected;
- people present;
- privacy / visibility scope;
- epistemic status at acquisition;
- current epistemic status;
- whether later corrected;
- correction source;
- relationship(s) involved;
- emotional salience;
- practical salience;
- unresolved obligation or open-thread link;
- last meaningful callback/use where useful.

### Memory retrieval order

Memory retrieval is two-stage:

1. **Authorization gate**
   - Did this character have access?
   - Had the event happened by this story position?
   - Was the information private?
   - Was it actually transferred?
   - Has a later correction changed its status?
   - Is the memory prohibited by current chronology?

2. **Salience selection**
   - current relationship relevance;
   - current scene similarity;
   - recency;
   - emotional importance;
   - practical usefulness;
   - unresolved obligation;
   - embarrassment;
   - repetition;
   - character-specific memory bias.

Relevance must **never** bypass authorization.

### Character-specific salience

The permanent brain may bias which authorized memories surface.

Examples:
- Nimera may retrieve exact wording, provenance, contradiction, and correction history;
- Torren may retrieve route conditions, practical consequence, physical pattern, and people's habits;
- Cyanis may over-retrieve failures, promises, exposure, and unfinished responsibility;
- Ilyra may retrieve explicit boundaries, what actually helped, and how a person preferred care;
- Vaelira may retrieve prediction failures, changed variables, calibration corrections, and conditions that altered a model.

These are salience biases, not supernatural recall.

## Relationship runtime state

Do not compress a relationship into one friendship number.

For the people actually interacting, runtime should supply the dimensions that matter to the current scene. Useful dimensions include:

- chronology stage;
- trust;
- familiarity;
- conflict safety;
- disagreement tolerance;
- teasing permission;
- profanity / vulgar-banter permission;
- affectionate-insult permission;
- physical-care / touch permission where relevant;
- favor-asking comfort;
- refusal safety;
- willingness to ask preference;
- willingness to state preference;
- ordinary-company comfort;
- silence comfort;
- disclosure comfort;
- shared jokes / callbacks;
- borrowed language;
- unresolved friction;
- recent rupture;
- recent repair;
- current asymmetry, if one person is more comfortable than the other.

These dimensions can progress independently.

Examples:
- Ilyra and Seyrik may establish **safe refusal** before affectionate insult;
- Torren and Nimera may develop professional respect before paternal/familial meaning;
- Vaelira may borrow a profane phrase before she becomes generally high-comfort with profanity;
- two people may have high trust and low disclosure comfort.

Relationship state must be **story-position specific**, not inferred from the eventual endpoint.

## Scene-local Person state

Before a Person Agent proposes dialogue, the runtime should assemble a temporary scene-local state.

Useful fields:

- immediate wants;
- immediate avoidances;
- current task;
- physical activity;
- attention target;
- private emotional appraisal;
- what the character thinks is happening;
- what they are uncertain about;
- active belief / suspicion / misunderstanding;
- relevant authorized memories;
- open conversational threads;
- what they are willing to discuss;
- what they are unwilling to discuss;
- whether they want company / distance / action / information / amusement / silence;
- whether they currently want to speak;
- what would make them interrupt;
- what they prefer to keep private;
- visible expression / performance choice.

A permanent trait does not automatically become the scene motive.

Example:
Ilyra may permanently care about agency, but her actual scene motive may be:
> **I want Seyrik to come eat with me.**

That is enough.

## Competing-motive rule

Person Agents may hold multiple live motives at once.

Examples:
- Cyanis wants rest **and** wants to finish the work;
- Ilyra wants Seyrik's company **and** does not want to pressure him;
- Vaelira wants the answer **and** recognizes that obtaining it could be intrusive;
- Nimera wants to ask the question **and** knows the question may not be hers to ask;
- Torren wants to solve the practical problem **and** knows taking over would violate somebody else's choice.

The scene should emerge from which motive wins, which is suppressed, and what remains visible.

Do not reduce a character to one selected trait.

## Private appraisal vs visible expression

Internal response and outward expression are separate runtime decisions.

A character may:
- feel fear;
- make a joke;
- become physically still;
- discuss only the practical issue;
- choose not to reveal the fear.

Runtime should therefore distinguish:
- **private appraisal**;
- **visible nonverbal expression**;
- **spoken expression**;
- **withheld content**.

Performance tells do not automatically become dialogue.

## Pre-generation reliability gate

Before rehearsal/dialogue generation, validate:

1. exact story position;
2. participant/recruitment legality;
3. hard current identity facts;
4. knowledge and reveal gates;
5. forbidden future knowledge;
6. location and player-control legality;
7. relationship chronology and relevant relationship dimensions;
8. current physical/emotional state;
9. memory authorization;
10. active epistemic states;
11. scene-local wants / avoidances / attention;
12. unresolved dependencies.

If any hard field conflicts with current authority:
- use owning current authority;
- repair stale runtime synthesis;
- do not ask a Person Agent to reconcile the contradiction in dialogue.

## Post-generation validation gate

Before a generated scene can be accepted:

- verify every factual claim against current hard context;
- verify every memory/callback belonged to that speaker;
- verify every relationship behavior is earned at this story position;
- verify no belief/suspicion was accidentally stated as authorial fact;
- verify no future knowledge leaked;
- verify no stale class/Face/equipment/name survived;
- verify no character became narrator/canon checker;
- verify silence would not be stronger than redundant participation;
- verify staging/player-control legality.

Bad output is revised **behind the fiction**.

## Post-scene learning / continuity update

After a scene passes the Canon Checker, ask:

> **What actually changed because this scene happened?**

Possible committed changes include:
- new fact learned;
- claim heard;
- inference formed;
- suspicion strengthened/weakened;
- misunderstanding created/corrected;
- preference learned;
- boundary stated;
- promise made;
- joke/callback established;
- favor given;
- rupture created;
- repair completed;
- relationship permission changed;
- open thread created/resolved;
- character discovered or stated something about their own preference.

**No change** is a valid result.

Do not automatically advance:
- trust;
- friendship;
- intimacy;
- disclosure;
- profanity permission;
- affectionate insult;
- physical familiarity;
- forgiveness.

Only explicitly earned deltas persist.

Open-conversation rehearsal, sandbox generation, or rejected drafts do not update authored continuity.

## Conversation floor / inertia / open-thread contract

A scene is not six independent characters answering the same prompt.

### Participation selection

Before each beat, ask which present characters actually have **speaking pressure**.

Speaking pressure may come from:
- immediate motive;
- relationship impulse;
- expertise that changes the beat;
- emotional investment;
- an open thread;
- joke;
- objection;
- correction;
- action need.

Silence/yield pressure may come from:
- the point already being made;
- no new motive;
- fatigue;
- discomfort;
- privacy;
- caution;
- redundancy;
- another person owning the beat more naturally.

Presence alone is never a reason to speak.

### Conversational floor

The runtime should track who currently holds the floor.

A Person Agent may:
- **take** the floor;
- **hold** it;
- **yield**;
- **interrupt**;
- remain **silent**.

Interruption must have a character-local reason. It is not a generic tool for making dialogue feel lively.

### Topic action

A character may:
- continue the current subject;
- narrow it;
- answer only part;
- shift subjects;
- avoid;
- close the subject;
- leave it unresolved.

Not every question should receive a complete answer.

A truthful derailment does not have to be forced back toward the scene purpose merely because the author knows what the scene is "about."

### Open threads

Scenes may leave behind:
- unanswered questions;
- unfinished arguments;
- borrowed items;
- promises;
- insults awaiting retaliation;
- awkward moments;
- concerns someone chose not to pursue;
- unresolved suspicions.

An open thread becomes durable continuity only if the Canon Checker determines it was meaningfully established.

Later callbacks to that thread still require normal memory authorization.

### Ensemble geometry

Prefer:
- one pair carrying the exchange while others react nonverbally;
- two simultaneous social clusters;
- a character entering late because something finally gives them motive;
- a character leaving the exchange;
- silence after the point lands.

Avoid acknowledgment turns whose only function is to prove every present character heard the previous line.

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
- **No spoken dialogue runs while player-controlled traversal is active.** If a route conversation is needed, trigger an authored stop and pause/lock movement first.
- **No spoken dialogue runs during active combat.** Battle-related dialogue may occur immediately before combat begins or after combat has fully ended.
- Long dialogue requires a breathable authored context: a settlement, camp, secured room, recovery point, story-bearing cell, safe pocket, or explicitly protected stop.
- Short post-battle reaction is naturally suited to post-battle grace after victory/defeat resolution has completed.
- Do not place a mandatory conversation inside a corridor whose intended identity is pursuit or sustained high pressure; move the processing scene to the next credible safe threshold.
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


## Detailed scene-construction interface

The following scene-building rules were previously split into a separate scene-construction document. They are now part of the Agent System master authority so **use the Agent Brain** and **build the scene** resolve through one document.

### 3. Dialogue Director scene-job packet

Before drafting, the Dialogue Director should be able to answer these fields.

#### Story
- chapter / sequence ID;
- exact story position;
- scene purpose;
- mandatory facts/events;
- prohibited future knowledge;
- participant list;
- party state entering/exiting.

#### Geography
- location;
- sub-area / cell;
- cell role;
- area phase;
- entry direction / exit direction where relevant;
- important landmark or visible event;
- whether the player controls movement during the exchange.

#### Gameplay history
- time/activity since last meaningful story beat;
- recent encounter pressure;
- recent boss / elite / puzzle / traversal mechanic;
- resource/recovery state if narratively observable;
- whether the player is in a quiet interval or pressure corridor;
- whether normal hostile pressure resumes immediately afterward.

#### People
- each participant's current physical/emotional state;
- hard current identity/context facts injected from authority;
- relationship runtime state among the people actually interacting;
- relationship dimensions relevant to this exact scene;
- personal memories **authorized first**, then selected for salience;
- memory provenance / privacy where the callback matters;
- what each person knows as known fact;
- what each person only observed / heard / inferred / suspects / assumes / misunderstands;
- what each person plausibly notices first;
- each person's immediate wants and avoidances;
- current task / physical activity;
- what each person is willing or unwilling to discuss;
- relevant open threads;
- private appraisal vs visible/spoken expression;
- whether each person currently has a motive to speak at all.

#### World life
- local civilian/work activity;
- current route/supply/repair/weather pressure;
- relevant ordinary-life opportunity;
- relevant local concern that does not exist solely to serve the plot.

#### Presentation
- scene mode;
- portrait availability;
- field-model blocking needs;
- camera need;
- prop/environment interaction;
- lighting/sound/state-change opportunities;
- production-cost tier;
- any required implementation cue.

If these fields are unknown because the current story/map design has not established them, do not invent false precision. Mark the dependency open.

---

### 4. Scene modes

#### Mode A — Full authored stop scene
Best for:
- major decisions;
- revelations;
- recruitment;
- confrontation;
- emotionally complex processing;
- scenes requiring precise blocking or silence.

Use a safe threshold or deliberately protected story cell. Player movement may lock.

#### Mode B — Authored traversal stop
Best for:
- short contextual exchange tied to a route;
- route observations that genuinely need dialogue;
- relationship texture at a natural pause;
- brief explanation that should happen before exploration resumes.

Rules:
- player-controlled movement is paused/locked for the conversation;
- the scene is a triggered stop, not dialogue layered over movement;
- preserve local encounter pressure across the stop rather than resetting it;
- if stopping would damage the area's pressure or pacing, defer the conversation to the next credible safe threshold.

#### Mode C — Post-battle reaction
Best for:
- one or two observations;
- quick jokes;
- evidence noticed from the fight;
- immediate emotional residue.

Keep it short enough to live in post-battle grace unless an explicit safe scene follows.

#### Mode D — Story-bearing cell interaction
A normal playable cell can carry narrative through:
- optional NPC talk;
- landmark observation;
- short party exchange;
- environmental discovery;
- local dispute;
- small relationship beat.

This distributes story through the location without turning every beat into a full cutscene.

#### Mode E — Character-Life / hub / camp
Best for:
- ordinary life;
- relationship accumulation;
- pointless arguments;
- hobbies;
- food;
- repair;
- gossip;
- games;
- low-stakes vulnerability;
- silence.

Mandatory plot information must not be hidden only here unless the scene is itself mandatory under story authority.

#### Mode F — Pre-boss / post-boss threshold
Pre-boss dialogue should not over-explain a confrontation the environment or prior story already established.

Post-boss dialogue receives a real breath after:
- mandatory bosses;
- genuine form conclusions;
- Prime awakenings;
- major recruitment;
- surrender/capture;
- major revelation.

Do not immediately throw the player into a random encounter after a major authored payoff.

---

### 5. Area-design rules that directly affect dialogue

The ongoing JRPG area study is research/design guidance. Its current numerical timing bands are not silently locked canon.

The following structural concepts are valid authoring tools:

#### Playable density
Do not judge a location by raw physical size. Dialogue is one of several meaningful beat types alongside:
- combat;
- treasure/reward;
- traversal mechanic;
- route choice;
- landmark;
- environmental reveal;
- puzzle;
- rest;
- optional discovery.

A conversation should be placed because it improves the playable sequence, not because a timer says dialogue is due.

#### Cell grammar
A location is better understood as meaningful cells than as one undifferentiated map.

Useful cell roles include:
- entry;
- traversal;
- branch;
- reward;
- challenge;
- reset/recovery;
- story;
- landmark;
- boss.

Dialogue density and presentation should change with cell role.

#### Story-bearing cells
A cell can remain playable while carrying narrative function. This supports:
- distributed worldbuilding;
- short relationship beats;
- NPC conflict;
- location-specific observations;
- foreshadowing;
- optional lore.

Not every story-bearing cell becomes a cinematic.

#### Story distributed by sub-area
Long routes can distribute different narrative functions across successive sub-areas rather than putting all story at entrance and exit.

Possible sequence:
- entry orientation;
- local/world texture;
- relationship beat;
- ideological conflict;
- recovery/intimacy;
- escalation;
- boss approach.

The exact pattern depends on the location.

#### Quiet intervals
Dialogue should account for how long the player has been under the same kind of pressure.

A quiet interval can be valuable after:
- several encounters;
- a difficult traversal mechanic;
- a major reveal;
- a boss;
- sustained visual intensity.

Do not eliminate texture in the name of compression. Remove repetition, not meaningful variation.

#### Optional narrative branches
Exploration may reward the player with:
- character banter;
- NPC conversation;
- lore;
- scenery;
- local history;
- relationship texture.

Optional branches should not contain required main-story comprehension unless current story authority explicitly makes that branch mandatory.

#### Return / retraversal
If the player reuses space under a changed objective or state, dialogue should notice the changed context when a character plausibly would. Do not repeat the original entry explanation simply because the map is familiar.

---

### 6. Gameplay-loop pressure and dialogue readiness

For scene placement, use a qualitative dialogue-readiness state.

#### GREEN
Natural home for dialogue.
Examples:
- town;
- camp;
- secured room;
- recovery point;
- calm story-bearing cell;
- post-battle grace for short lines;
- intentional safe traversal window.

#### AMBER
Dialogue possible but should be short or carefully staged.
Examples:
- active route with normal encounter pressure;
- transitional corridor;
- investigation while moving;
- area where stopping too long would damage urgency.

#### RED
Do not insert ordinary long dialogue.
Examples:
- active pursuit;
- escape;
- immediate pre-impact danger;
- mechanically demanding traversal;
- battle state without an explicit story pause.

RED can become an authored protected pause only when current story/gameplay authority deliberately creates that pause.

---

### 10. Economical HD-2D staging

The goal is **economical**, not cheap-looking.

Spend complexity where the player sees and feels it.

#### Low-cost / high-value scene tools
Prefer first:
- existing field environment;
- B00 rigged-model position and facing;
- a small authored gesture;
- portrait-expression change;
- silent beat;
- camera reframe / restrained push / pan;
- foreground occlusion or reveal;
- prop interaction;
- ordinary task continuing under dialogue;
- lighting shift;
- sound cue;
- music drop or return;
- background NPC movement;
- environment state swap;
- weather/particle layer already owned by the area.

#### Medium-cost tools
Use when earned:
- area-specific bespoke gesture;
- short authored path/blocking sequence;
- unique prop state;
- selective depth move;
- localized VFX;
- specific environmental animation.

#### High-cost tools
Reserve for moments whose meaning depends on them:
- bespoke full-body animation sequence;
- large destruction event;
- extensive crowd simulation;
- unique cinematic environment build;
- complex one-use transformation animation;
- large simulation that cannot be reused.

Whenever possible, sell scale with:
- composition;
- layered depth;
- sound;
- lighting;
- background motion;
- silhouettes;
- state changes;
- partial views;
- reaction;

rather than physically building or simulating the entire event.

#### Hybrid-performance rule
Diyse is not a flat visual novel and not a fully animated movie.

Major scenes should make the hybrid presentation itself useful:
- geography carries spatial truth;
- field models carry body relation and movement;
- portraits carry facial acting;
- camera/light/sound carry focus and scale;
- dialogue carries what cannot be better communicated another way.

If a scene only works with an expensive fully animated movie, redesign it unless that moment truly earns the cost.
If a scene becomes emotionally flat when reduced to text boxes alone, use the existing hybrid staging tools rather than adding explanatory dialogue.

---

### 12. Visual-first information rule

Before writing exposition, ask what the player can already see.

Examples:
- damaged road;
- abandoned carts;
- changed guard posture;
- flooded route;
- crowd flow;
- empty market stalls;
- repaired barricade;
- missing bridge section;
- distant smoke;
- a machine already cycling incorrectly.

Characters may react to visible evidence, but they do not need to describe the entire image aloud.

Important spatial discoveries should receive a clean visual beat before portrait/text density covers the frame.

---

### 13. Scene rhythm

A useful important-scene rhythm may include:

> arrival / visual read → practical reaction → social geometry → pressure or disagreement → beat/silence → turn/reveal → reaction → exit/handoff

This is not a mandatory template.

Comedy may use:
> setup → beat → reaction → escalation or exit

Emotional scenes may use:
> ordinary task → avoided subject → small breach → silence → partial answer → ordinary task resumes

Investigation may use:
> observe → competing interpretations → evidence correction → next action

Do not mechanically apply every step.

---

### 14. Scene economy

Before finalizing, remove:
- repeated explanations;
- six-person roll call;
- redundant emotional summary;
- a joke after the joke already landed;
- dialogue describing obvious visual information;
- extra travel created only to house a conversation;
- conversation that stalls a high-pressure gameplay section;
- bespoke staging whose meaning could be carried by existing assets.

Preserve:
- meaningful silence;
- character texture;
- environmental discovery;
- useful disagreement;
- local life;
- relationship-specific humor;
- recovery after real pressure;
- optional conversation that makes a place feel inhabited.

> **Remove repetition, not texture.**

---

### 15. Canon Checker scene audit

A scene should not commit until the checker can answer yes to the relevant questions.

#### Canon
- Is every hard current fact injected from owning authority rather than guessed from memory?
- Is every fact current?
- Does every character know only what they can know here?
- Was each callback/memory authorized for that character before relevance was considered?
- Is a claim/inference/suspicion clearly still a claim/inference/suspicion rather than silently upgraded to fact?
- Are current terminology/classes/Faces/equipment/location names used?
- Does the scene preserve mandatory story causality?
- Did any future knowledge, stale authority, or private memory leak into a Person Agent?

#### Character
- Does each participant sound like this person at this point in the relationship?
- Does each speaker have a scene-local motive rather than merely a relevant trait?
- Are reactions shaped by current fatigue/stress/history rather than generic drama?
- Are private appraisal, visible expression, and spoken disclosure appropriately separated?
- Are competing motives allowed rather than collapsing the person to one trait?
- Is anyone explaining their character-sheet theme too perfectly?
- Does every spoken line have a character-local reason beyond informing the player?
- Is anyone functioning as narrator, recap voice, canon checker, correctness confirmer, or continuity reconciler?
- Could any line be removed because the previous line, staging, or UI already made the point?
- If canon needed correction during drafting, was the line itself fixed rather than another character inserted to recite the correction?

#### Ensemble
- Does everyone who speaks need to speak?
- Is silence allowed?
- Does the social geometry feel like people sharing space rather than a turn queue?

#### Map / gameplay
- Is this conversation in a credible place to happen?
- Does its length fit the current pressure window?
- Would an encounter or traversal mechanic make the scene impossible?
- Does the scene respect what the player just physically experienced?
- Is important visual information given room before text?

#### Craft
- Does the speech sound adult and spoken?
- Is subtext allowed to remain subtext?
- Does humor arise from character and timing?
- Are expressive reactions staged instead of over-described in dialogue?
- Has the scene ended after the point lands?

#### Production
- Does the staging use the current HD-2D/B00 presentation?
- Can existing field models, portraits, props, camera, light, sound, and state changes carry the scene?
- Is expensive bespoke animation actually justified?
- Does presentation remain mechanically legal?

Only after these checks should authored story memory/state be committed.

The commit step must record **deltas, not a rewritten personality**:
- what was learned;
- what was merely heard;
- what was inferred;
- what was corrected;
- what preference/boundary/callback became established;
- what relationship permission genuinely changed;
- which open threads remain unresolved.

If nothing earned persistence, commit no character/relationship delta.

## Runtime service

The current external service lives at:
> `external-services/canary/`

Its `brains/` and shared `context/` files are deployment/runtime synthesis only. They should identify their source-authority paths so stale runtime data can be audited quickly.

The service should receive shared world/magic-and-Cards/economy/dialogue-life/scene-construction context in addition to the character brain, personal memory/state, and observable scene payload.

For authored generation, the service should assemble a **validated scene packet** in this order:

1. hard current context from owning authority;
2. chronology/knowledge authorization;
3. relationship runtime dimensions;
4. authorized persistent memory retrieval;
5. epistemic state;
6. current physical/emotional state;
7. scene-local wants / avoidances / attention;
8. private appraisal / visible-expression choice;
9. dialogue/scene rules.

Semantic relevance is never allowed to outrank chronology, privacy, ownership, or current canon.

## Commit rule

Only a Canon Checker **PASS** may commit generated story memory/state to persistent story continuity.

Open-conversation/sandbox memories remain separate from authored story continuity unless explicitly promoted through the normal authoring/canon process.
