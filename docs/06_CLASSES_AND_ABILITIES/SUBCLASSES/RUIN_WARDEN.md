# Diyse — Ruin Warden
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Master-canon class/resource authority:** **v2.08 / Audit123**, with compatible **Audit115** class normalization and later current working corrections.  
**Authority treatment:** explicit/newer working corrections are preserved as working overrides when they have not yet been promoted into the audit chain.


**Owner:** Seyrik  
**Donor tradition:** Blue Warden  
**Identity:** slow preservation-oriented Ruin/healing hybrid with balanced defenses  
**Trait:** **Ruin's Mercy**  
**Ultimate:** **Mercy Through Ruin**

## Ability spine
| Unlock | Ability | MP | Current effect |
|---:|---|---:|---|
| CL1 | **Siphon Rune** | 16 | One enemy; Hybrid / Ruin 75/25; 165 Power; self-heal 35% eligible damage, capped at 20% Max HP; no Bleed; `Rune` is flavor only. |
| CL4 | **Stolen Grace** | 20 | One enemy; Magical / Colorless; 170 Power; heal other lowest-HP conscious ally for 30% eligible damage + 0.35 × Magic, capped at 25% target Max HP. |
| CL7 | **Restoring Ward** | 22 | One ally; heal 18% Max HP + 0.90 × Magic; remove 1 harmful status; +10 Total Defense through end next round. |
| CL9 | **Withering Mercy** | 34 | All enemies; Magical / Earth; 150 Power; 20% Staggered; recovery pool = 12% total eligible HP damage split across conscious party, each capped at 15% Max HP. |
| CL11 | **Reclaimed Breath** | 38 | Revive one KO ally at 25% Max HP. |
| CL13 | **Mercy Through Ruin** | 64 | Subclass Ultimate; all enemies; Hybrid / Ruin 75/25; 320 Power; allies heal 25% Max HP + 1.00 × Magic, cleanse 1 harmful status, and gain +20 Total Defense for 2 rounds. |

## Masteries
| Unlock | Mastery | Current effect |
|---:|---|---|
| CL3 | **Deeper Siphon** | Siphon Rune recovery 35% → 40% of eligible damage; 20% Max-HP cap unchanged. |
| CL5 | **Shared Grace** | Stolen Grace Magic coefficient 0.35 → 0.45; 25% target-Max-HP cap unchanged. |
| CL7 | **Equipment Mastery** | Unlocks class eligibility for the donor **Blue Warden Relic**, subject to actual Relic ownership and other established requirements. |
| CL11 | **Legacy Mastery** | Unlocks class eligibility for the donor **Blue Warden Legacy**, subject to donor Legacy completion/ownership and other established requirements. |

The previous third mechanical Subclass Mastery and old fourth-node Equipment-Mastery layout are historical. Current v85 structure is two mechanical Masteries → Equipment Mastery → Legacy Mastery, with no Mastery Point cost.

## Trait ranks
- Rank I: when Seyrik's Drain heals himself, heal other lowest-HP conscious ally for 15% of the HP actually restored.
- Rank II: shared amount 15% → 25%.
- Rank III: whenever a Ruin Warden Ability restores HP to a conscious ally, that ally gains +10 Status Resistance through end following round; refreshes, does not stack; revival itself does not trigger it.

## Global references
- Damage/penetration: `05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md`
- Hit/Evasion: `05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md`
- Critical: `05_BATTLE_SYSTEM/CRITICAL_HITS.md`
- Elements/statuses: `05_BATTLE_SYSTEM/ELEMENTS.md` and `STATUS_EFFECTS.md`

## Firewall
Do not restore removed historical mechanics merely because an archived version of this class used them.
