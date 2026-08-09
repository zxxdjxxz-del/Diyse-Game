# Diyse — Current Implementation Status

**Authority checkpoint:** v1.36 / Audit48  
**Step 7B.5:** COMPLETE / PASS on real Android hardware  
**Step 7B.6:** COMPLETE / PASS — production dialogue authoring handoff locked  
**Step 7C:** ACTIVE  
**Current Step 7C milestone:** Chapter 0 COMPLETE / MERGED; next Chapter 1 S007–S011  
**Active repository:** `zxxdjxxz-del/Diyse-Game`  
**Accepted 7B.5 gameplay baseline:** `f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`  
**Accepted 7B.6 implementation merge:** `96c6bdc77f39c988f2185634b4e51546f2a0d76b`  
**Approved Chapter 0 production merge:** `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`

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
| 7B.6 | PASS | Stable-ID dialogue scene Resources, portrait registry, authoring template, schema validation and Resource-to-runner integration |
| Step 7C Chapter 0 | PASS / MERGED | S001–S006 + C01/C02 approved; scene validators, cross-scene continuity gate, full regression, rendered-field proof and Android APK export passed |

## Accepted production-dialogue checkpoint

Chapter 0 is complete in the live repository.

- Mandatory scenes: S001 Opening; S002 Wreck Field exploration; S003 Evacuation Relay decision; S004 Field Triage Camp revelation; S005 Confrontation; S006 Aftermath.
- Optional Character-Life scenes: C01 The Fire Is Too Close; C02 Food After Triage.
- Mandatory authored beat total: 260.
- Optional C01/C02 authored beat total: 101.
- Ilyra first enters in S004.
- Pursuit refusal remains S003; incomplete damaged-Card response remains S004; final confrontation remains S005; permanent Ilyra recruitment and Brackenwall route handoff remain S006.
- C01/C02 remain optional and nonessential to mandatory-story comprehension.
- No Prime identity reveal, player dialogue choice architecture, romance route, or gameplay-system redesign was introduced.

Final accepted Chapter 0 PR head: `87157f9dae359f0b72a6ec9f5a1956d2056671cb`. Final merge: `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`.

Final Chapter 0 validation:
- Godot Smoke Validation run `31296623423`: success.
- Android APK Proof run `31296623417`: success.
- Android artifact ID `9033158865`; artifact ZIP digest `sha256:ae726063592d9845a6b667a8188d28ab4e5ed69177205be35997e6ba104b92c3`.

Two pre-merge validator defects were corrected without changing production scene canon: unsupported typed-array constructor syntax and a substring guard that incorrectly matched `quest` inside `question`.

## Accepted implementation behaviors

### Exploration / 2.5D
The active Godot line supports real 3D fields/depth/lighting/collision with stylized 2D/2.5D character presentation and Android touch movement. Proof visuals remain replaceable fixtures.

### Dialogue
Production dialogue uses `DiyseDialogueSceneDefinition` Resources, stable semantic IDs, `DiyseDialoguePortraitRegistry` indirection, cue metadata separate from spoken text, generic Resource-backed runner integration, and schema rejection of choice/response/branch fields. Chapter 0 proves that interface across a complete production chapter.

### Combat
The accepted resolver uses discrete rounds, enemy action locking before player confirmation, Item priority, Defend priority, then Speed ordering with current tie rules. Four permanent characters are active at maximum. Queued hostile player actions automatically retarget from defeated enemies according to the accepted encounter-slot rule.

### Standard Cards
Standard Cards are data-driven and unlimited-use without charges, Essence, Card ranks or per-battle Standard-use counters.

### Prime Manifestations
Prime activation, pending state, party suspension, direct player control, Prime-only command selection, hostile targeting of the Prime, finite duration and party return are proven without replacing the ordinary round system.

### Persistence
Persistent state remains separate from scene nodes and serializes as versioned plain data under Godot `user://`. Representative state survives full Android app close/relaunch; invalid saves fail safely.

## Chapter-level production workflow

Chapter 0 established the default Step 7C production pattern:

1. one branch/PR per chapter or comparable substantial narrative block;
2. scene-by-scene user review and checkpointing;
3. scene-specific validation without a full Android export after every dialogue-only scene;
4. one whole-chapter continuity/repetition/voice/runtime pass;
5. full Godot + Android regression on the exact final chapter head;
6. merge only after the exact head is green;
7. one authority/archive checkpoint after chapter completion.

An engine/schema/platform change can justify earlier full gating.

## Non-canon technical fixtures

Graybox maps, placeholder sprites/portraits, disposable proof dialogue, `PROOF_SCHEMA`, Raider proof enemies/stats, `Proof Strike`, temporary flat damage/rewards, proof-specific flags/state and debug UI remain non-canon fixtures.

## Remaining production scope

The architecture and Chapter 0 PASS do not mean the game is content-complete. Normal production continues through Chapter 1 S007–S011 and later Chapters 2–12, remaining Character-Life/Hub scenes, final visual/audio/UI work, complete production content, broader Android performance/device QA, and release hardening.