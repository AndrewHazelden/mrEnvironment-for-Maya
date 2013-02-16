"""
MrEnvironment script V1.1
--------------------------------
Created by Andrew Hazelden  andrew@andrewhazelden.com

This script makes it easy to use the mib_lookup_spherical, mib_lookup_cube1 and 
mib_lookup_cube6 shaders in Autodesk Maya. The script links in the required nodes and adds 
a place3Dtexture node for rotating the environment map.


Python Functions:
createMrCube1()
createMrCube6()
createMrSphere()


Version History
----------------
Version 1.0 Beta - Released Jan 7, 2013
Created first version of the mental ray environment creation script, icons, and shelf.

Version 1.1 - Released Feb 16, 2013
Updated python code to fix cube6 face order issue.


"""



"""
Automatic Mental Ray mib_lookup_cube1
--------------------------------------------
A python function to create a cubic environment map.
"""
	
def createMrCube1():
	import maya.cmds as cmds
	#import maya.mel as mm	
	
	#Variables
	envMapFileTexture = "sourceimages/cube1_map.png"
	
	# ---------------------------------------------------------------------
	# Create the custom mental ray cube1 environment map shading network
	# ---------------------------------------------------------------------

	# Create the nodes
	env_mib_lookup_cube1 = cmds.shadingNode( 'mib_lookup_cube1', n='env_mib_lookup_cube1', asShader=True) 
	env_tex_vector = cmds.shadingNode( 'mib_texture_vector', n='env_mib_texture_vector1', asUtility=True ) 
	env_tex_remap = cmds.shadingNode( 'mib_texture_remap', n='env_mib_texture_remap1',  asUtility=True) 
	env_place3D = cmds.shadingNode( 'place3dTexture', n='place3dTexture1', asUtility=True )
	
	env_map_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='env_map_mentalrayTexture1', asTexture=True) 

	# Set the texture vector node to use select the ray direction option (-4)
	cmds.setAttr( env_tex_vector+'.select', -4)

	# Set the texture vector node selspace attribute to use world space coordinates (2)
	cmds.setAttr( env_tex_vector+'.selspace', 2)

	# Lock the place3DTexture node translate attribute to keep node at the origin
	cmds.setAttr( env_place3D+'.translate', lock=True)

	# ---------------------------------------------------------------------
	# Connect the nodes
	# ---------------------------------------------------------------------
	
	# Node Connection Summary:	
	# mib_texture_vector.outValue > mib_texture_remap.input
	# mib_texture_remap.outValue > mib_lookup_cube1.dir
	# place3dTexture.worldInverseMatrix[0] > mib_texture_remap.transform 
	# mentalrayTexture.message > mib_lookup_cube1.tex
	
	# Camera Connections:
	# mib_lookup_cube1.message > perspShape.miEnvironmentShader
	
	
	# Connect the mib_texture_vector node to the mib_texture_remap input
	cmds.connectAttr( env_tex_vector+'.outValue', env_tex_remap+'.input' )
	
	# Connect the mib_texture_remap node to cube1 direction input
	cmds.connectAttr( env_tex_remap+'.outValue', env_mib_lookup_cube1+'.dir' )

	# Connect the place3DTexture node to the mib_texture_remap node 4x4 translation matrix
	cmds.connectAttr( env_place3D+'.worldInverseMatrix[0]', env_tex_remap+'.transform')

	# Connect the cube1 map file texture
	cmds.connectAttr( env_map_mr_tex+'.message', env_mib_lookup_cube1+'.tex' )
	
	# Assign a default file name to the cubic face texture
	cmds.setAttr( env_map_mr_tex+'.fileTextureName', envMapFileTexture , type="string")

	# ---------------------------------------------------------------------
	# Connect the shader to the perspective camera
	# ---------------------------------------------------------------------

	# Connect new node
	cmds.connectAttr( env_mib_lookup_cube1+'.message', 'perspShape.miEnvironmentShader', force=True ) 
	
	# ---------------------------------------------------------------------
	# Set the texture_remap node to rotate the environment map upright
	# using a Place3DTexture rotateX -90 which provides a final output of a
	# mib_texture_remap RotateY +90 degree matrix offset
	# ---------------------------------------------------------------------
			
	cmds.setAttr( env_place3D+'.rotateX', -90.0)

	#cmds.setAttr( env_tex_remap+'.transform', 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, type="matrix")
	
	# ---------------------------------------------------------------------
	# Disable the Torus X/Y/ attribute
	# ---------------------------------------------------------------------
	
	cmds.setAttr( env_tex_remap+'.torus_x',0)
	cmds.setAttr( env_tex_remap+'.torus_y',0)
	cmds.setAttr( env_tex_remap+'.torus_z',0)
	
	
	#Select the place3Dtexture node
	cmds.select(env_place3D, r=True)

"""
Automatic Mental Ray mib_lookup_cube6
--------------------------------------------
A python function to create a cubic environment map.
"""
	
