# Diyse — Status Application Route

**Status:** ROUTING SURFACE  
**Authority:** `BATTLE_SYSTEM_MASTER.md` §11

Current universal chance-based status application uses:

`final application chance = action base chance × target susceptibility`

Susceptibility:

- Vulnerable ×1.5
- Normal ×1.0
- Resistant ×0.5
- Immune ×0

Final chance caps at 100%.

Individual effects may explicitly modify a chance or guarantee/prevent an application, but this file must not define a second global resolver.
