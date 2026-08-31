# Diyse — Equipment System Master
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary written equipment authority:** compatible **Audit117 / Audit118 / Audit121**, plus newer accepted v85 tracker-level equipment closures.  
**Current written whole-project authority:** **v2.20 / Audit135**.  
**Rule:** where v85 contains a later explicitly accepted equipment decision that has not yet been promoted, preserve it as **tracker-level final / pending formal promotion** rather than rewriting older audit history.


## Functional equipment slots

Exactly:
1. **Weapon**
2. **Secondary**
3. **Armor**

There is no fourth generic Accessory slot.

## One-slot versus two-slot weapons

A one-slot Primary uses Weapon and leaves Secondary available.

A two-slot weapon uses:
> **Weapon + Secondary**

and therefore prevents a Shield or Focus from being equipped simultaneously.

## Current native weapon families

| Character | Native Base weapon family | Slot behavior |
|---|---|---|
| Cyanis | Sword | Weapon |
| Ilyra | Wardrod | Weapon |
| Torren | Great Bow | Weapon + Secondary |
| Nimera | Conduit | normally Weapon; specific two-handed Conduits may use Weapon + Secondary |
| Vaelira | Arcane Staff | Weapon |
| Seyrik | Two-Handed Sword | Weapon + Secondary |

## Secondary equipment

Current active Secondary families:
- Shield
- Focus

Ilyra:
- Wardrod is Primary;
- Shield **or** Focus may occupy Secondary;
- Shield and Focus cannot be equipped simultaneously.

Vaelira:
- Arcane Staff remains one-slot Primary;
- Focus remains legal in Secondary.

## Persistent legality

Once legal equipment access is unlocked, changing selected class does not silently erase already-established legal equipment access under the current class/equipment architecture.

Exact donor unlock timing is referenced from `06_CLASSES_AND_ABILITIES`.

## Equipment does not choose Ability formula

An equipped weapon does not silently change a learned Ability between Physical/Magical/Hybrid.

Individual equipment Traits may modify an eligible action only where explicitly authored.

## Action-Speed firewall

**Action Speed is not an active Diyse combat mechanic.**

Equipment may legally provide:
- persistent raw **SPD**;
- temporary or conditional **Speed ±N%** that resolves through `05_BATTLE_SYSTEM/STAT_CHANGES.md`;
- an explicitly supported action-local bonus such as Base Hit, Evasion, application reliability, MP-cost reduction, healing potency, damage, penetration, or direct-damage reduction;
- a specifically authored initiative-routing effect only where the battle-system owner explicitly supports it.

Equipment may **not** provide:
- `action Speed`;
- cast speed;
- per-action priority;
- a hidden initiative multiplier;
- mid-round turn-order reshuffling merely because one selected action is described as faster.

A legal Speed modifier applied after the current round's initiative is fixed does not move that action earlier in the current round. If the Speed modifier remains active at the next normal-round initiative setup, it affects ordering there normally.

Historical/current migrated equipment wording that used `action Speed` is retired and must be normalized to one of the supported mechanics above rather than implemented as a new subsystem.

## Max HP / Max MP equipment bonuses

Equipment bonuses to **Max HP** and **Max MP** are persistent flat raw additions.

Use:
- `Max HP +N`
- `Max MP +N`

Do not use percentage-based Max HP / Max MP equipment bonuses under the current system.

These flat bonuses:
- are added after Player-Level natural stat calculation and selected-class HP/MP multiplier resolution;
- stack additively across legally equipped items;
- are not temporary stat changes;
- do not use the temporary core-stat ±40% cap.

Exact current conversions and construction details are owned by `HP_MP_FLAT_BONUS_RULES.md`.

## Count firewall

Current equipment:
- 38 ordinary
- 36 Relics
- 17 Legacies
- 91 total

Do not restore:
- the 12 former Subclass Relics;
- six separate shared-Legacy artifacts;
- generic Accessory inventory as a fourth equipment slot.
