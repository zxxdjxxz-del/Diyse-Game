# Diyse — Mandatory Boss Route Recertification

## Purpose
Systematically check mandatory story bosses against both:
1. the **campaign-only / mandatory-route** player level at that encounter; and
2. the **completionist / all-currently-available-content** player level at that same encounter.

The boss keeps one fixed authored stat line.
There is **no dynamic player-level scaling**.

## Acceptance rule
Tune the boss primarily to the mandatory-route party so the main story remains fair without optional grinding.

Then certify the exact same boss against the completionist route:
- completionists may be safer;
- completionists may win roughly **2–3 rounds faster**;
- optional progression should feel rewarding;
- do not raise the boss simply to erase the completionist advantage.

Only change raw stats when the existing boss materially misses its intended story-boss tier.

## Current sequence
The systematic ledger begins at Chapter 1 and proceeds through Chapters 1–13.

### Chapter 1 — Hollow Watch Castellan
**Status:** **WORKING PASS / RECERTIFIED**

The earlier v27 check was invalid because it used the end-Chapter-1 ~Lv5 level instead of the actual S008 party state.

Actual encounter profile:
- central mandatory reference: **~Lv2**
- high-side / extra-EXP reference: **~Lv3**
- three-character party: Cyanis / Ilyra / Maevra

Current working boss:
- Lv **6**
- HP **450**
- ATK **42**
- MAG **27**
- DEF **27**
- Spirit **24**
- SPD **25**
- EVA **0**
- Status Resistance **5**

Support:
- Ballista — 120 HP / 55 ATK / 20 DEF / 18 Spirit / 24 SPD
- Watch Seal — 100 HP / 22 DEF / 28 Spirit / 10% Fortress direct-damage reduction

Round result:
- aggressive: **~4–5**
- normal: **~6**
- safety: **~7–8**

Decision:
> **RETAIN THIS WORKING PACKAGE AS THE CHAPTER-1 CALIBRATION ANCHOR**

The former 1,758-HP / ATK36 line is not the current working balance target.

### Chapter 2 — Archive Leviathan
**Status:** **v78 VALIDATED / POWER COMPLETE / RECORDED PATTERN CLOSED**

Actual route references:
- mandatory central: **~Lv6**
- completionist/high-side: **~Lv7**

Inherited:
- Lv9
- HP 2,592
- ATK50 / MAG52
- DEF31 / Spirit33
- SPD25 / EVA0 / SR5

Recovered player throughput:
- all-basic Lv6 party: **178.48 damage/round**
- inherited 2,592 HP: **14.52 all-basic rounds**
- recovered premium delta across legal MP: approximately **+262.48**
- ten-round no-heal envelope: approximately **2,047 damage**

Working change:
> **HP 2,592 → 1,900**

Expected:
- mandatory aggressive ~8–9
- mandatory normal **~9–10**
- completionist/high-side **~8–9**
- safety ~10–11

Architecture remains one bar / Recorded Pattern → Emergent same-bar.

Raw offense:
> **ATK50 / MAG52 RECERTIFIED**

Direct-damage actions:
- Leviathan Rend — **220 Power**
- Vault Crash — **140 Power per target**
- Archive Undertow — **150 Power per target**
- Recorded Pattern — **Power N/A; no direct damage**

The boss now passes the explicit Power-completeness gate.

### Chapter 2 — Commander Rhazek — Bastion Master
**Status:** **v78 VALIDATED / POWER COMPLETE**

Actual route:
- mandatory central: **~Lv7**
- completionist: **~Lv8**
- high-side optional route can approach **~Lv9**

Working raw line:
- Lv10
- HP **2,050**
- ATK **58**
- MAG **44**
- DEF **36**
- Spirit **32**
- SPD **27**
- EVA **5**
- SR **5**

Direct-damage Power block:
- Commander's Cut — **180**
- Shieldline Break — **220**
- Command-Link Pulse — **135 per target**
- Bastion Ranged Position / Crossfire Bolt — **165**
- Ruin-Driven Cut — **210**
- Bastion Breaker — **250**
- Ruin Sweep — **145 per target**

Finite support:
- Bastion Shield Detachment — **180 HP**
- Bastion Ranged Position — **150 HP**

State shift:
- **45% HP**
- same bar
- +6 DEF / +6 Spirit for remainder
- no refill / no free attack / no Prime refresh

Expected pacing:
- mandatory aggressive ~9–10
- mandatory normal **~10–11**
- completionist **~8–9**
- high-side ~7–8
- safety ~11–12

### Chapter 3 — First Command Warden
**Status:** **WORKING PASS / POWER COMPLETE**

Pre-battle mandatory:
> **11,280 EXP = Lv11**, 820 short of Lv12.

Pre-battle completionist fixed-content:
> **14,280 EXP = Lv12**, only 120 short of Lv13.

High-side:
> **~Lv13** with incidental optional combat.

Working raw line:
- Lv14
- HP **2,850**
- ATK **72**
- MAG **72**
- DEF **43**
- Spirit **43**
- SPD **30**
- EVA 0
- SR 10

Direct-damage Powers:
- Authority Lance — **190**
- Judgment Pulse — **140 per target**
- Seal Reprisal — **100**
- Major Ruling — **210 per target**
- Recorded Analogue — **150 single / 105 AoE**
- Warden Crush — **245**
- Challenged Verdict — **230**
- Command Collapse — **165 per target**

