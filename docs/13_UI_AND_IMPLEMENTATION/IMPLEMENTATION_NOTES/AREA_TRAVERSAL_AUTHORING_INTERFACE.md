# Diyse — Area & Traversal Authoring Interface for Dialogue

**Status:** ACTIVE DESIGN INTERFACE / RESEARCH-DERIVED  
**Owner:** `13_UI_AND_IMPLEMENTATION`  
**Source basis:** ongoing `Diyse_JRPG_Area_Design_Study` plus compatible current gameplay/dialogue pacing authority.  
**Important:** this document does **not** lock exact area minutes, cell counts, branch counts, encounter counts, chapter runtimes, or level bands unless a current owning area/story/balance source separately locks them.

## Purpose

Dialogue cannot be authored independently from the space and gameplay that surround it.

This interface gives `03_DIALOGUE` the map/traversal information needed to place and shape scenes without turning the ongoing area-design research into accidental hard canon.

---

## 1. Playable density, not raw map size

The area study's central useful principle is:

> **Meaningful play matters more than raw physical footprint.**

A location gains playable density through combinations of:
- traversal;
- combat;
- route choice;
- treasure/reward;
- landmarks;
- environmental discovery;
- puzzles/mechanics;
- NPC interaction;
- party dialogue;
- rest/recovery;
- visual change;
- shortcuts/retraversal;
- optional exploration.

Dialogue is one meaningful beat type among several. Do not solve a sparse area merely by adding more conversations.

---

## 2. Three timing measures

When area timing is eventually measured, distinguish:
- **critical-path time** — direct progression;
- **natural first-play time** — plausible first visit with some exploration;
- **thorough-exploration time** — substantial optional checking.

Dialogue placement should normally be designed around the expected player experience for that route state, not around speedrun traversal or full completionism.

No numerical target becomes canon here.

---

## 3. Cell model

Treat a location as a sequence/network of meaningful cells rather than one continuous undifferentiated map.

Useful roles:
- **Entry cell** — orientation, first visual read, arrival state.
- **Traversal cell** — ordinary movement/combat.
- **Branch cell** — route decision.
- **Reward cell** — treasure, equipment, lore, optional payoff.
- **Challenge cell** — difficult fight, puzzle, hazard, traversal mechanic.
- **Reset/recovery cell** — save/heal/shop/safe room/camp.
- **Story-bearing cell** — gameplay space with an intentional narrative function.
- **Landmark cell** — memorable navigational/visual anchor.
- **Boss cell** — approach, arena, aftermath.

A cell may serve more than one role, but its dominant player experience should be legible.

### Dialogue implication
Line density, staging and duration should match the cell.

For example:
- entry: short orientation or reaction after the visual read;
- traversal: sparse contextual lines;
- branch: practical disagreement or route observation;
- recovery: longer conversation becomes credible;
- landmark: let the image land before explanation;
- boss approach: narrowing, focus, less casual chatter unless contrast is intentional.

---

## 4. Story-bearing cells

A **Story-Bearing Cell** is playable geography that also has an intentional narrative job.

Possible functions:
- optional lore;
- local NPC interaction;
- character/worldview exchange;
- relationship texture;
- foreshadowing;
- ideological conflict;
- intimacy/recovery;
- confrontation setup;
- environmental story.

This allows long locations to distribute narrative across the route instead of placing one large scene at the entrance and one at the exit.

A story-bearing cell does not automatically become a full cutscene.

---

## 5. Distributed story by sub-area

Long routes should be allowed to change narrative function as the player advances.

Illustrative pattern only:

```text
ENTRY
orientation / local texture
    ↓
EARLY TRAVERSAL
worldbuilding / minor NPCs
    ↓
MID AREA
character or ideological exchange
    ↓
RECOVERY NODE
intimacy / regroup / practical conversation
    ↓
LATE AREA
escalation / foreshadowing / reduced optionality
    ↓
APPROACH
confrontation setup
```

