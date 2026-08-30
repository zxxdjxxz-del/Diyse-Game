# Chapter 10 — Mandatory vs Completionist Enemy/Boss Validation

**Version:** v86  
**Status:** **PASS / VALIDATED WITH FOREST-FORMATION, ACTION-WEIGHT, AND QUEST-BOSS DATA DEPENDENCIES**  
**Power-audit status:** **CLOSED — no direct-damage Power changed**

## Purpose
Validate current Chapter 10 — **The Last Blank** — against the player state that actually exists at each point rather than treating **Lv47** as the whole chapter baseline.

Chapter 10 uses the post-Volition combat framework:
- all six permanent characters are available;
- active battle party remains **maximum 4**;
- Subclasses are legal throughout;
- completionist optional EXP/CEXP, gear, Cards, Primes, Hunts, Character Quests, and Legacy progress are allowed to create a real advantage;
- enemies remain fixed authored encounters and do not dynamically scale upward.

The direct-damage Power audit remains closed. No Chapter-10 action requires a Power retune.

---

## 1. Chapter-level anchors
Mandatory campaign spine:
> **Lv42 chapter start → Lv47 chapter end**

Exact fixed mandatory EXP:
- Chapter-9 clear: **184,300 EXP = Lv42**;
- Chapter-10 ordinary allocation: **31,800 EXP**;
- Chapter-10 named/story allocation: **21,500 EXP**;
- Chapter-10 clear: **237,600 EXP = Lv47 exactly**.

Before Registry Warden, all Chapter-10 ordinary mandatory EXP has been earned and the three pre-boss named packages total **8,500 EXP**:
> **224,600 EXP = Lv45**, 1,700 EXP short of Lv46.

After Registry Warden:
> **232,600 EXP = Lv46**.

Last Blank resolution + chapter clear then lands at:
> **237,600 EXP = Lv47 exactly**.

### Practical mandatory route bands
Because exact forest random-formation allocation is not fully recovered, use encounter bands rather than inventing false exact thresholds:
- eastern forest / Cerythvale departure: **Lv42→43**;
- Eastern Wayfinder: **~Lv43→44**;
- Buried Registry approach: **~Lv44→45**;
- Registry Warden: **Lv45**;
- post-Warden resolution: **Lv46→47**.

### Completionist route
Fixed optional EXP already legal by the end of Chapter 9 is **89,200 EXP**.
Before committing to Chapter 10, a completionist may additionally clear:
- Ilyra Character Quest — **10,000 EXP**;
- Major Hunt #3 Concordance Guardian — **8,000 EXP**.

Therefore a fully current completionist can begin Chapter 10 at:
> **291,500 EXP = Lv51**.

The same fixed Chapter-10 route then reaches:
- early/middle route: approximately **Lv51→53**;
- Registry Warden: **331,800 EXP = Lv54**;
- chapter clear: **344,800 EXP = Lv55**.

Very exhaustive incidental combat can push the high side around **~Lv55→56**.

Torren's Character Quest unlocks **after Chapter 10**. Its 15,000 EXP can move a post-clear completionist to **359,800 EXP = Lv56** before Major Hunt #4, but its boss is separately data-dependent below.

---

## 2. Party / Subclass / Prime boundary
Throughout Chapter 10:
- six permanent characters are available;
- only four act in battle;
- Subclasses are legal;
- two Prime slots per character remain legal under the current post-Volition system where equipped/acquired;
- story and optional Prime access remains fixed by current acquisition rules;
- no guest character expands the active cap.

The **v91 CEXP recalibration** now places normal full class completion at ~Lv55–60. True-battle testing must use the resulting Class-Level breadth; Chapter-10 enemies are not pre-emptively scaled upward.

---