Command Seal:
- Power N/A
- records completed command category
- never removes Attack / Ability / Card / Item / Defend
- repeating the marked category triggers Seal Reprisal after the action resolves

Command Ring:
- 260 HP
- targetable during 1-round Major Ruling Preparation
- disruption cancels the ruling
- may align again after 3 full rounds

State B:
- begins at 45% HP
- same bar
- no refill
- no transition damage
- no Prime refresh

Expected:
- mandatory normal **~10–11**
- completionist **~8–9**
- high-side ~7–8

### Chapter 4 — Elder Briarhide
**Status:** **WORKING PASS / POWER COMPLETE**

Actual route:
- mandatory: **Lv13**
- completionist fixed-content: **Lv15 exactly**
- high-side: **~Lv16**

Current raw line:
- Lv14
- HP **2,100**
- ATK **72**
- MAG 28
- DEF **60**
- Spirit **55**
- SPD36
- EVA10
- SR5

Direct Powers:
- Territorial Rush — **190**
- Scarred Maul — **225**
- Briar Sweep — **125 per target**
- Recovered Last Sentinel / Sentinel Impact — **340**

Non-damaging:
- Guard the Den — Power N/A
- Warning Display — Power N/A

Duration:
> **exactly 4 rounds**

Rounds 1–3 are ordinary combat.
Round 4 forces Last Sentinel.
Elder Briarhide retreats alive after the Prime action resolves.

This is a fixed-duration protected encounter, so completionist advantage is safety/resource efficiency rather than a faster clear.

### Chapter 4 — Reaction Conduit
**Status:** **WORKING PASS / POWER COMPLETE**

Actual route:
- mandatory **15,350 EXP = Lv13**
- completionist fixed-content **20,550 EXP = Lv15**
- high-side **~Lv16**

Working raw line:
- Lv17
- HP **2,400**
- ATK **58**
- MAG **80**
- DEF **50**
- Spirit **55**
- SPD **33**
- EVA5
- SR5

Expression cycle:
> Fire → Ice → Lightning → Earth

Direct Powers:
- Reaction Pressure — **180**
- Spillway Burst — **120 per target**
- Exposure Thrash — **160**

Non-damaging:
- Instinctive Guard — Power N/A

Expression-linked Pressure riders:
- Fire 20% Burn
- Ice 20% Freeze
- Lightning 15% Stun
- Earth 20% Staggered

At 0 HP:
> researcher stabilized alive.

Expected:
- mandatory normal **~8–9**
- completionist **~6–7**
- high-side ~5–6
- safety ~9–10

### Chapter 4 — Regulation Crucible → The Seventh Reaction
**Status:** **WORKING PASS / POWER COMPLETE**

Actual route:
- mandatory **21,462 EXP = Lv15**
- completionist fixed-content **26,662 EXP = Lv17**
- high-side **~Lv18**

Form I:
- Lv18
- HP 2,400
- ATK 64
- MAG 90
- DEF54 / Spirit57 / SPD30
- Regulation Slash 185
- Pairwise Return 100 × up to 2
- Compensating Drive 220
- Core Discharge 135 AoE
- Regulator Guard N/A

Four chambers:
- 300 HP each
- 48 DEF / 50 Spirit
- exactly two scheduled active at once
- Power N/A
- destroyed stay destroyed

Form II:
- Lv19
- HP 2,900 fresh
- ATK72
- MAG98
- DEF58 / Spirit62 / SPD32
- Unified Impact 205
- Compression Lance 245
- Seventh Confluence 160 AoE
- Overflow Equation 2 × 115
- Central Rebalance N/A

Fresh-body rules:
- no damage spillover
- no chamber respawn
- no intermediate payout
- Prime availability refreshes
- no third form

Expected complete encounter:
- mandatory **~13–15**
- completionist **~10–12**
- high-side **~9–11**

### Chapter 5 — Furnace Tyrant
**Status:** **WORKING PASS / POWER COMPLETE**

Route:
- Chapter-5 start: 25,600 EXP / Lv17
- expected occupied-forge entry segment: ~3,300 ordinary EXP
- mandatory pre-boss: **~28,900 EXP = Lv18**
- fixed completionist pre-boss: **~37,100 EXP = Lv20**
- high-side: **~Lv21**

Raw:
- Lv23
- HP3,400
- ATK100 / MAG72
- DEF66 / Spirit56
- SPD32 / EVA0 / SR5

Heat:
- Controlled: -10% outgoing final direct damage / +10 Total Defense
- Heated: baseline
- Overheated: +15% outgoing final direct damage / -15 Total Defense

Powers:
- Furnace Lash 195
- Furnace Ram 235
- Scouring Jet 185
- Heat Wash 135 AoE
- Foundry Breaker 285 AoE
- Stabilize Armor N/A

Finite support:
- two Furnace Servitors at 60% HP
- Servitor HP280
- Scalding Vent150
- Feed Furnace N/A
- Overheat Vent80 AoE

Foundry Breaker:
- one-round Interruptible Preparation
- eligible <=50% HP
- legal cooling to Controlled during Preparation interrupts it

