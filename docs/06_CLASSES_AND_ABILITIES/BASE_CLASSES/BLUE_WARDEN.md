# Diyse — Blue Warden
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Master-canon class/resource authority:** **v2.08 / Audit123**, with compatible **Audit115** class normalization and later current working corrections, including the approved 2026-08-30 Ability-MP reduction.  
**Authority treatment:** explicit/newer working corrections are preserved as working overrides when they have not yet been promoted into the audit chain.


**Owner:** Ilyra  
**Class line:** Native Base Class  
**Identity:** healer/protector; Magic-based healing with balanced defenses  
**Trait:** **Gentle Continuance**  
**Ultimate:** **Dawn Without End**

## Ability spine
| Unlock | Ability | MP | Current effect |
|---:|---|---:|---|
| CL1 | **Mend** | 14 | **Power: N/A — no direct damage.** One conscious ally; direct healing: **22% target Max HP + 1.50 × Ilyra's Magic**. |
| CL1 | **Clear Warding** | 15 | **Power: N/A — no direct damage.** One conscious ally; remove **1 eligible universal harmful status**, grant **+5 Status Resistance for 2 rounds**, and restore **5% target Max HP**. |
| CL1 | **Renewal** | 22 | **Power: N/A — no direct damage.** All conscious active-party allies restore **10% target Max HP + 0.90 × Ilyra's Magic**. Does not automatically grant Regen. |
| CL3 | **Warden's Valor** | 15 | One enemy; Magical / Colorless; **170 Power**; no healing, status, or defensive rider. |
| CL6 | **Revive** | 29 | **Power: N/A — no direct damage.** One KO active permanent-party ally; return the target at **35% Max HP**. Cannot target summons, devices, or Prime manifestations. |
| CL9 | **Lifeline** | 34 | **Power: N/A — no direct damage.** One conscious active-party ally; establish **Lifeline Prepared** immediately through the end of the following normal round. The first eligible damage instance during that window that would reduce the target to 0 HP instead leaves the target at **1 HP**, then immediately restores **18% target Max HP + 0.80 × Ilyra's Magic**. Triggers once and is consumed. |
| CL13 | **Dawn Without End** | 51 | Base Ultimate; all enemies; Magical / Colorless; **220 Power per target**. After enemy damage resolves: revive up to **2 selected KO active permanent-party allies at 30% Max HP**; then every conscious active permanent-party member, including allies just revived, restores **20% target Max HP + 1.50 × Ilyra's Magic**, removes **all eligible universal harmful statuses**, and gains **Regen: 5% Max HP per round for 3 rounds**. |

## Lifeline Prepared rules
Lifeline is an authored Prepared protection state, not a universal harmful/beneficial status category.

- It becomes active when Lifeline resolves.
- It lasts through the **end of the following normal round** if unused.
- It protects against the first otherwise-legal damage instance that would reduce the protected ally to 0 HP, unless that damage is explicitly scripted/unpreventable by its own owner.
- On trigger, the protected ally remains at 1 HP before Lifeline's emergency recovery is applied.
- The triggering damage does not continue below 1 HP after Lifeline activates.
- The state is consumed after that one successful prevention/recovery trigger.
- Recasting Lifeline on the same ally while it is already active refreshes the window; it does not create multiple pending protections.
- A different ally may have their own Lifeline state from a separate legal cast.
- Lifeline cannot trigger while the protected party member is suspended by an Awakened Prime because that party member cannot be targeted during Prime rounds; its normal-round expiry clock follows the global Prime tactical-state pause rule.

## Dawn Without End resolution order
Resolve the Ultimate in this order:
1. resolve the **220-Power Magical / Colorless** hit against all enemies;
2. choose and revive up to **2 KO active permanent-party allies** at 30% Max HP;
3. heal every conscious active permanent-party member for **20% Max HP + 1.50 × Ilyra's Magic**;
4. remove all eligible universal harmful statuses from those conscious party members;
5. apply **5% Max-HP Regen for 3 rounds** to those conscious party members.

Dawn Without End does not revive summons, devices, Prime manifestations, or permanent characters who are not part of the active battle party.

## Masteries
| Unlock | Mastery | Current effect |
|---:|---|---|
| CL3 | **Gentle Hands** | Mend gains +10% healing potency. |
| CL6 | **Clear Heart** | Clear Warding additionally removes **1 eligible ordinary negative stat change**. |
| CL9 | **Restored Breath** | Revive recovery 35% → **45% target Max HP**. |
| CL12 | **Stronger Lifeline** | Lifeline emergency Max-HP heal component 18% → **23%**; +0.80 × Magic remains unchanged. |

All four Core Masteries unlock automatically at the listed Class Levels under the current v85 working override.


## Global references
- Damage/penetration: `05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md`
- Hit/Evasion: `05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md`
- Critical: `05_BATTLE_SYSTEM/CRITICAL_HITS.md`
- Elements/statuses: `05_BATTLE_SYSTEM/ELEMENTS.md` and `STATUS_EFFECTS.md`
- Turn/round and Prepared timing: `05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md`

## Firewall
Do not restore older Warden's Valor support/action-modification wording; the current Warden's Valor is the authored **170-Power Magical / Colorless offensive Ability** above. Do not restore Poison or obsolete harmful-status lists to Blue Warden support effects.
