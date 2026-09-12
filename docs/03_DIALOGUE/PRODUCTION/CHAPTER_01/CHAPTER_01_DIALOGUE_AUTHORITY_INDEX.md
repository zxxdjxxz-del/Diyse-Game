# Chapter 1 — Dialogue Authority Index

**Chapter:** 1  
**Status:** COMPLETE CURRENT WORKING PRODUCTION — NATURAL-TURN + SPOKEN-DIALOGUE/NARRATION AUDITS COMPLETE; COMBINED READ-THROUGH REQUIRES RESYNCHRONIZATION  
**Combined read-through:** `CHAPTER_01_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` — stale where atomic sources have changed  
**Character-Life numbering authority:** `../CHARACTER_LIFE_NUMBERING_LOCK.md`  
**Rhythm authority:** `../../AGENT_SYSTEM/NATURAL_TURN_LENGTH_AND_FLOOR_HOLDING_LOCK.md`  
**Spoken-dialogue authority:** `../../AGENT_SYSTEM/SPOKEN_DIALOGUE_VS_NARRATION_LOCK.md`

## Authority rule

Chapter 1 keeps both forms deliberately:

1. the standalone scene files are the atomic edit authorities for exact scene wording;
2. `CHAPTER_01_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` is a combined read-through only when its embedded source SHA matches the current atomic source.

The combined manuscript also embeds pre-normalization Character-Life source keys `C03/C04/C05`; those are legacy source keys, not canonical IDs. Canonical numbering is controlled by `../CHARACTER_LIFE_NUMBERING_LOCK.md`.

## Mainline dialogue authority

1. `BEAT_01_BRACKENWALL_PROTOCOL_DRAFT_A.md` — spoken/narration audit current
2. `BEAT_02_BRIAR_PASSAGE_FIRST_TRAVERSAL_DRAFT_A.md`
3. `BEAT_03_GREENHOLLOW_TORREN_DRAFT_A.md` — spoken/narration audit current
4. `BEAT_04_HOLLOW_WATCH_APPROACH_DRAFT_A.md`
5. `BEAT_05_OCCUPIED_HOLLOW_WATCH_FORT_DRAFT_A.md` — spoken/narration audit current
6. `BEAT_06_BLACK_HOST_EXCAVATION_LOWER_ACCESS_DRAFT_A.md` — spoken/narration audit current
7. `BEAT_07_LOWER_JUNCTION_SIX_CHANNELS_DRAFT_A.md` — spoken/narration audit current
8. `BEAT_08_FORCED_INNER_SECTION_DRAFT_A.md`
9. `BEAT_09_HOLLOW_WATCH_CASTELLAN_DRAFT_A.md`
10. `BEAT_10_POST_CASTELLAN_MURAL_DRAFT_A.md` — spoken/narration audit current
11. `BEAT_11_HOLLOW_WATCH_RESOLUTION_TORREN_RECRUITMENT_DRAFT_A.md` — spoken/narration audit current
12. `BEAT_12_SOUTHERN_BRIAR_PASSAGE_DRAFT_A.md`
13. `BEAT_13_BRIARHIDE_STALKER_DRAFT_A.md`
14. `BEAT_14_THE_JUNCTION_HIDDEN_MONUMENT_DRAFT_A.md`
15. `BEAT_15_JUNCTION_CAMP_CLEANUP_DRAFT_A.md`

## Character-Life dialogue authority

Available independently during the Beat-15 Junction cleanup window:

- **C02 — Torren's Version of Dinner** — legacy source key `C03_TORRENS_VERSION_OF_DINNER_REHEARSAL_FIRST_DRAFT_C.md`
- **C03 — What the Map Says** — legacy source key `C04_WHAT_THE_MAP_SAYS_REHEARSAL_FIRST_DRAFT_A.md`
- **C04 — Not Professionally** — legacy source key `C05_NOT_PROFESSIONALLY_REHEARSAL_FIRST_DRAFT_D.md`

Protected exact **C03** anchor remains:
> **CYANIS:** Old slut?  
> **TORREN:** Bitch.

The later callback remains:
> **TORREN:** Bitch.  
> **CYANIS:** Old slut.

## Natural-turn audit — COMPLETE

Material rhythm corrections were made previously to Beats 1, 3, 7, 10, 11, 14 and canonical Character-Life C02, C03, C04.

Beats 2, 4–6, 8–9, 12–13, and 15 were intentionally preserved as predominantly terse where guided movement, hostile exploration, boss timing, or transition function earned it.

## Spoken-dialogue / narration audit — COMPLETE

Material revisions:
- **Beat 1** — Maevra receives the failed Card-transfer event as a compressed consequence + medical boundary rather than having the just-seen transfer scene replayed in full.
- **Beat 3** — Torren receives only travel-relevant Card information; Cyanis accepts the Hollow Watch problem without restating Torren's motivation and evidence back to him.
- **Beat 5** — Hollow Watch records and the breach no longer make multiple characters repeat that the Host occupation is feeding the excavation after the environment has already established it.
- **Beat 6** — sustained forcing work, age layering, and inward persistence remain primarily environmental; dialogue adds only distinct judgments and danger.
- **Beat 7** — the relief visually shows civilians, litters, carts, animals, and six channels; characters discuss the implication rather than reading the visual checklist aloud.
- **Beat 10** — the mural remains visual-first; repeated lower-junction inventory and repeated evacuation imagery were removed while geography recognition, scale, the Junction, and the modern Crest remain genuine new interpretation.
- **Beat 11** — Maevra no longer recites the Hollow Watch chapter back to the people who just lived it; she gives the reporting task and flags the mural.

Audited and intentionally preserved:
- Beats 2, 4, 8, 9, 12–15 and canonical C02/C03/C04.

The current Chapter-1 Face-list wording conflict in Beat 14 is not silently corrected by this dialogue audit; exact dialogue remains source-controlled until a separate canon-correction pass is explicitly requested.

## Current synchronization state

Atomic files revised after the prior combined-manuscript assembly include at least:
- Beat 1 — `f054e310ed1ce499d0fbf0d101714ffa7d77eaf7`
- Beat 3 — `457b89437bb73bbda890320a78a5001666675a2f`
- Beat 5 — `a52e538d132ca9e1bcc53d3d2daf1c2cd7a2d060`
- Beat 6 — `99c142d76c914759fa7e9856637401ef826eb065`
- Beat 7 — `7fd571c4006f24b9a0d04edeb4983865f4be2dc4`
- Beat 10 — `b474ce616e8d9a617dd1fb84e8c227a0e82428a7`
- Beat 11 — `28bab6e2afa2778fe9df52981660a949682051b3`
- Beat 15 already had a later metadata/numbering SHA than the prior assembly.

Therefore the combined manuscript is not current exact wording for every embedded scene and must not override the standalone atomic files until resynchronized.

## Conflict order

If Chapter-1 dialogue sources disagree:
1. current Chapter-1 story authority and later explicit user corrections;
2. `../CHARACTER_LIFE_NUMBERING_LOCK.md` for Character-Life IDs;
3. exact standalone current production scene file for wording;
4. current workflow locks, including `SPOKEN_DIALOGUE_VS_NARRATION_LOCK.md`, for production interpretation;
5. combined manuscript only when its recorded source SHA matches the standalone file;
6. this authority index for order/status;
7. historical cumulative transcript or removed material only as provenance.

> **Chapter 1 has passed the natural-turn and spoken-dialogue / narration audits. Atomic dialogue is current; the combined manuscript requires resynchronization.**
