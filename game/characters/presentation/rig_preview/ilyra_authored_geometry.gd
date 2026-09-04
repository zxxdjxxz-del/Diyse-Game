extends "res://game/characters/presentation/rig_preview/ilyra_modular_blockout.gd"

# Stage 5: repo-safe authored-geometry proof.
# Keeps the ResourceLoader-based UAL chain and replaces the most obvious primitive
# silhouette pieces with custom triangle meshes. The approved Ilyra B00 remains authority.

var authored_cape_pivots: Array[Node3D] = []
var authored_hair_pivots: Array[Node3D] = []
var authored_tabard_pivots: Array[Node3D] = []
var _authored_attachments: Array[BoneAttachment3D] = []
var _authored_visible := true
var _auto_turntable := false
var _authored_hair: StandardMaterial3D

func _apply_proxy_style() -> void:
	super._apply_proxy_style()
	if _proxy_skeleton == null:
		return
	for attachment in _detail_attachments:
		attachment.visible = false
	_hide_old_proxy_layers()
	_authored_hair = _material(Color(0.93, 0.79, 0.43), 0.58, 0.0)
	_build_authored_head()
	_build_authored_hair()
	_build_authored_torso()
	_build_authored_waist()
	_build_authored_cape()
	_build_hard_gear()

func _hide_old_proxy_layers() -> void:
	var old_names := ["IlyraHair", "IlyraCape", "IlyraUtility", "IlyraWardrod", "IlyraShield"]
	for child in _proxy_skeleton.get_children():
		if child is Node3D and old_names.has(str(child.name)):
			(child as Node3D).visible = false

func _process(delta: float) -> void:
	super._process(delta)
	if _auto_turntable and actor != null and not _paused:
		actor.rotate_y(deg_to_rad(18.0 * delta))

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo:
		if event.keycode == KEY_T:
			_auto_turntable = not _auto_turntable
			_update_hud(_current_label(), str(animation_player.current_animation) if animation_player != null else "none")
			return
		if event.keycode == KEY_V:
			_authored_visible = not _authored_visible
			for attachment in _authored_attachments:
				if is_instance_valid(attachment):
					attachment.visible = _authored_visible
			_update_hud(_current_label(), str(animation_player.current_animation) if animation_player != null else "none")
			return
	super._unhandled_input(event)

func _current_label() -> String:
	if _clip_index < 0 or _clip_index >= ILYRA_DEMO_CLIPS.size():
		return "Ready"
	return str(ILYRA_DEMO_CLIPS[_clip_index]["label"])

func _build_authored_head() -> void:
	var head := _authored_attachment("Ilyra_Head_Authored", "Head")
	if head == null:
		return
	var face := MeshInstance3D.new()
	face.name = "AnimeFaceMesh"
	face.mesh = _ring_mesh([
		Vector4(-0.135, 0.050, 0.060, 0.000), Vector4(-0.095, 0.082, 0.080, 0.008),
		Vector4(-0.035, 0.108, 0.098, 0.012), Vector4(0.035, 0.124, 0.106, 0.006),
		Vector4(0.105, 0.108, 0.102, -0.002), Vector4(0.155, 0.072, 0.082, -0.010)
	], 12)
	face.material_override = _skin
	face.position = Vector3(0.0, 0.016, 0.010)
	head.add_child(face)
	var eye_white := _material(Color(0.97, 0.97, 0.95), 0.52, 0.0)
	for x in [-0.037, 0.037]:
		head.add_child(_sphere("EyeWhite", Vector3(x, 0.041, 0.111), Vector3(0.021, 0.012, 0.006), eye_white))
		head.add_child(_sphere("JadeIris", Vector3(x, 0.041, 0.118), Vector3(0.010, 0.010, 0.004), _jade))

