# Diyse — Migration Log

## Batch 01 — 05_BATTLE_SYSTEM
**Status:** EXTRACTED / RECONCILED  
**Baseline tracker:** v85  
**Current authority checked:** `docs/COMBAT_RULES.md` through v2.20 / Audit135, plus compatible Audit115 / Audit120 / Audit122 / Audit135.

Created:
- `05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`
- `05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md`
- `05_BATTLE_SYSTEM/TARGETING_AND_RETARGETING.md`
- `05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md`
- `05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md`
- `05_BATTLE_SYSTEM/CRITICAL_HITS.md`
- `05_BATTLE_SYSTEM/ELEMENTS.md`
- `05_BATTLE_SYSTEM/STATUS_EFFECTS.md`
- `05_BATTLE_SYSTEM/GUARD.md`
- `05_BATTLE_SYSTEM/BOSS_FORM_RULES.md`
- `05_BATTLE_SYSTEM/REMOVED_SYSTEMS_FIREWALL.md`

### Reconciliations applied
- v85's stale open Class Ability MP item is not carried into Battle System; Audit123 closed it.
- Audit122 Bleed cadence/clearing supersedes Audit115's old one-proc/any-heal behavior.
- current raw Status Resistance 0/5/10/15 is used; old percentage susceptibility is not a second generic resolver.
- Barrier removed.
- Brace removed.
- global Break/Stagger meter removed.
- Staggered status retained.
- Accuracy terminology normalized to Base Hit.
- fresh-HP forms refresh Prime availability; same-bar phases do not.

## Next batch
`06_CLASSES_AND_ABILITIES`

## Batch 02 — 06_CLASSES_AND_ABILITIES
**Status:** EXTRACTED / RECONCILED  
**Baseline tracker:** v85  
**Authority checked:** Audit115 class normalization, Audit123 closed Ability MP/CEXP authority, v85 current Mastery-Point removal and current class-name/kit corrections.

Created:
- class-system master and rules;
- all 6 Base-Class files;
- all 6 Subclass files;
- 78-entry Ability/Ultimate register;
- current closed MP-cost register;
- Trait register;
- Ultimate register;
- current Mastery architecture;
- selected-class stat-package multipliers;
- retired-Synthesis firewall.

### Reconciliations applied
- current classes: Crest Arcanist / Vowblade / Routeweaver / Proofhunter / Axiomblade / Ruin Warden;
- Synthesis removed;
- Mastery Point currency removed in active v85 working branch;
- Core Masteries auto-unlock at CL3 / 6 / 9 / 12;
- Subclass Masteries auto-unlock at CL3 / 5 / 7 / 11;
- Subclass Node 3 is Equipment Mastery; Node 4 is Legacy Mastery;
- donor Relic access at Subclass CL7;
- donor Legacy access at Subclass CL11;
- native Base-Class Legacy remains independent of donor Legacy Mastery;
- old third mechanical Subclass-Mastery effects quarantined rather than accidentally creating extra nodes;
- Ability MP costs preserved as CLOSED under Audit123;
- specific normalized Subclass kits use the fifth normal Ability at CL11; stale generic CL10 summary is flagged.

## Next batch
`07_CARDS`

## Batch 03 — 07_CARDS
**Status:** EXTRACTED / RECONCILED  
**Baseline tracker:** v85  
**Authority checked:** Audit116 Card/Prime command authority, Audit119 Standard/Prime MP and Prime scaling/control, Audit122 current Bleed runtime, later v85 source/Prismatic-Deluge closures.

Created:
- Card-system master and Six Faces files;
- full 24-Standard-Card register;
- 6 Standard-Card Face files;
- Standard Card use rules;
- exact Card acquisition ledger;
- Prime system rules;
- Prime loadout/access;
- Prime scaling;
- Prime status/control;
- Story Prime acquisition/awakening schedule;
- 6 individual Story Prime files;
- 6 individual Major-Hunt Prime files;
- Story and Major-Hunt Prime registers;
- retired Prime-state/name firewall;
- migration validation.

