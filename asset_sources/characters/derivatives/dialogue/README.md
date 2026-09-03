# Diyse Dialogue Portrait Derivatives

Production dialogue portraits/busts belong here after they are derived from and approved against the current character masters in `../../current/`.

## Runtime contract

Dialogue data uses stable **character ID + expression ID** through `DiyseDialoguePortraitRegistry`. Do not author scene data against final image paths.

Existing proof IDs demonstrate the semantic pattern:
- Cyanis: `neutral`, `amused`
- Torren: `neutral`, `dry`

Those proof expressions are not a requirement that every character receive the same expression set. Add production expressions when authored scenes need them.

Preferred approved export filename pattern:
`<character_id>_<expression_id>.png`

Final pixel dimensions are not locked here. Validate framing at the actual dialogue presentation scale; current Dialogue UI authority calls for large high-resolution portraits generally around 35–45% of screen height where practical.

## Required provenance record

For each approved file, record alongside the production manifest/review:
- character ID;
- expression ID;
- source master path/fingerprint;
- output dimensions;
- crop/framing;
- transparency/background treatment;
- orientation requirements;
- approval status.

Do not place current B00 master images here as copies. This lane contains derivatives only.
