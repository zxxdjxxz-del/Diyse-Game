# Diyse-Game

Clean Godot production repository for **Diyse**, a 2.5D, party-based, command-driven turn-based JRPG targeting Android.

This repository is the active implementation line. The older `zxxdjxxz-del/Diyse` repository is historical prototype reference only and is not a code source unless an explicit task authorizes a named reuse.

## Current authority and phase

- Controlling written authority: **Diyse v1.40 Chapter 0 Rebuild Change-Control Overlay**, inheriting all compatible v1.39 canon.
- Immediate predecessor/root baseline: **Clean Active Master Canon v1.39 — Chapter 1 Production Dialogue Canonization and Step 7C Second-Chapter Completion Revision**.
- Technical baseline: **Active Technical Annex v1.39** plus the v1.40 Chapter 0 implementation/change-control overlay.
- Chapter 0 change control: `docs/authority/CHAPTER_0_REBUILD_V1_40_CHANGE_CONTROL_2026-08-09.md`.
- Recovery checkpoint target: **v1.40 / Audit55**.

**Step 7B.5 is COMPLETE and PASSED on a real Android device.** The clean Godot architecture has proven 2.5D exploration, authored portrait dialogue, Diyse round combat, unlimited data-driven Standard Cards, direct-control Prime replacement, deterministic hostile retargeting, and versioned save/load persistence across app close/relaunch.

**Step 7B.6 is COMPLETE and PASSED.** Production dialogue has a stable-ID Resource contract, portrait-registry indirection, schema validation, a generic Resource-to-DialogueRunner adapter, and a Step 7C authoring template. The accepted 7B.6 implementation merge is `96c6bdc77f39c988f2185634b4e51546f2a0d76b`.

**Step 7C is ACTIVE. The rebuilt Chapter 0 S001-S006 is COMPLETE / USER-APPROVED / ACTIVE CANON, but its runtime Resource replacement and Godot/Android revalidation are PENDING.**

The previous mandatory Chapter 0 Resource merge `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5` is now historical pipeline evidence only for S001-S006. Those mandatory Resources are superseded content until replaced by exact v1.40 serialization. C01 and C02 remain current optional Character-Life scenes.

**Chapter 1 S007-S011 canon prose remains preserved exactly under v1.39.** Its separate runtime Resource-conversion/validation gate remains pending.

## Baseline rules

- Engine line: Godot 4.7.x stable; accepted proof target Godot 4.7.1.
- Language: GDScript.
- Platform target: Android, landscape.
- Presentation: 2.5D — 3D environments/depth/lighting/traversal with stylized 2D/2.5D character presentation and illustrated dialogue portraits where appropriate.
- Dialogue: fully authored; no player dialogue choices.
- Production dialogue content: stable-ID `DiyseDialogueSceneDefinition` Resources with `DiyseDialoguePortraitRegistry` asset indirection.
- Combat: traditional discrete round-based command combat.
- At beginning of round, enemies lock legal actions before unconfirmed player commands exist.
- Player selects one action for every conscious active party member before confirmation.
- Resolution priority: Items first, Defend second, all remaining actions by current effective Speed.
- Speed controls order only and never grants extra ordinary actions.
- No overwatch, interrupts, reaction commands, real-time interception, threshold bonus turns, or enemy retargeting after reading player commands.
- Maximum active party: four.
- Permanent commands: Attack / Ability / Card / Item / Defend.
- MP is the universal ordinary Ability resource; no character-specific combat gauges.
- Current Cards: 24 Standard + 12 Prime.
- Standard Cards are unlimited-use.
- If a queued player hostile action's original enemy target is defeated before resolution, it retargets to the next living enemy in encounter-slot order, wrapping when necessary, unless an authored effect explicitly overrides targeting.
- Content architecture should be data-driven wherever practical.
- Do not invent mechanics or silently change canon to make implementation easier.

## Chapter 0 v1.40 implementation target

Approximately 55 mandatory minutes, working implementation range approximately 52-57 minutes, with about seven authored/tutorial encounters and no normal Chapter 0 random-encounter rhythm.

Encounter progression:

1. Raider — basic round grammar.
2. Raider + Crossbowman — differentiated threats.
3. Shieldbearer + Raider — target-value decisions.
4. Rift Hound + Raider — Speed/order pressure only.
5. Handler + Hound — complementary support actions.
6. Ruin Vanguard Pursuer — visible locked intent/objective planning.
7. Riftmaw + two Handlers — first major Cyanis + Ilyra whole-party planning encounter.

Riftmaw retains one continuous HP bar; Restrained -> Unbound is processed between completed rounds without a refill or bonus action; Cornered is low-HP future-round weighting, not a third full phase.

## Current replacement gate

Before rebuilt Chapter 0 can be called implementation-validated:

1. serialize exact approved S001-S006 wording/cues into stable Resources;
2. update the six scene validators and Chapter 0 continuity gate;
3. integrate the approved battle handoffs without changing the resolver contract;
4. run scene validation;
5. run the full Godot regression suite on the exact final head;
6. run the Android debug/export checkpoint on the same head;
7. record the new v1.40 implementation PASS.

## Proof-content warning

Passing Steps 7B.5 and 7B.6 validates architecture and accepted behavior, not temporary prototype content. Graybox geometry, placeholder sprites/portraits, proof dialogue, `PROOF_SCHEMA`, proof enemies, `Proof Strike`, flat proof damage, temporary rewards, proof flags/cues, debug UI, and superseded pre-v1.40 S001-S006 content are not current canon fixtures.

See `AGENTS.md`, `docs/ACTIVE_CANON.md`, `docs/IMPLEMENTATION_STATUS.md`, `docs/CHAPTER_00_STEP7C_STATUS.md`, `docs/authority/CHAPTER_0_REBUILD_V1_40_CHANGE_CONTROL_2026-08-09.md`, `docs/DIALOGUE_AUTHORING_SCHEMA.md`, `docs/STEP_7C_AUTHORING_TEMPLATE.md`, and the relevant subsystem rules before implementing production content.