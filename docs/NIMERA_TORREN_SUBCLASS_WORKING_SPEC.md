# Diyse — Nimera ← Torren Subclass Working Spec

**Status:** APPROVED CLASS-REWORK DESIGN — NOT YET MASTER-CANON PROMOTED  
**Parent trackers:** `docs/CLASS_REWORK_MASTER_TRACKER.md`, `docs/CLASS_CEXP_WORKING_MODEL.md`, `docs/CLASS_MASTERY_WORKING_MODEL.md`  
**Authority boundary:** v1.84 / Audit99 plus newer explicit class-rework decisions. On August 21, 2026 the user clarified that the class-rework proposals advanced under their repeated “Let’s continue” responses are approved. This file therefore records the latest refined Nimera ← Torren package as approved within the class-rework project. Later explicit revisions still supersede it.

## 1. Approved identity

- **Subclass name: Truthshot.**
- **Character/class pairing:** **Nimera — Cardweaver / Truthshot**.
- The old Cyanis-derived **Sixfold Knight** direction is superseded.

Nimera genuinely learns Torren's War Archer discipline rather than receiving a Face-heavy pseudo-knight kit. Her subclass uses real Great Bows and translates Torren's practical quarry logic into Nimera's analytical style.

Approved inherited War Archer language:
- target assessment;
- Hunter's Measure;
- prepared interruption;
- pinning / mobility control;
- penetration against hard targets;
- repeated-shot pressure;
- exploiting known weaknesses.

Do not create an `Appraised` status. Diysean Appraisal remains an information-reveal action. Indexed remains the separate Sovereign Index / Standard Card state.

## 2. Approved equipment progression

| Subclass CL | Equipment result |
|---:|---|
| **CL1** | Gain legal use of Torren's **Great Bow** family. Great Bows occupy Weapon + Secondary. |
| **CL3** | Gain legal use of **War Archer armor**. |
| **CL5** | No fabricated Secondary or duplicate two-hand permission. Great Bow use is already complete at CL1. |
| **CL10** | Equipment Mastery becomes eligible. Buying Subclass Mastery Node 4 grants access to the War Archer donor **Relic**. |
| Synthesis | Later paired Legacy access under the final Synthesis rule. |

## 3. Approved selected-Subclass stat package

- Attack +8%
- Accuracy +8%
- Speed +6%
- Defense -6%

This keeps Nimera clearly more martial and accurate than Cardweaver without trying to out-stat Torren at his own tradition.

## 4. Approved five normal abilities

### CL1 — Measured Shot
**120 Physical Power; 6 MP; single target.**

- Great Bow technique.
- Applies **Hunter's Measure for 2 rounds** on hit.
- Hunter's Measure is the same shared War Archer state Torren uses; there is no Nimera-only mark.
- If Diysean Appraisal has already revealed the target's permitted combat data, Measured Shot gains **+10 Base Hit**. This is a direct information check, not an `Appraised` status.

### CL4 — Held Argument
**150 Physical Power; 8 MP; prepared single-target response.**

- Arms one prepared bow response against the selected enemy.
- Fires automatically when that target begins an eligible **Interruptible** action.
- Uses the existing one-armed Prepared-effect limit shared by Abilities and Standard Cards.
- Against Hunter's Measure, gains **+10 Base Hit** and **+15 percentage points to its authored interrupt chance**.

### CL7 — Pin the Variable
**145 Physical Power; 9 MP; single target.**

- Applies **Speed Down for 2 rounds** using normal status-resolution rules.
- Against Hunter's Measure, gains **+20 percentage points to the Speed Down application chance** and **10% Defense penetration**.

### CL9 — Structural Failure
**210 Physical Power; 12 MP; single target.**

- **35% Defense penetration**.
- Gains **+15% final damage** against targetable components, devices, wards, constructs, and equivalent authored structural targets.
- Against Hunter's Measure, gains an additional **+10 Base Hit**.

### CL11 — Corroboration
**4 hits × 60 Physical Power = 240 total Power; 14 MP; one target.**

- All four hits are one Ability action and do not create extra ordinary actions.
- Against Hunter's Measure, each hit after the first gains a cumulative **+5 Base Hit** and **+5% Critical Chance** relative to the prior hit.
- Automatic hostile retargeting follows the global combat rule if the original target is defeated before resolution; once the Ability begins resolving, its authored multihit package remains one coherent action.

## 5. Approved Trait — Applied Evidence

### Rank I — CL1
Subclass attacks gain **+10 Base Hit** against enemies with Hunter's Measure.

### Rank II — CL6
Subclass attacks additionally gain **+10% Critical Chance** against enemies with Hunter's Measure.

### Rank III — CL12
Subclass attacks additionally gain **15% Defense penetration** against enemies with Hunter's Measure.

The Trait creates no personal resource, no new mark, and no Face-counting loop.

## 6. Approved Ultimate — Final Annotation

**CL13; 360 Physical Power; single target.** Ultimate cost follows the final global Ultimate convention.

- **+20 Base Hit**.
- **50% Defense penetration**.
- Gains **+20% final damage** if the target has Hunter's Measure.
- Gains **+15% final damage** against large enemies, Hunts, targetable components, devices, wards, constructs, and equivalent hard-point targets.
- Does **not** consume Hunter's Measure.

## 7. Approved Subclass Mastery nodes

| Node | Eligibility | Effect |
|---:|---:|---|
| **Subclass 1 — Exact Measure** | CL3 | Measured Shot gains +15 Power and +10 Base Hit. |
| **Subclass 2 — Prepared Proof** | CL5 | Held Argument gains +20 Power and +15 percentage points to its interrupt chance against Hunter's Measure. |
| **Subclass 3 — Hard Evidence** | CL7 | Pin the Variable gains +10 percentage points to Speed Down application; Structural Failure gains +10 Power. |
| **Subclass 4 — Equipment Mastery** | **CL10** | Unlocks legal use of the War Archer donor Relic. |

Each costs 1 MP under the inherited nine-point Mastery economy.

## 8. Approved Torren/Nimera shared interaction

Hunter's Measure is intentionally party-shared between the pair:
- Torren can exploit Measure applied by Nimera;
- Nimera can exploit Measure applied by Torren;
- neither consumes Measure by default;
- the design rewards fielding them together without requiring both in the active party.

Nimera's Base information mechanics remain useful without becoming mandatory. Diysean Appraisal can improve Measured Shot accuracy by revealing permitted target data, but Truthshot is fully functional without creating or tracking an Appraisal status.

## 9. Remaining implementation checks, not design reversals

These do not reopen the approved package; they are implementation/balance normalization work:
- normalize global interrupt-chance terminology;
- normalize global status-application terminology;
- apply the final universal Ultimate cost convention once that convention is settled;
- map the approved structural-target categories to the final engine tagging scheme;
- design the Torren/Nimera Synthesis interaction after both reciprocal subclasses are fully CL13-complete.
