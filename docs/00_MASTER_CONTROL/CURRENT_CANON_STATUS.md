# Diyse — Current Canon Status

**Project-folder reorganization:** COMPLETE  
**Migration baseline:** v85 consolidated working tracker  
**Written master-canon head used:** v2.20 / Audit135 + newer accepted corrections

## Active numbered domains
All major domains `01` through `16` are migrated.

## Current major locks
- 6 permanent playable characters
- active party max 4
- Chapter 0 + Chapters 1–13
- true PONR = Last Shelter → Reactor Galleries
- four standard elements
- five universal harmful statuses
- Spirit is the magic-resistance stat
- 24 Standard Cards + 12 Primes
- six Faces: **Might / Elements / Grace / Perception / Memory / Ruin**
- Prime progression Recovered → Awakened
- 38 ordinary equipment + 36 Relics + 17 Legacies
- Player Level cap 70
- campaign-only ending about Lv62
- 5 Side Quests + 6 Character Quests + 11 Regional Hunts + 6 Major Hunts
- HD-2D active presentation target
- final whole-project music OPEN

## Current CEXP timing — v92 RECRUITMENT-CORRECTED / RECALIBRATED
Full Base + Subclass progression on the correctly managed mandatory route now completes across:
> **Player Lv55–60**

Locks:
- CL13 remains **6,000 cumulative CEXP**;
- Ch12 mandatory CEXP = **1,250**;
- Ch13 mandatory CEXP = **1,750**, with **1,500 before Last Shelter / 250 after**;
- post-Volition mandatory cumulative = **7,000 end Ch12 / 8,500 Last Shelter**;
- optional CEXP = **1,000 before MH6 / 1,075 including MH6**.

Old Lv53–57, temporary Lv62, and ~1,800 optional-CEXP planning models are retired.

## Current implementation debt
- proof `first_champion` bearer lock is stale
- proof `gold` is stale; current currency = Auren
- proof item/equipment records are not production content
- stale Mastery Point assumptions must not ship

## Archive rule
`99_ARCHIVE` is provenance/history only and never silently overrides active domains.


## v18 incremental status
- Mirena quest EXP redistribution is merged exactly.
- Post-v17 Major Hunt unlock timing is merged: #1 after Ch5, #2 after Ch6, #3 after Ch8, #4 after Ch9; #5 remains after Ch10.






## Major Hunt timing
- #1 Ashen Whitehorn — after **Chapter 6**
- #2 Crownless Siege Marshal / Crownless War Engine — after **Chapter 7**
- #3 Concordance Guardian — after **Chapter 9**
- #4 Worldscar Leviathan — after **Chapter 10**
- #5 Final Archive Arbiter — after **Chapter 11**
- #6 The Unfinished World — unchanged existing late dual gate


## Major Hunt recertification status
- #1 Ashen Whitehorn — **recertified**: after Ch6, recommended Lv33.
- #2 Crownless Siege Marshal / War Engine — **recertified**: after Ch7, encounter recommendation Lv41.
- #3 Concordance Guardian — **recertified**: after Ch9, recommended Lv54.
- #4 Worldscar Leviathan — **recertified**: after Ch10, recommended Lv60.
- #5 Final Archive Arbiter — **recertified**: after Ch11, recommended Lv65.
- #6 — unchanged late Lv70 target.


Major Hunt #1–#5 later-unlock recertification is complete. The current recommendation ladder is:
> **Lv33 / Lv41 / Lv54 / Lv60 / Lv65 / Lv70**


## Mandatory boss route recertification
Current workflow:
> mandatory-route level → same boss checked against completionist level → change stats only if the boss misses its intended tier.

Completionists are allowed to be safer and roughly 2–3 rounds faster. Bosses do not dynamically scale to erase optional progression.

