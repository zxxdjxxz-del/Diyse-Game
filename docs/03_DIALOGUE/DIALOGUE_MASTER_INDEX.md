# Diyse — Dialogue Master Index

**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicit user corrections/current domain migrations.  
**Dialogue production root:** `docs/03_DIALOGUE/PRODUCTION/`

## Dialogue Engine hard rules

Current production dialogue uses the rehearsal-first Agent Brain pipeline:

> **scene/world state → independent Person Agent Brain rehearsals → Dialogue Editor → mature-adult speech/profanity audit → invisible Canon/Knowledge Checker → spoken-dialogue vs narration audit → economical HD-2D staging/implementation**

Owning pipeline lock:
- `AGENT_SYSTEM/CHAPTER_0_1_PIPELINE_CONTINUITY_LOCK.md`

Story-beat guardrail lock:
- `AGENT_SYSTEM/STORY_BEAT_AS_GUARDRAIL_LOCK.md`

Natural-turn / floor-holding lock:
- `AGENT_SYSTEM/NATURAL_TURN_LENGTH_AND_FLOOR_HOLDING_LOCK.md`

Mature-adult speech / profanity lock:
- `AGENT_SYSTEM/MATURE_ADULT_SPEECH_AND_PROFANITY_LOCK.md`

Spoken-dialogue vs narration lock:
- `AGENT_SYSTEM/SPOKEN_DIALOGUE_VS_NARRATION_LOCK.md`

Character-Life numbering lock:
- `PRODUCTION/CHARACTER_LIFE_NUMBERING_LOCK.md`

Hard rhythm rule:
> **Concision is not a one-sentence limit. A character yields the floor because the interaction changes, not because the script reached a period.**

Hard mature-adult speech rule:
> **DIYSE characters are mature adults. Do not sanitize them into polite JRPG dialogue, and do not make them uniformly profane. Character, relationship, rank/register, and state decide the language.**

Hard spoken-dialogue rule:
> **The environment shows. Evidence owners interpret. Authority figures decide. Characters react. Nobody recites the scene back to the player.**

A conversational turn may be a fragment, one sentence, several connected sentences, an interrupted thought, or silence. Dialogue-box pagination is a presentation unit and does not define the end of a speaker turn.

New-listener briefings must be compressed to what the listener actually needs; the listener should pull further detail through character-driven questions rather than causing the previous scene to be replayed for the player.

Retroactive rhythm audit tracker:
- `CHAPTER_0_3_NATURAL_TURN_RHYTHM_AUDIT_TRACKER.md`

**Retroactive Chapters 0–3 natural-turn rhythm audit status: COMPLETE.**  
**Retroactive Chapters 0–3 spoken-dialogue / narration audit status: COMPLETE.**  
**Mature-adult speech / profanity audit status: Chapter 0 CURRENT; Chapters 1–3 to be included in the active character/ensemble re-audit rather than treated as a mechanical profanity-insertion pass.**

### Person-Brain performance state

The newer Person-Brain performance standard is current across Chapter 0, Chapter 1, and all Chapter-3 atomic dialogue. Chapter 2's completed natural-turn / spoken-dialogue production is retained as current and was not reopened merely to rename the pass.

The Person-Brain standard means:
- topic owners may hold the floor through a complete thought;
- interruption must come from motive, urgency, expertise, impatience, humor, or relationship;
- speakers do not receive equal turns merely because they are present;
- individual rhythms, self-correction, profanity, uncertainty, and conversational habits survive the Dialogue Editor;
- current character authority controls dialogue assignment, not class/Face stereotypes.

Current mature-adult speech calibration:
- **Nimera:** high/frequent profanity; it is a major part of her natural speech and often lives inside technical reasoning, self-correction, arguments, and humor;
- **Torren:** casual and unselfconscious profanity, especially in veteran shorthand, irritation, affectionate insult, and increasingly relaxed conversation;
- **Ilyra:** moderate, dry, and sometimes unexpectedly sharp profanity; healer/Grace coding must never sanitize her;
- **Cyanis:** moderate profanity, freer with trust, fatigue, frustration, or sharp affectionate banter; command responsibility may control register without making him prudish;
- **Maevra:** moderate and register-sensitive; she may be cleaner in formal command, but rank does not sanitize her, especially with Cyanis/Ilyra whom she already knows very well or Torren where old familiarity is established.

This is qualitative, not a swear-count target. The audit question is whether the line sounds like that particular mature adult in that relationship/state.

Current Ilyra guardrail:
> **Grace is not a dialogue assignment.**

Ilyra is not automatically assigned the medical, safety, food/sleep, emotional-interpreter, relationship-reader, caretaker, or moral-referee line. Medical expertise owns a turn when the scene genuinely requires it; humor, curiosity, irritation, profanity, uncertainty, gossip, and ordinary opinion are equally valid reasons for her to speak.

