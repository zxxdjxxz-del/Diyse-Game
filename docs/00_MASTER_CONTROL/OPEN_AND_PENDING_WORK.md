# Diyse — Open & Pending Work

This is the cross-domain index of work that remains genuinely unresolved after the folder reorganization and v75 cleanup.

## Priority 1 — Enemy static completion — COMPLETE v90
Owner:
`09_ENEMIES_AND_ENCOUNTERS` + `16_BALANCE_AND_TESTING`

Status boundaries:
- direct-damage Power authoring audit — **CLOSED**;
- Chapters 0–13 enemy Power coverage — **COMPLETE**;
- Regional Hunts #1–#11 Power coverage — **COMPLETE**;
- Major Hunts #1–#6 Power coverage — **COMPLETE**;
- mandatory story-boss route recertification — **COMPLETE AS PRELIMINARY BOSS CALIBRATION**;
- whole-roster mandatory-vs-completionist planned paper validation — **COMPLETE THROUGH CHAPTER 13 / v89**; targeted data/runtime QA dependencies remain.
- Chapter 0 mandatory-vs-completionist validation — **ADJUSTED / VALIDATED in v76**.
- Chapter 1 mandatory-vs-completionist validation — **ADJUSTED / VALIDATED in v78 Maevra-corrected form**; Watch Captain Frame HP **820 → 500** confirmed with Maevra; Cistern Devourer retained with four-person party.
- Chapter 2 mandatory-vs-completionist validation — **ADJUSTED / VALIDATED in v78**; all direct-damage Powers retained; Archive Leviathan Recorded Pattern exact details + 45% threshold closed.
- Chapter 3 mandatory-vs-completionist validation — **ADJUSTED / VALIDATED in v79**; Grand Inquisitor Frame HP **1,450 → 1,200**; current ordinary Powers, First Command Warden, and Archive Judgment Engine retained; False-Warrant Adept remains a placement dependency.
- Chapter 4 mandatory-vs-completionist validation — **PASS / VALIDATED in v80**; no raw-stat or Power changes; Reaction Annex formations restored; protected Annex staff remain placement dependencies.
- Chapter 5 mandatory-vs-completionist validation — **PASS / VALIDATED in v81**; formations restored v90; Highland Resistance Fighter placement remains story-owned.
- Chapter 6 mandatory-vs-completionist validation — **PASS / VALIDATED in v82**; formations restored v90; authored-special placements remain story-owned.
- Chapter 7 mandatory-vs-completionist validation — **PASS / VALIDATED in v83**; formations restored v90; authored-special placements remain story-owned.
- Chapter 8 mandatory-vs-completionist validation — **PASS / VALIDATED in v84**; formations restored v90; RH8 within-chapter timing remains story-owned.
- Chapter 9 mandatory-vs-completionist validation — **PASS / VALIDATED in v85**; formations restored v90; RH9 timing remains story-owned; Major Hunt #3 recertification carried forward.
- Chapter 10 mandatory-vs-completionist validation — **PASS / VALIDATED in v86**; Eastern Forest formations restored v90; Old Relay Warden exact sheet closed v90; absent migrated action percentages use the active fallback rule.
- Chapter 11 mandatory-vs-completionist validation — **PASS / VALIDATED in v87**; approved formations retained; absent migrated action percentages use the v90 fallback; Crown Engine Technician placement and RH10 access remain story-owned.
- Chapter 12 mandatory-vs-completionist validation — **PASS / VALIDATED in v88**; formation weights restored v90 and action fallback active; Kharvek placement/RH11 timing remain story-owned; MH6 runtime-duration gate remains QA-only.
- Chapter 13 mandatory-vs-completionist validation — **PASS / VALIDATED in v89**; Lv57 start → Lv58 Archon → Lv60 Last Shelter/PONR → Lv61 final boss → Lv62 ending; completionist reaches Lv70 by Last Shelter; no numerical or Power changes.
- **CAMPAIGN PAPER VALIDATION COMPLETE through Chapters 0–13.** v90 also closes the static formation/Character-Quest-boss/support-object/action-selection gaps. Story placements remain tracked outside static enemy design and do not block the active representative true-battle suite.

Method:
- test each encounter against the guaranteed mandatory-route party state available at that point;
- test the same fixed encounter against a plausible completionist party using optional progression available before that encounter;
- do not dynamically scale enemies to erase optional progression;
- validate survivability, damage intake, status pressure, action economy, encounter duration, resource attrition, and completionist advantage;
- preserve existing kits unless a specific validation failure justifies targeted tuning;
- a targeted Power change is allowed only as a balance correction for that specific action, not as a reopening of the global Power audit.

