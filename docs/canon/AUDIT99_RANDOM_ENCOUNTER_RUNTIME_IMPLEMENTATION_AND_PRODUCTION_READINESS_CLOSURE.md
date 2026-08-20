# Audit99 — Random-Encounter Runtime Implementation and Production-Readiness Closure

**Authority:** Diyse: HD-2D JRPG Clean Active Complete Master Canon **v1.84 / Audit99**  
**Date:** August 20, 2026  
**Status:** **LOCKED / CONTROLLING** for the implemented Audit98 random-encounter runtime architecture, Chapter 1–4 executable formation-runtime status, area-tuning contract, transition semantics, transient encounter handoff behavior, and the current production-readiness boundary for enemy and item work.

Audit99 inherits all compatible v1.83/Audit98, v1.82/Audit97, v1.81/Audit96, v1.80/Audit95, v1.79/Audit94, v1.78/Audit93, and earlier canon unless explicitly clarified below.

## 0. Authority contract

Audit99 does **not** change the story, chapter structure, world map, party roster, level cap, Hunt identities, Hunt unlock gates, Prime rewards, EXP economy, encounter-count targets, or the Audit98 random-encounter probability curve.

It closes the implementation status created after Audit98 and establishes what is now actually executable in the repository versus what remains open production work.

Where a prior implementation-facing note still says a runtime feature is unimplemented but Audit99 says it is implemented, **Audit99 controls**.

## 1. Repository implementation chain now established

The current Audit98 encounter runtime is implemented through the following full engineering-proof chain:

**resolved player movement**  
→ **eligible horizontal travel distance**  
→ **area world-distance / S conversion**  
→ **hidden Audit98 encounter pressure**  
→ **Light / Standard / Heavy tier selection**  
→ **weighted legal local formation**  
→ **immediate exact-repeat suppression**  
→ **transient random-encounter payload**  
→ **generated 1–8-enemy battle state**  
→ **victory / engineering successful-flee return**  
→ **field return with correct pressure restoration**

This chain is implemented and regression-tested.

## 2. Audit98 runtime foundation — implemented

The repository now contains an executable balance/runtime layer for:

- the approximately **210 expected campaign ordinary-random-encounter center**;
- all 12 chapter encounter-count centers;
- chapter Light / Standard / Heavy weights;
- chapter formation-size grammar;
- the **8 simultaneously active enemy maximum**;
- chapter ordinary-formation EXP anchors;
- the Chapter-5-onward Audit98 EXP curve;
- hidden eligible-distance encounter pressure;
- weighted local formation selection;
- exact immediate-repeat suppression where alternatives exist.

The implementation must continue to reproduce the locked Audit98 cumulative EXP milestones exactly.

### 2.1 EXP rounding implementation lock

The runtime must use deterministic **round-half-to-even to the nearest 100 EXP** for the Audit98 late-game level-up-cost calculation.

This implementation detail is locked because Godot's default `.5` rounding behavior produced a 100-EXP drift beginning at Level 54 during CI validation.

The accepted runtime reproduces the canon milestones exactly, including:

- L53 = **312,400**;
- L54 = **326,000**;
- L55 = **340,000**;
- L60 = **415,400**.

Audit98's formula itself is unchanged.

## 3. Eligible movement source — implemented

Encounter pressure is fed by **actual resolved horizontal displacement after collision resolution**.

Therefore:

- desired input alone does not count;
- held movement time alone does not count;
- attempted wall-pushing with zero displacement does not count;
- vertical-only displacement does not count;
- movement-disabled displacement does not count;
- actual horizontal travel does count.

This preserves Audit98's distance-based encounter rule in real movement code rather than approximating it from input or frame time.

## 4. Reusable field encounter controller — implemented

A shared field encounter controller owns:

- one encounter-pressure state;
- one formation selector;
- current chapter context;
- current random-area ID;
- world-units-per-S tuning;
- enable/disable state;
- authored pause state;
- battle-active latch;
- previous formation ID;
- pending random-battle payload.

It is responsible for converting eligible movement into normalized S distance and requesting a legal random formation when pressure triggers.

It does **not** own final battle resolution, enemy stat design, or final map geometry.

## 5. Battle-return state behavior — implemented

### Victory

A random-encounter victory:

- clears the active battle request;
- resets encounter pressure;
- preserves immediately previous formation identity for anti-repeat behavior.

### Successful flee

The current engineering-successful-flee return:

- resumes near **0.65S** effective pressure;
- preserves **0.20S** grace;
- preserves immediately previous formation identity.

The final player-facing flee-success formula/UI remains open.

### Failed flee attempt

A failed flee attempt does not reset accumulated pressure and does not end the current battle.

### Safe reset

A true safe reset:

- clears pressure;
- clears transition grace;
- clears anti-repeat history.