## 3. Ordinary enemies — individual-body validation
Current Chapter-10 ordinary roster:
- Thornvine Creeper — Lv42 / **1,050 HP**;
- Briar Boar — Lv43 / **1,420 HP**;
- Archive Scribe Engine — Lv43 / **1,050 HP**;
- Judgment Frame — Lv44 / **1,520 HP**;
- Erasure Wisp — Lv43 / **820 HP**;
- Command-Station Sentry — Lv44 / **1,360 HP**;
- Authority Lens — Lv44 / **940 HP**;
- Command Ring Drone — Lv44 / **980 HP**.

For a conservative incoming-damage reference, use **Vaelira's Green Arcanist natural body with no equipment HP/Defense/Spirit added**. Actual geared parties are safer.

### Eastern forest — Lv42 mandatory reference
Representative strongest direct hits:
- Thorn Lash — **~9.4% Max HP**;
- Root Spit — **~9.0%**;
- Briar Boar Tusk Rush — **~13.8%**;
- Shoulder Charge — **~12.9%**;
- Rooting Impact — **~14.7%**.

Bleed and Staggered create the intended pressure; raw direct damage does not threaten healthy one-action deletion.

### Eastern Wayfinder — Lv43 mandatory reference
Representative pressure:
- Scribe Beam — **~11.1% Max HP**;
- Index Burst — **~8.8% per target**;
- Judgment Strike — **~13.9%**;
- Adjudication Pulse — **~8.0% per target**;
- Enforcement Crush — **~15.4%**;
- Erasure Touch — **~12.3%**;
- Empty Pulse — **~8.9% per target**;
- Ruin Flicker — **~10.9%**.

### Buried Registry — Lv44 mandatory reference
Representative pressure:
- Command Blade — **~12.7% Max HP**;
- Station Pulse — **~8.7%**;
- Authority Ray — **~12.8%**;
- Classification Flash — **~9.1% per target**;
- Ring Bolt — **~9.0%**;
- Registry Pulse — **~6.9% per target**;
- cross-used Judgment Frame Enforcement Crush — **~14.9%**.

At the Chapter-10 completionist band around Lv51–54, the strongest ordinary single-target actions fall to roughly **~8.5–11.9%** on the same deliberately under-geared class reference.

**Verdict:**
> **PASS / RETAIN ALL CHAPTER-10 ORDINARY RAW STATS AND POWERS.**

---

## 4. Formation durability / action economy
Recovered exact composition references exist for Eastern Wayfinder and Buried Registry.

### Eastern Wayfinder
Light/standard/heavy formations contain **5–8 bodies**.
The heaviest recovered formation is:
> 2 Archive Scribe Engines + 3 Judgment Frames + 3 Erasure Wisps

Combined raw HP:
> **9,120 HP spread across 8 bodies**.

A deliberately low-assumption four-character mandatory AoE reference using only early Base-Class AoEs that are unquestionably available long before Chapter 10 — Crest Knight Sweeping Edge, Cardweaver Weave Burst, Green Arcanist Stormburst, and Ruin Vanguard Fracturing Brand — with **no equipment offense added** produces approximately:
- Scribe Engine: **~437 damage per full serious AoE round** → ~2.4 rounds;
- Judgment Frame: **~426** → ~3.6 rounds;
- Erasure Wisp: **~463** → ~1.8 rounds.

Equipment, stronger later abilities, affinities, Cards, criticals, Subclasses, and Prime use only improve this throughput.

### Buried Registry
The heaviest recovered formation is:
> 3 Command-Station Sentries + 2 Judgment Frames + 1 Authority Lens + 2 Command Ring Drones

Combined raw HP:
> **10,020 HP spread across 8 bodies**.

Using the same no-equipment early-Base-AoE reference at Lv44 gives approximate full-party AoE-round durability:
- Command-Station Sentry: **~3.1 rounds**;
- Judgment Frame: **~3.5 rounds**;
- Authority Lens: **~2.0 rounds**;
- Command Ring Drone: **~2.1 rounds**.

