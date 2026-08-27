# Diyse — Audit122: Base Hit, Evasion, and Bleed Runtime Lock

**Master-canon version:** **v2.07 / Audit122**  
**Date:** August 27, 2026  
**Status:** **MASTER CANON — CONTROLLING**  
**Parent authority:** **v2.06 / Audit121** plus compatible Audit120/Audit119/Audit115 rules.  
**Purpose:** Close the remaining Base-Hit/Evasion resolver ambiguity and promote the current Bleed lifecycle, superseding stale Accuracy terminology and the old any-heal-clears-Bleed rule.

Where this audit conflicts with Audit121 or older combat documentation, **Audit122 controls for Base Hit/Evasion resolution and Bleed timing/clearing only**.

---

# 1. No natural Accuracy stat

Diyse does not use a natural character `Accuracy` stat.

Use:
- **Base Hit** as the authored action-side hit value;
- **Evasion** as the target-side avoidance value.

Any old `Accuracy` wording that means hit reliability should be normalized to **Base Hit** unless an explicitly different concept is being described.

---

# 2. Base Hit / Evasion resolver

For an action that uses the ordinary hit check:

> **AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers**

> **EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers**

> **FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)**

Resolve one ordinary hit roll against `FinalHitChance` unless the action explicitly uses another authored hit rule.

The clamp is:
- minimum **5%**;
- maximum **100%**.

Explicit guaranteed-hit, forced-miss, immunity, or scripted overrides may bypass the ordinary clamp where directly authored.

---

# 3. Base Hit authoring bands

Use these as normal authoring targets, not automatic category hard-codes:

- standard reliable actions: about **100 Base Hit**;
- intentionally heavy / less reliable actions: about **90–95**;
- precision actions: about **105–115**;
- exceptional precision may reach about **120** where justified.

An action's exact authored Base Hit controls over the category guideline.

---

# 4. Hit/Evasion is separate from harmful-status application

A successful hit does not automatically guarantee an authored harmful status.

Resolve:
1. hit/evasion legality and hit roll;
2. direct damage / other hit-dependent resolution;
3. harmful-status application under its own authored chance and resistance rules.

Critical Chance is also separate:
- miss → no Critical roll;
- hit → Critical roll if eligible;
- a Critical does not automatically improve harmful-status application.

Audit120's compatible Critical rules remain active.

---

# 5. Bleed — current timing

**Bleed is the most common physical harmful status.**

Current Bleed damage cadence:

> **Bleed deals its authored Bleed damage each round and again when the affected character acts.**

The old Audit115 rule limiting Bleed to one proc per round is superseded.

Do not suppress an action-triggered Bleed proc merely because the round-based Bleed tick already occurred.

If an effect grants more than one actual action, each qualifying action follows the current Bleed-on-action rule unless that effect explicitly says otherwise.

Bleed damage remains indirect status damage:
- it does not Crit;
- it does not use Defense/Spirit;
- it may KO unless a specific encounter rule says otherwise.

---

# 6. Bleed — current clearing

Bleed does **not** disappear because the target receives an ordinary partial heal or Regen tick.

Bleed clears only through an eligible current clearing route:

1. **the affected unit is restored to full HP**;
2. an eligible **harmful-status clear** removes Bleed;
3. an eligible **item** removes Bleed.

Therefore the older rule:

> `any successful HP heal restoring at least 1 HP removes Bleed`

is superseded.

Likewise, ordinary Regen restoring HP does not clear Bleed unless that restoration reaches full HP or the Regen effect explicitly includes a valid status clear.

---

# 7. Staggered terminology interaction

Staggered remains an ordinary harmful status, not a global Break/Stagger meter.

Where older Staggered text says `Accuracy -X%`, interpret that current hit-side penalty as a **Base Hit percentage modifier** under the resolver in this audit.

Do not create an Accuracy stat to preserve the old label.

---

# 8. Implementation verdict

Audit122 closes the Base Hit/Evasion formula as implementation-ready and updates Bleed runtime behavior.

Do not leave the hit/evasion resolver marked OPEN in implementation documentation.

Do not implement the old any-heal-clears-Bleed lifecycle or old one-Bleed-proc-per-round restriction.
