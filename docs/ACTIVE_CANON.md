# Diyse — Active Engineering Canon Guardrails

This file is an implementation-facing summary. It does **not** replace the authoritative Diyse master canon, active annexes, protected character source files, or newer explicit user approvals. If this summary conflicts with a newer controlling project authority, the newer authority wins and this file must be updated deliberately.

## Current written authority

- **Controlling whole-project authority:** Diyse Clean Active Master Canon **v1.40 Chapter 0 Rebuild Change-Control Overlay**, inheriting all compatible v1.39 authority.
- **Immediate predecessor/root baseline:** Clean Active Master Canon v1.39 — Chapter 1 Production Dialogue Canonization and Step 7C Second-Chapter Completion Revision.
- **Technical baseline inherited:** Active Technical Annex v1.39 plus the v1.40 Chapter 0 implementation/change-control overlay.
- **Chapter 1 canon wording:** `Diyse_Chapter_1_Production_Dialogue_S007-S011_v1.0_2026-08-09.docx` remains unchanged and controlling.
- **Chapter 0 change-control record:** `docs/authority/CHAPTER_0_REBUILD_V1_40_CHANGE_CONTROL_2026-08-09.md`.
- **Recovery checkpoint target:** v1.40 / Audit55. v1.39 / Audit54 becomes the frozen predecessor when the Audit55 package is issued.

## Workflow state

- Dialogue study: **COMPLETE**.
- Step 7B.5 technical feasibility: **PASS — real Android device**.
- Step 7B.6 production dialogue handoff: **COMPLETE / PASS**.
- Step 7C Dialogue-First Scene Writing: **ACTIVE**.
- Rebuilt Chapter 0 S001-S006: **COMPLETE / USER-APPROVED / ACTIVE CANON**.
- Chapter 0 runtime Resource replacement and revalidation: **PENDING**.
- C01 `The Fire Is Too Close` and C02 `Food After Triage`: **retained optional Chapter 0 Character-Life canon**.
- Chapter 1 S007-S011 prose: **CANON / PRESERVED**.
- Chapter 1 Resource conversion and implementation validation remain a separate pending gate.
- Active implementation repository: `zxxdjxxz-del/Diyse-Game`.

## Chapter 0 supersession rule

The previous Chapter 0 production merge `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5` remains valid historical proof of the dialogue Resource/validator/Android pipeline, but its mandatory scene Resources S001-S006 are **not current content authority after v1.40**.

Until exact v1.40 replacement Resources are serialized and revalidated:

- do not copy dialogue or staging from the old S001-S006 Resources into new content;
- do not report the old Chapter 0 Godot/Android PASS as validation of the rebuilt scenes;
- do not delete the old Resources until their exact replacements and validators are ready on the same branch;
- do not modify C01/C02 merely because mandatory Chapter 0 was reopened; they remain current unless a compatibility change is actually required.

## Project foundation

- Diyse is a mature-fantasy 2.5D JRPG with an approximately 20-hour critical path.
- Permanent roster: exactly six — Cyanis Dovaren, Ilyra Amarin, Torren Harth, Nimera Pellan, Vaelira Serren, Seyrik Rell.
- Maximum active battle party: four.
- Character level cap: 50.
- Combat is command-driven traditional discrete rounds.
- MP is the universal ordinary Ability resource; there are no character-specific combat gauges/resources.
- Permanent battle commands: Attack / Ability / Card / Item / Defend.
- Current Card collection: 24 Standard Cards + 12 Prime Cards.
- Standard Cards are unlimited-use.
- Current Faces: Might, Elements, Grace, Resource, Change, Ruin.
- After-story free roam exists; no exclusive post-ending progression or hidden true ending.

## Presentation authority

Diyse is a **2.5D** game: real 3D environments/depth/lighting/traversal and cinematic battle spaces combined with stylized 2D/2.5D character presentation and expressive illustrated dialogue portraits where appropriate.

## Dialogue authority

Diyse has **no player dialogue choices**. Cyanis is a defined authored protagonist. Do not implement response wheels, tone menus, affinity dialogue, branching player-spoken responses, persuasion trees, good/evil dialogue, or romance dialogue choices.

Production dialogue uses the locked stable-ID interface:

- `DiyseDialogueSceneDefinition` Resources;
- stable semantic scene, beat, character/NPC, expression, trigger, and completion IDs;
- beat IDs use `<SCENE_ID>_B###`;
- portrait assets resolve through `DiyseDialoguePortraitRegistry` rather than raw paths in scene data;
- camera/staging/movement/implementation information remains cue metadata separate from spoken text;
- known choice/response/branch fields are rejected by validation.

