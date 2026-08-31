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
- active battle party maximum **4**;
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
- each Prime identity has one use until a valid rest/restoration effect makes it Ready again;
- spent state persists across battle end;
- genuine fresh boss bodies **do not** restore spent Prime identities;
- same-bar state changes do not restore spent Primes;
- after an Awakened Prime ends, **2 full normal party rounds** must pass before another Ready Prime can be invoked;
- Awakened Prime round sequencing is owned by `../05_BATTLE_SYSTEM/PRIME_ROUND_SEQUENCING.md`;
- Emergency Kit is an explicit authored Prime-restoration effect and restores all acquired Prime identities to Ready without bypassing the separate spacing rule.

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

## Current Major Hunt timing
- #1 **Ashen Whitehorn** — after Chapter 6 — recommended **Lv33**;
- #2 **Crownless Siege Marshal → Crownless War Engine** — after Chapter 7 — encounter recommendation **Lv41**;
- #3 **Concordance Guardian** — after Chapter 9 — recommended **Lv54**;
- #4 **Worldscar Leviathan** — after Chapter 10 — recommended **Lv60**;
- #5 **Final Archive Arbiter** — after Chapter 11 — recommended **Lv65**;
- #6 **The Unfinished World** — after Final Archive Arbiter clear + Vaelkor defeat in Chapter 12 — recommended **Lv70**.

Only Major Hunt #2 has a genuine fresh second body, and that fresh War Engine does **not** restore spent Prime identities.

## Current enemy / encounter status
Static enemy design is closed across the numbered campaign:
- direct-damage Power audit complete;
- Chapter 0–13 broad enemy audit complete;
- mandatory-vs-completionist paper validation complete;
- Regional Hunts #1–#11 Power-complete;
- Major Hunts #1–#6 Power-complete;
- Character Quest combat-boss sheets complete where a boss exists;
- formation composition/weight authority complete;
- targetable support/component static sheets complete where current authority specifies them.

Current Face-themed enemy terminology includes **Memory Schema** and **Perception Node**. Enemy Face naming never grants player Card/Prime commands.

## Representative true-battle certification
Completed:
- Hollow Watch Castellan — **PASS / RETAIN v93**;
- Archive Leviathan — **PASS / RETAIN v97**;
- Regulation Crucible → The Seventh Reaction — **PASS / RETAIN v99**.

Regulation v99 retained:
- Form-I HP **2,400**;
- Form-II HP **2,900**;
- all current raw stats/Powers/chamber architecture.

Strict prepared mandatory Lv15 benchmark:
- no Prime: **100% wins / median 18**;
- one legal Recovered Last Sentinel use: **100% wins / median 14**.

Current next representative anchor:
> **Warden of the Nameless / Revision Arbiter — Chapter 7 — mandatory Lv30 / completionist Lv34**

The Revision Arbiter test must use current Awakened Prime sequencing and the current persistent-spend Prime model.

Detailed balance status:
- `../16_BALANCE_AND_TESTING/BALANCE_CLOSURE_STATUS.md`
- `../16_BALANCE_AND_TESTING/OPEN_BALANCE_ITEMS.md`

## Current implementation debt
Proof/runtime material may still contain intentionally stale fixtures. Known examples include:
- proof `first_champion` bearer lock;
- proof `gold` instead of Auren;
- proof item/equipment records;
- old queue/Confirm Round battle architecture;
- stale technical IDs that require save-safe migration.

Current canon beats proof runtime. See:
> `../13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md`

## Current open non-balance areas
- unresolved exact Auren payouts/reward packages where Economy keeps them open;
- Kessara service fee if any;
- final production UI/readability validation;
- final audio/music completion and mix validation;
- device/performance budgets;
- explicitly bounded story-placement/return-trigger questions still marked open in their owning domains.