func _build_authored_hair() -> void:
	var head := _authored_attachment("Ilyra_Hair_Authored", "Head")
	if head == null:
		return
	var cap := MeshInstance3D.new()
	cap.name = "HairCapMesh"
	cap.mesh = _ring_mesh([
		Vector4(-0.090, 0.125, 0.112, -0.012), Vector4(-0.010, 0.145, 0.132, -0.022),
		Vector4(0.085, 0.148, 0.137, -0.028), Vector4(0.165, 0.095, 0.105, -0.035)
	], 14)
	cap.material_override = _authored_hair
	cap.position = Vector3(0.0, 0.030, -0.020)
	head.add_child(cap)
	var specs := [
		[Vector3(-0.11,-0.02,-0.05), Vector3(-0.13,-0.18,-0.07), Vector3(-0.18,-0.46,-0.05)],
		[Vector3(-0.04,-0.03,-0.10), Vector3(-0.06,-0.22,-0.12), Vector3(-0.10,-0.58,-0.09)],
		[Vector3(0.03,-0.03,-0.11), Vector3(0.04,-0.23,-0.13), Vector3(0.09,-0.60,-0.09)],
		[Vector3(0.10,-0.02,-0.07), Vector3(0.13,-0.18,-0.08), Vector3(0.21,-0.46,-0.03)]
	]
	for i in range(specs.size()):
		var pivot := Node3D.new()
		pivot.name = "HairLockPivot_%02d" % i
		head.add_child(pivot)
		var lock := MeshInstance3D.new()
		lock.name = "WindsweptHairLock_%02d" % i
		lock.mesh = _ribbon_mesh(specs[i], [0.050, 0.038, 0.010])
		lock.material_override = _authored_hair
		pivot.add_child(lock)
		authored_hair_pivots.append(pivot)

func _build_authored_torso() -> void:
	var chest := _authored_attachment("Ilyra_Torso_Authored", "spine_03")
	if chest == null:
		return
	chest.add_child(_box("IvoryWardenVest", Vector3(0,-0.105,0.035), Vector3(0.31,0.35,0.15), _ivory))
	chest.add_child(_box("PaleBlueCenterPanel", Vector3(0,-0.105,0.116), Vector3(0.075,0.30,0.012), _pale_blue))
	chest.add_child(_box("HighBlueCollar", Vector3(0,0.085,0.030), Vector3(0.20,0.08,0.13), _deep_blue))
	chest.add_child(_sphere("CapeClasp", Vector3(0,0.028,0.121), Vector3(0.029,0.029,0.014), _silver))

func _build_authored_waist() -> void:
	var pelvis := _authored_attachment("Ilyra_Waist_Authored", "pelvis")
	if pelvis == null:
		return
	pelvis.add_child(_box("LeatherBelt", Vector3(0,0.02,0), Vector3(0.38,0.055,0.17), _leather))
	pelvis.add_child(_box("LeftPouch", Vector3(-0.205,-0.05,0.02), Vector3(0.10,0.13,0.08), _leather))
	pelvis.add_child(_box("RightUtility", Vector3(0.205,-0.065,0), Vector3(0.08,0.11,0.07), _leather))
	for spec in [["FrontIvoryTabard",0.0,0.145,0.075,0.43,_ivory],["FrontBlueInset",0.0,0.066,0.032,0.365,_pale_blue],["LeftLayer",-0.137,0.12,0.07,0.335,_ivory],["RightLayer",0.137,0.12,0.07,0.335,_pale_blue]]:
		var pivot := Node3D.new()
		pivot.name = str(spec[0]) + "Pivot"
		pivot.position = Vector3(float(spec[1]), -0.105, 0.12 if float(spec[1]) == 0.0 else 0.03)
		pelvis.add_child(pivot)
		var panel := MeshInstance3D.new()
		panel.name = str(spec[0])
		panel.mesh = _tapered_panel(float(spec[2]), float(spec[3]), float(spec[4]))
		panel.material_override = spec[5]
		panel.position.y = -float(spec[4]) * 0.43
		pivot.add_child(panel)
		authored_tabard_pivots.append(pivot)