def createMrCube6():
	import maya.cmds as cmds
	#import maya.mel as mm	
	
	#Variables
	envMapLeftFileTexture = "sourceimages/left.png"
	envMapRightFileTexture = "sourceimages/right.png"
	envMapBottomFileTexture = "sourceimages/bottom.png"
	envMapTopFileTexture = "sourceimages/top.png"
	envMapFrontFileTexture = "sourceimages/front.png"
	envMapBackFileTexture = "sourceimages/back.png"
	
	# ---------------------------------------------------------------------
	# Create the custom mental ray cube6 environment map shading network
	# ---------------------------------------------------------------------
	
	# Create the nodes
	env_mib_lookup_cube6 = cmds.shadingNode( 'mib_lookup_cube6', n='env_mib_lookup_cube6', asShader=True) 
	env_tex_vector = cmds.shadingNode( 'mib_texture_vector', n='env_mib_texture_vector1', asUtility=True ) 
	env_tex_remap = cmds.shadingNode( 'mib_texture_remap', n='env_mib_texture_remap1',  asUtility=True)
	env_place3D = cmds.shadingNode( 'place3dTexture', n='place3dTexture1', asUtility=True )
	
	envMapLeft_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='left_env_mentalrayTexture1', asTexture=True)
	envMapRight_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='right_env_mentalrayTexture1', asTexture=True)
	envMapBottom_mr_tex= cmds.shadingNode( 'mentalrayTexture', n='bottom_env_mentalrayTexture1', asTexture=True)
	envMapTop_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='top_env_mentalrayTexture1', asTexture=True)
	envMapFront_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='front_env_mentalrayTexture1', asTexture=True)
	envMapBack_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='back_env_mentalrayTexture1', asTexture=True)
	
	
	# Set the texture vector node to use select the ray direction option (-4)
	cmds.setAttr( env_tex_vector+'.select', -4)
	
	# Set the texture vector node selspace attribute to use world space coordinates (2)
	cmds.setAttr( env_tex_vector+'.selspace', 2)
	
	# Lock the place3DTexture node translate attribute to keep node at the origin
	cmds.setAttr( env_place3D+'.translate', lock=True)
	
	# ---------------------------------------------------------------------
	# Connect the nodes
	# ---------------------------------------------------------------------
	
	# Node Connection Summary:	
	# mib_texture_vector.outValue > mib_texture_remap.input
	# place3dTexture.worldInverseMatrix[0] > mib_texture_remap.transform 
	# mib_texture_remap.outValue > mib_lookup_cube6.dir
	
	# Texture Map Connection Summary:	
	# left_env_mentalrayTexture1 > mib_lookup_cube6.tex_mx
	# right_env_mentalrayTexture1 > mib_lookup_cube6.tex_px
	# bottom_env_mentalrayTexture1 > mib_lookup_cube6.tex_my
	# top_env_mentalrayTexture1 > mib_lookup_cube6.tex_py
	# back_env_mentalrayTexture1 > mib_lookup_cube6.tex_mz
	# front_env_mentalrayTexture1 > mib_lookup_cube6.tex_pz
	
	# Camera Connections:
	# mib_lookup_cube6.message > perspShape.miEnvironmentShader
	
	
	# Connect the mib_texture_vector node to the mib_texture_remap input
	cmds.connectAttr( env_tex_vector+'.outValue', env_tex_remap+'.input' )
	
	# Connect the mib_texture_remap node to cube6 direction input
	cmds.connectAttr( env_tex_remap+'.outValue', env_mib_lookup_cube6+'.dir' )

	# Connect the place3DTexture node to the mib_texture_remap node 4x4 translation matrix
	cmds.connectAttr( env_place3D+'.worldInverseMatrix[0]', env_tex_remap+'.transform')

	# Connect the 6 cubic map file textures
	cmds.connectAttr( envMapLeft_mr_tex+'.message', env_mib_lookup_cube6+'.tex_mx' )
	cmds.connectAttr( envMapRight_mr_tex+'.message', env_mib_lookup_cube6+'.tex_px' )
	cmds.connectAttr( envMapBottom_mr_tex+'.message', env_mib_lookup_cube6+'.tex_my' )
	cmds.connectAttr( envMapTop_mr_tex+'.message', env_mib_lookup_cube6+'.tex_py' )
	cmds.connectAttr( envMapBack_mr_tex+'.message', env_mib_lookup_cube6+'.tex_mz' )
	cmds.connectAttr( envMapFront_mr_tex+'.message', env_mib_lookup_cube6+'.tex_pz' )
	
	# Assign a default file name to each cubic face
	cmds.setAttr( envMapLeft_mr_tex+'.fileTextureName', envMapLeftFileTexture , type="string")
	cmds.setAttr( envMapRight_mr_tex+'.fileTextureName', envMapRightFileTexture , type="string")
	cmds.setAttr( envMapBottom_mr_tex+'.fileTextureName', envMapBottomFileTexture , type="string")
	cmds.setAttr( envMapTop_mr_tex+'.fileTextureName', envMapTopFileTexture , type="string")
	cmds.setAttr( envMapFront_mr_tex+'.fileTextureName', envMapFrontFileTexture , type="string")
	cmds.setAttr( envMapBack_mr_tex+'.fileTextureName', envMapBackFileTexture , type="string")
	
	# ---------------------------------------------------------------------
	# Connect the shader to the perspective camera
	# ---------------------------------------------------------------------
	
	# Connect new node
	cmds.connectAttr( env_mib_lookup_cube6+'.message', 'perspShape.miEnvironmentShader', force=True ) 
	
	# ---------------------------------------------------------------------
	# Set the texture_remap node to rotate the environment map upright
	# using a Place3DTexture rotateX -90 which provides a final output of a
	# mib_texture_remap RotateY +90 degree matrix offset
	# ---------------------------------------------------------------------
			
	cmds.setAttr( env_place3D+'.rotateX', -90.0)
	
	#cmds.setAttr( env_tex_remap+'.transform', 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, type="matrix")
	
	# ---------------------------------------------------------------------
	# Disable the Torus X/Y/ attribute
	# ---------------------------------------------------------------------
	
	cmds.setAttr( env_tex_remap+'.torus_x',0)
	cmds.setAttr( env_tex_remap+'.torus_y',0)
	cmds.setAttr( env_tex_remap+'.torus_z',0)
	
	#Select the place3Dtexture node
	cmds.select(env_place3D, r=True)
	



