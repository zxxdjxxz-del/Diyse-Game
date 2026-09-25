> **v96 BLEED RULE NOTE:** Bleed now starts at **3% Max HP per qualifying proc** and escalates to **4%** after the affected unit completes 3 turns with that Bleed uncleared. The Normal/Smart and Safety lines remain valid for the encounter-body verdict because their tested Ballista-priority policy prevented Heavy Bolt Bleed from occurring. The historical Aggressive support-ignore Bleed-risk percentages below are **superseded** and must be refreshed before being used as current risk metrics.

# Watch Castellan — True-Battle Certification v93

**Encounter:** Chapter 1 / S008  
**Test layer:** actual round-resolution simulation, distinct from paper balance  
**Verdict:** **TRUE-BATTLE PASS — RETAIN CURRENT 450-HP BODY / CURRENT POWERS**

## Snapshot — mandatory
- Party: **Cyanis + Ilyra + Maevra guest**
- Character Level: **Lv2**
- Active size: **3**
- Class access: Crest Knight / Blue Warden current early kit; no CL3 unlocks are assumed. Whether the exact S008 CEXP point is CL1 or CL2 is combat-equivalent because CL2 unlocks no Ability, Mastery, Trait rank, or stat package.
- Cards: **none before first clear**; Faultline Sight is the S008 first-clear reward.
- Primes: **none**; Prime access begins later.
- Equipment:
  - Cyanis — Crestblade / Crest Plate / Yahtrean Shield
  - Ilyra — Wardrod / Blue Warden Mail / Warding Focus
  - Maevra — Command Spear / Commander's Harness guest package
- Starting state for this boss-isolation benchmark: **full HP / full MP**.
- Consumables: not used in the baseline simulation.

### Exact Lv2 bodies
| Character | HP | MP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Cyanis | 267 | 28 | 59 | 47 | 63 | 49 | 22 | 0 | 0 |
| Ilyra | 254 | 35 | 47 | 61 | 35 | 60 | 22 | 0 | 0 |
| Maevra | 267 | 27 | 40 | 16 | 28 | 27 | 23 | 5 | 5 |

## Snapshot — completionist/high-side
Chapter 1 has almost no optional equipment/Card divergence before S008. The meaningful high-side is **Lv3** with the same legal equipment and no pre-clear Card/Prime access.

| Character | HP | MP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Cyanis | 304 | 31 | 61 | 49 | 65 | 50 | 22 | 0 | 0 |
| Ilyra | 289 | 39 | 48 | 63 | 37 | 62 | 23 | 0 | 0 |
| Maevra | 283 | 28 | 42 | 17 | 29 | 27 | 23 | 5 | 5 |

## Restored rules used by the simulation
- permanent-character / story-guest damaging Abilities without an explicit current Base Hit use **Base Hit 100**;
- Basic Attack: Physical / Neutral / 100 Power / Base Hit 100;
- Critical: 5% base / 1.5×;
- Castellan Fortress AI: Wallbound Strike 65 / Bastion Sweep 35, with Sweep repetition lock;
- Walking AI: Fortress Slam 40 / Iron Pursuit 40 / Wall-Shear Sweep 20, with Slam/Sweep repetition locks;
- equal legal single-target selection;
- Ballista: Prepare → Fire → Reload, fixed visible target, finite and destroyable;
- Watch Seal: 10% final direct-damage reduction while functional and Castellan remains Fortress-bound;
- Walking transition on the current 450-HP body once HP is 247 or lower after a completed damage package;
- Bleed/Staggered, Hit/Evasion, action order, and MP are resolved under current battle-system rules.

## Player policies tested
### Normal / smart
1. Destroy the telegraphed finite Ballista immediately.
2. Leave Watch Seal intact and push Castellan until Walking State naturally breaks the seal link.
3. Cyanis uses available Crest MP intelligently; Harmonized Crest is honored.
4. Maevra uses Linebreaker while affordable, then basic attacks.
5. Ilyra heals/cleanses from information available at round start; otherwise attacks.
6. No Items.

