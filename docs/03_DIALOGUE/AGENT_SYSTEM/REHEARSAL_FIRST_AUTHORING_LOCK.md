# Diyse — Rehearsal-First Dialogue Authoring Lock

**Status:** CURRENT EXPLICIT USER DIRECTION  
**Domain:** dialogue generation / editing workflow  
**Purpose:** preserve the stronger human behavior of the earlier Dialogue Engine rehearsals while keeping every production draft inside the already-established gameplay presentation.

## Hard rule

> **Do not generate the production script directly from canon constraints. Rehearse the people first, edit the rehearsal second, canon-check the edited scene third.**

Story/reveal rules define the playable situation. They are not the conversational voice of the scene.


## Story beat as guardrail

This section absorbs the former separate story-beat guardrail lock.

### Core rule

> **Story structure controls the situation, hard outcomes, reveal boundaries, and gameplay state. It does not pre-write the conversational path.**

A story/beat packet is a **guardrail and destination**, not a rehearsal script.

The Dialogue Director must not convert a structural packet into a list such as:
- Character A states fact X;
- Character B corrects it;
- Character C voices the safety rule;
- Character D summarizes the conclusion;
- Character A explicitly explains why the final choice is voluntary.

That form predetermines the scene and reduces Person Agents to voice filters over an already-written conversation.

### What may be supplied to Person Agent rehearsals

Supply only what the characters need to inhabit the moment:
- current location and visible situation;
- who is present;
- what just happened;
- each person's actual knowledge and memories;
- relevant relationship state;
- immediate physical/gameplay pressure;
- the genuine problem or decision in front of them;
- hard story outcomes that must be true by the end;
- forbidden reveals / continuity boundaries.

Where a fact has necessary provenance, that provenance remains binding. Example: Torren may own a route observation because he physically copied or observed it; Ilyra may own a medical observation because she personally examined the condition. This is not permission to assign every required story point to a speaker.

### What must NOT be supplied as rehearsal choreography

Do not pre-compose:
- speaker order;
- question → answer → correction sequences;
- required jokes;
- required interruptions;
- required verbal acknowledgements;
- explicit statements of theme;
- explicit statements of character motivation that behavior can show;
- lines whose only purpose is to certify that the scene satisfied a structural rule;
- recruitment speeches explaining why someone is joining;
- safety speeches when a character can simply behave cautiously;
- knowledge-firewall dialogue such as characters repeatedly announcing what they do not know;
- canon-checker phrasing such as `that's all we know`, `nothing is proven`, `important distinction`, `we cannot conclude`, or `that is the fact` when ordinary speech can carry the same boundary.

**Reveal firewalls are production constraints, not required spoken dialogue.** Prefer to preserve them through what characters simply do not claim, or through natural questions, hesitation, disagreement, irritation, incomplete theories, concrete observations, or a plain `don't know` when that is what a person would actually say.

The Canon / Knowledge Checker remains responsible for ensuring the finished scene does not overclaim.

### Outcome versus route

Valid hard outcome:
> By the end of Beat 8, Nimera has chosen to continue and permanently joins the party.

Invalid rehearsal instruction:
> Cyanis tells Nimera she is free to choose; Nimera explains her reasons; Torren asks whether she means permanently; Nimera explicitly confirms permanent recruitment.

Valid hard outcome:
> The party chooses Ivorybridge as the next practical northern search point without Ancient evidence confirming that the routes lead there.

Invalid rehearsal instruction:
> Cyanis states that Ivorybridge is not on the Ancient map; Nimera says it is only a hypothesis; Ilyra restates that the route destination remains unknown; Torren verbally confirms the uncertainty before they leave.

The rehearsal must discover how the people actually get there.

### Dialogue Editor rule

After rehearsal, aggressively remove any line that exists mainly to:
- explain the beat structure;
- explain why a character is allowed to make their own choice;
- summarize a motivation already visible through behavior;
- restate a reveal firewall;
- assign credit to every participant;
- make the scene's theme explicit;
- ensure every present character has spoken.

A required outcome may be communicated by action, silence, gameplay transition, UI confirmation, or a very small exchange. It does not require a speech.

### Quality test

Before approving a scene, hide the beat checklist and ask:

> **Would these people still plausibly arrive at this exchange if they only knew the situation they are living through?**

If the answer is no—if a line exists because the author needs to explain the story architecture—rerun or cut it.

### Chapter 3 Beats 6–8 remediation

Beats 6–8 must be rerun under this rule before Chapter 3 dialogue production continues into Beat 9.

Preserve their structural outcomes and reveal boundaries, but retire conversational choreography from their production specs and drafts.

## Gameplay presentation comes first

Before staging any dialogue, obey:
> `../../13_UI_AND_IMPLEMENTATION/FIELD_TRAVERSAL_AND_DIALOGUE_PRESENTATION_LOCK.md`

The dialogue layer does **not** get to invent a different game presentation.

Current baseline follows an FF7-style field-scene grammar adapted to Diyse:
- ordinary traversal shows **Cyanis only** as the field character;
- companions do not form a visible follower train during free exploration;
- when an authored scene triggers, the other characters who are present may appear as field models for that scene;
- after the scene, ordinary exploration returns to Cyanis-only traversal;
- dialogue is primarily **simple portraits + dialogue box** over the existing field/background;
- scene field models may provide simple spatial presence/blocking, but portraits and text carry most of the acting;
- the environment follows layered HD-2D / 2.5D construction with selective depth geometry, not a fully modeled 3D cinematic stage.

