# Audit100 — Reciprocal Class, Synthesis, and Legacy Architecture Lock

**Authority:** Diyse: HD-2D JRPG Clean Active Complete Master Canon **v1.85 / Audit100**  
**Date:** August 22, 2026  
**Status:** **LOCKED / CONTROLLING** for the reciprocal class-rework architecture, Sixfold Volition subclass system, CL13 class progression, weapon-independent Ability legality, all six approved Subclasses, all six Synthesis effects, all three Synthesis-resolution story beats, and all six Legacy mappings/acquisition rules defined below.

Audit100 inherits all compatible v1.84/Audit99 and earlier canon unless explicitly superseded or clarified below.

## 0. Authority contract

Audit100 promotes the completed class-rework material developed after Audit99 into master canon.

It does **not** alter:
- Audit98/Audit99 character-level EXP math or random-encounter architecture;
- the world map or regional geography;
- chapter macro-story structure outside the specific late-Chapter-11 resolution beats and Chapter-12 Legacy pickup presentation locked here;
- the permanent six-character roster;
- the four-active-member battle-party limit;
- the universal player level cap of 60;
- existing Card/Prime architecture except where a class/Synthesis rule below explicitly references it.

Where an incorporated class-rework working document still carries an older header such as **NOT YET MASTER-CANON PROMOTED**, that status line is superseded by Audit100. The detailed approved mechanics in the incorporated documents are promoted unless Audit100 explicitly leaves an item open.

## 1. Incorporated detailed authorities

Audit100 incorporates the following approved detailed design files as subordinate master-canon authorities for exact mechanics, formulas, timing, stat packages, VFX boundaries, and pair-specific implementation details:

### Subclass specifications
- `docs/CYANIS_VAELIRA_SUBCLASS_WORKING_SPEC.md`
- `docs/VAELIRA_CYANIS_SUBCLASS_WORKING_SPEC.md`
- `docs/ILYRA_SEYRIK_SUBCLASS_WORKING_SPEC.md`
- `docs/SEYRIK_ILYRA_SUBCLASS_WORKING_SPEC.md`
- `docs/TORREN_NIMERA_SUBCLASS_WORKING_SPEC.md`
- `docs/NIMERA_TORREN_SUBCLASS_WORKING_SPEC.md`

### Cross-class / Synthesis authorities
- `docs/CLASS_REWORK_CROSS_BALANCE_AUDIT_2026-08-21.md`
- `docs/CLASS_SYNTHESIS_WORKING_MODEL.md`
- `docs/CLASS_SYNTHESIS_CROSS_BALANCE_AUDIT_2026-08-21.md`
- `docs/CYANIS_VAELIRA_SYNTHESIS_WORKING_SPEC.md`
- `docs/ILYRA_SEYRIK_SYNTHESIS_WORKING_SPEC.md`
- `docs/TORREN_NIMERA_SYNTHESIS_WORKING_SPEC.md`

### Legacy authorities
- `docs/CYANIS_VAELIRA_LEGACY_WORKING_SPEC.md`
- `docs/ILYRA_SEYRIK_LEGACY_WORKING_SPEC.md`
- `docs/TORREN_NIMERA_LEGACY_WORKING_SPEC.md`

### Supporting implementation-facing rules
- `docs/COMBAT_RULES.md` for the approved no-Ability-weapon-requirement rule and compatible combat semantics.

If one of these subordinate files conflicts with Audit100, **Audit100 controls**.

## 2. Sixfold Volition — formal terminology and function

The former **Sixfold Accord** terminology is superseded.

The formal event/system name is **The Sixfold Volition**.

Locked function:
- no permanent character has or uses a Subclass before the Sixfold Volition;
- all six Subclasses unlock at the Sixfold Volition;
- afterward, the six permanent characters cross-train through three reciprocal pairs;
- the training relationships are reciprocal rather than a one-way donor ring.

Reciprocal pairs are exactly:
- **Cyanis ⇄ Vaelira**
- **Ilyra ⇄ Seyrik**
- **Torren ⇄ Nimera**

## 3. Class-level architecture — locked

### 3.1 Caps
- Base Class cap = **CL13**.
- Subclass cap = **CL13**.
- Base and Subclass CEXP are separate.
- CEXP goes only to the currently selected class.
- All recruited permanent characters receive full CEXP to their selected class whether active or reserve.
- Unrecruited characters receive no CEXP.
- Guests follow their own authored rules.

