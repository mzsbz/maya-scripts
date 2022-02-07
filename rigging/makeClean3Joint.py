###
#
# NAME : MAKE CLEAN 3-JOINT
# VER  : 001.r03
# DATE : 06 NOVEMEBER 2017
#
# ZAIDSALIHIN :)
#
###

import maya.cmds as mc

def zeroAxis():
    sel = mc.ls(sl=True)
    for item in sel:
        mc.setAttr('%s.rotateX'%item, 0 )
        mc.setAttr('%s.rotateY'%item, 0 )
        mc.setAttr('%s.rotateZ'%item, 0 )
        mc.setAttr('%s.jointOrientX'%item, 0 )
        mc.setAttr('%s.jointOrientY'%item, 0 )
        mc.setAttr('%s.jointOrientZ'%item, 0 )
        mc.setAttr('%s.rotateAxisX'%item, 0 )
        mc.setAttr('%s.rotateAxisY'%item, 0 )
        mc.setAttr('%s.rotateAxisZ'%item, 0 )

def lraON():
    sel = mc.ls(sl=True)
    for item in sel:
        mc.setAttr('%s.displayLocalAxis'%item, 1 )

def resetJoints():
    # FOR SELECTED joint1, joint2, joint3; UNPARENT THEN zeroAxis()
    sel = mc.ls(sl=True)
    mc.select(hi=True)
    currJoints = mc.ls(sl=True)

    mc.parent(w=True)
    mc.select(currJoints)

    zeroAxis()
    lraON()

    mc.select(clear=True)

def aimJoints():
    # SELECT joint2 THEN joint1; aimConstraint WITH upVector joint3
    mc.select(currJoints[1],currJoints[0])
    mc.aimConstraint(mo=False, wut='object', wuo=currJoints[2])
    mc.select(clear=True)

    # SELECT joint3 THEN joint2; aimConstraint WITH upVector joint1
    mc.select(currJoints[2],currJoints[1])
    mc.aimConstraint(mo=False, wut='object', wuo=currJoints[0])
    mc.select(clear=True)

    # DELETE aimConstraints
    mc.delete(currJoints[0] + '_aimConstraint1', currJoints[1] + '_aimConstraint1')

def sewJoints():

    # PARENT joint3 TO joint2; PARENT joint2 TO joint1
    mc.parent(currJoints[2], currJoints[1])
    mc.parent(currJoints[1] ,currJoints[0])

    # zeroAxis() joint3
    mc.select(currJoints[2])
    zeroAxis()

    # FT joint1
    mc.select(currJoints[0])
    mc.makeIdentity( apply=True )
    mc.select(clear=True)
