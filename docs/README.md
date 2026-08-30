# DIYSE CANON REORGANIZATION — v98 REPOSITORY TRANSITION AUDIT

**Supersedes:** v97 package as the current working package. v97 Archive Leviathan certification remains retained.

## v98 changes
- Audited the active `Diyse-Game` repository boundary at current `main` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.
- Confirmed that commit exactly matches the runtime/source checkpoint already inspected during the v97 reorganization.
- Confirmed the subject-folder package is canon/documentation only and must **not** replace Godot runtime/build/test files.
- Defined the clean transition: preserve runtime/build/test/CI surfaces, replace the old `docs/` authority, and rewrite root `README.md` / `AGENTS.md` as thin authority routers.
- Added `90_WORKING/REPOSITORY_REPLACEMENT_AUDIT_v98.md` and staged proposed root guidance under `90_WORKING/GITHUB_TRANSITION_STAGING/`.
- **No canon or balance values changed. No GitHub mutation executed.**

# DIYSE — CANON PROJECT LIBRARY

**Status:** FINALIZED SUBJECT-FOLDER REORGANIZATION  
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Written master-canon head used during migration:** **v2.20 / Audit135**, plus newer explicit corrections preserved in active domain files.

This package replaces the old giant cumulative-tracker workflow with a stable subject-based project library.

## Read order

1. `00_MASTER_CONTROL/`
2. the relevant numbered subject domain
3. `90_WORKING/` only when the subject is explicitly still open/reopened
4. `99_ARCHIVE/` only for provenance/history

## Authority rule

Current active domain files are the normal source of truth.

If material conflicts:
1. newest explicit approved correction;
2. current active domain authority;
3. cross-domain rule in `00_MASTER_CONTROL`;
4. clearly marked working material for an unresolved question;
5. archive/provenance material only for history.

`99_ARCHIVE` never silently overrides active canon.

## Active content domains

- `01_CHARACTERS`
- `02_STORY`
- `03_DIALOGUE`
- `04_WORLD_AND_LORE`
- `05_BATTLE_SYSTEM`
- `06_CLASSES_AND_ABILITIES`
- `07_CARDS`
- `08_ITEMS_AND_EQUIPMENT`
- `09_ENEMIES_AND_ENCOUNTERS`
- `10_PROGRESSION_AND_EXP`
- `11_QUESTS`
- `12_ECONOMY_AND_REWARDS`
- `13_UI_AND_IMPLEMENTATION`
- `14_ART_AND_VISUALS`
- `15_AUDIO_AND_MUSIC`
- `16_BALANCE_AND_TESTING`

## Working and archive

`90_WORKING` contains unresolved/reopened work only. It is not a second canon library.

`99_ARCHIVE` contains migration history, retired authority, and provenance references. It is deliberately non-authoritative.


## v76 balance update
Chapter 0 mandatory-vs-completionist difficulty validation is complete. Riftmaw's raw HP was corrected for actual Lv1 solo throughput, while the enemy Power audit remains closed. See `16_BALANCE_AND_TESTING/BALANCE/CHAPTER_00_MANDATORY_COMPLETIONIST_VALIDATION.md`.

## v77 balance update
Chapter 1 mandatory-vs-completionist difficulty validation is complete using the actual **Lv1 chapter start → Lv5 chapter end** progression points. Watch Captain Frame was corrected **820 → 500 HP** for its real Hollow Watch Lv2–3 access point. Ordinary enemy Powers, Hollow Watch Castellan Powers, Briarhide Powers, and Cistern Devourer Powers remain unchanged. See `16_BALANCE_AND_TESTING/BALANCE/CHAPTER_01_MANDATORY_COMPLETIONIST_VALIDATION.md`.


## v78 balance update
Chapter 1 was corrected to explicitly include Maevra in all relevant battle-party states; Watch Captain Frame 500 HP and Cistern Devourer 2,706 HP remain validated. Chapter 2 mandatory-vs-completionist validation is complete using **Lv5 start → Lv9 end** with Cyanis + Ilyra + Torren + Maevra. No direct-damage Power changed. Archive Leviathan Recorded Pattern is now exact: one visible pattern, 20% repeated-action direct-damage reduction, 2 rounds in State A / 1 round in State B, **45% HP** same-bar emergence. See `16_BALANCE_AND_TESTING/BALANCE/CHAPTER_02_MANDATORY_COMPLETIONIST_VALIDATION.md`.


## v79 balance update
Chapter 3 mandatory-vs-completionist validation is complete using the actual **Lv9 start → Lv13 end** progression points rather than a flat chapter level. Maevra is explicitly included as a legal guest combatant; after Nimera's S019 recruitment the combat roster contains five available bodies with a four-active-member hard cap. The previously approved Chapter-3 formation compositions were recovered into the owning enemy folder without reviving their old numeric stats/EXP. Grand Inquisitor Frame failed its 2–4 serious-round Elite role at true Lv9–10 access and was corrected **1,450 → 1,200 HP**. First Command Warden and Archive Judgment Engine remain unchanged. No direct-damage Power changed. Next validation frontier: **Chapter 4**.

