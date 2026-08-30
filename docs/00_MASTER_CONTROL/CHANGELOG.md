# v97 — Archive Leviathan True-Battle Certification

- Certified Archive Leviathan with 20,000-run prepared mandatory Lv6 and completionist/high-side Lv7 true-battle distributions.
- Mandatory: 100% wins / median10 / mean10.05 / 0.05% any-KO.
- Completionist/high-side: 100% wins / median9 / mean8.58 / 0% any-KO.
- Retained HP1,900, ATK50, MAG52, DEF31, Spirit33, SPD25, all status chances, and all direct-damage Powers.
- Closed Recorded Pattern's deterministic formation trigger: actor-qualified same-action consecutive-offense repeat; trigger hit remains full damage; later matching uses receive existing 20% penalty.
- Restored Clear Warding's exact +5 Status Resistance / 2-round value into Blue Warden owning authority.
- Synchronized stale active-queue and balance-closure CEXP/true-battle statuses.
- Next representative anchor: Regulation Crucible → Seventh Reaction.

---

# v96 — Bleed Escalation

- Bleed begins at **3% Max HP per qualifying proc**.
- If the same Bleed remains uncleared through **3 affected-unit turns**, it increases by **+1 percentage point** to **4% Max HP per qualifying proc** until removal.
- The third turn's action proc still uses 3%; escalation becomes active after that turn resolves.
- Reapplication while Bleed is already active does not reset its age or escalation; full removal followed by a new application restarts at 3%.
- Cadence remains round tick + action tick, including qualifying extra actual actions.
- Application chances and removal rules are unchanged.
- Regional Hunt conversion: **2.25% initially → 3% escalated**.
- Major Hunt / mandatory boss conversion: **1.5% initially → 2% escalated**.
- Hollow Watch Castellan's smart-line true-battle PASS remains valid because its certified Ballista-priority route prevents Bleed from resolving.

---

# v95 — Bleed Magnitude Increase

- **Bleed magnitude increased from 2% to 3% Max HP per qualifying proc.**
- Cadence remains unchanged: one qualifying proc each round and another whenever the affected unit takes an actual action.
- Normal acting target therefore takes approximately **6% Max HP per round** from Bleed before extra-action effects.
- Bleed remains indirect, cannot Crit, ignores Defense/Spirit, may KO, and retains its existing clear conditions.
- High-rank conversion remains proportional: Regional Hunts take **75% ordinary Bleed magnitude (2.25% Max HP/proc)**; Major Hunts and mandatory bosses take **50% ordinary magnitude (1.5% Max HP/proc)**.
- Existing Bleed application chances are unchanged.
- Hollow Watch Castellan's main smart-line true-battle certification remains structurally valid because the Ballista never fires in that policy; its old aggressive-support-ignore Bleed-risk statistics are superseded and must be refreshed under v95 before being quoted as current.

---

# Diyse — Active Canon Changelog

This is a concise current-facing change record, not the full migration history.

Full migration batches are archived under:
`99_ARCHIVE/MIGRATION_HISTORY/`

## Current late corrections carried into active canon

### Structure
- main story = Chapter 0 + Chapters 1–13
- new Chapter 10 inserted after Crownfall/Rhazek
- former Chapters 10–12 became Chapters 11–13

### Geography
- Crownhold / Southhold / Heartlands → Yahtrenhold
- Edgelands → The Westways
- Diysereach / formal Highlands → The Greyspires
- Blackstone → Black Host Territory
- Westreach / Yahtrens Stand → Westguard
- Waystone Cut → Ridgecut
- Westline Relay formal name → Westline

### Cards
- Resource → Acuity
- Last Measure → Last Cartographer
- Concordant removed
- Prime states = Recovered → Awakened
- 3 Standard Card slots
- 2 Prime slots/character after Sixfold Volition
- Story Prime bearer no longer owner-locks battle use

### Classes / progression
- Synthesis removed
- Mastery Point currency removed
- Masteries unlock automatically by Class Level
- [SUPERSEDED] class completion timing was temporarily targeted around Player Lv62, then Lv53–57; the current next-pass target is Lv55–60

### Combat
- Spirit is current magic-resistance stat label
- no natural Accuracy stat
- Barrier removed
- Brace removed
- global Break/Stagger meter removed
- four standard elements only
- Bleed current cadence/clear rules preserved

### Equipment
- 38 ordinary + 36 Relic + 17 Legacy = 91
- no general Accessory slot
- Ilyra = Wardrod + Shield-or-Focus
- Legacies stronger than Relics overall

### Quests
- ordinary Side Quest roster reduced to 5
- Character Quests = 6
- current CQ boss distribution = 4 boss / 2 no-boss
- true optional-content cutoff = Last Shelter → Reactor Galleries

### Visuals
- HD-2D is active presentation target
- Cyanis exact master has no shield; crest/amulet at hip
- Nimera = age22; green/gold Card and hip book

### Audio
- final whole-project music reset to OPEN
- old regional soundtrack schemes remain research only


## v18 incremental merge

### Mirena Side Quest EXP redistribution
- A Measure of Bread: **1,500 → 0 EXP**
- The Crown's Debt: **3,500 → 0 EXP**
- What We Build After: **9,500 → 14,500 EXP**
- Mirena quest-line total remains **14,500 EXP**
- total ordinary Side Quest EXP remains **20,000 EXP**





### Major Hunt unlock timing correction
All Major Hunts that unlocked before Chapter 10 were moved one chapter later:
- Major Hunt #1 — Ashen Whitehorn: after Ch4 → **after Ch5**
- Major Hunt #2 — Crownless Siege Marshal / Crownless War Engine: after Ch5 → **after Ch6**
- Major Hunt #3 — Concordance Guardian: after Ch7 / Sixfold Volition → **after Ch8**
- Major Hunt #4 — Worldscar Leviathan: after Ch8 → **after Ch9**
- Major Hunt #5 remains **after Chapter 10**
- Major Hunt #6 remains under its existing late dual gate.

The Mirena change in this v18 is **EXP redistribution only**, not quest unlock timing.


### Major Hunt unlock timing — current v19
The first five Major Hunts now unlock on the following schedule:
- #1 Ashen Whitehorn — **after Ch6**
- #2 Crownless Siege Marshal / Crownless War Engine — **after Ch7**
- #3 Concordance Guardian — **after Ch9**
- #4 Worldscar Leviathan — **after Ch10**
- #5 Final Archive Arbiter — **after Ch11**
- #6 The Unfinished World remains under its existing late dual gate.

This supersedes the prior v18 schedule.


### Major Hunt timing propagation
The current after-Ch6 / after-Ch7 / after-Ch9 / after-Ch10 / after-Ch11 schedule is now propagated into:
- `09_ENEMIES_AND_ENCOUNTERS/MAJOR_HUNTS`
- `10_PROGRESSION_AND_EXP/OPTIONAL_EXP.md`
- `11_QUESTS/HUNTS/MAJOR_HUNT_ACCESS_REGISTER.md`
- `16_BALANCE_AND_TESTING`
- dependent Legacy/Forge-component source timing in `08_ITEMS_AND_EQUIPMENT`

No Major Hunt raw stats or recommended levels were changed by this propagation.


### CEXP completion target restored
- Full Base + Subclass completion target restored to **Player Lv53–57**.
- The temporary Lv62 class-completion target is retired.
- Existing 6,000-CEXP CL13 curve and formal chapter allocations remain active.
- CEXP now requires verification rather than a mandatory rebalance.
- Major Hunt difficulty recertification becomes the highest-priority balance pass.


### Major Hunt #1 difficulty recertification
Ashen Whitehorn was recertified for its new after-Ch6 access window:
- recommended level **22 → 33**
- HP **11,270 → 15,600**
- ATK **96 → 130**
- MAG **78 → 94**
- DEF **73 → 92**
- Spirit **68 → 85**
- SPD **38 → 44**
- EVA 10 unchanged
- Status Resistance 10 unchanged

Major Hunts #2–#5 remain pending. #6 remains unchanged.


### Major Hunt #2 difficulty recertification
Crownless Siege Marshal / Crownless War Engine was recertified for its new after-Ch7 access window.

Crownless Siege Marshal:
- Lv **28 → 40**
- HP **9,360 → 13,600**
- ATK **124 → 155**
- MAG **92 → 110**
- DEF **90 → 111**
- Spirit **78 → 96**
- SPD **35 → 41**
- EVA 5 unchanged
- Status Resistance 10 unchanged

Crownless War Engine:
- Lv **29 → 41**
- HP **11,650 → 16,900**
- ATK **139 → 174**
- MAG **102 → 122**
- DEF **99 → 121**
- Spirit **86 → 105**
- SPD **33 → 39**
- EVA 0 unchanged
- Status Resistance 10 unchanged

Combined raw body HP:
- **21,010 → 30,500**

The genuine fresh-body Form-II Prime refresh remains unchanged.
Major Hunts #3–#5 remain pending.


### Major Hunt #3 difficulty recertification
Concordance Guardian was recertified for its new after-Ch9 access window:
- recommended level **35 → 54**
- HP **18,180 → 27,400**
- ATK **146 → 194**
- MAG **151 → 210**
- DEF **115 → 144**
- Spirit **118 → 151**
- SPD **40 → 49**
- EVA 5 unchanged
- Status Resistance 15 unchanged

Six Faces → Open Concordance remains a same-bar state transition with no Prime refresh.

Major Hunts #4–#5 remain pending.


### Major Hunt #4 difficulty recertification
Worldscar Leviathan was recertified for its new after-Ch10 access window:
- recommended level **47 → 60**
- HP **30,200 → 38,800**
- ATK **187 → 221**
- MAG **207 → 246**
- DEF **148 → 166**
- Spirit **156 → 178**
- SPD **44 → 53**
- EVA 0 unchanged
- Status Resistance 10 unchanged

Prismatic Confluence remains a same-bar state transition with no Prime refresh.

Major Hunt #5 remains pending.


### Major Hunt #5 difficulty recertification
Final Archive Arbiter was recertified for its new after-Ch11 access window:
- recommended level **58 → 65**
- HP **43,100 → 52,600**
- ATK **229 → 258**
- MAG **244 → 276**
- DEF **194 → 202**
- Spirit **198 → 211**
- SPD **50 → 56**
- EVA 5 unchanged
- Status Resistance 15 unchanged

Custody Protocols, Archive Burden, and Transfer Windows remain same-bar systems with no Prime refresh.

### Major Hunt recertification closure
Major Hunts #1–#5 are now fully recertified for the delayed unlock schedule:
> **Lv33 / Lv41 / Lv54 / Lv60 / Lv65**

Major Hunt #6 remains unchanged at Lv70.

The next highest-priority content pass is Chapter 5 dialogue beat rewriting.


### Mandatory boss route recertification resumed
The work queue is corrected back to the mandatory-boss mandatory-vs-completionist pass.

Hollow Watch Castellan:
- mandatory reference ~Lv5
- completionist reference ~Lv5
- boss Lv6
- 1,758 HP / 36 ATK / 27 MAG / 27 DEF / 24 Spirit / 25 SPD / 0 EVA / 5 SR
- **PASS / RETAIN**
- no raw-stat change

Next:
> Archive Leviathan

The earlier automatic promotion of Chapter-5 dialogue to current priority is superseded.


### Hollow Watch Castellan actual-party recertification recovery
Recovered the later v85 working balance result that supersedes the stale v27 end-Ch1 Lv5 check.

Actual S008 profile:
- central ~Lv2
- high-side ~Lv3

Current working package:
- Castellan: Lv6 / **600 HP / 42 ATK / 27 MAG / 27 DEF / 24 Spirit / 25 SPD**
- Ballista: **120 HP / 55 ATK / 20 DEF / 18 Spirit / 24 SPD**
- Watch Seal: **100 HP / 22 DEF / 28 Spirit / 10% Fortress direct-damage reduction**

Certified working pacing:
- aggressive **~6–7**
- normal **~8**
- safety **~9–10**

The prior 1,758-HP / ATK36 PASS rationale is superseded for the current boss-balance pass.

Next boss:
> **Archive Leviathan**


### Hollow Watch Castellan pacing trim
The Chapter-1 calibration boss was intentionally shortened:
- HP **600 → 450**
- ATK / MAG / DEF / Spirit / SPD unchanged
- Ballista unchanged
- Watch Seal unchanged

