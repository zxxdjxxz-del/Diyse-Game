# DIYSE Chapter 4 — Acceptance Ledger

**Chapter:** Chapter 4 — *The Seventh Reaction*  
**Working branch:** `author/chapter-04-dialogue`  
**Whole-project authority:** Complete Master Canon v1.64 / Audit79, plus later explicit user corrections/approvals  
**Ledger started:** August 18, 2026

## Purpose

This is the living change-control record for Chapter 4 dialogue/scene development.

Every user acceptance or direct canon correction made during Chapter 4 development must be recorded here before work advances far enough for that decision to be lost in chat history.

The ledger distinguishes:

- **LOCKED / ACCEPTED** — approved controlling material.
- **SUPERSEDED** — previously accepted material replaced by a later explicit correction.
- **WORKING / NOT YET ACCEPTED** — drafted material that must not be treated as canon merely because it exists.
- **RETRACTED / INVALID PROMOTION** — material the assistant incorrectly promoted without actual user acceptance.

## Recording rules

1. A direct user correction is immediately controlling and must be recorded as a LOCKED entry.
2. An explicit acceptance is recorded as a LOCKED entry.
3. When continuation clearly follows approval of the immediately preceding proposed scene, record the accepted scope conservatively; do not silently promote unrelated material.
4. Exact dialogue wording must be copied verbatim when wording itself is accepted.
5. Do not rewrite an accepted entry in place to hide history. Add a new entry and mark the old one SUPERSEDED when a later correction changes it.
6. Working drafts remain non-canon until accepted.
7. Before drafting the next Chapter 4 scene, check this ledger and the current whole-project authority.
8. **Before each scene, briefly re-check the participating characters' personalities/voice anchors and the relationship state relevant to that scene so the writing stays in character.** This is a scene-level guardrail, not a requirement to break scenes into tiny dialogue blocks.
9. Preserve the established adult-natural dialogue style and expressive 2D/2.5D JRPG/anime reaction language without turning either into a rigid per-line checklist.
10. **Before each scene, also check the broader production/gameplay requirements:** continuity and knowledge firewall, current party state, scene purpose, affordable 2.5D staging, exploration/combat rhythm, random-battle eligibility, encounter spacing, and any relevant Hunt/optional-content or chapter-transition state. Do not turn a chapter route into uninterrupted dialogue; allow traversal and random-battle spaces between authored conversations where the fiction supports hostile exploration.

---

## ACCEPTED / LOCKED

### CH4-A001 — Three-map order and Ivorybridge destination

**Date:** 2026-08-18  
**Status:** LOCKED  
**Acceptance type:** Direct user correction

**Controlling user wording:**

> The second map is the one found at the wayfinder. The third map is the one from the post warden room. After studying the 3 they decide the next stop is ivorybridge

**Locked interpretation:**

- The party does **not** begin Chapter 4 already knowing that Ivorybridge is the next destination.
- The three-map comparison happens **before** the decision to travel to Ivorybridge.
- In the three-map comparison set:
  - **Map 2** is the map found at the **Wayfinder** in Chapter 1.
  - **Map 3** is the map from the **post-Warden room** in Chapter 3, preserved through Torren's quick field copy/sketch.
- The Wayfinder map was the **first map the party found chronologically**; this entry does not redefine the provenance of Map 1 in the three-map comparison set.
- Only after studying all three maps together does the party identify **Ivorybridge** as the next stop.
- Therefore the Chapter 4 travel lead comes from the party's own three-map investigation rather than from arriving in Ivorybridge first and solving the relationship afterward.

**Supersedes:** Any working Chapter 4 opening that places the three-map comparison in Ivorybridge or assumes the party already knows Ivorybridge is the destination before studying the three maps.

### CH4-A002 — S022_B001–B011 exact opening and Vaelira introduction

**Date:** 2026-08-18  
**Status:** LOCKED  
**Acceptance type:** Explicit user acceptance — “I accept it”

