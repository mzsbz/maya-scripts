import maya.cmds as cmds
import maya.mel as mel

rootDirectory = 'Y:/'

variantHead = ['Head_01', 'Head_02', 'Head_03', 'Head_04']
variantFeet = ['Flat', 'Heels', 'Pumps', 'Ankle']
variantPose = ['idleSkirt', 'idleSkitBag', 'idleWOSkirt', 'idleWOSkirtBag', 
                'poseSkirt', 'poseSkirtBag', 'poseWOSkirt', 'poseWOSkirtBag', 
                'poseSelfieWOSkirt', 'poseSelfieWOSkirtBag', 'poseSelfieSkirt', 'poseSelfieSkirtBag']

variantPoseFrame = {variantPose[0]: 195, variantPose[1]: 400, variantPose[2]: 620, variantPose[3]: 820, variantPose[4]: 1260, variantPose[5]: 1480, 
                    variantPose[6]: 1050, variantPose[7]: 1680, variantPose[8]: 1723, variantPose[9]: 1770, variantPose[10]: 1821, variantPose[11]: 1891}

objectsToDupe = ['Original_Source|Body_Source', 'Original_Source|Body_eyebrows_01_r_Source', 'Original_Source|Body_eyebrows_01_l_Source', 'Original_Source|Body_Eyelash_1_Source',
                 'Original_Source|Body_Eyelash_2_Source', 'Original_Source|Body_Eye_Left_Source', 'Original_Source|Body_Eye_Right_Source', 'Original_Source|Body_Hair_1_Source',
                 'Original_Source|Body_Hair_2_Source', 'Original_Source|Body_Hair_3_Source', 'Original_Source|Body_Hair_4_Source', 'Original_Source|Body_Hair_5_Source', 'Original_Source|Body_Hair_6_Source','Original_Source|Body_Hair_7_Source','Original_Source|Oval_Spec_Source', 
                 'Original_Source|Rec_Spec_Source', 'Original_Source|Circle_Spec_Source', 'Original_Source|Black_hairTie_Scrunchy_Source', 'Original_Source|Blue_hairTie_Scrunchy_Source', 
                 'Original_Source|Yellow_hairTie_Scrunchy_Source', 'Original_Source|Brown_hairTie_Scrunchy_Source', 'Original_Source|Apparel_Shirt_1_Source', 'Original_Source|Apparel_Shirt_2_Source', 
                 'Original_Source|Apparel_Shirt_3_Source', 'Original_Source|Apparel_Shirt_4_Source', 'Original_Source|Apparel_Shirt_5_Source', 'Original_Source|Apparel_Shirt_6_Source', 
                 'Original_Source|Apparel_Pants_1_Source', 'Original_Source|Apparel_Pants_1_forBoots_Source', 'Original_Source|Apparel_Pants_2_Source', 'Original_Source|Apparel_Pants_3_Source', 
                 'Original_Source|Apparel_jumper_1_Source', 'Original_Source|Apparel_jumper_1_forBoots_Source', 'Original_Source|Apparel_jumper_2_Source', 'Original_Source|Apparel_jumper_2_forBoots_Source', 
                 'Original_Source|Apparel_Dress_1_Source', 'Original_Source|Apparel_Dress_2_Source', 'Original_Source|bFlats_Shoes_Source', 'Original_Source|bSandles_Shoes_Source', 
                 'Original_Source|pFlats_Shoes_Source', 'Original_Source|pSandles_Shoes_Source', 'Original_Source|bOT_heels_Shoes_Source', 'Original_Source|pOT_heels_Shoes_Source', 
                 'Original_Source|bOB_pumps_Shoes_Source', 'Original_Source|pOB_pumps_Shoes_Source', 'Original_Source|Loafer_Shoes_Source', 'Original_Source|Ankle_Boots_Shoes_Source', 
                 'Original_Source|pBoots_Shoes_Source', 'Original_Source|bBoots_Shoes_Source', 'Original_Source|Bag_Buckle_Strap_Black_Source', 'Original_Source|Bag_Buckle_Main_Black_Source', 
                 'Original_Source|Bag_Buckle_Strap_Pink_Source', 'Original_Source|Bag_Buckle_Main_Pink_Source', 'Original_Source|Bag_Box_Strap_Pink_Source', 'Original_Source|Bag_Box_Main_Pink_Source', 
                 'Original_Source|Bag_Box_Strap_Black_Source', 'Original_Source|Bag_Box_Main_Black_Source' , 'Original_Source|phone_Source']

objectsOriginal = [u'Hips', u'Body', u'Body_eyebrows_01_r', u'Body_eyebrows_01_l', u'Body_Eyelash_1', u'Body_Eyelash_2', u'Body_Eye_Left', u'Body_Eye_Right', u'Body_Hair_1', u'Body_Hair_2', 
                   u'Body_Hair_3', u'Body_Hair_4', u'Body_Hair_5', u'Body_Hair_6', u'Body_Hair_7', u'Oval_Spec', u'Rec_Spec', u'Circle_Spec', u'Black_hairTie_Scrunchy', u'Blue_hairTie_Scrunchy', u'Yellow_hairTie_Scrunchy', u'Brown_hairTie_Scrunchy', 
                   u'Apparel_Shirt_1', u'Apparel_Shirt_2', u'Apparel_Shirt_3', u'Apparel_Shirt_4', u'Apparel_Shirt_5', u'Apparel_Shirt_6', u'Apparel_Pants_1', u'Apparel_Pants_1_forBoots', u'Apparel_Pants_2', 
                   u'Apparel_Pants_3', u'Apparel_jumper_1', u'Apparel_jumper_1_forBoots', u'Apparel_jumper_2', u'Apparel_jumper_2_forBoots', u'Apparel_Dress_1', u'Apparel_Dress_2', u'bFlats_Shoes', 
                   u'bSandles_Shoes', u'pFlats_Shoes', u'pSandles_Shoes', u'bOT_heels_Shoes', u'pOT_heels_Shoes', u'bOB_pumps_Shoes', u'pOB_pumps_Shoes', u'Loafer_Shoes', u'Ankle_Boots_Shoes', 
                   u'pBoots_Shoes', u'bBoots_Shoes', u'Bag_Buckle_main_jnt_BIND', u'Bag_Buckle_Strap_Black', u'Bag_Buckle_Main_Black', u'Bag_Buckle_Strap_Pink', u'Bag_Buckle_Main_Pink', 
                   u'Bag_Box_main_jnt_BIND', u'Bag_Box_Strap_Pink', u'Bag_Box_Main_Pink', u'Bag_Box_Strap_Black', u'Bag_Box_Main_Black', u'phone', u'phone_BIND']

