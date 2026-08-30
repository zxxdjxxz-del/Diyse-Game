# Diyse — Final Consolidation Validation

## Structure
- numbered active domains 01–16 present — PASS
- `90_WORKING` present — PASS
- `99_ARCHIVE` present — PASS
- migration-only v1 organization plan removed from active control — PASS
- full batch migration log removed from active control — PASS
- historical copies preserved in archive — PASS

## Active-control cleanup
- `DIYSE_MASTER_INDEX.md` no longer says reorganization is in progress — PASS
- stale post-migration `Then:` sequence removed — PASS
- current project structure added — PASS
- current terminology glossary added — PASS
- retired terminology map added — PASS
- source authority manifest added — PASS
- open/pending work consolidated — PASS
- active canon changelog added — PASS

## Canon integrity
- exact duplicate Markdown file groups: **0** — PASS
- active authority precedence made explicit — PASS
- archive made explicitly non-authoritative — PASS
- working layer made explicitly non-canonical until promotion — PASS
- [SUPERSEDED BY v91] v74/v75 CEXP timing notes are historical; v91 formally recalibrates normal-route full Base + Subclass completion to **~Lv55–60** — PASS
- final music remains OPEN — PASS
- exact image/map binaries not fabricated — PASS

## Domain Markdown counts — current v91
- `00_MASTER_CONTROL`: **12**
- `01_CHARACTERS`: **34**
- `02_STORY`: **31**
- `03_DIALOGUE`: **66**
- `04_WORLD_AND_LORE`: **29**
- `05_BATTLE_SYSTEM`: **13**
- `06_CLASSES_AND_ABILITIES`: **25**
- `07_CARDS`: **33**
- `08_ITEMS_AND_EQUIPMENT`: **38**
- `09_ENEMIES_AND_ENCOUNTERS`: **272**
- `10_PROGRESSION_AND_EXP`: **27**
- `11_QUESTS`: **28**
- `12_ECONOMY_AND_REWARDS`: **27**
- `13_UI_AND_IMPLEMENTATION`: **35**
- `14_ART_AND_VISUALS`: **31**
- `15_AUDIO_AND_MUSIC`: **26**
- `16_BALANCE_AND_TESTING`: **60**
- `90_WORKING`: **10**
- `99_ARCHIVE`: **6**
- root Markdown: **2**

## High-risk retired-term scan
- unclassified active-context hits: **0** — PASS


## v82 package check
- Chapter-6 mandatory/completionist validation file present — PASS
- Chapter-6 boss/Hunt status handoffs synchronized — PASS
- Direct-damage Power audit remains closed — PASS
- Markdown file count in v82 package: **780**


## v83 package check
- Chapter-7 mandatory/completionist validation file present — PASS
- Chapter-7 boss/Elite/Hunt status handoffs synchronized — PASS
- Sixfold Volition excluded from pre-Volition Chapter-7 combat baseline — PASS
- Direct-damage Power audit remains closed — PASS
- exact duplicate Markdown file groups: **0** — PASS
- Markdown file count in v83 package: **781**


## v91 package check
- Enemy static design remains closed — PASS
- Prime loadout access restored to **1 slot pre-Volition / 2 slots post-Volition** — PASS
- CL13 threshold remains **6,000 CEXP** — PASS
- mandatory-route class completion target **~Lv55–60** — PASS
- optional CEXP exact ledger **1,000 before MH6 / 1,075 including MH6** — PASS
- Ch12 ordinary CEXP pool **450** and formation bands synchronized — PASS
- Ch13 ordinary CEXP pool **370** and formation bands synchronized — PASS
- exact duplicate Markdown groups: **0** — PASS
- next certification task: canonical party snapshots + representative true-battle simulations


## v92 recruitment-aware CEXP package check
- v91 campaign CEXP budgets retained — PASS
- no retroactive pre-recruitment CEXP — PASS
- corrected Volition centers: Torren 5,350 / Vaelira 5,250 / Cyanis-Ilyra 4,950 / Nimera 4,500 / Seyrik 3,500 — PASS
- mandatory full Base + Subclass completion ~Lv56–60, inside Lv55–60 target — PASS
- pre-Volition optional ceiling does not force Base CL13 overflow — PASS
- next task remains canonical boss-test snapshots + representative true battles


## Bleed magnitude authority — v95
- `05_BATTLE_SYSTEM/STATUS_EFFECTS.md` owns the current **3% Max HP per qualifying proc** Bleed magnitude.
- Existing Bleed application chances remain encounter-owned and unchanged.
- True-battle tests from v95 forward must use the new magnitude.


## Bleed escalation authority — v96
- `05_BATTLE_SYSTEM/STATUS_EFFECTS.md` owns the current escalation rule: **3% Max HP/proc initially → 4% after 3 affected turns uncleared**.
- High-rank conversions remain proportional: Regional Hunts **2.25% → 3%**; Major Hunts / mandatory bosses **1.5% → 2%**.
- Existing Bleed application chances remain encounter-owned and unchanged.
- True-battle tests from v96 forward must use the escalation rule.
