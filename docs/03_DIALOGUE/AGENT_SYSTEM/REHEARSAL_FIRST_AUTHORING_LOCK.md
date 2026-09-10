# Diyse — Rehearsal-First Dialogue Authoring Lock

**Status:** CURRENT EXPLICIT USER DIRECTION  
**Domain:** dialogue generation / editing workflow  
**Purpose:** preserve the stronger human behavior of the earlier Dialogue Engine rehearsals while keeping every production draft inside the already-established gameplay presentation.

## Hard rule

> **Do not generate the production script directly from canon constraints. Rehearse the people first, edit the rehearsal second, canon-check the edited scene third.**

Story/reveal rules define the playable situation. They are not the conversational voice of the scene.

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

`KNOWLEDGE_FIREWALL_INVISIBILITY_RULE.md` remains mandatory.

### 5. Economical presentation pass — REDUCTIVE, NOT ADDITIVE
After dialogue survives the Editor and Canon Checker, translate the beat into the established game presentation rather than designing a new cinematic layer.

#### Ordinary traversal
> **Cyanis remains the sole visible party field character.**

Legal walking dialogue may use portraits/text while Cyanis moves. A guide does not need to appear physically just because they are directing the route.

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

## Walking dialogue

`WALKING_DIALOGUE_LOCK.md` still controls when speech may happen during traversal.

A legal Torren- or Maevra-guided walking exchange does **not** require that guide on the field. Cyanis remains the visible traversal avatar; the guide speaks through the portrait/dialogue UI.

If the party reaches an authored stop/trigger, the relevant characters may then appear as field models for that scene.

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
