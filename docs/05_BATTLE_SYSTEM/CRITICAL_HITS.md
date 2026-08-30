# Diyse — Critical Hits
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current domain authority checked:** repository `docs/COMBAT_RULES.md`, current through **v2.20 / Audit135**, plus compatible Audit115, Audit120, Audit122, Audit135.  
**Migration rule:** current master canon outranks stale/open wording inherited by v85.


## Global values

Base Critical Chance:
# **5%**

Ordinary random Critical Chance cap:
# **50%**

Eligible Critical multiplier:
# **1.5×**

Critical Chance bonuses are flat **percentage-point additions**.

## Resolution order

1. Resolve Base Hit / Evasion.
2. Miss → no Critical roll.
3. Hit → roll Critical if the hit is eligible.
4. Successful Critical → multiply eligible resolved direct damage by **1.5×**.

A Critical:
- does not ignore Defense;
- does not ignore Spirit;
- does not use a second damage formula;
- does not automatically improve harmful-status application.

## Multihit

Each authored direct hit rolls Critical independently by default unless the action explicitly defines one shared Critical roll.

## Hybrid

One authored Hybrid hit uses **one Critical roll** on its combined eligible Physical + Magical direct-damage result.

Do not roll separately for the internal Physical and Magical components.

## Magical Crits

Eligible Magical direct hits use the same **1.5×** multiplier.

## Cannot Crit

At minimum:
- Burn;
- Bleed;
- explicitly no-Crit copied/echo damage;
- indirect Max-HP damage unless explicitly authored otherwise;
- healing.
