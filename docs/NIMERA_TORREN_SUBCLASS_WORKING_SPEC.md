# Diyse — Nimera ← Torren Subclass Working Spec

**Status:** ACTIVE WORKING DESIGN — NOT MASTER CANON  
**Parent trackers:** `docs/CLASS_REWORK_MASTER_TRACKER.md`, `docs/CLASS_CEXP_WORKING_MODEL.md`, `docs/CLASS_MASTERY_WORKING_MODEL.md`  
**Authority boundary:** v1.84 / Audit99 plus newer explicit class-rework decisions. This file replaces the old Cyanis-derived Sixfold Knight direction for Nimera only as a working redesign; final names and exact numbers remain subject to approval.

## 1. Design identity

Nimera genuinely learns Torren's War Archer discipline rather than receiving a Face-heavy pseudo-knight kit. Her subclass uses real Great Bows and translates Torren's practical quarry logic into Nimera's analytical style.

Core inherited War Archer language:
- target assessment;
- Hunter's Measure;
- prepared interruption;
- pinning / mobility control;
- penetration against hard targets;
- repeated-shot pressure;
- exploiting known weaknesses.

Do not create an `Appraised` status. Diysean Appraisal remains an information-reveal action. Indexed remains the separate Sovereign Index / Standard Card state.

## 2. Equipment progression

| Subclass CL | Equipment result |
|---:|---|
| **CL1** | Gain legal use of Torren's **Great Bow** family. Great Bows occupy Weapon + Secondary. |
| **CL3** | Gain legal use of **War Archer armor**. |
| **CL5** | No fabricated Secondary or duplicate two-hand permission. Great Bow use is already complete at CL1. Subclass Mastery Node 2 may become eligible here under the working Mastery model. |
| **CL10** | Equipment Mastery becomes eligible. Buying Subclass Mastery Node 4 grants access to the War Archer donor **Relic**. |
| Synthesis | Later paired Legacy access under the final Synthesis rule. |

## 3. Working selected-Subclass stat package

- Attack +8%
- Accuracy +8%
- Speed +6%
- Defense -6%

This keeps Nimera clearly more martial and accurate than Cardweaver without trying to out-stat Torren at his own tradition.

## 4. Five normal abilities

### CL1 — Measured Shot
**Working numbers:** 120 Physical Power; 6 MP; single target.

- Great Bow technique.
- Applies **Hunter's Measure for 2 rounds** on hit.
- Hunter's Measure is the same shared War Archer state Torren uses; there is no Nimera-only mark.
- If Diysean Appraisal has already revealed the target's permitted combat data, Measured Shot gains **+10 Base Hit**. This is a direct information check, not an `Appraised` status.

Purpose: immediately lets Nimera participate in Torren's quarry language and lets either character set up the other.

### CL4 — Held Argument
**Working numbers:** 150 Physical Power; 8 MP; prepared single-target response.

- Arms one prepared bow response against the selected enemy.
- Fires automatically when that target begins an eligible **Interruptible** action.
- Uses the existing one-armed Prepared-effect limit shared by Abilities and Standard Cards.
- Against Hunter's Measure, gains **+10 Base Hit** and **+15 percentage points to its authored interrupt chance**.

Purpose: Nimera learns Torren's Watchful Aim logic but expresses it as a deliberate, evidence-based counterargument rather than raw instinct.

### CL7 — Pin the Variable
**Working numbers:** 145 Physical Power; 9 MP; single target.

- Applies **Speed Down for 2 rounds** using the normal status-resolution rules.
- Against Hunter's Measure, gains **+20 percentage points to the Speed Down application chance** and **10% Defense penetration**.

Purpose: direct descendant of Torren's pinning/control language; creates positional tempo without introducing movement or a new gauge.

### CL9 — Structural Failure
**Working numbers:** 210 Physical Power; 12 MP; single target.

- **35% Defense penetration**.
- Gains **+15% final damage** against targetable components, devices, wards, constructs, and equivalent authored structural targets.
- Against Hunter's Measure, gains an additional **+10 Base Hit**.

