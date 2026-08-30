# Diyse — Battle System Master
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current domain authority checked:** repository `docs/COMBAT_RULES.md`, current through **v2.20 / Audit135**, plus compatible Audit115, Audit120, Audit122, Audit135.  
**Migration rule:** current master canon outranks stale/open wording inherited by v85.


## Scope

This folder is the canonical home for global combat rules shared by characters, enemies, Cards, equipment, and encounters.

It owns:
- round and action-order rules;
- global commands;
- targeting / automatic retargeting;
- Physical / Magical / Hybrid damage resolution;
- penetration;
- Base Hit / Evasion;
- Critical Hits;
- the four standard elements;
- universal harmful statuses;
- Status Resistance;
- Guard as a legal defensive state;
- global boss fresh-body / same-bar distinction;
- removed-system firewalls.

It does **not** own:
- individual character Ability kits → `06_CLASSES_AND_ABILITIES`;
- Standard/Prime Card catalogs → `07_CARDS`;
- item/equipment catalogs → `08_ITEMS_AND_EQUIPMENT`;
- enemy kits or encounter-specific stats → `09_ENEMIES_AND_ENCOUNTERS`;
- EXP/CEXP/level progression → `10_PROGRESSION_AND_EXP`.

## Current top-level battle constants

- Presentation target: **HD-2D**
- Active permanent party: **4**
- Maximum simultaneously active enemies: **8**
- Permanent commands:
  - Attack
  - Ability
  - Card
  - Item
  - Defend
- Speed determines action order; it does **not** grant extra ordinary actions.
- MP is the universal ordinary Ability resource.
- No natural `Accuracy` stat exists.
- Standard elements: **Fire / Ice / Lightning / Earth**
- Universal harmful statuses: **Burn / Freeze / Stun / Staggered / Bleed**
- Ruin is a **special affinity/school**, not a fifth standard element.

## Current battle execution references

See:
- `TURN_AND_ROUND_RULES.md`
- `TARGETING_AND_RETARGETING.md`
- `DAMAGE_FORMULAS.md`
- `BASE_HIT_AND_EVASION.md`
- `CRITICAL_HITS.md`
- `ELEMENTS.md`
- `STATUS_EFFECTS.md`
- `GUARD.md`
- `BOSS_FORM_RULES.md`
- `REMOVED_SYSTEMS_FIREWALL.md`

## Important v85 reconciliation

Several v85 statements were superseded by later/current master-canon documents even though they remain visible in tracker history.

Current corrections used in this folder:
- the **Class Ability MP certification is CLOSED** under Audit123; it is not an open Battle-System item;
- the old generic percentage-based status-susceptibility table is **not** a second universal status resolver;
- current general **Status Resistance** uses the 0 / 5 / 10 / 15 raw-stat bands;
- **Barrier is removed** globally;
- **Brace is removed**;
- the global **Break/Stagger meter is removed**;
- **Staggered** remains a normal harmful status;
- current Bleed cadence/clearing follows Audit122, not Audit115's older one-proc/any-heal rules; **v96 uses 3% Max HP per qualifying proc initially, escalating to 4% after the affected unit completes 3 turns without Bleed being removed**.

## Cross-domain rule

When another folder needs a global battle rule, it should reference this folder rather than restating a second editable copy.