objectsToExport = ['|Body', '|Body_eyebrows_01_r', '|Body_eyebrows_01_l', '|Body_Eyelash_1', '|Body_Eyelash_2', '|Body_Eye_Left', '|Body_Eye_Right', '|Body_Hair_1', '|Body_Hair_2', '|Body_Hair_3', 
                   '|Body_Hair_4', '|Body_Hair_5', '|Body_Hair_6', '|Body_Hair_7', '|Oval_Spec', '|Rec_Spec', '|Circle_Spec', '|Black_hairTie_Scrunchy', '|Blue_hairTie_Scrunchy', '|Yellow_hairTie_Scrunchy', '|Brown_hairTie_Scrunchy', '|Apparel_Shirt_1', 
                   '|Apparel_Shirt_2', '|Apparel_Shirt_3', '|Apparel_Shirt_4', '|Apparel_Shirt_5', '|Apparel_Shirt_6', '|Apparel_Pants_1', '|Apparel_Pants_1_forBoots', '|Apparel_Pants_2', '|Apparel_Pants_3', 
                   '|Apparel_jumper_1', '|Apparel_jumper_1_forBoots', '|Apparel_jumper_2', '|Apparel_jumper_2_forBoots', '|Apparel_Dress_1', '|Apparel_Dress_2', '|bFlats_Shoes', '|bSandles_Shoes', '|pFlats_Shoes', 
                   '|pSandles_Shoes', '|bOT_heels_Shoes', '|pOT_heels_Shoes', '|bOB_pumps_Shoes', '|pOB_pumps_Shoes', '|Loafer_Shoes', '|Ankle_Boots_Shoes', '|pBoots_Shoes', '|bBoots_Shoes', '|Bag_Buckle_Strap_Black', 
                   '|Bag_Buckle_Main_Black', '|Bag_Buckle_Strap_Pink', '|Bag_Buckle_Main_Pink', '|Bag_Box_Strap_Pink', '|Bag_Box_Main_Pink', '|Bag_Box_Strap_Black', '|Bag_Box_Main_Black' , '|phone']

####

def keepOriginal():
    cmds.group(objectsOriginal, n='Original')
    pm.select('Original', hi=True)
    for item in pm.selected():
        item.rename(item.name() + '_Source')
    

def makePoses(FeetID, PoseID):

    dupedSuffix = variantPose[PoseID] + '_feet' + variantFeet[FeetID]
    
    cmds.select(clear=True)
    cmds.currentTime(variantPoseFrame[variantPose[PoseID]])
    
    for item in objectsToDupe:
        cmds.duplicate(item, n=item + '_' + dupedSuffix)
        
    cmds.select('*' + dupedSuffix)
    cmds.group(n=dupedSuffix, w=True)    

        
def savePoses(FeetID, PoseID):
        
    dupedSuffix = variantPose[PoseID] + '_feet' + variantFeet[FeetID]

    pm.select(dupedSuffix, hi=True)
    
    for item in pm.selected():
        item.rename(item.name().replace('_Source_' + dupedSuffix, ' '))
        item.rename(item.name().replace('Original_Source_', ' '))
     
    selectedGrp = cmds.ls(sl=True)
    cmds.parent(selectedGrp, w=True)
    
    cmds.select(clear=True)
    cmds.select(objectsToExport)
    
    filename = dupedSuffix + '.glb'
    
    mel.eval('source "' + rootDirectory + 'ProjectName/Working Assets/Art/3D/Maya/CK_ShoesBag/scripts/BabylonGLBExportParams.mel"')
    mel.eval('$parameters[0] = "' + rootDirectory + 'ProjectName/Working Assets/Art/3D/Export/GLB/Poses/' + filename + '"')
    mel.eval('print $parameters[0]')
    mel.eval('ScriptToBabylon -exportParameters $parameters;')
    
    cmds.delete(objectsToExport)


def exportPoses():

    keepOriginal()
    
    for i in range(len(variantFeet)):
        
        cmds.setAttr('Body_shape.heels_shoes', 0)
        cmds.setAttr('Body_shape.Pump_shoes', 0)
        cmds.setAttr('Body_shape.Ankle_noots', 0)
        
        if i == 1:
            cmds.setAttr('Body_shape.heels_shoes', 1)
        elif i == 2:
            cmds.setAttr('Body_shape.Pump_shoes', 1)
        elif i == 3:
            cmds.setAttr('Body_shape.Ankle_noots', 1)
            
        for j in range(len(variantPose)):
            makePoses(i, j)
            savePoses(i, j)
        
        
exportPoses()