### Rebuilt Chapter 0 dialogue locks

- S001: Cyanis ordinary convoy work/observation first; Ilyra absent; no supernatural response; clean Raider-to-Round-1 handoff with no free attack.
- S002: survivor/wreck exploration plus four authored tutorial battles; no pursuit decision.
- S003: credible pursuit refusal; Handler/Hound and Pursuer separated by player-controlled stabilization; Pursuer intent is already locked before command confirmation; Ilyra not clearly shown/heard.
- S004: Ilyra first clearly appears through independent triage authority; incomplete green-and-gold response occurs here; First Mercy does not respond.
- S005: Cyanis + Ilyra vs Riftmaw + two Handlers; one HP bar; Restrained -> Unbound between completed rounds; optional Cornered behavior; no Card rescue.
- S006: incomplete survivor count, bounded playable sweep, one survivor recovered, one confirmed dead, at least three unresolved; Ilyra independently remains; Brackenwall next.

Protected S006 recruitment center:

> I'm not doing it for you.  
> There are still people missing.  
> Then we find them.

## Combat implementation authority

The accepted round architecture is mandatory:

1. beginning-of-round state is established;
2. each conscious enemy locks one legal action from that state before inspecting any unconfirmed player command;
3. the player selects one action for every conscious active party member before confirmation;
4. Item actions resolve first;
5. Defend actions resolve second;
6. all remaining actions resolve by current effective Speed;
7. Speed determines order only and never grants an extra ordinary action.

Do not introduce overwatch, interrupts, reaction commands, real-time interception, hidden bonus turns, Speed-based extra actions, or enemy retargeting after reading unconfirmed commands.

Visible intent represents an already-locked enemy action and is information for round planning, not a reaction window.

### Chapter 0 combat learning progression

1. Raider — basic round grammar.
2. Raider + Crossbowman — differentiated threats; no free pre-battle shot.
3. Shieldbearer + Raider — target-value/defender role; no spontaneous intercept reaction.
4. Rift Hound + Raider — Speed/order pressure only.
5. Handler + Hound — complementary legal enemy actions.
6. Ruin Vanguard Pursuer — visible locked intent/objective planning.
7. Riftmaw + two Handlers — first major Cyanis + Ilyra whole-party planning encounter.

Riftmaw uses one continuous HP bar. Restrained -> Unbound is processed between completed rounds without refill or free action. Cornered changes later round-start weighting only. Any surviving Handler after Riftmaw defeat exits through a legal scripted withdrawal/neutralization classification without a revenge action.

## Chapter 0 / Chapter 1 information firewall

Through Chapter 0:

- the damaged Card/object remains unidentified;
- First Champion is not identified;
- no Prime/bearer framework is explained;
- First Mercy does not respond;
- the Card does not solve Riftmaw.

Chapter 1 S007-S011 remains v1.39 canon. S007 opens Cyanis + Ilyra at Brackenwall beside the sealed artifact wagon; Maevra becomes temporarily playable by the end of S007; Torren becomes permanent by the end of S009; S010 is the first sustained four-commandable-character leg; S011 leads to Dunmere while First Champion remains unidentified.

## Cards / Primes / persistence

- Standard Cards remain unlimited-use and data-driven; no charges, Essence, Card ranks, refresh counters, or per-battle Standard-use counters.
- Prime Manifestations remain directly controlled and distinct from ordinary summons under the established replacement/suspension architecture.
- Persistent game/session state remains separate from scene nodes and serializes as versioned plain data under Godot `user://`.

## Relationship/story guardrails relevant to engineering

- No romance system, affection meter, jealousy system, triangle, triad, or route.
- Authored relationships can exist without gameplay meters.
- Maevra is temporary playable/recurring major ally, never a seventh permanent roster member.
- Kessara remains nonplayable.
- All six permanent characters survive the canonical ending.
- Vaelkor does not knowingly ally with the surviving fragment; covert influence does not remove his human agency or responsibility.

## Proof-content exclusion

Do not mistake technical fixtures or superseded content for canon. Graybox geometry, placeholder assets, proof dialogue, `PROOF_SCHEMA`, proof enemies/stats, `Proof Strike`, temporary flat damage/rewards, proof flags/cues, debug UI, and the superseded pre-v1.40 S001-S006 scene text are not current production content authority.

## Historical repository rule

The older `zxxdjxxz-del/Diyse` repository is historical prototype material only. Its libGDX architecture and prototype mechanics are not implementation authority for `Diyse-Game`.