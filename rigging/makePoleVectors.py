###
#
# NAME : MAKE POLE VECTORS
# VER  : 001
# DATE : 15 DECEMBER 2017
#
# ZAIDSALIHIN :)
#
###
import maya.cmds as mc

# DEFINE mkHmNULL
def mkHmNULL(toMkHmNULLS):

    mc.spaceLocator()
    sel = mc.ls(sl=True)

    mc.rename(sel[0], toMkHmNULLS + 'HmNULL')

    mc.select( toMkHmNULLS , add=True);
    sel = mc.ls(sl=True)

    mc.parentConstraint(sel[1], sel[0], mo=False)
    mc.delete(sel[0]+'_parentConstraint1')
    mc.parent(sel[1], sel[0])

# CREATE AND POSITION LOCATORS
mc.spaceLocator(n='l_pvBow');
mc.spaceLocator(n='l_pvArrow');
mc.spaceLocator(n='r_pvBow');
mc.spaceLocator(n='r_pvArrow');

mc.parent('l_pvArrow' ,'l_pvBow');
mc.parent('r_pvArrow' ,'r_pvBow');

mc.pointConstraint('l_armA_Ik_DVR', 'l_armC_Ik_EFF', 'l_pvBow', mo=False);
mc.pointConstraint('r_armA_Ik_DVR', 'r_armC_Ik_EFF', 'r_pvBow', mo=False);

mc.aimConstraint('l_armB_Ik_DVR', 'l_pvBow', aim=[0, 0, 1], u=[1, 0, 0], wut='objectrotation', wu=[0, 0, 1], wuo='l_armB_Ik_DVR');
mc.aimConstraint('r_armB_Ik_DVR', 'r_pvBow', aim=[0, 0, 1], u=[1, 0, 0], wut='objectrotation', wu=[0, 0, 1], wuo='r_armB_Ik_DVR');

mc.setAttr('l_pvArrow.translateZ', 25 )
mc.setAttr('r_pvArrow.translateZ', 25 )

# DEFINE PV LOCATORS
mc.parent('l_pvArrow' ,'r_pvArrow', w=True);
mc.delete('l_pvBow' ,'r_pvBow');

mc.rename('l_pvArrow' , 'l_arm_PvNULL');
mc.rename('r_pvArrow' , 'r_arm_PvNULL');

mkHmNULL('l_arm_PvNULL');
mkHmNULL('r_arm_PvNULL');

mc.hide('l_armPvHmNULLShape', rh=True);
mc.hide('r_armPvHmNULLShape', rh=True);
mc.showHidden('l_arm_PvNULL');
mc.showHidden('r_arm_PvNULL');

# MAKE PV
mc.poleVectorConstraint('l_arm_PvNULL', 'l_arm_Ik_HND');
mc.poleVectorConstraint('r_arm_PvNULL', 'r_arm_Ik_HND');
