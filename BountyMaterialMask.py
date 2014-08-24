#Add 1 scene
#delete all materials of scene objects
import bpy, random ,sys

def SetMaterial():
	
	m.bounty.mat_type = 'shinydiffusemat'
	r = random.random()
	m.bounty.diff_color.hsv = (r,1,1)
	m.diffuse_color = m.bounty.diff_color
	m.bounty.emittance = 1
	#print (ob)
	#sys.exit(0)

	return{'FINISHED'}
	
bpy.context.scene.render.engine = 'THEBOUNTY'

SceneName = "MaterialID Mask"
#if Material Scene is already created then remove it
if SceneName in bpy.data.scenes: 
	bpy.data.scenes.remove(bpy.data.scenes[SceneName])
	#sys.exit()

#Create new identical scene
bpy.ops.scene.new(type='FULL_COPY') 
scn = bpy.context.scene 
scn.name = SceneName

#active = bpy.context.active_object
bpy.ops.object.select_all(action='SELECT') 
      
#Restict render for lights	  
for ob in bpy.data.scenes[scn.name].objects: 

	if ob.type == 'LAMP': 
		ob.hide_render = True

	if (ob.type == 'MESH'):

		#MESHLIGHTS
		if (ob.bounty.geometry_type == 'mesh_light'):
			ob.hide_render = True
		
		#PORTAL MESHLIGHTS
		if (ob.bounty.geometry_type == 'portal_light'):
			ob.hide_render = True

#set random colors to all mesh objects materials
for ob in bpy.context.selected_editable_objects:
	
	if ob.type == 'MESH':
		for mat in ob.material_slots:
			m = mat.material
			SetMaterial()
			
			for i in range(0, 18):
				#print (ob.material_slots)
				#sys.exit()
				mat.material.texture_slots.clear(i)
		else:
		#object has no material so add one material
			if (len(ob.material_slots)) == 0 :
				
				m = bpy.data.materials.new('visuals')
				SetMaterial()
				ob.data.materials.append(m)
		
bpy.ops.object.select_all(action='DESELECT') 

#set render settings
bpy.context.scene.bounty.bg_transp = True
bpy.context.scene.bounty.intg_light_method = 'directlighting'
bpy.context.scene.bounty.intg_use_AO = False
bpy.context.scene.bounty.AA_passes = 4
bpy.context.scene.bounty.AA_inc_samples = 2
bpy.context.scene.bounty.AA_threshold = 0.003
bpy.context.scene.bounty.gs_clay_render = False
bpy.context.scene.bounty.gs_transp_shad = False
bpy.context.scene.bounty.gs_z_channel = False

#World Background settings
bpy.context.scene.world.bounty.bg_type = 'Single Color'
bpy.context.scene.world.bounty.bg_use_ibl = False

