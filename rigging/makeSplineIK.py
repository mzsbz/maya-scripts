###
#
# NAME : MAKE SPLINE IK
# VER  : 002.r00
# DATE : 03 NOVEMBER 2017
#
# ZAIDSALIHIN :)
#
###

import maya.cmds as mc

joints = mc.ls(sl=True);
print joints;

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
    #DUPLICATE _DVR JOINTS
    mc.duplicate(joints[0], po=True, n='m_spineA_Ik_A_DVR');
    mc.duplicate(joints[(len(joints)-1)], po=True, n='m_spineA_Ik_B_DVR');
    mc.duplicate(joints[(len(joints)/2)], po=True, n='m_spineA_Ik_C_DVR');
    mc.select('m_spineA_Ik_A_DVR', 'm_spineA_Ik_B_DVR','m_spineA_Ik_C_DVR');
    mc.parent(w=True);
    mc.select(clear=True);

    #SET DVR JOINT RADII
    mc.setAttr('m_spineA_Ik_A_DVR.radius', 2);
    mc.setAttr('m_spineA_Ik_B_DVR.radius', 2);
    mc.setAttr('m_spineA_Ik_C_DVR.radius', 2);

    #MAKE DVRs HmNULLS
    mkHmNULL('m_spineA_Ik_A_DVR');
    mkHmNULL('m_spineA_Ik_B_DVR');
    mkHmNULL('m_spineA_Ik_C_DVR');

    #AIM TO C
    mc.aimConstraint('m_spineA_Ik_C_DVR', 'm_spineA_Ik_A_DVR', aim=[1, 0, 0], u=[0, 1, 0], wut='objectrotation', wu=[0, 0, 1], wuo='m_spineA_Ik_C_DVR', skip=['x'] );
    mc.aimConstraint('m_spineA_Ik_C_DVR', 'm_spineA_Ik_B_DVR', aim=[-1, 0, 0], u=[0, 1, 0], wut='objectrotation', wu=[0, 0, 1], wuo='m_spineA_Ik_C_DVR', skip=['x'] );

    #CONSTRAINT C TO A/B
    mc.pointConstraint('m_spineA_Ik_A_DVR', 'm_spineA_Ik_B_DVR', 'm_spineA_Ik_C_DVRHmNULL', mo=False);

#CREATE IKSPLINE
mc.ikHandle(sj=joints[0], ee=joints[(len(joints)-1)], c='m_spineA_Ik_CRV', roc=True, pcv=False, ccv=False, sol='ikSplineSolver', n='m_spineA_Ik_HND');

#MAKE DVRs
mkDVRs();

#BIND DVR TO CURVE
mc.skinCluster('m_spineA_Ik_A_DVR', 'm_spineA_Ik_B_DVR', 'm_spineA_Ik_C_DVR', 'm_spineA_Ik_CRV', tsb=True, bm=0, nw=1, mi=1, omi=True, rui=True, dr=1.0);