The exact sequence depends on the location's story role.

### Dialogue implication
Do not repeat the same explanatory function in every sub-area. The location should feel like it is progressing, not looping through identical conversation beats.

---

## 6. Beat pacing vs progression pacing

These are different.

### Beat pacing
How frequently the player receives something meaningful:
- fight;
- dialogue;
- reward;
- discovery;
- landmark;
- mechanic;
- route choice.

### Progression pacing
How quickly the player reaches:
- midpoint;
- major story scene;
- boss;
- location exit.

A long route can have slow progression but healthy beat pacing.

### Dialogue implication
Do not assume a long traversal requires a major cutscene every few minutes. Minor dialogue, NPC texture, discoveries, encounters and landmarks can share the pacing load.

---

## 7. Event clustering and quiet intervals

Meaningful beats should not be evenly spaced by formula.

Some events benefit from clustering:
- arrival + visual reveal + short reaction;
- boss defeat + silence + immediate consequence;
- settlement entry + civilian activity + optional conversations.

Other stretches benefit from quiet:
- after a heavy reveal;
- after a boss;
- during atmospheric traversal;
- while the player learns a new spatial mechanic;
- before a confrontation.

### Dialogue implication
Silence and gameplay are legitimate pacing. Do not fill every quiet interval with banter simply because the engine can generate it.

---

## 8. Dialogue-readiness states

Use a qualitative state when planning scene placement.

### GREEN — breathable
Good for full authored conversation.
Examples:
- settlement;
- camp;
- secured room;
- recovery point;
- calm story-bearing cell;
- protected boss aftermath;
- intentional safe route segment.

### AMBER — active but manageable
Good for short dialogue or walking exchange.
Examples:
- ordinary encounter-enabled road;
- investigation corridor;
- transitional field segment;
- location where urgency exists but is not immediate.

### RED — sustained pressure
Avoid ordinary long dialogue.
Examples:
- pursuit;
- escape;
- collapse/hazard sequence;
- mechanically demanding traversal;
- active battle;
- immediate threat corridor.

A RED state may contain a deliberate story-combat pause only when current story/gameplay authority creates one.

---

## 9. Dialogue-safe traversal

Standing dialogue-facing gameplay rule:

- Mandatory authored walking dialogue temporarily suppresses encounter triggering for the exchange plus a short buffer.
- The local encounter-pressure state is **preserved**, not reset, discarded, or exploited.
- Short post-battle banter can use the normal grace window.
- Long dialogue requires a credible safe context or explicit protected traversal window.
- Do not weaken an area's intended combat identity globally just to make room for prose.
- If a corridor is supposed to feel like high-pressure pursuit, move the processing conversation to the next secured threshold.
- Boss aftermaths, major recruitment, surrender/capture, Prime awakening, major revelation, and genuine transformation endings deserve authored breathing room before random pressure resumes.

Current implementation may represent the exact suppression mechanics differently over time, but the pacing purpose remains controlling unless explicitly revised.

---

## 10. Normal traversal is gameplay

Diyse should not become a walk-and-talk game by default.

Normal traversal may contain dialogue, but the core pattern remains available:

> **gameplay → natural stopping point → authored scene → gameplay**

Walking conversation is especially appropriate when:
- the speaker is commenting on the route;
- the environment is part of what is being discussed;
- an NPC is physically leading the group;
- the scene is short enough not to punish exploration control;
- maintaining motion improves naturalism.

Stop-and-talk is better when:
- precise blocking matters;
- silence matters;
- multiple people need readable reactions;
- the player needs to process a reveal;
- traversal pressure would undermine delivery.

---

## 11. Side paths and optional dialogue

Exploration branches may reward with narrative rather than only items.

Possible optional narrative rewards:
- local history;
- party banter;
- a relationship beat;
- NPC life;
- environmental storytelling;
- a small mystery;
- a memorable view;
- a practical discovery.

