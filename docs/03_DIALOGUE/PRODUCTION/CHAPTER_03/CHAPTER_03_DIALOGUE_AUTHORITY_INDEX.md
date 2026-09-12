# Chapter 3 — Dialogue Authority Index

**Chapter:** 3  
**Status:** COMPLETE CURRENT WORKING DIALOGUE PRODUCTION — MAINLINE 1–15 + C06/C07; SPOKEN-DIALOGUE / NARRATION AUDIT CURRENT; COMBINED READ-THROUGH REQUIRES RESYNCHRONIZATION  
**Single-file read-through:** `CHAPTER_03_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` — currently stale against revised atomic sources listed below  
**Primary story authority:** `../../../02_STORY/CHAPTERS/CHAPTER_03.md`  
**Dialogue workflow authority:** `../../AGENT_SYSTEM/CHAPTER_0_1_PIPELINE_CONTINUITY_LOCK.md`  
**Spoken-vs-narration authority:** `../../AGENT_SYSTEM/SPOKEN_DIALOGUE_VS_NARRATION_LOCK.md`  
**Guardrail workflow authority:** `../../AGENT_SYSTEM/STORY_BEAT_AS_GUARDRAIL_LOCK.md`  
**Character-Life numbering authority:** `../CHARACTER_LIFE_NUMBERING_LOCK.md`  
**Rhythm authority:** `../../AGENT_SYSTEM/NATURAL_TURN_LENGTH_AND_FLOOR_HOLDING_LOCK.md`  
**Closing audit:** `CHAPTER_03_DIALOGUE_CLOSING_INTEGRATION_AUDIT_2026-09-12.md`

## Purpose

This file locates the current Chapter-3 dialogue authorities and defines the relationship between the atomic scene files and the complete single-file read-through.

## Authority rule

Chapter 3 deliberately keeps both forms:

1. the **standalone scene files** listed below are the atomic edit authorities for exact scene wording and scene-level implementation detail;
2. `CHAPTER_03_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` is the combined single-file read-through when its embedded source SHAs match the current atomic files.

The combined manuscript records each embedded source filename and Git blob SHA. If a standalone source changes, the manuscript must be resynchronized and its corresponding SHA marker updated. A SHA mismatch means the standalone source wins until synchronization is repaired.

The 2026-09-12 spoken-dialogue / narration work materially revised Beats **2, 3, 4, 6, 9, 10, 12, 13, and 15** after the last combined-manuscript synchronization. Therefore the combined manuscript is currently a stale read-through copy for those nine scenes. All other embedded scenes remain unchanged by these passes.

Character-Life numbering is global and chronological. Chapter 3's active Character-Life scenes are canonically **C06** and **C07**. Their current `H01/H03` filenames are legacy source keys only and do not control the live IDs.

## Mainline dialogue authority

1. `BEAT_01_CAELORA_GATE_ARRIVAL_DRAFT_A.md`
2. `BEAT_02_ROYAL_AUDIENCE_CH2_REPORT_DRAFT_A.md` — royal-voice / new-listener compression current
3. `BEAT_03_IMPOSSIBLE_ORDERS_DRAFT_A.md` — royal-voice / duplicate-recap removal current
4. `BEAT_04_SEAL_NOT_USED_DRAFT_A.md` — royal-voice / narration-reduction current
5. `BEAT_05_OLD_CITY_ACCESS_ARCHIVE_DESCENT_DRAFT_A.md`
6. `BEAT_06_SCHOLAR_IN_REDACTED_STACKS_DRAFT_A.md` — new-listener recap compression current
7. `BEAT_07_ANCIENT_BARRIER_FIRST_COOPERATION_DRAFT_A.md`
8. `BEAT_08_ARCHIVE_SCRIBE_ENGINE_NIMERA_JOINS_DRAFT_A.md`
9. `BEAT_09_BURIED_COLLECTIONS_DORMANT_CARD_RESEARCH_DRAFT_A.md` — narration-reduction current
10. `BEAT_10_RECENT_READER_HALL_OF_SEALS_DRAFT_A.md` — narration-reduction current
11. `BEAT_11_FIRST_COMMAND_WARDEN_DRAFT_A.md`
12. `BEAT_12_SEALWRIGHT_CHAMBER_COPYING_ATTEMPTS_DRAFT_A.md` — narration-reduction current
13. `BEAT_13_MIRENAS_CONCERN_CRESTHAVEN_LEAD_DRAFT_A.md` — royal-voice / debrief compression current
14. `BEAT_14_REST_IN_CAELORA_MORNING_DEPARTURE_DRAFT_A.md`
15. `BEAT_15_CRESTHAVEN_HEADQUARTERS_CLEANUP_WINDOW_DRAFT_A.md` — narration-reduction current