### 3.2 Class thresholds
Cumulative CEXP thresholds are locked as:
- CL1 = 0
- CL2 = 150
- CL3 = 350
- CL4 = 600
- CL5 = 950
- CL6 = 1,350
- CL7 = 1,800
- CL8 = 2,300
- CL9 = 2,850
- CL10 = 3,450
- CL11 = 4,150
- CL12 = 4,950
- CL13 = 6,000

The retired 4,800-CEXP CL12 model must not return.

### 3.3 Base Class unlock structure
The approved Base CL13 structure is:
- CL1: Trait Rank I + Base Abilities 1–3 + starting equipment permissions;
- CL3: Base Ability 4;
- CL5: native advanced-equipment permission where the tradition has an honest one;
- CL6: Base Ability 5 + Trait Rank II;
- CL9: Base Ability 6;
- CL12: Trait Rank III;
- CL13: Base Ultimate.

Do not invent a fake CL5 equipment breakthrough merely for symmetry.

### 3.4 Subclass unlock structure
The approved Subclass CL13 structure is:
- CL1: donor basic Primary access + Trait Rank I + Ability 1;
- CL3: donor Armor access;
- CL4: Ability 2;
- CL5: donor native advanced-equipment / Secondary permission where that tradition genuinely has one;
- CL6: Trait Rank II;
- CL7: Ability 3;
- CL9: Ability 4;
- CL10: Equipment Mastery eligibility;
- CL11: Ability 5;
- CL12: Trait Rank III;
- CL13: Ultimate.

A fresh Subclass begins at **CL1 with 0 CEXP toward CL2**.

## 4. Open-equipment and persistent-Ability rule — reconfirmed

Once equipment access or an Ability is legally unlocked, it remains available regardless of currently selected Base/Subclass unless an explicit global rule says otherwise.

Selected class controls:
- that class's stat package;
- that class's Trait;
- any effect explicitly defined as selected-class-only.

Selected class does **not** erase already learned equipment access or Abilities.

## 5. Global Ability weapon-independence rule — locked

**No Ability or Ultimate may require a particular equipped weapon.**

Once learned, every Ability and Ultimate remains usable with any otherwise-legal equipment loadout.

Equipment still matters for:
- ordinary **Attack**;
- equipment stats and defenses;
- Weapon / Secondary slot geometry;
- Relic / Legacy legality;
- visual presentation.

If an Ability visually implies a weapon not currently equipped, presentation adapts through an authored manifested/projected weapon expression rather than disabling the command.

This rule specifically supersedes earlier drafts that weapon-gated Truthshot or Axiomblade techniques.

Abilities use their own authored formula and hit package. They do **not** inherit the equipped weapon's normal Attack hit pattern unless explicitly authored.

## 6. Equipment inheritance architecture — locked

Ordinary reciprocal donor-equipment progression is:

- **Vaelira ← Cyanis:** Swords → Crest armor → Shield + second-Sword permission.
- **Cyanis ← Vaelira:** Arcane Staffs → Green Arcanist armor → Focus.
- **Seyrik ← Ilyra:** Wardrods → Warding armor → Shield + Focus where legal.
- **Ilyra ← Seyrik:** Two-Handed Swords → Ruin armor; no fabricated CL5 reward.
- **Torren ← Nimera:** one-slot Conduits → Cardweaver armor → two-handed Conduits + Focus where Secondary is free.
- **Nimera ← Torren:** Great Bows → War Archer armor; no fabricated CL5 Secondary.

A two-slot Great Bow, Two-Handed Sword, or two-slot Conduit still occupies Weapon + Secondary normally.

Donor equipment is not cherry-picked. Reciprocal training grants the donor Base tradition's legal ordinary equipment package according to the approved schedule.

## 7. Relic / Mastery boundary — locked where settled

The overall Mastery architecture remains **9 one-point nodes**:
- 4 Core Masteries;
- 4 Subclass Masteries;
- 1 Synthesis.

Each node costs **1 Mastery Point** and unspent MP may be banked.

