# Diyse — Class Ability MP Balance

**Status:** ACTIVE MP-BALANCE REGRESSION CHECKLIST  
**Class/MP authority:** `../../06_CLASSES_AND_ABILITIES/`

Exact Ability/Ultimate identities, base MP costs, and class-authored cost modifiers are owned by `06_CLASSES_AND_ABILITIES`. This file does not freeze a second copy of those numbers.

## Verify

For every current MP-costing Ability/Ultimate:
- use is rejected below required MP;
- exact current authored base cost is consumed on legal use;
- unlocked class modifiers apply only when their owning rules allow;
- minimum-cost clamps are respected where authored;
- cost modifiers do not rewrite the stored authored base cost;
- MP validation consults only resources that exist in current class/battle authority.

## Progression boundary

Ability MP validation is separate from campaign CEXP placement.

Current campaign EXP/CEXP placement is **rebuild-pending**; the full Base + Subclass completion target remains **Lv55–60**.