Revised expected pacing:
- aggressive **~4–5 rounds**
- normal **~6 rounds**
- safety **~7–8 rounds**

The goal is for this early boss to resolve a little faster without reducing its turn-by-turn threat.


### Archive Leviathan actual-party HP recertification
Recovered and promoted the v85 partial working result into the current subject folders.

Actual S013 references:
- mandatory central **~Lv6**
- completionist/high-side **~Lv7**

HP:
- **2,592 → 1,900**

Lv6 all-basic party output:
- **178.48 / round**
- old 2,592 HP = **14.52 all-basic rounds**

Current pacing target:
- aggressive ~8–9
- mandatory normal **~9–10**
- completionist/high-side **~8–9**
- safety ~10–11

Preserved:
- Lv9 encounter identity
- DEF31 / Spirit33 / SPD25 / EVA0 / SR5
- one continuous HP bar
- Recorded Pattern → Emergent same-bar
- no refill / no transition damage / no Prime refresh
- Leviathan Rend 25% Bleed
- Vault Crash 15% Staggered per target

ATK34 / MAG45 remain **uncertified placeholders** because exact authored action Powers remain unrecovered.

Next:
> Commander Rhazek — Bastion Master


### Direct-damage Power completeness pass begins
New hard rule:
> every direct-damage action requires explicit numeric Power.

No combat kit may remain numerically PASS/CLOSED with qualitative-only or unspecified direct damage.

Base-Class missing Powers were filled across all six permanent characters.

Archive Leviathan direct-damage package:
- Leviathan Rend — **220 Power**
- Vault Crash — **140 Power per target**
- Archive Undertow — **150 Power per target**
- Recorded Pattern — **Power N/A; adaptation only**
- raw offense **ATK50 / MAG52**

The enemy move Power audit continues encounter-by-encounter.

Next:
> Commander Rhazek — Bastion Master


### Commander Rhazek — Bastion Master recertification
Chapter-2 S015 boss now passes both the route-level and Power-completeness gates.

Actual route references:
- mandatory ~Lv7
- completionist ~Lv8
- high-side optional route may approach Lv9

Raw line:
- HP **2,700 → 2,050**
- ATK **49 → 58**
- MAG **31 → 44**
- DEF 36 unchanged
- Spirit 32 unchanged
- SPD **26 → 27**
- EVA5 / SR5 unchanged

Direct-damage Powers:
- Commander's Cut 180
- Shieldline Break 220
- Command-Link Pulse 135 AoE
- Crossfire Bolt 165
- Ruin-Driven Cut 210
- Bastion Breaker 250
- Ruin Sweep 145 AoE

Finite support:
- Bastion Shield Detachment — 180 HP
- Bastion Ranged Position — 150 HP

45% HP Ruin/armor escalation remains same-bar with no Prime refresh.

Expected pacing:
- mandatory normal ~10–11
- completionist ~8–9

Next:
> First Command Warden


### First Command Warden recertification
Chapter-3 S020 boss now passes mandatory-vs-completionist and Power-completeness checks.

Actual route:
- mandatory 11,280 EXP = Lv11
- completionist fixed-content 14,280 EXP = Lv12, 120 short of Lv13
- optional-incidental high side ~Lv13

Raw line:
- HP **3,723 → 2,850**
- ATK **57 → 72**
- MAG **57 → 72**
- DEF43 unchanged
- Spirit43 unchanged
- SPD **29 → 30**
- EVA0 / SR10 unchanged

Direct Powers:
- Authority Lance 190
- Judgment Pulse 140 AoE
- Seal Reprisal 100
- Major Ruling 210 AoE
- Recorded Analogue 150 single / 105 AoE
- Warden Crush 245
- Challenged Verdict 230
- Command Collapse 165 AoE

Command Ring:
- 260 HP / 40 DEF / 46 Spirit
- targetable during Ruling Preparation
- disruption cancels the Ruling
- may align again after 3 rounds

Expected pacing:
- mandatory ~10–11
- completionist ~8–9

Next:
> Elder Briarhide


### Elder Briarhide recertification
S022 protected encounter now passes route-level and Power-completeness checks.

Actual access:
- mandatory Lv13
- completionist fixed-content Lv15 exactly
- high-side ~Lv16

Raw line:
- HP2,100 retained
- ATK **64 → 72**
- MAG28 retained
- DEF **44 → 60**
- Spirit **39 → 55**
- SPD36 / EVA10 / SR5 retained

Powers:
- Territorial Rush 190
- Scarred Maul 225
- Briar Sweep 125 AoE
- Guard the Den N/A
- Warning Display N/A

Round 4:
- Recovered Last Sentinel
- Sentinel Impact 340 Power / 40% Defense penetration
- Elder Briarhide retreats alive

Duration is intentionally **exactly 4 rounds** for both mandatory and completionist routes.
Optional progression improves safety rather than shortening this scripted Prime-manifestation encounter.

Next:
> Reaction Conduit


### Reaction Conduit recertification
S023 harmed-researcher stabilization encounter now passes route-level and Power-completeness checks.

Actual route:
- mandatory 15,350 EXP = Lv13
- completionist fixed-content 20,550 EXP = Lv15
- high-side ~Lv16

Raw line:
- HP **3,100 → 2,400**
- ATK **50 → 58**
- MAG **72 → 80**
- DEF **47 → 50**
- Spirit **52 → 55**
- SPD **32 → 33**
- EVA5 / SR5 unchanged

Expression cycle:
> Fire → Ice → Lightning → Earth

Powers:
- Reaction Pressure 180
- Spillway Burst 120 AoE
- Exposure Thrash 160
- Instinctive Guard N/A

Status riders remain:
- Burn20 / Freeze20 / Stun15 / Staggered20

Expected:
- mandatory ~8–9
- completionist ~6–7

0 HP resolves as stabilization, not death.

Next:
> Regulation Crucible → The Seventh Reaction


### Regulation Crucible → The Seventh Reaction recertification
Chapter-4 final boss now passes route-level, fresh-form, support-object, and Power-completeness checks.

Actual pre-boss:
- mandatory 21,462 EXP = Lv15
- completionist fixed-content 26,662 EXP = Lv17
- high-side ~Lv18

Form I:
- HP2,400 retained
- ATK54 → 64
- MAG73 → 90
- DEF51 → 54
- Spirit53 → 57
- SPD28 → 30
- Powers 185 / 100×2 / 220 / 135 AoE

Four chambers are now explicitly:
- 300 HP each
- 48 DEF / 50 Spirit
- no independent turns / Power N/A

Form II:
- HP2,900 retained
- ATK60 → 72
- MAG80 → 98
- DEF55 → 58
- Spirit57 → 62
- SPD30 → 32
- Powers 205 / 245 / 160 AoE / 2×115

Fresh Form II refreshes Prime availability.
No third form.

Expected total:
- mandatory ~13–15
- completionist ~10–12

Next:
> Furnace Tyrant


### Furnace Tyrant recertification
Recovered the established one-bar Heat identity and completed the numerical/action sheet.

Preserved prior authority:
- one continuous HP bar
- visible Heat risk/reward
- finite Furnace Servitors
- Foundry Breaker as Interruptible Preparation
- Siege Without Return as same-bar late escalation
- no second action
- Ice/environmental coolant as legal cooling
- Furnace Lash Bleed
- Foundry Breaker Staggered

Route:
- mandatory ~Lv18
- completionist ~Lv20
- high-side ~Lv21

Raw:
- HP3,801 → **3,400**
- ATK87 → **100**
- MAG51 → **72**
- DEF61 → **66**
- Spirit50 → **56**
- SPD30 → **32**

Powers:
- Furnace Lash195
- Furnace Ram235
- Scouring Jet185
- Heat Wash135 AoE
- Foundry Breaker285 AoE
- Scalding Vent150
- Overheat Vent80 AoE

Two Servitors enter once at 60% HP.
Foundry Breaker becomes eligible at 50%.
Siege Without Return begins at 30%.

Expected:
- mandatory ~9–10
- completionist ~7–8

Furnace Servitor now also has its own individual Power-authority file.

Next:
> Deepforge Colossus — Assembly Frame → Worldsmith Body


### Deepforge Colossus recertification
Recovered and preserved the Assembly Frame → Worldsmith Body functional-inheritance architecture.

Route:
- mandatory 37,678 EXP = Lv20
- completionist 45,878 EXP = Lv22
- high-side ~Lv23

Assembly Frame:
- HP3,400 retained
- ATK93 → 102
- MAG51 → 78
- SPD26 → 28
- Powers 205 / 140 AoE / 195 / 170

Assemblies:
- Guard Press HP320
- Repair Arm HP300
- Command Loom HP280
- all Power N/A
- destroyed remain destroyed
- none is a mandatory HP gate

Worldsmith Body:
- HP4,000 retained
- ATK101 → 112
- MAG62 → 90
- SPD29 → 31
- Powers 225 / 215 / 155 AoE / 260 / Forge Collapse300 AoE

Forge Collapse remains Protected Preparation.

Current global fresh-body rule supersedes historical Deepforge wording:
> Worldsmith Body refreshes Prime availability.

No Barrier mechanic was restored.

Expected:
- mandatory ~14–16 total
- completionist ~11–13

Next:
> Crownstorm Roc


### Crownstorm Roc recertification
Chapter-6 Weather Crown boss now passes route-level and Power-completeness checks.

Preserved:
- Perched Sovereign → Stormbound one-bar architecture
- no fresh-body Prime refresh
- Gale presentation is not Wind

Route:
- mandatory ~Lv23
- completionist ~Lv25
- high-side ~Lv26

Raw:
- HP5,921 → **4,800**
- ATK88 → **100**
- MAG95 → **112**
- DEF55 → **60**
- Spirit61 → **66**
- SPD41 → **43**
- EVA10 / SR10 retained

Perched Powers:
- Talon200
- Crownbolt215
- Hail Scatter135 AoE
- Gale Sweep145 AoE

Stormbound at 50% HP:
- +10 Speed
- Dive245
- Crownstorm Bolt255
- Stormglass Burst165 AoE
- Gale Pressure170 AoE

No Wind element was introduced.

Expected:
- mandatory ~9–10
- completionist ~7–8

Next:
> Matron Zevraya → Perfected War Mother


### Matron Zevraya recertification
Recovered the established Reservoir architecture before filling the missing Power sheet.

Preserved:
- Blood Matron Form I
- Sustenance / Armor / Brood / Conduction Reservoirs
- Crimson Brood as same-bar late Form-I state
- genuine fresh Perfected War Mother
- surviving-function inheritance
- voluntary/self-directed transformation
- dedicated Bleed sources only
- conditional Storm Stun / Frost Freeze through Conduction
- no Poison / Blood status / Wind / Water

Route:
- mandatory ~Lv24
- completionist fixed ~Lv27
- high-side ~Lv28

Blood Matron:
- HP5,283 → 4,400
- ATK74 → 90
- MAG104 → 122
- DEF65 → 68
- Spirit74 → 76
- SPD38 → 40

Reservoir HP:
- Sustenance320
- Armor340
- Brood300
- Conduction320

Crimson Brood:
- 45% HP
- same bar
- Crimson Arc165 AoE

Perfected War Mother:
- HP6,162 → 5,200
- ATK90 → 112
- MAG113 → 132
- DEF69 → 72
- Spirit77 → 80
- SPD39 → 42

Core direct Powers:
- Form I 205 / 225 / 145 AoE / 220
- Reservoir 190 / 200
- Form II 245 / 270 / 285 / 175 AoE
- inherited Siphon/Conduction230

Current global fresh-body rule supersedes old Zevraya-specific no-refresh wording:
> Perfected War Mother refreshes Prime availability.

No Barrier was retained from stale Reservoir language; Armor uses temporary Total Defense instead.

Expected:
- mandatory ~15–17
- completionist ~12–14

Next:
> Masked Ruin Vanguard — Seyrik


### Masked Ruin Vanguard — Seyrik recertification
Chapter-6 forced-disengagement fight now passes route-level, nonlethal, and Power-completeness checks.

Route:
- mandatory ~62,000 EXP = Lv25
- completionist fixed ~74,200 EXP = Lv27 approaching Lv28
- high-side ~Lv28–29

Raw:
- HP5,302 → **4,000**
- ATK104 retained
- MAG79 retained
- DEF63 retained
- Spirit59 retained
- SPD38 retained
- EVA5 / SR10 retained