The following are canonized now:
- **Equipment Mastery is Subclass Mastery Node 4**;
- Equipment Mastery becomes eligible at **Subclass CL10**;
- spending 1 MP on Equipment Mastery grants donor **Relic** access;
- ordinary donor equipment is learned earlier through Subclass progression;
- Legacy eligibility is later and tied to Synthesis.

The exact final effect text and final gate schedule for the four Core Masteries, and any still-unfinalized earlier Subclass Mastery-node gate/effect text other than Equipment Mastery at CL10, remain open for the dedicated Core Mastery reconciliation pass.

## 8. Final reciprocal Subclasses — locked

The six permanent characters' final Base/Subclass pairings are:

- **Cyanis — Crest Knight / Crest Arcanist**
- **Vaelira — Green Arcanist / Axiomblade**
- **Ilyra — Blue Warden / Vowblade**
- **Seyrik — Ruin Vanguard / Ruin Warden**
- **Torren — War Archer / Routeweaver**
- **Nimera — Cardweaver / Truthshot**

Supersessions:
- **Ruin Warden** supersedes `Ruin Reclaimer` and `Ruin Healer`.
- **Truthshot** supersedes the retired Cyanis-derived / Sixfold Knight direction for Nimera.
- **Routeweaver** is the controlling Torren Subclass name.

## 9. Subclass identities and locked ability spines

### 9.1 Cyanis — Crest Arcanist
Trait: **Crest Resonance**.

Abilities:
- Arcane Lance
- Warding Crest
- Nullifying Seal
- Arcane Rupture
- Elemental Convergence
- Ultimate: **Crest Dominion**

Identity: Colorless Crest magic, Fields, Seals, anti-magic/structural disruption, penetration, and controlled elemental convergence.

Crest Arcanist Abilities are weapon-independent once learned.

### 9.2 Vaelira — Axiomblade
Trait: **Formal Equivalence**.

Abilities:
- First Principle
- Proven Advance
- Counterproof
- Axiom Rend
- Equivalent Form
- Ultimate: **Final Axiom**

Identity: Cyanis-derived Crest discipline translated through Vaelira's elemental/arcanist logic, with authored Martial and Arcane expressions independent of equipped weapon.

### 9.3 Ilyra — Vowblade
Trait: **Mercy in Steel**.

Abilities:
- Vital Edge
- Mercy Returned
- Living Covenant
- Vowkeeper's Reprisal
- Vow of Severance
- Ultimate: **Mercy's Final Edge**

Damaging Vowblade Abilities use the approved **50% Attack / 50% Spirit Hybrid** formula.

Identity: preservation expressed through decisive offense, self-sustain, ally recovery, and protective aftermath without self-damage or a personal gauge.

### 9.4 Seyrik — Ruin Warden
Trait: **Ruin's Mercy**.

Abilities:
- Siphon Rune
- Stolen Grace
- Restoring Ward
- Withering Mercy
- Reclaimed Breath
- Ultimate: **Mercy Through Ruin**

**Siphon Rune** is one authored hit using **60% Attack / 40% Magic Hybrid** scaling.

Identity: Blue Warden preservation translated through controlled Ruin logic: drain, transfer, cleansing, protection, recovery, and revival.

### 9.5 Torren — Routeweaver
Trait: **Field Weaving**.

Abilities:
- Throughline
- Clear Route
- Crossroads
- Covered Crossing
- Forced Passage
- Ultimate: **Open the Way**

Damaging Routeweaver Abilities use the approved **50% Attack / 50% Magic Hybrid** formula.

Identity: Cardweaver-derived routing, field control, hybrid pressure, and selective Standard Card support without becoming a second Cardweaver.

### 9.6 Nimera — Truthshot
Trait: **Applied Evidence**.

Abilities:
- Measured Shot
- Held Argument
- Pin the Variable
- Structural Failure
- Corroboration
- Ultimate: **Final Annotation**

Identity: genuine War Archer discipline translated through Nimera's evidence/analysis language: Hunter's Measure, Prepared interruption, mobility pressure, penetration, multihit accuracy/critical scaling, and hard-target exploitation.

Truthshot Abilities remain usable with non-Great-Bow legal loadouts; presentation adapts as needed.

## 10. Torren / Nimera shared-state rules — locked

**Hunter's Measure** is the shared War Archer-derived quarry state for Torren and Nimera.