## Spoken-dialogue / narration audit — 2026-09-12

The Chapter-3 pass is the first full production application of `SPOKEN_DIALOGUE_VS_NARRATION_LOCK.md`.

The governing rule is:

> **The environment shows. Evidence owners interpret. Authority figures decide. Characters react. Nobody recites the scene back to the player.**

Current interpretation:
- **Lysara converts information into judgment, boundaries, questions, or orders.** She does not repeat evidence competent people in the room have already established.
- **Mirena converts evidence into investigation choices and trust boundaries.** She does not summarize the clue stack merely so the audience hears it again.
- **New-listener briefings are compressed.** A character who genuinely needs earlier information receives consequence-first facts and pulls any extra detail through their own questions; the script does not replay the previous scene chronologically.
- **The environment carries visible progression.** If the player has just seen a route, copying progression, or evidence cluster, dialogue adds interpretation, uncertainty, decision, or character response rather than a spoken checklist.
- **Scholars and technical owners may still explain evidence** when interpretation itself is their job; narration reduction is not a universal brevity rule. Nimera keeps evidence-boundary lines when only she can responsibly make the distinction.

Representative current Lysara register includes:
- `Commander. Start with the people.`
- `Harth. Certain?`
- `Then not today.`
- `Say it plainly.`
- `No accusations without proof.`
- `Can you prove unrecorded access?`
- `Then neither is fact. Move on.`
- `Copies only.`

Representative current trims:
- Beat 2 gives the royal room the Card-separation result once, in compressed form.
- Beat 3 no longer repeats the same Card-separation test to the same room; Ilyra states only the live consequence: moving it is a known risk.
- Beat 6 compresses the separation history for Nimera as a genuine new listener and lets her ask for the details she actually needs.
- Beat 9 reduces the recent-reader discovery to `Same run of page markers through both.`, `Same subjects we're chasing.`, and `Same trail.` rather than restating the whole clue cluster.
- Beat 10 lets the keeper ledger establish the seal finding and reduces the recent-reader continuation to `Same marker pattern.` / `Same trail. Down here before us.`
- Beat 12 leaves the copying progression primarily in the environment; the spoken conclusion is only `And more specific.` before the question of whether the practitioner and recent reader were the same person.
- Beat 13 compresses both the seal-practice debrief and Warden/Card sequence; Mirena asks only for decision-relevant facts instead of replaying what the player just saw.
- Beat 15 reduces Mirena's optional-route handoff to the operational facts the party needs: the passage is open, marked, and the crew stopped at the threshold.

This is the target for future DIYSE dialogue unless explicitly revised: character-owned, evidence-aware, and unwilling to repeat information simply to make the plot legible.

## Character-Life dialogue authority

Both scenes are independently available during the Beat-15 Cresthaven cleanup window before the explicit **Begin Chapter 4** choice. In the combined manuscript they appear after the intact Beat-1→15 mainline as a cleanup appendix.

### C06 — Nimera Takes Over a Table

Current legacy atomic dialogue source:
- `H01_NIMERA_TAKES_OVER_A_TABLE_DRAFT_A.md`

Current legacy authority spec:
- `H01_NIMERA_TAKES_OVER_A_TABLE_SPEC.json`

Protected exact opening anchors:
> **CYANIS:** I bet you use that cape to sneak up on the goats you fuck.  
> **TORREN:** You look like a walking dick in armor.

### C07 — Ilyra and Nimera

Current legacy atomic dialogue source:
- `H03_ILYRA_AND_NIMERA_DRAFT_A.md`

Current legacy authority spec:
- `H03_ILYRA_AND_NIMERA_SPEC.json`

Historical H02/H04 concepts remain retired. They do not reserve live Character-Life numbers.

## Protected mainline anchor

Beat 11 final Warden messages remain exact and ordered:

> **PREVIOUS ERROR**  
> **LAST SENTINEL CONFIRMED**

