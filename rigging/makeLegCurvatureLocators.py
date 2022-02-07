# MAKE arm CURVATURE LOCATORS

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
mc.spaceLocator(n='l_armA_Curvature_RotNULL');
mc.spaceLocator(n='l_armA_Curvature_PosNULL');
mc.spaceLocator(n='l_armB_Curvature_RotNULL');
mc.spaceLocator(n='l_armB_Curvature_PosNULL');
mc.spaceLocator(n='r_armA_Curvature_RotNULL');
mc.spaceLocator(n='r_armA_Curvature_PosNULL');
mc.spaceLocator(n='r_armB_Curvature_RotNULL');
mc.spaceLocator(n='r_armB_Curvature_PosNULL');

mc.parent('l_armA_Curvature_PosNULL' ,'l_armA_Curvature_RotNULL');
mc.parent('l_armB_Curvature_PosNULL' ,'l_armB_Curvature_RotNULL');
mc.parent('r_armA_Curvature_PosNULL' ,'r_armA_Curvature_RotNULL');
mc.parent('r_armB_Curvature_PosNULL' ,'r_armB_Curvature_RotNULL');

mc.pointConstraint('l_armA_A_Twist_DVR', 'l_armA_B_Twist_DVR', 'l_armA_Curvature_RotNULL', mo=False);
mc.pointConstraint('l_armB_A_Twist_DVR', 'l_armB_B_Twist_DVR', 'l_armB_Curvature_RotNULL', mo=False);
mc.pointConstraint('r_armA_A_Twist_DVR', 'r_armA_B_Twist_DVR', 'r_armA_Curvature_RotNULL', mo=False);
mc.pointConstraint('r_armB_A_Twist_DVR', 'r_armB_B_Twist_DVR', 'r_armB_Curvature_RotNULL', mo=False);

mc.aimConstraint('l_armA_A_Twist_DVR', 'l_armA_Curvature_RotNULL', aim=[-1, 0, 0], u=[0, 0, 1], wut='objectrotation', wu=[0, 0, 1], wuo='l_armA_A_Twist_DVR');
mc.aimConstraint('l_armB_A_Twist_DVR', 'l_armB_Curvature_RotNULL', aim=[-1, 0, 0], u=[0, 0, 1], wut='objectrotation', wu=[0, 0, 1], wuo='l_armB_A_Twist_DVR');
mc.aimConstraint('r_armA_A_Twist_DVR', 'r_armA_Curvature_RotNULL', aim=[1, 0, 0], u=[0, 0, 1], wut='objectrotation', wu=[0, 0, 1], wuo='r_armA_A_Twist_DVR');
mc.aimConstraint('r_armB_A_Twist_DVR', 'r_armB_Curvature_RotNULL', aim=[1, 0, 0], u=[0, 0, 1], wut='objectrotation', wu=[0, 0, 1], wuo='r_armB_A_Twist_DVR');

mc.setAttr('l_armA_Curvature_PosNULL.translateZ', 15 )
mc.setAttr('l_armB_Curvature_PosNULL.translateZ', 10 )
mc.setAttr('r_armA_Curvature_PosNULL.translateZ', -15 )
mc.setAttr('r_armB_Curvature_PosNULL.translateZ', -10 )
