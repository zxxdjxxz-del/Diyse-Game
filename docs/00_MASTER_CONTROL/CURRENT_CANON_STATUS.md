# Diyse — Current Canon Status

**Project-folder reorganization:** **COMPLETE**  
**Migration baseline:** v85 consolidated working tracker  
**Current authority model:** v2.20 / Audit135 plus all later explicit approved corrections promoted into the organized owning domains.

This file is a current cross-domain status summary only. Historical incremental version notes belong in `CHANGELOG.md` and `99_ARCHIVE`, not here.

## Repository / authority state
- active numbered domains `01` through `16` are migrated;
- `90_WORKING` is only for intentionally unresolved/reopened work;
- `99_ARCHIVE` is provenance/history only and never silently overrides active canon;
- current owner precedence is defined in `AUTHORITY_AND_CHANGE_CONTROL.md`;
- implementation work must also follow root `AGENTS.md` and `13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_AUTHORITY_PRECEDENCE.md`.

## Current project locks
- 6 permanent playable characters;
- active battle party maximum **4** in the general game rules;
- **Chapter 1 exception: combat-party cap = 3**. Chapter 1 opens with Cyanis + Ilyra; Torren becomes the third combatant for Hollow Watch and remains the third thereafter. Maevra is never a Chapter-1 battle-party body;
- Chapter 0 + Chapters **1–13**;
- true PONR = **Last Shelter → Reactor Galleries**;
- Player Level cap **70**;
- campaign ending around **Lv62**;
- HD-2D anime presentation target;
- final whole-project music remains OPEN.

## Current combat locks
- fixed discrete round-based combat; no ATB and no whole-party action queue;
- each character chooses/resolves an action when their Speed-derived turn arrives;
- commands exactly: **Attack / Ability / Card / Item / Defend**;
- four standard elements: **Fire / Ice / Lightning / Earth**;
- Ruin is a special affinity/school, not a fifth standard element;
- five universal harmful statuses;
- Spirit is the magic-resistance defensive stat;
- temporary Attack/Magic/Defense/Spirit/Speed changes use percentages and the current ±40% per-axis caps;
- equipment Max HP / Max MP bonuses use current flat `+N` construction rules.

## Current Card / Face locks
Exactly:
- **24 Standard Cards**;
- **12 Primes**;
- **36 total Card identities**.

Current Six Faces exactly:
> **Might / Elements / Grace / Perception / Memory / Ruin**

Retired Face labels:
> Resource / Acuity / Change

Perception:
> Accuracy-oriented effects under the existing Base Hit/application-reliability system, Evasion, Critical Hits, and Fields; reading position, timing, openings, and space.

Memory:
> recall, repetition, preservation, and reuse of prior actions/states; what has happened remaining available to influence the present.

Detailed Face owner:
> `../07_CARDS/SIX_FACES.md`

## Current Prime locks
- progression: **Recovered → Awakened** only;
- Prime invocation and Prime commands cost **0 MP**;
- each Prime identity has **one use until restored by valid rest or an explicitly authored restoration effect**;
- Prime spent/Ready state **persists across battle end** until valid restoration;
- same-bar state changes do **not** refresh Prime availability;
- genuine fresh-HP boss forms/bodies also do **not** refresh Prime availability;
- a form transition never creates a new automatic Prime-use allowance;
- after any Prime manifestation ends, **3 full normal party rounds** must pass before another Ready Prime can be invoked;
- Awakened Prime round sequencing is owned by `../05_BATTLE_SYSTEM/PRIME_ROUND_SEQUENCING.md`;
- valid rest and explicit authored restoration effects such as Emergency Kit restore eligible spent Prime identities to Ready without bypassing an active spacing rule.

## Current class / progression locks
Permanent six:
- Cyanis — Crest Knight / Crest Arcanist;
- Ilyra — Blue Warden / Vowblade;
- Torren — War Archer / Routeweaver;
- Nimera — Cardweaver / Proofhunter;
- Vaelira — Green Arcanist / Axiomblade;
- Seyrik — Ruin Vanguard / Ruin Warden.