Purpose: Nimera stops merely identifying weak structure and starts shooting through it.

### CL11 — Corroboration
**Working numbers:** 4 hits × 60 Physical Power = 240 total Power; 14 MP; one target.

- All four hits are one Ability action and do not create extra ordinary actions.
- Against Hunter's Measure, each hit after the first gains a cumulative **+5 Base Hit** and **+5% Critical Chance** relative to the prior hit.
- Automatic hostile retargeting follows the global combat rule if the original target is defeated before resolution; once the Ability begins resolving, its authored multihit package stays coherent with the resolver's normal target handling.

Purpose: Torren's repeated-shot pressure translated into Nimera's habit of confirming a conclusion through accumulating evidence.

## 5. Trait — Applied Evidence

### Rank I — CL1
Subclass attacks gain **+10 Base Hit** against enemies with Hunter's Measure.

### Rank II — CL6
Subclass attacks additionally gain **+10% Critical Chance** against enemies with Hunter's Measure.

### Rank III — CL12
Subclass attacks additionally gain **15% Defense penetration** against enemies with Hunter's Measure.

The Trait creates no personal resource, no new mark, and no Face-counting loop.

## 6. Ultimate — Final Annotation

**CL13. Working numbers:** 360 Physical Power; single target; Ultimate cost follows the final global Ultimate convention.

- **+20 Base Hit**.
- **50% Defense penetration**.
- Gains **+20% final damage** if the target has Hunter's Measure.
- Gains **+15% final damage** against large enemies, Hunts, targetable components, devices, wards, constructs, and equivalent hard-point targets.
- Does **not** consume Hunter's Measure.

Purpose: the conclusion of Torren's lesson — assess the target, choose the exact point that matters, and end the argument with one decisive shot.

## 7. Subclass Mastery nodes — working redesign

These replace the old Sixfold Knight Subclass Mastery effects for Nimera.

| Node | Eligibility | Working effect |
|---:|---:|---|
| **Subclass 1 — Exact Measure** | CL3 | Measured Shot gains +15 Power and +10 Base Hit. |
| **Subclass 2 — Prepared Proof** | CL5 | Held Argument gains +20 Power and +15 percentage points to its interrupt chance against Hunter's Measure. |
| **Subclass 3 — Hard Evidence** | CL7 | Pin the Variable gains +10 percentage points to Speed Down application; Structural Failure gains +10 Power. |
| **Subclass 4 — Equipment Mastery** | **CL10** | Unlocks legal use of the War Archer donor Relic. |

Each costs 1 MP under the inherited nine-point Mastery economy.

## 8. Shared Torren/Nimera interaction

Hunter's Measure is intentionally party-shared between the pair:
- Torren can exploit Measure applied by Nimera;
- Nimera can exploit Measure applied by Torren;
- neither consumes Measure by default;
- the design should reward fielding them together without requiring them to be paired in the active party.

Nimera's Base information mechanics remain useful without becoming mandatory. Diysean Appraisal can improve Measured Shot accuracy by revealing permitted target data, but the Archer subclass is fully functional without creating or tracking an Appraisal status.

## 9. Name status

No final Subclass name is master-canon locked yet.

**Leading working name: `Truthshot`.**

The name is intended to read as Nimera-specific rather than as a generic precision-archer label: she gathers information, rejects bad assumptions, identifies what is actually true about the target, and turns that conclusion into the shot. `Trueshot`, `Proof Archer`, `Pattern Archer`, and `Threadshot` remain earlier non-canon alternatives unless explicitly restored.

## 10. Open balance checks before promotion

- Compare the proposed Power / MP values directly against the final Torren War Archer numbers so Nimera learns the tradition without simply surpassing its originator.
- Confirm exact global interrupt-chance terminology and status-chance terminology.
- Confirm Ultimate MP/cost convention before assigning a number to Final Annotation.
- Confirm whether structural-target bonus categories need one shared engine tag rather than several authored flags.
- Design Nimera's Synthesis passive only after the full reciprocal subclass set is stable.
