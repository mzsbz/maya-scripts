# MAKE ARM CURVATURE LOCATORS

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
mc.spaceLocator(n='l_armUpCurvatureRotNULL');
mc.spaceLocator(n='l_armUpCurvaturePosNULL');
mc.spaceLocator(n='l_armDnCurvatureRotNULL');
mc.spaceLocator(n='l_armDnCurvaturePosNULL');
mc.spaceLocator(n='r_armUpCurvatureRotNULL');
mc.spaceLocator(n='r_armUpCurvaturePosNULL');
mc.spaceLocator(n='r_armDnCurvatureRotNULL');
mc.spaceLocator(n='r_armDnCurvaturePosNULL');

mc.parent('l_armUpCurvaturePosNULL' ,'l_armUpCurvatureRotNULL');
mc.parent('l_armDnCurvaturePosNULL' ,'l_armDnCurvatureRotNULL');
mc.parent('r_armUpCurvaturePosNULL' ,'r_armUpCurvatureRotNULL');
mc.parent('r_armDnCurvaturePosNULL' ,'r_armDnCurvatureRotNULL');

mc.pointConstraint('l_armUpTwistADVR', 'l_armUpTwistBDVR', 'l_armUpCurvatureRotNULL', mo=False);
mc.pointConstraint('l_armDnTwistADVR', 'l_armDnTwistBDVR', 'l_armDnCurvatureRotNULL', mo=False);
mc.pointConstraint('r_armUpTwistADVR', 'r_armUpTwistBDVR', 'r_armUpCurvatureRotNULL', mo=False);
mc.pointConstraint('r_armDnTwistADVR', 'r_armDnTwistBDVR', 'r_armDnCurvatureRotNULL', mo=False);

mc.aimConstraint('l_armUpTwistADVR', 'l_armUpCurvatureRotNULL', aim=[-1, 0, 0], u=[0, 0, 1], wut='objectrotation', wu=[0, 0, 1], wuo='l_armUpTwistADVR');
mc.aimConstraint('l_armDnTwistADVR', 'l_armDnCurvatureRotNULL', aim=[-1, 0, 0], u=[0, 0, 1], wut='objectrotation', wu=[0, 0, 1], wuo='l_armDnTwistADVR');
mc.aimConstraint('r_armUpTwistADVR', 'r_armUpCurvatureRotNULL', aim=[1, 0, 0], u=[0, 0, 1], wut='objectrotation', wu=[0, 0, 1], wuo='r_armUpTwistADVR');
mc.aimConstraint('r_armDnTwistADVR', 'r_armDnCurvatureRotNULL', aim=[1, 0, 0], u=[0, 0, 1], wut='objectrotation', wu=[0, 0, 1], wuo='r_armDnTwistADVR');

mc.setAttr('l_armUpCurvaturePosNULL.translateZ', -5 )
mc.setAttr('l_armDnCurvaturePosNULL.translateZ', -5 )
mc.setAttr('r_armUpCurvaturePosNULL.translateZ', 5 )
mc.setAttr('r_armDnCurvaturePosNULL.translateZ', 5 )