### Boundaries
- Mandatory story comprehension should not depend on an optional branch unless the branch is reclassified as mandatory.
- Longer optional narrative branches should pay off proportionally.
- Returning from an optional branch should not create excessive empty retraversal merely because dialogue happened there.
- Optional conversation should feel connected to the place, not like portable skit content pasted onto any map.

---

## 12. Retraversal and changed state

Reusing geography can be efficient and meaningful when the context changes.

Changed purpose may come from:
- escape;
- altered objective;
- enemy control shift;
- environmental damage;
- opened shortcut;
- changed civilian presence;
- new hazard;
- changed story knowledge.

### Dialogue implication
Characters should react to the **new state**, not replay the original introduction.

Retraversal is most valuable when the player can feel mastery or changed meaning rather than simple backtracking.

---

## 13. Recovery and decompression

A substantial recovery boundary is a useful home for:
- processing what just happened;
- ordinary conversation;
- food/sleep/repair context;
- interpersonal friction;
- quiet affection;
- optional Character-Life material;
- planning without artificial urgency.

Do not treat every rest point as a mandatory emotional scene. Recovery is an opportunity, not a quota.

---

## 14. Environmental storytelling before dialogue

Important spatial information should be allowed to communicate visually.

Examples:
- evacuation flow;
- a damaged bridge;
- changed guard coverage;
- empty stalls;
- repair crews;
- flooded passage;
- distant smoke;
- a machine behaving incorrectly;
- barricade progression;
- a new route opening.

### Dialogue implication
Use dialogue to interpret, disagree, personalize, or act on evidence—not to narrate every visible fact back to the player.

The dialogue UI should not immediately cover a major visual discovery before the player has had a readable moment to see it.

---

## 15. Area scale and progression remain linked

The research study explicitly identifies a future interaction:

> **larger encounter-enabled geography can change player power.**

More route length may create more:
- random encounters;
- EXP;
- drops;
- resource use;
- recovery needs.

Therefore exact map size cannot be finalized independently from progression/encounter validation.

### Dialogue implication
Do not write lines that depend on unvalidated exact encounter counts, levels, travel minutes, or resource depletion unless the current owning balance/story source has locked them.

Characters may react qualitatively to a hard journey, repeated fights, exhaustion or shortage when current scene state supports it.

---

## 16. Map-design handoff fields for the Dialogue Director

Every authored scene inside a traversable location should ideally receive:

```text
location:
sub_area:
cell_role:
area_phase:
story_bearing_function:
dialogue_readiness: GREEN | AMBER | RED
player_control: locked | movement_allowed | partial
encounter_pressure_before:
encounter_pressure_after:
recent_gameplay:
recovery_state:
visible_environmental_information:
entry_context:
exit_context:
optional_or_mandatory:
```

Unknown fields should remain open rather than guessed.

---

## 17. Validation questions

Before placing a dialogue beat in an area:

- Does this line/scene belong to this specific place?
- Is the player in the right pressure state to hear it?
- What meaningful gameplay happened immediately before it?
- What happens immediately after it?
- Is the environment already communicating part of the information?
- Would a short exchange work better than a full scene?
- Would silence work better?
- Does this cell already carry too many meaningful beats?
- Is the dialogue masking a sparse map rather than improving pacing?
- Is an optional branch hiding mandatory information?
- Does the player get a clean visual read of a landmark/reveal?
- Does the scene respect normal random-encounter grammar?
- Is an exact timing/size assumption still research-only?

---

## 18. Relationship to current Dialogue Engine

The controlling dialogue integration file is:
> `../../../03_DIALOGUE/AGENT_SYSTEM/SCENE_CONSTRUCTION_STACK.md`

The Dialogue Director should consume this interface before scene generation whenever location/traversal context is relevant.

The research study remains free to evolve. New measurements may refine this interface without automatically changing story canon or locking numerical area targets.