Therefore the large formation count does **not** behave like eight boss-health targets. The lighter Lens/Drone/Wisp bodies collapse first and rapidly reduce enemy action economy. Heavy formations remain appropriate MP/status/resource-pressure spikes.

### Remaining formation dependencies
- Exact eastern-forest formation table was not recovered and is **not invented** here.
- Current individual Chapter-10 files do not expose exact per-action selection weights for these reused ordinary kits. Therefore exact worst-case status/burst probability remains a **data-recovery dependency**, not a reason to retune the authored bodies blindly.

**Verdict:**
> **PASS for recovered Wayfinder/Registry compositions; OPEN only for unrecovered forest composition and exact action-weight probability.**

---

## 5. Optional Elite / authored protected / Regional Hunt
Current Chapter 10 intentionally has:
- **no optional Elite**;
- **no authored/protected combat identity**;
- **no Regional Hunt**.

Nothing is invented to fill those categories.

---

## 6. Mandatory boss — Registry Warden
Actual player references:
- mandatory — **Lv45**;
- completionist fixed-content — **Lv54**;
- high-side — **~Lv55**.

Retain:
- Lv49;
- **13,514 HP**;
- ATK157 / MAG172 / DEF124 / Spirit126 / SPD46 / EVA0 / SR10;
- Closed Registry → Open Registry at **40% HP**;
- one continuous HP bar;
- no refill / no transition attack / no Prime refresh;
- Closed Record = +15 Total Defense through end of following round;
- Open Registry = Speed +10 / Total Defense −15;
- status-neutral kit by design.

On the no-equipment fragile Lv45 reference:
- Closed Registry single-target actions are roughly **~13.2–15.1% Max HP**;
- Catalog Sweep is **~9.2% per target**;
- Open Registry Lance / Unsealed Verdict are **~16.7–16.8%**;
- Paired Citation total is **~17.8%**;
- Open-state AoE is roughly **~11.4–12.6% per target**.

At Lv54 completionist, the same strongest direct actions fall to roughly **~9.9–13.3%**.

Existing duration certification remains coherent:
- mandatory normal — **~10–11 rounds**;
- completionist — **~7–8 rounds**;
- high-side — **~6–7 rounds**.

Open Registry intentionally trades defense for speed and pressure instead of adding a second HP body.

**Verdict:**
> **PASS / FORMALLY VALIDATED v86 / RETAIN ALL RAW STATS, THRESHOLDS, AND POWERS.**

---

## 7. Post-Chapter-10 Character Quest dependency — Old Relay Warden
Torren's Character Quest — **The Road That Returns** — unlocks after Chapter 10 under current quest authority.

Current enemy authority preserves:
> **Old Relay Warden — one-bar Character Quest boss**

However the current reorganized library does **not** contain an exact recovered raw-stat/action sheet for Old Relay Warden. Earlier working authority also explicitly left its exact numerical move sheet deferred rather than supplying a hidden completed package.

Therefore:
> **OPEN — DATA DEPENDENCY**

Do not invent its HP, ATK/MAG, defenses, Powers, action weights, or exact status rates merely to close the spreadsheet.

The known design boundary remains:
- one bar;
- heavy relay/mechanical impact identity;
- at least one existing heavy impact may carry **20–25% Staggered**;
- Stun only if the final exact kit contains a genuine electrical/high-energy relay discharge.

This quest-boss gap belongs to the later **Quest Boss Recovery / Validation** sweep and does not invalidate the fixed Chapter-10 route.

---

## 8. Major Hunt #4 — Worldscar Leviathan
Unlock:
> **after Chapter 10**

Current recommendation:
> **Lv60**

Current body:
- Lv60 / **38,800 HP**;
- ATK221 / MAG246 / DEF166 / Spirit178 / SPD53 / EVA0 / SR10;
- one continuous HP bar;
- Prismatic Confluence at **50% HP**;
- Confluence: Magic +10%, Speed +10, Total Defense −10;
- no HP refill / no Prime refresh / no free transition action.

