# Diyse — Current Canon Status

**Repository transition:** v98 subject-folder migration in progress on `migration/v98-subject-canon`  
**Historical safety branch:** `archive/pre-v98-reorganization`  
**Written migration baseline:** v2.20 / Audit135 plus later accepted corrections through v97

## Authority model
The numbered subject domains are the active source of truth. `00_MASTER_CONTROL` routes authority and records cross-domain locks. `90_WORKING` contains only genuinely unresolved/reopened work. Historical material and pre-v98 Git history never silently override current domain authority.

## Current project locks
- Permanent playable cast: **6**.
- Active battle party: **4**.
- Story structure: **Chapter 0 + Chapters 1–13**.
- True irreversible PONR: **Last Shelter → Reactor Galleries**.
- Regions: **Yahtrenhold / The Westways / The Greyspires / Black Host Territory**.
- Standard elements: **Fire / Ice / Lightning / Earth**.
- Universal harmful statuses: **Burn / Freeze / Stun / Staggered / Bleed**.
- Defensive magic-resistance stat: **Spirit**.
- No natural Accuracy stat; actions use Base Hit versus Evasion.
- Barrier does not exist. Brace does not exist. There is no global Break/Stagger meter.
- Bleed: **3% Max HP per qualifying proc**, escalating to **4%** after 3 affected-unit turns uncleared; round tick + actual-action tick; full-HP/status-clear/eligible-item removal only.
- Standard Cards: **24**; Primes: **12**.
- Faces: **Might / Elements / Grace / Acuity / Change / Ruin**.
- Prime progression: **Recovered → Awakened** only; Concordant removed.
- Equipment: **38 ordinary + 36 Relics + 17 Legacies = 91**.
- Player level cap: **70**; normal campaign ending about **Lv62**; Last Shelter about **Lv60**.
- CEXP: CL13 = **6,000 cumulative**; recruitment-aware normal-route Base + Subclass completion targets approximately **Player Lv55–60**.
- Optional content: **5 Side Quests / 6 Character Quests / 11 Regional Hunts / 6 Major Hunts**.
- Presentation target: **HD-2D anime**.
- Whole-project music plan: **OPEN**.

## Current class pairs
- Cyanis Dovaren — Crest Knight / Crest Arcanist
- Ilyra Amarin — Blue Warden / Vowblade
- Torren Harth — War Archer / Routeweaver
- Nimera Pellan — Cardweaver / Proofhunter
- Vaelira Serren — Green Arcanist / Axiomblade
- Seyrik Rell — Ruin Vanguard / Ruin Warden

Synthesis is removed. Mastery Point currency is removed. No permanent Subclass use occurs before end-Ch7 Sixfold Volition.

## Major Hunt current recommendation ladder
> **Lv33 / Lv41 / Lv54 / Lv60 / Lv65 / Lv70**

Unlocks:
- #1 after Chapter 6
- #2 after Chapter 7
- #3 after Chapter 9
- #4 after Chapter 10
- #5 after Chapter 11
- #6 existing late dual gate

Exact Hunt bodies, rewards, and mechanics live in the owning enemy/quest/balance domains.

## Balance-validation state
- Chapters 0–13 mandatory-vs-completionist paper validation: **COMPLETE**.
- Enemy direct-damage Power audit: **CLOSED**.
- Enemy static design / formation recovery: **CLOSED**, with story-owned placement/timing dependencies tracked separately.
- Recruitment-aware CEXP recalibration: **CLOSED v92**, retaining v91 budgets.
- Hollow Watch Castellan representative true battle: **CERTIFIED v93**.
- Archive Leviathan representative true battle: **CERTIFIED v97 / RETAIN**.
- Next representative true-battle anchor: **Regulation Crucible → Seventh Reaction**.

## v97 carried corrections
- Archive Leviathan retained its current HP/raw stats/status chances/direct-damage Powers after true-battle certification.
- Recorded Pattern has a deterministic repeated-offense formation trigger.
- Blue Warden Clear Warding: **+5 Status Resistance for 2 rounds** after cleansing.
- No gameplay numeric retune was introduced by the repository reorganization.

## Implementation debt
Implementation/proof assets may still contain stale historical assumptions. Current implementation divergence tracking belongs under `13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/`. Canon documentation controls design intent until runtime is reconciled.

For exact values, use the owning numbered domain rather than expanding this status file into another cumulative tracker.
