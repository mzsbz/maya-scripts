#aimConstraints for leg/arm rollJointDVRs

# SELECT ADVRs FIRST, BDVRs SECOND

import maya.cmds as mc

def aimConLEFT:

    sel = mc.ls(sl=True)
    
    selA = sel[0]
    selB = sel[1]
    
    mc.aimConstraint(selB, selA, aim=[1, 0, 0], u=[0, 1, 0], wut='none')
    mc.aimConstraint(selA, selB, aim=[-1, 0, 0], u=[0, 1, 0], wut='none')
    
def aimConRIGHT:
    
    sel = mc.ls(sl=True)
    
    selA = sel[0]
    selB = sel[1]
    
    mc.aimConstraint(selB, selA, aim=[-1, 0, 0], u=[0, -1, 0], wut='none')
    mc.aimConstraint(selA, selB, aim=[1, 0, 0], u=[0, -1, 0], wut='none')