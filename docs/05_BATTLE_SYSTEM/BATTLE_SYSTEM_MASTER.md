# Diyse — Battle System Master
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current domain authority checked:** repository `docs/COMBAT_RULES.md`, current through **v2.20 / Audit135**, plus compatible Audit115, Audit120, Audit122, Audit135 and newer explicit user corrections.  
**Migration rule:** current explicit user corrections and current organized domain canon outrank stale/open wording inherited by v85.


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
- Battle flow uses **discrete rounds**, not ATB.
- Normal turn order is established at round start from current effective **Speed** and tie rules.
- A player action is selected **when that character's turn arrives** and then resolves immediately before the next normal turn.
- Enemy AI likewise selects its action when that enemy/entity turn arrives from the current legitimate battle state.
- There is **no full-party command queue** and no universal **Confirm Round** step.
- **Item** and **Defend** do not have separate universal priority phases; they resolve on the acting character's normal Speed-ordered turn.
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

## Important reconciliation

Several older tracker/master-canon statements remain visible in project history but are superseded by current organized-domain authority and newer explicit corrections.

Current corrections used in this folder:
- normal combat remains round-based, but the old whole-party command-lock / Confirm-Round flow is retired;
- the old Item-first / Defend-second universal action phases are retired;
- the **Class Ability MP certification** was superseded by the approved 2026-08-30 15% Ability-MP reduction owned by `06_CLASSES_AND_ABILITIES`;
- the old generic percentage-based status-susceptibility table is **not** a second universal status resolver;
- current general **Status Resistance** uses the 0 / 5 / 10 / 15 raw-stat bands;
- **Barrier is removed** globally;
- **Brace is removed**;
- the global **Break/Stagger meter is removed**;
- **Staggered** remains a normal harmful status;
- current Bleed cadence/clearing follows the latest active rule: **3% Max HP per qualifying proc initially, escalating to 4% after the affected unit completes 3 turns without Bleed being removed**, with the established round tick + action tick cadence.

## Cross-domain rule

When another folder needs a global battle rule, it should reference this folder rather than restating a second editable copy.
