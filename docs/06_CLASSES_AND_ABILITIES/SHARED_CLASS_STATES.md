# Diyse — Shared Class States
**Current working authority:** 2026-08-30 Torren/Nimera class redesign.  
**Domain:** shared class-authored combat states used by more than one current playable class.  

This file owns the exact shared definition of a class state when multiple class sheets use the same state. Individual class Abilities own how they apply, refresh, or exploit that state.

General class-state lifecycle defaults — including KO behavior, battle-end clearing, target/body replacement, and same-state refresh/replacement — are owned by `CLASS_STATE_LIFECYCLE.md`. A shared state's explicit rules in this file override those defaults where they are more specific.

## Hunter's Measure

**Current users:** War Archer and Proofhunter.

Hunter's Measure is an authored tactical state, **not** one of the five universal harmful statuses.

While an enemy has Hunter's Measure:
- that enemy suffers **Evasion −10**;
- all active party members gain **+10 percentage points Critical Chance** against that enemy.

### Duration
When applied during normal turn resolution:
- it is active immediately for the remainder of the current round;
- it remains active for the next **2 full normal rounds**;
- this explicit window overrides generic numbered-round shorthand.

Reapplication:
- refreshes the full authored window;
- does not stack a second Hunter's Measure instance.

### Resistance / removal boundary
- Ordinary Status Resistance does **not** resist Hunter's Measure.
- Ordinary harmful-status cleanse does **not** automatically remove it.
- It ends when its authored duration expires, battle ends, its target/body is defeated or replaced, or an owning explicit effect says it removes the state.
- The character who applied or refreshed Hunter's Measure becoming KO does **not** by itself remove the state from the enemy.

### Form boundary
A genuinely separate fresh-HP enemy/boss form does **not** inherit Hunter's Measure from the previous form unless that encounter explicitly says otherwise.

### Shared-state rule
War Archer and Proofhunter use this **same state identity**. Applying or refreshing it from either class updates the same Hunter's Measure instance on that target.

No class may create a separate stronger/weaker version of Hunter's Measure merely by renaming or reapplying it. Class Traits, Masteries, Abilities, equipment, and other effects may instead grant their own bonuses **against** a Measured target.

## Firewall
Do not reinterpret Hunter's Measure as:
- a universal harmful status;
- a hidden Break/Stagger meter;
- an Accuracy stat;
- a separate Torren/Nimera version;
- automatic enemy-information revelation beyond what an explicit current effect actually reveals.
