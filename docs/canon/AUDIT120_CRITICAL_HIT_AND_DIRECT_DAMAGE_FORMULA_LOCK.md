# Diyse — Audit120: Critical Hit and Direct-Damage Formula Lock

**Master-canon version:** **v2.05 / Audit120**  
**Date:** August 26, 2026  
**Status:** **MASTER CANON — CONTROLLING**  
**Parent authority:** **v2.04 / Audit119** plus all compatible older locks.  
**Purpose:** Lock Diyse's Critical Hit system and correct the controlling direct-damage equation without replacing the established Attack/Defense, Magic/Spirit, Power, penetration, Hybrid, affinity, and later-modifier architecture.

Where this audit conflicts with Audit119 Section 2's direct-damage equation or any older unresolved Critical wording, **Audit120 controls**. Audit119 remains controlling for compatible Standard-Card/Prime MP, consumables, named resistance, Prime scaling/control, progression, and other domains not changed here. Audit115 remains controlling for compatible status/element/Ruin rules.

---

# 1. Controlling Physical direct-damage formula

Diyse's Physical direct-damage formula is:

> **BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)**

with:

> **EffectiveDefense = CurrentDefense × (1 - EffectiveDefensePenetration)**

Defense penetration follows the already-established Diyse same-axis rules and cap.

Important:
- do **not** replace or rewrite this Attack/Defense formula;
- Critical Hits do **not** use a separate attack formula;
- Critical Hits do **not** ignore Defense;
- penetration improves the normal damage result first, then Critical modifies that eligible resolved direct damage.

Audit119's prior `Offense × 1.50 × 150/(150+Defense)` resolver is superseded wherever it conflicts with this section.

---

# 2. Magical direct-damage formula

Eligible Magical direct damage follows the same architecture on the magical axis:

> **BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)**

with:

> **EffectiveSpirit = CurrentSpirit × (1 - EffectiveSpiritPenetration)**

Magic remains the magical/healing output stat. **Spirit** is the magical defensive stat.

No separate spell-critical multiplier exists.

---

# 3. Hybrid direct hits

For one authored Hybrid hit:

1. resolve the Attack-derived component against Defense using its authored Physical weight;
2. resolve the Magic-derived component against Spirit using its authored Magical weight;
3. apply each component's legal same-axis penetration independently;
4. combine the resulting eligible direct-damage components;
5. if that authored hit critically strikes, multiply the **combined** eligible direct damage by the Critical multiplier.

A concise component form is:

> **PhysicalComponent = PhysicalWeight × [Attack² / (Attack + EffectiveDefense)] × (Power / 100)**

> **MagicalComponent = MagicalWeight × [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)**

> **HybridNormalDirectDamage = PhysicalComponent + MagicalComponent**

Do **not** roll separate Critical Hits for the physical and magical internal portions of one single authored Hybrid hit.

Character Ability Ruin remains the compatible authored Hybrid weighting from Audit115 unless separately revised: **75% Attack / 25% Magic**.

---

# 4. Critical damage multiplier

For an eligible direct damaging hit:

> **CriticalDamage = ResolvedDirectDamage × 1.5**

Therefore:

> **CriticalMultiplier = 1.5**

A normal hit uses:

> **CriticalMultiplier = 1.0**

A Critical Hit:
- does not ignore Defense or Spirit;
- does not recalculate the attack with a separate formula;
- does not change Power;
- does not automatically change element/affinity;
- does not automatically improve harmful-status application.

---

# 5. Critical placement in the damage order

For an eligible direct hit, use this controlling order:

1. resolve the **Base Hit / Evasion** check;
2. if the hit misses, stop — no Critical roll occurs;
3. if the hit connects, resolve its Critical Chance roll;
4. establish Power and authored damage type/Hybrid weights;
5. establish current Attack/Magic and current Defense/Spirit;
6. resolve legal same-axis penetration;
7. calculate the normal Physical/Magical components;
8. combine Hybrid components when applicable;
9. if the hit critically strikes, multiply the eligible combined direct damage by **1.5**;
10. apply remaining later-stage affinity/final-damage/target-side/Guard/Barrier/interception modifiers according to the normal global damage-order rules;
11. round at the normal final-damage step.

Diyse continues to have **no universal random ±damage variance** unless a later rule explicitly adds one.

This means penetration improves the normal damage calculation first, and Critical then multiplies the resulting eligible direct damage.

---

# 6. Base Critical Chance

Every eligible direct damaging hit has:

> **BaseCriticalChance = 5%**

Critical Chance modifiers are **flat percentage-point additions**.

Examples:
- `+5% Critical Chance` means **+5 percentage points**;
- `+10% Critical Chance` means **+10 percentage points**;
- `+15% Critical Chance` means **+15 percentage points**.