- Either may apply it where authored.
- Either may exploit Hunter's Measure applied by the other.

Keep distinct:
- **Hunter's Measure** = shared quarry/target state;
- **Diysean Appraisal** = Nimera information reveal only;
- **Indexed** = Card-specific state from Sovereign Index.

There is **no `Appraised` status** and Audit100 does not create one.

## 11. Synthesis — universal architecture locked

Synthesis is the ninth/final Mastery node.

A character may purchase Synthesis only when all of the following are true:
1. **Base Class CL13**;
2. **Subclass CL13**;
3. all four Core Mastery nodes purchased;
4. all four Subclass Mastery nodes purchased;
5. that character's authored resolution/integration story requirement completed;
6. **1 unspent MP** available.

Purchase costs exactly **1 MP**.

A reciprocal pair may satisfy the story requirement in one shared authored scene, but eligibility and purchase remain **individual**.

The story gate is mandatory authored continuity, not romance, affinity, dialogue choice, or a permanently missable route.

Each Synthesis grants:
- one permanent character-specific Base/Subclass integration passive; and
- reciprocal partner **Legacy eligibility** under the pair mapping below.

Synthesis is persistent after purchase.

Synthesis does **not**:
- create a third/fusion class;
- merge stat packages;
- activate both Traits simultaneously;
- add an ordinary action;
- add an equipment slot;
- add a Standard Card slot;
- add a personal gauge;
- copy a partner's entire kit;
- bypass two-slot equipment geometry;
- create weapon requirements;
- bypass Prepared-effect limits;
- refresh or add Prime uses/slots;
- award class levels or another MP.

A learned Ability retains its source-class identity for Synthesis trigger checks regardless of selected class.

## 12. Final six Synthesis effects — locked

### Cyanis — Unified Crest
A selected/resolved Crest Knight Ability may establish existing **Crest Attunement** when absent. Consuming Crest Attunement with a legal Crest Field/Seal arms **+15% Power** for Cyanis's next damaging Crest Knight Ability before the end of the following round.

### Vaelira — Unified Spectrum
A damaging Axiomblade Ability against an Imprinted target may use one existing Imprint element without consuming the Imprint. Once per round, a matching Axiomblade hit extends that matching Imprint by **+1 round** up to its authored maximum. Prism Cycle retains precedence. No automatic Composite Reaction is created.

### Ilyra — Mercy Unbroken
A qualifying non-Ultimate Blue Warden heal/cleanse on another ally arms **+10% Power** for the next damaging non-Ultimate Vowblade Ability before the end of the following round. A Vowblade Ability/Ultimate that restores HP to another ally arms **-3 MP** on the next non-Ultimate Blue Warden Ability, minimum 1 MP.

### Seyrik — Tempered Ruin
A damaging non-Ultimate Ruin Vanguard Ability arms **-3 MP** on the next non-Ultimate Ruin Warden Ability, minimum 1 MP. A Ruin Warden Ability/Ultimate that restores HP to another ally arms **+10% Power** for the next damaging non-Ultimate Ruin Vanguard Ability.

### Torren — Measured Passage
A damaging non-Ultimate War Archer Ability resolving against Hunter's Measure arms **-2 MP** on the next non-Ultimate Routeweaver Ability, minimum 1 MP. Establishing or legally extending a Torren Route Field arms **+10% Power** for the next damaging non-Ultimate War Archer Ability against Hunter's Measure.

### Nimera — Living Proof
A target satisfies Living Proof's known-target condition when Diysean Appraisal has revealed its permitted combat data **and** Hunter's Measure is currently present. Once per round, Nimera's first damaging non-Ultimate Truthshot against that target gains **+10% Power**. A qualifying Truthshot/Final Annotation hit then arms **+10 Base Hit / application reliability** for the next hostile Standard Card against that same target where relevant.

## 13. Synthesis normalization rules — locked

The approved six-Synthesis cross-balance audit is a **PASS** with no broad raw-number rebalance.