### Reconciliations applied
- Standard Card MP prices use current 18–48 Audit119/v85 ladder rather than Audit116's old costs.
- Prime Invocation uses 50 / 80 / 90; individual Prime commands cost 0 additional MP.
- Current Prime progression is Recovered → Awakened only.
- Last Cartographer and Parallax Host are current names.
- Acuity is the current Face name.
- Sanguine Alloy is Might; Worldsplitter is Elements/Earth.
- Measured Response, Burden Shift, and Split Moment preserve renamed source continuity.
- Audit122 Bleed lifecycle replaces stale Audit116 any-heal-clears / old action-proc wording.
- later v85 source closure supplies all 24 Standard Card homes.
- Prismatic Deluge is current tracker-level 90 × 4 = 360 total per target.
- Prime Ruin commands retain individually authored formulas and are not forced into character-Ability 75/25.
- Prime and Standard Card loadout systems remain separate.

## Next batch
`08_ITEMS_AND_EQUIPMENT`

## Batch 04 — 08_ITEMS_AND_EQUIPMENT
**Status:** EXTRACTED / RECONCILED  
**Baseline tracker:** v85  
**Authority checked:** Audit117 / Audit118 / Audit121 plus later accepted v85 equipment, consumable, Legacy, and Forge-component closures.

Created:
- Equipment System Master
- Equipment slot/handedness rules
- 91-piece Equipment Master Register
- ordinary weapon / armor / shield / Focus registers
- Conduit rules
- 36-Relic master / weapon / armor / secondary registers
- current Relic Trait file with removed Barrier/Brace dependencies cleaned
- exact 36/36 Relic placement ledger
- Relic-copy rules
- retired-Relic firewall
- 17-Legacy master register
- individual character Legacy package files
- Native Legacy project rules
- donor Legacy access
- 6 Legacy precursor ledger
- 6 Character Quest Legacy Component ledger
- 30 Forge Component matrix
- 20 Consumable register + use rules
- economy handoff
- open implementation handoff
- migration validation

### Reconciliations applied
- equipment count = 38 ordinary + 36 Relic + 17 Legacy = 91;
- 12 former Subclass Relics remain removed;
- no separate shared-Legacy artifact catalog;
- current v85 17/17 Legacy rebalance retained as tracker-level final / pending promotion;
- Barrier, Brace, Break-meter dependencies removed from current equipment text;
- Ilyra uses Wardrod + Shield-or-Focus;
- Torren Great Bow, Seyrik 2H Sword, and Nimera Legacy Conduit use Weapon + Secondary;
- Relic copying remains max quantity 2 and requires a matching copy-specific component;
- Legacy equipment cannot be copied;
- Forge Components = 30 = 12 Legacy-gate + 18 Relic-copy;
- Face material `Resource/Regulator` normalized to `Acuity/Calibration`;
- Consumables use current 20-item closure;
- pricing/shop economy is handed off to `12_ECONOMY_AND_REWARDS`;
- Kessara fee/UI/pickup presentation remains OPEN rather than invented.

## Next batch
`10_PROGRESSION_AND_EXP`

## Batch 05 — 10_PROGRESSION_AND_EXP
**Status:** EXTRACTED / RECONCILED  
**Baseline:** v85  
**Authority checked:** Audit123–Audit128 plus v85 Mastery-Point removal override.

Created Player EXP, campaign spine, CEXP, recruitment, class-completion, Mastery, reserve, formation, mandatory reward, optional reward, Level-70 proof, diminishing-return, encounter-planning, and enemy-handoff files.