Unless an effect explicitly states another operation, do not multiply Critical Chance bonuses.

Example:

> 5% base + 10 percentage points = **15% Critical Chance**

---

# 7. Ordinary Critical Chance cap

Ordinary random Critical Chance is capped at:

> **50%**

Explicitly authored overrides may still create:
- guaranteed Critical Hits;
- forced Critical Hits;
- Critical immunity;
- Critical suppression.

A guaranteed/forced Critical Hit bypasses the ordinary 50% random-chance cap because it is an authored override, not an ordinary percentage roll.

---

# 8. Base Hit before Critical

Critical Chance never improves hit chance.

Resolve:

1. Base Hit / Evasion;
2. miss → no Critical roll;
3. hit → Critical roll;
4. successful Critical roll → use the 1.5× Critical multiplier.

**Base Hit** and **Critical Chance** are separate mechanics.

`Accuracy` is not the canonical hit-stat term. Use **Base Hit** in current combat/equipment wording.

---

# 9. Multi-hit actions

Each authored direct hit normally rolls Critical Chance independently.

A four-hit action may therefore resolve as, for example:
- Hit 1 — normal
- Hit 2 — Critical
- Hit 3 — normal
- Hit 4 — Critical

Do not automatically make the entire Ability critical because one hit crits.

This is especially important for authored abilities/effects that modify Critical Chance on specific later hits.

If an individual action explicitly says the whole sequence uses one shared Critical roll, that action-specific rule overrides the default.

---

# 10. Eligible Magical direct hits

Eligible Magical direct hits use the same Critical multiplier:

> **CriticalDamage = NormalMagicalDirectDamage × 1.5**

The normal magical formula continues to use:
- Magic as offense;
- Spirit as defense;
- Spirit penetration where applicable.

No separate spell-critical damage multiplier exists unless a later audit explicitly creates one.

---

# 11. Damage that cannot Critical

Preserve existing no-Critical rules.

At minimum:
- **Burn cannot Crit**;
- **Bleed cannot Crit**;
- copied/echo damage explicitly authored as unable to Crit remains unable to Crit;
- indirect Max-HP damage does not Crit unless explicitly authored otherwise;
- healing does not Crit unless a separate healing-critical system is deliberately created later.

Critical Hits are primarily a property of eligible **direct damaging hits**.

---

# 12. Critical Hits and status application

A Critical Hit does **not** automatically improve harmful-status application.

Example:
- action has 20% Burn;
- action has 5% Critical Chance;
- the hit Crits;
- Burn still resolves using its normal application rules unless the action/equipment/other effect explicitly modifies Burn application chance.

Critical Chance and status application reliability are separate systems.

---

# 13. Worked Physical example

Attacker:
- Attack = 150
- Power = 180

Target:
- Defense = 100
- no Defense penetration

Normal Physical damage:

> 150² / (150 + 100) = 90

> 90 × 1.8 = 162

Normal hit:

> **162**

Critical Hit:

> 162 × 1.5 = **243**

---

# 14. Worked penetration example

Attacker:
- Attack = 150
- Power = 180

Target:
- Defense = 100
- Defense penetration = 50%

Effective Defense:

> 100 × (1 - 0.50) = 50

Normal Physical damage:

> 150² / (150 + 50) = 112.5

> 112.5 × 1.8 = 202.5

Normal rounded final damage is approximately:

> **203**

Critical pre-rounding result:

> 202.5 × 1.5 = 303.75

Final rounded damage:

> **304**

---

# 15. Worked Hybrid Critical example

If one authored Hybrid hit resolves to:
- Physical component = 180
- Magical component = 120

Combined normal direct damage:

> 180 + 120 = **300**

If the authored hit Crits:

> 300 × 1.5 = **450**

One Critical roll applies to the authored Hybrid hit, not separately to its two internal components.

---

# 16. Final core rule

For an eligible direct hit:

> **NormalDamage = existing Diyse direct-damage formula**

Then:

> **FinalCriticalStageDamage = NormalDamage × (1.5 if Critical; otherwise 1.0)**

Preserve Diyse's existing:
- Attack / Defense;
- Magic / Spirit;
- Power;
- same-axis penetration and cap;
- Hybrid weighting;
- affinity;
- later final-modifier architecture.

Audit120 adds/locks only the Critical system:
- **5% base Critical Chance**;
- flat percentage-point Critical Chance modifiers;
- **50% ordinary random Critical Chance cap**;
- independent per-hit rolls for multi-hit actions by default;
- **1.5× Critical Damage**;
- no Defense/Spirit bypass;
- no automatic harmful-status boost;
- no Criticals on Burn/Bleed or other explicitly excluded indirect damage.