Current position:
- Hollow Watch Castellan — **v93 TRUE-BATTLE CERTIFIED / RETAINED** using actual S008 ~Lv2 central / ~Lv3 high-side
- working line: Lv6 / 450 HP / 42 ATK / 27 MAG / 27 DEF / 24 Spirit / 25 SPD
- pacing: aggressive ~4–5 / normal ~6 / safety ~7–8
- Archive Leviathan — **v97 TRUE-BATTLE CERTIFIED / RETAIN / POWER COMPLETE**: HP1,900 / ATK50 / MAG52; Rend220 / Crash140 / Undertow150
- Commander Rhazek — Bastion Master — **VALIDATED v78 / POWER COMPLETE**: mandatory ~Lv7 / completionist ~Lv8; Lv10 / HP2,050 / ATK58 / MAG44
- First Command Warden — **VALIDATED v79 / POWER COMPLETE**: mandatory Lv11 / completionist Lv12 nearly Lv13; Lv14 / HP2,850 / ATK72 / MAG72
- Elder Briarhide — **VALIDATED v80 / POWER COMPLETE**: mandatory Lv13 / completionist Lv15; Lv14 / HP2,100 / ATK72 / DEF60 / Spirit55; exactly 4 rounds
- Reaction Conduit — **VALIDATED v80 / POWER COMPLETE**: mandatory Lv13 / completionist Lv15; Lv17 / HP2,400 / ATK58 / MAG80; ~8–9 mandatory rounds
- Regulation Crucible → The Seventh Reaction — **v99 TRUE-BATTLE CERTIFIED / PASS / RETAIN / POWER COMPLETE**: mandatory Lv15 / completionist Lv17; Form-I HP2,400 / Form-II HP2,900 retained; strict prepared Lv15 no-Prime benchmark **100% wins / median 18**, with one legal Recovered Last Sentinel **100% wins / median 14**
- Furnace Tyrant — **VALIDATED v81 / POWER COMPLETE**: mandatory Lv18 / completionist Lv20; Lv23 / HP3,400 / ATK100 / MAG72; ~9–10 mandatory rounds
- Furnace Servitor direct-damage kit — **POWER COMPLETE**
- Deepforge Colossus — **VALIDATED v81 / POWER COMPLETE**: mandatory Lv20 / completionist Lv22; Form-I HP3,400 / Form-II HP4,000; ~14–16 mandatory rounds
- Guard Press / Repair Arm / Command Loom — **POWER COMPLETE**
- Crownstorm Roc — **VALIDATED v82 / POWER COMPLETE**: mandatory Lv23 / completionist Lv25; Lv26 / HP4,800 / ATK100 / MAG112; ~9–10 mandatory rounds
- Matron Zevraya → Perfected War Mother — **VALIDATED v82 / POWER COMPLETE**: mandatory Lv24 / completionist Lv27; Blood Matron HP4,400 / Perfected War Mother HP5,200; ~15–17 mandatory rounds
- Zevraya Reservoirs / Brood Organisms — **POWER COMPLETE**
- Masked Ruin Vanguard — Seyrik — **VALIDATED v82 / POWER COMPLETE**: mandatory Lv25 / completionist Lv27; Lv27 / HP4,000; 20% protected disengagement floor
- Chainworks Behemoth — **VALIDATED v83 / RAW LINE RETAINED / POWER COMPLETE**: mandatory Lv27 / completionist Lv31; Lv29 / HP5,135 unchanged; ~9 mandatory rounds
- Restraint Anchors — **POWER COMPLETE**
- Warden of the Nameless / Revision Arbiter — **VALIDATED v83 / POWER COMPLETE; current true-battle stress certification ACTIVE**: mandatory Lv30 / completionist Lv34; Lv34 / HP7,600 / ATK124 / MAG138
- Western Rift Engine — **VALIDATED v84 / RAW LINE RETAINED / POWER COMPLETE**: mandatory Lv33 / completionist Lv39; Lv36 / HP9,775 unchanged; ~10–11 mandatory rounds
- Rift Echo — **POWER COMPLETE**
- Marshal Varkesh → Rift Conqueror — **VALIDATED v84 / RAW LINES RETAINED / POWER COMPLETE**: mandatory Lv35 / completionist Lv42; HP7,326 → fresh HP8,485; ~13–15 mandatory rounds
- Equal Mercy Arbiter — **VALIDATED v85 / RAW LINE RETAINED / POWER COMPLETE**: mandatory Lv37 / completionist Lv45; Lv40 / HP10,025 unchanged; ~12–13 mandatory rounds
- Commander Rhazek — Reforged Commander → Bastion Devourer — **VALIDATED v85 / RAW LINES RETAINED / POWER COMPLETE**: mandatory Lv40 / completionist Lv49; HP8,431 → fresh HP10,462; ~14–16 mandatory rounds
- Registry Warden — **VALIDATED v86 / RAW LINE RETAINED / POWER COMPLETE**: mandatory Lv45 / completionist Lv54; Lv49 / HP13,514 unchanged; ~10–11 mandatory rounds
- Calder → Crown-Bound Living Anchor — **VALIDATED v87 / RAW LINES RETAINED / POWER COMPLETE**: mandatory Lv49 / completionist Lv59; HP10,133 → fresh HP13,662; ~15–17 mandatory rounds
- Authentication Lenses / Living Anchor Clamps — **POWER COMPLETE**
- The Custodian — **VALIDATED v87 / RAW LINE RETAINED / POWER COMPLETE**: mandatory Lv51 / completionist Lv60; Lv55 / HP16,017 unchanged; ~11–12 mandatory rounds
- Perception Node / Ruin Containment Seal — **POWER COMPLETE**
- Marshal Varkesh — Final Capture — **VALIDATED v88 / RAW LINE RETAINED / POWER COMPLETE**: mandatory Lv54 / completionist Lv64; Lv58 / HP17,106 unchanged; two-Beacon capture floor
- Varkesh final-capture supports — **POWER COMPLETE**
- Emperor Vaelkor Draeven → Sovereign Panoply Unbound — **VALIDATED v88 / HP DURATION ADJUSTED / POWER COMPLETE**: mandatory Lv56 / completionist Lv66; HP16,800 → fresh HP20,200; **18–20 mandatory rounds**
- Last Weapon Archon — **VALIDATED v89 / HP PACING ADJUSTED / POWER COMPLETE**: mandatory Lv58 / completionist Lv69–70; Lv63 / HP20,800; **15–17 mandatory rounds**
- Reconstituted Entity → The Last Command — **VALIDATED v89 / HP PACING ADJUSTED / POWER COMPLETE**: mandatory Lv61 / completionist Lv70; HP22,500 → fresh HP28,500; ~22–24 mandatory rounds
- Heart Manifestation / Unbound Shards — **POWER COMPLETE**
- mandatory story-boss route recertification — **COMPLETE THROUGH FINAL BOSS**
- direct-damage enemy/boss Power audit — **CLOSED**
- Chapter 1 ordinary/Elite/authored enemy batch — **PASS**
- Chapter 0 — **PASS**; Riftmaw retained; S001/S002/S005 encounter order and remaining kits reconciled
- Chapter 2 ordinary/Elite/authored batch — **PASS**
- Memory Scribe / Archive Duplicant copy conversion — **POWER COMPLETE / BOUNDED**
- Hold the Junction — **PASS / one fixed four-body encounter / no second wave**
- Chapter 3 ordinary enemies / S018 lawful encounters / Grand Inquisitor Frame — **MAIN BATCH PASS**
- False-Warrant Adept — **OPEN placement/role; retained but not spawned without evidence**
- Chapter 4 ordinary / Annex Duelist / protected Annex roster — **PASS**
- Elemental Researcher / Annex Battle Mage / Crucible Attendant — **Power-complete; no random spawn / no invented mandatory placement**
- Freeze rollout — **Chapter 4 confirmed**
- Chapter 5 ordinary enemies / Ruin Forgemaster — **PASS**
- Highland Resistance Fighter — **Power-complete nonlethal kit; exact Chapter-5 story placement remains open**
- Chapter 6 ordinary enemies / Crimson Progenitor — **PASS**
- Weather Crown Shield Guard / Blood Husk / Perfected Soldier — **Power-complete / exact placement bounded**
- Chapter 6 firewall — **no Wind/Water element; no Poison/Blood status**
- Chapter 7 ordinary enemies / First Registrar's Shade — **PASS**
- Beast Handler + Bound Rift Hound / Resistance Saboteur / Controlled Prisoner / Command-Seal Warden — **Power-complete / placement bounded**
- Prison identity-system firewall — **no permanent player-state erasure**
- Chapter 8 ordinary enemies / Conqueror Legate — **PASS**
- Chapter 8 authored/protected roster — **none; no Western Rift/Westguard special identities invented**
- Chapter 8 firewall — **no Spatial element/grid/rows/adjacency/extra actions/command reading**
- Chapter 9 ordinary/carryover enemies / Ruin Breach Captain — **PASS**
- Mercy Warden / Relay-Fever Patient — **Power-complete nonlethal authored identities**
- Relay-Fever Patient — **never random / stabilization outcome / no death presentation**
- Chapter 10 reused ordinary enemies — **PASS / 8 reused / 0 new**
- Chapter 10 optional Elite — **none / intentional**
- Registry Warden handoff — **verified unchanged / Power-complete / status-neutral**
- Chapter 11 ordinary enemies / Perfect Administrator — **PASS**
- Crown Engine Technician — **Power-complete nonlethal / placement bounded**
- Face-name firewall — **enemy Might/Elements/Grace/Perception/Memory/Ruin naming does not grant Card/Prime use**
- Chapter 12 ordinary enemies / Lord-Marshal Kharvek — **PASS**
- Compelled Relay Bearer — **Power-complete nonlethal / never random / compulsion story-owned**
- civilian firewall — **civilian populations are not default enemies**
- Chapter 13 ordinary enemies / Devourer of Names — **PASS**
- final Last Weapon/Entity support handoff — **verified unchanged**
- numbered-chapter broad enemy audit — **Chapters 1–13 complete**
- broad chapter-enemy Power audit — **Chapters 0–13 complete**