### Key reconciliations
- restored End Ch12 ~Lv57 / Last Shelter ~Lv60 / ending ~Lv62 spine;
- quarantined temporary End Ch12 Lv62 / ending Lv66 branch;
- retained 6,000-CEXP CL13 curve;
- class-level completion remains Ch12 / ~Lv53–57;
- v85 removes Mastery Point currency despite older Audit123 schedule;
- Masteries auto-unlock at Base CL3/6/9/12 and Subclass CL3/5/7/11;
- optional cap-proof pool = 195,000 EXP, giving a 16,300 Lv70 buffer;
- ordinary weak-enemy Player EXP diminishes, authored packages do not;
- no CEXP diminishing-return system;
- optional CEXP retained as ~1,800 family envelope rather than inventing per-activity values.

## Next batch
`09_ENEMIES_AND_ENCOUNTERS`

## Batch 06 — 09_ENEMIES_AND_ENCOUNTERS
**Status:** EXTRACTED / RECONCILED  
**Baseline:** v85  
**Authority checked:** Audit90 / Audit93 production roster, Audit129–135 raw-stat closure, later accepted tracker roster/action cleanup for current Chapters 8–13.

Created:
- global enemy-system rules;
- reuse/variant policy;
- nonlethal/protected encounter rule;
- boss-form architecture;
- Chapter 0–13 enemy roster files;
- chapter-role master register;
- 34-row mandatory named/form raw-stat register;
- 12-Elite master register;
- 11 Regional Hunts plus individual Hunt files;
- 6 Major Hunts plus individual Hunt files;
- support-object register;
- Character Quest boss registry;
- recovered Chapter-10, Chapter-12 and Chapter-13 formation-composition references;
- retired enemy terminology/mechanic firewall;
- migration validation.

### Key reconciliations
- Audit130's Regulation Crucible Form-I HP 2,400 supersedes Audit129's 2,200.
- Reaction Conduit supersedes Elemental Hexarch.
- Annex Duelist uses exactly four element states.
- Weather Crown Shield Guard is current.
- current Chapter 10 has no optional Elite.
- current Chapter 11 uses Perfect Administrator / Authority Remnant / Calder / Custodian.
- current Chapter 12 uses Lord-Marshal Kharvek, final-capture Varkesh, Vaelkor and Throne Hunt.
- current Chapter 13 uses Devourer of Names, Last Weapon Archon and Reconstituted Entity → The Last Command; no Regional Hunt.
- fresh HP refreshes Prime availability; same-bar states do not.
- no Barrier, Brace, Break meter, natural Accuracy, Water/Wind standard element, or hidden extra-action systems.
- unresolved component/support HP was not fabricated.
- old 160-production-identity count retained only as provenance rather than misused as a chapter-role row count.

## Next batch
`01_CHARACTERS`

## Batch 07 — 01_CHARACTERS
**Status:** EXTRACTED / RECONCILED  
**Baseline:** v85 plus current character overlays and newest explicit corrections.

Created:
- 6 permanent playable character files;
- 9 major supporting-character files;
- 6 major-antagonist files;
- permanent-six relationship map;
- Torren/Maevra, Seyrik/Talia, Torren/Edda and Ceryth-family relationship files;
- antagonist differentiation;
- character chronology;
- open-detail register;
- retired-character terminology firewall;
- authority boundary file;
- migration validation.

### Reconciliations
- Nimera = age 22, not stale age 23.
- Torren = Acuity / Last Cartographer, not Resource / Last Measure.
- current twelve-class naming used instead of older subclass labels.
- Sixfold Volition used instead of deprecated Sixfold Accord.
- Maevra = age 41; old age 38/34 retired.
- Kessara kept nonplayable.
- Varkesh visual marked LOCKED under later visual authority.
- Othmar and Reconstituted Entity Step-1–5 status updated to complete under v1.51 rather than stale v1.49 open bookkeeping.
- Entity survival mechanism deliberately left open.
- dialogue, visuals and mechanics were referenced across domain boundaries rather than duplicated.

## Next batch
`04_WORLD_AND_LORE`

## Batch 08 — 04_WORLD_AND_LORE
**Status:** EXTRACTED / RECONCILED  
**Baseline:** v85 plus Audit108–111 map/travel authority, compatible ancient-history/knowledge locks, and later explicit founding/chronology corrections.