Universal normalization:
- one Ability action can satisfy a given Synthesis trigger only once regardless of multihit, AoE, multi-heal, or multi-cleanse resolution;
- each directional clause may hold at most one armed copy;
- opposite directional clauses may coexist when legally armed;
- current Synthesis Power bonuses and MP discounts do **not** apply to Ultimates;
- an Ultimate may arm a later Synthesis effect only where explicitly authored;
- merely arming a Prepared effect never counts as a damaging trigger; an actually resolving response may qualify where explicitly legal;
- all Synthesis mechanics remain weapon-independent;
- no new resource/state family is created beyond already-existing authored states.

## 14. Mandatory Synthesis-resolution story beats — locked

All three pair-resolution beats are mandatory authored continuity in the late-game preparation window. Exact final dialogue and final scene numbering remain for the later script-integration pass, but their function, thesis, placement family, and outcomes are locked.

### 14.1 Cyanis ⇄ Vaelira — What Holds, What Changes
- **Placement:** late Chapter 11, preferred at Cresthaven during the return/preparation window before Chapter 12's point of no return.
- A fixed Crest fails under changed elemental conditions; a fully adaptive pattern loses its stable center.
- Together they build a pattern where Cyanis anchors only what must remain fixed while Vaelira lets the surrounding channels adapt.
- Cyanis resolves that protection does not require freezing the entire shape.
- Vaelira resolves that adaptation does not require refusing commitment.
- Completion satisfies the Synthesis story prerequisite for both characters.
- No item reward, boss, quest branch, romance framing, or new system is attached.

### 14.2 Ilyra ⇄ Seyrik — Keep Them Alive
- **Placement:** late Chapter 11 at the Forward Hub treatment/recovery staging.
- An unnamed wounded Black Host captive requires treatment; there is no false argument over whether the captive deserves to live.
- Ilyra defines what must be protected; Seyrik applies controlled Ruin only within that boundary.
- Ilyra later chooses the hard intervention herself; Seyrik demonstrates growth by stopping exactly where necessary destruction ends.
- Locked distinctions: **mercy is not forgiveness; restraint is not passivity; violence is not automatically decisiveness**.
- Completion satisfies both Synthesis story prerequisites.
- The captive remains unnamed and does not create a redemption route or recurring-NPC obligation.

### 14.3 Torren ⇄ Nimera — Enough to Move
- **Placement:** late Chapter 11 at the Forward Hub operations/map table.
- Torren's sound veteran judgment initially cannot be transferred because too much reasoning remains implicit.
- Nimera's exhaustive analysis initially preserves too many branches to remain useful under time pressure.
- They produce one primary route, one fallback, and the observable condition that determines when to switch.
- Torren resolves that experience becomes more valuable when its reasoning can be transmitted.
- Nimera resolves that uncertainty does not invalidate a responsible decision when the decisive facts are known.
- Completion satisfies both Synthesis story prerequisites.
- The closing proof is that another runner can correctly use the route without either of them present.

## 15. Legacy architecture — locked

Legacy equipment remains a distinct third tier after ordinary donor equipment and donor Relics.

Tier structure:
1. Subclass CL1–5 = ordinary donor equipment tradition;
2. Subclass CL10 + purchased Equipment Mastery = donor Relic access;
3. full Synthesis eligibility + purchased Synthesis = reciprocal pair Legacy eligibility.

Synthesis grants **legal permission**, not automatic item creation.

A physical Legacy item must still be acquired from its authored source.

Once a Legacy is acquired and a character is legally eligible, full Legacy bonuses apply to that legal wearer under the inherited open-equipment rule.

Exact final numerical Legacy stats and final passive text, if any, remain for the production item/equipment audit.

## 16. Final six Legacy items and reciprocal mappings — locked

### Cyanis ⇄ Vaelira
- Crest Knight Legacy: **Stillpoint Aegis** — **Shield**.
  - Native tradition: Crest Knight.
  - Vaelira gains reciprocal eligibility after purchasing **Unified Spectrum / Synthesis**.
- Green Arcanist Legacy: **Living Prism** — **Focus**.
  - Native tradition: Green Arcanist.
  - Cyanis gains reciprocal eligibility after purchasing **Unified Crest / Synthesis**.

### Ilyra ⇄ Seyrik
- Blue Warden Legacy: **Mercy's Boundary** — **Shield**.
  - Native tradition: Blue Warden.
  - Seyrik gains reciprocal eligibility after purchasing **Tempered Ruin / Synthesis**.
