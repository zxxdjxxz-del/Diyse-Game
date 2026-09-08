# 01_CHARACTERS

**Status:** ACTIVE CHARACTER-INFORMATION AUTHORITY  
**Domain rule:** this folder owns character identity, biography, chronology, personality, relationship logic, recruitment/party status, character-arc anchors, **ordinary-life behavior**, and concise voice direction.

## What belongs here
- identity and role;
- age/chronology;
- background and formative history;
- personality;
- values, flaws, fears, contradictions;
- relationship logic;
- ordinary-life behavior, interests, habits, humor, irritations, and social tendencies when established;
- state-sensitive behavior such as how fatigue/anger/fear pressure a character without replacing personality;
- character-specific knowledge/expertise boundaries;
- recruitment/party status;
- concise voice shorthand;
- current character-arc anchors.

## What does not belong here
- Ability numbers, Traits, Masteries, exact class mechanics → `06_CLASSES_AND_ABILITIES`
- Card/Prime command details → `07_CARDS`
- equipment stats → `08_ITEMS_AND_EQUIPMENT`
- boss raw stats → `09_ENEMIES_AND_ENCOUNTERS`
- full scene/dialogue scripts → `03_DIALOGUE`
- exact visual appearance/turnarounds/color specifications → `14_ART_AND_VISUALS`
- global lived-world conditions → `04_WORLD_AND_LORE/LIVED_WORLD_SOCIAL_CONTEXT.md`
- prices/commerce/economic calibration → `12_ECONOMY_AND_REWARDS`

## Permanent playable roster
Exactly six:
1. Cyanis
2. Ilyra
3. Torren
4. Nimera
5. Vaelira
6. Seyrik

Current files:
- `PLAYABLE/Cyanis.md`
- `PLAYABLE/Ilyra.md`
- `PLAYABLE/Torren.md`
- `PLAYABLE/Nimera.md`
- `PLAYABLE/Vaelira.md`
- `PLAYABLE/Seyrik.md`

These files are also the primary character-personality/lived-person source used to build the Dialogue Engine runtime brain syntheses. The runtime YAMLs do not outrank these files.

Do **not** infer or restore surnames for the permanent six from superseded migration files.

Maevra is recurring/temporary/guest where authored and is never a seventh permanent member. Kessara is a major recurring **nonplayable** supporting character. Their current files are `SUPPORTING/Maevra.md` and `SUPPORTING/Kessara.md`; do not restore retired migration surnames for them either.

## Relationship authority
Permanent-six pair logic and conversational geometry are routed through:
> `RELATIONSHIPS/PERMANENT_SIX_RELATIONSHIP_MAP.md`

That map preserves all 15 pair languages while exact spoken wording remains owned by `03_DIALOGUE`.

## Cross-domain current authority
- roster/name/biography/personality/lived-person authority: this folder;
- exact class mechanics: `06_CLASSES_AND_ABILITIES`;
- Face/Card/Prime mechanics: `07_CARDS`;
- exact current visual masters: `14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/README.md` and `asset_sources/characters/current/`;
- Dialogue Engine architecture: `03_DIALOGUE/AGENT_SYSTEM/README.md`.

When stale migration text conflicts with a newer explicit correction, preserve compatible character truth but replace the stale name/system label. See `CHARACTER_AUTHORITY_BOUNDARIES.md`.