Siege Without Return:
- 30% HP
- same bar
- Heat floor Heated
- no cooling action
- no extra action
- no Prime refresh

Expected:
- mandatory normal **~9–10**
- completionist **~7–8**
- high-side ~6–7

### Chapter 5 — Deepforge Colossus — Assembly Frame → Worldsmith Body
**Status:** **WORKING PASS / POWER COMPLETE**

Route:
- mandatory **37,678 EXP = Lv20**
- completionist fixed-content **45,878 EXP = Lv22**
- high-side **~Lv23**

Form I:
- Lv24 / HP3,400
- ATK102 / MAG78
- DEF70 / Spirit55 / SPD28
- Hammer205
- Sweep140 AoE
- Forge Discharge195
- Clamp and Draw170
- Reinforce Chassis N/A
- Field Repair N/A

Assemblies:
- Guard Press HP320
- Repair Arm HP300
- Command Loom HP280
- no independent turns
- all Power N/A
- destroyed remain destroyed

Form II:
- Lv25 / HP4,000 fresh
- ATK112 / MAG90
- DEF73 / Spirit60 / SPD31
- Clamp225
- Foundry Arc215
- Construction Sweep155 AoE
- Worldline Crush260
- Forge Collapse300 AoE
- Reinforced Load N/A
- Self-Stabilize N/A

Forge Collapse:
> **Protected Preparation**

Fresh-body correction:
> **Prime availability refreshes at Worldsmith Body.**

Expected:
- mandatory complete **~14–16**
- completionist **~11–13**
- high-side **~10–12**

### Chapter 6 — Crownstorm Roc
**Status:** **WORKING PASS / POWER COMPLETE**

Route:
- Chapter-5 end 44,400 EXP = Lv22
- working Weather-Crown approach slice ~5,000 ordinary EXP
- mandatory pre-boss **~49,400 EXP = Lv23**
- fixed completionist **~61,600 EXP = Lv25**
- high-side **~Lv26**

Raw:
- Lv26
- HP4,800
- ATK100 / MAG112
- DEF60 / Spirit66
- SPD43 / EVA10 / SR10

Perched Sovereign:
- Talon200
- Crownbolt215
- Hail Scatter135 AoE
- Gale Sweep145 AoE
- Crown Perch N/A

Stormbound:
- begins at 50% HP
- same bar
- +10 Speed
- Dive245
- Crownstorm Bolt255
- Stormglass Burst165 AoE
- Gale Pressure170 AoE
- Eye of the Crown N/A

Transition:
- no refill
- no free attack
- no extra action
- no Prime refresh

`Gale` is Physical / Neutral presentation, not Wind.

Expected:
- mandatory normal **~9–10**
- completionist **~7–8**
- high-side ~6–7

### Chapter 6 — Matron Zevraya → Perfected War Mother
**Status:** **WORKING PASS / POWER COMPLETE**

Route:
- mandatory pre-boss **~57,500 EXP = Lv24**
- completionist fixed-content **~69,700 EXP = Lv27**
- high-side **~Lv28**
- RH#6 excluded from fixed proof until exact relative unlock is recovered

Blood Matron:
- Lv28 / HP4,400
- ATK90 / MAG122
- DEF68 / Spirit76 / SPD40
- Ritual Incision205 / 25% Bleed
- Alteration Lance225
- Surgical Sweep145 AoE
- Ruin Infusion220

Reservoirs:
- Sustenance HP320
- Armor HP340
- Brood HP300
- Conduction HP320
- no independent turns
- all bodies Power N/A
- destroyed functions remain gone

Reservoir-enabled Powers:
- Sustenance Draw190
- Weather Conduction200
- Brood Rend155

Crimson Brood:
- begins at 45% HP
- same bar
- Crimson Arc165 AoE
- no refill / free attack / Prime refresh

Perfected War Mother:
- Lv29 / HP5,200 fresh
- ATK112 / MAG132
- DEF72 / Spirit80 / SPD42
- Tearing Blade245 / 25% Bleed
- Ruin Scythe270
- Warbody Crush285
- Ruin Wave175 AoE
- Siphon230 if Sustenance survived
- Conduction230 if Conduction survived
- Brood Rend175 if Brood survived

Fresh-body rule:
> **Prime availability refreshes.**

Expected complete:
- mandatory **~15–17**
- completionist **~12–14**
- high-side ~11–13

### Chapter 6 — Masked Ruin Vanguard — Seyrik
**Status:** **WORKING PASS / POWER COMPLETE**

Route:
- immediate post-Zevraya mandatory **~62,000 EXP = Lv25**
- fixed completionist **~74,200 EXP = Lv27 approaching Lv28**
- RH#6, if legally pre-fight and cleared, moves route to ~Lv28
- high-side **~Lv28–29**

Raw:
- Lv27
- HP **4,000**
- ATK104
- MAG79
- DEF63
- Spirit59
- SPD38
- EVA5
- SR10

Raw stats except HP are retained from inherited certification.

Direct Powers:
- Ruin Cleave **165**
- Rift Lance **175**
- Ember Brand **150**
- Fracturing Brand **145 per target**
- Unmaking Blow **245**

Unmaking Blow:
- eligible <=60% HP
- 25% applicable-axis penetration
- +15% final damage if target already Bleeding