### Safety
Destroy Ballista, then Watch Seal, then commit to Castellan; heal/cleanse conservatively.

### Aggressive
Ignore support objects and race the 450-HP body, accepting Heavy Bolt / Bleed risk.

## 20,000-run result — mandatory Lv2
| Policy | Win rate | Mean rounds | Median | 10–90% band | Any-KO rate | Mean remaining party HP | Ballista shots | Status exposure |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Normal / smart | **100%** | **6.28** | **6** | **6–7** | **0%** | **67.8%** | **0.00** | Staggered in 14.0% of runs |
| Safety | **100%** | **7.43** | **7** | **7–8** | **0%** | **68.9%** | **0.00** | Staggered in 14.5% |
| Aggressive | **100%** | **4.98** | **5** | **5–5** | **2.23%** | **59.6%** | **1.83** | Bleed in 30.5%; Staggered in 15.9% |

## 20,000-run result — high-side Lv3
| Policy | Win rate | Mean rounds | Median | 10–90% band | Any-KO rate | Mean remaining party HP |
|---|---:|---:|---:|---:|---:|---:|
| Normal / smart | **100%** | **6.00** | **6** | **6–6** | **0%** | **67.9%** |
| Safety | **100%** | **7.02** | **7** | **7–7** | **0%** | **67.3%** |
| Aggressive | **100%** | **4.74** | **5** | **4–5** | **0.63%** | **65.4%** |

## Representative mandatory battle — normal/smart policy
The following is a representative 6-round run from the repeated distribution.

### Round 1
- Castellan: Wallbound Strike → Maevra, **44** damage.
- Ballista: Prepare Heavy Bolt → Maevra.
- Maevra: Linebreaker → Ballista, **46**.
- Cyanis: Crest Strike → Ballista, **62**.
- Ilyra: Attack → Ballista, **33**.
- Ballista destroyed before its prepared shot can resolve.

### Round 2
- Castellan: Wallbound Strike → Maevra, **44**.
- Maevra: Linebreaker → Castellan, **38** after Fortress/Seal handling.
- Cyanis: Resonant Pulse → Castellan, **47**, consuming Harmonized Crest Rank-I setup.
- Ilyra: Attack → Castellan, **27**.
- Castellan: 338 / 450 HP.

### Round 3
- Castellan: Wallbound Strike → Maevra, **44**.
- Maevra: Attack → Castellan, **32 Critical**.
- Cyanis: Attack → Castellan, **36**.
- Castellan crosses 55% threshold and tears free; Watch Seal protection ends.
- Ilyra: Attack → Castellan, **27**.
- Castellan: 243 / 450 HP, Walking State.

### Round 4
- Castellan: Fortress Slam → Ilyra, **50**.
- Party attacks: **24 + 40 + 30**.
- Castellan: 149 HP.

### Round 5
- Castellan: Iron Pursuit → Cyanis, **30**.
- Party attacks: **24 + 40 + 30**.
- Castellan: 55 HP.

### Round 6
- Castellan: Iron Pursuit → Ilyra, **41**.
- Maevra Attack **24**, Cyanis Attack **40**; Castellan defeated before Ilyra's action is needed.

End state:
- Cyanis **237 / 267 HP**, 6 MP
- Ilyra **163 / 254 HP**, 35 MP
- Maevra **135 / 267 HP**, 7 MP
- no KO; no Item use; Ballista destroyed; Watch Seal remained physically intact but lost its effect at Walking State.

## Certification read
The current encounter succeeds at its intended early-game job:
- support objects matter: ignoring them is faster but measurably riskier;
- destroying the Ballista is tactically rewarded and cancels its prepared shot as authored;
- Watch Seal matters during Fortress but does not force a separate mandatory add-clear;
- Ilyra's healing is available without being compulsory in a normal favorable run;
- the Walking transition occurs early enough to be experienced rather than skipped;
- completionist/high-side Lv3 is easier but does not erase the encounter structure;
- the current 450-HP body does **not** need another HP or Power change.

> **TRUE-BATTLE VERDICT: PASS / RETAIN.**
