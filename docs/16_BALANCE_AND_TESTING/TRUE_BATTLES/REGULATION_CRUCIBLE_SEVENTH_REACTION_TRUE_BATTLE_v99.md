# Regulation Crucible → The Seventh Reaction — Representative True-Battle Certification

**Version:** v99  
**Chapter / Scene:** Chapter 4 / S024 — Regulation Core  
**Encounter:** Regulation Crucible → The Seventh Reaction  
**Test type:** design-layer stochastic true-battle simulation  
**Verdict:** **PASS / RETAIN**

## Purpose
This test supersedes the older paper-only Chapter-4 pacing estimate for the mandatory two-form boss. It resolves actual round order, MP, healing, Items, targeting, Hit/Evasion, Criticals, harmful statuses, chamber state, fresh-form transition behavior, current Recovered Last Sentinel use, and current enemy action-selection fallback.

This is not runtime-engine QA. It is the current design oracle for later implementation and engine testing.

## Encounter authority used
### Form I — Regulation Crucible
- Lv18
- HP **2,400**
- ATK **64**
- MAG **90**
- DEF **54**
- Spirit **57**
- SPD **30**
- EVA **0**
- SR **10**

Four targetable chambers:
- Fire / Ice / Lightning / Earth
- **300 HP / 48 DEF / 50 Spirit / 0 EVA / 10 SR** each
- chambers have no independent turns
- exactly two scheduled active chamber slots per round
- destroyed chambers stay destroyed and scheduled destroyed slots remain empty

Form-I direct damage:
- Regulation Slash — **185 Power**
- Pairwise Return — **100 Power × up to 2**
- Compensating Drive — **220 Power**
- Core Discharge — **135 Power per target**
- Regulator Guard — **Power N/A**; Defense +10% / Spirit +10% through end of following round

### Form II — The Seventh Reaction
- genuine fresh body
- Lv19
- HP **2,900**
- ATK **72**
- MAG **98**
- DEF **58**
- Spirit **62**
- SPD **32**
- EVA **0**
- SR **10**

Surviving chamber identities carry into Form II. Destroyed identities remain absent. If all four chambers were destroyed, the inherited element cycle is Colorless with no inherited elemental harmful-status rider.

Form-II direct damage:
- Unified Impact — **205 Power**
- Compression Lance — **245 Power**
- Seventh Confluence — **160 Power per target**
- Overflow Equation — **2 × 115 Power**
- Central Rebalance — **Power N/A**; Spirit +10% / Speed +10% through end of following round

### Fresh-form Prime rule
The Form-I → Form-II transition:
- does not spill damage forward;
- does not award an intermediate reward;
- does not respawn destroyed chambers;
- does **not** restore a spent Prime identity.

A Ready Prime that was not used in Form I remains Ready normally. A Prime spent in Form I remains spent until a valid rest/restoration event.

## Enemy action selection
The encounter has no separate current percentage-weight table.

The current enemy action-selection fallback therefore applies:
1. enforce form/state eligibility and repetition locks;
2. build the currently legal selected-action set when the boss turn arrives;
3. select uniformly at random among those legal actions.

Single-target actions use uniform random selection among currently conscious legal party targets in this design-layer model. Enemy AI does not inspect future uncommitted player choices.

## Party snapshot — strict mandatory route
**Player Level:** Lv15  
**Active party:** Cyanis / Ilyra / Torren / Vaelira  
**Available permanent roster:** Cyanis / Ilyra / Torren / Nimera / Vaelira  
**Starting state:** full HP / full MP boss-isolation benchmark  
**Subclass:** unavailable  
**Standard Cards:** conservatively omitted from the primary test  
**Prime:** Recovered Last Sentinel tested both unused and used once; never refreshed by Form II

Current mandatory planning Class-Level centers immediately pre-boss:
- Cyanis — Crest Knight **CL6**
- Ilyra — Blue Warden **CL6**
- Torren — War Archer **CL7**
- Nimera — Cardweaver **CL5**, near CL6
- Vaelira — Green Arcanist **CL7**