## Enemy/boss difficulty validation
Historical v75–v89 balance task — **COMPLETED**:
> Mandatory-vs-completionist validation across ordinary enemies, Elites, story bosses, Regional Hunts, Major Hunts, authored encounters, formations, and supports.

This is a difficulty/tuning pass, **not** a reopened Power-authoring audit. Existing Power values remain closed unless a specific encounter fails validation and requires targeted tuning.


## Direct-damage Power completeness
Hard gate:
> every direct-damage action must have explicit numeric Power before its kit can be called complete.

Base Classes are now Power-complete.
Current Subclass, Standard Card, and Prime direct-damage rows remain Power-complete.
Enemy/boss action sheets have passed this gate across Chapters 0–13 and all Hunts. Reopen Power authoring only when a specific kit is explicitly revised or playtest-driven tuning demonstrates that a specific coefficient must change.


## Hunt Power status
- Regional Hunts #1–#11 — **POWER COMPLETE**
- RH10/RH11 supports — **exact / Power N/A**
- Major Hunts #1–#6 — **POWER COMPLETE**
- whole Hunt direct-damage Power audit — **COMPLETE**


## v76 Chapter 0 difficulty validation
- Chapter 0 mandatory-vs-completionist validation — **ADJUSTED / VALIDATED**.
- Chapter 0 has no meaningful completionist divergence before mandatory combat resolves.
- Mandatory Cyanis baseline now explicitly includes **3 Field Salves** as finite story-issued inventory.
- Riftmaw HP changed **760 → 340** after actual Lv1 Cyanis throughput check.
- Riftmaw ATK/MAG/DEF/Spirit/Speed and all action Powers remain unchanged.
- exact Lv1–70 natural-stat formula restored to `10_PROGRESSION_AND_EXP/NATURAL_STAT_CURVE.md`.
- guaranteed Chapter-0 loadouts recorded in `08_ITEMS_AND_EQUIPMENT/STARTING_LOADOUTS.md`.
- v76 next frontier was Chapter 1 ordinary formations / Watch Captain Frame / authored content / Regional Hunt #1; **that frontier is completed by v77 below**.


