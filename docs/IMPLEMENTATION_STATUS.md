# Diyse — Current Implementation Status

**Authority checkpoint:** v1.40 / Audit55 change-control target  
**Inherited root baseline:** v1.39  
**Step 7B.5:** COMPLETE / PASS on real Android hardware  
**Step 7B.6:** COMPLETE / PASS — production dialogue authoring handoff locked  
**Step 7C:** ACTIVE  
**Rebuilt Chapter 0 canon:** COMPLETE / USER-APPROVED  
**Rebuilt Chapter 0 runtime Resource replacement:** PENDING  
**Chapter 1 S007-S011 prose:** CANON / PRESERVED  
**Active repository:** `zxxdjxxz-del/Diyse-Game`  
**Accepted 7B.5 gameplay baseline:** `f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`  
**Accepted 7B.6 implementation merge:** `96c6bdc77f39c988f2185634b4e51546f2a0d76b`

## Controlling Chapter 0 change control

`docs/authority/CHAPTER_0_REBUILD_V1_40_CHANGE_CONTROL_2026-08-09.md`

The user explicitly approved the rebuilt Chapter 0 S001-S006 on August 9, 2026. The new canon supersedes the previous mandatory Chapter 0 wording and encounter assumptions while preserving C01/C02 and Chapter 1 S007-S011.

## Proven technical chain

| Gate | Status | Accepted proof |
|---|---|---|
| 7B.5A | PASS | Clean Godot 2.5D field architecture, camera and collision |
| 7B.5B | PASS | Android touch movement, boundaries and repeatable APK pipeline |
| 7B.5C | PASS | Authored portrait dialogue, expressions, silent reactions, no choices, control return |
| 7B.5D | PASS | Four-character discrete-round combat and deterministic priority/tie rules |
| 7B.5E | PASS | Unlimited data-driven Standard Card path and automatic hostile retargeting |
| 7B.5F | PASS | Bearer-locked direct-control Prime replacement/suspension/return architecture |
| 7B.5G | PASS | Versioned plain-data save/load and persistence across full Android app close/relaunch |
| 7B.6 | PASS | Stable-ID dialogue Resources, portrait registry, authoring template, schema validation, Resource-to-runner integration |
| Old Step 7C Chapter 0 | HISTORICAL PASS / CONTENT SUPERSEDED | Merge `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5` proved the pipeline, validators, Godot regression and Android export for the pre-v1.40 scene set |
| v1.40 Chapter 0 canon | APPROVED / NOT YET RUNTIME-VALIDATED | Rebuilt S001-S006 approved after round-system, continuity, dialogue-density and runtime audit |

## Important implementation distinction

The previous Chapter 0 validation runs and Android artifact remain valid evidence that the production architecture worked, but **they do not validate the v1.40 replacement content**.

Until new Resources are serialized and revalidated:

- `game/content/dialogue/chapter_00/S001.tres` through `S006.tres` are superseded implementation;
- they must not be cited as exact current canon dialogue;
- they should remain in place only until the replacement set is ready to avoid leaving the branch in a half-deleted state;
- C01/C02 remain current optional content unless compatibility work proves necessary.

## Rebuilt Chapter 0 target

Mandatory target runtime: approximately 55 minutes, working range approximately 52-57 minutes.

Authored/tutorial encounter progression:

1. Raider — basic round grammar.
2. Raider + Crossbowman — differentiated threats.
3. Shieldbearer + Raider — target-value decisions.
4. Rift Hound + Raider — Speed/order pressure only.
5. Handler + Hound — complementary support actions.
6. Ruin Vanguard Pursuer — visible locked intent/objective planning.
7. Riftmaw + two Handlers — first major Cyanis + Ilyra whole-party planning encounter.

Chapter 0 does not use the normal random-encounter rhythm; normal hostile random encounters begin in Chapter 1.

## Accepted combat behavior

The resolver remains traditional discrete-round combat:

1. beginning-of-round state processing;
2. enemies lock one legal action before reading any unconfirmed player command;
3. player selects one action for every conscious active party member before confirmation;
4. Item priority;
5. Defend priority;
6. remaining actions by current effective Speed;
7. Speed controls order only and never grants extra ordinary actions.

The v1.40 Chapter 0 replacement must not introduce overwatch, interrupts, reaction commands, real-time interception, bonus turns on state transitions, or enemy retargeting after reading player commands.

Visible intent is information about an already-locked action.

## Chapter 0 scene-state locks

- S001: Ilyra absent; no supernatural response; no free pre-battle Raider action.
- S002: four authored tutorial battles; no pursuit decision.
- S003: pursuit refusal; Handler/Hound; stabilization gap; Pursuer; Ilyra remains unidentified.
- S004: Ilyra first clear appearance; incomplete green-and-gold response; Cyanis stabilization; no hidden S005 buff.
- S005: Riftmaw one HP bar; Restrained -> Unbound between completed rounds; optional Cornered AI weighting; no Card rescue.
- S006: bounded survivor sweep; one recovered alive, one confirmed dead, at least three unresolved; Ilyra remains independently; Brackenwall next.

## Chapter 1 preservation

Chapter 1 S007-S011 production prose under v1.39 remains canon and is not reopened by v1.40.

- S007 opens Cyanis + Ilyra at Brackenwall beside the sealed artifact wagon.
- Maevra becomes temporarily playable by the end of S007.
- Torren becomes permanent by the end of S009.
- S010 is the first sustained four-commandable-character Chapter 1 leg.
- S011 leads to Dunmere and does not identify First Champion.

Chapter 1 Resource conversion/implementation validation remains its own pending gate.

## v1.40 Chapter 0 replacement gate

1. consolidate the exact approved S001-S006 script/cue source;
2. serialize it into stable `Sxxx_B###` Resources;
3. update scene-specific validators and Chapter 0 continuity validation;
4. integrate the approved seven-battle handoffs without changing the resolver contract;
5. run all scene validators;
6. run full Godot regression on the exact final head;
7. run Android debug/export proof on that same head;
8. record a new implementation PASS only after every gate is green.

## Remaining production scope

- v1.40 Chapter 0 Resource replacement and revalidation;
- Chapter 1 Resource conversion and validation;
- later Chapters 2-12 production dialogue/content;
- Phase 29B exact formations;
- Phase 30 numerical/progression rebase;
- Phase 31 integrated pacing validation;
- remaining Character-Life/Hub content and final visual/audio/UI/device/release hardening.
