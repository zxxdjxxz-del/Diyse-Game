# Chapter 0 Step 7C Production Status

Authority checkpoint: **v1.40 / Audit55 change-control target**.

Controlling change-control record: `docs/authority/CHAPTER_0_REBUILD_V1_40_CHANGE_CONTROL_2026-08-09.md`.

## Canon scene set

- [x] S001 — Opening — rebuilt and user-approved August 9, 2026
- [x] S002 — Wreck Field exploration — rebuilt and user-approved August 9, 2026
- [x] S003 — Evacuation Relay decision — rebuilt and user-approved August 9, 2026
- [x] S004 — Field Triage Camp revelation — rebuilt and user-approved August 9, 2026
- [x] S005 — Confrontation — rebuilt around the actual discrete-round combat system and user-approved August 9, 2026
- [x] S006 — Aftermath — rebuilt and user-approved August 9, 2026
- [x] C01 — The Fire Is Too Close — retained optional Character-Life canon
- [x] C02 — Food After Triage — retained optional Character-Life canon

## v1.40 canon result

- [x] Whole-Chapter 0 continuity / voice / runtime re-audit: GREEN.
- [x] Target mandatory runtime remains approximately 55 minutes, with a working 52-57 minute implementation range.
- [x] Chapter 0 uses approximately seven authored/tutorial encounters and no normal random-encounter rhythm.
- [x] Ilyra is not clearly shown or heard until S004; S004 owns her first identifiable appearance and spoken line.
- [x] Pursuit refusal remains S003 and is based on observable operational risk, not prophecy or omniscience.
- [x] The incomplete green-and-gold damaged-Card response remains S004.
- [x] Riftmaw remains S005 and uses one continuous HP bar with Restrained -> Unbound and optional low-HP Cornered behavior.
- [x] Permanent Ilyra recruitment and Brackenwall handoff remain S006.
- [x] S006 contains one explicit survivor recovery, one confirmed death, and at least three unresolved southbound tracks.
- [x] C01/C02 remain optional and nonessential to mandatory-story comprehension.
- [x] No First Champion identification, First Mercy response, player dialogue choices, or romance-route architecture is introduced.
- [x] Chapter 1 S007-S011 canon wording remains unchanged.

## Combat compatibility lock

All Chapter 0 battles use the accepted Diyse round architecture:

1. enemies lock one legal action from the legitimate beginning-of-round state;
2. enemy AI does not inspect unconfirmed player commands;
3. the player chooses one action for every conscious active party member before confirmation;
4. Items resolve first;
5. Defend resolves second;
6. remaining actions resolve by current effective Speed;
7. Speed changes order only and never grants extra ordinary actions.

No Chapter 0 encounter may add overwatch, interrupts, real-time reaction commands, hidden bonus turns, Speed-based extra actions, or mid-resolution retarget cheating.

## Superseded implementation checkpoint

The previous Chapter 0 merge `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5` and its successful Godot/Android validation remain historical evidence that the production dialogue pipeline works.

However, after the v1.40 approval, the old mandatory Resources `S001.tres` through `S006.tres` are **superseded implementation pending replacement**. Their previous PASS does not validate the new canon text or rebuilt encounter integration.

C01 and C02 are retained and are not superseded by this change control.

## Runtime replacement gate

- [ ] Serialize exact approved rebuilt S001-S006 production wording/cues into stable-ID Resources.
- [ ] Update scene validators for new beat counts and protected boundaries.
- [ ] Update Chapter 0 cross-scene continuity validation.
- [ ] Update encounter handoff/integration data for the seven-battle learning progression.
- [ ] Run scene-specific validators.
- [ ] Run full Godot regression on the exact replacement head.
- [ ] Run Android debug/export proof on the same head.
- [ ] Record the v1.40 implementation PASS and replace the superseded old Chapter 0 runtime checkpoint.

## Current result

**Chapter 0 rebuild is COMPLETE / USER-APPROVED / ACTIVE CANON.**  
**Chapter 0 v1.40 runtime Resource replacement and revalidation are PENDING.**

Do not describe the old S001-S006 Resources as current canon. Do not rewrite Chapter 1 S007-S011 while performing the Chapter 0 replacement.