**Accepted exact source:** `docs/chapters/dialogue/chapter_04/S022.md`, S022_B001 through S022_B011.

**Locked scope:**

- Ivorybridge arrival and settlement presentation.
- Torren/Nimera/Ilyra/Cyanis opening road-and-liquor banter.
- The technician sends the party to **Vaelira Serren**.
- Vaelira is introduced **working competently**, not posing as an exposition device.
- The three maps are laid out for Vaelira in the already-locked A001 order/context.
- Torren reads terrain; Nimera reads constructed geometry; Vaelira recognizes why the maps connect.
- Vaelira identifies the maps as independent maps using the same positional grammar rather than fragments of one sheet.
- The Sixfold Annex transcription establishes a related Ancient regulation system.
- Vaelira's contained demonstration succeeds exactly as predicted and establishes genuine expertise.
- Exact central exchange is locked:
  - `CYANIS: Who checks your model?`
  - Vaelira answers herself / Annex staff.
  - `CYANIS: Who checks theirs?`
  - Cyanis ultimately distinguishes checking the answer from checking the question.
- The anomaly is re-read from boundary marker to possible **transfer point**.
- Vaelira explicitly says she does not know what is being transferred rather than bluffing.
- S022_B011 ends with the decision to go to the **Sixfold Annex**, followed by Ilyra asking about food and Torren immediately agreeing.

**Exact-wording rule:** The accepted wording/staging in `S022.md` B001–B011 is controlling and must not be rewritten unless explicitly reopened by the user.

### CH4-A005 — Scene-level personality/relationship check

**Date:** 2026-08-18  
**Status:** LOCKED  
**Acceptance type:** Direct user workflow correction

**Controlling user wording:**

> I think I said that wrong I just meant before each scene we should check to make sure we are sticking we the characters personalities a little more. We can do it scene by scene to we don't have to do such small blocks

**Locked workflow requirement:**

- Before drafting each **scene**, briefly review the personalities/voice anchors of the characters participating in that scene.
- Check the relationship state that matters to those interactions so nobody jumps ahead in familiarity, intimacy, hostility, or trust.
- Then draft the scene at a normal useful size. There is **no requirement** to split a scene into tiny blocks merely to perform this check.
- Continue using the established adult-natural dialogue and expressive 2D/2.5D JRPG/anime reaction style.
- Scene-level review is a consistency guardrail, not a rigid visible checklist that has to appear in the dialogue itself.

**Supersedes:** CH4-A003's overly strict “before every pass/block” interpretation.

### CH4-A006 — Scene-level full production/gameplay check and dialogue spacing

**Date:** 2026-08-18  
**Status:** LOCKED  
**Acceptance type:** Direct user workflow correction

**Controlling user wording:**

> Also doing the other checks and cheap 2.5d, random battles with spaces in-between dialogue like we did on the other chapters

**Locked workflow requirement:**

Before drafting each Chapter 4 scene, do the same broader integration check used on the completed chapters, not only the personality/relationship check:

- confirm the scene's story purpose, continuity, chronology, geography and current party state;
- preserve the modern-knowledge / Ancient-Diysean knowledge firewall and avoid future-lore leakage;
- check character personalities and current relationships as required by CH4-A005;
- stage the scene for **affordable 2.5D production** using reusable portraits, expression/pose swaps, camera inserts, props, authored environment states, lighting/VFX and small sprite movement rather than expensive bespoke cinematic animation, physics simulation or systemic crowd behavior;
- preserve the established adult-natural dialogue plus expressive JRPG/anime reaction performance;
- treat **traditional random battles as the normal hostile-exploration layer where fiction supports them**;
- suppress random encounters in authored safe/story pockets, towns, conversations, boss staging and other deliberately controlled moments;
- leave real **exploration/traversal space between dialogue scenes and dialogue clusters** so the chapter does not become an uninterrupted conversation corridor;
- use appropriately sized random-battle stretches rather than giant empty zones or a fixed forced battle after every conversation;
- when a route or dungeon continues across multiple story beats, let gameplay breathe between them with movement, exploration, environmental observation and encounter pressure before the next authored dialogue trigger;
- check relevant encounter/boss/Hunt/optional-scene rules and chapter-transition consequences before locking the scene.

