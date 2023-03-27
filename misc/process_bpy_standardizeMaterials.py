import bpy

# Get all materials in the scene
all_materials = bpy.data.materials

# Loop through all materials
for mat in all_materials:
    if mat.use_nodes:  # Check if the material uses nodes
        nodes = mat.node_tree.nodes
        principled_bsdf = nodes.get("Principled BSDF")
        if principled_bsdf:  # Check if the material has a Principled BSDF node
            principled_bsdf.inputs["Metallic"].default_value = 0.0
            principled_bsdf.inputs["Roughness"].default_value = 9.0
            principled_bsdf.inputs["Clearcoat Roughness"].default_value = 0.0