Chapter 3 is now the first fully closed chapter where the **Nimera Person-Brain pass and the later Ilyra role-balance pass are both explicitly complete in sequence**. The Nimera work was preserved; Ilyra was then re-audited under her later character guardrail rather than leaving the earlier safety/caretaker assignments in place.

Walking-dialogue lock:
- `AGENT_SYSTEM/WALKING_DIALOGUE_LOCK.md`

Ordinary traversal does not receive walking dialogue unless someone is genuinely guiding the route.

---

# Canonical Character-Life Sequence — Current Through Chapter 3

> **C01 → C02 → C03 → C04 → C05 → C06 → C07, with no live gaps.**

- **C01 — Six Minutes** — Chapter 0
- **C02 — Torren's Version of Dinner** — Chapter 1
- **C03 — What the Map Says** — Chapter 1
- **C04 — Not Professionally** — Chapter 1
- **C05 — Still Burns** — Chapter 2
- **C06 — Nimera Takes Over a Table** — Chapter 3
- **C07 — Ilyra and Nimera** — Chapter 3

Retired/superseded development IDs do not reserve numbers. Some atomic filenames still carry legacy source prefixes until they and their synchronized manuscripts are regenerated together; `PRODUCTION/CHARACTER_LIFE_NUMBERING_LOCK.md` controls canonical live IDs.

---

# Canonical Chapter Dialogue Locations — Chapters 0–3

| Chapter | Current status | Chapter-level dialogue authority |
|---|---|---|
| Ch0 | **COMPLETE CURRENT WORKING PRODUCTION; PERSON-BRAIN PERFORMANCE + CYANIS CHARACTER AUDIT + ILYRA ROLE-BALANCE + MATURE-ADULT SPEECH/PROFANITY + NATURAL-TURN + SPOKEN-VS-NARRATION CURRENT** — P01–P07 + optional C01; atomic files current, combined read-through stale for revised scenes | `PRODUCTION/CHAPTER_00/CHAPTER_00_DIALOGUE_AUTHORITY_INDEX.md` |
| Ch1 | **COMPLETE CURRENT WORKING PRODUCTION; PERSON-BRAIN PERFORMANCE + NATURAL-TURN + SPOKEN-VS-NARRATION CURRENT; FINAL ENSEMBLE + MATURE-ADULT SPEECH RE-AUDIT STILL NEEDED UNDER NEWER CHARACTER RULES** — Beats 1–15 + C02/C03/C04; atomic files current, combined read-through stale where flagged | `PRODUCTION/CHAPTER_01/CHAPTER_01_DIALOGUE_AUTHORITY_INDEX.md` |
| Ch2 | **COMPLETE CURRENT WORKING PRODUCTION; NATURAL-TURN + SPOKEN-VS-NARRATION + TORREN SOCIAL-COMFORT CURRENT; FULL ENSEMBLE + ILYRA + MATURE-ADULT SPEECH RE-AUDIT STILL NEEDED** — Beats 1–16 + C05 | `PRODUCTION/CHAPTER_02/CHAPTER_02_DIALOGUE_AUTHORITY_INDEX.md` |
| Ch3 | **COMPLETE CURRENT WORKING PRODUCTION; PERSON-BRAIN PERFORMANCE + ILYRA ROLE-BALANCE COMPLETE ACROSS BEATS 1–15 + C07; C06 CURRENT/INTENTIONALLY ILYRA-FREE; CLOSING INTEGRATION + NATURAL-TURN + SPOKEN-VS-NARRATION AUDITS COMPLETE; TORREN SOCIAL-PROGRESSION + MATURE-ADULT SPEECH RE-AUDIT STILL NEEDED** — atomic files current, combined read-through stale | `PRODUCTION/CHAPTER_03/CHAPTER_03_DIALOGUE_AUTHORITY_INDEX.md` |

These four chapter folders are the correct live production locations. Where a combined manuscript's embedded SHA differs from the current atomic source, the atomic source is the exact wording authority.

---

# Chapter 0

Folder:
- `PRODUCTION/CHAPTER_00/`

Authority index:
- `CHAPTER_00_DIALOGUE_AUTHORITY_INDEX.md`

Current sequence:
> **P01 → P02 → P03 → P04 → P05 → P06 → P07 → optional C01 `Six Minutes` → explicit departure to Brackenwall**

Person-Brain performance: **CURRENT.**  
Cyanis character audit: **COMPLETE.**  
Ilyra role-balance: **CURRENT.**  
Mature-adult speech / profanity audit: **CURRENT.**  
Natural-turn audit: **COMPLETE.**  
Spoken-dialogue / narration audit: **COMPLETE.**

