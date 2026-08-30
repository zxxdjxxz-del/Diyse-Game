# Diyse — Fields
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary recovered authority:** compatible **Audit115** Field rules, reconciled with the current turn-entry round model and current Prime replacement rules.  
**Authority rule:** this file owns the global Field lifecycle. Individual Abilities, Cards, enemies, encounters, and other effects own the exact Field they create and its printed effects.

## Definition

A **Field** is a battlefield-attached temporary multi-round combat state.

Fields are valid globally.

A Field is **not**:
- a universal harmful status;
- a stat-change category by itself;
- Guard;
- a Prepared action;
- a hidden gauge;
- a replacement for the removed Barrier system.

Ordinary Status Resistance does not resist a Field merely because that Field is beneficial or harmful.

Ordinary harmful-status remedies do not remove Fields unless an effect explicitly says it can remove a Field.

## Creation

A Field becomes active when its creating action resolves unless its owning effect explicitly establishes a later start.

Its printed effects become active immediately on all currently legal subjects.

Examples of current player Field authority:
- Cardweaver **Ancient Override** — Field;
- War Archer **Choose the Route / Clear Route** — Field;
- War Archer **Choose the Route / Covered Route** — Field.

Explicit non-Field examples:
- Routeweaver **Crossroads** is a linked-enemy route state, **not** a Field;
- Routeweaver **Open the Way** is a next-round initiative-routing Ultimate, **not** a Field;
- Crest Arcanist has **no Field-creation Ability** in its current normalized kit.

## Duration

A Field written as lasting a number of rounds follows the global round-duration rule in `TURN_AND_ROUND_RULES.md` unless its owner explicitly prints another clock.

Therefore during ordinary combat:
1. the Field activates immediately when created;
2. if created during ordinary turn resolution, the application round counts as its first duration round;
3. its first duration checkpoint is that ordinary round's end-of-round processing;
4. a Field created during end-of-round processing does not instantly consume a duration checkpoint at that same boundary.

A Field's duration does not retroactively alter actions that resolved before the Field existed.

## Speed and other Field modifiers

A Field may contain ordinary stat changes, Base Hit modifiers, Status Resistance, direct-damage reduction, Card modifiers, MP-cost modifiers, or other explicitly authored effects.

Each contained effect resolves through its own global owner.

In particular:
- a Speed modifier from a Field becomes active immediately but does **not** reshuffle initiative already fixed for the current round;
- if still active at the next normal round's initiative check, that Speed modifier affects ordering normally;
- Defense/Spirit/Attack/Magic changes use `STAT_CHANGES.md`;
- MP-cost changes use `06_CLASSES_AND_ABILITIES/MP_COST_RULES.md` where applicable;
- direct-damage reduction uses `DAMAGE_FORMULAS.md`;
- harmful statuses use `STATUS_EFFECTS.md`.

A Field does not create a special stacking exception merely because multiple modifiers come from one battlefield state.

## Same-Field reapplication

Unless an owning Field explicitly says otherwise:
- creating the **same named Field from the same source identity** while it is already active refreshes/replaces that instance at its full authored duration;
- it does not create a second additive copy of the same Field;
- one source does not gain multiple simultaneous copies of its own same named Field.

If an owning class or action establishes a stricter source limit, that stricter limit controls.

Current examples:
- Cardweaver **Ancient Override** refreshes its existing Nimera-authored Ancient Override rather than stacking a second copy;
- War Archer **Choose the Route** allows only one Torren-authored War Archer Route Field at once; choosing Clear Route or Covered Route replaces the other.

## Different Fields / global slot rule

There is **no universal one-Field battlefield slot**.

Different legal Fields may coexist unless an owning action, class, encounter, or specific Field says otherwise.

Their contained effects still obey the normal same-axis/stat/direct-reduction/cost-modifier rules. Coexistence therefore does not imply that every numeric modifier adds together.

## Field removal

Only an effect explicitly capable of removing a Field may do so.

Current player examples include:
- **Arcane Rupture** — removes 1 removable hostile Field after damage;
- **Crest Dominion** — removes 1 removable hostile Field as part of its post-damage package.

**Ancient Override no longer removes a hostile Field on creation.** Its current identity is party MP economy.

If a player-controlled effect can remove exactly one hostile Field and more than one eligible hostile Field exists, the player chooses which eligible Field is removed as part of that action's legal content selection.

An enemy/AI Field-removal effect chooses according to its owning AI/encounter rule.

A Field explicitly marked protected, scripted, or nonremovable by its encounter owner cannot be removed by ordinary Field-removal effects.

Removing a Field ends only that Field and the effects that depend on that Field remaining active. It does not automatically cleanse separate harmful statuses or separate stat changes that were authored as independent effects.

## Awakened Prime interaction

Awakened Prime control uses **Prime rounds**, not normal party rounds.

Therefore ordinary numbered-round Fields:
- remain recorded while the ordinary party is suspended;
- do **not** consume their normal-round duration checkpoints merely because a Prime round completed;
- resume their normal-round duration clock when normal party-round flow resumes.

A party-authored ordinary Field does **not** automatically treat the manifested Prime body as a normal conscious party member or ally target. It affects the Prime only if the Field or Prime effect explicitly says it does.

Likewise, Field effects continue only on subjects that remain legally included by their own wording during Prime control; the suspended ordinary party is not acting or targetable during Prime rounds.

Recovered Story Prime manifestations occur inside the ordinary-round structure and do not create a separate multi-round Field-duration clock by themselves.

## Removal / battle end

Ordinary Fields end when:
- their duration expires;
- an eligible explicit Field-removal effect removes them;
- their owning replacement rule replaces them;
- the battle ends;
- an encounter-specific rule explicitly clears them.

A battle ending does not carry an ordinary combat Field into the next battle unless an exceptional owning rule explicitly says otherwise.

## Firewall

Do not restore through Field wording:
- Barrier;
- Brace;
- global Break/Stagger meter;
- Card Seals;
- Imprints;
- a universal one-Field slot;
- a Field gauge or Field resource.