## v80 balance update
Chapter 4 mandatory-vs-completionist validation is complete using its real **Lv13 start → ~Lv15 middle → Lv17 end** progression. Maevra is not treated as a Chapter-4 default combatant; Vaelira joins permanently after S022 and becomes a legal fifth roster option while the active-party cap stays four. The approved Reaction Annex opening/middle/late formation compositions and weights were restored to the owning enemy folder without reviving obsolete historical stat/EXP rows. Ordinary enemies, Annex Duelist, Elder Briarhide, Reaction Conduit, Regulation Crucible → The Seventh Reaction, and Crown Prototype all retain their current raw stats and direct-damage Powers. No numerical balance change was required. Next frontier: **Chapter 5**.

## v81 balance update
Chapter 5 mandatory-vs-completionist validation is complete using the actual **Lv17 start → Lv22 end** progression rather than a flat chapter-end assumption. The five permanent characters are available throughout, but the active party remains four; Maevra is not included as a default Chapter-5 combat guest and Seyrik is not playable yet. Ordinary Chapter-5 enemy bodies, Ruin Forgemaster, Furnace Tyrant, Deepforge Colossus, and Whitehorn Ravager all retain their current raw stats and direct-damage Powers. Exact Chapter-5 ordinary formations and Highland Resistance Fighter placement remain explicit data/story dependencies because the chapter is not line-complete. No numerical balance change was required. Next frontier: **Chapter 6**.


## v82 balance update
Chapter 6 mandatory-vs-completionist validation is complete using the actual **Lv22 start → Lv27 end** route progression. Seyrik is explicitly treated as a hostile/authored story identity until his forced-disengagement encounter and becomes playable only after the chapter-end recruitment resolution; the active battle party remains four. Weather Crown and Crimson Work ordinary bodies, authored-special kits, Crimson Progenitor, Crownstorm Roc, Matron Zevraya → Perfected War Mother, Masked Seyrik, Winterglass Titan, and post-Chapter-6 Major Hunt #1 Ashen Whitehorn all retain current raw stats and direct-damage Powers. Exact Chapter-6 ordinary formations and authored-special placements remain story/data dependencies. No numerical balance change was required. Next frontier: **Chapter 7**.


## v83 balance update
Chapter 7 mandatory-vs-completionist validation is complete using the actual **Lv27 start → Lv32 end** progression. All six permanent characters are available, but the active battle party remains four; Seyrik is fully playable throughout the chapter. Sixfold Volition occurs only after the Prison/Change resolution, so all Chapter-7 mandatory combat is validated with Base Classes rather than Subclasses. Chapter-7 ordinary enemies, authored/protected kits, First Registrar's Shade, Chainworks Behemoth, Warden of the Nameless / Revision Arbiter, Regional Hunt #7 Rift Gate Colossus, and the existing post-Chapter-7 Major Hunt #2 recertification all pass without numerical or Power changes. Exact ordinary formations were later restored in v90; authored-special placements remain story-owned. Next frontier: **Chapter 8 — Lv32 start → Lv37 end**, with Subclass access legal throughout.


## v84 balance update
Chapter 8 mandatory-vs-completionist validation is complete using the actual **Lv32 start → Lv33 Western Rift Engine → Lv35 Varkesh → Lv37 end** route anchors. All six permanent characters are available, the active party remains four, and Subclass access is legal throughout the chapter. Chapter-8 ordinary enemies, Conqueror Legate, Western Rift Engine, Marshal Varkesh → Rift Conqueror, and Regional Hunt #8 Rift Siege Beast all retain their current raw stats and direct-damage Powers. Major Hunt #2's existing after-Chapter-7 recertification remains compatible and is included as a legitimate completionist progression source. Chapter-8 formations were later restored in v90; RH8 exact within-chapter timing remains story-owned. No numerical balance change was required. Next frontier: **Chapter 9 — Lv37 start → Lv42 end**.


## v85 balance update
Chapter 9 mandatory-vs-completionist validation is complete using the actual **Lv37 start → Lv37 Equal Mercy → Lv38 post-Last-Sanctuary → Lv40 Rhazek → Lv42 end** progression rather than a flat chapter-end level. All six permanent characters are available, the active party remains four, and Subclass access is legal throughout. Chapter-9 ordinary enemies, Mercy Warden, Relay-Fever Patient, Ruin Breach Captain, Equal Mercy Arbiter, Commander Rhazek → Bastion Devourer, Regional Hunt #9 Mercyfallen Behemoth, and the existing post-Chapter-9 Major Hunt #3 Concordance Guardian recertification all pass without numerical or direct-damage Power changes. Rhazek is validated against **Lv48 completionist without RH9** and **Lv49 with RH9**, preserving the unresolved exact RH9 return trigger rather than inventing one. Chapter-9 formations were later restored in v90; RH9's exact within-chapter trigger remains story-owned. Next frontier: **Chapter 10 — Lv42 start → Lv47 end**.