func _build_authored_cape() -> void:
	var chest := _authored_attachment("Ilyra_Cape_Authored", "spine_03")
	if chest == null:
		return
	chest.add_child(_box("CapeShoulderMantle", Vector3(0,0.02,-0.12), Vector3(0.45,0.14,0.05), _pale_blue))
	var panels := [
		[[Vector3(0,0,0),Vector3(0,-0.24,-0.015),Vector3(0.01,-0.48,-0.02)],[0.22,0.21,0.18]],
		[[Vector3(0,-0.42,0),Vector3(-0.02,-0.66,-0.02),Vector3(-0.04,-0.86,-0.01)],[0.18,0.16,0.11]],
		[[Vector3(-0.03,-0.78,0),Vector3(-0.06,-0.98,0.01),Vector3(-0.09,-1.13,0.03)],[0.12,0.09,0.02]]
	]
	for i in range(panels.size()):
		var pivot := Node3D.new()
		pivot.name = "CapeAuthoredPivot_%02d" % i
		pivot.position = Vector3(0, -0.08 if i == 0 else 0, -0.145)
		chest.add_child(pivot)
		var mesh := MeshInstance3D.new()
		mesh.name = "CapeCloth_%02d" % i
		mesh.mesh = _ribbon_mesh(panels[i][0], panels[i][1])
		mesh.material_override = _pale_blue
		pivot.add_child(mesh)
		authored_cape_pivots.append(pivot)

func _build_hard_gear() -> void:
	for side in ["l","r"]:
		var arm := _authored_attachment("Ilyra_Authored_Bracer_%s" % side, "lowerarm_%s" % side)
		if arm != null:
			arm.add_child(_cylinder("SilverBracer", Vector3(0,-0.12,0), 0.05, 0.22, _silver))
		var calf := _authored_attachment("Ilyra_Authored_Greave_%s" % side, "calf_%s" % side)
		if calf != null:
			calf.add_child(_box("SilverGreave", Vector3(0,-0.18,0.025), Vector3(0.115,0.31,0.075), _silver))
	var right := _authored_attachment("Ilyra_Wardrod_Authored", "hand_r")
	if right != null:
		right.add_child(_cylinder("Wardrod", Vector3(0,-0.31,0.02), 0.021, 0.70, _silver))
		right.add_child(_sphere("WardrodFocus", Vector3(0,-0.66,0.02), Vector3(0.05,0.075,0.025), _pale_blue))
	var left := _authored_attachment("Ilyra_Shield_Authored", "hand_l")
	if left != null:
		var shield := MeshInstance3D.new()
		shield.name = "WardenShield"
		shield.mesh = _extruded_outline([Vector2(0,0.25),Vector2(0.17,0.17),Vector2(0.20,0),Vector2(0.13,-0.18),Vector2(0,-0.255),Vector2(-0.13,-0.18),Vector2(-0.20,0),Vector2(-0.17,0.17)],0.035)
		shield.material_override = _silver
		shield.position = Vector3(-0.035,-0.02,0.135)
		left.add_child(shield)

func _authored_attachment(node_name: String, bone_name: String) -> BoneAttachment3D:
	if _proxy_skeleton == null or _proxy_skeleton.find_bone(bone_name) < 0:
		return null
	var attachment := BoneAttachment3D.new()
	attachment.name = node_name
	attachment.bone_name = bone_name
	_proxy_skeleton.add_child(attachment)
	_authored_attachments.append(attachment)
	return attachment

func _ring_mesh(rings: Array[Vector4], segments: int) -> ArrayMesh:
	var v: Array[Vector3] = []
	for ring in rings:
		for i in range(segments):
			var a := TAU * float(i) / float(segments)
			v.append(Vector3(cos(a)*ring.y, ring.x, sin(a)*ring.z + ring.w))
	var idx: Array[int] = []
	for r in range(rings.size()-1):
		for i in range(segments):
			var n := (i+1)%segments
			var a := r*segments+i
			var b := r*segments+n
			var c := (r+1)*segments+n
			var d := (r+1)*segments+i
			idx.append_array([a,c,b,a,d,c])
	return _array_surface(v,idx)

