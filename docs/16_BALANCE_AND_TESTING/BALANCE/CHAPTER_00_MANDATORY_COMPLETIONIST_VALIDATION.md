# Diyse — Chapter 0 Mandatory-vs-Completionist Validation

**Chapter:** 0 — The Broken Convoy  
**Status:** **ADJUSTED / VALIDATED**  
**Power audit:** **CLOSED — NO POWER VALUES CHANGED**

## Route relationship
Chapter 0 has no meaningful completionist divergence before its combat is resolved.

Therefore:
> **mandatory baseline = completionist baseline for Chapter 0**

Optional Character-Life material opens only after the mandatory chapter state and does not improve these encounters.

## Player baseline
### Cyanis — S001 through S002
Player Level:
> **Lv1 / static**

Class:
> Crest Knight CL1

Guaranteed body:
- HP 231
- MP 25
- ATK 56
- MAG 45
- DEF 61
- Spirit 47
- SPD 21

Guaranteed equipment:
- Crestblade
- Crest Plate
- Yahtrean Shield

Guaranteed field resources:
- **3 Field Salves**

CL1 relevant offense:
- Basic Attack — 100 Power Physical
- Crest Strike — 140 Power / 10 MP
- Resonant Pulse — 150 Power Magical / 12 MP

### S005 party
Cyanis retains the above body.

Ilyra joins combat at Lv1 / Blue Warden CL1 with:
- HP 220
- MP 31
- ATK 45
- MAG 59
- DEF 34
- Spirit 59
- SPD 22

Guaranteed equipment:
- Wardrod
- Blue Warden Mail
- Warding Focus

S005 begins from an authored fresh encounter state:
> **Cyanis and Ilyra start at full HP and full MP**

This recovery boundary is not a Card/Prime effect.

S005 also retains:
> **+15 Total Defense to Cyanis and Ilyra for Rounds 1–3**

## Damage reference — Cyanis
Approximate direct damage under the current formula before crits or temporary defensive states:

| Target | Basic Attack | Crest Strike | Resonant Pulse |
|---|---:|---:|---:|
| Ch0 Raider | 46.8 | 65.5 | 55.2 |
| Crossbowman | 47.5 | 66.5 | 55.2 |
| Ruin Shieldbearer | 41.3 | 57.8 | 49.0 |
| Beast Handler / Convoy Rift Hound | 43.6 | 61.0 | ~50–51 |
| Ruin Vanguard Pursuer | 38.7 | 54.2 | 45.3 |
| Riftmaw | 38.7 | 54.2 | 45.3 |
| Injured Soldier | 43.0 | 60.1 | 51.5 |
| War-Sorcerer | 40.2 | 56.3 | 42.8 |

## Encounter findings
### 0-01 — Opening Line
Raider + Crossbowman + Shieldbearer

Result:
> **PASS**

The individual actions are deliberately low-pressure against Cyanis's starting defenses, while the three-body action economy creates the intended tutorial pressure.

No Power adjustment required.

### 0-02 — Handler Pressure
Beast Handler + Convoy Rift Hound

Result:
> **PASS**

Drive the Hound increases the next Hound direct-damage action but grants no extra action. The formation is materially stronger than 0-01 without creating an early one-round kill threat.

No Power adjustment required.

### 0-03 — Ruin Vanguard Pursuer
Protected disengagement at 70% HP or after two full rounds.

Result:
> **PASS**

The 620-HP body is not a true time-to-zero durability target. The two-round/70% disengagement rule controls duration and keeps the encounter threatening without demanding a kill.

No Power or raw-stat adjustment required.

### 0-04 — Riftmaw
Original current body entering this validation:
> **760 HP**

At Cyanis's actual Lv1 body, that durability projected roughly **18–20 basic-equivalent solo actions** before defensive turns/misses, despite the action kit itself being survivable.

That is excessive solved-state duration for a solo Chapter-0 boss and creates an endurance failure after the preceding authored encounters.

Targeted tuning:
> **Riftmaw HP 760 → 340**

All other Riftmaw raw stats and all Power values remain unchanged.

At 340 HP:
- basic-only clear is about **9 successful Cyanis attacks** before Guard/miss variation;
- a saved Crest Strike shortens that slightly;
- incoming legal direct-damage actions remain threatening but survivable from a properly recovered state;
- the guaranteed Field Salves make the authored S001 endurance line recoverable without a hidden normal-shop assumption.

Result:
> **ADJUSTED**

### 0-05 — S002 Convoy Rift Hound
Exactly one Hound.

Result:
> **PASS**

Its current durability and damage remain appropriate for a post-boss authored solo pressure encounter when the guaranteed Field Salves are included in the mandatory baseline.

No Power/raw adjustment required.

### 0-06 — S005 War-Sorcerer + injured Soldier
War-Sorcerer HP620 / Soldier HP165.

The War-Sorcerer remains the encounter victory target under the current S005 authority.

Baseline two-character basic throughput against the War-Sorcerer is approximately:
- Cyanis: 40.2
- Ilyra: 30.2
- combined: **~70.4 damage per round** before Ability use

That puts the central target around a **9-round basic-attack reference**, while Ilyra's healing and the three-round +15 Total Defense protection carry the intended survival/tutorial burden.

Rift Lance remains a visible once-per-battle prepared spike rather than routine pressure.

Result:
> **PASS**

No Power/raw adjustment required.

## Chapter 0 certification
### Mandatory route
> **PASS AFTER TARGETED RIFTMAW DURABILITY ADJUSTMENT**

### Completionist route
> **SAME BASELINE / PASS**

There is no optional-progression gap to erase or preserve inside Chapter 0.

## Changes made by this validation
1. Restored the neutral Player-Level natural-stat formula to the active progression folder.
2. Added explicit guaranteed Cyanis/Ilyra Chapter-0 starting loadouts for reproducible player bodies.
3. Guaranteed **3 Field Salves** as Chapter-0 field issue; normal shop progression remains unchanged.
4. Reduced **Riftmaw HP 760 → 340**.
5. Changed **zero direct-damage Power values**.

## Next validation frontier
Do not redo the already-authored preliminary mandatory story-boss recertification for Chapters 1–13 unless the broader formation/resource pass exposes a contradiction.

Proceed to:
> **Chapter 1 ordinary formations + Watch Captain Frame + authored/nonlethal content + Cistern Devourer**, while carrying Hollow Watch Castellan's existing mandatory/completionist boss recertification forward.