Created:
- world/lore master
- current region terminology
- retired place/lore terminology firewall
- exact final-map manifest/authority
- visible-map location register
- 13-hub register
- Ch0–Ch13 travel route register
- individual Yahtrenhold / Westways / Greyspires / Black Host Territory files
- Yahtrea / Black Host / Ancient-major site registers
- Character Quest geography register
- final-domain geography
- Yahtrea founding/modern history
- Ancient Diysean history
- Century of Twilight / Last Day
- Underground Crest civilization
- Entity / Last Weapon authorial truth
- Cards / return-of-magic chronology
- world chronology
- modern-knowledge firewall
- long-form cartographic mystery
- Yahtrea/Crown faction file
- Black Host faction file
- migration validation

### Reconciliations
- Audit111 region names control: Yahtrenhold / Westways / Greyspires / Black Host Territory.
- Crownhold, Southhold, Heartlands, Edgelands, Diysereach, formal Highlands and Blackstone are retired.
- Westguard replaces Westreach/Yahtrens Stand.
- The Blackspine remains canon though its printed final-map label is intentionally omitted.
- final map authority uses Audit111 1402×1122 hash b3cd7138...
- map binary is not fabricated/copied; manifest is preserved.
- current founding chronology uses King Yahtren and present ≈700 AF.
- Caelora is named for Yahtren's wife Caelora and occupies an Ancient Diysean capital site.
- first Card activation ≈200 AF; natural magical births ≈220 AF; magical creatures ≈250 AF.
- reason for delayed Card activation remains intentionally unexplained/open.
- ancient Cards remain post-Last-Weapon inheritance.
- Entity remains wholly unknown to modern civilization at story start.
- sole Entity-fragment survival mechanism remains open.
- Final Archive stays separate from the mandatory final-domain entrance.
- Last Shelter → Reactor Galleries remains the true point of no return.

## Next batch
`02_STORY`

## Batch 09 — 02_STORY
**Status:** EXTRACTED / RECONCILED  
**Baseline:** v85 plus current chapter index, closed Ch0–4 sources, Audits 91/92/107/109/112/113, current Ch11–13 operational projections, and later explicit story corrections.

Created:
- Story README/master spine
- current Chapter 0–13 files
- current scene-ID index
- cartographic mystery arc
- Calder/order/Prime-research arc
- Seyrik pre-reveal/defection arc
- Story Prime milestone ledger
- Black Host war arc
- final reveal/Severance arc
- recruitment/party-state continuity
- reveal-order firewall
- point-of-no-return file
- current terminology firewall
- retired story-branch firewall
- dialogue handoff
- open story-items register
- validation

### Reconciliations
- Chapter 10 The Last Blank inserted and current Ch11–13 reindex preserved.
- Ch10 party discovers Eastern Wayfinder rather than starting with knowledge of it.
- physical cartographic mystery ends in Ch10 before Registry Warden.
- Calder caused the lawful Ch0 Card transfer; Ch3 composite seizure remains a later abuse.
- Ch11 owns Calder/Crown Engine/Custodian truth.
- Ch12 owns final Black Host campaign, live Varkesh capture, Vhalmarch, Vaelkor, cleanup.
- late reciprocal-pair resolution beats preserved as story beats but removed from Synthesis gating.
- Ch13 launch is returnable; Last Shelter→Reactor Galleries is true PONR.
- Final Archive remains separate optional-major content.
- current Final Severance uses Last Cartographer/Acuity.
- current explicit correction overrides older Ch13 projection: one Entity fragment survived, but exact ancient survival mechanism remains OPEN.
- no third final-boss form; all six survive; no post-game.
- retired region/place terms removed from current-facing story prose.

## Next batch
`03_DIALOGUE`

## Batch 10 — 03_DIALOGUE
**Status:** EXTRACTED / RECONCILED  
**Repository source checkpoint:** `3fd07e92eda04f31ba613a654b3b1b28071f44e6`

