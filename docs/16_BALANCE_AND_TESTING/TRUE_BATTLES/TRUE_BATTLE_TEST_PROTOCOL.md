# Diyse — True-Battle Test Protocol

**Status:** ACTIVE TRUE-BATTLE TEST METHOD  
**Balance/QA authority:** `../README.md`

True-battle tests resolve actual battle flow under current repository rules. They are evidence, not a second authority source.

## Source rule

Before every test, read current inputs from:

- combat math/timeline/statuses — `../../05_BATTLE_SYSTEM/`
- classes/Abilities/MP — `../../06_CLASSES_AND_ABILITIES/`
- Cards/Primes — `../../07_CARDS/`
- equipment/items — `../../08_ITEMS_AND_EQUIPMENT/`
- encounters — `../../09_ENEMIES_AND_ENCOUNTERS/`
- Player EXP/CEXP route state — `../../10_PROGRESSION_AND_EXP/`

Do not reuse an earlier test snapshot as authority for a later run.

## Snapshot requirements

Record before combat:

- current Character Level / Class Level state;
- legal active four and reserves;
- selected classes;
- equipment/loadouts;
- Standard Cards / Prime loadouts and Ready/Spent state;
- consumables;
- starting HP/MP;
- encounter-specific forced states;
- route profile and intentional incoming attrition.

## Mandatory vs completionist comparison

Where practical, hold constant ordinary equipment, normal-stock consumables, active four, and tactical competence.

Let route differences come from actual progression state. Optional Card/Prime/Relic/Legacy advantages may be tested separately.

## Prime rules

Use current Prime authority. In particular:

- spent identities persist until valid restoration;
- boss form/state transitions alone do not restore spent identities;
- Awakened manifestation uses the 3-segment Manifestation Meter;
- meter is spent only on successful EXECUTION;
- meter-emptying action enters Final Return;
- normal Dismissal resolves on the Prime's already-scheduled next TURN;
- after demanifestation, nobody may invoke a Prime until the invoker processes 3 personal TURNs;
- the invoker's hidden reserve TURNs count;
- restoration does not bypass an active lockout.

## Stochastic resolution

Where actions/targets/crits/statuses are random:

1. preserve the same tactical policy;
2. record representative logs where useful;
3. run enough samples to estimate outcome distribution;
4. do not treat one lucky/unlucky run as balance authority.

## Primary difficulty signals

Measure:

- temporary-KO incidence;
- wipe incidence;
- ending HP/MP;
- item/recovery pressure;
- mechanic-response pressure;
- timeline duration.

## Retune rule

Do not change an owning-domain value from one anomalous run.

A balance change requires reproducible evidence of structural failure and must be made in the owning domain with affected regression tests rerun.