Protected floor:
- 20% Max HP = **800**
- damage clamps at floor
- pending Seyrik action canceled
- immediate authored disengagement

Expected:
- mandatory normal **~7–8**
- completionist **~5–6**
- high-side ~4–5

### Chapter 7 — Chainworks Behemoth
**Status:** **WORKING PASS / RAW LINE RETAINED / POWER COMPLETE**

Route:
- Chapter-6 end: 69,300 EXP / Lv27
- Ashford approach planning slice: ~4,000 ordinary EXP
- mandatory pre-boss: **~73,300 EXP = Lv27**
- fixed optional advantage available: **21,900 EXP**
- completionist pre-boss: **~95,200 EXP = Lv31**
- high-side: **~Lv32**

Raw:
> **RETAIN — Lv29 / HP5,135 / ATK109 / MAG57 / DEF77 / Spirit59 / SPD32 / EVA0 / SR5**

Anchors:
- exactly 3
- HP240 each
- DEF72 / Spirit62 / SR10
- Power N/A
- +5 Total Defense per intact Anchor while Bound

Transition:
- normal at 55% HP
- early if 2+ Anchors destroyed
- no refill / free attack / Prime refresh
- intact Anchors at transition give +5% Attack each for first 2 Freed rounds

Bound:
- Chain Rend205 / 25% Bleed
- Gate Crush225 / 20% Staggered
- Tether Drag180 / Speed Down15%
- Restrained Sweep140 AoE

Freed:
- Chain Rend225 / 25% Bleed
- Gate Crush165 AoE / 15% Staggered
- Behemoth Rush265
- Freed Sweep175 AoE

Expected:
- mandatory center **~9 rounds**
- completionist **~6–7**
- high-side ~5–6

### Chapter 7 — Warden of the Nameless / Revision Arbiter
**Status:** **WORKING PASS / POWER COMPLETE**

Route:
- mandatory pre-boss **92,020 EXP = Lv30**
- completionist fixed-content **120,720 EXP = Lv34**
- high-side **~Lv35**

Raw:
- Lv34
- HP **7,600**
- ATK **124**
- MAG **138**
- DEF **86**
- Spirit **92**
- SPD **42**
- EVA5
- SR10

Closed Record:
- 3 Assertion Layers
- 80% direct-damage reduction while any layer remains
- one layer removed after first completed ordinary action from each distinct active character
- no new command
- Power N/A

Adjudication:
- Name Redaction220
- Registry Pulse145 AoE
- Severing Writ205 / 20% Staggered
- Revision Lance245 / 20% Stun
- Reconciliation Order N/A

Revision Claim:
- 25% damage-output tax on one character
- clears when that character completes a different command category
- max 2 rounds
- never disables commands
- Power N/A

Open Revision:
- 40% HP
- same bar
- 2 short 40%-reduction assertion layers
- Lance280
- Identity Severance270 / 20% Staggered
- Rewrite Wave180 AoE
- Recursive Judgment2×140
- Final Reconciliation N/A

No state refreshes Prime availability.

Expected:
- mandatory normal **~12–13**
- completionist **~9–10**
- high-side ~8–9

### Chapter 8 — Western Rift Engine
**Status:** **WORKING PASS / RAW LINE RETAINED / POWER COMPLETE**

Route:
- Chapter-7 end: 100,600 EXP / Lv32
- Horizon Vault breakthrough: +1,500
- working ordinary approach slice: ~6,000
- mandatory pre-boss: **~108,100 EXP = Lv33**
- fixed optional advantage: **48,700 EXP**
- completionist pre-boss: **~156,800 EXP = Lv39**
- RH#8, if legally pre-Engine, pushes route to **~Lv40**

Raw:
> **RETAIN — Lv36 / HP9,775 / ATK86 / MAG133 / DEF97 / Spirit89 / SPD33 / EVA0 / SR10**

Engine Core:
- Rift Lance235
- Engine Shock210 / 20% Stun
- Core Pressure150 AoE
- Anchor Crush195 / 20% Staggered
- Core Recalibration N/A

Rift Echo:
- exactly one at 70% HP
- HP420 / MAG128
- Echo Bolt165
- Echo Static145 / 15% Stun
- finite / no respawn

Rift Incarnate:
- 45% HP
- same bar
- +10 Speed / -10 Total Defense
- Incarnate Lance275
- Rift Flash255 / 25% Stun
- Fracture Wave180 AoE / 15% Staggered
- Unbound Surge2×140
- Incarnate Sweep165 AoE

No state refreshes Prime availability.
No Spatial element.

Expected:
- mandatory normal **~10–11**
- completionist **~7–8**
- high-side ~6–7

### Chapter 8 — Marshal Varkesh → Rift Conqueror
**Status:** **WORKING PASS / RAW LINES RETAINED / POWER COMPLETE**

Route:
- Chapter-7 end 100,600 EXP
- Ch8 ordinary before final combat 18,962
- prior Ch8 named rewards 1,500 + 5,000 + 2,200
- mandatory pre-boss **128,262 EXP = Lv35**
- fixed optional advantage **57,200 EXP**
- completionist pre-boss **185,462 EXP = Lv42**
- high-side **~Lv43**

