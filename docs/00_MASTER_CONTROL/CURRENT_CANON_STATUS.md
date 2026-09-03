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

## Current economy locks
Currency:
> **G**

Retired currency name:
> **Auren**

Current scale and starting state:
- **1 economy unit = 200 G**;
- Chapter-0 starting wallet = **2,500 G**;
- Field Salve = **200 G**.

Current direct-G calibration:
- mandatory route = **~316,900 G**;
- ordinary formations = **~135,600 G** (~42.8% of mandatory direct G);
- mandatory story bosses / named encounters = **92,700 G**;
- fixed authored combat/event payouts = **5,300 G**;
- mandatory non-battle map = **80,800 G**;
- authored optional direct G = **329,600 G**;
- broad completionist direct-cash reference = **~646,500 G**, intentionally close to the ~650,000 G target.

Affordability validation:
- chapter-by-chapter mandatory-route liquidity is **PASS** under an aggressive modeled spend of one meaningful equipment purchase per chapter plus generous healing/MP/revive/status/utility restocking;
- premium Consumables are not required baseline purchases.

Premium Consumables:
- Emergency Kit — **8,000 G**;
- Reservoir Tonic — **12,000 G**;
- Emergency Rally — **15,000 G**;
- every Consumable-selling shop carries **1 of each from first access**;
- no automatic restock;
- guaranteed authored copies remain separate;
- premium Consumables remain non-sellable.

Other economy locks:
- protected/nonlethal resolution does **not** default to 0 G;
- Regional and Major Hunts receive strong G regardless of separate permanent rewards;
- 38-item registered ordinary-equipment catalog value = **251,000 G**;
- Relic-copy service fee = **6,000 G per successful copy**;
- all 18 current copy opportunities = **108,000 G** maximum service spend;
- exact Relic-copy service-provider/character integration is **OPEN** and must not be assigned to Kessara solely from legacy filenames or migration text;
- ordinary enemies have no random Consumable/equipment/material/vendor-trash economy;
- exactly **9 Regional Markets**.

Detailed economy authority:
> `../12_ECONOMY_AND_REWARDS/ECONOMY_MASTER.md`

## Current Major Hunt timing
- #1 **Ashen Whitehorn** — after Chapter 6 — recommended **Lv33**;
- #2 **Crownless Siege Marshal → Crownless War Engine** — after Chapter 7 — encounter recommendation **Lv41**;
- #3 **Concordance Guardian** — after Chapter 9 — recommended **Lv54**;
- #4 **Worldscar Leviathan** — after Chapter 10 — recommended **Lv60**;
- #5 **Final Archive Arbiter** — after Chapter 11 — recommended **Lv65**;
- #6 **The Unfinished World** — after Final Archive Arbiter clear + Vaelkor defeat in Chapter 12 — recommended **Lv70**.

Only Major Hunt #2 has a genuine fresh second body, and that fresh War Engine does **not** restore spent Prime identities.

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
- proof `gold` variable/data semantics and old currency-scale values that must be reconciled to current **G** authority;
- proof item/equipment records;
- old queue/Confirm Round battle architecture;
- stale technical IDs that require save-safe migration.

Current canon beats proof runtime. See:
> `../13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md`

## Current open areas
- story-owned special-enemy placement/timing dependencies explicitly left unresolved;
- Chapters 5–13 exact dialogue where not yet line-complete;
- Kessara's exact story/party role, biography fields, and any character-specific Relic-copy/service integration not yet re-established by current explicit authority;
- production implementation reconciliation;
- final production UI/readability validation;
- final audio/music completion and mix validation;
- visual production/style certification;
- whole-game/device/performance QA;
- explicitly bounded story/lore details still marked open in their owning domains.

The former mandatory-route enemy-difficulty recalibration sequence is not listed here as an open master-queue item because it is being handled through a different process.

The core G economy/reward design is **CLOSED** and is not an open-gap item unless later playtest evidence or an explicit design revision reopens it. The provider identity for the Relic-copy service is a character/story integration question and does not reopen the 6,000-G economy value.