Enemy action kit intentionally uses the eventual Ruin Vanguard coefficients:
- Ruin Cleave165
- Rift Lance175
- Ember Brand150
- Fracturing Brand145 AoE
- Unmaking Blow245

No Cards, Prime, Controlled Apocalypse, or Shardfang are used by this encounter.

Protected disengagement:
- floor **800 HP / 20%**
- crossing damage clamps
- pending Seyrik action cancels
- story sequence begins immediately

This is encounter-specific, not a global Mercy/Capture/Subdual system.

Expected:
- mandatory ~7–8
- completionist ~5–6

Next:
> Chainworks Behemoth


### Chainworks Behemoth recertification
Recovered the existing one-bar Anchor architecture and completed its action coefficients.

Route:
- mandatory ~73,300 EXP = Lv27
- completionist fixed ~95,200 EXP = Lv31
- high-side ~Lv32

Completionist proof includes:
- The Marks We Leave
- Regional Hunts #1–#6
- Major Hunt #1, unlocked after Chapter 6

Raw line:
> **RETAINED UNCHANGED — Lv29 / HP5,135 / ATK109 / MAG57 / DEF77 / Spirit59 / SPD32 / EVA0 / SR5**

Exactly 3 Restraint Anchors:
- HP240 each
- DEF72 / Spirit62
- +5 Total Defense each while Bound
- Power N/A

Transition:
- 55% HP normally
- earlier after 2+ Anchors destroyed
- same bar
- no Prime refresh

Recovered status roles preserved:
- Chain Rend = 25% Bleed
- Gate Crush = 20% Staggered single / 15% AoE

Powers:
- Bound 205 / 225 / 180 / 140 AoE
- Freed 225 / 165 AoE / 265 / 175 AoE

Expected:
- mandatory ~9
- completionist ~6–7

This is the first boss in the current route pass whose inherited raw line was explicitly retained rather than retuned.

Next:
> Warden of the Nameless / Revision Arbiter


### Warden of the Nameless / Revision Arbiter recertification
Chapter-7 climax now passes route-level, action-tax, same-bar, and Power-completeness checks.

Pre-boss:
- mandatory 92,020 EXP = Lv30
- completionist fixed 120,720 EXP = Lv34
- high-side ~Lv35

Raw:
- HP8,913 → **7,600**
- ATK112 → **124**
- MAG120 → **138**
- DEF84 → **86**
- Spirit89 → **92**
- SPD40 → **42**

Opening story/combat requirement now has an exact no-choice implementation:
- 3 Assertion Layers
- first completed ordinary action from three distinct active characters removes them
- 80% direct-damage reduction until complete
- no special sixth command
- no Barrier

Revision Claim:
- temporary 25% direct-damage-output tax
- target clears it by using a different command category
- never disables a command

Open Revision:
- 40% same-bar state
- 2 short assertion layers at 40% reduction
- no Prime refresh

Powers:
- Adjudication 220 / 145 AoE / 205 / 245
- Open Revision 280 / 270 / 180 AoE / 2×140

Expected:
- mandatory ~12–13
- completionist ~9–10

Next:
> Western Rift Engine


### Western Rift Engine recertification
Chapter-8 Horizon Vault boss now passes route-level, same-bar, finite-support, and Power-completeness checks.

Route:
- mandatory ~108,100 EXP = Lv33
- completionist fixed ~156,800 EXP = Lv39
- high-side ~Lv40 if RH#8 is legally available pre-Engine or equivalent optional combat is completed

Post-Volition optional content is intentionally allowed to create a large level spread.

Raw line:
> **RETAINED UNCHANGED — Lv36 / HP9,775 / ATK86 / MAG133 / DEF97 / Spirit89 / SPD33 / EVA0 / SR10**

Engine Core Powers:
- Rift Lance235
- Engine Shock210 / 20% Stun
- Core Pressure150 AoE
- Anchor Crush195 / 20% Staggered

Finite Rift Echo:
- one deployment at 70% HP
- HP420
- Echo Bolt165
- Echo Static145 / 15% Stun
- no replacement/respawn

Rift Incarnate:
- starts at 45% HP
- same bar
- +10 Speed / -10 Total Defense
- no Prime refresh
- Powers275 / 255 / 180 AoE / 2×140 / 165 AoE

No Spatial element was introduced.

Expected:
- mandatory ~10–11
- completionist ~7–8

Next:
> Marshal Varkesh → Rift Conqueror


### Marshal Varkesh → Rift Conqueror recertification
Chapter-8 final combat now passes exact route-level, fresh-body, story-survival, and Power-completeness checks.

Exact mandatory pre-boss:
> **128,262 EXP = Lv35**

Completionist fixed-content:
> **185,462 EXP = Lv42**

High-side:
> ~Lv43

Both inherited raw bodies are retained unchanged.

Marshal:
- Lv38 / HP7,326 / ATK140 / MAG93 / DEF93 / Spirit85 / SPD44
- Powers230 / 255 / 160 AoE / 210
- Seize Initiative N/A

Rift Conqueror:
- Lv39 / HP8,485 / ATK151 / MAG107 / DEF97 / Spirit91 / SPD45
- fresh body / Prime refresh
- Powers270 / 295 / 2×150 / 185 AoE / 195 AoE
- Tempo Dominance N/A

Varkesh tempo identity is expressed through temporary Attack/Magic/Speed boosts, never extra actions.

Rift Conqueror remains a deliberate escalation, not possession.

At 0 HP:
- Varkesh is combat-defeated;
- survives;
- successfully withdraws;
- Chapter-12 live capture remains separate.

Expected:
- mandatory ~13–15
- completionist ~10–12

Next:
> Equal Mercy Arbiter


### Equal Mercy Arbiter recertification
Chapter-9 Equal Mercy climax now passes route-level, action-tax, same-bar, and Power-completeness checks.

Route:
- mandatory ~146,800 EXP = Lv37
- completionist fixed ~225,000 EXP = Lv45
- high-side ~Lv46

Fixed optional proof includes:
- The Third Caravan
- Regional Hunts #1–#8
- Major Hunts #1–#2
- Vaelira/Cyanis/Nimera/Seyrik Character Quests

It excludes:
- RH#9 until exact pre/post-Arbiter return timing is recovered
- Major Hunt #3 until after Chapter 9
- Ilyra CQ until after Chapter 9

Raw:
> **RETAINED UNCHANGED — Lv40 / HP10,025 / ATK105 / MAG140 / DEF89 / Spirit107 / SPD43 / EVA0 / SR10**

Mercy Protocol:
- 50% round-start direct-damage reduction
- one support-only Ability/Card/Item or Defend opens full damage for rest of round
- no new command
- no Barrier/Triage resource

Open Sanctuary:
- 45% HP
- same bar
- tax ends permanently
- +10 Speed / -10 Total Defense
- no Prime refresh

Powers:
- Mercy state 235 / 215 / 155 AoE / 260
- Open Sanctuary 285 / 190 AoE / 275 / 2×145 / 250

Expected:
- mandatory ~12–13
- completionist ~9–10

Next:
> Commander Rhazek — Reforged Commander → Bastion Devourer


### Commander Rhazek — Reforged Commander → Bastion Devourer recertification
Chapter-9 climax now passes exact route-level, fresh-body, short-exposed-end, and Power-completeness checks.

Exact mandatory pre-boss:
> **173,800 EXP = Lv40**

Boss reward:
> 181,300 EXP = Lv41

Chapter clear:
> **184,300 EXP = Lv42 exactly**

Completionist fixed:
> **263,000 EXP = Lv49**

High-side:
> ~Lv50

Both inherited raw bodies are retained unchanged.

Reforged Commander:
- Lv43 / HP8,431 / ATK163 / MAG100 / DEF111 / Spirit96 / SPD44
- Powers250 / 285 / 175 AoE / 265
- Hold the Line N/A

Bastion Devourer:
- Lv44 / HP10,462 / ATK175 / MAG131 / DEF107 / Spirit104 / SPD46
- genuine fresh body / Prime refresh
- Powers295 / 325 / 205 AoE / 190 AoE / Demolition Breaker335 AoE
- Reinforced Advance N/A

Demolition Breaker:
- below 55% Form-II HP
- one-round Protected Preparation

Exposed Rhazek:
- begins at 18% Form-II HP
- same bar
- -20 Total Defense / +10 Speed
- Powers340 / 310 / 220 AoE
- no Prime refresh
- no third full-health form

Bastion integration remains voluntary, not possession.

Expected:
- mandatory ~14–16
- completionist ~11–13

Next:
> Registry Warden


### Registry Warden recertification
Chapter-10 Buried Registry threshold boss now passes exact route-level, status-neutral, same-bar, and Power-completeness checks.

Exact mandatory pre-boss:
> **224,600 EXP = Lv45**

After Warden:
> **232,600 = Lv46**

Chapter end:
> **237,600 = Lv47 exactly**

Completionist fixed:
> **331,800 EXP = Lv54**

High-side:
> ~Lv55

Completionist additions after Chapter 9:
- Ilyra CQ +10,000
- Major Hunt #3 +8,000

Raw line:
> **RETAINED UNCHANGED — Lv49 / HP13,514 / ATK157 / MAG172 / DEF124 / Spirit126 / SPD46 / EVA0 / SR10**

Closed Registry:
- Powers250 / 235 / 165 AoE / 270
- Closed Record N/A / +15 Total Defense

Open Registry:
- 40% HP same-bar
- +10 Speed / -15 Total Defense
- Powers300 / 300 / 205 AoE / 2×160 / 225 AoE
- no Prime refresh

Status-neutral rule preserved:
- no Burn
- no Freeze
- no Stun
- no Staggered
- no Bleed
- no invented Registry status

Expected:
- mandatory ~10–11
- completionist ~7–8

Next:
> Chancellor Othmar Calder — Protector of Continuity → Crown-Bound Living Anchor


### Chancellor Othmar Calder → Crown-Bound Living Anchor recertification
Chapter-11 S062 confrontation now passes route-level, fresh-body, support-object, agency, and Power-completeness checks.

Working intra-chapter ordinary allocation:
- pre-Calder 27,000
- post-Calder/deeper domain 18,300
- total remains locked 45,300

Mandatory pre-boss:
> **264,600 EXP = Lv49**

Completionist fixed:
> **399,800 EXP = Lv59**

High-side:
> ~Lv60

Both raw bodies retained unchanged.

Protector of Continuity:
- Lv54 / HP10,133 / ATK137 / MAG193 / DEF118 / Spirit134 / SPD50
- Powers270 / 185 AoE / 245 / 240 / 300
- Protector's Order N/A

Authentication Lenses:
- 2 × HP600
- Power N/A
- +5 Total Defense / +5 Base Hit each

Crown-Bound Living Anchor:
- Lv55 / HP13,662 / ATK181 / MAG204 / DEF139 / Spirit139 / SPD47
- genuine fresh body / Prime refresh
- Powers305 / 295 / 210 AoE / 290 / Continuity Collapse345 AoE
- Institutional Continuance N/A

Living Anchor Clamps:
- 2 × HP720
- Power N/A
- +5 Total Defense each
- finite Continuity Collapse load points

Continuity Collapse:
- below 60%
- Interruptible Preparation
- loaded Clamp destruction cancels
- successful resolution consumes Clamp
- maximum 2 successful resolutions

Calder remains willing/responsible; Living Anchor integration is not possession.

Expected:
- mandatory ~15–17
- completionist ~12–14

Next:
> The Custodian


### The Custodian recertification
Chapter-11 S063 now passes exact route-level, one-bar reconciliation-state, support-object, knowledge-firewall, narrative-survival, and Power-completeness checks.

The full remaining 18,300 Chapter-11 ordinary EXP is now placed in the deeper administrative route before Custodian direct contact.

Mandatory pre-Custodian:
> **286,900 EXP = Lv51**

Custodian reward:
> 289,400 EXP

Remaining Chapter-11 story rewards:
> **299,100 EXP = Lv52 exactly**

Completionist fixed:
> **422,100 EXP = Lv60**

High-side:
> ~Lv61

RH#10 remains excluded from the fixed proof until exact S063-relative access is recovered.

Raw line:
> **RETAINED UNCHANGED — Lv55 / HP16,017 / ATK177 / MAG190 / DEF144 / Spirit146 / SPD48 / EVA0 / SR10**

Acuity Node:
- HP700
- Power N/A
- +10 Base Hit / +10 Speed