Marshal Varkesh:
> **RETAIN — Lv38 / HP7,326 / ATK140 / MAG93 / DEF93 / Spirit85 / SPD44 / EVA5 / SR10**

Form-I Powers:
- Marshal's Cut230 / 20% Bleed
- Tempo Break255 / 20% Staggered
- Command Sweep160 AoE
- Rift Volley210
- Seize Initiative N/A

Rift Conqueror:
> **RETAIN — Lv39 / HP8,485 / ATK151 / MAG107 / DEF97 / Spirit91 / SPD45 / EVA5 / SR10**

Fresh body:
- no spillover
- no free attack
- Prime availability refreshes

Form-II Powers:
- Conqueror Cleave270 / 25% Bleed
- Rift Drive295 / 20% Staggered
- Rift Barrage2×150
- Conqueror Sweep185 AoE
- Riftstorm Burst195 AoE / 15% Stun
- Tempo Dominance N/A

Outcome:
- 0 HP defeats Rift Conqueror
- Varkesh survives and withdraws
- no Chapter-8 capture floor

Expected:
- mandatory **~13–15**
- completionist **~10–12**
- high-side ~9–11

### Chapter 9 — Equal Mercy Arbiter
**Status:** **PASS / FORMALLY VALIDATED v85 / RAW LINE RETAINED / POWER COMPLETE**

Route:
- Chapter-8 end: 138,800 EXP / Lv37
- sanctuary progression: +1,500
- working Larkspire ordinary slice: ~6,500
- mandatory pre-boss: **~146,800 EXP = Lv37**
- fixed optional advantage: **78,200 EXP**
- completionist pre-boss: **~225,000 EXP = Lv45**
- high-side: **~Lv46**

Raw:
> **RETAIN — Lv40 / HP10,025 / ATK105 / MAG140 / DEF89 / Spirit107 / SPD43 / EVA0 / SR10**

Mercy Protocol:
- each normal party round starts with Sanctuary Restraint
- 50% direct-damage reduction
- support-only Ability/Card/Item or Defend removes it for rest of round
- no new command / no Barrier

State A:
- Arbiter's Measure235
- Containment Writ215 / 20% Staggered
- Sanctuary Pulse155 AoE
- Equal Judgment260 / 20% Stun
- Temper Harm N/A

Open Sanctuary:
- begins at 45% HP
- same bar
- restraint tax ends
- +10 Speed / -10 Total Defense
- no refill / free attack / Prime refresh

State B:
- Open Sanctuary Lance285
- Mercy Is Not Surrender190 AoE
- Containment Verdict275 / 20% Staggered
- Sanctuary Reversal2×145
- Final Admonition250 / 20% Stun
- Open Hand N/A

Expected:
- mandatory normal **~12–13**
- completionist **~9–10**
- high-side ~8–9

### Chapter 9 — Commander Rhazek — Reforged Commander → Bastion Devourer
**Status:** **PASS / FORMALLY VALIDATED v85 / RAW LINES RETAINED / POWER COMPLETE**

Exact route:
- Chapter-8 end 138,800
- Ch9 ordinary EXP 25,000
- named rewards before boss 10,000
- mandatory pre-boss **173,800 EXP = Lv40**
- after boss 181,300 = Lv41
- after chapter clear **184,300 = Lv42 exactly**

Completionist:
- fixed optional advantage excluding RH9 **78,200 EXP**
- pre-boss without RH9 **252,000 EXP = Lv48**
- if RH9 is legally cleared before the climax: **263,000 EXP = Lv49**
- high-side **~Lv50**

Reforged Commander:
> **RETAIN — Lv43 / HP8,431 / ATK163 / MAG100 / DEF111 / Spirit96 / SPD44 / EVA5 / SR10**

Form-I:
- Reforged Cut250 / 25% Bleed
- Shieldline Break285 / 25% Staggered
- Command Rupture175 AoE
- Ruin-Driven Advance265
- Hold the Line N/A

Bastion Devourer:
> **RETAIN — Lv44 / HP10,462 / ATK175 / MAG131 / DEF107 / Spirit104 / SPD46 / EVA0 / SR10**

Fresh-body:
- no spillover
- no free attack
- Prime availability refreshes

Form-II:
- Devouring Cleave295 / 25% Bleed
- Bastion Breaker325 / 25% Staggered
- Ruin Sweep205 AoE
- Siege Pulse190 AoE
- Demolition Breaker335 AoE / 25% Staggered
- Reinforced Advance N/A

Demolition Breaker:
- below 55% Form-II HP
- 1-round Protected Preparation
- 3-round repetition lock

Exposed Rhazek:
- begins at 18% Form-II HP
- same bar
- -20 Total Defense / +10 Speed
- Last Line340 / 25% Bleed
- Ruin-Driven Cut310
- Command Collapse220 AoE / 15% Staggered
- no Prime refresh

Expected:
- mandatory **~16–18**
- completionist **~12–14**
- high-side ~11–13

### Chapter 10 — Registry Warden
**Status:** **WORKING PASS / RAW LINE RETAINED / POWER COMPLETE**

