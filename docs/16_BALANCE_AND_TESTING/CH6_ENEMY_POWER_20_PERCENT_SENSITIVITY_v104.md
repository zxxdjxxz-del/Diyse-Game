# Diyse — Chapter 6 Enemy Direct-Damage Power +20% Sensitivity — v104

**Status:** **WORKING SENSITIVITY / NOT OWNER CANON**  
**Parent:** `GLOBAL_ENEMY_POWER_20_PERCENT_SENSITIVITY_v104.md`  
**Purpose:** determine whether the proposed global `enemy direct-damage Power ×1.20` baseline remains fair in a faster, more status-heavy chapter and whether mandatory bosses still require local structural/offensive tuning.

This is design-layer stochastic balance testing, not runtime-engine QA.

---

# Route anchors
Current Chapter-6 progression authority:
- chapter start — Lv22 mandatory;
- Crownstorm Roc — **Lv23 mandatory / Lv25 completionist**;
- Matron Zevraya — **Lv24 mandatory / Lv27 completionist**;
- Masked Seyrik — **Lv25 mandatory / Lv27→28 completionist**;
- chapter end — Lv27 mandatory.

The core comparison continues the v103/v104 rule:
> **mandatory and completionist use the same ordinary equipment.**

No Relic/Legacy equipment advantage is given to the completionist line.

Shared ordinary reference is chapter-appropriate rather than deliberately stale:
- Cyanis — Deepforge Blade / conservative ordinary heavy armor / ordinary Shield;
- Ilyra — Crucible Wardrod / conservative ordinary Warding armor / Warding Focus;
- Torren — Storm War Bow / conservative ordinary medium armor;
- Vaelira — Arcanist Staff / conservative ordinary caster armor.

Weapon timing is current catalog authority:
- Deepforge Blade — first availability Ch5;
- Storm War Bow — first availability Ch6;
- Arcanist Staff — Ch4;
- Vaelira does not receive Veycross Battlestaff until Ch7.

The older v82 Chapter-6 validation did not own an exact armor loadout, only a conservative chapter-appropriate armor reference. This v104 study therefore does not pretend a more exact armor-source lock exists than the repository currently provides.

---

# 1. Chapter-6 ordinary roster pressure screen

Chapter 6 is a stronger test of the global scalar than Chapter 5 because many ordinary enemies are fast enough to act before slower party members.

Representative current → ×1.20 conversions:
- Weather Crown Adept — 180 Lightning / 175 Ice → **216 / 210**;
- Storm Feather — 165 / 160 Lightning / 120 AoE → **198 / 192 / 144**;
- Storm Roc Juvenile — 190 / 135 Ice AoE / 205 → **228 / 162 / 246**;
- Sky Skirmisher — 175 / 200 / 155 Lightning → **210 / 240 / 186**;
- Ruin Vanguard Reaper — 205 / 215 Ruin / 145 AoE → **246 / 258 / 174**;
- War-Sorcerer — 190 Fire / 205 Ruin / 145 AoE → **228 / 246 / 174**;
- Iron Maw — 220 / 240 / 150 AoE → **264 / 288 / 180**.

The scalar does not alter:
- their Speed;
- Stun/Freeze/Burn/Bleed/Staggered application chances;
- action count;
- formation composition;
- support actions.

Risk focus:
> cumulative opening pressure from multiple SPD35–43 enemies, not one-action deletion.

No Chapter-6 individual direct hit becomes an obvious healthy-full-HP one-shot merely from the ×1.20 scalar.

Exact whole-formation full-status distribution remains a follow-up sensitivity item because the recovered formation table was restored after the older v82 validation and should be tested as a formation layer, not inferred from single-enemy checks.

---

# 2. Crownstorm Roc

Current architecture retained for sensitivity:
- one 4,800-HP bar;
- Perched Sovereign → Stormbound at 50%;
- SPD43 before Stormbound Speed increase;
- no free transition attack;
- no HP refill.

×1.20 direct Powers:

Perched:
- Sovereign Talon — 200 → **240**;
- Crownbolt — 215 → **258**;
- Hail Scatter — 135 AoE → **162**;
- Gale Sweep — 145 AoE → **174**.

Stormbound:
- Stormbound Dive — 245 → **294**;
- Crownstorm Bolt — 255 → **306**;
- Stormglass Burst — 165 AoE → **198**;
- Gale Pressure — 170 AoE → **204**.

Status chances remain unchanged.

## Calibrated boss-isolation result
The stochastic harness was calibrated so current-Power mandatory pacing remains around the owner's established ~9–10-round normal target before comparing the scalar.

10,000-run same-gear results:

### Mandatory Lv23 — smart recovery/status-aware
Current:
- 100% wins;
- median **9** rounds;
- **0.20% any-KO**;
- 0 wipes observed.

×1.20:
- **99.98% wins**;
- median **9** rounds;
- **0.80% any-KO**;
- **0.02% wipes**.

### Mandatory Lv23 — aggressive
Current:
- 100% wins;
- **0.30% any-KO**.

×1.20:
- **99.97% wins**;
- **1.82% any-KO**;
- **0.03% wipes**.

### Completionist Lv25 — same equipment
×1.20 smart:
- 100% wins;
- median **8** rounds;
- **0.15% any-KO**;
- 0 wipes observed.