Ruin Containment Seal:
- HP760
- Power N/A
- +10 Total Defense
- −15% final direct Ruin damage taken

Open Reconciliation:
- 45% HP same-bar
- surviving supports disengage
- +10 Speed / -15 Total Defense
- no Prime refresh

Powers:
- Closure 290 / 275 / 195 AoE / 315
- Open 335 / 345 / 230 AoE / 3×120 / 215 AoE

At 0 HP:
- enforcement ends;
- Custodian remains functional as the S063/S064 information interface.

Knowledge firewall preserved:
- Custodian believes the Entity was destroyed;
- it does not know one fragment survived.

Corrected Devouring Singularity's source label:
> Chapter 10 → **Chapter 11 — Custodian reconciliation**

Expected:
- mandatory ~11–12
- completionist ~8–9

Next:
> Marshal Varkesh — Final Capture


### Marshal Varkesh — Final Capture recertification
Chapter-12 S067/S068 now passes route-level, live-capture, support-object, one-bar, and Power-completeness checks.

Chapter-12 ordinary split:
- pre-Varkesh **24,000**
- post-Varkesh **23,100**
- total remains locked **47,100**

Mandatory pre-Varkesh:
> **326,100 EXP = Lv54**

Completionist fixed:
> **492,800 EXP = Lv64**

High-side:
> ~Lv65

RH#11 is excluded from the fixed proof until exact Varkesh-relative access is recovered.

Raw:
> **RETAINED UNCHANGED — Lv58 / HP17,106 / ATK226 / MAG148 / DEF144 / Spirit131 / SPD55 / EVA5 / SR10**

Supports:
- Reforged Command Standard HP900 / Power N/A
- one Varkesh Black Guard HP1,400
- East Retreat Beacon HP1,100 / Power N/A
- West Retreat Beacon HP1,100 / Power N/A

Capture floor:
- while either Beacon survives, Varkesh clamps at **3,421 HP / 20%**
- both Beacons destroyed removes floor
- 0 HP then resolves **captured alive**

Varkesh Powers:
- 315 / 340 / 220 AoE / 300
- at 50% same-bar: 365 / 245 AoE / 2×180
- no Prime refresh

Black Guard:
- 235 / 205 / Interpose N/A

This cleanly separates:
- Chapter-8 combat defeat + withdrawal
from
- Chapter-12 live capture.

Expected:
- mandatory ~11–13
- completionist ~8–10

Next:
> Emperor Vaelkor Draeven → Sovereign Panoply Unbound


### Emperor Vaelkor Draeven → Sovereign Panoply Unbound recertification
Chapter-12 S069 now passes exact route-level, fresh-body, agency, late-state, and Power-completeness checks.

Mandatory pre-Vaelkor:
> **360,700 EXP = Lv56**

Boss clear:
> 367,700 EXP = Lv56

Chapter clear:
> **369,100 EXP = Lv57 exactly**

Completionist fixed:
> **527,400 EXP = Lv66**

RH#11 pre-clear, if legal:
> 541,200 EXP = Lv67

Both inherited raw lines retained unchanged.

Emperor:
- Lv60 / HP13,648 / ATK223 / MAG209 / DEF155 / Spirit150 / SPD54
- Powers325 / 305 / 225 AoE / 315 / 205 AoE
- Imperial Guard N/A

Sovereign Panoply:
- Lv61 / HP16,615 / ATK238 / MAG224 / DEF163 / Spirit157 / SPD55
- genuine fresh body / Prime refresh
- Powers360 / 365 / 250 AoE / 2×190 / 240 AoE / Sovereign Overrun390 AoE
- Absolute Command N/A

Sovereign Overrun:
- below 55%
- one-round Protected Preparation
- 3-round repetition lock

Final Sovereignty:
- 25% Form-II HP
- same bar
- +10 Speed / -15 Total Defense
- no Prime refresh

Agency firewall:
- genuine surrender offer
- Vaelkor refuses by choice
- Panoply is deliberate human war/relic equipment
- no possession
- no third form

Expected:
- mandatory ~14–16
- completionist ~11–13

Next:
> Last Weapon Archon


### v53 — Vaelkor duration increase
User direction:
> **Vaelkor should take a little longer.**

Adjusted HP only:
- Emperor of the Reforged Host **13,648 → 14,900**
- Sovereign Panoply Unbound **16,615 → 18,100**

Unchanged:
- ATK
- MAG
- DEF
- Spirit
- SPD
- EVA
- SR
- every action Power
- status chances
- Protected Preparation
- fresh-body Prime refresh
- Final Sovereignty threshold/effects

Revised pacing:
- mandatory **~16–18 rounds**
- completionist **~12–14**
- high-side **~11–13**

This makes the Chapter-12 climax slightly longer without increasing per-hit lethality.


### v54 — Vaelkor mandatory pacing set to 18–20 rounds
User direction:
> **Make it 18–20 mandatory.**

Adjusted HP only:
- Emperor of the Reforged Host **14,900 → 16,800**
- Sovereign Panoply Unbound **18,100 → 20,200**

Unchanged:
- all non-HP raw stats
- all action Powers
- status chances
- Sovereign Overrun
- fresh-body Prime refresh
- Final Sovereignty

New expected pacing:
- mandatory **18–20**
- completionist **13–15**
- high-side **12–14**


### Last Weapon Archon recertification
Chapter-13 pre-Shelter guardian now passes exact route-level, same-bar, lore-firewall, and Power-completeness checks.

Mandatory:
- pre-boss **396,700 EXP = Lv58**
- Archon clear **408,700 = Lv59**
- Last Shelter **415,400 = Lv60 exactly**

Completionist:
- established +195,000 proof pool → **591,700 = Lv69**, 2,400 short of Lv70
- if legally available MH#6 is also cleared → **Lv70 cap**

Raw:
> **RETAINED UNCHANGED — Lv63 / HP18,424 / ATK236 / MAG220 / DEF160 / Spirit160 / SPD56 / EVA0 / SR15**

Archive Authority Powers:
- 320 / 325 / 345 / 225 AoE
- Archive Seal N/A

Weapon Protocol Unsealed:
- begins 60% HP same-bar
- +10 Speed / -10 Total Defense
- Powers365 / 385 / 270 AoE / 3×135 / 250 AoE
- Sequence Alignment N/A
- no Prime refresh

One-time visible historical sequence:
> convergence → compression → discharge

Firewall:
- Archon is not Entity intelligence
- no possession
- no second body
- does not reveal how the sole Entity fragment survived

Expected:
- mandatory ~13–15
- broad completionist ~9–11
- cap route ~8–10

Next:
> Reconstituted Entity → The Last Command


### v56 — Last Weapon Archon mandatory pacing increased
User direction:
> **Pacing should be higher — 15–17 mandatory.**

HP-only adjustment:
- Last Weapon Archon **18,424 → 20,800 HP**

Unchanged:
- all non-HP raw stats
- all action Powers
- status chances
- Weapon Protocol Unsealed threshold
- same-bar behavior
- Prime-refresh behavior

Revised expected pacing:
- mandatory **15–17**
- broad completionist **10–12**
- Lv70 cap **9–11**


### Reconstituted Entity → The Last Command recertification
The mandatory story-boss route pass now reaches and closes the final boss.

Exact mandatory pre-boss:
> **432,600 EXP = Lv61**

After final combat:
> **446,100 EXP = Lv61**

After Final Severance:
> **448,100 EXP = Lv62 exactly**

Completionist reference:
> **Lv70 cap**

Final-boss HP pacing:
- Reconstituted Entity **15,074 → 22,500 HP**
- The Last Command **19,367 → 28,500 HP**
- all non-HP raw stats retained

Form I Powers:
-350 /365 /380 /240 AoE /225 AoE
- Reconstitute N/A

Heart Manifestation:
- max1 at65%
- HP1,100
- Power N/A
- same sole Entity continuity

Crest Integration:
- genuine fresh-body transition
- Prime availability refreshes

Form II Powers:
-390 /405 /410 /280 AoE /265 AoE /2×210 / Final Directive430 AoE
- Absolute Continuity N/A

Unbound Shards:
- max2 at70%/40%
- HP1,050 each
- Power N/A
- same sole Entity continuity

Distributed Command:
-25% same-bar
- +10 Speed / -15 Total Defense
- no Prime refresh

Expected:
- mandatory **22–24**
- Lv70 completionist **18–20**

At The Last Command 0 HP:
- combat ends
- no third form
- Final Severance begins

Final Severance is a story-resolution manifestation sequence, so required Story Prime roles are not blocked by combat once-per-form usage flags.

Final ontology firewall preserved:
- exactly one surviving continuity
- no second fragment/copy/branch
- exact ancient survival mechanism remains OPEN

### Mandatory story-boss route pass
> **COMPLETE THROUGH FINAL BOSS**

Next:
> broader enemy-action Power audit for remaining ordinary enemies / Elites / unresolved supports


### v58 — Broader enemy Power audit begins / Chapter 1 closed
The post-boss broad enemy-action audit has begun.

Chapter 1 is now the first fully certified ordinary/Elite/authored batch.

New individual Chapter-1 ordinary authorities:
- Black Host Raider
- Black Host Crossbowman
- Ruin Shieldbearer
- Brackenwall Reaver
- Greenhollow Stalker
- Thornvine Creeper
- Briar Boar
- Hollow Watch Sentry
- Hollow Watch Ballista

All now have:
- chapter-specific raw bodies
- exact direct-damage Power
- Base Hit
- typing
- current legal riders
- Power N/A on non-damage actions

Hollow Watch teaching relationship is now exact:
- Sentry uses interruptible Targeting Signal
- ordinary Ballista Snap Bolt135
- marked Heavy Bolt200
- mark can be prevented by damaging/defeating the preparing Sentry

Briarhide Stalker:
- raw Lv4 / HP850 retained
- Powers155 /135 /110 AoE
- targetable Black Host Irritant Fitting HP180 / Power N/A
- Briarhide protected floor213 /25% while fitting survives
- fitting0 ends fight nonlethally

Watch Captain Frame:
- raw Lv6 / HP820 retained
- Powers175 /125 AoE /210
- Watchline Guard N/A

Status rollout:
- no Burn/Stun/Freeze introduced in Ch1
- Bleed is the only harmful rider used by this batch
- Hollow Watch constructs are Bleed Immune

### Chapter 0 audit discovery
Line-complete current Chapter-0 S005 explicitly names:
- Convoy War-Sorcerer
- injured Iron Cohort Soldier
- Rift Lance Preparation from Round2 onward

The migrated Chapter-0 enemy roster still contains an unreconciled older identity set including Riftmaw.

Chapter 0 is therefore **not** falsely marked Power-complete.

Next:
> Chapter 2 ordinary enemies + Archive Duplicant, while Chapter-0 encounter identity remains a separate reconciliation item.


### v59 — Chapter-0 Riftmaw preservation correction
User correction:
> **Riftmaw should still be in Chapter 0.**

Confirmed and preserved.

The v58 audit wording incorrectly framed S005's Convoy War-Sorcerer + injured Iron Cohort Soldier as a potential roster conflict with Riftmaw.

Correct interpretation:
- **Riftmaw remains the Chapter-0 mandatory named/boss encounter.**
- Ruin Vanguard Pursuer remains Seyrik under concealed identity.
- S005 Convoy War-Sorcerer + injured Iron Cohort Soldier is additional/current Chapter-0 combat content.
- The S005 encounter does not replace, retire, merge with, or rename Riftmaw.

The remaining Chapter-0 audit task is:
> reconcile exact encounter order and action sheets while keeping Riftmaw intact.

No Chapter-1 balance values were changed by this correction.


### v60 — Chapter 2 broad enemy Power batch closed
Chapter 2 ordinary / authored / Elite combat now has individual Power/raw authority.

Completed ordinary/carryover identities:
- Redwater Initiate
- Bogshell
- Cistern Leech
- Archive Current
- Memory Scribe
- Vault Sentinel
- Drowned Archive Maw
- Bastion Shield Guard
- Bastion Crossbow Guard
- Transfer Adept
- Black Host Raider — Chapter-2 variant
- Beast Handler — Chapter-2 variant
- Rift Hound — Chapter-2 variant

Memory Scribe:
- records only after eligible action completion
- no command prediction
- copied direct damage = **65% source total Power**
- clamp **80–180**
- copied statuses/penetration/resource effects removed