Exact mandatory route:
- Chapter-9 end **184,300 EXP**
- all Ch10 ordinary before boss **31,800**
- named pre-boss **8,500**
- pre-boss **224,600 EXP = Lv45**
- Warden clear → **232,600 = Lv46**
- Last Blank + chapter-clear → **237,600 = Lv47 exactly**

Completionist:
- fixed optional advantage **107,200 EXP**
- pre-boss **331,800 EXP = Lv54**
- high-side **~Lv55**

Raw:
> **RETAIN — Lv49 / HP13,514 / ATK157 / MAG172 / DEF124 / Spirit126 / SPD46 / EVA0 / SR10**

Closed Registry:
- Registry Lance250
- Threshold Hammer235
- Catalog Sweep165 AoE
- Cross-Reference270
- Closed Record N/A / +15 Total Defense

Open Registry:
- begins at 40% HP
- same bar
- +10 Speed / -15 Total Defense
- Lance300
- Unsealed Verdict300
- Full Disclosure205 AoE
- Paired Citation2×160
- Final Index225 AoE

No harmful status riders.
No state refreshes Prime availability.

Expected:
- mandatory normal **~10–11**
- completionist **~7–8**
- high-side ~6–7

### Chapter 11 — Chancellor Othmar Calder — Protector of Continuity → Crown-Bound Living Anchor
**Status:** **WORKING PASS / RAW LINES RETAINED / POWER COMPLETE**

Route:
- Chapter-10 end **237,600 EXP = Lv47**
- working pre-Calder ordinary slice **27,000**
- mandatory pre-boss **264,600 EXP = Lv49**
- remaining Ch11 ordinary after Calder **18,300**
- fixed optional advantage **135,200 EXP**
- completionist pre-boss **399,800 EXP = Lv59**
- RH#10 excluded pending exact relative access
- high-side **~Lv60**

Protector of Continuity:
> **RETAIN — Lv54 / HP10,133 / ATK137 / MAG193 / DEF118 / Spirit134 / SPD50 / EVA5 / SR10**

Authentication Lenses:
- 2 × HP600
- Power N/A
- each +5 Total Defense / +5 Base Hit

Form-I Powers:
- Continuity Writ270
- Emergency Injunction185 AoE
- Administrative Rebuff245
- Provenance Seal240
- Authenticated Judgment300
- Protector's Order N/A

Crown-Bound Living Anchor:
> **RETAIN — Lv55 / HP13,662 / ATK181 / MAG204 / DEF139 / Spirit139 / SPD47 / EVA0 / SR10**

Fresh-body:
- no spillover
- no free attack
- **Prime availability refreshes**

Living Anchor Clamps:
- 2 × HP720
- Power N/A
- each +5 Total Defense
- finite Continuity Collapse load points

Form-II Powers:
- Anchor Crush305 / 20% Staggered
- Crownline Surge295
- Living Continuity210 AoE
- Bound Verdict290
- Continuity Collapse345 AoE
- Institutional Continuance N/A

Continuity Collapse:
- below 60% Form-II HP
- Interruptible Preparation
- destroying loaded Clamp cancels
- successful resolution consumes loaded Clamp
- max 2 successful resolutions

Expected:
- mandatory **~15–17**
- completionist **~12–14**
- high-side ~11–13

### Chapter 11 — The Custodian
**Status:** **WORKING PASS / RAW LINE RETAINED / POWER COMPLETE**

Exact working route:
- Ch10 end **237,600 EXP = Lv47**
- pre-Calder ordinary +27,000
- Calder clear +4,000
- deeper administrative ordinary +18,300
- pre-Custodian **286,900 EXP = Lv51**
- Custodian/direct contact +2,500 → 289,400
- remaining story rewards → **299,100 EXP = Lv52 exactly**

Completionist:
- fixed optional advantage **135,200 EXP**
- pre-Custodian **422,100 EXP = Lv60**
- RH#10 excluded pending exact S063 timing
- RH#10 pre-clear would produce **435,100 = Lv61**
- high-side **~Lv61**

Raw:
> **RETAIN — Lv55 / HP16,017 / ATK177 / MAG190 / DEF144 / Spirit146 / SPD48 / EVA0 / SR10**

Supports:
- Acuity Node — HP700 / Power N/A / +10 Base Hit +10 Speed
- Ruin Containment Seal — HP760 / Power N/A / +10 Total Defense / −15% final Ruin damage taken

Administrative Closure:
- Convergence Lance290
- Compression Strike275 / 20% Staggered
- Discharge Pulse195 AoE
- Administrative Verdict315
- Custodial Hold N/A

Open Reconciliation:
- 45% HP same-bar
- surviving supports disengage
- +10 Speed / -15 Total Defense
- Open Convergence335
- Compression Verdict345
- Discharge Field230 AoE
- Threefold Sequence3×120
- Reconciliation Pulse215 AoE
- Open Record N/A

No state refreshes Prime availability.

0 HP:
- enforcement defeated;
- Custodian remains as direct-contact historical interface.

Expected:
- mandatory normal **~11–12**
- completionist **~8–9**
- high-side ~7–8

### Chapter 12 — Marshal Varkesh — Final Capture
**Status:** **WORKING PASS / RAW LINE RETAINED / POWER COMPLETE**

