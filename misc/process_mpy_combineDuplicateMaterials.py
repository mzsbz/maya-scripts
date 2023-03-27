import maya.cmds as cmds

def find_duplicate_materials(suffix_pattern = '_ncl1_'):
    # Get a list of all materials in the scene
    materials = cmds.ls(materials=True)

    # Create a dictionary to store duplicate materials
    duplicate_materials = {}

    # Loop through all materials in the scene
    for material in materials:
        # Split the material name at the suffix
        material_parts = material.rsplit(suffix_pattern, 1)
        if len(material_parts) == 2:
            material_base_name, material_suffix = material_parts
            try:
                # Try to convert the enumeration number to an int
                material_suffix = int(material_suffix)
            except ValueError:
                # If the suffix is not a number, set it to None
                material_suffix = None

            # Check if the base material exists
            if cmds.objExists(material_base_name):
                if material_base_name in duplicate_materials:
                    # Add the material to the list of duplicates
                    duplicate_materials[material_base_name].append((material, material_suffix))
                else:
                    # Create a new entry in the dictionary for the material base name
                    duplicate_materials[material_base_name] = [(material, material_suffix)]
            else:
                # Print a warning if the base material does not exist
                print('Base material "%s" not found for material "%s"' % (material_base_name, material))

    # Print the duplicate materials
    for base_name, material_list in duplicate_materials.items():
        # Check if there are multiple materials with the same base name
        if len(material_list) > 1:
            # Sort the materials by their suffix
            material_list.sort(key=lambda x: x[1])

            # Print the duplicate materials
            print('Duplicate materials for "%s":' % base_name)
            #for material in material_list:
            #    print('\t%s' % material[0])
            
    return duplicate_materials

duplicate_materials = find_duplicate_materials()

print(duplicate_materials.keys())

# Selects objects with duplicate materials and replace with base_material

for base_material in duplicate_materials.keys():
    print(base_material)
        
    for duplicate_material in duplicate_materials[base_material]:
        print(duplicate_material[0])
        cmds.select(duplicate_material[0])
        cmds.hyperShade(objects="")
        cmds.sets( e=True, forceElement= base_material + '_SG' )
        cmds.delete(duplicate_material[0])