# Chapter 0 — Dialogue Authority Index

**Chapter:** 0 — Broken Convoy  
**Status:** CURRENT WORKING DIALOGUE AUTHORITY — MAINLINE + C01; NATURAL-TURN RHYTHM + SPOKEN-DIALOGUE/NARRATION AUDITS COMPLETE; COMBINED READ-THROUGH REQUIRES RESYNCHRONIZATION  
**Combined chapter read-through:** `CHAPTER_00_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` — currently stale for P03 and P07  
**Rhythm authority:** `../../AGENT_SYSTEM/NATURAL_TURN_LENGTH_AND_FLOOR_HOLDING_LOCK.md`  
**Spoken-dialogue authority:** `../../AGENT_SYSTEM/SPOKEN_DIALOGUE_VS_NARRATION_LOCK.md`

## Authority rule

The standalone P01–P07 and C01 rehearsal-first files in this folder are the exact scene-level production authorities.

`CHAPTER_00_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` remains the convenient assembled read-through, but its embedded P03 and P07 wording predates the 2026-09-12 spoken-dialogue / narration audit. Where it disagrees with those standalone files, the standalone file wins until the manuscript is regenerated.

Current sequence:
- P01 — Convoy / Opening Ambush
- P02 — Wreck Field
- P03 — Evacuation Relay Decision
- P04 — Field Triage / Ilyra / First Flare
- P05 — Concealed Ruin Vanguard
- P06 — Riftmaw + Convoy War-Sorcerer
- P07 — Aftermath / Survivor Recovery
- optional C01 — Six Minutes

## Natural-turn / floor-holding audit — COMPLETE

Audit result:
- P01–P02 intentionally preserve clipped crisis/rescue cadence.
- P03–P07 were previously adjusted where speakers yielded merely because a sentence ended.
- C01 received the largest quiet-scene rhythm correction.
- no story outcome, reveal boundary, Card state, party state, or chapter transition changed.

## Spoken-dialogue / narration audit — COMPLETE

Owning rule:
- `../../AGENT_SYSTEM/SPOKEN_DIALOGUE_VS_NARRATION_LOCK.md`

Material revisions:
- **P03** — Cyanis no longer re-explains the entire north-cut suspicion to the same officer who heard it in P02. The officer asks what changed; Cyanis answers with the new operational fact: five casualties still need carrying.
- **P07** — Ilyra states her decision to stay once; the reason is supplied only when Cyanis challenges the premise, rather than being given twice in immediate succession.

Audited and intentionally preserved:
- P01, P02, P04, P05, P06, and C01. Their short turns, field commands, medical checks, or low-stakes conversation are character-owned rather than authorial recap.

Core interpretation:
> **The environment shows. Evidence owners interpret. Authority figures decide. Characters react. Nobody recites the scene back to the player.**

## Current synchronization state

Current atomic SHAs changed after the last chapter-manuscript assembly:
- P03 — `bc7f2a8a8d9da72e2e7a6533c29b48e1fdde4689`
- P07 — `e0cacc87ebf00ef0d19748ef1c6d46c216e80fe7`

Therefore the combined Chapter-0 manuscript is not current exact wording for those two scenes until resynchronized.

## Conflict order

If Chapter-0 dialogue sources disagree:
1. current Chapter-0 story authority and later explicit user corrections;
2. current standalone rehearsal-first scene authority;
3. `../../AGENT_SYSTEM/SPOKEN_DIALOGUE_VS_NARRATION_LOCK.md` and other current workflow locks for production interpretation;
4. `CHAPTER_00_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` only where its scene wording still matches the current standalone authority;
5. older/historical dialogue only as provenance.

Do not use removed pre-rehearsal or historical transcript sets as current dialogue authority.

> **Chapter 0 has passed both the natural-turn / floor-holding audit and the spoken-dialogue / narration audit. Atomic sources are current; P03/P07 require combined-manuscript resynchronization.**
