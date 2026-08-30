# Diyse — Class Ability MP Costs
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Master-canon class/resource authority:** **v2.08 / Audit123**, with compatible **Audit115** class normalization, later current working corrections, the approved 2026-08-30 global Ability-MP reduction, and the later 2026-08-30 Cardweaver/Routeweaver cost mechanics.  
**Authority treatment:** explicit/newer user corrections override older certified prices and are promoted here as current domain authority.

# Status
**CLOSED under the 2026-08-30 direct correction, with explicitly authored later dynamic/modifier exceptions.**

All fixed-price character Ability/Ultimate authored Base MP costs were reduced by **15%** from the immediately previous authoritative values.

Rounding rule for that closed pass:
> multiply the prior authored Base MP by **0.85**, then round to the nearest whole MP; exact `.5` results round upward.

The exact fixed-price table below is authoritative. Do not reapply the 15% global multiplier at runtime.

Standard Card MP costs were not part of that global pass. Prime Invocation is owned by `07_CARDS` and costs **0 MP**.

## Base Classes
| Class | Ability | Authored Base MP |
|---|---|---:|
| Crest Knight | Crest Strike | 9 |
| Crest Knight | Crest Reprisal | 15 |
| Crest Knight | Resonant Pulse | 10 |
| Crest Knight | Sweeping Edge | 17 |
| Crest Knight | Twin Advance | 19 |
| Crest Knight | Crest Rend | 27 |
| Crest Knight | Crest of Companions | 48 |
| Blue Warden | Mend | 14 |
| Blue Warden | Clear Warding | 15 |
| Blue Warden | Renewal | 22 |
| Blue Warden | Warden's Valor | 15 |
| Blue Warden | Revive | 29 |
| Blue Warden | Lifeline | 34 |
| Blue Warden | Dawn Without End | 51 |
| War Archer | Cinder Shot | 10 |
| War Archer | Sizing Shot | 10 |
| War Archer | Choose the Route | 17 |
| War Archer | Pinning Strike | 15 |
| War Archer | Colossus Draw | 22 |
| War Archer | Relentless Barrage | 26 |
| War Archer | The Great Beast Falls | 44 |
| Cardweaver | Echo Weave | **Variable*** |
| Cardweaver | Weave Burst | 19 |
| Cardweaver | Hastened Weave | 10 |
| Cardweaver | Ancient Override | 26 |
| Cardweaver | Weave Spark | 17 |
| Cardweaver | Perfect Recall | 24 |
| Cardweaver | Grand Reweaving | 48 |
| Green Arcanist | Frost Needle | 12 |
| Green Arcanist | Stonebreak | 12 |
| Green Arcanist | Cinder Bloom | 19 |
| Green Arcanist | Stormburst | 22 |
| Green Arcanist | Prism Lance | 20 |
| Green Arcanist | Spectrum Cascade | 29 |
| Green Arcanist | Arcanum Ascendant | 51 |
| Ruin Vanguard | Ruin Cleave | 9 |
| Ruin Vanguard | Rift Lance | 10 |
| Ruin Vanguard | Ember Brand | 10 |
| Ruin Vanguard | Fracturing Brand | 17 |
| Ruin Vanguard | Call Shardfang | 26 |
| Ruin Vanguard | Unmaking Blow | 26 |
| Ruin Vanguard | Controlled Apocalypse | 51 |

`*` **Echo Weave dynamic Base MP:** choose the record first, then calculate **75% of that recorded action's authored Base MP**, round normally, minimum **8 MP**. That result is Echo Weave's pre-modifier cost for the use. The source actor does not pay again.

## Subclasses
| Class | Ability | Authored Base MP |
|---|---|---:|
| Crest Arcanist | Arcane Lance | 19 |
| Crest Arcanist | Elemental Crest | 15 |
| Crest Arcanist | Nullifying Seal | 22 |
| Crest Arcanist | Arcane Rupture | 31 |
| Crest Arcanist | Elemental Convergence | 27 |
| Crest Arcanist | Crest Dominion | 54 |
| Axiomblade | First Principle | 12 |
| Axiomblade | Proven Advance | 17 |
| Axiomblade | Counterproof | 20 |
| Axiomblade | Axiom Rend | 26 |
| Axiomblade | Equivalent Form | 29 |
| Axiomblade | Final Axiom | 51 |
| Vowblade | Vital Edge | 14 |
| Vowblade | Mercy Returned | 19 |
| Vowblade | Living Covenant | 26 |
| Vowblade | Vowkeeper's Reprisal | 24 |
| Vowblade | Vow of Severance | 32 |
| Vowblade | Mercy's Final Edge | 54 |
| Ruin Warden | Siphon Rune | 14 |
| Ruin Warden | Stolen Grace | 17 |
| Ruin Warden | Restoring Ward | 19 |
| Ruin Warden | Withering Mercy | 29 |
| Ruin Warden | Reclaimed Breath | 32 |
| Ruin Warden | Mercy Through Ruin | 54 |
| Routeweaver | Throughline | 12 |
| Routeweaver | Set the Pace | 15 |
| Routeweaver | Crossroads | 24 |
| Routeweaver | Covered Crossing | 20 |
| Routeweaver | Frozen Passage | 29 |
| Routeweaver | Open the Way | 53 |
| Proofhunter | Measured Shot | 12 |
| Proofhunter | Held Argument | 17 |
| Proofhunter | Pin the Variable | 19 |
| Proofhunter | Structural Failure | 26 |
| Proofhunter | Corroboration | 29 |
| Proofhunter | Final Annotation | 51 |

## Current percentage cost modifiers
These are runtime modifiers and do not rewrite the fixed Base MP table.

- **Cardweaver — Living Archive Rank I:** Nimera's Standard Cards cost **20% less MP**; Rank III increases this to **30% less MP**.
- **Cardweaver — Ancient Override:** while the Field is active, all party members' MP-costing Abilities, Ultimates, and Standard Cards cost **15% less MP**; **Efficient Override** increases this to **20% less MP**. Prime actions remain 0 MP and are unaffected.
- **Routeweaver — Throughline:** the first allied MP-costing Ability or Standard Card each normal round that targets the Throughlined enemy costs **20% less MP**.
- **Routeweaver — Open the Way:** each routed action in its authored next-round sequence costs **20% less MP**.

When two or more of the explicitly compatible percentage cost modifiers above affect the same action, multiply their remaining-cost factors and round the resulting MP cost once to the nearest whole MP, minimum 1 MP. Example: a 30-MP Standard Card under Living Archive Rank I and Ancient Override uses `30 × 0.80 × 0.85 = 20.4`, which rounds to **20 MP**.

Echo Weave establishes its dynamic pre-modifier cost first; Ancient Override or another legal percentage modifier may then reduce that Echo Weave cost.

## Other Mastery / Trait cost modifiers
These modify authored base cost after the relevant effect unlocks:

- Crest Knight — **Clear Channel:** Resonant Pulse 10 → **9**
- Green Arcanist — **Efficient Spectrum:** first eligible elemental Green Arcanist Base Ability each ordinary round costs **2 less MP**, minimum 1
- Ruin Vanguard — **Controlled Unmaking:** Unmaking Blow 26 → **24**
- Crest Arcanist Trait **Crest Resonance Rank I:** all MP-costing Crest Arcanist Abilities cost **2 less MP**, minimum 1

The retired War Archer **Patient Aim** and Cardweaver **Tight Weave** cost modifiers are no longer active.

Runtime ordering for unrelated flat and percentage modifiers may be implemented consistently without reopening the fixed Base MP prices unless a demonstrated contradiction appears.