## v77 Chapter 1 difficulty validation
- Chapter 1 mandatory-vs-completionist validation — **ADJUSTED / VALIDATED**.
- Validation uses actual **Lv1 chapter start → Lv5 chapter end** progression rather than a flat Lv5 reference.
- S008 Hollow Watch reference remains ~Lv2 mandatory / ~Lv3 high-side.
- Chapter-1 ordinary enemies, Sentry/Ballista teaching pair, Briarhide nonlethal encounter, Hollow Watch Castellan, and Cistern Devourer all validate without direct-damage Power changes.
- Watch Captain Frame HP changed **820 → 500** to restore its 2–4 serious-round Optional-Elite role at actual Lv2–3 access.
- Cistern Devourer remains fixed **Lv7 recommended** despite becoming available after S011 at roughly Lv5; the early-access challenge gap is intentional.
- next validation frontier = **Chapter 2, Lv5 start → Lv9 end** with encounter-specific internal anchors.


## v78 encounter-balance checkpoint
- Chapter 1 documentation corrected to explicitly count Maevra as a real active guest; Watch Captain Frame 500 HP and Cistern Devourer 2,706 HP remain validated.
- Chapter 2 mandatory-vs-completionist validation complete at **Lv5 start → Lv9 end** with Cyanis + Ilyra + Torren + Maevra.
- Archive Duplicant, Rhazek, Hold the Junction, and Transfer Executioner retain current raw/Powers.
- Archive Leviathan Recorded Pattern v97 closure: a visible Pattern forms only when the same actor repeats the same exact eligible direct-damage action on consecutive offensive actions; later repeats while active deal 20% less final direct damage; 2 rounds State A / 1 round Emergent; same-bar emergence at 45% HP.
- Global direct-damage Power audit remains closed.
- Next validation frontier: Chapter 3.