### Exact source migrated
- Chapter 0: S001–S006 + C01–C02 from validated Godot Resources
- Chapter 1: S007–S011 + C03–C05
- Chapter 2: S012–S016 + C06–C07
- Chapter 3: S017–S021 + H01–H04
- Chapter 4: S022–S026 + C08/C09/H05 + Crown Prototype dialogue

Total line-complete scene sources: **41**

### Bounded corrections
- S009 Sixfold Accord → Sixfold Volition
- S019 Resource → Acuity
- Chapter-0 retired ward label removed from current-facing transcript staging
- existing Yahtrenhold/four-element corrections preserved

### Domain disentangling
- Chapters 5–13 receive authoring-status gates only; no fake dialogue
- embedded mechanics in old dialogue source are non-authoritative here
- Crown Prototype dialogue extracted without stale combat/Card-effect specification
- exact source manifest/checksums added

## Next batch
`11_QUESTS`

## Batch 11 — 11_QUESTS
**Status:** EXTRACTED / RECONCILED

Created:
- current quest-system master and family boundaries
- 28-activity optional-content register
- availability/final-cutoff authority
- combat/reuse rules
- world-state payoff rules
- dialogue handoff
- 6 current Character Quest files + master + Legacy handoff + retired CQ firewall
- 5 current ordinary Side Quest files + master + retired SQ firewall
- 11 Regional Hunt access register
- 6 Major Hunt access register
- open quest-items register
- migration validation

### Major reconciliations
- Audit103's 10 ordinary Side Quests superseded by the current final **5**.
- Removed: The Water Between Houses, The Dark Span, One Fire Burning, The Living List, When the Roads Open.
- Current Character Quest boss distribution normalized:
  Vaelira boss; Cyanis boss; Nimera none; Seyrik boss; Ilyra none; Torren boss.
- Crest Load Warden → Crest-Exhausted Warden.
- Revision Custodian removed.
- Black Host Remnant Captain and Old Relay Warden retained as current.
- Torren unlock uses after Chapter 10; route uses Ridgecut / Westline; Acuity / Last Cartographer.
- Character Quest completion grants the unique Legacy Component; it does not directly grant finished Legacy equipment.
- all current optional content uses Last Shelter → Reactor Galleries as the final cutoff where otherwise accessible.
- Hunts use fixed authored tuning, not old dynamic Party+ offsets.
- Major Hunt #6 dual gate/current one-bar architecture preserved.
- final current EXP packages linked to `10_PROGRESSION_AND_EXP`.

## Next batch
`12_ECONOMY_AND_REWARDS`

## Batch 12 — 12_ECONOMY_AND_REWARDS
**Status:** EXTRACTED / RECONCILED

Created:
- Economy README/master
- Auren denomination authority
- exact current 20-Consumable Auren/equivalence ledger
- normal-stock progression and commerce endpoints
- Cresthaven Quartermaster authority
- Vhalmarch Forward Supply authority
- exact 38/38 ordinary-equipment Auren purchase/replacement table
- ordinary-equipment sell rule and full sell table
- ordinary-equipment registration/repurchase/anti-missability rules
- campaign-income / encounter-Auren tuning boundaries
- optional-content reward master and Side/CQ/Hunt boundaries
- reward-only Consumable placement
- Kessara copy-fee open boundary
- chest/enemy reward handoffs
- reward distribution rules
- open-economy register
- retired-economy firewall
- migration validation

