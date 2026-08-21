# Diyse — Ilyra ← Seyrik Subclass Working Spec

**Status:** APPROVED CLASS-REWORK DESIGN — NOT YET MASTER CANON  
**Parent trackers:** `docs/CLASS_REWORK_MASTER_TRACKER.md`, `docs/CLASS_CEXP_WORKING_MODEL.md`, `docs/CLASS_MASTERY_WORKING_MODEL.md`  
**Authority boundary:** v1.84 / Audit99 plus newer explicit class-rework decisions. On August 21, 2026 the user explicitly approved the class-rework proposals previously advanced under “Let’s continue.” Where an older provisional draft conflicts with a later refinement, the latest refinement below controls.

## 1. Approved identity

- **Subclass name: Vowblade.**
- **Character/class pairing:** **Ilyra — Blue Warden / Vowblade**.
- Vowblade is Ilyra learning Seyrik's Ruin Vanguard survival/offense discipline while retaining her own vow-and-mercy philosophy.
- The subclass's core thesis is: **Ilyra saves people by continuing to fight and by turning violent momentum back into survival.**
- Vowblade is not a second Ruin Vanguard and does not use self-damage, execute mechanics, a personal gauge, or a new bespoke status.

## 2. Approved equipment progression

| Subclass CL | Equipment result |
|---:|---|
| **CL1** | Gain legal use of Seyrik's **Two-Handed Sword** family; it occupies Weapon + Secondary. |
| **CL3** | Gain legal use of **Ruin Vanguard armor**. |
| **CL5** | No fabricated equipment reward; Seyrik has no honest additional ordinary Secondary family to pass here. |
| **CL10** | Equipment Mastery becomes eligible; purchasing it unlocks the Ruin Vanguard donor **Relic**. |
| Synthesis | Later paired Legacy access under the final Synthesis rule. |

Ilyra's already-unlocked Wardrod, Focus, and Shield permissions remain legal under open equipment.

## 3. Approved selected-Subclass stat package

- **HP +8%**
- **Attack +10%**
- **Spirit +8%**
- **Defense -6%**

The old `Magic -6%` drawback is superseded. Vowblade trades physical safety for stronger offensive/sustain pressure rather than receiving a mostly irrelevant Magic penalty.

## 4. Approved damage and weapon rules

### Hybrid formula
All damaging Vowblade abilities use their authored **50% Attack / 50% Spirit Hybrid** formula unless an ability explicitly says otherwise.

This formula belongs to the abilities themselves, not to the selected-subclass Trait, so unlocked Vowblade abilities retain their authored formula when used under the game's persistent-ability rules.

### Weapon legality
All damaging Vowblade abilities are legal with either:
- Ilyra's native **Wardrod**; or
- Seyrik's learned **Two-Handed Sword**.

The weapon changes build expression and animation, not the authored damage formula or Power.

Legal practical expressions include:
- Two-Handed Sword → aggressive drain-bruiser emphasis;
- Wardrod + Shield → defensive Vowblade;
- Wardrod + Focus → Spirit/support-heavy Vowblade;
- Wardrod alone → legal but less specialized.

Two-Handed Sword versions receive no hidden Power bonus merely for using the donor weapon; equipment stats and Secondary-slot opportunity cost already provide the tradeoff.

### Damage identity
Vowblade does **not** create a separate Ruin damage element. Its damaging abilities are neutral Hybrid attacks unless an ability explicitly establishes another damage property.

Ruin may appear as provenance/visual language and may use an existing Ruin-technique tag only if an established combat interaction actually consumes that tag. Do not invent a tag solely for symmetry.

## 5. Approved Trait — Mercy in Steel

### Rank I — CL1
Vowblade direct damage restores Ilyra for **10% of eligible HP damage dealt**.

### Rank II — CL6
While Ilyra is below **50% HP**, her Vowblade direct damage gains **+15% final damage**.

### Rank III — CL12
When **Mercy in Steel Rank I's own healing** would restore Ilyra above maximum HP, **50% of that excess Rank-I healing** is instead restored to the conscious ally with the lowest HP percentage.