## Crownstorm verdict
> **×1.20 HELPS BUT CROWNSTORM REMAINS TOO SAFE FOR THE NEW MANDATORY-BOSS STANDARD.**

The global scalar is not the problem. The encounter simply has too little sustained punishment under competent play despite its Speed/control identity.

Keep Crownstorm flagged for local boss tuning after the global baseline decision.

---

# 3. Matron Zevraya → Perfected War Mother

Current architecture:
- Blood Matron — 4,400 HP;
- Crimson Brood same-bar state at 45%;
- Perfected War Mother — fresh 5,200 HP;
- four finite Form-I Reservoirs;
- surviving Reservoir functions can affect Form II.

×1.20 applies only to direct-damage Powers. Reservoir HP, healing values, status chances and boss stats remain unchanged.

## Structural problem exposed
The harder test reproduces the same action-density problem discovered in Deepforge.

Under the fallback selected-action logic:
- **Adaptive Plating** is a non-damaging selected action while Armor Reservoir survives;
- **Controlled Reconstruction** is a non-damaging selected action during Crimson Brood while Sustenance survives;
- **Warbody Plating** is a non-damaging selected Form-II action if Armor survives.

Therefore destroying Armor/Sustenance can remove low-pressure boss turns from the legal menu.

That can make a supposedly safer Reservoir-dismantling route more attack-dense after the party has already spent actions destroying Reservoirs.

Verdict on current architecture:
> **DO NOT CERTIFY RESERVOIR INCENTIVE UNTIL ACTION-DENSITY INVERSION IS FIXED.**

This is not caused by the ×1.20 scalar.

---

# 4. Zevraya structural sensitivity candidate

To test the intended encounter rather than the inverted menu, a non-canonical structural sensitivity was run:

### Armor branch
While Armor Reservoir survives:
> continuous functional **Defense +15% / Spirit +15%**

It does not consume Zevraya's selected action.

If Armor survives into Form II, the same functional defensive branch applies to Perfected War Mother.

### Controlled Reconstruction
If Sustenance survives into Crimson Brood:
> the existing 240-HP reconstruction becomes a bounded conditional passive trigger, still hard-capped to one use.

It does not replace a selected attack.

### Sustenance Draw / Perfected Siphon
Remain selected **damaging** actions because they already create direct pressure while healing.

### Conduction
Remains a selected damaging action.

### Brood
Remains an extra finite hostile body if its Reservoir survives.

This sensitivity does not change the authored magnitudes; it changes only whether non-damaging inherited functions dilute selected offense.

---

# 5. Zevraya ×1.20 structural-candidate results

The player-offense harness is calibrated so the current-Power Lv24 dismantling line sits around the owner's existing ~15–17-round complete-encounter duration before applying the enemy scalar.

10,000-run same-gear ×1.20 results:

| Route | Win rate | Any-KO | Wipe | Median rounds |
|---|---:|---:|---:|---:|
| **Lv24 mandatory — rush Reservoirs** | **98.79%** | **47.15%** | **1.21%** | **17** |
| **Lv24 mandatory — dismantle** | **99.44%** | **44.17%** | **0.56%** | **16** |
| **Lv27 completionist — rush, same gear** | **99.99%** | **11.14%** | **0.01%** | **14** |
| **Lv27 completionist — dismantle, same gear** | **100%** | **9.10%** | **0% observed** | **14** |

Interpretation:
1. **Mandatory temporary KOs become normal rather than exceptional.**
2. The mandatory route remains very beatable with competent play.
3. Wipes exist, especially when rushing the encounter's strategic objects.
4. Dismantling now produces a real safety benefit instead of increasing attack density.
5. Completionist progression buys a large safety margin even with identical equipment.
6. Completionist does not become completely immune to pressure; the boss still matters.

This is substantially closer to the revised Diyse boss-difficulty philosophy than the old v82 PASS state.

---

# 6. Chapter-6 read after sensitivity

Evidence so far:

### Global ×1.20
> **Still promising.**

It does not create obvious one-shot behavior in ordinary bodies and provides a useful whole-roster offense floor.

### Bosses
> **A global scalar alone is not enough.**

- Furnace Tyrant — still too safe at ×1.20.
- Crownstorm Roc — still too safe at ×1.20.
- Zevraya — can reach the desired difficulty profile at ×1.20 once her Reservoir support functions stop diluting offense.

This suggests the forward balancing model should be:
> **global enemy direct-damage floor + encounter-specific boss mechanics/action-density tuning.**

Do not solve every weak boss with another universal multiplier.

---

# Current Chapter-6 verdict

> **GLOBAL ×1.20 REMAINS VIABLE / CROWNSTORM LOCAL TUNING NEEDED / ZEVRAYA STRUCTURAL FIX PROMISING / OWNER VALUES NOT YET CHANGED**

Next:
1. run the Chapter-6 recovered ordinary formations as full formation/status distributions under ×1.20;
2. retain Crownstorm as a local-tuning flag;
3. retain the Zevraya non-diluting Reservoir candidate for later promotion decision;
4. carry ×1.20 into the Chapter-7 representative boss/dungeon layer before deciding on global canon promotion.
