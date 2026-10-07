# Diyse — Damage and Healing Formula Route

**Status:** ROUTING SURFACE  
**Authority:** `BATTLE_SYSTEM_MASTER.md`

Current formula authority is owned by `BATTLE_SYSTEM_MASTER.md`, especially:

- §6 Core combat stats
- §7 Equipment
- §8 Damage, healing, potency, variance, and caps
- §9 Critical hits and hit rules
- §10 Elements
- §15 Queued-action evaluation
- §18 Battle victory, defeat, escape, revival, and simultaneous outcomes
- §19 Reactions, counters, Reflect, and redirection

Current scalable damage architecture:

`Base Damage = Potency × Offensive Stat × (K / (K + Defensive Stat))`

with current design target **K = 300**.

Do not define a second damage/healing formula or hidden weapon-power layer here.