Coverage:
1. Chapter 0–13 ordinary formations and reused variants;
2. Elites;
3. authored/protected/nonlethal encounters;
4. story bosses and their supports/forms;
5. Regional Hunts;
6. Major Hunts;
7. support objects and encounter formations where they materially affect difficulty.

Detailed protocol:
`16_BALANCE_AND_TESTING/BALANCE/ENEMY_BOSS_MANDATORY_COMPLETIONIST_VALIDATION.md`

## Priority 2 — CEXP recalibration — CLOSED v92 (v91 budgets retained; recruitment arithmetic corrected)
Owner:
`10_PROGRESSION_AND_EXP`

Closed:
- CL13 retained at **6,000 CEXP**;
- mandatory-route full Base + Subclass completion now spans **~Lv55–60**;
- Ch12 CEXP recalibrated to **1,250**;
- Ch13 CEXP recalibrated to **1,750**, split **1,500 pre–Last Shelter / 250 post**;
- exact optional CEXP ledger authored: **1,000 before MH6 / 1,075 including MH6**;
- old Lv53–57, Lv62, and ~1,800 optional-CEXP timing models retired.

## Priority 2A — True-battle certification — ACTIVE
Owner:
`16_BALANCE_AND_TESTING`

Before campaign-wide runtime QA, build reproducible party snapshots and run representative turn-by-turn battles against selected early/mid/late/final bosses. Each snapshot must specify:
- exact story point and Player Level;
- exact CEXP earned and selected-class allocation;
- Base/Subclass CLs and available abilities/Ultimates;
- equipment/Relics/Legacies;
- Standard Cards;
- Prime slots and available Prime states;
- consumables and starting HP/MP.

Run both mandatory-route and completionist baselines where optional progression exists.

## Priority 3 — Economy/reward exact gaps
Owner:
`12_ECONOMY_AND_REWARDS`

Still open where not separately closed:
- exact Side Quest Auren/Consumable packages;
- Character Quest monetary add-ons;
- exact Hunt Auren payouts where unresolved;
- consumable resale where unresolved;
- Kessara service fee, if any.

## Priority 4 — Implementation reconciliation
Owner:
`13_UI_AND_IMPLEMENTATION`

High-impact engineering work:
- remove stale Mastery Point implementation assumptions;
- replace proof bearer-locked `first_champion` Prime behavior;
- implement Auren rather than proof `gold`;
- replace proof equipment/item content;
- build production save schema/migrations;
- build production menus/combat UI.

## Priority 5 — Full production playtest / QA
Owner:
`16_BALANCE_AND_TESTING`

After the targeted balance passes above:
- campaign route playtests;
- light / typical / heavy / completionist route playtests;
- boss/Hunt regressions;
- resource attrition checks;
- optional overlevel checks;
- Prime regressions;
- Android QA.

## Later — Music/audio
Owner:
`15_AUDIO_AND_MUSIC`

Current final soundtrack:
> **entirely OPEN**

## Later — Art production
Owner:
`14_ART_AND_VISUALS`

Visual canon is organized, but final production assets remain a separate production workload.

## Rule
Do not use this index to silently reopen a closed owner-domain rule.


## v93 active balance frontier — TRUE BATTLES
- Trait-effect migration recovery: **CLOSED**.
- Player/guest omitted Base Hit default: **CLOSED at 100** unless an owning action says otherwise.
- Representative true-battle boss suite: **ACTIVE**.
- First anchor: **Hollow Watch Castellan / S008**.
- CEXP recruitment-aware calibration remains v92 authority.

- Hollow Watch Castellan true-battle certification: **CLOSED / PASS v93**.
- Archive Leviathan true-battle certification: **CLOSED / PASS v97**.
- Next true-battle anchor: **Regulation Crucible → Seventh Reaction**.


## Bleed v96 simulation follow-up
- Global Bleed starts at **3% Max HP per qualifying proc** and escalates to **4% after 3 affected turns uncleared**.
- Hollow Watch normal/smart pass remains closed because its successful line prevents Bleed resolution.
- Refresh the historical aggressive support-ignore metrics when/if that branch is used as a current benchmark.
- All remaining true-battle anchors use v96 Bleed escalation.


## v97 Archive Leviathan follow-up
- Archive Leviathan design-layer true battle is **CLOSED / PASS / RETAIN**.
- Recorded Pattern deterministic repeat trigger is closed; no random first-use recording remains.
- Current prepared mandatory test uses legal purchased early-core consumables; it does not add a mandatory free-item grant.
- No-item stress remains evidence only and does not replace the canonical prepared line.
- Representative suite remains **ACTIVE**; next anchor is Regulation Crucible → Seventh Reaction.