A character may be present in the conversation without being physically represented during traversal, then appear normally once the scene trigger stops exploration.

## Required authoring sequence

### 1. Dialogue Director — build the situation
Provide each relevant Person Agent with only the material needed to inhabit the current moment:
- where they are;
- what just happened;
- what they personally know;
- what they want right now;
- who else is present;
- current relationship state;
- physical/gameplay pressure;
- visible world information already required by the area/beat;
- required story event or decision;
- whether the moment is ordinary traversal or an authored triggered scene.

The Director does not pre-compose the desired conversation rhythm and does not invent extra environment content or physical staging merely to make the scene feel richer.

### 2. Person Agents — rehearse independently
Let each person respond as themselves rather than as a carrier for one required fact.

The rehearsal may contain interruption, false starts, unfinished answers, silence, misunderstanding, wrong-part answers, irritation, mundane observations, profanity where natural, failed jokes, private pair-language, nonparticipation, or plausible error.

**Do not make everyone clever at the same time.**

**The character sheet is for the writer. The character must never sound like they have read it.**

A character does not need to state their trait, expertise boundary, relationship function, theme, or knowledge limit for that information to shape their behavior.

### 3. Dialogue Editor — cut aggressively
The rehearsal is a scene laboratory, not the finished script.

The Editor should:
- keep the strongest human behavior;
- remove repeated information;
- remove lines whose only job is canon compliance;
- remove party roll call;
- preserve selective participation and relationship-specific rhythm;
- let portraits, silence, and already-required story visuals carry what speech does not need to carry;
- end exchanges once the point lands;
- cut polished lines that make everyone sound equally authored;
- strip physical micro-direction the actual field presentation does not need.

More natural rehearsal material is useful. More final lines are not automatically better.

### 4. Canon Checker — remain invisible
Only after the dialogue has a human shape does the Canon Checker verify:
- reveal timing;
- individual knowledge;
- terminology;
- gameplay legality;
- map/traversal legality;
- character authority;
- encounter rules;
- current field/dialogue presentation;
- production constraints.

If a line violates canon, repair or remove that line without teaching the cast to verbalize the firewall.

`SPOKEN_DIALOGUE_VS_NARRATION_LOCK.md` remains mandatory and includes the knowledge-firewall invisibility rule.

### 5. Economical presentation pass — REDUCTIVE, NOT ADDITIVE
After dialogue survives the Editor and Canon Checker, translate the beat into the established game presentation rather than designing a new cinematic layer.

#### Ordinary traversal
> **Cyanis remains the sole visible party field character.**

No dialogue runs while Cyanis is moving under player control. If the route needs a conversation, the game must trigger an authored stop and pause/lock movement before the dialogue begins.

#### Authored triggered scene
> **Relevant present characters may appear as field models once the scene trigger stops ordinary traversal.**

This is normal presentation, not a special exception. A triggered scene may show the party/NPCs standing together in sensible positions while portraits and the dialogue box carry the conversation.

After the scene, those companion models do not become a permanent follower train; normal traversal returns to Cyanis-only field presentation.

Do not automatically add:
- companion walking/following during free traversal;
- constant pointing, crouching, equipment adjustment, weapon handling, foliage interaction, or other tiny physical gestures;
- extra rooms, platforms, paths, ledges, set pieces, or environmental beats;
- new NPC business, crowds, or ambient comedy;
- props solely to give characters something to touch;
- extra clues or environmental storytelling not required by current story/map authority;
- bespoke animation;
- camera/light/sound choreography just because it is available;
- extra dialogue beats created to justify staging.

Simple scene-field presence is allowed. Micro-choreography is not the default.

### Micro-detail accumulation is also additive
A scene can become expensive and over-authored without adding one large set piece.

The dialogue manuscript is not the area-art dressing document and not an animation blocking script.

Do not stack repeated tracks, broken brush, mud details, scratches, bones, extra markers, tiny prop interactions, repeated looks/turns, hand business, posture business, or successive environmental clues merely to make traversal feel authored.

> **Prefer one necessary story visual over five supporting visual details.**

## Traversal and combat dialogue boundary

There is **no walking/traversal dialogue** and **no mid-battle dialogue**.

- During ordinary player-controlled traversal, dialogue does not run.
- A route conversation requires an authored trigger that stops traversal first.
- During active combat, dialogue does not run.
- Boss or battle-related dialogue belongs immediately before combat begins or after combat has fully ended.
- Post-battle reaction may be brief, but it is still a post-combat state rather than an active-battle bark.

This boundary is global. A guide, relationship beat, lore observation, joke, or dramatic line does not create an exception.


## Quality tests

Before a scene is treated as a strong working draft, ask:

> **If the story/reveal checklist were hidden from us, would these exact people still plausibly talk this way in this exact situation?**

Then:

> **Does this scene use the game we already decided to build, or did the dialogue draft quietly invent a different presentation?**

Then:

> **Does this physical action actually need to be shown, or can the scene field models simply stand there while the portraits and dialogue carry it?**

If it does not need to be shown, remove it.

## Chapter 1 remediation

Chapter 1 dialogue must be normalized to this gameplay presentation before later beats are treated as production-ready.

That means preserving the dialogue that works while correcting presentation to:
- Cyanis-only ordinary traversal;
- relevant party/NPC field models appearing when authored scenes trigger;
- portraits + dialogue box as the main conversational performance;
- simple scene blocking where useful;
- no unnecessary micro-gesture/prop choreography;
- only story-required major visuals.

This is a staging correction, not permission to unnecessarily rewrite approved character dialogue.