- This overflow transfer cannot revive.
- It does not create a barrier.
- It does not chain or bounce repeatedly.
- It does **not** redirect overflow from Vital Edge, Living Covenant, Mercy's Final Edge, or other authored healing sources.

## 6. Approved five normal abilities

### CL1 — Vital Edge
**8 MP · one enemy · 185 Hybrid Power · 50% Attack / 50% Spirit**

After damage, restore Ilyra for **15% of eligible HP damage dealt**.

This authored heal is separate from Mercy in Steel Rank I and Living Covenant.

### CL4 — Mercy Returned
**10 MP · one enemy · 215 Hybrid Power · 50% Attack / 50% Spirit**

After damage, heal the conscious ally other than Ilyra with the lowest HP percentage for:

**12% target Max HP + 0.90 × Ilyra's Spirit**.

Mercy Returned remains the subclass's dedicated offensive-heal button.

### CL7 — Living Covenant
**18 MP · self stance · 3 rounds**

While active:
- Vowblade direct damage restores Ilyra for an additional **10% of eligible HP damage dealt**;
- Ilyra gains **Major interruption resistance**.

Living Covenant works with any legal equipment setup and is not a damaging action.

### CL9 — Vowkeeper's Reprisal
**12 MP · one enemy · 235 Hybrid Power · 50% Attack / 50% Spirit**

If the target damaged another ally during the previous round:
- gains **+20% final damage**;
- after damage, heals that harmed ally for **10% target Max HP + 0.75 × Ilyra's Spirit**.

If more than one ally qualifies, final deterministic target-selection wording remains an implementation detail to be resolved without changing the approved ability identity or numbers.

### CL11 — Vow of Severance
**15 MP · one enemy · 250 Hybrid Power · 50% Attack / 50% Spirit · 30% penetration**

- The Hybrid attack applies **30% penetration against its applicable Defense/Spirit components**.
- After damage, applies **Minor Defense Down + Minor Spirit Down for 2 rounds**.
- No separate authored healing rider.
- No self-damage, execute, or bespoke Ruin status.

This is the late-game defense-breaking expression of what Ilyra learns from Seyrik's Fracturing/Unmaking side of Ruin Vanguard.

## 7. Approved Ultimate — Mercy's Final Edge

**One enemy · 520 Hybrid Power · 50% Attack / 50% Spirit · 40% penetration**

Resolution order:
1. deal damage;
2. restore Ilyra for **30% of eligible HP damage dealt**;
3. heal all other conscious allies for **10% Max HP + 0.75 × Ilyra's Spirit**;
4. all conscious allies gain **15% direct-damage reduction through the end of the following round**.

Additional boundaries:
- no revive;
- no barrier;
- no cleanse;
- no self-damage;
- no execute;
- does not apply Defense/Spirit Down.

Approved selected-Vowblade interactions:
- Mercy in Steel Rank I healing applies normally in addition to the Ultimate's authored 30% self-heal;
- Mercy in Steel Rank II's +15% final damage applies if Ilyra begins the action below 50% HP;
- Mercy in Steel Rank III may redirect only overflow generated by Rank I itself;
- Living Covenant, if already active, may provide its normal additional damage-based healing.

Mercy's Final Edge remains intentionally different from Blue Warden's Dawn Without End: it is a decisive single-target strike that stabilizes the party through successful offense, not Ilyra's strongest emergency-recovery/revival tool.

## 8. Approved sustain totals / balance rule

With unmastered Living Covenant active:
- ordinary damaging Vowblade ability: **20%** damage-derived self-healing from Mercy in Steel Rank I + Living Covenant;
- Vital Edge: **35%** total damage-derived self-healing before any other effect.

With mastered Living Covenant active:
- ordinary damaging Vowblade ability: **25%** damage-derived self-healing;
- Vital Edge: **40%** total damage-derived self-healing.

Mercy's Final Edge adds its separate authored 30% self-heal and is intentionally allowed to reach Ultimate-level recovery.

## 9. Approved Subclass Mastery nodes

Each costs 1 MP under the inherited nine-point Mastery economy.