### Major reconciliations
- Auren is the current ordinary currency; 1 economy unit = 20 Auren.
- corrected current Salve family is 250 / 750 / 1,500 / 2,250 HP.
- patched stale 600 / 1,200 HP values in the migrated `08` Consumable register.
- current 20-item Consumable ledger preserved, including Grand Salve and Reservoir Tonic 640-equivalent correction.
- three reward-only Consumables remain outside ordinary stock and retain their current first-guaranteed placements.
- older 19-item Consumable and 48-piece ordinary-equipment economy branches quarantined.
- current ordinary catalog is 38; all 38 now have one exact Auren purchase/replacement ledger in `12`.
- ordinary sell calculation preserves the established economy-unit 50%-rounded-down rule after Auren conversion.
- Cresthaven remains full registered ordinary-equipment backfill authority.
- current working market spine uses nine Regional Markets and Westguard terminology, with formal hub/service sync caveat retained.
- Vhalmarch uses event-relative `after capture/stabilization` wording so stale pre-reindex chapter numbers do not propagate.
- old Elite/Hunt/Side-Quest cash bands retained only as tuning provenance; no unsupported exact Auren payouts invented.
- Side Quest/CQ direct economic packages and Kessara copy fee remain OPEN rather than guessed.

## Next batch
`13_UI_AND_IMPLEMENTATION`

## Batch 13 — 13_UI_AND_IMPLEMENTATION
**Status:** EXTRACTED / RECONCILED  
**Runtime checkpoint inspected:** `3fd07e92eda04f31ba613a654b3b1b28071f44e6`

Created:
- UI/implementation master
- current runtime implementation-status map
- authority-precedence/divergence rules
- screen/Android and input rules
- menu/exploration/combat/battle-flow/status UI requirements
- party/formation UI
- class/CEXP/Mastery UI
- equipment UI
- Standard Card UI
- Prime UI
- inventory/material UI
- quest/Hunt UI
- world-map/travel UI
- shop/economy UI
- dialogue UI
- save-data + save/load UI
- Kessara Relic-copy service UI boundary
- stable-ID/data rules
- runtime state boundary
- open UI/implementation register
- retired UI/runtime firewall
- Godot foundation notes
- code/canon divergence ledger
- validation/test gates
- content-data handoff
- Android performance/accessibility notes
- implementation frontier
- migration validation

### Major reconciliations
- current v85 **removes Mastery Points** despite stale Audit123-era repository docs; no point UI/persistence is allowed.
- current Prime architecture supersedes old proof bearer lock and proof duration.
- production UI/save state must use **Auren**, not proof `gold`.
- proof item/equipment/Prime names are not production content.
- Chapter ID support extends through chapter_13 and current story scene numbering through S073.
- current 3 Standard Card slots + 2 Prime slots are separate.
- current equipment slots are Weapon / Secondary / Armor only.
- dialogue remains no-choice and Resource/registry-driven.
- save schema v1 is retained as proven foundation, not declared final production schema.
- Kessara copy-service logic is implemented/tested; fee/timing/original-vs-copy UX remain open.
- Last Shelter → Reactor Galleries remains the final UI warning/return cutoff.

## Next batch
`14_ART_AND_VISUALS`

## Batch 14 — 14_ART_AND_VISUALS
**Status:** EXTRACTED / RECONCILED

Created:
- art/visual master
- character visual-authority register
- six permanent playable visual files
- Maevra / Kessara / royal-supporting visual files
- antagonist visual-authority file
- HD-2D environment master
- regional / Ancient Diysean / Black Host environment languages
- Cresthaven evolution authority
- Chapters 0–4 environment families
- final world-map visual handoff
- scene/VFX tier system
- four-element VFX language
- Face/Card/Prime visual language
- Final Severance Story-Prime visual roles
- portrait/sprite derivation
- character silhouette separation
- animation-cost rules
- asset naming/versioning
- open visual-production register
- retired visual firewall
- migration validation

### Major reconciliations
- HD-2D retained as sole active presentation target.
- approved anime-style studio renders treated as exact appearance masters, not loose inspiration.
- Cyanis latest correction preserved: shield removed; crest/amulet moved to hip; hazel eyes/light facial hair/current blue-silver-black read.
- Nimera latest master preserved at age 22 with increased purple hair presence and green/gold Card + book.
- Ilyra, Torren, Seyrik, Maevra, Kessara exact appearance anchors preserved.
- Vaelira kept LOCKED without fabricating missing text details not recovered from her exact approved image.
- Kessara's 4'4" height explicitly protected from visual infantilization.
- Varkesh visual status normalized to LOCKED.
- current four-element VFX architecture only; Wind/Water combat-element art retired.
- Final Severance visual sequence uses Acuity / Last Cartographer.
- Audit111 final map dimensions/hash/label presentation preserved.
- exact approved image binaries are not regenerated or replaced by text-only reconstruction.

