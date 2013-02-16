MrEnvironment V1.1 By Andrew Hazelden  
----------
[andrew@andrewhazelden.com](mailto:andrew@andrewhazelden.com)  
[http://www.andrewhazelden.com](http://www.andrewhazelden.com  )  

![mrEnvironment test render](https://raw.github.com/AndrewHazelden/mrEnvironment-for-Maya/master/screenshots/mrEnvironment_test_render.png)

##About this Script

This is an automatic mental ray environment creation script that makes it easy to use the `mib_lookup_spherical`, `mib_lookup_cube1` and `mib_lookup_cube6` shaders in Autodesk Maya. 

The script links in the required nodes and adds a place3Dtexture node for rotating the placement of the environment map in the background of your Maya scene. This removes the need to use 4x4 matrix transforms with the `mib_texture_remap` node.

There are three Maya test scenes that show the effect of the spherical, cube1, and cube6 shelf icons.

The script also includes a Maya "Environment" shelf that adds a set of pre-made icons.


![mrEnvironment shelf](https://raw.github.com/AndrewHazelden/mrEnvironment-for-Maya/master/screenshots/mrEnvironment_shelf.png)

The python script "MrEnvironment.py" has the following functions:  
createMrCube1()  
createMrCube6()  
createMrSphere()  

* * * * * * * * * * 
 
##Environment Shader Usage

You can link the cubic environment map to a camera's environment shader port or assign it to a specific material's using the materials shading group.

If you link the env shader to a camera the environment map will show up in the reflected color on the glossy materials in the scene. If you link the env shader directly to a material's shading group it will override any camera specific environment maps in your scene.

To assign the environment shader to a specific camera, open the hypershade and use the middle mouse button to drag the environment shader onto the camera node. In the connection popup window select default. The env shader should be automatically connected to the camera's environment shader input.

To assign the environment shader to a specific material's shading group, open the hypershade and use the middle mouse button to drag the environment shader onto the materials shading group node. In the connection popup window select default. The env shader should be automatically connected to the shading group .miEnvironmentShader input.

* * * * * * * * * *

##Mac OS X Install

1. Copy the icons to your user account's Maya icons folder:
~/Library/Preferences/Autodesk/maya/2013-x64/prefs/icons/

2. Copy the python scripts `__init__.py` and `mrEnvironment.py` from the "scripts" folder to your user account's Maya script folder:
~/Library/Preferences/Autodesk/maya/2013-x64/prefs/scripts

3. Copy the `shelf_Environments.mel` file from the "shelves" folder to your user account's Maya shelves folder:
~/Library/Preferences/Autodesk/maya/2013-x64/prefs/shelves

4. (optional) Copy the sample environment map textures to your current Maya project's sourceimages folder.



##Windows Install

1. Copy the icons to your user account's Maya icons folder:
My Documents\maya\2013\prefs\icons\

2. Copy the python scripts `__init__.py` and `mrEnvironment.py` from the "scripts" folder to your user account's Maya script folder:
My Documents\maya\2013\prefs\scripts

3. Copy the `shelf_Environments.mel` file from the "shelves" folder to your user account's Maya shelves folder:
My Documents\maya\2013\prefs\shelves

4. (optional) Copy the sample environment map textures to your current Maya project's sourceimages folder.


##Linux Install

1. Copy the icons to your user account's Maya icons folder:
~/maya/2013-x64/prefs/shelves/icons

2. Copy the python scripts `__init__.py` and `mrEnvironment.py` from the "scripts" folder to your user account's Maya script folder:
~/maya/2013-x64/prefs/scripts

3. Copy the `shelf_Environments.mel` file from the "shelves" folder to your user account's Maya shelves folder:
~/maya/2013-x64/prefs/shelves

4. (optional) Copy the sample environment map textures to your current Maya project's sourceimages folder.


* * * * * * * * * *

##How the setup Script works

The script starts by setting the `mib_texture_vector` node to select a ray direction output (select -4) using world space.

![mib_texture_vector node](https://raw.github.com/AndrewHazelden/mrEnvironment-for-Maya/master/screenshots/mib_texture_vector.png)

The `mib_texture_remap` node rotates the environment map in the scene.

![mib_texture_remap node](https://raw.github.com/AndrewHazelden/mrEnvironment-for-Maya/master/screenshots/mib_texture_remap.png)

The place3DTexture node provides the in-scene rotation manipulator and handles the 4x4 matrix math required by the `mib_texture_remap` transform attribute.

The place3DTetxure node starts with a value of RotateX -90 to orient the environment cube map "upright".

![place3dtexture Node](https://raw.github.com/AndrewHazelden/mrEnvironment-for-Maya/master/screenshots/place3Dtexture.png)

###mib\_lookup\_cube1 Setup

The `mib_lookup_cube1` node expects the single texture map to be oriented in a horizontal strip format with the cube map face order of:  
1 Left  
2 Right  
3 Bottom  
4 Top (flipped vertically)  
5 Back  
6 Front  

![cube1 texture map example](https://raw.github.com/AndrewHazelden/mrEnvironment-for-Maya/master/screenshots/cube1_map.png)

If your Cubicmap face textures are 1024x1024px then the horizontal cubemap strip would have the dimensions of 6144x1024px.

Node Connections:  	
`mib_texture_vector.outValue > mib_texture_remap.input  
mib_texture_remap.outValue > mib_lookup_cube1.dir  
place3dTexture.worldInverseMatrix[0] > mib_texture_remap.transform `

Texture Map Connection Summary:  
`mentalrayTexture.message > mib_lookup_cube1.tex`  

Camera Connections:  
`mib_lookup_cube1.message > perspShape.miEnvironmentShader`

![](https://raw.github.com/AndrewHazelden/mrEnvironment-for-Maya/master/screenshots/cube1.png)

* * * * * * * * * *

###mib\_lookup\_cube6 Setup

Node Connections:  	
`mib_texture_vector.outValue > mib_texture_remap.input  
place3dTexture.worldInverseMatrix[0] > mib_texture_remap.transform   
mib_texture_remap.outValue > mib_lookup_cube6.dir  `
	
Texture Map Connection Summary:	 
`left_env_mentalrayTexture1 > mib_lookup_cube6.tex_mx  
right_env_mentalrayTexture1 > mib_lookup_cube6.tex_px  
bottom_env_mentalrayTexture1 > mib_lookup_cube6.tex_my  
top_env_mentalrayTexture1 > mib_lookup_cube6.tex_py  
back_env_mentalrayTexture1 > mib_lookup_cube6.tex_mz  
front_env_mentalrayTexture1 > mib_lookup_cube6.tex_pz`
	
Camera Connections:  
`mib_lookup_cube6.message > perspShape.miEnvironmentShader`

![](https://raw.github.com/AndrewHazelden/mrEnvironment-for-Maya/master/screenshots/cube6.png)

* * * * * * * * * *

###mib\_lookup\_spherical Setup

Node Connection Summary:  	
`mib_texture_vector.outValue > mib_texture_remap.input  
mib_texture_remap.outValue > env_mib_lookup_spherical.dir  
place3dTexture.worldInverseMatrix[0] > mib_texture_remap.transform  `

Texture Map Connection Summary:  
`mentalrayTexture.message > env_mib_lookup_spherical.tex`

Camera Connections:  
`env_mib_lookup_spherical.message > perspShape.miEnvironmentShader`

![mib lookup spherical node](https://raw.github.com/AndrewHazelden/mrEnvironment-for-Maya/master/screenshots/mib_lookup_spherical.png)

* * * * * * * * * *

##Version History

Version 1.0 Beta  
Released Jan 8, 2013  
Created first version of the mrEnvironment script, icons, and shelf.  

Version 1.1  
Released Feb 16, 2013  
Updated python code to fix cube6 face order issue.  

* * * * * * * * * *

Copyright (c) 2013 Andrew Hazelden.