## Natural-turn / floor-holding audit result

Material rhythm revisions:
- Beat 2 — Royal Audience / Chapter-2 Report;
- Beat 3 — Impossible Orders;
- Beat 9 — Buried Collections / Dormant Card Research;
- Beat 10 — Recent Reader / Hall of Seals;
- Beat 12 — Sealwright Chamber / Copying Attempts;
- Beat 14 — Rest in Caelora / Morning Departure;
- Beat 15 — Cresthaven Headquarters / Cleanup Window.

Audited and intentionally preserved as predominantly terse/mixed because the scene earns it:
- Beat 1;
- Beats 5–8;
- Beat 11;
- C06;
- C07.

Beat 4 and Beat 13 also carry the later royal-voice / narration-reduction work described above.

Key rhythm interpretation:
- formal reports allow the report owner to finish a linked report unit before questioning interrupts;
- research findings remain with the character who owns the evidence/caveat;
- Beat 14's quiet evening contains natural multi-sentence floor holding instead of uniform one-line ping-pong;
- technical collaboration, danger, battle, and rapid comedy remain legitimately terse where appropriate;
- authority figures do not repeat established facts merely to make the plot legible;
- visible evidence progression should not be followed by a spoken recap unless a character is adding a genuinely new inference.

## Prior closing integration audit result

The earlier 2026-09-12 chapter-wide integration audit remains valid beneath the rhythm and spoken-vs-narration passes.

Key corrections from that pass remain in force:
- Beat 4 guardrail-first Agent-Brain rerun, now additionally royal-voice polished;
- Beat 6 and Beat 7 integration trims;
- Beat 11 Warden/Card timing preserved without claiming causation;
- Beat 12 no new map / northern-route display and no spoken four-step recap of the visible copying progression;
- Beat 13 selective debrief with Maevra kept out of co-debriefer/exposition duty, now additionally stripped of redundant clue recap;
- C07 avoids the retired injury/treatment premise and remains low-stakes Character-Life comedy.

## Current production state

- Beats 1–15 — current working dialogue complete.
- C06 and C07 — current cleanup Character-Life dialogue complete.
- standalone atomic files — current exact wording authority.
- combined single-file production read-through — requires resynchronization for Beats 2/3/4/6/9/10/12/13/15 after the spoken-vs-narration passes.
- spoiler-free Chapters 0–3 reader edition — regenerated separately with all current revised Chapter-3 dialogue and all Character-Life scenes labeled as Interludes.
- closing integration audit — complete.
- natural-turn / floor-holding rhythm audit — complete.
- spoken-dialogue / narration audit — complete for current Chapter-3 scenes.
- Nimera permanently joins in Beat 8; current permanent combat party thereafter is Cyanis + Ilyra + Torren + Nimera.
- Beat 11 exact Warden messages remain `PREVIOUS ERROR` → `LAST SENTINEL CONFIRMED`.
- Cyanis's Card becomes stable deep Ruby only after the Warden is fully inert; causation remains unresolved.
- Beat 15 establishes Cresthaven as operational headquarters and opens Chapter-3 cleanup.
- Regional Hunt #3 is unlocked there without a dialogue-heavy mini-story.
- Chapter 3 remains active until the player deliberately chooses to begin Chapter 4.

## Conflict order

If Chapter-3 dialogue sources disagree, use this order:
1. current `../../../02_STORY/CHAPTERS/CHAPTER_03.md` plus later explicit user corrections/current dedicated story locks;
2. `../CHARACTER_LIFE_NUMBERING_LOCK.md` for Character-Life IDs;
3. exact standalone current production scene file listed here for exact wording and scene-level implementation detail;
4. `CHAPTER_03_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` as the combined read-through copy **only when its recorded source SHA matches the current standalone file**;
5. this authority index for order/status and locating current sources;
6. `CHAPTER_03_DIALOGUE_CLOSING_INTEGRATION_AUDIT_2026-09-12.md` for prior closing-pass rationale;
7. historical/superseded files only as provenance.

> **Chapter-3 current working dialogue production: COMPLETE through Beats 1–15 + canonical C06/C07. Atomic sources and the spoiler-free reader edition are current; the combined production manuscript requires resynchronization for Beats 2/3/4/6/9/10/12/13/15 after the spoken-vs-narration passes.**