## 6. Area encounter tuning contract — implemented

Area-level encounter configuration must use the reusable area encounter-tuning contract rather than hardcoding chapter/area/S values into each field scene.

The tuning contract includes:

- tuning ID;
- chapter;
- random-area ID;
- world-units-per-S;
- random-encounter enabled state;
- entry transition mode;
- calibration state.

### 6.1 Calibration states

Supported states are exactly:

1. `engineering_only`
2. `awaiting_geometry`
3. `production_calibrated`

An encounter-enabled area may not remain `awaiting_geometry`.

This prevents guessed S-distance values from silently becoming production balance.

## 7. Area transition semantics — implemented

### Same ecology

- preserve current pressure;
- add no ecology-transition grace;
- preserve anti-repeat history.

### New ecology

- preserve current pressure;
- switch to the new legal local formation table;
- add **0.10S transition grace**;
- preserve anti-repeat history.

### Safe reset

- reset pressure;
- clear grace;
- clear anti-repeat history.

The 0.10S ecology-transition grace is separate from, and does not replace, the successful-flee 0.20S grace.

## 8. Transient field → combat → field handoff — implemented

Random encounters use runtime-only transient encounter state for the current proof/runtime handoff.

Transient state:

- carries the generated random payload into combat;
- carries victory/flee/defeat proof results back to the field;
- is **not serialized** into disk saves;
- is cleared when a save is loaded so stale encounter state cannot resurrect.

No save-schema bump is created by this transient bridge.

Encounter-pressure save persistence remains a separate future decision.

## 9. Generated random battle-state contract — implemented

The generated battle adapter accepts legal random formations with **1–8 active enemies**.

It:

- rejects empty formations;
- rejects formations above 8 active enemies;
- rejects malformed/nonpositive-HP executable enemy definitions;
- preserves the accepted four-member proof party;
- preserves the existing Card/Prime regression path;
- carries the formation's generated EXP reward;
- retains the formation ID.

The historical deterministic `setup_demo()` combat proof remains preserved as a separate regression path.

## 10. Chapter 1–4 executable random-formation status

The current repository contains weighted Light / Standard / Heavy random-formation catalogs for exactly these 10 Chapter 1–4 combat areas:

### Chapter 1
- Brackenwall — `ch01_brackenwall`
- Greenhollow — `ch01_greenhollow`
- Hollow Watch — `ch01_hollow_watch`

### Chapter 2
- Dunmere / Waterworks — `ch02_dunmere_waterworks`
- Sunken Archive — `ch02_sunken_archive`
- Red Transfer Bastion — `ch02_red_transfer_bastion`

### Chapter 3
- Way-Fort — `ch03_way_fort`
- Suppressed Archives — `ch03_suppressed_archives`
- Command Station — `ch03_command_station`

### Chapter 4
- Reaction Annex — `ch04_reaction_annex`

These catalogs:

- use Audit90-approved ordinary/carryover identities for their local ecology;
- exclude Elites, Hunts, bosses, authored lawful/victim human encounters, and named non-random encounters;
- obey the chapter active-enemy maximum;
- use the Audit98 chapter whole-formation EXP anchors;
- provide at least two weighted alternatives per implemented local tier so anti-repeat behavior can function.

The exact local catalogs are current implementation authority for Chapters 1–4 unless later audited and superseded.

## 11. Current proof-only enemy combat data boundary

Only the small subset of enemy executable stat data required by the current Greenhollow engineering proof is presently instantiated as proof combat data.

Current proof identities include:

- Greenhollow Stalker;
- Thornvine Creeper;
- Briar Boar.

Their proof HP/MP/speed and related executable constants are **ENGINEERING ONLY / NON-CANON / NOT FINAL BALANCE**.

Audit99 explicitly prohibits treating those proof values as final enemy stats merely because they are executable.

## 12. Production traversal-scene readiness boundary

As of Audit99, the repository does **not** yet contain Chapter 1–4 production traversal `.tscn` maps with final authored geometry suitable for real encounter-spacing calibration.

Therefore:

- no production `world_units_per_s` values are locked yet;
- no guessed production spacing may be promoted from the proof harness;
- the current Greenhollow **20 world units = 1S** value remains engineering-only;
- production S-distance values must be measured/calibrated after real traversal geometry exists.

This is a deliberate production boundary, not a missing design decision.

## 13. Enemy production status — current master boundary

Enemy **architecture and identity planning** are substantially closed by Audits 90, 93, 94, 95, 96, and 98.

The remaining enemy work is primarily production implementation and balance.

### 13.1 Closed / inherited

The following remain controlling:

- whole-game enemy identity/role architecture from Audit93;
- exactly 11 Regional Hunts;
- exactly 6 Major Hunts;
- exactly 17 Hunt-class optional encounters;
- Elite / Hunt / mandatory-boss category separation;
- fixed authored encounter strength with no dynamic level scaling;
- 8 simultaneously active enemies maximum;
- Audit94 reuse/palette-material production strategy;
- Audit98 campaign and Hunt EXP economy;
- Chapter 1–4 local random-formation catalogs listed above.

### 13.2 Still open / not final canon

The following are **not yet globally finalized** unless a narrower earlier canon source explicitly locks a particular value:

- final ordinary-enemy HP / Attack / Defense / Magic / Spirit / Speed constants;
- final ordinary-enemy move kits;
- final enemy AI priorities and reactions;
- final elemental/status weakness and resistance tables;
- final drop/material tables;
- final gold rewards where applicable;
- final Chapters 5–12 random-formation catalogs;
- final Elite executable stat/AI packages;
- final Regional-Hunt executable stat/AI packages;
- final Major-Hunt executable stat/AI packages;
- final mandatory-boss executable stat/AI packages;
- final enemy battle sprites, animations, hit/death sets, and VFX hookup;
- target-device performance tuning for 4-party + 8-enemy VFX-heavy encounters.

These remain the correct enemy production frontier.

## 14. Item/equipment production status — current master boundary

Audit99 does **not** invent or silently lock a new item catalog.

All compatible previously locked equipment-system rules remain inherited, including:

- open equipment and persistent unlocked abilities;
- Subclass selection controlling stat package, Trait, and Subclass-only abilities rather than erasing unlocked gear access;
- donor / Legacy architecture already locked elsewhere;
- Legacy equipment bonuses applying to any legal wearer;
- Nimera's Conduit weapon concept;
- Torren Routeweaver inheritance of the relevant Nimera Base equipment concept;
- Cards remaining a separate system from normal inventory/equipment.

However, the **production item catalog and economy are still open** unless a specific earlier canon entry explicitly locks an individual item.

The next item audit must therefore determine and lock, at minimum:

- master item taxonomy;
- total practical item-count target;
- consumable families and tiers;
- weapon progression by legal equipment family;
- armor progression;
- accessory progression;
- Conduit catalog;
- Legacy equipment exact production stats where still open;
- materials and enemy-drop economy;
- shop inventories and price progression;
- treasure/chest reward distribution;
- sell values;
- item-use restrictions;
- status-cure inventory coverage;
- Hunt/boss non-EXP item rewards;
- crafting/upgrade rules only if such a system remains desired after audit;
- item IDs, icons, descriptions, sorting/category tags, and save/runtime schema.

No assumed 300-item-style catalog, crafting system, or shop economy is canon merely from genre convention.

## 15. Current production order after Audit99

Recommended sequence:

1. establish the first reusable **production traversal-scene shell**;
2. prove one Chapter 1 production area on authored geometry;
3. calibrate its first real production `world_units_per_s`;
4. attach the existing local formation table through production-calibrated area tuning;
5. build the ordinary-enemy production combat-data schema and final-stat methodology;
6. populate Chapters 1–4 ordinary enemy production data;
7. author Chapters 5–12 local formation catalogs;
8. implement Elites, Hunts, and mandatory bosses;
9. perform full-game enemy balance and Android performance passes;
10. run the dedicated **item/equipment catalog and economy audit** before broad item implementation.

The item audit may be started earlier as a parallel design pass, but broad item implementation should not precede a locked item taxonomy/economy authority.

## 16. Repository implementation lineage captured by this closure

Audit99 formally recognizes the merged implementation sequence that followed Audit98:

- PR #60 — Audit98 encounter runtime foundation;
- PR #61 — reusable Audit98 field encounter controller;
- PR #62 — live resolved-movement encounter feed;
- PR #63 — generated random-encounter battle-state contract;
- PR #64 — transient field → combat → field random-encounter loop;
- PR #65 — reusable area encounter-tuning contract and ecology-transition semantics.

These implementation milestones are now part of the current master-canon production state rather than unrecorded post-Audit98 engineering history.

## 17. Supersession / clarification summary

Audit99 supersedes only stale implementation-status statements that said the following were not yet implemented:

- live eligible-distance feeding from resolved movement;
- reusable field encounter controller;
- generated random-formation battle-state initialization;
- transient field/combat/field random handoff;
- area encounter-tuning Resource contract;
- ecology-transition grace behavior.

Audit99 does **not** supersede Audit98's numeric progression/economy authority.

## 18. Final lock

The project now has a tested random-encounter runtime architecture through the engineering field/combat loop and a production-safe area-tuning contract.

The next major unresolved gameplay-content domains are:

- production traversal geometry;
- final enemy combat data/AI/visual implementation;
- Chapters 5–12 formation catalogs;
- full item/equipment catalog and economy.

These are open production frontiers, not gaps to be filled by unstated assumptions.