### Strict equipment snapshot
The strict mandatory test does not assume later optional/reward gear.

Cyanis:
- Crestblade
- Crest Plate
- Yahtrean Shield
- combat body: **788 HP / 69 MP**

Ilyra:
- Wardrod
- Blue Warden Mail
- Warding Focus
- combat body: **751 HP / 86 MP**

Torren:
- Yahtrean War Bow
- War Archer Gear
- combat body: **751 HP / 73 MP**

Vaelira:
- Arcanist Staff
- Green Arcanist Garb
- combat body: **616 HP / 96 MP**

No tested item in this snapshot carries a Max-HP or Max-MP equipment modifier, so the later-restored flat Max HP / Max MP equipment rule does not change this certification result.

## Prepared consumable snapshot
The strict mandatory prepared test uses normal purchasable stock available by Chapter 4:
- 3 × Restorative Salve — 750 HP each
- 2 × Flow Tonic — 50 MP each
- 2 × Stability Remedy
- 2 × Rousing Salts

Total purchase value:
> **460 Auren**

This is a reproducible preparation benchmark, **not a mandatory free grant**.

Smart Item policy:
- revive a KO ally with Rousing Salts when immediate Ilyra recovery is not the better legal line;
- use Stability Remedy on an actionable Freeze/Stun/Staggered target when control removal matters immediately;
- use Restorative Salve when party HP pressure reaches the policy threshold;
- use Flow Tonic to preserve necessary healing/offense when MP becomes the binding resource.

Items spend the actor's normal turn.

## Player tactical policies
Two meaningful Form-I policies were tested.

### Core rush
Prioritize the 2,400-HP core and carry all surviving chamber identities into Form II.

### Chamber control
Spend enough offense to remove chambers before finishing the core. This deliberately trades some Form-I tempo for reduced inherited Form-II elemental/status pressure.

For both policies:
- Ilyra prioritizes survival, necessary healing, and legal cleanse;
- Torren establishes Hunter's Measure and uses his strongest legal measured offense when MP permits;
- Vaelira uses her strongest legal elemental offense while managing MP;
- Cyanis uses current learned Crest Knight offense and contributes Items when that is the stronger line;
- Recovered Last Sentinel, when enabled, is saved for Form II and used once;
- the fresh form never restores that Prime use.

## Repeated-run results — strict mandatory Lv15
Each row uses **5,000 runs** with the same policy and legal preparation state.

| Form-I policy | Recovered Last Sentinel | Win rate | Median rounds | Mean rounds | P90 rounds | Any KO | Mean ending HP | Mean ending MP | Mean harmful statuses | Mean Items used |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Core rush | No Prime | **100%** | **18** | **17.78** | **19** | **0.20%** | 65.88% | 7.89% | 2.54 | 4.94 |
| Core rush | Use Last Sentinel in Form II | **100%** | **14** | **14.18** | **16** | **0.02%** | 65.02% | 7.64% | 1.93 | 3.77 |
| Chamber control | No Prime | **100%** | **18** | **18.34** | **20** | **0.06%** | 66.52% | 6.52% | **0.33** | 3.97 |
| Chamber control | Use Last Sentinel in Form II | **100%** | **15** | **14.89** | **17** | **0.08%** | 64.46% | 6.35% | **0.31** | 3.06 |

## Completionist / upgraded reference
A plausible Lv17 completionist/upgraded ordinary-equipment reference was also tested as a comparative stress line.

| Reference | Win rate | Median rounds | Mean rounds | P90 rounds | Any KO |
|---|---:|---:|---:|---:|---:|
| Lv17 + Recovered Last Sentinel | **100%** | **13** | **12.70** | **14** | 6.16% |
| Lv17, no Prime | **99.74%** | **16** | **16.44** | **18** | 29.02% |