Torren/Nimera Face alignment:
- War Archer — **Perception**;
- Routeweaver — **Memory**;
- Cardweaver — **Memory**;
- Proofhunter — **Perception**.

Class progression:
- Base Class cap **CL13**;
- Subclass cap **CL13**;
- CL13 = **6,000 cumulative CEXP**;
- Mastery Point currency removed;
- Masteries unlock automatically by Class Level;
- normal mandatory-route full Base + Subclass completion occurs around **Player Lv55–60**.

## Economy status
Currency terminology remains:
> **G**

Retired currency name:
> **Auren**

The detailed economy is **scheduled for a later rebuild/recalibration**.

Therefore:
- existing prices, chapter-income totals, liquidity totals, Hunt G, and completionist cash totals are **provisional planning data**, not hard current locks;
- cleanup/consolidation work must not spend time rebalancing or propagating G totals unless the economy rebuild explicitly begins;
- structural non-economy canon must not be inferred from old payout tables;
- ordinary enemies still do not gain a random junk/material-drop economy merely because old reward files exist.

Detailed economy working material remains under:
> `../12_ECONOMY_AND_REWARDS/`

## Major Hunt timing
Major Hunt cadence remains individually owned in the Hunt/story files and may contain locked milestones even though Chapters 5–13 are still development-in-progress.

Do not use this master summary to invent or freeze later-chapter placement details that have not been separately approved.

Prime rule for every Major Hunt:
> **fresh forms do not refresh spent Prime identities.**

## Chapter-authority maturity boundary
- Chapters **0–3** have the strongest current completed/consolidated authority.
- Chapter **4** story structure is current, but its ordinary enemy/formation layer is explicitly **REWORK PENDING**.
- Chapters **5–13** remain **development-in-progress** and still require additional story/enemy/balance/dialogue work.
- Individual facts inside Chapters 5–13 may still be explicitly locked by their own newer authority, but the chapter packages as a whole must not be treated as finished/certified merely because inherited files contain PASS / COMPLETE / VALIDATED language.
- When later-chapter files conflict, preserve the newest explicit lock and mark the unresolved remainder open rather than synthesizing new canon during cleanup.

## Current enemy / encounter status
Static enemy/encounter owner files and prior true-battle/sensitivity reports remain available in their owning domains.

Important routing correction:
- the former mandatory-route enemy difficulty recalibration stream is **not an active work item in the master queue anymore**;
- the former ×1.20 global direct-damage test floor is **not a standing instruction for new work**;
- First Command Warden is **not** automatically the next balance task;
- the former boss-local retune list is **not** the current work sequence.

Historical v103–v105 reports remain valid as analytical evidence of the tests they actually performed, but they do not determine what should be worked on next.

Future balance work follows the separately established current handling process or a new explicit instruction. Do not revive the retired queue workflow from historical reports alone.

Detailed balance material remains under:
> `../16_BALANCE_AND_TESTING/`

## Current implementation debt
Proof/runtime material may still contain intentionally stale fixtures. Known examples include:
- proof `first_champion` bearer lock;
- proof `gold` variable/data semantics and old numeric economy fixtures; player-facing terminology must use **G**, while detailed values await the planned economy rebuild;
- proof item/equipment records;
- old queue/Confirm Round battle architecture;
- stale technical IDs that require save-safe migration.

Current canon beats proof runtime. See:
> `../13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md`

## Current open areas
- story-owned special-enemy placement/timing dependencies explicitly left unresolved;
- Chapter 4 ordinary-enemy / formation rework;
- Chapters **5–13 broader story/enemy/balance/dialogue development**, not only missing exact dialogue;
- production implementation reconciliation;
- final production UI/readability validation;
- final audio/music completion and mix validation;
- visual production/style certification;
- whole-game/device/performance QA;
- explicitly bounded story/lore details still marked open in their owning domains.

The former mandatory-route enemy-difficulty recalibration sequence is not listed here as an open master-queue item because it is being handled through a different process.

The detailed G economy remains **rebuild/recalibration pending**. Existing prices, payouts, liquidity totals, Hunt cash, and completionist totals are provisional planning/history data rather than hard current locks.