## v79 Chapter 3 difficulty validation
- Chapter 3 mandatory-vs-completionist validation — **ADJUSTED / VALIDATED** on actual **Lv9 start → Lv13 end** progression.
- S018 lawful confrontations validated at Lv9 with Cyanis + Ilyra + Torren + Maevra.
- Nimera joins in S019; thereafter five combatants are available (four permanent + Maevra guest) with **four active maximum**.
- Accepted Chapter-3 random formation compositions/weights recovered into the owning enemy folder; old raw-stat/EXP rows remain retired.
- Grand Inquisitor Frame HP corrected **1,450 → 1,200** for true Lv9–10 first access; all action Powers and all other raw stats retained.
- First Command Warden retained at Lv14 / 2,850 HP after Lv11 mandatory and Lv12–13 completionist checks.
- Archive Judgment Engine retained at Lv15 / 4,928 HP / recommended Lv15.
- False-Warrant Adept remains an explicit placement dependency, not a Power gap.
- Global direct-damage Power audit remains closed.
- **Next validation frontier: Chapter 4.**

## v80 Chapter 4 difficulty validation
- Chapter 4 mandatory-vs-completionist validation — **PASS / VALIDATED** on actual **Lv13 start → ~Lv15 middle → Lv17 end** progression.
- Maevra is not the default Chapter-4 traveling fifth and is not used as a Chapter-4 balance assumption.
- Vaelira joins permanently after S022; five permanent characters are then available with **four active maximum**.
- Accepted Reaction Annex opening/middle/late formation compositions and weights restored into `09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_04_FORMATIONS.md`; superseded historical enemy-stat / formation-EXP rows were not restored.
- Chapter-4 ordinary roster — **PASS / RETAIN**.
- Annex Duelist — **PASS / RETAIN Lv18 / 1,700 HP**.
- Elder Briarhide — **PASS / retained fixed 4-round authored structure**.
- Reaction Conduit — **PASS / RETAIN 2,400 HP**.
- Regulation Crucible → The Seventh Reaction — **PASS / RETAIN 2,400 HP core + fresh 2,900 HP Form II**.
- Crown Prototype — **PASS / RETAIN Lv20 recommendation / 6,503 HP**; early Lv17–18 access remains intentionally below recommendation.
- Elemental Researcher / Annex Battle Mage / Crucible Attendant remain **OPEN placement dependencies** and must not be random-spawned or given invented mandatory placements.
- **No raw-stat or direct-damage Power change in v80.**
- **Next validation frontier: Chapter 5.**