Exact working route:
- Chapter-11 end **299,100 EXP = Lv52**
- pre-Varkesh ordinary **24,000**
- Blackspine / Draevensreach breakthrough **3,000**
- mandatory pre-boss **326,100 EXP = Lv54**
- remaining post-Varkesh ordinary **23,100**
- Chapter-12 end remains **369,100 EXP = Lv57**

Completionist:
- fixed optional advantage **166,700 EXP**
- pre-Varkesh **492,800 EXP = Lv64**
- RH#11 excluded pending exact relative access
- high-side **~Lv65**

Raw:
> **RETAIN — Lv58 / HP17,106 / ATK226 / MAG148 / DEF144 / Spirit131 / SPD55 / EVA5 / SR10**

Supports:
- Command Standard HP900 / Power N/A
- one Black Guard HP1,400
- East Beacon HP1,100 / Power N/A
- West Beacon HP1,100 / Power N/A

Capture:
- while either Beacon survives: HP floor **3,421 / 20%**
- both Beacons destroyed removes floor
- 0 HP afterward = **captured alive**

Varkesh:
- Final Marshal Cut315 / 25% Bleed
- Tempo Break340 / 25% Staggered
- Command Sweep220 AoE
- Pursuit Lance300
- Seize Initiative N/A

50% late pressure:
- same bar
- +10 Speed / -10 Total Defense
- Breakthrough Drive365
- Encirclement Sweep245 AoE
- Last Withdrawal2×180
- no Prime refresh

Black Guard:
- Guardline Cut235 / 15% Bleed
- Covering Rush205 / 15% Staggered
- Interpose N/A

Expected:
- mandatory **~11–13**
- completionist **~8–10**
- high-side ~7–9

### Chapter 12 — Emperor Vaelkor Draeven → Sovereign Panoply Unbound
**Status:** **WORKING PASS / RAW LINES RETAINED / POWER COMPLETE**

Exact route:
- Chapter-11 end **299,100 EXP**
- mandatory pre-Vaelkor **360,700 EXP = Lv56**
- full two-form clear → **367,700 = Lv56**
- chapter clear → **369,100 = Lv57 exactly**

Completionist:
- fixed optional advantage **166,700 EXP**
- pre-Vaelkor **527,400 EXP = Lv66**
- RH#11 excluded pending exact relative access
- RH#11 pre-clear would produce **541,200 = Lv67**
- high-side **~Lv67**

Emperor of the Reforged Host:
> **ADJUSTED — Lv60 / HP16,800 / ATK223 / MAG209 / DEF155 / Spirit150 / SPD54 / EVA5 / SR10**

Form-I:
- Imperial Cut325 / 25% Bleed
- Sovereign Bolt305 Lightning / 20% Stun
- Reforged Sweep225 AoE
- Imperial Verdict315
- Thronefire205 AoE Fire / 15% Burn
- Imperial Guard N/A

Sovereign Panoply Unbound:
> **ADJUSTED — Lv61 / HP20,200 / ATK238 / MAG224 / DEF163 / Spirit157 / SPD55 / EVA0 / SR10**

Fresh-body:
- no spillover
- no free transition attack
- **Prime availability refreshes**

Form-II:
- Panoply Cleave360 / 25% Bleed
- Unbound Judgment365 / 20% Staggered
- Sovereign Discharge250 AoE Lightning / 15% Stun
- Panoply Barrage2×190
- Imperial Furnace240 AoE Fire / 20% Burn
- Sovereign Overrun390 AoE / 20% Staggered
- Absolute Command N/A

Sovereign Overrun:
- below 55% Form-II HP
- 1-round Protected Preparation
- 3-round repetition lock

Final Sovereignty:
- 25% Form-II HP
- same bar
- +10 Speed / -15 Total Defense
- no Prime refresh

Expected:
- mandatory **~16–18**
- completionist **~12–14**
- high-side ~11–13

Agency:
- genuine surrender offer
- Vaelkor refuses
- Panoply escalation is deliberate
- no possession / no third form

### Chapter 13 — Last Weapon Archon
**Status:** **FORMALLY VALIDATED v89 / RAW LINE RETAINED / POWER COMPLETE**

Exact route:
- Chapter-12 end **369,100 EXP = Lv57**
- all pre-Shelter ordinary before boss **18,600**
- Deepest/Deep City/Archive +4,000
- fragment-survival truth +5,000
- pre-boss **396,700 EXP = Lv58**
- Archon +12,000 → **408,700 = Lv59**
- Last Shelter +6,700 → **415,400 = Lv60 exactly**

Completionist:
- established proof pool +195,000 → **591,700 = Lv69**, 2,400 short of cap
- MH#6 is also legally available if Arbiter was cleared; with it, route is **Lv70 cap**
- balance references mandatory Lv58 / broad completionist Lv69 / full completionist Lv70

Raw:
> **ADJUSTED — Lv63 / HP20,800 / ATK236 / MAG220 / DEF160 / Spirit160 / SPD56 / EVA0 / SR15**

Archive Authority:
- Archon Edge320 / 20% Bleed
- Convergence Lance325
- Compression Ram345 / 20% Staggered
- Discharge Field225 AoE
- Archive Seal N/A

Weapon Protocol Unsealed:
- 60% HP
- same bar
- +10 Speed / -10 Total Defense
- Unsealed Convergence365
- Compression Verdict385 / 25% Staggered
- Weapon Discharge270 AoE
- Threefold Execution3×135
- Archive Collapse250 AoE
- Sequence Alignment N/A
- no Prime refresh