First-access player references:
- mandatory chapter-clear party — **Lv47**;
- completionist without Torren CQ — approximately **Lv55**;
- completionist with Torren CQ's 15,000 EXP — approximately **Lv56**;
- intended recommendation — **Lv60**.

On the no-equipment fragile reference:

### Lv47 immediate mandatory access
Before Confluence:
- Worldscar Lance / Leviathan Crush / Worldscar Ruin — roughly **~32.7–33.1% Max HP**;
- Basin Collapse — **~24.2% per target**.

During Confluence:
- boosted Worldscar Lance — **~37.5%**;
- Confluence Spear total — **~41.4%**;
- Prismatic Wave — **~30.3% per target**.

This is intentionally punishing because Lv47 is **13 levels below recommendation**.

### Lv56 completionist access
During Confluence:
- strongest singles are roughly **~25.3–31.6%**;
- AoE is roughly **~21.0–23.2% per target**.

### Lv60 recommendation
During Confluence:
- strongest singles are roughly **~22.7–28.2%**;
- AoE is roughly **~18.7–20.7% per target**.

This preserves the intended hierarchy:
> Chapter-10 route boss << immediate completionist Major-Hunt challenge < recommended Lv60 Major-Hunt state.

A Lv55–56 completionist may challenge early and gain a real reward for extensive optional progression, but the Lv60 recommendation still matters.

**Verdict:**
> **PASS / EXISTING RECERTIFICATION FORMALLY VALIDATED v86 / RETAIN Lv60, 38,800 HP, AND ALL POWERS.**

---

## 9. v86 change ledger
### Numerical changes
> **NONE**

### Power changes
> **NONE**

### Authority/status changes
- Chapter-10 player-state anchors made explicit: **Lv42 start → Lv45 Registry Warden → Lv46 post-Warden → Lv47 clear**.
- Completionist route made explicit: **Lv51 start → Lv54 Registry Warden → Lv55 clear** under fixed authored optional content.
- Wayfinder and Buried Registry recovered formations formally checked for durability/action-economy decay.
- Eastern forest exact formations remain unrecovered rather than fabricated.
- Exact ordinary action-selection weights remain a narrow data-recovery dependency.
- Registry Warden promoted from working recertification to **FORMALLY VALIDATED v86**.
- Major Hunt #4 Worldscar Leviathan promoted from unlock/raw recertification to full two-baseline **FORMALLY VALIDATED v86**.
- **Historical v86 note:** Old Relay Warden was entered as an open data dependency here; **resolved in v90** when its exact current production sheet was authored.

---

# Final Chapter-10 verdict
> **PASS / VALIDATED WITH EXPLICIT FOREST-FORMATION, ACTION-WEIGHT, AND QUEST-BOSS DATA DEPENDENCIES**

Validated anchors:
- chapter start — **Lv42 mandatory / Lv51 completionist**;
- Eastern Wayfinder — **~Lv43→44 mandatory / ~Lv52→53 completionist**;
- Buried Registry — **~Lv44→45 mandatory / ~Lv53→54 completionist**;
- Registry Warden — **Lv45 mandatory / Lv54 completionist**;
- chapter clear — **Lv47 mandatory / Lv55 completionist**;
- Major Hunt #4 — **Lv60 recommended**, with completionist first-access around Lv55–56.

All currently numeric Chapter-10 route enemies and the Chapter-10 mandatory boss pass without stat or Power tuning.

The remaining Chapter-10-window unknowns are data recovery/placement problems, not demonstrated balance failures:
- exact eastern-forest random formations;
- exact ordinary action-selection weights;
- Old Relay Warden exact numerical/action sheet.

## Next frontier
> **Chapter 11 — Lv47 start → Lv52 end**, with Subclasses legal throughout and post-Chapter-10 optional progression carried forward normally.
