# Diyse — Kessara Relic-Copy UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## IMPLEMENTED FOUNDATION
Current service logic already validates:
1. original Relic obtained;
2. Relic not already copied;
3. Face has remaining copy opportunity;
4. matching-Face Relic-copy component exists;
5. commit consumes that component;
6. same Relic identity becomes quantity 2.

Per Face:
> exactly **3** Relic-copy components / copy opportunities.

Per individual Relic:
> at most **1 forged duplicate**, quantity max **2**.

Legacies cannot use this service.

## Required service UI information
A future service menu must be able to show:
- Relic identity;
- Face;
- original obtained / not obtained;
- current quantity;
- copied already / copy available;
- matching component available;
- Face copy opportunities used/remaining or equivalent clear eligibility feedback;
- final result quantity 2 after success.

## Failure reasons already represented by service code
- invalid state;
- original not obtained;
- already copied;
- Face copy limit reached;
- no matching component;
- commit failed.

Player-facing wording can be polished without changing the rule.

## Still OPEN
- exact service unlock/menu timing;
- whether an Auren service fee exists;
- fee amount;
- exact original-vs-copy visual badge/label;
- confirmation flow;
- service animation/presentation.

Do not hardcode a fee until `12_ECONOMY_AND_REWARDS` closes it.