## v84 Chapter 8 difficulty validation
- Chapter 8 mandatory-vs-completionist validation — **PASS / VALIDATED**.
- Route anchors: **Lv32 start → Lv33 Western Rift Engine → Lv35 Varkesh → Lv37 end**.
- Six permanent characters available; active battle party remains four.
- Subclass access is legal throughout Chapter 8.
- Chapter-8 ordinary enemies and rare Conqueror Executioner retain current raw stats/Powers.
- Conqueror Legate retained at Lv38 / 3,650 HP.
- Western Rift Engine retained at Lv36 / 9,775 HP; finite Rift Echo and 45% same-bar Incarnate state retained.
- Marshal Varkesh retained at Lv38 / 7,326 HP → fresh Rift Conqueror Lv39 / 8,485 HP; the historical fresh-form Prime-refresh assumption is **retired** — fresh Form II does not restore spent Prime identities under current Prime rules.
- Regional Hunt #8 Rift Siege Beast retained at recommended Lv44 / 15,875 HP.
- Major Hunt #2 recertification carried forward as a legitimate Chapter-8 completionist progression source.
- No numerical or direct-damage Power changes.
- [v84 historical note; **formation portion CLOSED v90**] RH8 within-chapter timing remains story-owned.
- Chapter 9 is subsequently validated in v85; see the v85 section below.


## v85 Chapter 9 difficulty validation
- Chapter 9 mandatory-vs-completionist validation — **PASS / VALIDATED**.
- Route anchors: **Lv37 start → Lv37 Equal Mercy → Lv38 post-Last-Sanctuary → Lv40 Rhazek → Lv42 end**.
- Six permanent characters available; active battle party remains four; Subclasses are legal throughout.
- Chapter-9 ordinary enemies retain current raw stats/Powers.
- Mercy Warden and Relay-Fever Patient retain their authored nonlethal/stabilization resolutions and medical-story firewalls.
- Ruin Breach Captain retained at Lv44 / 4,350 HP.
- Equal Mercy Arbiter retained at Lv40 / 10,025 HP with 45% same-bar Open Sanctuary transition.
- Commander Rhazek retained at Lv43 / 8,431 HP → fresh Bastion Devourer Lv44 / 10,462 HP; the historical fresh-body Prime-refresh assumption is **retired** — fresh bodies do not restore spent Prime identities under current Prime rules.
- Regional Hunt #9 Mercyfallen Behemoth retained at recommended Lv50 / 18,882 HP.
- Major Hunt #3 Concordance Guardian retained at post-Ch9 recommended Lv54 / 27,400 HP.
- Rhazek completionist comparison is robust to unresolved RH9 timing: **Lv48 without RH9 / Lv49 with RH9**.
- No numerical or direct-damage Power changes.
- [v85 historical note; **formation portion CLOSED v90**] RH9 exact S### return trigger remains story-owned.
- superseded by v86 Chapter-10 validation below.


## v86 Chapter 10 difficulty validation
- Chapter 10 mandatory-vs-completionist validation — **PASS / VALIDATED**.
- Mandatory anchors: **Lv42 start → Lv45 Registry Warden → Lv46 post-Warden → Lv47 clear**.
- Completionist fixed-content anchors: approximately **Lv51 start → Lv54 Registry Warden → Lv55 clear**.
- Six permanent characters available; active battle party remains four; Subclasses are legal throughout.
- All eight reused Chapter-10 ordinary bodies retain current stats/Powers.
- [v86 historical note; **CLOSED v90**] Eastern Forest formations are recovered and missing migrated per-action percentages now use the active fallback rule.
- Registry Warden retained at Lv49 / 13,514 HP and promoted to **FORMALLY VALIDATED v86**.
- Major Hunt #4 Worldscar Leviathan retained at recommended Lv60 / 38,800 HP and promoted to full two-baseline **FORMALLY VALIDATED v86**.
- [v86 historical note; **CLOSED v90**] Old Relay Warden now has an exact current raw/action/AI sheet.
- No numerical or direct-damage Power changes.
- next validation frontier: **Chapter 11 — Lv47 start → Lv52 end**.