| Node | Eligibility | Approved effect |
|---:|---:|---|
| **Subclass 1 — Steeled Mercy** | CL3 | **Vital Edge +15 Power**; if Ilyra begins the action below 50% HP, **+10 Base Hit**. |
| **Subclass 2 — Mercy Carried** | CL5 | **Mercy Returned +15 Power**; its authored ally heal increases **12% Max HP → 15% Max HP** while the **0.90 × Spirit** term stays unchanged. |
| **Subclass 3 — Unbroken Covenant** | CL7 | Living Covenant's additional damage-based healing increases **10% → 15%**; **Vowkeeper's Reprisal +15 Power**. |
| **Subclass 4 — Equipment Mastery** | **CL10** | Unlocks legal use of the Ruin Vanguard donor **Relic**. |

Mastery does not directly modify Vow of Severance or Mercy's Final Edge; those late abilities arrive complete.

## 10. Approved naming set

- Subclass: **Vowblade**
- Trait: **Mercy in Steel**
- CL1: **Vital Edge**
- CL4: **Mercy Returned**
- CL7: **Living Covenant**
- CL9: **Vowkeeper's Reprisal**
- CL11: **Vow of Severance**
- CL13: **Mercy's Final Edge**
- Mastery 1: **Steeled Mercy**
- Mastery 2: **Mercy Carried**
- Mastery 3: **Unbroken Covenant**
- Mastery 4: **Equipment Mastery**

Superseded labels include `Living Edge`, `Vowguard Reprisal`, and the earlier `Severing Vow` wording.

## 11. Approved HD-2D animation / VFX architecture

Do not double production cost by creating a bespoke body animation for every Wardrod and Two-Handed Sword version. Use reusable animation families plus ability-specific VFX, timing, camera treatment, and follow-through.

| Animation family | Abilities | Wardrod expression | Two-Handed Sword expression |
|---|---|---|---|
| **Driving Strike** | Vital Edge, Mercy Returned | forward step + sweeping Wardrod cut / manifested edge | compact diagonal heavy slash |
| **Committed Strike** | Vowkeeper's Reprisal, Vow of Severance | two-handed Wardrod drive with manifested edge | full-body planted sword strike |
| **Invocation** | Living Covenant | Wardrod planted/raised | sword lowered or grounded into stance |
| **Ultimate** | Mercy's Final Edge | unique authored sequence using Wardrod expression | same premium sequence with sword-specific attack poses |

### Visual language
- Ilyra's native Grace remains **blue-white, controlled, protective**.
- Seyrik's influence appears as a restrained **violet / purple-black Ruin fracture** through the offensive portion of the technique.
- Do not use Black Host corruption language or imply Ilyra is being corrupted.
- Strongest recurring visual thesis: **Seyrik's influence appears in the attack; Ilyra's identity appears in what she does with the aftermath.**

Ability-specific direction:
- **Vital Edge:** quick blue-white strike with thin violet fracture; a restrained vitality strand returns to Ilyra.
- **Mercy Returned:** same economical strike family, but the post-hit recovery arcs toward the wounded ally.
- **Living Covenant:** blue-white vow mark beneath Ilyra with restrained violet lines; it may fracture and reseal when offensive healing triggers.
- **Vowkeeper's Reprisal:** stronger violet trailing edge and a visible connection to the ally who was harmed, followed by the healing return.
- **Vow of Severance:** the strongest normal-skill Ruin visual; a violet fracture opens through the target's defensive aura and blue-white lines lock across the break.
- **Mercy's Final Edge:** premium three-beat presentation — **Vow → Edge → Mercy** — ending with blue-white recovery bursting from Ilyra across the party.

## 12. Remaining open work

The Vowblade package above is approved at the class-rework level. Remaining work is downstream implementation/promotion work:
- deterministic tie wording for Vowkeeper's Reprisal if multiple allies were harmed by the same target;
- final runtime data implementation and regression tests;
- final production weapon-stat balance;
- Ilyra/Seyrik Synthesis and paired Legacy resolution;
- later promotion into the appropriate master-canon audit when the whole class-rework package is ready.
