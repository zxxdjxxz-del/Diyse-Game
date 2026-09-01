# Diyse — Boss Effective Stat Level +5 Sensitivity — v106

**Status:** WORKING SENSITIVITY / NOT OWNER CANON  
**Global layer retained for comparison:** enemy direct-damage Power × **1.20**  
**Purpose:** test whether bosses should keep their displayed/authored Level but use core combat stats equivalent to five additional levels of stat growth.

## Rule under test
Enemy levels in Diyse are authored, not dynamically scaled. For a deterministic sensitivity, preserve each boss's existing identity ratios and apply the same five-level growth ratio from the active natural-stat curve to:
- Attack;
- Magic;
- Defense;
- Spirit;
- Speed.

Keep unchanged:
- displayed Level;
- HP;
- EXP/CEXP reward;
- Evasion / Status Resistance;
- direct-damage Power apart from the separate active ×1.20 global sensitivity;
- Base Hit / Crit / status chances;
- AI / repetition locks / mechanics / forms.

### Why HP is held fixed
Boss HP is already authored separately around encounter duration. Applying the natural +5-level HP ratio would add roughly:
- Ch3: +30% HP;
- Ch6: +18–19% HP;
- Ch9: +13–14% HP;
- Ch12: +10–11% HP.

That would primarily lengthen fights and obscure whether the core-stat increase improves danger. This sensitivity therefore treats HP as pacing authority and leaves it unchanged.

## Growth ratios
Approximate +5-level core-stat growth from the active curve:
- Lv14 → effective Lv19 stats: ATK/MAG +25.0%, DEF/SPR +24.1%, SPD +9.0%;
- Lv28–29 → effective Lv33–34 stats: ATK/MAG +15.5–15.9%, DEF/SPR +15.1–15.5%, SPD +7.1–7.2%;
- Lv43–44 → effective Lv48–49 stats: ATK/MAG +11.5–11.7%, DEF/SPR +11.2–11.4%, SPD +5.9%;
- Lv60–61 → effective Lv65–66 stats: ATK/MAG +9.0–9.1%, DEF/SPR +8.8–8.9%, SPD +4.9%.

## Representative raw lines

| Encounter/form | Display Lv | HP retained | ATK | MAG | DEF | Spirit | SPD |
|---|---:|---:|---:|---:|---:|---:|---:|
| First Command Warden | 14 | 2,850 | **90** | **90** | **53** | **53** | **33** |
| Zevraya — Blood Matron | 28 | 4,400 | **104** | **141** | **79** | **88** | **43** |
| Zevraya — Perfected War Mother | 29 | 5,200 | **129** | **153** | **83** | **92** | **45** |
| Rhazek — Reforged Commander | 43 | 8,431 | **182** | **112** | **124** | **107** | **47** |
| Rhazek — Bastion Devourer | 44 | 10,462 | **195** | **146** | **119** | **116** | **49** |
| Vaelkor — Emperor | 60 | 16,800 | **243** | **228** | **169** | **163** | **57** |
| Vaelkor — Sovereign Panoply | 61 | 20,200 | **259** | **244** | **177** | **171** | **58** |

## Direct-damage effect with ×1.20 Power
Against the same mandatory equipment snapshots used by v105, the +5 core-stat growth increases direct damage from the boss's ATK/MAG nonlinearly through the current damage formula.

Approximate average direct-hit change compared with current owner stats:
- Ch3 Warden: core-stat growth alone ~+37%; with ×1.20 Power, roughly **+65% direct damage vs current canon**;
- Ch6 Zevraya: core-stat growth alone ~+23%; with ×1.20 Power, roughly **+48% direct damage**;
- Ch9 Rhazek: core-stat growth alone ~+17%; with ×1.20 Power, roughly **+40–41% direct damage**;
- Ch12 Vaelkor: core-stat growth alone ~+13%; with ×1.20 Power, roughly **+35–36% direct damage**.

Boss DEF/Spirit growth also lowers player direct throughput modestly without requiring HP inflation:
- Ch3: roughly 7–8% lower direct throughput against the boss;
- Ch6: roughly 5% lower;
- Ch9: roughly 4% lower;
- Ch12: roughly 3–4% lower.

This should add a small amount of encounter duration while increasing danger much more than duration.

## Calibrated difficulty read from v105 response curves
The v105 four-point study already measured how KO incidence responds as direct offensive pressure rises from +20% toward +35%. Mapping the +5 core-stat package onto those response curves gives the following **sensitivity ranges**, not runtime-certification results:

- **Ch3 First Command Warden:** likely moves out of the near-zero KO floor into roughly a **single-digit to low-teens KO environment**, but its Command Seal/Ring/analogue action-tax structure may still require local pressure tuning.
- **Ch6 Zevraya:** likely moves into roughly a **20–30% mandatory any-KO environment** even before the separate Reservoir action-density rewrite; max-level same-gear should remain materially safer.
- **Ch9 Rhazek:** likely remains only around a **few-percent mandatory KO environment** because support/Preparation/exposed-state windows still dilute pressure. +5 stats alone probably does not solve Rhazek.
- **Ch12 Vaelkor:** likely reaches roughly a **high-teens / ~20% mandatory any-KO environment**, much closer to the desired mandatory climax profile while same-gear Lv67 remains substantially safer.

## Design read
This sensitivity is more promising than simply raising boss Power again because it strengthens several boss-facing axes at once:
1. harder direct hits through ATK/MAG;
2. slightly longer pressure windows through DEF/Spirit;
3. more initiative pressure through SPD;
4. no HP sponge inflation;
5. displayed encounter Level and reward structure remain unchanged.

It also naturally tapers over the campaign: the early boss receives a larger proportional stat correction while late bosses receive a smaller one.

## Current working conclusion
> **PROMISING BOSS-WIDE LAYER: +5 EFFECTIVE CORE-STAT LEVELS, DISPLAY LEVEL AND HP UNCHANGED**

Keep the global ordinary/enemy ×1.20 Power experiment separate.

Expected two-layer structure if later certified:
- ordinary/hostile roster: global direct-Power floor around ×1.20;
- bosses: ×1.20 Power plus +5 effective core-stat levels;
- individual bosses such as Rhazek may still require local action-density/mechanic tuning.

Do not promote owner files until exact true-battle reruns confirm the sensitivity.