Chapter 0 still contains story-earned medical emphasis where Ilyra is literally running triage and observing the Card's unexplained physical effects, but P05 and C01 establish that she also owns tactical uncertainty, humor, profanity, first impressions, ordinary curiosity, and nonmedical social behavior.

The Cyanis-specific audit confirmed that he already reads as a mature adult rather than a sanitized protagonist: command clarity can stay clean when clarity matters, while ordinary humor, bluntness, and profanity remain available according to his state and relationship. No atomic rewrite was required solely to increase profanity.

Spoken-vs-narration material revisions:
- **P03** — the north-cut suspicion is not re-explained to the same officer; Cyanis answers what changed operationally.
- **P07** — Ilyra states the decision to stay once and supplies the reason only when Cyanis challenges it.

Combined read-through:
- `CHAPTER_00_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` — **stale against revised atomic dialogue.**

---

# Chapter 1

Folder:
- `PRODUCTION/CHAPTER_01/`

Authority index:
- `CHAPTER_01_DIALOGUE_AUTHORITY_INDEX.md`

Canonical Character-Life scenes:
- **C02 — Torren's Version of Dinner**;
- **C03 — What the Map Says**;
- **C04 — Not Professionally**.

Person-Brain performance: **CURRENT.**  
Natural-turn audit: **COMPLETE.**  
Spoken-dialogue / narration audit: **COMPLETE.**  
Mature-adult speech / profanity audit: **to be integrated into the pending final ensemble character-balance pass.**

Ilyra role-balance correction is current across the main pressure points. Her medical expertise remains available when genuinely needed, but she is no longer the default post-battle checker, food/sleep monitor, relationship reader, or human-consequence narrator.

The pending ensemble pass must also preserve current Maevra authority: she already knows Cyanis and Ilyra very well as separate people, while remaining their senior commander. Familiarity permits shorthand, teasing, bluntness, and natural profanity; it does not make them equal-rank best friends during operations.

Spoken-vs-narration material revisions:
- Beats **1, 3, 5, 6, 7, 10, 11, 14**.

Key result:
- new-listener Card briefings are consequence-first rather than replayed chronologically;
- Hollow Watch occupation/excavation staging carries information the environment can show;
- the six-channel relief and mural stay visual-first instead of being read aloud as checklists;
- the Hollow Watch resolution reports what Greenhollow needs, not the chapter back to the people who lived it;
- the hidden monument's cartographic surface is interpreted immediately instead of being announced to the player, and the Six Face exchange asks what the marks might mean rather than describing their visible placement first.

Protected **C03** anchor remains exact:
- Cyanis: `Old slut?`
- Torren: `Bitch.`

Known Beat-14 Face-list wording remains source-controlled and is not silently changed by this dialogue audit.

Combined read-through:
- `CHAPTER_01_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` — **requires resynchronization after atomic dialogue and prior numbering revisions.**

---

# Chapter 2

Folder:
- `PRODUCTION/CHAPTER_02/`

Authority index:
- `CHAPTER_02_DIALOGUE_AUTHORITY_INDEX.md`

Current state:
- all sixteen mainline beats have one standalone exact current dialogue authority;
- **C05 — Still Burns** is current cleanup Character-Life dialogue;
- Torren's Chapter-2 social-comfort correction is current.

Natural-turn audit: **COMPLETE.**  
Spoken-dialogue / narration audit: **COMPLETE.**  
Mature-adult speech / profanity audit: **to be integrated into the pending full four-character ensemble pass.**

Chapter 2's completed production remains current, but it still requires the dedicated ensemble character-balance pass for Cyanis, Ilyra, Torren, and Maevra under the newest character rules. That pass must include the mature-adult speech/profanity audit rather than treating it as a separate cosmetic rewrite.

Spoken-vs-narration material revisions:
- Beats **2, 5, 6, 10, 13, 14, 16**.

Key result:
- Dunmere's idle wagons communicate the visible road stoppage without Maevra verbally inventorying what the player can already see;
- Archive staging carries visible organization/forcing evidence while Ilyra and Torren supply only distinct interpretation;
- the western wall map is allowed to read visually before the cast begins genuine route analysis;
- prisoner testimony is not paraphrased three times after the witnesses establish the facts;
- Rhazek no longer narrates the player's dungeon progress or his visible withdrawal order back to the party;
- Dunmere's final debrief is consequence-first rather than a beat-by-beat Chapter-2 recap;
- the elder's thematic summary is reduced to the character-appropriate `Both matter.`

Core outcomes remain unchanged: current prisoners rescued, Rhazek loses the Old Bastion locally but survives a credible withdrawal, earlier transferred captives remain unresolved, Greenhollow ↔ Dunmere travel reopens, and Chapter 3 begins only through explicit player confirmation.