## v86 balance update
Chapter 10 mandatory-vs-completionist validation is complete using the actual **Lv42 start → Lv45 Registry Warden → Lv46 post-Warden → Lv47 end** route anchors. Completionist authored-content progression is tracked at approximately **Lv51 chapter start → Lv54 Registry Warden → Lv55 clear**. All eight reused ordinary enemy bodies, the recovered Eastern Wayfinder/Buried Registry formations, Registry Warden, and post-Chapter-10 Major Hunt #4 Worldscar Leviathan retain their current raw stats and direct-damage Powers. No numerical balance change was required. Those v86 data gaps were later closed in v90: Eastern Forest formations were recovered, missing migrated action percentages gained a deterministic fallback, and Old Relay Warden received an exact current sheet. Next frontier: **Chapter 11 — Lv47 start → Lv52 end**.


## v87 balance update
Chapter 11 mandatory-vs-completionist validation is complete using the actual **Lv47 start → Lv49 Calder → Lv51 Custodian → Lv52 end** route anchors. Completionist authored-content progression is tracked at approximately **Lv57 chapter start → Lv59 Calder → Lv60 Custodian → Lv61 clear** before any unresolved RH#10 timing assumption. The approved Chapter-11 opening/middle/late formation compositions and weights were recovered into `09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_11_FORMATIONS.md` without reviving obsolete historical stat/EXP rows. All nine ordinary bodies, Crown Engine Technician kit, Perfect Administrator, Calder → Crown-Bound Living Anchor, The Custodian, Regional Hunt #10 Authority Remnant, and post-Chapter-11 Major Hunt #5 Final Archive Arbiter retain current raw stats and direct-damage Powers. Exact ordinary action-selection weights, Crown Engine Technician scene placement, and RH#10 exact within-chapter access remain explicit data/story dependencies. No numerical balance change was required. Next frontier: **Chapter 12 — Lv52 start → Lv57 end**.


## v88 balance update
Chapter 12 mandatory-vs-completionist validation is complete using the actual **Lv52 start → Lv54 Varkesh → Lv56 Vaelkor → Lv57 clear** route anchors. A fixed-content completionist enters around **Lv63**, reaches Varkesh at **Lv64**, Vaelkor at **Lv66** (or ~Lv67 if RH11 is legally available and cleared beforehand), and ends just short of Lv67 before unresolved/late optional content. All eleven ordinary bodies, the nine recovered formations, Compelled Relay Bearer, Lord-Marshal Kharvek, Marshal Varkesh final capture, Emperor Vaelkor → Sovereign Panoply Unbound, Regional Hunt #11 Throne of Emperor Vaelkor, and Major Hunt #6 The Unfinished World retain current raw stats and direct-damage Powers. Kharvek placement, RH11 timing, exact ordinary action/formation weights, and The Unfinished World's final runtime duration remain explicit dependencies. No numerical balance value or direct-damage Power changed. Next frontier: **Chapter 13 — Lv57 start → Lv60 Last Shelter → Lv62 ending**.


## v89 balance update
Chapter 13 mandatory-vs-completionist validation is complete using the actual **Lv57 start → Lv58 Last Weapon Archon → Lv60 Last Shelter/PONR → Lv61 final boss → Lv62 ending** route anchors. The established completionist proof pool produces **Lv68 at Chapter-13 start, Lv69 before the Archon without MH6, and Lv70 by Last Shelter**; a full all-content route may cap earlier. All nine Chapter-13 ordinary bodies, the recovered 3–4-body formations, Devouring Echo / Calamity Memory replay rules, Devourer of Names, Last Weapon Archon, Reconstituted Entity → The Last Command, and the final support objects retain current raw stats and direct-damage Powers. No numerical enemy value or Power changed. The planned paper Enemy & Boss Mandatory-vs-Completionist Validation is now **complete through Chapters 0–13**. Remaining targeted data/runtime dependencies are tracked separately. **This v89 note is superseded by v91: CEXP recalibration is closed at ~Lv55–60; representative true-battle certification is next.**


