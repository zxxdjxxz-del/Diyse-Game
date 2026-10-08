# Diyse — Class State Lifecycle

**Status:** ACTIVE STRUCTURAL RULE / EXACT STATES OPEN  
**Authority:** current class-domain owner plus `../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`.

Class kits may author temporary setup, stance, prepared-reaction, link, record, or other tactical states.

No exact class-authored state package is currently locked while the class kits are being rebuilt.

Any future class-authored state must explicitly define:

- what unit/object carries the state;
- creation trigger;
- duration in current TURN-based terms;
- refresh/reapplication behavior;
- consumption/trigger behavior;
- KO/incapacitation behavior;
- battle-end clearing;
- enemy body/form replacement behavior;
- interaction with Prime suspension;
- whether ordinary cleanse or susceptibility applies.

Class states must not silently create new universal gauges, stats, status families, or a separate timing system.

Prime-local state behavior remains owned by `../07_CARDS/PRIME_CARDS/PRIME_SYSTEM_RULES.md`.