This requirement follows the existing project baseline in `docs/ACTIVE_CANON.md`: random battles are the ordinary hostile-exploration layer, safe/story pockets suppress triggering, and affordable 2.5D relies on reusable poses/portraits/props/camera inserts and authored environment states.

### CH4-A007 — Promote the scene-authoring method to a permanent whole-game rule

**Date:** 2026-08-18  
**Status:** LOCKED / WHOLE-GAME WORKFLOW AUTHORITY  
**Acceptance type:** Direct user instruction

**Controlling user wording:**

> This should be the rule going forward for the rest of the game it needs to be always remembered

**Locked interpretation:**

- CH4-A005 and CH4-A006 are no longer merely Chapter 4 habits; their combined scene-authoring method is the default workflow for **all remaining DIYSE scene development**.
- The durable whole-game authority is now `docs/SCENE_AUTHORING_STANDARD.md`.
- `docs/STEP_7C_AUTHORING_TEMPLATE.md` now requires that standard before new scene drafting.
- The rule applies to Chapters 4–12, the Sixfold Accord, optional Character-Life/hub scenes, Hunt-linked authored scenes, battle-linked authored scenes, and `WORLD_AFTER` aftermath content, plus any earlier scene explicitly reopened later.
- Before each scene: check story/continuity, knowledge, party state, personalities/voices, relationship progression, adult-natural dialogue, expressive JRPG/anime reactions, affordable 2.5D staging, gameplay breathing room, random-battle spacing where appropriate, encounter/boss/Hunt constraints where relevant, and the handoff into the next playable state.
- Scene drafts may be normal useful size; this requirement does **not** force tiny-block authoring.
- Dialogue must not crowd out exploration/combat. Hostile routes should contain real traversal/random-battle space between authored dialogue beats where fiction supports it; safe/story pockets remain encounter-suppressed.
- Chapter completion still requires mandatory scenes plus that chapter's associated optional Character-Life/hub scenes, followed by a whole-chapter integration pass.
- This whole-game rule remains active unless the user explicitly revises or supersedes it later.

---

## SUPERSEDED / RETRACTED

### CH4-A003 — Mandatory pre-pass personality / relationship / performance check

**Status:** SUPERSEDED by CH4-A005.

The earlier interpretation required a re-check before every small dialogue pass/block. The user clarified that the intended rule is **once per scene**, allowing normal-sized scene drafts.

### CH4-A004 — S022_B012–B014 promotion

**Status:** RETRACTED / INVALID PROMOTION.

The assistant incorrectly treated a prior “Let's continue” as acceptance of S022_B012–B014 even though that continuation request occurred **before** those beats were drafted. The user never accepted B012–B014.

Consequences:

- S022_B012–B014 are **not canon** and are not accepted Chapter 4 source.
- `S022.md` has been restored to the actual accepted boundary: **S022_B001–B011 only**.
- Future continuation resumes after B011 and may be drafted at normal scene-sized scope under the whole-game standard promoted by CH4-A007.

---

## WORKING / NOT YET ACCEPTED

No additional Chapter 4 material is currently accepted beyond CH4-A001, CH4-A002, CH4-A005, CH4-A006 and CH4-A007.

The next Chapter 4 scene/continuation after S022_B011 remains working until the user accepts, corrects, or replaces it.

---

## Supersession index

| Entry | Status | Replaced by |
|---|---|---|
| CH4-A003 | SUPERSEDED | CH4-A005 |
| CH4-A004 | RETRACTED / INVALID PROMOTION | — |

## Next acceptance number

**CH4-A008**