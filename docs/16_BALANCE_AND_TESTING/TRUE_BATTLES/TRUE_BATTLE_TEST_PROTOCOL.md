# Diyse — True-Battle Test Protocol

**Status:** ACTIVE TRUE-BATTLE TEST METHOD  
**Balance/QA authority:** `../README.md`

True-battle tests resolve actual battle flow under the current repository rules. They are balance/QA evidence, not a second source of enemy stats, progression, Prime rules, equipment, or rewards.

## Source rule

Before every test, read current inputs from their owners:
- combat math/status/round rules — `../../05_BATTLE_SYSTEM/`;
- classes/Abilities/MP — `../../06_CLASSES_AND_ABILITIES/`;
- Cards/Primes — `../../07_CARDS/`;
- equipment/items — `../../08_ITEMS_AND_EQUIPMENT/`;
- encounter bodies/forms/actions — `../../09_ENEMIES_AND_ENCOUNTERS/`;
- Player EXP/CEXP route state — `../../10_PROGRESSION_AND_EXP/`.

Never copy an old true-battle snapshot forward as current authority.

## Snapshot requirements

Record before combat:
- current Character Level / Class Level / learned ability state;
- legal active party and active four;
- selected classes;
- equipment/loadouts;
- Standard Cards / Prime loadouts and Ready/spent state;
- consumables;
- starting HP/MP;
- encounter-specific forced states;
- route profile and any incoming attrition intentionally included.

## Mandatory vs completionist core comparison

Where practical, hold constant:
- ordinary equipment;
- normal-stock consumables;
- active four;
- competent tactical policy.

Let real route differences come from Player Level, CEXP, and naturally learned progression.

Optional Card/Prime/Relic/Legacy advantages may be tested separately so they do not hide the underlying progression signal.

## Prime rules

Use the current Prime owner at test time. In particular:
- spent Prime identities persist until valid restoration;
- a boss state/form transition does not restore spent Primes merely because a new body begins;
- after Prime dismissal, **3 full normal party rounds** must complete before another Ready Prime may be invoked;
- explicit authored restoration effects may restore Ready/spent state without bypassing the spacing gate unless their current owner explicitly says otherwise.

## Stochastic resolution

Where actions/targets/hits/crits/statuses are random:
1. preserve the exact tactical policy;
2. record representative logs where useful;
3. run enough repeated samples to estimate outcome distribution;
4. do not treat one lucky/unlucky run as balance authority.

## Primary difficulty signals

Measure:
- temporary-KO incidence;
- wipe incidence;
- ending HP/MP;
- item/recovery pressure;
- mechanic-response pressure;
- duration secondarily.

## Retune rule

Do not change a closed owner-domain value from one strange run.

A balance change should require reproducible evidence of a real structural failure, then be made in the owning domain with affected regression tests rerun.

Design-layer simulation does not replace runtime QA.