## v90 enemy static completion
- **Enemy static design — CLOSED.**
- Character Quest combat bosses: exact sheets complete for Vaelira, Cyanis, Seyrik, and Torren; Nimera/Ilyra remain no-boss quests by design.
- Chapter 1–13 formation compositions are present in `09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/`; Chapter 0 is authored/tutorial-only.
- Recovered formation weights are restored, including Ch12/Ch13 30/45/25 and Ch10 20/55/25 tier weights.
- All targetable support objects/components have current numerical bodies and explicit Power or `Power: N/A`.
- Missing migrated per-action percentages are no longer an implementation blocker: `09_ENEMIES_AND_ENCOUNTERS/ACTION_SELECTION_DEFAULT.md` supplies uniform selection among currently eligible actions after all forced/eligibility/lock rules; explicit owning-file weights override it.
- Exact placement of bounded authored identities and exact within-chapter Hunt return triggers remain **story integration**, not enemy-design incompleteness.
- Runtime duration/resource QA remains under `16_BALANCE_AND_TESTING`; MH6 runtime duration is especially retained as a QA gate.
- **CEXP recalibration — CLOSED v92 (v91 budgets retained; recruitment arithmetic corrected). Next balance task: build canonical mandatory/completionist party snapshots and run representative true-battle simulations.**


## v94 status synchronization
Closure bookkeeping synchronized after v93. No combat values changed. Representative true-battle suite remains active.


## v95 Bleed magnitude update
- Bleed = **3% Max HP per qualifying proc**.
- Cadence unchanged: round tick + action tick; extra actual actions each qualify.
- Existing application chances and clear rules unchanged.
- Regional Hunt Bleed magnitude conversion remains 75%; Major Hunt / mandatory boss conversion remains 50%.
- Hollow Watch's v93 normal/smart certification remains valid; aggressive Bleed-risk metrics are marked superseded pending v95 refresh.


## v96 Bleed escalation update
- Bleed starts at **3% Max HP per qualifying proc**.
- After the affected unit completes **3 turns uncleared**, the same Bleed escalates to **4% Max HP per qualifying proc** until removed.
- Reapplication while active does not reset the escalation clock; removal and later reapplication starts a fresh 3% Bleed.
- Regional Hunt conversion: **2.25% → 3%**; Major Hunt / mandatory boss: **1.5% → 2%**.
- Application chances, cadence, and clear rules remain unchanged.


## v97 Archive Leviathan true-battle certification
- Mandatory Lv6 prepared: **100% wins / median 10 / mean 10.05 / 0.05% any-KO** across 20,000 runs.
- Completionist/high-side Lv7 prepared: **100% wins / median 9 / mean 8.58 / 0% any-KO** across 20,000 runs.
- No Leviathan HP, raw stat, status chance, or direct-damage Power changed.
- Recorded Pattern deterministic trigger closed for implementation.
- Blue Warden Clear Warding migration omission restored: **+5 Status Resistance for 2 rounds** after cleansing.

## v99 Regulation Crucible true-battle certification
- Regulation Crucible → The Seventh Reaction is **PASS / RETAIN** at **2,400 HP core + fresh 2,900 HP Form II**.
- Strict prepared mandatory Lv15 benchmark with no Prime: **100% wins / median 18**.
- The same benchmark using the one legal Recovered Last Sentinel use: **100% wins / median 14**.
- Chamber control remains tactically meaningful by sharply reducing harmful-status pressure rather than merely shortening the fight.
- Fresh Form II does **not** restore a spent Prime identity.
- No boss HP, raw stat, status chance, or direct-damage Power changed.
- Current representative true-battle anchor: **Warden of the Nameless / Revision Arbiter**.