These completionist rows are comparative references, not the strict mandatory oracle.

## Chamber-mechanic result
The chamber mechanic is doing real tactical work.

At strict mandatory Lv15 without Prime:
- core rush averages about **2.54** harmful-status applications;
- chamber control averages about **0.33**;
- median duration remains **18 rounds** in both lines;
- chamber control also lowers average Item expenditure from about **4.94 → 3.97**.

Therefore chamber removal is not fake busywork and does not merely inflate duration. It exchanges some Form-I actions for dramatically safer Form-II inheritance while keeping overall pacing in the same band.

## Prime-value result
Recovered Last Sentinel is strong but not mandatory.

On strict mandatory core rush:
- no Prime median = **18 rounds**;
- with one Recovered Last Sentinel use = **14 rounds**;
- both lines = **100% wins** in 5,000 runs.

The Prime therefore provides a major tempo/safety reward without functioning as a required key and without needing a fresh-form refresh.

## Resource-pressure result
The encounter is intentionally long enough that MP matters.

Strict mandatory winning lines finish with only about **6–8% mean MP remaining**, depending route. That makes Flow Tonic and ordinary resource management meaningful while the prepared inventory prevents the fight from becoming a random MP-collapse check.

The result does not demonstrate a reason to reduce boss HP. It demonstrates that the two-form encounter is a major Chapter-4 resource test.

## Representative strict mandatory battle log
The following representative clear uses:
- Lv15 strict equipment;
- core rush;
- prepared consumables above;
- **no Prime**;
- seed 60;
- current legal boss-action fallback.

Result:
> **WIN — Round 18 / 6 Items used / 2 harmful statuses / 0 KO**

### Round 1 — Regulation Crucible
Active chambers: Fire / Ice
- Vaelira — Prism Lance
- Regulation Crucible — Pairwise Return [Fire / Ice]
- Ilyra — Stability Remedy → Torren, removing Freeze
- Torren — Sizing Shot
- Cyanis — Twin Advance

End: core **2,019 / 2,400**. Party MP: Cyanis 50 / Ilyra 86 / Torren 63 / Vaelira 76.

### Round 2
Active chambers: Lightning / Earth
- Vaelira — Prism Lance
- Regulation Crucible — Regulation Slash
- Ilyra — Warden's Valor
- Torren — Colossus Draw
- Cyanis — Twin Advance

End: core **1,339 / 2,400**.

### Round 3
Active chambers: Fire / Lightning
- Vaelira — Prism Lance
- Regulation Crucible — Regulator Guard
- Ilyra — Warden's Valor
- Torren — Colossus Draw
- Cyanis — Twin Advance

End: core **596 / 2,400**.

### Round 4
Active chambers: Ice / Earth
- Vaelira — Prism Lance
- Regulation Crucible — Regulation Slash
- Ilyra — Warden's Valor
- Torren — Sizing Shot
- Cyanis — Crest Strike

End: core **167 / 2,400**.

### Round 5 — fresh-form transition
Active chambers: Fire / Ice
- Vaelira — Prism Lance
- Regulation Crucible — Core Discharge
- Ilyra — Warden's Valor; Form-I core reaches 0
- **TRANSITION:** all four chambers survived; The Seventh Reaction appears at **2,900 / 2,900**. No Prime restoration occurs.
- Torren — Attack against Form II
- Cyanis — Flow Tonic → Cyanis

End: Form II **2,833 / 2,900**.

### Round 6
Inherited element: Ice
- The Seventh Reaction — Central Rebalance
- Vaelira — Flow Tonic → Vaelira
- Ilyra — Warden's Valor
- Torren — Attack
- Cyanis — Twin Advance

End: **2,560 / 2,900**.

### Round 7
Inherited element: Lightning
- The Seventh Reaction — Compression Lance
- Vaelira — Prism Lance
- Ilyra — Attack
- Torren — Attack
- Cyanis — Twin Advance