Archive Duplicant:
- raw Lv9 /HP1,000 retained
- Powers180 /145 AoE
- copied direct damage = **80% source total Power**
- clamp **110–240**
- Guard N/A

Hold the Junction:
- exactly one authored combat
- fixed Shield Guard + Crossbow Guard + Transfer Adept + Rift Hound
- no second wave / reinforcements
- fixed 350 EXP /30 CEXP story payout

Chapter-2 status rollout:
- Burn introduced through Redwater Initiate and Transfer Adept
- Bleed retained
- no Stun
- no Freeze
- water/current presentation uses Ice where applicable

Regional Hunt #2 is not silently certified by this ordinary/Elite pass.

Next:
> Chapter 3 ordinary enemies + Grand Inquisitor Frame + lawful nonlethal encounter kits


### v61 — Chapter 3 broad enemy Power pass
Chapter 3 current line-complete combat has been numerically closed except for one roster-placement identity.

Ordinary identities completed:
- Way-Fort Marauder
- Rift Boltman
- Black Host Ward-Sorcerer
- Archive Scribe Engine
- Judgment Frame
- Erasure Wisp
- Command-Station Sentry
- Authority Lens
- Command Ring Drone

Status rollout:
> **Stun introduced in Chapter 3**

Stun sources are bounded and use existing status rules.
Freeze remains for Chapter 4.

S018 confrontation I:
- Ivory Watch Guard
- Royal Polearm Officer
- Ivory Crossbow Sentinel
- all resolve nonlethally at0 HP
- no personal loot
- Order Clerk remains noncombat
- reward400 EXP /24 CEXP

S018 confrontation II:
- Ivory Adjudicator Sereth alone
- Lv12 /HP950
- Powers190 /135 AoE /175 Lightning
- protected contradiction threshold **333 HP /35%**
- threshold immediately opens Ledger declaration section and ends combat
- all five player command categories remain available
- reward500 EXP /30 CEXP

Grand Inquisitor Frame:
- raw Lv14 /HP1,450 retained
- Powers220 /155 AoE /235 Lightning
- 25% Stun on Lock Sequence
- Guard N/A

### False-Warrant Adept
The migrated roster retains this identity, but current line-complete S018 never names or places it.

No recovered current kit or formation placement exists.

Therefore it is:
> **RETAINED / PLACEMENT OPEN / DO NOT SPAWN YET**

This avoids falsely identifying a culprit or altering the approved lawful-authority scene.

Regional Hunt #3 remains outside this ordinary/Elite batch.

Next:
> Chapter 4 ordinary enemies + Annex Duelist + authored nonlethal/special kits


### v62 — Chapter 4 broad enemy Power pass
Chapter 4 ordinary / Elite / protected-roster action coverage is now complete.

Ordinary:
- Reaction Node
- Composite Elemental
- Reaction Hound
- Element Mirror
- Annex Crucible Guard

All now have exact:
- raw bodies
- Power
- Base Hit
- damage type
- legal riders

### Freeze rollout
Chapter 4 now explicitly introduces:
> **Freeze**

Freeze appears on:
- Reaction Node Ice assignment20%
- Composite Elemental Ice expression20%
- Reaction Hound Frostbite Snap20%
- Annex Battle Mage Ice stance20% if separately placed
- Annex Duelist Ice state25%

No Wind/Water element restored.

### Element Mirror
The Mirror now copies:
> **element only**

Element Return always uses fixed180 Power.

It does not copy source Power/status/target shape, avoiding an unbounded copied-action mechanic.

### Protected Annex staff
Elemental Researcher:
-150 /115 AoE

Annex Battle Mage:
-175 /135 AoE

Crucible Attendant:
-155 /145

All are nonlethal Power-complete roster identities.

But:
> **they do not random-spawn and are not inserted into current mandatory line-complete scenes**

S023 explicitly says academy staff are not random enemies.

Elemental Researcher is not automatically identified as the Reaction Conduit victim.

### Annex Duelist
Inherited raw:
> Lv18 /HP1,700 /72 ATK /72 MAG /50 DEF /49 Spirit /34 SPD

One bar / exactly four states:
> Fire → Ice → Lightning → Earth

Thresholds:
> 75% /50% /25%

Powers:
-210
-240 current element
-170 AoE current element
-2×130
- Recenter N/A

No state refill, free action, or Prime refresh.

### Existing mandatory Chapter-4 encounters
Unchanged and already complete:
- Elder Briarhide
- Reaction Conduit
- Regulation Crucible → The Seventh Reaction

Regional Hunt #4 remains separate.

Next:
> Chapter 5 ordinary enemies + Ruin Forgemaster + Highland Resistance Fighter nonlethal kit


### v63 — Chapter 5 broad enemy Power pass
Chapter 5 ordinary / Elite / protected enemy actions are now Power-complete.

Ordinary identities:
- Furnace Cohort
- Black Host Forge Guard
- Siege Engineer
- Furnace Servitor
- Ruin Hammerman
- Deepforge Repair Frame
- Deepforge Lifter
- Molten Crawler

### Furnace Servitor
Ordinary Chapter-5 body:
> Lv19 / HP380 / MAG78 / DEF44 / Spirit47 / SPD31

Existing action kit remains:
- Scalding Vent150 Fire /20% Burn
- Feed Furnace N/A
- Overheat Vent80 AoE /10% Burn on eligible defeat trigger

Furnace Tyrant finite support instance remains:
> **HP280**

The two bodies are not conflated.

### Highland Resistance Fighter
New exact combat kit:
- Lv18 /HP520
- Resistance Strike165
- Driving Blow185 /15% Staggered
- Covering Sweep125 AoE
- Hold Ground N/A
- 0 HP = nonlethal yield/disarm

Chapter 5 is not line-complete.

Therefore:
> exact scene placement / formation / story reason / fixed reward remain OPEN.

No new resistance faction name or culprit framing is invented.

### Ruin Forgemaster
Inherited raw retained:
> Lv23 /HP2,250 /ATK88 /MAG62 /DEF64 /Spirit57 /SPD31

Powers:
- Forgemaster Hammer240
- Ruin Temper225 Ruin /20% Staggered
- Cinder Break210 Fire /25% Burn
- Anvil Sweep175 AoE
- Temper Armor N/A

No second form or support wave.

### Status usage
Chapter 5 introduces no new harmful status.

It reuses the already established status set.

### Existing mandatory bosses
Unchanged:
- Furnace Tyrant
- Deepforge Colossus
- mandatory support objects

Regional Hunt #5 remains separate.

Next:
> Chapter 6 ordinary enemies + Crimson Progenitor + authored Weather Crown/Crimson special identities


### v64 — Chapter 6 broad enemy Power pass
Chapter 6 ordinary / Elite / authored-special enemy actions are now Power-complete.

Ordinary identities completed:
- Weather Crown Adept
- Storm Feather
- Crown Perch Sentinel
- Storm Roc Juvenile
- Black Host Sky Skirmisher
- Ruin Vanguard Reaper
- Black Host War-Sorcerer
- Ruin Marker
- Rift Hound — Chapter-6 variant
- Iron Maw
- Blood Attendant
- Weather Crown Parasite

### Weather / element firewall
Standard elements remain:
> Fire / Ice / Lightning / Earth

`Gale` remains Physical / Neutral or Colorless presentation where authored.

No Wind.
No Water.

### Crimson-work firewall
No:
- Poison
- Blood status
- Blood element
- generic life-force resource

Blood/Crimson wording remains presentation/lore only.

### Authored-special identities
Weather Crown Shield Guard:
- 180 Physical /170 Lightning
- Guard N/A
- exact placement bounded

Blood Husk:
-205 /195 Ruin /145 AoE
- exact placement/outcome bounded

Perfected Soldier:
-225 /220 Ruin /150 AoE
- one capped180 HP Stabilize
- exact placement/outcome bounded

All three:
> do not random-spawn

### Rift Hound
Chapter-6 body is now separate from Chapter 2:
> Lv25 /HP720 /ATK92 /MAG50 /DEF53 /Spirit45 /SPD39

Powers:
-185
-180 Ruin /20% Bleed
-155 AoE

### Crimson Progenitor
Inherited raw retained:
> Lv28 /HP2,700 /ATK92 /MAG104 /DEF69 /Spirit72 /SPD38

Powers:
-245 /25% Bleed
-250 Ruin
-180 AoE
-270 /25% Staggered
- Adaptive Growth N/A

One bar.
Engineered non-person organism.
No infinite brood loop.

### Already-complete Chapter-6 mandatory content
Unchanged:
- Crownstorm Roc
- Matron Zevraya → Perfected War Mother
- four Reservoirs
- finite Brood organisms
- Masked Seyrik forced disengagement

Regional Hunt #6 remains separate.

Next:
> Chapter 7 ordinary enemies + First Registrar's Shade + Beast Handler / Bound Rift Hound authored kit


### v65 — Chapter 7 broad enemy Power pass
Chapter 7 ordinary / Elite / authored-protected enemy actions are now Power-complete.

Ordinary identities completed:
- Occupation Infantry
- Brand Enforcer
- Chain Enforcer
- Red Brand Adept
- Beast-Pen Stalker
- Rift Gate Trooper
- Rift Artillerist
- Gate Projector Drone
- Registration Guard
- Name Clerk
- Redaction Adept
- Role Echo
- Nameless Executor

### Role Echo
Replayed Role is now bounded:
> **70% of completed source total Power, clamp100–220**

It:
- records only after the source action resolves;
- never predicts commands;
- copies no statuses/penetration/resource effects;
- cannot copy Prime commands;
- cannot change permanent class/identity/equipment/Card state.

### Prison identity-system firewall
Name Clerk / Redaction Adept / Role Echo / Nameless Executor / First Registrar's Shade presentation never allows permanent:
- renaming;
- level/class deletion;
- equipment removal;
- Card/ability erasure;
- command-category removal;
- save-state alteration.

### Beast Handler + Bound Rift Hound
Chapter-7 Handler:
> Lv29 / HP780 / ATK108

Powers:
- Handler Lash170
- Drive the Bound Hound N/A
- Handler Guard N/A

Bound Rift Hound:
> Lv29 / HP920 / ATK118 / SPD42

Powers:
- Bound Pounce205
- Ruin Bite195 /20% Bleed
- Chain Rush155 AoE

Exact authored placement/end condition remains open.
The balance pass does not declare the Hound killed at0 HP.

### Other authored/protected
Resistance Saboteur:
-175 /190 Fire /130 AoE
- placement/outcome bounded

Controlled Prisoner:
-165 /115 AoE
- Resist Command N/A
- 0 HP is nonlethal combat incapacity
- exact control mechanism remains story-owned

Command-Seal Warden:
-220 /155 AoE /215 Lightning
- Command Guard N/A
- does not remove player command categories

All remain non-random authored identities.

### First Registrar's Shade
Inherited raw retained:
> Lv33 / HP2,950 / ATK104 / MAG116 / DEF76 / Spirit82 / SPD44

Powers:
-245
-180 AoE Ruin
-265 /20% Staggered
-250 Lightning /25% Stun
- Preserve Record N/A

One bar.
No permanent-state erasure.

Existing Chainworks Behemoth / Restraint Anchors and Warden of the Nameless / Revision Arbiter remain unchanged and complete.

Regional Hunt #7 remains separate.

Next:
> Chapter 8 ordinary enemies + Conqueror Legate + remaining Western Rift/Westguard authored special identities

### v66 — Chapter 8 broad enemy Power pass
Chapter 8 ordinary / Elite enemy actions are now Power-complete.

Ordinary identities:
- Veteran Ruin Cohort
- Conqueror Shieldbearer
- Rift Cannoneer
- Anchor Technician
- Western Engine Frame
- Rift Siege Hound
- Western War-Sorcerer
- Varkesh Tactician
- Conqueror Executioner — rare

### Spatial/system firewall
No:
- Spatial damage element
- grid
- rows
- adjacency
- hidden severance gauge
- bonus/extra ordinary actions
- command-reading AI

Rift / anchor / tactical presentation uses existing systems only.

### Varkesh Tactician
Planning is represented by a selected support action:
- Attack +10%
- Magic +10%
- Base Hit +10
- no extra action

It never reads unconfirmed player commands.

### Anchor Technician
- Anchor Arc190 Lightning /15% Stun
- Stabilize Unit restores220 HP, max2 successes
- Vector Calibration Base Hit+10
- support actions Power N/A

