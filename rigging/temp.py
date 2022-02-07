import maya.cmds as mc

l_snap = '''
import maya.cmds as mc
def l_ikFkSnap():


    if mc.getAttr('l_armA_Attr_CON.IkFk'):

        # From FK to IK
        tempConstraintA = mc.parentConstraint("l_arm_Fk_CON", "l_armA_Ik_CON")
        mc.setKeyframe('l_armA_Ik_CON')
        mc.delete(tempConstraintA)

        # Do vector match voodoo
        arm01Vec = [mc.xform("l_armB_Fk_CON", t=1, ws=1, q=1)[i] - mc.xform("l_armA_Fk_CON", t=1, ws=1, q=1)[i] for i in range(3)]
        arm02Vec = [mc.xform("l_armB_Fk_CON", t=1, ws=1, q=1)[i] - mc.xform("l_arm_Fk_CON", t=1, ws=1, q=1)[i] for i in range(3)]

        # Transform polevector
        mc.xform("l_arm_Pv_CON", t=[mc.xform("l_armB_Fk_CON", t=1, q=1, ws=1)[i] + arm01Vec[i] * .75 + arm02Vec[i] * .75 for i in range(3)], ws=1)
        mc.setKeyframe("l_arm_Pv_CON")

    else:

        # From IK to FK
        tempConstraintA = mc.orientConstraint("l_armA_Ik_DVR", "l_armA_Fk_CON")
        mc.setKeyframe( 'l_armA_Fk_CON')

        tempConstraintB = mc.orientConstraint("l_armB_Ik_DVR", "l_armB_Fk_CON")
        mc.setKeyframe( 'l_armB_Fk_CON')

        tempConstraintC = mc.orientConstraint("l_arm_Ik_DVR", "l_arm_Fk_CON")
        mc.setKeyframe( 'l_arm_Fk_CON')

        mc.delete(tempConstraintA, tempConstraintB, tempConstraintC)


mc.scriptJob(attributeChange=['l_armA_Attr_CON.IkFk',l_ikFkSnap])
'''

r_snap = '''
import maya.cmds as mc
def r_ikFkSnap():


    if mc.getAttr('r_armA_Attr_CON.IkFk'):

        # From FK to IK
        tempConstraintA = mc.parentConstraint("r_arm_Fk_CON", "r_armA_Ik_CON")
        mc.setKeyframe('r_armA_Ik_CON')
        mc.delete(tempConstraintA)

        # Do vector match voodoo
        arm01Vec = [mc.xform("r_armB_Fk_CON", t=1, ws=1, q=1)[i] - mc.xform("r_armA_Fk_CON", t=1, ws=1, q=1)[i] for i in range(3)]
        arm02Vec = [mc.xform("r_armB_Fk_CON", t=1, ws=1, q=1)[i] - mc.xform("r_arm_Fk_CON", t=1, ws=1, q=1)[i] for i in range(3)]

        # Transform polevector
        mc.xform("r_arm_Pv_CON", t=[mc.xform("r_armB_Fk_CON", t=1, q=1, ws=1)[i] + arm01Vec[i] * .75 + arm02Vec[i] * .75 for i in range(3)], ws=1)
        mc.setKeyframe("r_arm_Pv_CON")

    else:

        # From IK to FK
        tempConstraintA = mc.orientConstraint("r_armA_Ik_DVR", "r_armA_Fk_CON")
        mc.setKeyframe( 'r_armA_Fk_CON')

        tempConstraintB = mc.orientConstraint("r_armB_Ik_DVR", "r_armB_Fk_CON")
        mc.setKeyframe( 'r_armB_Fk_CON')

        tempConstraintC = mc.orientConstraint("r_arm_Ik_DVR", "r_arm_Fk_CON")
        mc.setKeyframe( 'r_arm_Fk_CON')

        mc.delete(tempConstraintA, tempConstraintB, tempConstraintC)

mc.scriptJob(attributeChange=['r_armA_Attr_CON.IkFk',r_ikFkSnap])
'''

mc.scriptNode( st=2, bs=l_snap.replace("'''","''" ), n='l_arm_IkFk_SN', stp='python')
mc.scriptNode( st=2, bs=r_snap.replace("'''","''" ), n='r_arm_IkFk_SN', stp='python')