One-time visible sequence:
> convergence → compression → discharge

Expected:
- mandatory normal **~15–17**
- broad completionist Lv69 **~10–12**
- full/cap Lv70 **~9–11**

Story firewall:
- not Entity intelligence
- no possession
- no exact fragment-survival-mechanism reveal

### Chapter 13 — Reconstituted Entity → The Last Command
**Status:** **FORMALLY VALIDATED v89 / HP PACING RETAINED / POWER COMPLETE**

Exact route:
- Last Shelter **415,400 EXP = Lv60**
- post-PONR ordinary +11,200
- Reactor Galleries +3,500
- Reactor–Crest Interface +2,500
- mandatory pre-boss **432,600 EXP = Lv61**
- full two-form clear +13,500 → **446,100 = Lv61**
- Final Severance/ending +2,000 → **448,100 = Lv62 exactly**

Completionist:
> **Lv70 cap**

### Reconstituted Entity
> **HP ADJUSTED — Lv63 / HP22,500 / ATK224 / MAG228 / DEF158 / Spirit163 / SPD55 / EVA5 / SR15**

Form-I:
- Devouring Reach350 / 25% Bleed
- Reconstituted Judgment365
- Continuity Crush380 / 25% Staggered
- Devouring Field240 AoE
- Ruin Memory225 AoE
- Reconstitute N/A

Heart Manifestation:
- max1 at65%
- HP1,100 / Power N/A
- +10 Total Defense / Magic+10%

Continuity Hunger:
-35%
- +10 Speed / -10 Total Defense
- same bar / no Prime refresh

### The Last Command
> **HP ADJUSTED — Lv64 / HP28,500 / ATK247 / MAG247 / DEF168 / Spirit168 / SPD58 / EVA5 / SR15**

Fresh-body:
- no spillover
- no free attack
- **Prime availability refreshes**

Form-II:
- Last Command Strike390 / 25% Bleed
- Total Directive405
- Crest Sever410 / 25% Staggered
- Command Without End280 AoE
- Reincorporation Wave265 AoE
- Crest Rewrite2×210
- Final Directive430 AoE / 25% Staggered
- Absolute Continuity N/A

Unbound Shards:
- max2 at70% / 40%
- HP1,050 each / Power N/A
- +5 Total Defense / +5% ATK/MAG each

Final Directive:
- below55%
- one-round Protected Preparation
-3-round repetition lock

Distributed Command:
-25%
- +10 Speed / -15 Total Defense
- same bar / no Prime refresh

Expected:
- mandatory **~22–24**
- completionist Lv70 **~18–20**

At Form-II 0 HP:
- combat ends
- no third body
- Final Severance begins

Final Severance story manifestations are not blocked by combat Prime usage flags.

## Mandatory story-boss route recertification
> **COMPLETE THROUGH THE FINAL BOSS**

## Next
> **Direct-damage Power audit is closed. Proceed to whole-roster Enemy & Boss Mandatory-vs-Completionist Validation.**


### v53 Vaelkor duration adjustment
User requested a slightly longer Vaelkor climax.

Adjusted:
- Emperor of the Reforged Host HP **13,648 → 14,900**
- Sovereign Panoply Unbound HP **16,615 → 18,100**

Unchanged:
- ATK / MAG / DEF / Spirit / SPD
- action Powers
- status riders
- fresh-body Prime refresh
- Final Sovereignty behavior

Revised expected total:
- mandatory **~18–20 rounds**
- completionist **~13–15**
- high-side **~12–14**


### v54 Vaelkor pacing target
User-set target:
> **18–20 mandatory rounds**

Final HP-only values:
- Form I **16,800 HP**
- Form II **20,200 HP**

No changes to:
- ATK / MAG / DEF / Spirit / SPD
- action Powers
- status riders
- Protected Preparation
- Prime-refresh behavior
- Final Sovereignty


### v56 Last Weapon Archon pacing target
User-set target:
> **15–17 mandatory rounds**

Adjusted:
- Last Weapon Archon HP **18,424 → 20,800**

Unchanged:
- ATK / MAG / DEF / Spirit / SPD
- all action Powers
- all status riders
- 60% Weapon Protocol threshold
- same-bar architecture
- no Prime refresh


## v78 Chapter-2 broader validation note
Chapter 2 was revalidated as a Lv5→9 chapter with Maevra explicitly occupying the fourth active slot. Archive Leviathan and Rhazek pacing remain valid. Archive Leviathan Recorded Pattern is now exact at 20% repeated-action direct-damage reduction, one visible pattern at a time, 2 rounds in State A / 1 round in State B, with a 45% HP same-bar threshold.


## v89 campaign-wide whole-roster handoff
Chapter 13 has now been formally validated at its real Lv57→58 Archon→60 Last Shelter/PONR→61 final-boss→62 ending sequence, with completionist Lv70 at the final sequence. The preliminary mandatory-boss recertification is therefore fully promoted through the finale for the planned paper validation layer. No Chapter-13 raw stat or Power changed in v89. CEXP recalibration is **closed v91**; representative true-battle certification is next.
