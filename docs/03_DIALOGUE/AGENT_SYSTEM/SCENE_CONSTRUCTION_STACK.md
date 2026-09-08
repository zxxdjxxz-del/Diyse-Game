# Diyse Dialogue Engine — Unified Scene Construction Stack

**Status:** ACTIVE DIALOGUE-AUTHORING INTERFACE  
**Domain owner:** `03_DIALOGUE`  
**Purpose:** make dialogue, character behavior, gameplay pacing, map/traversal design, lived-world context, and economical HD-2D staging operate as one scene-building system.

This document does not create new story canon, area dimensions, encounter counts, prices, or character facts. It tells the Dialogue Engine how to consume the current owning authorities together.

---

## 1. The rule

A Diyse scene is not written as a screenplay first and fitted into the game later.

It is built from the full playable situation:

> **Character + relationship + knowledge + recent experience + physical location + gameplay pressure + lived world + scene purpose + HD-2D staging + production cost.**

The working dialogue mnemonic remains:

> **Talk like people. React like anime characters. Time jokes like a comedy. Structure important scenes like a great RPG. Remember they are living through a war. And occasionally let them argue about absolutely nothing.**

The mnemonic is not the whole system. The entire stack below applies simultaneously.

---

## 2. Authority stack used before writing

### A. Story truth
Read the current owning `02_STORY` material for:
- exact story position;
- required events;
- participant availability;
- reveal timing;
- current party state;
- required outcomes;
- facts that must remain unknown;
- area-specific story purpose.

Dialogue may improve delivery but may not silently change the event.

### B. Character truth
Read current `01_CHARACTERS` authority for every speaking or materially reacting person:
- personality;
- values and contradictions;
- expertise;
- social behavior;
- humor;
- stress behavior;
- current relationship language;
- knowledge boundaries;
- ordinary-life identity.

The writer's character sheet is not dialogue. Characters almost never state their own thematic summary perfectly.

### C. Personal continuity
Use committed character-local memory and current state:
- promises;
- arguments;
- callbacks;
- injuries;
- care accepted/refused;
- trust;
- fatigue;
- practical favors;
- unresolved misunderstandings;
- mundane facts actually established in prior continuity.

### D. Lived-world and economy context
Use current world/economy authority when relevant:
- watches;
- food;
- sleep;
- transport;
- repairs;
- missing people;
- displacement;
- shortages;
- medical pressure;
- local work;
- route conditions;
- weather;
- services and commerce.

These pressures may affect conversation without every scene becoming exposition about the war or economy.

### E. Area / traversal context
Use the current area map and the dialogue-facing traversal interface:
> `../../13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/AREA_TRAVERSAL_AUTHORING_INTERFACE.md`

Know:
- location and sub-area;
- cell function;
- area phase;
- whether the player just fought, explored, solved, discovered, rested, backtracked, or arrived;
- whether this is a story-bearing cell or ordinary playable space;
- current pressure / recovery window;
- what the environment already communicates visually.

### F. HD-2D production/staging context
Use current `14_ART_AND_VISUALS` authority plus `13_UI_AND_IMPLEMENTATION/DIALOGUE_UI.md`.

Current character runtime direction is B00 rigged 3D field/battle models with high-resolution 2D portrait presentation where appropriate. Historical fixed 80px/200px sprite targets are not current production gates.

### G. Battle / encounter legality
Use current battle and encounter authority when dialogue touches combat:
- no presentation-created bonus actions;
- no invented interrupts or movement actions;
- no dialogue line implying a mechanic that did not occur;
- no mandatory conversation randomly interrupted by an encounter.

---

## 3. Dialogue Director scene-job packet

Before drafting, the Dialogue Director should be able to answer these fields.

### Story
- chapter / sequence ID;
- exact story position;
- scene purpose;
- mandatory facts/events;
- prohibited future knowledge;
- participant list;
- party state entering/exiting.

### Geography
- location;
- sub-area / cell;
- cell role;
- area phase;
- entry direction / exit direction where relevant;
- important landmark or visible event;
- whether the player controls movement during the exchange.