func _ribbon_mesh(points: Array, widths: Array) -> ArrayMesh:
	var v: Array[Vector3] = []
	for i in range(points.size()):
		var p: Vector3 = points[i]
		var w := float(widths[i])
		v.append(Vector3(p.x-w,p.y,p.z))
		v.append(Vector3(p.x+w,p.y,p.z))
	return _array_surface(v,_grid_indices(points.size(),2))

func _tapered_panel(top_width: float, bottom_width: float, height: float) -> ArrayMesh:
	var v: Array[Vector3] = [Vector3(-top_width,0,0),Vector3(top_width,0,0),Vector3(-bottom_width,-height,0),Vector3(bottom_width,-height,0)]
	return _array_surface(v,[0,3,1,0,2,3])

func _extruded_outline(outline: Array, depth: float) -> ArrayMesh:
	var v: Array[Vector3] = []
	var h := depth*0.5
	for p in outline:
		v.append(Vector3(float(p.x),float(p.y),h))
	for p in outline:
		v.append(Vector3(float(p.x),float(p.y),-h))
	var n := outline.size()
	var idx: Array[int] = []
	for i in range(1,n-1):
		idx.append_array([0,i+1,i,n,n+i,n+i+1])
	for i in range(n):
		var j := (i+1)%n
		idx.append_array([i,n+j,j,i,n+i,n+j])
	return _array_surface(v,idx)

func _grid_indices(rows: int, columns: int) -> Array[int]:
	var idx: Array[int] = []
	for r in range(rows-1):
		for c in range(columns-1):
			var a := r*columns+c
			var b := a+1
			var d := (r+1)*columns+c
			var e := d+1
			idx.append_array([a,e,b,a,d,e])
	return idx

func _array_surface(vertices: Array[Vector3], indices: Array[int]) -> ArrayMesh:
	var st := SurfaceTool.new()
	st.begin(Mesh.PRIMITIVE_TRIANGLES)
	for i in range(0,indices.size(),3):
		var a := vertices[indices[i]]
		var b := vertices[indices[i+1]]
		var c := vertices[indices[i+2]]
		var normal := (b-a).cross(c-a).normalized()
		st.set_normal(normal)
		st.add_vertex(a)
		st.set_normal(normal)
		st.add_vertex(b)
		st.set_normal(normal)
		st.add_vertex(c)
	return st.commit() as ArrayMesh

func _update_secondary_motion() -> void:
	var speed := 1.7 if animation_player != null and animation_player.current_animation in [&"Walk_Loop",&"Jog_Fwd_Loop",&"Shield_Dash"] else 1.0
	for i in range(authored_cape_pivots.size()):
		authored_cape_pivots[i].rotation.x = deg_to_rad(5.0 + sin(_proxy_time*(1.8+i*0.18)*speed+i*0.55)*(2.4+i))
	for i in range(authored_hair_pivots.size()):
		authored_hair_pivots[i].rotation.z = deg_to_rad(sin(_proxy_time*2.1*speed+i*0.63)*1.3)
	for i in range(authored_tabard_pivots.size()):
		authored_tabard_pivots[i].rotation.x = deg_to_rad(1.5 + sin(_proxy_time*1.85*speed+i*0.6)*1.3)

func _update_hud(display_name: String, clip_name: String) -> void:
	if info_label == null:
		return
	var geometry_state := "AUTHORED GEOMETRY ON" if _authored_visible else "ANIME BODY ONLY"
	var turn_state := "AUTO TURN ON" if _auto_turntable else "AUTO TURN OFF"
	info_label.text = "Diyse — Ilyra authored-geometry / UAL proof\n%s  [%s]\n%s | %s | B00 remains exact visual authority\nSPACE next   P pause   V compare   Q/E rotate   T turntable   R restart   ESC quit" % [display_name,clip_name,geometry_state,turn_state]