Combined read-through:
- `CHAPTER_02_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` — **requires resynchronization after atomic dialogue and prior numbering revisions.**

---

# Chapter 3

Folder:
- `PRODUCTION/CHAPTER_03/`

Authority index:
- `CHAPTER_03_DIALOGUE_AUTHORITY_INDEX.md`

Combined read-through:
- `CHAPTER_03_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` — **stale against the current atomic scenes.**

Prior closing integration audit:
- `CHAPTER_03_DIALOGUE_CLOSING_INTEGRATION_AUDIT_2026-09-12.md`

Current state:
- Beats 1–15 — **Person-Brain performance + Ilyra role-balance complete** in standalone atomic authority;
- **C06 — Nimera Takes Over a Table** — current and intentionally Ilyra-free;
- **C07 — Ilyra and Nimera** — Person-Brain current; Ilyra role-balance audited and retained;
- closing integration audit complete;
- natural-turn / floor-holding rhythm audit complete;
- spoken-dialogue / narration audit complete;
- Torren's newer social-progression rule and the new mature-adult speech/profanity lock still require a targeted Chapter-3 re-audit before the chapter is considered fully aligned with the newest character system.

Ilyra role-balance sequence:
- **Beats 1–5** were corrected after the newer Ilyra guardrail was established.
- **Beats 6–15** were then re-audited because their Nimera-focused Person-Brain rewrites predated that Ilyra correction.
- **Beats 6, 7, 8, 10, 11, 12, 14, and 15** received material dialogue changes.
- **Beats 9 and 13** already satisfied the newer Ilyra standard and were retained.
- **C07** already satisfied the newer Ilyra standard and was retained.

Key Ilyra result across Chapter 3:
- Cyanis owns his own direct Card experience and Card-custody choices;
- Torren owns physical route/load observations when he is the one who can actually see them;
- Crown authority owns Crown investigative boundaries;
- Nimera owns her own methodological / experiment constraints;
- Ilyra's medical expertise remains available where genuinely scene-earned, but she is no longer the default post-fight checker, food/sleep monitor, sealed-door monitor, Card-custody proxy, party parent, or automatic safety voice;
- Ilyra now contributes repeatedly through research questions, evidence wording, curiosity, dry humor, teasing, profanity-compatible adult social behavior, and ordinary preferences.

Current Torren/Nimera progression authority must also be respected in the upcoming re-audit: Chapter 3 is first contact only. Their eventual father/daughter-like bond is a later earned destination and must not be written backward into the chapter where they meet.

Spoken-vs-narration material revisions remain in force:
- Beats 2, 3, 4, 6, 9, 10, 12, 13, 15.

Protected **C06** exact anchors:
- Cyanis: `I bet you use that cape to sneak up on the goats you fuck.`
- Torren: `You look like a walking dick in armor.`

Beat 11 exact Warden messages remain:
- `PREVIOUS ERROR`
- `LAST SENTINEL CONFIRMED`

---

# Later Chapters

| Chapter | Dialogue status |
|---|---|
| Ch4 | pending current Dialogue Engine production under current restructured story authority **with Person-Brain performance, natural-turn/floor-holding, mature-adult speech/profanity, spoken-vs-narration, relationship progression, and current character dialogue-assignment rules active from the first rehearsal** |
| Ch5 | beat rewrite required before dialogue generation |
| Ch6 | macro/beat authority; dialogue pending |
| Ch7 | macro authority; dialogue pending |
| Ch8 | macro authority; dialogue pending |
| Ch9 | macro/beat authority; dialogue pending |
| Ch10 | detailed story architecture; dialogue pending |
| Ch11 | macro authority; dialogue pending |
| Ch12 | macro authority; dialogue pending |
| Ch13 | macro authority; dialogue pending |

All later chapter dialogue uses the locked rehearsal-first Agent Brain pipeline plus all later workflow corrections from the first production pass onward. **Do not repeat the Chapter-3 sequencing mistake:** current character-specific guardrails, relationship-progression rules, and mature-adult speech/profanity behavior must be applied during the same rehearsal/editor cycle as the Person-Brain performance pass, not retrofitted afterward.

---

# Source-cleanup rule

Current production dialogue belongs in:
> `docs/03_DIALOGUE/PRODUCTION/CHAPTER_##/`

Each chapter's authority index / assembly tells production where the exact current dialogue lives.

When a scene receives a targeted revision, update its standalone current production file first. Do not retain an unsynchronized duplicate transcript as competing live authority; either deliberately reassemble it or keep the chapter-level file as an explicit assembly/status map.

For Character-Life, use the canonical ID from `PRODUCTION/CHARACTER_LIFE_NUMBERING_LOCK.md`. Legacy file prefixes are implementation provenance only and must not create holes in the live numbering sequence.

Use Git history for superseded copies.