No universal Anchor resource/system is created.

### Conqueror Executioner
Remains:
> **rare ordinary**

It is not promoted to a second optional Elite.

### Conqueror Legate
Inherited raw retained:
> Lv38 /HP3,650 /ATK138 /MAG102 /DEF97 /Spirit88 /SPD43

Powers:
-280 /25% Bleed
-295 /20% Staggered
-275 Ruin
-205 AoE
- Command Posture N/A

One bar.
No support wave or extra action.

### Authored/protected correction
Current Chapter-8 roster contains:
> **none**

The prior queue phrase referencing remaining Western Rift / Westguard authored-special identities was overly broad.

No such identities are invented in v66.

Existing Western Rift Engine / Rift Echo and Marshal Varkesh / Rift Conqueror certifications remain unchanged.

Regional Hunt #8 remains separate.

Next:
> Chapter 9 ordinary enemies + Ruin Breach Captain + Mercy Warden / Relay-Fever Patient authored kits

### v67 — Chapter 9 broad enemy Power pass
Chapter 9 ordinary / Elite / authored-protected actions are Power-complete.

Completed ordinary/carryover:
Triage Automaton, Recovery Hound, Quarantine Custodian, Veteran Ruin Cohort Ch9, Western War-Sorcerer Ch9, Conqueror Shieldbearer Ch9, Rift Cannoneer Ch9, Siege Engineer Ch9.

Medical/quarantine firewall:
> no Poison / disease meter / Triage resource / universal Mercy command.

Mercy Warden:
- Lv39 / HP1,650
- Powers210 /155AoE /220 Lightning
- Guard N/A
- 0 HP nonlethal
- no random spawn

Relay-Fever Patient:
- Lv38 / HP1,100
- Powers155 /165 Lightning /110AoE
- Resist the Surge N/A
- never random
- 0 HP = stabilized / safely restrained
- no death presentation / patient loot

Ruin Breach Captain retained raw:
> Lv44 / HP4,350 / ATK160 / MAG120 / DEF108 / Spirit99 / SPD46

Powers300 /310 Ruin /220AoE /285 Fire; Breach Command N/A.

Equal Mercy Arbiter and Rhazek → Bastion Devourer remain unchanged.
Regional Hunt #9 remains separate.

Next:
> Chapter 10 carryover ordinary enemies + no-Elite exception + Registry Warden handoff verification

### v68 — Chapter 10 reused-enemy Power pass
Chapter 10 is numerically closed around its deliberate reuse architecture.

Exactly:
> **8 reused ordinary identities / 0 new ordinary identities**

Chapter-10 bodies/action variants now exist for Thornvine Creeper, Briar Boar, Archive Scribe Engine, Judgment Frame, Erasure Wisp, Command-Station Sentry, Authority Lens, and Command Ring Drone.

No renamed clones were created.

Optional Elite:
> **NONE — INTENTIONAL**

Authored/protected:
> **NONE**

Regional Hunt:
> **NONE**

Registry Warden handoff verified unchanged:
- Lv49 / HP13,514 / ATK157 / MAG172 / DEF124 / Spirit126 / SPD46
- Closed:250 /235 /165AoE /270; Closed Record N/A
- Open:300 /300 /205AoE /2×160 /225AoE
- one bar
- Open Registry at40%
- no refill
- no Prime refresh
- no support wave
- status-neutral

Next:
> Chapter 11 ordinary enemies + Perfect Administrator + Crown Engine Technician authored nonlethal kit

### v69 — Chapter 11 broad enemy Power pass
Chapter 11 ordinary / Elite / authored-protected actions are Power-complete.

Ordinary identities:
Crown Engine Sentinel, Continuity Adjudicator, Emergency Executor Frame, Administrative Sentinel, Permission Scribe, Might Bastion, Element Matrix, Grace Curator, Change Schema.

Face-name firewall:
> enemy Might / Elements / Grace / Change terminology does not grant Cards or Prime Invocation.

Element Matrix uses only Fire / Ice / Lightning / Earth.

Permanent-state firewall:
> Continuity / Permission / Change / administrative presentation cannot permanently rename characters, alter levels/classes, remove equipment, erase Cards/abilities/commands, or alter save data.

Crown Engine Technician:
- Lv48 /HP1,260
-185 /195 Lightning /135 Fire AoE
- Protect Position N/A
- nonlethal at0 HP
- no death presentation / no random spawn
- placement bounded

Perfect Administrator retained:
> Lv55 /HP5,800 /ATK180 /MAG198 /DEF137 /Spirit141 /SPD52

Powers310 Hybrid /300 Ruin /220AoE /2×165; Absolute Procedure N/A.
One bar; no support wave/transformation/permanent state erasure.

Calder and Custodian encounter/support files remain unchanged.
Regional Hunt #10 remains separate.

Next:
> Chapter 12 ordinary enemies + Lord-Marshal Kharvek + Compelled Relay Bearer authored nonlethal kit


### v70 — Chapter 12 broad enemy Power pass
Chapter 12 ordinary / Elite / authored-protected actions are now Power-complete.

Ordinary identities:
- Reforged Legionary
- Imperial Bulwark
- Imperial Pursuit Lancer
- Host Field Chirurgeon
- Veiled Blade
- Crimson Veil Adept
- Purple Veil Adept
- Sovereign's Royal Guard
- Black Host Crown Knight
- Throne Deacon
- Renewal War-Sorcerer

### Civilian firewall
Chapter-12 story rule reaffirmed:
> **civilian populations are not default enemy combatants**

The ordinary roster represents the imperial military/armed command machine, not the civilian population.

### Veil/color firewall
Crimson/Purple naming does not create Blood/Purple elements or Poison.

Elements remain Fire / Ice / Lightning / Earth.
Ruin remains a special school.

### Compelled Relay Bearer
- Lv55 / HP1,420
- Compelled Strike175
- Relay Discharge190 Lightning /15% Stun
- Relay Surge125 AoE
- Resist the Relay N/A
- never random
- 0 HP = safely disabled / disconnected from immediate relay crisis
- no death presentation / no personal loot
- exact compulsion mechanism remains story-owned
- no possession or universal control status is asserted

### Lord-Marshal Kharvek
Inherited raw retained:
> Lv61 / HP6,750 / ATK224 / MAG166 / DEF152 / Spirit142 / SPD56

Finite support:
> **1 Imperial Bulwark — Chapter-12 body**

Powers:
-325 /25% Bleed
-315 Ruin
-345 /25% Staggered
-235 AoE
- Marshal Order N/A

One bar.
No transformation.
No support respawn.
No extra action.
No Prime refresh.

Existing Varkesh Final Capture, mandatory Varkesh supports, and Vaelkor two-form encounter remain unchanged.

Regional Hunt #11 and its Authority/Renewal Attendant Frames remain separate.

Next:
> Chapter 13 ordinary enemies + Devourer of Names + final Last Weapon / Entity ordinary-support handoff verification


### v71 — Chapter 13 broad enemy Power pass
Chapter 13 ordinary / Elite / final-support actions are now Power-complete.

Ordinary identities:
- Hunger Aspect
- Ruin Aspect
- Silence Aspect
- Fear Aspect
- Devouring Echo
- Terrain Maw
- Empty Sky Wraith
- Dying-Light Wisp
- Calamity Memory

### Sole-continuity firewall
Hunger / Ruin / Silence / Fear Aspects are expressions of:
> **the same sole Reconstituted Entity continuity**

They are not extra surviving fragments, souls, copies, or sequel seeds.

Devouring Echo and Calamity Memory likewise do not create independent surviving Entity continuities.

### Status/element firewall
No Silence/Fear/Name status.

No Wind/Light/Dark/Void normal element.

Standard elements remain Fire/Ice/Lightning/Earth.
Ruin remains a special school.

### Copy mechanics
Devouring Echo:
> 75% completed source total Power / clamp120–260

Calamity Memory:
> 85% completed source total Power / clamp140–300

Both record only after an eligible direct-damage action completes and cannot copy Prime commands or permanent state.

### Devourer of Names
Inherited raw retained:
> Lv63 / HP7,000 / ATK216 / MAG230 / DEF151 / Spirit159 / SPD57

Powers:
-330 Ruin /25% Bleed
-325
-235 AoE Ruin
-350 /25% Staggered
- Guard N/A

At60%:
> exactly one Consumed Echo

Consumed Echo:
- HP900
- Power N/A
- no independent turn
- no repair/respawn
- Magic+10% / +10 Total Defense while functional

No permanent identity/name/progression erasure.

### Final handoff verification
Unchanged:
- Last Weapon Archon — no support wave
- Heart Manifestation — max1 / Power N/A
- Reconstituted Entity → The Last Command
- Unbound Shards — max2 / Power N/A

Fresh Last Command remains the only fresh-body Prime refresh in the final encounter.

No third form.
No hidden continuity.
Exact ancient Entity-fragment survival mechanism remains OPEN.

### Numbered-chapter audit milestone
Broad ordinary/Elite enemy Power audit:
> **CHAPTERS 1–13 COMPLETE**

Remaining separate enemy-completeness work:
> Chapter 0 S005 / Riftmaw encounter-order and remaining-kit reconciliation


### v72 — Chapter 0 encounter-order + remaining-kit reconciliation
The final unresolved chapter-enemy Power block is closed.

### Exact encounter placement
Line-complete transitions are preserved.

S001 opening-combat segment:
1. Black Host Raider + Black Host Crossbowman + Ruin Shieldbearer
2. Beast Handler + Convoy Rift Hound
3. Ruin Vanguard Pursuer
4. Riftmaw

S002:
> exactly one Convoy Rift Hound

S003:
> no combat

S004:
> direct transition from S003 / no standalone battle before S005

S005:
> Convoy War-Sorcerer + injured Iron Cohort Soldier

S006:
> no combat

### Riftmaw
Explicitly retained:
> **mandatory named/boss / Lv4 / HP760**

Powers:
-165
-175 Ruin
-120 AoE Ruin
- Maw Guard N/A

No harmful-status rider.

### Ruin Vanguard Pursuer
Seyrik remains concealed.

Raw:
> Lv4 / HP620

Powers:
-150
-155 Ruin
- Guard N/A

Encounter ends at70% HP or after2 full rounds, whichever comes first.
Pursuer retreats alive.
No identity reveal.

### S005
Convoy War-Sorcerer:
> Lv4 / HP620 / MAG40

Powers:
-140
-100 AoE
-210 Ruin

Rift Lance Preparation:
> Round2 or later only / Power N/A / once per battle

Injured Iron Cohort Soldier:
> Lv3 / HP165

Powers:
-110
-125
- Cover the Sorcerer N/A

Victory:
> War-Sorcerer reaches0 HP

If Soldier remains active:
> withdraws through east cut.

### Incomplete Card response
S005 Rounds1–3:
> Cyanis + Ilyra **+15 Total Defense**

This is authored protection only:
- no Prime activation
- no selectable Card use
- no summon
- no MP cost
- no Prime-use flag

The visual fractured geometry may remain until the post-battle fade.

### Chapter-0 status/progression boundary
No harmful party statuses in Chapter 0.
Player Level remains static.

### Audit milestone
Broad ordinary / Elite / authored chapter-enemy Power audit:
> **CHAPTERS 0–13 COMPLETE**

Regional Hunts and Major Hunts remain separate from this chapter-pass closure.


### v73 — Regional Hunt Power closure
All 11 Regional Hunts are now Power-complete.

Raw stats, recommendations, access timing, and fixed scaling remain unchanged.

### Early status chronology
RH1:
> Bleed only; no Burn/Stun/Freeze

RH2:
> Burn/Bleed legal; no Stun/Freeze

RH3:
> Stun legal; no Freeze

RH4 onward:
> full established harmful-status vocabulary available

No Poison/Silence/Fear/Name/Blood status is created.

### Regional Hunt #6
Winterglass Titan:
> Frozen Shell → Thawed Core is same-bar

At50%:
- Shell defense ends
- Speed+10
- ATK/MAG+10%
- no HP refill
- no Prime refresh

### Regional Hunt #7
Rift Gate Colossus:
> one bar

At50%:
> same-bar Marching Protocol

No fresh body / Prime refresh.

### Regional Hunt #10
Authority Remnant:
> one bar / finite Echo machinery / not Entity