## Next batch
`15_AUDIO_AND_MUSIC`

## Batch 15 — 15_AUDIO_AND_MUSIC
**Status:** EXTRACTED / RECONCILED

Created:
- audio authority master
- current music OPEN-status authority
- soundtrack open-scope register
- functional music requirements
- story/music continuity boundary
- diegetic-music boundary
- originality/reference rule
- sound-design master
- combat/Card/Prime/UI/environment SFX requirement files
- dialogue/voice-audio boundary
- historical music-research firewall
- Ancient Diyse music R&D summary
- Ancient research-method file
- historical regional-music research summary
- reference/originality research firewall
- runtime audio-status file
- bus/settings requirements
- audio-state/transition requirements
- asset naming/metadata rules
- open audio register
- retired audio/music firewall
- migration validation

### Major reconciliations
- later Complete Master authority controls: **ALL whole-project music remains OPEN**.
- older Heartlands=LOOP / Highlands=POCKET / Edgelands=SONG scheme is preserved only as research history.
- old Black Host metal-derived and Ancient Diyse psychedelic/progressive prescriptions are not restored as current score canon.
- latest recovered Ancient Music appendix through **Sample 52** is preserved as research authority only.
- no soundtrack track list, leitmotif scheme, regional score, voice plan, or mix target was invented.
- current gameplay systems still define functional SFX needs.
- no production audio bank exists in the inspected runtime repository.

## Next batch
`16_BALANCE_AND_TESTING`

## Batch 16 — 16_BALANCE_AND_TESTING
**Status:** EXTRACTED / CROSS-DOMAIN VALIDATED

Created:
- balance closure/status authority
- change-control rules
- campaign progression balance
- CEXP rebalance frontier
- encounter hierarchy
- boss-form balance rules
- Hunt certification
- Ability-MP verification
- Card/Prime balance verification
- equipment/economy/status/formula/optional-content balance files
- weak-enemy DR test vectors
- test-strategy master
- campaign playtest matrix
- encounter pacing plan
- boss playtest template
- Prime/status/save/Android/nonlethal/quest regression plans
- current automated-test inventory
- known regression debt
- required new automated tests
- static cross-domain consistency report
- raw-stat certification index
- current balance-risk watchlist
- QA severity/acceptance
- final release gates
- open/reopened balance register
- retired balance firewall
- runtime test-suite status
- migration validation

### Critical reconciliation
A cross-domain contradiction was caught rather than papered over:
- old Audit123-derived CEXP allocation projects full Base+Subclass completion around Player Lv53–57;
- later explicit user direction changed the desired timing to **around Player Lv62** and identified the CEXP pass as needing a redo.

Therefore:
> **CEXP completion timing/allocation is REOPENED / PENDING RECALIBRATION.**

The current 6,000-CEXP curve/chapter tables remain the last formal reference model, but Lv53–57 is no longer an accepted completion target. No new CEXP values were invented in the migration.

### Static checks
- mandatory EXP = 448,100
- ordinary + named split = 448,100
- encounter centers = 225
- optional cap-proof pool = 195,000
- Lv70 pre-Shelter buffer = 16,300
- Hunt/Elite counts consistent

### Runtime-test note
Existing Godot test sources were inspected. A fresh Godot execution was not claimed because the artifact environment does not expose the project runtime binary. Existing stale Prime/bearer-lock assertions are catalogued for update.

## Next
`FINAL CONSOLIDATION / 90_WORKING + 99_ARCHIVE CLEANUP`
