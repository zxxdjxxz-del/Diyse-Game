# Diyse — Class State Lifecycle
**Current working authority:** 2026-08-30 class-state normalization.  
**Domain:** ordinary class-authored combat states that are not universal harmful statuses, temporary core-stat modifiers, Fields, summons, or Prime-local states.

This file owns the default lifecycle of class-authored tactical/setup states. Individual class sheets still own each state's exact trigger, subject, magnitude, duration, consumption rule, and any explicit exception.

## Boundary with other systems

This file does **not** redefine:
- universal harmful statuses or Regen — `../05_BATTLE_SYSTEM/STATUS_EFFECTS.md`;
- temporary Attack / Magic / Defense / Spirit / Speed modifiers — `../05_BATTLE_SYSTEM/STAT_CHANGES.md`;
- Fields — `../05_BATTLE_SYSTEM/FIELDS.md`;
- summons such as Shardfang — their owning class file;
- Prime-local states or the pause of normal-round tactical states during Awakened Prime manifestation — `../07_CARDS/PRIME_CARDS/PRIME_SYSTEM_RULES.md`.

A class effect should use the narrowest existing category that actually fits it rather than creating a hidden new status/resource system.

## State categories

### Self-attached stored state
A short-lived benefit or stored condition attached to the acting character and consumed or replaced by a later qualifying action.

Current examples:
- Crest Arcanist — **Crest Attunement**;
- Axiomblade — **Formal Equivalence stored element**;
- Vowblade — **Tempered Mercy**;
- Routeweaver — **Route Weaving Rank I stored benefit**.

### Self stance
A temporary mode attached to the acting character that modifies qualifying actions while it remains active.

Current example:
- Vowblade — **Living Covenant**.

### Prepared protection / reaction state
A pending explicitly authored reaction or prevention attached to the subject named by the Ability.

Current examples:
- Crest Knight — **Crest Reprisal Prepared** is attached to Cyanis;
- Blue Warden — **Lifeline Prepared** is attached to the protected ally.

Prepared action timing remains governed by the owning Ability plus `../05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md`.

### Target-attached tactical state / link
A state attached to one or more battle targets after an action establishes it.

Current examples:
- War Archer / Proofhunter — **Hunter's Measure**;
- Routeweaver — **Throughline**;
- Routeweaver — **Crossroads**.

Shared state identity remains owned by `SHARED_CLASS_STATES.md` where more than one class uses the same state.

### Archive / preserved record state
A record set attached to the recording character rather than to the original action's source.

Current examples:
- Cardweaver — current **Living Archive** recording window;
- Cardweaver — **Perfect Recall / Preserved Record**.

### Pending initiative-routing state
A one-shot pending instruction for a future normal-round initiative setup.

Current examples:
- Routeweaver — **Covered Crossing**;
- Routeweaver — **Open the Way**.

These do not grant extra actions and remain subject to the exact Torren-eligibility checks in the Routeweaver owner.

## Default creation and reapplication

Unless an owning effect explicitly says otherwise:
- a class-authored state becomes active immediately when its source action finishes establishing it;
- the same named state from the same source on the same subject does **not** create a generic second stack;
- successful reapplication refreshes the existing duration or replaces its stored payload with the newest legal payload;
- different state identities may coexist when their owning rules otherwise allow it;
- a consumed one-shot state ends immediately after its qualifying consumption/trigger resolves.

An explicit class owner may override refresh/replace behavior, but silence never implies self-stacking.

## KO / incapacitation lifecycle

Attachment controls KO behavior.

### State attached to the KO'd unit itself
When a unit becomes KO/incapacitated:
- its self-attached stored states clear;
- its self stances clear;
- its own self-attached Prepared states clear;
- its actor-attached archive/preserved-record states clear;
- those cleared states do **not** automatically return if the unit is later revived.

Therefore, under the current owners, KO clears examples such as Crest Attunement, a stored Formal Equivalence element, Tempered Mercy, Living Covenant, Crest Reprisal Prepared, Living Archive's current record window, and Perfect Recall's Preserved Record when those states are attached to the KO'd character.

### State attached to a different target
The source character becoming KO does **not** automatically erase an already-established target-attached tactical state or Prepared protection on another legal subject unless the owning effect explicitly requires the source to remain conscious/present.

Examples:
- Hunter's Measure on an enemy does not vanish merely because Torren or Nimera is KO'd;
- Throughline or Crossroads does not vanish merely because Torren is KO'd;
- Lifeline Prepared on an ally does not vanish merely because Ilyra is KO'd after casting it.

If the **subject carrying the state** becomes KO, is defeated, leaves battle, or is replaced by another battle body, the state ends unless its owner explicitly says it transfers or survives that event. Revival does not restore a state cleared with the subject's KO.

A source-side reward that would restore HP/MP or otherwise benefit an incapacitated source still requires that source to be a legal recipient when the reward resolves; persistence of the target-attached state does not make a KO source able to receive ordinary recovery unless another rule permits it.

## Battle-end lifecycle

Ordinary class-authored tactical/setup states are battle-local.

At battle end:
- self stored states and stances clear;
- Prepared states clear;
- target-attached tactical states and links clear;
- archive/preserved-record states clear;
- pending initiative-routing states clear.

They do not persist into the next battle unless a future effect explicitly defines an out-of-battle persistent state.

Prime **spent/Ready availability is not a class state** and follows its separate rest-based persistence rule.

## Enemy form / body replacement

A same-HP-bar phase/state change does not by itself remove a target-attached class state; the state continues under its own duration and structural rules unless the encounter explicitly removes it.

A genuine fresh-HP body/form is a different battle body. A class state attached to the previous enemy body does **not** transfer to the new body unless the encounter or state owner explicitly says it does.

This applies generally to target-attached states such as Hunter's Measure, Throughline, and Crossroads links.

Unrelated party self-states are not erased merely because the enemy changes body; they continue under their own lifecycle unless the encounter explicitly clears them.

Fresh-body classification itself remains owned by `../05_BATTLE_SYSTEM/BOSS_FORM_RULES.md`.

## Awakened Prime interaction

Do not duplicate Prime timing here.

For a class-authored state measured in normal rounds, an Awakened Prime manifestation pauses that normal-round clock under `../07_CARDS/PRIME_CARDS/PRIME_SYSTEM_RULES.md` unless the state owner explicitly says otherwise.

Prime suspension does not count as KO and therefore does not invoke the KO-clearing rules above.

Prime commands do not automatically become legal subjects/triggers for ordinary class states merely because the state remains recorded during suspension.

## Firewall

Do not reinterpret these states as:
- universal harmful statuses;
- hidden gauges/resources;
- generic buff/debuff stacks outside their authored effect;
- extra-action systems;
- a restored action queue;
- a reason to bypass Field, temporary-stat, status, summon, or Prime ownership boundaries.