### Gameplay history
- time/activity since last meaningful story beat;
- recent encounter pressure;
- recent boss / elite / puzzle / traversal mechanic;
- resource/recovery state if narratively observable;
- whether the player is in a quiet interval or pressure corridor;
- whether normal hostile pressure resumes immediately afterward.

### People
- each participant's current state;
- relationship state among the people actually interacting;
- personal memories relevant to this moment;
- what each person knows;
- what each person plausibly notices first.

### World life
- local civilian/work activity;
- current route/supply/repair/weather pressure;
- relevant ordinary-life opportunity;
- relevant local concern that does not exist solely to serve the plot.

### Presentation
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

## 4. Scene modes

### Mode A — Full authored stop scene
Best for:
- major decisions;
- revelations;
- recruitment;
- confrontation;
- emotionally complex processing;
- scenes requiring precise blocking or silence.

Use a safe threshold or deliberately protected story cell. Player movement may lock.

### Mode B — Walking / traversal dialogue
Best for:
- short contextual exchange;
- route observations;
- relationship texture;
- low-complexity explanation that belongs to movement;
- conversation that benefits from the environment remaining active.

Rules:
- use only where gameplay pressure permits;
- player movement/camera/path following may continue;
- mandatory walking dialogue temporarily suppresses encounter triggering for the authored window plus a short buffer;
- encounter pressure is preserved, not reset;
- do not use a long walking scene in a high-pressure pursuit corridor.

### Mode C — Post-battle reaction
Best for:
- one or two observations;
- quick jokes;
- evidence noticed from the fight;
- immediate emotional residue.

Keep it short enough to live in post-battle grace unless an explicit safe scene follows.

### Mode D — Story-bearing cell interaction
A normal playable cell can carry narrative through:
- optional NPC talk;
- landmark observation;
- short party exchange;
- environmental discovery;
- local dispute;
- small relationship beat.

This distributes story through the location without turning every beat into a full cutscene.

### Mode E — Character-Life / hub / camp
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

### Mode F — Pre-boss / post-boss threshold
Pre-boss dialogue should not over-explain a confrontation the environment or prior story already established.

Post-boss dialogue receives a real breath after:
- mandatory bosses;
- genuine form conclusions;
- Prime awakenings;
- major recruitment;
- surrender/capture;
- major revelation.

Do not immediately throw the player into a random encounter after a major authored payoff.

### Mode G — Story-combat pause
Use only when current battle authority explicitly permits an authored pause/transition. The dialogue must not imply free actions outside the legal battle system.

---

## 5. Area-design rules that directly affect dialogue

The ongoing JRPG area study is research/design guidance. Its current numerical timing bands are not silently locked canon.

The following structural concepts are valid authoring tools:

### Playable density
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

### Cell grammar
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

### Story-bearing cells
A cell can remain playable while carrying narrative function. This supports:
- distributed worldbuilding;
- short relationship beats;
- NPC conflict;
- location-specific observations;
- foreshadowing;
- optional lore.

Not every story-bearing cell becomes a cinematic.

### Story distributed by sub-area
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

### Quiet intervals
Dialogue should account for how long the player has been under the same kind of pressure.

A quiet interval can be valuable after:
- several encounters;
- a difficult traversal mechanic;
- a major reveal;
- a boss;
- sustained visual intensity.

Do not eliminate texture in the name of compression. Remove repetition, not meaningful variation.

### Optional narrative branches
Exploration may reward the player with:
- character banter;
- NPC conversation;
- lore;
- scenery;
- local history;
- relationship texture.

Optional branches should not contain required main-story comprehension unless current story authority explicitly makes that branch mandatory.

### Return / retraversal
If the player reuses space under a changed objective or state, dialogue should notice the changed context when a character plausibly would. Do not repeat the original entry explanation simply because the map is familiar.

---

## 6. Gameplay-loop pressure and dialogue readiness

For scene placement, use a qualitative dialogue-readiness state.

