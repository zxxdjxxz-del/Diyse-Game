shader_type canvas_item;

uniform float motion_strength : hint_range(0.0, 2.0) = 0.9;
uniform float motion_enabled : hint_range(0.0, 1.0) = 1.0;

void vertex() {
	float strength = motion_strength * motion_enabled;
	float top_weight = 1.0 - smoothstep(0.72, 0.98, UV.y);
	float breath = sin(TIME * 1.75);
	float sway = sin(TIME * 0.95);

	// Keep the feet visually planted while the upper body shifts its weight.
	VERTEX.x += sway * 8.0 * top_weight * strength;

	// Very small chest/ribcage expansion. This is intentionally restrained.
	float torso_y = exp(-pow((UV.y - 0.46) / 0.18, 2.0));
	float torso_center = 1.0 - smoothstep(0.16, 0.48, abs(UV.x - 0.5));
	VERTEX.x += (UV.x - 0.5) * 13.0 * breath * torso_y * torso_center * strength;
	VERTEX.y -= 1.8 * breath * torso_y * strength;

	// Secondary motion proxy for long hair / cape edges. A segmented production
	// rig will replace this region-based deformation with dedicated pieces.
	float outer = smoothstep(0.22, 0.48, abs(UV.x - 0.5));
	float secondary_zone = outer * (1.0 - smoothstep(0.68, 0.94, UV.y));
	float flutter = sin(TIME * 2.05 + UV.y * 11.0 + UV.x * 5.0);
	VERTEX.x += flutter * 4.0 * secondary_zone * strength;
	VERTEX.y += cos(TIME * 1.82 + UV.x * 8.0) * 1.0 * secondary_zone * strength;
}