## v90 enemy-completion update
The dedicated Character Quest boss completion pass closes the three intentionally deferred exact sheets and Seyrik's missing raw-body gap. Elemental Forecast Construct, Crest-Exhausted Warden, Black Host Remnant Captain, and Old Relay Warden now each have implementation-ready raw stats, Powers, Base Hit, weights, status/AI rules, and mandatory-vs-completionist paper validation under `09_ENEMIES_AND_ENCOUNTERS/QUEST_BOSSES/`. The global campaign Power audit remains closed; these values complete previously deferred quest-boss sheets rather than reopening already audited campaign actions. Formation-table consolidation, support-object completeness, and the action-selection fallback are also closed in v90. Bounded scene placements are now explicitly story-integration dependencies rather than enemy-design gaps; runtime-only QA remains separate.


### v90 static-enemy closure
Enemy static design is now **CLOSED**. Chapter 1–13 formation authority is restored under `09`, Chapter 0 remains authored/tutorial-only, support objects are numerically complete, and missing migrated per-action percentages have a deterministic eligible-action fallback. Exact story placements and runtime playtests are intentionally separate. **Historical v90 note: CEXP was next at this point; v91–v92 subsequently closed that recalibration.**


## v91 progression/test-readiness update
Prime loadout access is restored to **1 slot per permanent character from Chapter-4 Prime battle-loadout access until Sixfold Volition, then 2 slots after Volition**. CEXP is formally recalibrated without changing the 6,000-CEXP CL13 curve: mandatory-route full Base + Subclass completion now spans **~Lv55–60**, with **7,000 post-Volition mandatory CEXP by end Ch12** and **8,500 by Last Shelter**. Optional CEXP is now exact at **1,000 before Major Hunt #6 / 1,075 including it**. The next balance step is to build exact party snapshots and run representative true-battle simulations.


## v92 recruitment-aware CEXP correction
The v91 late-game CEXP budgets remain active, but its inherited character-specific Volition planning centers were approximate. v92 now applies CEXP only from each permanent character's actual recruitment handoff onward. Corrected mandatory Volition centers are **Torren 5,350 / Vaelira 5,250 / Cyanis 4,950 / Ilyra 4,950 / Nimera 4,500 / Seyrik 3,500**. This moves Torren's mandatory full-class completion from ~Lv55 to about **Lv56**, while the overall completion spread remains **~Lv56–60 inside the intended Lv55–60 band**. True-battle snapshots must use this recruitment-aware ledger.

## First true-battle certification
- **Hollow Watch Castellan — PASS / RETAIN.**
- Mandatory Lv2 smart-policy median: **6 rounds** across 20,000 simulations; 0% KO incidence.
- High-side Lv3 smart-policy median: **6 rounds**; 0% KO incidence.
- Aggressive support-ignore play is faster but creates Heavy-Bolt/Bleed exposure and nonzero KO risk, confirming the support architecture has tactical value.


## v94 closure-status synchronization
Owning content was already correctly migrated through v93. v95 synchronizes stale master/status labels only; no design numbers changed.



## v96 — Bleed escalation update
- Bleed still starts at **3% Max HP per qualifying proc**.
- If the same Bleed remains active through **3 affected-unit turns**, it escalates by **+1 percentage point** to **4% Max HP per qualifying proc** until removed.
- The third affected turn's own action proc uses 3%; escalation activates after that turn resolves.
- Reapplying active Bleed does not reset its age/escalation. Full removal followed by a new application restarts at 3%.
- Existing round-tick + action-tick cadence, application chances, indirect-damage rules, and clear conditions are unchanged.
- Regional Hunt conversion: **2.25% → 3%** after escalation. Major Hunt / mandatory boss conversion: **1.5% → 2%**.
- Hollow Watch normal/smart true-battle verdict remains valid because its certified line prevents Heavy Bolt Bleed from resolving.

## v95 — Bleed magnitude update
- Global Bleed magnitude: **2% → 3% Max HP per qualifying proc**.
- Existing round-tick + action-tick cadence remains unchanged.
- Existing Bleed application chances remain unchanged.
- Hunt/boss magnitude conversions remain 75% / 50%, now resolving to 2.25% / 1.5% Max HP per proc respectively.
- Hollow Watch normal/smart true-battle verdict remains valid; aggressive Bleed-risk statistics from v93 are historical until refreshed under v95.


## v97 — Archive Leviathan true battle
Archive Leviathan is now **TRUE-BATTLE PASS / RETAIN**. Mandatory Lv6 prepared testing produced a 10-round median / 10.05 mean with 0.05% any-KO; completionist/high-side Lv7 produced a 9-round median / 8.58 mean with 0% any-KO. No boss numerical value or Power changed. The only boss-mechanic closure is the deterministic Recorded Pattern trigger: the same actor must repeat the same exact eligible direct-damage action on consecutive offensive actions; the trigger hit remains full damage and later matching uses receive the existing 20% penalty while the visible Pattern is active.

Blue Warden Clear Warding's migrated stat-change text is restored to its accepted exact value: **+5 Status Resistance for 2 rounds**. The representative true-battle suite remains active; Regulation Crucible → Seventh Reaction is next.