At70% and35%:
- one Echo Node
- max2
- HP1,050
- no independent turn
- Power N/A
- each gives MAG+5% / +5 Total Defense
- no respawn

### Regional Hunt #11
Sealed Throne:
> Lv61 / HP11,800

Walking Throne:
> Lv62 / fresh HP14,200

Total:
>26,000 raw boss-body HP

Prime availability refreshes at Walking Throne.
No third form.

Authority Attendant Frame:
- HP1,450
- Power N/A
- ATK+10% / MAG+10% / Base Hit+5 while functional

Renewal Attendant Frame:
- HP1,350
- Power N/A
- heals450 after Throne action
- max3 successful triggers encounter-wide

Surviving Frames carry into Walking Throne without repair/refresh.

### Audit milestone
Regional Hunts:
> **#1–#11 POWER COMPLETE**

Next:
> Major Hunts #1–#6 action-kit Power closure


### v74 — Major Hunt action-kit Power closure
All six Major Hunts are now Power-complete.

No current recertified raw stat line or unlock timing was changed.

### Major Hunt #1 — Ashen Whitehorn
Powers:
-315
-295
-215 Ice AoE
-380 Last Run

Last Run:
> at30% same-bar / ATK+15% / SPD+10 / Total Defense−10

No Prime refresh.

### Major Hunt #2 — Crownless Siege Marshal → Crownless War Engine
Marshal:
-340
-325 Ruin
-245 AoE
- Guard N/A

War Engine:
-390
-380 Ruin
-285 Fire AoE
-365 Lightning
-430 AoE Overrun after Preparation

Fresh body:
> Prime availability refreshes at War Engine

No third form.

The stale Hunt Balance Certification line showing9,360+11,650 was corrected to the current recertified:
> **13,600 +16,900 =30,500 HP**

### Major Hunt #3 — Concordance Guardian
Six Faces rotate:
> Might → Elements → Grace → Acuity → Change → Ruin

Face Verdict has exact Face-specific Power.

At50%:
> Open Concordance same-bar

No Prime refresh.
Enemies do not use Cards/Prime Invocation.

### Major Hunt #4 — Worldscar Leviathan
Four-element cycle:
> Fire → Ice → Lightning → Earth

At50%:
> Prismatic Confluence same-bar

Confluence Spear:
>2×215 =430 total

Maximum one newly inflicted harmful status from the command.

No Prime refresh.

### Major Hunt #5 — Final Archive Arbiter
Custody Protocol:
> +10 Total Defense outside Transfer Windows

Archive Burden:
>70% /40%, max2, each Magic+5% / Total Defense−5

Transfer Windows:
> rounds3/6/9/... / Custody bonus suspended / Spirit−15

Transfer Sever:
>2×245 =490 total

No new player command or permanent-state effect.

### Major Hunt #6 — The Unfinished World
Exactly:
> one78,000-HP bar

States:
- WORLDFRAME —100%→70%
- WORLDHEART EXPOSED —70%→35%
- FINAL CONSTRUCTION —35%→0

No state refreshes Prime availability.

Highest prepared attack:
> Worldfall —450 Power per target Hybrid/Ruin after Worldfall Preparation

No fourth state / hidden HP body.

### Hunt Power milestone
Regional Hunts:
> **#1–#11 POWER COMPLETE**

Major Hunts:
> **#1–#6 POWER COMPLETE**

Whole Hunt direct-damage Power audit:
> **COMPLETE**


## v75 cleanup
- Direct-damage enemy/boss Power authoring audit is **CLOSED** across Chapters 0–13, Regional Hunts #1–#11, and Major Hunts #1–#6.
- Remaining combat-balance task is **Enemy & Boss Mandatory-vs-Completionist Validation**, covering ordinary enemies, Elites, authored encounters, story bosses, Regional Hunts, Major Hunts, formations, and supports.
- Power values are not globally reopened by that validation; tune a specific coefficient only when a specific encounter fails.
- CEXP next-pass target updated to **Player Lv55–60** for full Base + Subclass completion.
- CEXP recalibration is sequenced **after** enemy/boss mandatory-vs-completionist validation.
- Old active wording that treated Lv53–57 or Lv62 as the final CEXP acceptance target is superseded.


### v76 — Chapter 0 mandatory-vs-completionist validation
- Restored exact Player-Level neutral natural-stat formulas to active progression authority.
- Recorded guaranteed Chapter-0 Cyanis/Ilyra starting loadouts for reproducible combat bodies.
- Added 3 guaranteed Field Salves as finite Chapter-0 convoy issue; normal shop unlock remains Chapter 1.
- S005 now has an explicit fresh-start recovery boundary: Cyanis + Ilyra begin at full HP/full MP before battle initialization; this is not a Card/Prime effect.
- Validated Chapter-0 ordinary/authored/Elite pressure against actual Lv1 mandatory body.
- Riftmaw failed on excessive solo durability, not offensive Power.
- Riftmaw HP adjusted **760 → 340**.
- No Riftmaw action Power, ATK, MAG, DEF, Spirit, Speed, status, or architecture changed.
- S005 War-Sorcerer + injured Soldier passed against Cyanis + Ilyra with the established three-round +15 Total Defense protection.
- Chapter 0 completionist baseline is identical to mandatory baseline; no optional progression exists early enough to create a meaningful split.
- Next balance frontier: Chapter 1 ordinary formations, Watch Captain Frame, authored/nonlethal content, and Regional Hunt #1 while carrying forward the already-recified Hollow Watch Castellan boss line.


### v77 — Chapter 1 mandatory-vs-completionist validation
- Locked Chapter-1 testing to actual progression points: **Lv1 start → Lv5 end**, with S008 around Lv2 mandatory / Lv3 high-side.
- Chapter-1 ordinary enemy roster validated with **no raw-stat or Power changes**.
- Hollow Watch Sentry → Ballista interrupt-teaching relationship validated at actual ~Lv2.
- Briarhide Stalker / Irritant Fitting nonlethal objective validated at ~Lv3 with no changes.
- Hollow Watch Castellan's corrected ~Lv2/~Lv3 package validated and retained.
- Watch Captain Frame failed its 2–4 serious-round Elite target at actual Hollow Watch access.
- Watch Captain Frame HP adjusted **820 → 500**. All ATK/MAG/DEF/Spirit/SPD/EVA/SR, actions, status rules, and direct-damage Powers retained.
- Cistern Devourer validated as intentionally early-available after S011 but fixed **Lv7 recommended**; no dynamic scaling and no stat/Power change.
- Chapter 1 validation status: **ADJUSTED / VALIDATED**.
- Global direct-damage Power audit remains **CLOSED**.
- Next validation frontier: **Chapter 2, Lv5 start → Lv9 end**, with encounter-specific internal anchors.


## v78 — Chapter 1 Maevra correction + Chapter 2 validation
- Explicitly corrected Chapter-1 party-state math: Maevra is active at Hollow Watch and remains the fourth battle member after Torren recruitment.
- Watch Captain Frame 500 HP reconfirmed: ~132.9 serious-round damage at Lv2 with Cyanis Crest Strike + Ilyra Attack + Maevra Linebreaker; old 820 HP would be ~6.2 serious rounds before Guard.
- Cistern Devourer rechecked against Cyanis + Ilyra + Torren + Maevra; retained at Lv7 / 2,706 HP.
- Chapter 2 validated on actual Lv5→9 progression with Maevra included throughout.
- Archive Duplicant retained at 1,000 HP; serious Lv6 four-person round ~279.8 damage before Guard.
- Archive Leviathan retained at 1,900 HP / current Powers; Recorded Pattern exact closure authored: one visible action identity, 20% repeated-action final direct-damage reduction, 2 rounds State A / 1 round State B, 45% HP same-bar emergence.
- Commander Rhazek, Hold the Junction, and Transfer Executioner retained.
- Zero direct-damage Power values changed.
- Next mandatory-vs-completionist frontier: Chapter 3.


## v79 — Chapter 3 mandatory-vs-completionist validation
- Validated Chapter 3 on actual route progression: **Lv9 start → Lv13 end** with intermediate S018/S019/S020 level points.
- Recovered exact Maevra guest balance reference from the latest consolidated working tracker and explicitly included her as a legal Chapter 3 combat option.
- Restored accepted Chapter-3 formation compositions/weights into `09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_03_FORMATIONS.md`; old formation raw stats/EXP were not revived.
- Clarified post-Nimera combat state: five available combatants (four permanent + Maevra guest), **four active maximum**.
- Lawful S018 authored encounters validated at Lv9, including Ivory Adjudicator's protected 35% / 333-HP nonlethal threshold.
- Grand Inquisitor Frame corrected **1,450 → 1,200 HP**; all other raw stats and all direct-damage Powers retained.
- First Command Warden retained at Lv14 / 2,850 HP after Lv11 mandatory and Lv12–13 completionist party checks, including Maevra-containing formations.
- Archive Judgment Engine retained at Lv15 / 4,928 HP and fixed Lv15 recommendation; the Lv13 immediate chapter-clear party remains intentionally under-tier.
- False-Warrant Adept remains a placement dependency, not a Power gap.
- Global direct-damage Power audit remains **CLOSED**.
- Next validation frontier: **Chapter 4**.

## v80 — Chapter 4 Mandatory-vs-Completionist Validation
- validated Chapter 4 at **Lv13 opening → ~Lv15 middle → Lv17 late/end** rather than one flat chapter level;
- explicitly removed Maevra from the Chapter-4 default balance baseline;
- explicitly accounted for Vaelira's permanent recruitment after S022 while retaining the four-active-member cap;
- restored approved Reaction Annex opening/middle/late formation compositions and weights to `09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_04_FORMATIONS.md`;
- did not restore superseded historical phase-stat or formation-EXP rows;
- retained all current Chapter-4 ordinary enemy raw stats/Powers;
- retained Annex Duelist, Elder Briarhide, Reaction Conduit, Regulation Crucible → The Seventh Reaction, and Crown Prototype without numerical changes;
- preserved protected Annex staff as placement dependencies rather than inventing combat scenes;
- direct-damage Power audit remains closed;
- next validation frontier = Chapter 5.


## v82 — Chapter 6 mandatory-vs-completionist validation
- Validated Chapter 6 at actual route anchors: **Lv22 start → Lv23 Crownstorm Roc → Lv24 Matron Zevraya → Lv25 Masked Seyrik → Lv27 end**.
- Explicitly locked the Chapter-6 party boundary: five playable permanent characters / four active; Seyrik remains enemy/story identity until after his forced-disengagement encounter and chapter-end recruitment resolution.
- Weather Crown and Crimson Work ordinary enemy bodies retained with no stat/Power changes.
- Weather Crown Shield Guard, Blood Husk, and Perfected Soldier pass on kit but remain exact-placement dependencies.
- Crimson Progenitor retained at Lv28 / 2,700 HP; conservative serious-round throughput remains inside the optional-Elite target.
- Crownstorm Roc, Matron Zevraya → Perfected War Mother, and Masked Seyrik promoted from preliminary boss-route recertification to formal Chapter-6 mandatory/completionist validation.
- Winterglass Titan retained at Lv32 / 10,879 HP; its exact within-Chapter-6 unlock relative to Zevraya remains unresolved and is not used in the fixed pre-boss completionist proof.
- Major Hunt #1 Ashen Whitehorn retained at after-Ch6 unlock / recommended Lv33 / 15,600 HP.
- No numerical balance value or direct-damage Power changed.
- Next validation frontier: **Chapter 7 — Lv27 start → Lv32 end**.


## v83 — Chapter 7 mandatory-vs-completionist validation
- Validated Chapter 7 at actual route anchors: **Lv27 start → Lv30 Revision Arbiter → Lv32 end / Sixfold Volition**.
- All six permanent characters are available; active battle party remains four.
- Seyrik is fully playable throughout Chapter 7.
- Sixfold Volition occurs only after mandatory Chapter-7 combat, so Subclasses were excluded from all Chapter-7 encounter baselines.
- Retained all Chapter-7 ordinary enemy raw stats/Powers.
- Authored/protected Beast Handler + Bound Rift Hound, Resistance Saboteur, Controlled Prisoner, and Command-Seal Warden pass on kit; exact placements remain story dependencies.
- First Registrar's Shade retained at Lv33 / 2,950 HP; representative serious-party duration remains inside the 2–4-round Elite target.
- Chainworks Behemoth and Warden of the Nameless / Revision Arbiter promoted from preliminary boss recertification to formal v83 validation.
- Rift Gate Colossus retained at recommended Lv38 / 13,276 HP.
- Major Hunt #2 after-Ch7 Lv41 recertification carried forward with no contradiction.
- No numerical balance value or direct-damage Power changed.
- Next validation frontier: **Chapter 8 — Lv32 start → Lv37 end**, with Subclass access legal throughout.