End: **2,193 / 2,900**.

### Round 8
Inherited element: Earth
- The Seventh Reaction — Unified Impact
- Vaelira — Prism Lance
- Ilyra — Attack
- Torren — Attack
- Cyanis — Crest Strike

End: **1,777 / 2,900**.

### Round 9
Inherited element: Fire
- The Seventh Reaction — Compression Lance
- Vaelira — Frost Needle
- Ilyra — Attack
- Torren — Attack
- Cyanis — Attack

End: **1,515 / 2,900**.

### Round 10
Inherited element: Ice
- The Seventh Reaction — Seventh Confluence
- Vaelira — Attack
- Ilyra — Attack
- Torren — Attack
- Cyanis — Attack

End: **1,338 / 2,900**.

### Round 11
Inherited element: Lightning
- The Seventh Reaction — Central Rebalance
- Vaelira — Attack
- Ilyra — Attack
- Torren — Attack
- Cyanis — Attack

End: **1,161 / 2,900**.

### Round 12
Inherited element: Earth
- The Seventh Reaction — Unified Impact
- Vaelira — Attack
- Ilyra — Attack
- Torren — Attack
- Cyanis — Attack

End: **984 / 2,900**.

### Round 13
Inherited element: Fire
- The Seventh Reaction — Overflow Equation
- Vaelira — Restorative Salve → Vaelira
- Ilyra — Attack
- Torren — Attack
- Cyanis — Attack

End: **825 / 2,900**.

### Round 14
Inherited element: Ice
- The Seventh Reaction — Central Rebalance
- Vaelira — Attack
- Ilyra — Attack
- Torren — Attack
- Cyanis — Attack

End: **648 / 2,900**.

### Round 15
Inherited element: Lightning
- The Seventh Reaction — Compression Lance
- Vaelira — Stability Remedy → Vaelira, removing Stun
- Ilyra — Attack
- Torren — Attack
- Cyanis — Attack

End: **488 / 2,900**.

### Round 16
Inherited element: Earth
- The Seventh Reaction — Overflow Equation
- Vaelira — Restorative Salve → Torren
- Ilyra — Attack
- Torren — Attack
- Cyanis — Attack

End: **329 / 2,900**.

### Round 17
Inherited element: Fire
- The Seventh Reaction — Compression Lance
- Vaelira — Attack
- Ilyra — Attack
- Torren — Attack
- Cyanis — Attack

End: **132 / 2,900**.

### Round 18
Inherited element: Ice
- The Seventh Reaction — Central Rebalance
- Vaelira — Attack
- Ilyra — Attack
- Torren — Attack
- Cyanis — Attack; The Seventh Reaction reaches 0 HP and the encounter ends.

Representative ending state:
- no KO;
- about **76.6% aggregate HP** remaining;
- about **9.0% aggregate MP** remaining.

## Updated pacing interpretation
The old paper expectation of a universal **~13–15 mandatory rounds** is retired.

Current true-battle read:
- **strict mandatory Lv15, prepared, no Prime:** center around **18 rounds**, P90 about **19–20**;
- **strict mandatory Lv15, prepared, one Recovered Last Sentinel use:** center around **14–15 rounds**;
- **completionist Lv17, no Prime:** center around **16 rounds**;
- **completionist Lv17, one Recovered Last Sentinel use:** center around **13 rounds**.

This is a healthier description because it makes Prime use and chamber control visible choices instead of collapsing every legal route into one old paper band.

## Final verdict
> **PASS / RETAIN BOTH FORMS.**

Retain:
- Form-I HP **2,400**;
- Form-II fresh HP **2,900**;
- all current raw stats;
- all current direct-damage Powers;
- current chamber HP/stat lines;
- current chamber inheritance architecture;
- current no-Prime-refresh fresh-form rule.

No HP, raw-stat, Power, status-chance, or Prime-rule change is required.

The representative true-battle suite may advance to its midgame control/action-tax anchor.
