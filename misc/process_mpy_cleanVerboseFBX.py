import re
import maya.cmds as cmds

def replace_fbxasc_pattern_in_scene(pattern = "FBXASC\d\d\d"):
    """
    Replace the "FBXASC\d\d\d" pattern with "_" in the names of all writable DAG
    nodes, materials, and shaders in the scene.
    """
    # Get all writable DAG nodes in the scene
    nodes = cmds.ls(dag=True, readOnly=False)

    # Loop through each node and replace the pattern with "_"
    for node in nodes:
        try:
            # Replace the pattern with "_" in the node name
            new_name = re.sub(pattern, "_", node)
            cmds.rename(node, new_name)
        except:
            # Skip read-only nodes
            pass

    # Get all shading engines in the scene
    shading_engines = cmds.ls(type="shadingEngine")

    # Loop through each shading engine and replace the pattern with "_"
    for shading_engine in shading_engines:
        try:
            # Replace the pattern with "_" in the shading engine name
            new_name = re.sub(pattern, "_", shading_engine)
            cmds.rename(shading_engine, new_name)

            # Get the material connected to the shading engine
            material_connections = cmds.listConnections(shading_engine + ".surfaceShader")

            # If the shading engine is connected to a material, rename the material
            if material_connections:
                material = material_connections[0]
                new_name = re.sub(pattern, "_", material)
                cmds.rename(material, new_name)
        except:
            # Skip read-only nodes
            pass

def rename_SGwithMaterialNames():
    """
    Rename all Shader Groups with their connected Material names
    """
    # get all shading engines in the scene
    shading_engines = cmds.ls(type="shadingEngine")

    # loop through each shading engine
    for sg in shading_engines:
        # get the connected material name
        material = cmds.listConnections(sg + ".surfaceShader")[0]
        
        # skip default materials
        if material in ["lambert1", "particleCloud1"]:
            continue
        
        # check if the material is a read-only node
        if cmds.lockNode(material, q=True, lock=True):
            print("Node is locked, unlocking:", material)
            cmds.lockNode(material, lock=False)
        
        # create the new shading engine name
        new_sg_name = material + "_SG"
        
        # rename the shading engine
        cmds.rename(sg, new_sg_name)


def delete_empty_transforms():
    """
    Delete all empty transforms in the scene.
    """
    # Get all transforms in the scene
    transforms = cmds.ls(type="transform")

    # Loop through each transform and delete it if it has no children
    for transform in transforms:
        children = cmds.listRelatives(transform, children=True)
        if not children:
            cmds.delete(transform)
            
def delete_all_locators():
    """
    Delete all locators in the scene.
    """
    # Get all locators in the scene
    locators = cmds.ls(type="locator")

    # Delete each locator
    for locator in locators:
        cmds.delete(locator)

#####################################
# BUG: Run replace_fbxasc twice or it will miss out on some nodes

#replace_fbxasc_pattern_in_scene();
#replace_fbxasc_pattern_in_scene();
#rename_SGwithMaterialNames();
#delete_empty_transforms();
#delete_all_locators();