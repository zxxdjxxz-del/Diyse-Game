# Chapter 5 — Deepforge Colossus Assembly / Offense Tuning Candidate — v103

**Status:** **WORKING STRUCTURAL CANDIDATE / +15% RESULTS RETAINED / v104 +20% RETEST NEXT**  
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

# Historical v103 offensive candidate

With the assembly functions no longer diluting the attack menu, a much smaller direct-Power increase was sufficient than the rejected +45% brute-force pass.

The first structural test used approximately **+15%**.

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

No change was tested to:
- boss HP;
- raw ATK/MAG/DEF/Spirit/SPD;
- status chances;
- repetition locks;
- fresh-body architecture;
- assembly HP;
- Prime persistence.

---

# Same-gear 20,000-run v103 +15% sensitivity

Core party/equipment/consumables are identical to the parent v103 study.

## Mandatory Lv20 — rush Assembly Frame
All three functions survive into Worldsmith.

Results:
- wins — **96.665%**;
- wipe incidence — **3.335%**;
- any temporary KO — **37.37%**;
- mean ending combined HP — ~**39.1%**.

## Mandatory Lv20 — dismantle all three assemblies
Results:
- wins — **99.87%**;
- wipe incidence — **0.13%**;
- any temporary KO — **14.165%**;
- mean ending combined HP — ~**52.1%**.

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

# Design read from v103
This structural candidate produced three desired separations simultaneously:

1. **Mandatory vs completionist:** same equipment, but optional Player Level/CEXP produced a very large safety gain.
2. **Rush vs dismantle:** dismantling significantly reduced mandatory-route KO/wipe pressure.
3. **Danger without one-shots:** pressure came from sustained attack density and mechanics rather than a new instant-kill system.


Historical note: later global-scalar sensitivity work was exploratory and has been removed from the live balance tree. Git history preserves that experiment if provenance is ever needed.