### GREEN
Natural home for dialogue.
Examples:
- town;
- camp;
- secured room;
- recovery point;
- calm story-bearing cell;
- post-battle grace for short lines;
- intentional safe traversal window.

### AMBER
Dialogue possible but should be short or carefully staged.
Examples:
- active route with normal encounter pressure;
- transitional corridor;
- investigation while moving;
- area where stopping too long would damage urgency.

### RED
Do not insert ordinary long dialogue.
Examples:
- active pursuit;
- escape;
- immediate pre-impact danger;
- mechanically demanding traversal;
- battle state without an explicit story pause.

RED can become an authored protected pause only when current story/gameplay authority deliberately creates that pause.

---

## 7. Mature-adult naturalism

Characters may:
- interrupt;
- leave a sentence unfinished;
- repeat themselves;
- answer the wrong part;
- change subject;
- misunderstand;
- refuse;
- become petty;
- swear naturally according to their established voice;
- talk about something unimportant;
- fail to have a useful answer;
- sit in silence.

Do not make adult competence synonymous with emotional omniscience.

Important dialogue earns precision. Most dialogue should not sound like a quotation written for a trailer.

---

## 8. Comedy timing

Comedy is built from character and timing, not inserted joke quota.

Available tools:
- setup → beat → reaction;
- deadpan hold;
- awkward silence;
- escalation;
- callback;
- misunderstanding;
- overconfidence;
- overcommitment;
- reversal;
- one character refusing to participate in the expected joke;
- one character treating a ridiculous premise seriously;
- a relationship-specific insult that would be hostile from somebody else.

Do not flatten pair languages into one universal party banter voice.

---

## 9. Anime expressiveness

Anime influence supplies:
- readable expression changes;
- tonal elasticity;
- sincere emotional reaction;
- heightened but specific body language;
- fast movement between mundane, funny, dangerous, and painful states.

It does not authorize:
- constant shouting;
- stock embarrassment loops;
- generic sweat-drop behavior as prose shorthand;
- sexualized gag reactions;
- catchphrase dependence;
- characters becoming stupid to make a joke work.

Use the field model, portrait, camera, pause, and sound together so dialogue does not have to announce the reaction.

---

## 10. Economical HD-2D staging

The goal is **economical**, not cheap-looking.

Spend complexity where the player sees and feels it.

### Low-cost / high-value scene tools
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

### Medium-cost tools
Use when earned:
- area-specific bespoke gesture;
- short authored path/blocking sequence;
- unique prop state;
- selective depth move;
- localized VFX;
- specific environmental animation.

### High-cost tools
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

### Hybrid-performance rule
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

## 11. Visual-first information rule

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

## 12. Scene rhythm

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

## 13. Scene economy

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

## 14. Canon Checker scene audit

A scene should not commit until the checker can answer yes to the relevant questions.

### Canon
- Is every fact current?
- Does every character know only what they can know here?
- Are current terminology/classes/Faces/equipment/location names used?
- Does the scene preserve mandatory story causality?

### Character
- Does each participant sound like this person at this point in the relationship?
- Are reactions shaped by current fatigue/stress/history rather than generic drama?
- Is anyone explaining their character-sheet theme too perfectly?

### Ensemble
- Does everyone who speaks need to speak?
- Is silence allowed?
- Does the social geometry feel like people sharing space rather than a turn queue?

### Map / gameplay
- Is this conversation in a credible place to happen?
- Does its length fit the current pressure window?
- Would an encounter or traversal mechanic make the scene impossible?
- Does the scene respect what the player just physically experienced?
- Is important visual information given room before text?

### Craft
- Does the speech sound adult and spoken?
- Is subtext allowed to remain subtext?
- Does humor arise from character and timing?
- Are expressive reactions staged instead of over-described in dialogue?
- Has the scene ended after the point lands?

### Production
- Does the staging use the current HD-2D/B00 presentation?
- Can existing field models, portraits, props, camera, light, sound, and state changes carry the scene?
- Is expensive bespoke animation actually justified?
- Does presentation remain mechanically legal?

Only after these checks should authored story memory/state be committed.
