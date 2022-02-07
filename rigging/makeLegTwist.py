###
#
# NAME : MAKE LEG TWIST
# VER  : 001.r00
# DATE : 14 DECEMBER 2017
#
# ZAIDSALIHIN :)
#
###

import maya.cmds as mc


joints = [];
mc.select(hi=True)
joints = mc.ls(sl=True);
print joints;

#GET ROOT NAME
rootName =' ';
print rootName
rootName = joints[0][:-4]
print rootName

#DEFINE mkHmNULL
def mkHmNULL(toMkHmNULLS):

    mc.spaceLocator()
    sel = mc.ls(sl=True)

    mc.rename(sel[0], toMkHmNULLS + 'HmNULL')

    mc.select( toMkHmNULLS , add=True);
    sel = mc.ls(sl=True)

    mc.parentConstraint(sel[1], sel[0], mo=False)
    mc.delete(sel[0]+'_parentConstraint1')
    mc.parent(sel[1], sel[0])

#DEFINE makeDVRs
def mkDVRs():

    #DUPLICATE _Twist_DVR JOINTS
    mc.duplicate(joints[0], po=True, n=rootName+'_A_Twist_DVR');
    mc.duplicate(joints[(len(joints)-1)], po=True, n=rootName+'_B_Twist_DVR');
    mc.duplicate(joints[(len(joints)/2)], po=True, n=rootName+'_C_Twist_DVR');
    mc.select(rootName+'_A_Twist_DVR', rootName+'_B_Twist_DVR',rootName+'_C_Twist_DVR');
    mc.parent(w=True);
    mc.select(clear=True);

    #SET DVR JOINT RADII
    mc.setAttr(rootName+'_A_Twist_DVR.radius', 2);
    mc.setAttr(rootName+'_B_Twist_DVR.radius', 2);
    mc.setAttr(rootName+'_C_Twist_DVR.radius', 2);

    #MAKE DVRs HmNULLS
    mkHmNULL(rootName+'_A_Twist_DVR');
    mkHmNULL(rootName+'_B_Twist_DVR');
    mkHmNULL(rootName+'_C_Twist_DVR');

    #AIM TO C LEFT
    #mc.aimConstraint(rootName+'_C_Twist_DVR', rootName+'_A_Twist_DVR', aim=[1, 0, 0], u=[0, 1, 0], wut='objectrotation', wu=[0, 0, 1], wuo=rootName+'_C_Twist_DVR', skip=['x'] );
    #mc.aimConstraint(rootName+'_C_Twist_DVR', rootName+'_B_Twist_DVR', aim=[-1, 0, 0], u=[0, 1, 0], wut='objectrotation', wu=[0, 0, 1], wuo=rootName+'_C_Twist_DVR', skip=['x'] );

    #AIM TO C RIGHT
    mc.aimConstraint(rootName+'_C_Twist_DVR', rootName+'_A_Twist_DVR', aim=[-1, 0, 0], u=[0, -1, 0], wut='objectrotation', wu=[0, 0, 1], wuo=rootName+'_C_Twist_DVR', skip=['x'] );
    mc.aimConstraint(rootName+'_C_Twist_DVR', rootName+'_B_Twist_DVR', aim=[1, 0, 0], u=[0, -1, 0], wut='objectrotation', wu=[0, 0, 1], wuo=rootName+'_C_Twist_DVR', skip=['x'] );

    #CONSTRAINT C TO A/B
    mc.pointConstraint(rootName+'_A_Twist_DVR', rootName+'_B_Twist_DVR', rootName+'_C_Twist_DVRHmNULL', mo=False);


def mkAdvTwist():

    #CREATE IKSPLINE
    mc.ikHandle(sj=joints[0], ee=joints[(len(joints)-1)], c=rootName+'_Twist_Ik_CRV', roc=True, pcv=False, ccv=False, sol='ikSplineSolver', n=rootName+'_Twist_Ik_HND');

    #MAKE DVRs
    mkDVRs();

    #BIND DVR TO CURVE
    mc.skinCluster(rootName+'_A_Twist_DVR', rootName+'_B_Twist_DVR', rootName+'_Twist_Ik_CRV', tsb=True, bm=0, nw=1, mi=2, omi=True, rui=True, dr=0.5);

mkAdvTwist();
