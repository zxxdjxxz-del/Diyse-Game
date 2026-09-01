# Chapter 5 — Deepforge Colossus Assembly / Offense Tuning Candidate — v103

**Status:** **WORKING CANDIDATE / NOT OWNER CANON**  
**Parent study:** `CH5_DEEPFORGE_DIFFICULTY_RECALIBRATION_WORKING_v103.md`

## Why this candidate exists
The first harder same-gear test showed that simply raising all direct-damage Powers by ~45% can produce a good mandatory-vs-completionist KO separation, but it does not solve the encounter's assembly-action-density problem.

Current Guard Press and Repair Arm add non-damaging selected boss actions. Destroying those assemblies can therefore remove low-pressure turns and leave a more attack-dense action menu after the player has already spent turns dismantling parts.

A better design is to make surviving assemblies strengthen the body **without consuming its ordinary selected action**.

---

# Preferred structural candidate

## Guard Press
Replace selected **Reinforce Chassis / Reinforced Load** action-menu use with a continuous functional effect:

While Guard Press remains functional:
> **Defense +15% / Spirit +15%**

- applies to the current Assembly Frame while the assembly exists;
- if Guard Press survives transformation, applies to Worldsmith Body;
- destroying Guard Press removes/prevents this functional bonus;
- this is a functional assembly modifier, not Barrier/Brace and not an extra action.

## Repair Arm
Replace selected **Field Repair / Self-Stabilize** action-menu use with a conditional passive repair trigger.

After the boss completes its selected action, if:
- Repair Arm is functional;
- core HP is at or below **55% Max HP**;
- repair uses remain;
- the repair trigger is not inside its 2-boss-turn repetition lock;

then restore:
- Assembly Frame — **220 HP**;
- Worldsmith Body — **250 HP**.

Hard cap remains:
> **2 successful repairs per form**

After a repair triggers:
> **2 boss-turn repetition lock**

This trigger does not add another selected action and cannot restore an assembly.

## Command Loom
Retain the current passive function:
- +10 Base Hit to damaging selected actions;
- Forge Collapse Base Hit 90 → 100 while the Loom survives.

---

# Preferred offensive candidate

With the assembly functions no longer diluting the attack menu, a much smaller direct-Power increase is sufficient.

Working rounded package: approximately **+15%**.

## Form I
- Construction Hammer — **205 → 235**
- Load-Bearing Sweep — **140 → 160**
- Forge Discharge — **195 → 225**
- Clamp and Draw — **170 → 195**

## Form II
- Worldsmith Clamp — **225 → 260**
- Foundry Arc — **215 → 245**
- Construction Sweep — **155 → 180**
- Worldline Crush — **260 → 300**
- Forge Collapse — **300 → 345**

No proposed change in this candidate to:
- boss HP;
- raw ATK/MAG/DEF/Spirit/SPD;
- status chances;
- repetition locks;
- fresh-body architecture;
- assembly HP;
- Prime persistence.

---

# Same-gear 20,000-run sensitivity

Core party/equipment/consumables are identical to the parent v103 study.

## Mandatory Lv20 — rush Assembly Frame
All three functions survive into Worldsmith.

Results:
- wins — **96.665%**;
- wipe incidence — **3.335%**;
- any temporary KO — **37.37%**;
- mean ending combined HP — ~**39.1%**.

This creates real danger without making the mandatory route structurally blocked.

## Mandatory Lv20 — dismantle all three assemblies
Results:
- wins — **99.87%**;
- wipe incidence — **0.13%**;
- any temporary KO — **14.165%**;
- mean ending combined HP — ~**52.1%**.

This is the intended tactical payoff:
> spending actions dismantling the Frame buys a substantially safer Worldsmith fight.

The safer route is not free because the party must still spend Form-I actions on 900 total assembly HP.

## Completionist Lv22 — same equipment — rush
Results:
- wins — **100%**;
- any temporary KO — **0.58%**;
- no wipes observed in the 20,000-run sample;
- mean ending combined HP — ~**62.6%**.

## Completionist Lv22 — same equipment — dismantle all
Results:
- wins — **100%**;
- any temporary KO — **0.315%**;
- no wipes observed;
- mean ending combined HP — ~**63.8%**.

---

# Design read
This candidate produces three desired separations simultaneously:

1. **Mandatory vs completionist:**
   - same equipment;
   - Lv20 mandatory rush sees KOs in ~37% of runs;
   - Lv22 completionist rush sees KOs in well under 1%.

2. **Rush vs dismantle:**
   - mandatory rush is meaningfully more dangerous;
   - mandatory dismantle cuts KO incidence from ~37% to ~14% and wipe incidence from ~3.3% to ~0.1%.

3. **Danger without one-shot design:**
   - no new instant-kill mechanic;
   - no Barrier/Brace/Break meter;
   - Forge Collapse remains telegraphed and Defend remains useful;
   - danger comes from sustained attack density, status pressure, and the player's decision to preserve or dismantle functional assemblies.

## Important caution
Round-count results in the design-layer simulation are highly policy-sensitive because defensive play, MP restoration, and assembly targeting consume ordinary turns. Do not use those round counts alone to set HP.

The key evidence here is relative KO/wipe/resource behavior.

---

# Candidate verdict
> **PROMISING / NOT YET LOCKED**

This is currently preferred over the earlier brute-force ~45% Power-only sensitivity because it fixes the assembly incentive and requires only a modest offensive increase.

Next step if approved:
1. promote the assembly-function rewrite and rounded +15% Power package into the Deepforge owner;
2. run full no-Prime and same Recovered Last Sentinel certification lines;
3. use the resulting Chapter-5 profile to set the forward boss-difficulty ramp.
