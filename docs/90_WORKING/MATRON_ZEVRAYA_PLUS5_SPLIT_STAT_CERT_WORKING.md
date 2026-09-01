# Matron Zevraya — +5 Split-Stat Certification

**Status:** WORKING DIYSIM BALANCE FINDING / NOT OWNER CANON / NOT APPROVED FOR MAIN  
**Encounter owner remains:** `09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/MATRON_ZEVRAYA.md`  
**Companion snapshot:** `docs/90_WORKING/MATRON_ZEVRAYA_TRUE_BATTLE_SNAPSHOT_WORKING.md`

This report refines the older statement that a `+5 effective-stat-level` Zevraya layer was rejected. The older test raised **ATK, MAG, DEF, Spirit, and Speed together**. DiySim now supports split stat-level sensitivity so offensive pressure can be separated from durability inflation.

## Test frame
- Non-diluting Reservoir structure.
- Enemy direct-damage Power ×1.20.
- Mandatory party: Lv24.
- High-side party: Lv28.
- Same prepared Chapter-6 inventory and ordinary-equipment benchmark as the companion snapshot.
- Competent mechanic line: **Brood → Armor**.
- Comparison line: Rush, while still killing deployed Brood as a finite hostile body.
- Certification: **2,000 runs per line**, fresh seed 113.

## Split meaning
- **Offense +5:** scale Zevraya ATK/MAG by the neutral natural-curve ratio for +5 effective levels. Keep DEF, Spirit, Speed, HP, and MP at owner values.
- **All-core +5:** legacy overlay; scale ATK/MAG/DEF/Spirit/SPD together by +5 effective levels. HP/MP remain unchanged.

A corrected 1,000-run isolation screen also tested DEF/Spirit-only +5 and offense+Speed +5. DEF/Spirit-only increased duration and hazard exposure; offense+Speed was effectively identical to offense-only in this encounter because the Speed change did not cross a relevant turn-order threshold.

## 2,000-run certification

| Player line | Stat mode | Strategy | Win | Any KO | Wipe | Mean rounds | Ending HP | Items |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Lv24 mandatory | **Offense +5** | **Brood → Armor** | **96.15%** | **53.75%** | **3.85%** | **31.18** | **36.02%** | **7.95** |
| Lv24 mandatory | Offense +5 | Rush | **87.85%** | **72.35%** | **12.05%** | 32.69 | 26.82% | 8.61 |
| Lv24 mandatory | All-core +5 | **Brood → Armor** | **88.15%** | **72.20%** | **11.45%** | **33.24** | **27.13%** | **8.46** |
| Lv24 mandatory | All-core +5 | Rush | **68.95%** | **88.60%** | **28.55%** | 34.99 | 16.84% | 9.05 |
| Lv28 high-side | **Offense +5** | **Brood → Armor** | **100%** | **0.55%** | **0%** | **24.39** | **59.28%** | **4.88** |
| Lv28 high-side | Offense +5 | Rush | **100%** | **2.20%** | **0%** | 25.71 | 56.47% | 5.70 |
| Lv28 high-side | All-core +5 | **Brood → Armor** | **100%** | **1.55%** | **0%** | **26.13** | **56.58%** | **5.59** |
| Lv28 high-side | All-core +5 | Rush | **100%** | **6.10%** | **0%** | 27.57 | 53.52% | 6.43 |

## Isolation finding
The user hypothesis is confirmed: **raising DEF and Spirit is materially pushing the fight farther**.

At Lv24 with competent Brood → Armor play:
- offense-only +5: 31.18 rounds / 3.85% wipes;
- all-core +5: 33.24 rounds / 11.45% wipes.

The extra defensive scaling adds roughly two rounds while the boss is also hitting at the +5 offensive level. Those additional rounds create more Conduction, Bleed, control, and general damage exposure, so the effects compound rather than simply add.

In the corrected 1,000-run isolation screen, DEF/Spirit-only +5 was approximately 99.2% wins / 24.4% any-KO / 0.8% wipes at 31.85 rounds. That confirms durability by itself is not the main lethal pressure; it becomes severe when stacked with the offensive increase.

## Working interpretation
A minimum-level player is intended to be punished for arriving at only the mandatory level. On that philosophy, **+5 remains viable**, but the cleaner implementation is currently:

> **Power ×1.20 + Zevraya ATK/MAG effective-stat +5, while leaving DEF/Spirit and Speed at owner values.**

Why this is the stronger working candidate:
- competent Lv24 play is dangerous and resource-heavy rather than nearly automatic;
- ignoring the Reservoir mechanic is punished much harder: wipe rate rises from 3.85% to 12.05%;
- Lv28 still receives a dramatic reward for additional leveling: 100% wins and effectively no wipes;
- Zevraya becomes more threatening without also becoming a damage sponge;
- the old all-core +5 rejection should no longer be interpreted as evidence against **offense-only +5**.

All-core +5 is still mechanically possible if the intended mandatory-level experience is substantially harsher: even correct Brood → Armor play wipes about 11% of simulated runs and Rush wipes about 29%. That is a separate difficulty target, not merely a stronger version of the same clean offensive-pressure adjustment.

## Validation
- Split-overlay unit tests passed.
- Hollow Watch regression gate passed.
- First Command Warden regression/sensitivity gate passed.
- Normal DiySim branch workflow passed after the split-stat changes.
- +5 certification workflow completed all eight cells successfully.

This report changes no owner canon and does not modify `main`.