## v84 — Chapter 8 mandatory-vs-completionist validation
- Validated Chapter 8 at actual route anchors: **Lv32 start → Lv33 Western Rift Engine → Lv35 Varkesh → Lv37 end**.
- Counted all six permanent characters as available while preserving the four-active-member cap.
- Included legal Subclass access for the entire chapter; mandatory early Subclasses remain developing while completionist optional CEXP/gear/Cards/Primes are allowed to create a large advantage.
- Retained all Chapter-8 ordinary enemy raw stats and direct-damage Powers.
- Conqueror Legate retained at Lv38 / 3,650 HP and formally validated in its 2–4 serious-round Elite role.
- Western Rift Engine retained at Lv36 / 9,775 HP; finite Rift Echo and same-bar 45% Rift Incarnate transition retained; promoted to formal v84 validation.
- Marshal Varkesh Lv38 / 7,326 HP → Rift Conqueror Lv39 / 8,485 fresh HP retained; fresh-body Prime refresh and authored withdrawal outcome retained; promoted to formal v84 validation.
- Regional Hunt #8 Rift Siege Beast retained at recommended Lv44 / 15,875 HP; Chapter-8 story access does not reduce it to route difficulty.
- Major Hunt #2's after-Ch7 Lv41 recertification remains compatible and is a valid completionist progression source during Chapter 8.
- No numerical balance value or direct-damage Power changed.
- Exact Chapter-8 ordinary formations and exact RH8 within-chapter optional-return timing remain explicit data/story dependencies.
- Next validation frontier: **Chapter 9 — Lv37 start → Lv42 end**.


## v85 — Chapter 9 mandatory-vs-completionist validation
- Validated Chapter 9 at actual route anchors: **Lv37 start → Lv37 Equal Mercy → Lv38 post-Last-Sanctuary → Lv40 Rhazek → Lv42 end**.
- Counted all six permanent characters as available while preserving the four-active-member cap and full legal Subclass access.
- Retained all Chapter-9 ordinary enemy raw stats/Powers.
- Mercy Warden and Relay-Fever Patient formally validated as authored nonlethal/stabilization encounters; medical-story firewalls retained.
- Ruin Breach Captain retained at Lv44 / 4,350 HP.
- Equal Mercy Arbiter retained at Lv40 / 10,025 HP with Mercy Protocol and 45% same-bar Open Sanctuary transition; promoted to formal v85 validation.
- Commander Rhazek retained at Lv43 / 8,431 HP → fresh Bastion Devourer Lv44 / 10,462 HP with one fresh-body Prime refresh; promoted to formal v85 validation.
- Corrected the completionist comparison to account for unresolved RH9 timing: **Lv48 without RH9 / Lv49 with RH9**, rather than assuming RH9 is always cleared before Rhazek.
- Regional Hunt #9 Mercyfallen Behemoth retained at recommended Lv50 / 18,882 HP.
- Major Hunt #3 Concordance Guardian's after-Ch9 Lv54 recertification formally carried forward against Lv42 mandatory and ~Lv50 completionist first-access states.
- No numerical balance value or direct-damage Power changed.
- Exact Chapter-9 ordinary formations and RH9 exact S### return trigger remain explicit data/story dependencies.
- Next validation frontier: **Chapter 10 — Lv42 start → Lv47 end**.


## v86 — Chapter 10 mandatory-vs-completionist validation
- Validated Chapter 10 using **Lv42 start → Lv45 Registry Warden → Lv46 post-Warden → Lv47 clear** rather than a flat Lv47 chapter baseline.
- Completionist fixed-content comparison established at approximately **Lv51 start → Lv54 Registry Warden → Lv55 clear**.
- Retained all eight Chapter-10 reused ordinary raw bodies and direct-damage Powers.
- Formally checked recovered Eastern Wayfinder and Buried Registry 5–8-body formation durability; no composition retune required.
- Preserved exact eastern-forest formations and ordinary action-selection weights as data-recovery dependencies rather than inventing them.
- Promoted Registry Warden to **FORMALLY VALIDATED v86** with no raw-stat/Power/threshold change.
- Promoted Major Hunt #4 Worldscar Leviathan to full two-baseline **FORMALLY VALIDATED v86** at recommended Lv60 / 38,800 HP; no numerical change.
- Recorded Torren CQ boss Old Relay Warden as **OPEN — DATA DEPENDENCY** because its exact current raw/action sheet remains deferred/unrecovered.
- Direct-damage Power audit remains **CLOSED**.
- Next frontier: **Chapter 11 — Lv47 start → Lv52 end**.


## v87 — Chapter 11 mandatory-vs-completionist validation
- Validated Chapter 11 at actual route anchors: **Lv47 start → Lv49 Calder → Lv51 Custodian → Lv52 end**.
- Completionist authored-content path tracked at approximately **Lv57 start → Lv59 Calder → Lv60 Custodian → Lv61 clear**.
- Recovered approved Chapter-11 formation compositions/weights into `09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_11_FORMATIONS.md`; obsolete historical phase-stat and formation-EXP rows were not restored.
- Retained all nine current Chapter-11 ordinary enemy raw bodies and Powers.
- Crown Engine Technician kit retained; exact authored scene placement remains open.
- Perfect Administrator promoted to **FORMALLY VALIDATED v87** at Lv55 / 5,800 HP with no numerical change.
- Calder → Crown-Bound Living Anchor and The Custodian promoted from working boss recertification to **FORMALLY VALIDATED v87** with all support architecture/thresholds/Powers retained.
- Regional Hunt #10 Authority Remnant promoted to **FORMALLY VALIDATED v87** at recommended Lv56 / 21,913 HP; exact within-chapter access remains unresolved.
- Major Hunt #5 Final Archive Arbiter formally carried forward at recommended Lv65 / 52,600 HP for after-Ch11 access.
- Exact ordinary action-selection weights remain a data-recovery dependency.
- Direct-damage Power audit remains **CLOSED**.
- Next validation frontier: **Chapter 12 — Lv52 start → Lv57 end**.


## v88 — Chapter 12 mandatory-vs-completionist validation
- Validated Chapter 12 at **Lv52 start → Lv54 Varkesh → Lv56 Vaelkor → Lv57 end**.
- Completionist fixed-content route tracked at **Lv63 start → Lv64 Varkesh → Lv66 Vaelkor → Lv66 clear**, with RH11 capable of moving the high side to ~Lv67 depending exact timing.
- Retained all eleven Chapter-12 ordinary raw bodies and the recovered nine-formation composition set.
- Retained Compelled Relay Bearer and formally validated Lord-Marshal Kharvek; exact Kharvek placement remains story-owned.
- Promoted Marshal Varkesh — Final Capture and Emperor Vaelkor → Sovereign Panoply Unbound to **FORMALLY VALIDATED v88** with no numerical changes.
- Promoted Regional Hunt #11 to **FORMALLY VALIDATED v88** at retained Lv61–62; exact within-chapter timing remains unresolved.
- Paper-recertified Major Hunt #6 The Unfinished World at retained Lv70 / 78,000 HP against the actual post-Vaelkor route/completionist level relationship; runtime duration/attrition remains a final QA gate.
- No raw stat or direct-damage Power changed.
- Next validation frontier: **Chapter 13 — Lv57 start → Lv60 Last Shelter → Lv62 ending**.


## v89 — Chapter 13 mandatory-vs-completionist validation / campaign paper pass closure
- Validated Chapter 13 at **Lv57 start → Lv58 Last Weapon Archon → Lv60 Last Shelter/PONR → Lv61 final boss → Lv62 ending**.
- Completionist route tracked at **Lv68 chapter start → Lv69 pre-Archon without MH6 → Lv70 by Last Shelter**, with full all-content routes able to cap earlier.
- Retained all nine Chapter-13 ordinary bodies and all nine recovered 3–4-body formation compositions.
- Retained Devouring Echo / Calamity Memory replay clamps and permanent-state firewalls.
- Promoted Devourer of Names, Last Weapon Archon, and Reconstituted Entity → The Last Command to **FORMALLY VALIDATED v89**.
- Retained Heart Manifestation and Unbound Shards as finite no-turn / no-direct-damage support objects.
- Made the Last Shelter recovery/loadout point explicit as the true Lv60 balance boundary before the irreversible Reactor Galleries sequence.
- No enemy raw stat or direct-damage Power changed.
- Planned paper Enemy & Boss Mandatory-vs-Completionist Validation is now **complete through Chapters 0–13**.
- Remaining action-weight/placement/runtime dependencies remain tracked but do not block progression work.
- **CEXP recalibration to Player Lv55–60 full Base + Subclass completion is now the active next balance priority.**


## v90 — Enemy static completion
- Authored exact Character Quest boss sheets for Elemental Forecast Construct, Crest-Exhausted Warden, Black Host Remnant Captain raw body, and Old Relay Warden.
- Restored accepted Chapter 1, 2, 5, 6, 7, 8, 9, and Chapter-10 Eastern Forest formation authority into `09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/`.
- Restored Chapter 12 and Chapter 13 30/45/25 formation weights; retained Chapter 10's 20/55/25 area-tier model.
- Added `ACTION_SELECTION_DEFAULT.md`: explicit weights remain authoritative; otherwise choose uniformly among currently eligible selected actions after forced/phase/preparation/lock logic.
- Confirmed targetable support objects/components are numerically complete.
- Added `STORY_INTEGRATION_BOUNDARIES.md` so unfinished scene placement no longer reads as unfinished enemy design.
- Enemy static design is **CLOSED**; runtime QA remains separate.
- Next systemic balance task: **CEXP recalibration to Player Lv55–60 full Base + Subclass completion**.


## v91 — Prime-slot restoration + CEXP Lv55–60 recalibration
- Restored omitted Prime loadout rule: **1 Prime slot per permanent character from Chapter-4 Prime battle-loadout access until Sixfold Volition; 2 slots after Volition**.
- Preserved CL1–CL13 curve at **0→6,000 CEXP**.
- Recalibrated mandatory Ch12 CEXP **2,750 → 1,250**.
- Recalibrated mandatory Ch13 CEXP **1,500 → 1,750**, split **1,500 pre–Last Shelter / 250 post**.
- Mandatory post-Volition cumulative now reaches **7,000 end Ch12 / 8,500 Last Shelter**, producing normal-route full Base + Subclass completion across **~Lv55–60**.
- Authored exact optional CEXP ledger: **300 Regional Hunts + 250 Major Hunts #1–5 + 300 Character Quests + 150 Side Quests = 1,000 before MH6**; MH6 adds **75**, exhaustive total **1,075**.
- Retired old approximate ~1,800 optional CEXP envelope.
- Next balance step: canonical mandatory/completionist party snapshots and representative true-battle simulations.


## v92 — Recruitment-aware CEXP proof correction
- Corrected v91's inherited approximate Volition planning centers using each permanent character's actual recruitment handoff.
- Locked no-retroactive-CEXP rule for pre-recruitment mandatory awards.
- Canonical expected-route recruitment-chapter pickup: Torren 150 Ch1; Nimera 300 Ch3; Vaelira 500 Ch4; Seyrik 0 Ch6.
- Corrected mandatory Volition Base CEXP: Torren 5,350; Vaelira 5,250; Cyanis/Ilyra 4,950; Nimera 4,500; Seyrik 3,500.
- v91 Ch12/Ch13 budgets and 6,000-CEXP CL13 curve retained.
- Mandatory full Base + Subclass completion now centers ~Lv56–60, still inside the accepted Lv55–60 target.
- True-battle snapshots must use recruitment-aware CEXP and only optional CEXP earned while the character was already recruited.


## v94 — Closure-status synchronization
- synchronized chapter-validation labels in current canon status;
- campaign paper-validation file now explicitly distinguishes COMPLETE paper validation from ACTIVE true-battle follow-up;
- Hollow Watch Castellan owning file header promoted to v93 TRUE-BATTLE CERTIFIED.
- no combat numbers, Powers, CEXP, traits, cards, or Prime mechanics changed.