- Ruin Vanguard Legacy: **Purposebound** — **Two-Handed Sword**.
  - Native tradition: Ruin Vanguard.
  - Ilyra gains reciprocal eligibility after purchasing **Mercy Unbroken / Synthesis**.

### Torren ⇄ Nimera
- War Archer Legacy: **Known Ground** — **Great Bow**.
  - Native tradition: War Archer.
  - Nimera gains reciprocal eligibility after purchasing **Living Proof / Synthesis**.
- Cardweaver Legacy: **Decisive Record** — **one-slot Conduit**.
  - Native tradition: Cardweaver.
  - Torren gains reciprocal eligibility after purchasing **Measured Passage / Synthesis**.

Slot geometry remains normal:
- Shield / Focus = Secondary;
- Great Bow = Weapon + Secondary;
- Two-Handed Sword = Weapon + Secondary;
- one-slot Conduit = Weapon and leaves Secondary available if otherwise legal.

None of the six Legacies changes Ability legality.

## 17. Legacy acquisition presentation — locked

All six Legacy items are deterministic physical equipment pickups through one shared **Cresthaven secured-equipment release during the Chapter 12 pre-point-of-no-return preparation window**.

Locked production boundaries:
- reuse an existing Cresthaven armory / secured-equipment staging area;
- no new dungeon;
- no new Hunt or boss;
- no crafting recipe;
- no material grind;
- no special currency;
- no random drop;
- no new side quest;
- Synthesis does not conjure the items;
- the late-Chapter-11 pair-resolution scenes remain item-reward-free.

The player may physically collect a Legacy before the reciprocal character has purchased Synthesis. In that case, the item remains in inventory and the equipment UI shows the relevant Synthesis/Legacy requirement until eligibility is satisfied.

Acquisition and eligibility remain separate.

## 18. Cross-balance conclusions — locked

The approved class-rework and Synthesis cross-balance audits pass without broad raw-number rebalance.

Locked conclusions include:
- class stat-package asymmetry is intentional and should not be equalized by arithmetic sum;
- lower/higher early Ability Power is judged with cost, targeting, setup, penetration, status, Fields, and other utility rather than raw Power alone;
- no extra pre-Synthesis reciprocal synergy is required merely for symmetry;
- all six class identities remain distinct;
- no Subclass introduces a prohibited personal gauge, extra ordinary action, extra Card slot, or duplicate target-mark subsystem;
- no class or Synthesis specification establishes additive direct-damage-reduction stacking by itself.

The final **global direct-damage-reduction stacking rule** remains open for a separate normalization pass.

The universal **Ultimate MP-cost convention** also remains open.

## 19. Explicitly open / not promoted by Audit100

Audit100 intentionally leaves the following unresolved:
- final Core Mastery effect text;
- final Core Mastery gate schedule if later adjusted;
- any still-unfinalized early Subclass Mastery-node gate/effect text other than Equipment Mastery at CL10;
- Torren / Nimera / Vaelira working starting Base CL values unless separately approved elsewhere;
- final global direct-damage-reduction stacking semantics;
- universal Ultimate MP-cost convention;
- exact final numerical stats/passives for the six Legacy items;
- final Legacy item IDs, prices/sell values, descriptions, icons, and inventory sorting metadata;
- final Chapter-11 scene numbering and exact dialogue for the three resolution beats;
- the deliberate repository-wide stale-terminology sweep from `Sixfold Accord` to **Sixfold Volition**;
- production implementation/data regression work required to bring runtime content in line with the newly locked class authority.

These remain open design/implementation tasks and must not be filled by assumption.

## 20. Final lock

As of Audit100, Diyse's reciprocal class-rework layer is no longer provisional.

The project now has master-canon authority for:
- the Sixfold Volition name and reciprocal training architecture;
- Base/Subclass CL13 structure and CEXP thresholds;
- the six final Subclasses;
- global weapon-independent Ability/Ultimate legality;
- approved donor-equipment inheritance;
- Equipment Mastery at Subclass CL10;
- universal Synthesis eligibility and behavior;
- all six character-specific Synthesis effects;
- all three mandatory resolution/integration beats;
- all six Legacy names, equipment families, reciprocal mappings, and Chapter-12 acquisition presentation.

Compatible v1.84/Audit99 and earlier canon remains inherited everywhere Audit100 is silent.