"""
Automatic Mental Ray mib_lookup_spherical
--------------------------------------------
A python function to create a spherical environment map.
"""
	
def createMrSphere():
	import maya.cmds as cmds
	#import maya.mel as mm	
	
	#Variables
	envMapFileTexture = "sourceimages/equirectangular.png"
	
	# ---------------------------------------------------------------------
	# Create the custom mental ray spherical environment map shading network
	# ---------------------------------------------------------------------

	# Create the nodes
	env_mib_lookup_spherical = cmds.shadingNode( 'mib_lookup_spherical', n='env_mib_lookup_spherical1', asShader=True) 
	env_tex_vector = cmds.shadingNode( 'mib_texture_vector', n='env_mib_texture_vector1', asUtility=True ) 
	env_tex_remap = cmds.shadingNode( 'mib_texture_remap', n='env_mib_texture_remap1',  asUtility=True) 
	env_place3D = cmds.shadingNode( 'place3dTexture', n='place3dTexture1', asUtility=True )
	
	env_map_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='env_map_mentalrayTexture1', asTexture=True) 

	# Set the texture vector node to use select the ray direction option (-4)
	cmds.setAttr( env_tex_vector+'.select', -4)

	# Set the texture vector node selspace attribute to use world space coordinates (2)
	cmds.setAttr( env_tex_vector+'.selspace', 2)

	# Lock the place3DTexture node translate attribute to keep node at the origin
	cmds.setAttr( env_place3D+'.translate', lock=True)

	# ---------------------------------------------------------------------
	# Connect the nodes
	# ---------------------------------------------------------------------
	
	# Node Connection Summary:	
	# mib_texture_vector.outValue > mib_texture_remap.input
	# mib_texture_remap.outValue > env_mib_lookup_spherical.dir
	# place3dTexture.worldInverseMatrix[0] > mib_texture_remap.transform 
	# mentalrayTexture.message > env_mib_lookup_spherical.tex
	
	# Camera Connections:
	# env_mib_lookup_spherical.message > perspShape.miEnvironmentShader
	
	
	# Connect the mib_texture_vector node to the mib_texture_remap input
	cmds.connectAttr( env_tex_vector+'.outValue', env_tex_remap+'.input' )
	
	# Connect the mib_texture_remap node to cube1 direction input
	cmds.connectAttr( env_tex_remap+'.outValue', env_mib_lookup_spherical+'.dir' )

	# Connect the place3DTexture node to the mib_texture_remap node 4x4 translation matrix
	cmds.connectAttr( env_place3D+'.worldInverseMatrix[0]', env_tex_remap+'.transform')

	# Connect the cube1 map file texture
	cmds.connectAttr( env_map_mr_tex+'.message', env_mib_lookup_spherical+'.tex' )
	
	# Assign a default file name to the cubic face texture
	cmds.setAttr( env_map_mr_tex+'.fileTextureName', envMapFileTexture , type="string")

	# ---------------------------------------------------------------------
	# Connect the shader to the perspective camera
	# ---------------------------------------------------------------------

	# Connect new node
	cmds.connectAttr( env_mib_lookup_spherical+'.message', 'perspShape.miEnvironmentShader', force=True ) 
	
	# ---------------------------------------------------------------------
	# Set the texture_remap node to rotate the environment map upright
	# using a Place3DTexture rotateX -90 which provides a final output of a
	# mib_texture_remap RotateY +90 degree matrix offset
	# ---------------------------------------------------------------------
			
	#cmds.setAttr( env_place3D+'.rotateX', -90.0)

	#cmds.setAttr( env_tex_remap+'.transform', 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, type="matrix")
	
	# ---------------------------------------------------------------------
	# Disable the Torus X/Y/ attribute
	# ---------------------------------------------------------------------
	
	cmds.setAttr( env_tex_remap+'.torus_x',0)
	cmds.setAttr( env_tex_remap+'.torus_y',0)
	cmds.setAttr( env_tex_remap+'.torus_z',0)
