# Diyse — Regional Hunt Rewards

**Status:** EXACT REGIONAL-HUNT AUREN AUTHORITY

Exactly **11 Regional Hunts** exist.

## Domain split
- access / quest state → `11_QUESTS`
- enemy combat body → `09_ENEMIES_AND_ENCOUNTERS`
- Player EXP → `10_PROGRESSION_AND_EXP`
- equipment / Forge Component identity → `08_ITEMS_AND_EQUIPMENT`
- Auren / non-EXP economic balancing → `12_ECONOMY_AND_REWARDS`

## Reward philosophy
Regional Hunts are dedicated optional combat objectives and should pay more direct currency than a normal optional Elite at the same stage.

Baseline target:
> roughly **8–9 current-era ordinary formations' worth of Auren**

This is then reduced where a Hunt already supplies a meaningful deterministic Forge Component or other permanent authored reward.

Regional Hunts are first-clear objectives, not repeatable money farms.

## Exact Auren payouts
| # | Regional Hunt | Current access | EXP | Auren | Reward-budget note |
|---:|---|---|---:|---:|---|
| 1 | **Cistern Devourer** | Ch1 | 1,000 | **130** | standard early Hunt cash |
| 2 | **Transfer Executioner** | Ch2 | 1,500 | **180** | standard Hunt cash |
| 3 | **Archive Judgment Engine** | Ch3 | 2,200 | **240** | standard Hunt cash |
| 4 | **Crown Prototype** | Ch4 | 3,000 | **300** | standard Hunt cash |
| 5 | **Whitehorn Ravager** | Ch5 | 4,000 | **300** | **discounted: also supplies an Acuity/Calibration Relic-copy Forge Component** |
| 6 | **Winterglass Titan** | Ch6 | 5,200 | **350** | **discounted: also supplies an Elements/Prismglass Relic-copy Forge Component** |
| 7 | **Rift Gate Colossus** | Ch7 | 6,800 | **500** | standard Hunt cash |
| 8 | **Rift Siege Beast** | Ch8 | 8,500 | **500** | **discounted: also supplies a Ruin/Black Ore Relic-copy Forge Component** |
| 9 | **Mercyfallen Behemoth** | Ch9 | 11,000 | **720** | standard late Hunt cash |
| 10 | **Authority Remnant** | Ch11 | 13,000 | **960** | standard late Hunt cash |
| 11 | **Throne of Emperor Vaelkor** | Ch12 | 13,800 | **1,100** | strongest Regional Hunt; two-form encounter, no separate form payout |

## Full Regional Hunt cash budget
Clearing all 11 Regional Hunts yields:
> **5,280 Auren**

Player EXP across the 11 Hunts remains:
> **70,000 EXP**

The Auren total is optional surplus and is **not** required for mandatory-route baseline solvency.

## Existing Forge Component adjustments
Current source architecture attaches Relic-copy Forge Components to:
- **Whitehorn Ravager** → Acuity / Calibration;
- **Winterglass Titan** → Elements / Prismglass;
- **Rift Siege Beast** → Ruin / Black Ore.

Those permanent-material rewards are part of the Hunt's total value, so their direct Auren is intentionally below a pure-cash Hunt of comparable stage.

### Timing-authority note
The current Hunt access register and current Whitehorn combat file place **Whitehorn Ravager in Chapter 5**. An older Forge Component source matrix still carries a Chapter-6 label for that source. This reward file follows the current Hunt-access identity and does not move the Hunt; the source matrix needs a separate owner-domain synchronization pass.

## First-clear / form rules
- Auren is granted once for Hunt completion.
- A fresh HP form does **not** produce another Auren reward.
- Summoned, attendant, or generated support bodies pay **0 additional Auren**.
- Re-fighting a Hunt, if a future implementation ever allows it, does not automatically repeat the first-clear payout.

## No automatic extra package
Do not automatically add:
- random Consumable bundles;
- vendor-trash materials;
- ordinary equipment;
- Relics;
- Cards/Primes;

to every Regional Hunt merely for symmetry.

Any separately authored permanent reward remains part of that Hunt's total reward budget and should trigger a cash review if changed.
