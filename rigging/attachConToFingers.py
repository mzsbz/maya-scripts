###
#
# NAME : ATTACH FK CONTROLLERS TO FINGERS
# VER  : 003.r00
# DATE : 22 JANUARY 2018
#
# ZAIDSALIHIN :)
#
###

import maya.cmds as mc

# INIT VARIABLES
allJoint = [];
jointCON = [];

# SELECT ROOT JOINT
sel = mc.ls(selection=True);

# SELECT JOINT HIERARCHY AND STORE AS allJoint
mc.select(sel, hi=True);
allJoint = mc.ls(selection=True);

print allJoint

for item in range(0 , len(allJoint)-1):

    selJOINT = allJoint[item];
    rootName = selJOINT[:-4]
    print rootName
    conName = selJOINT.replace('CTR', 'CON');
    newCON = mc.circle( nr=(1, 0, 0), c=(0, 0, 0), n=(conName), ch=False);

    # CREATE ORIENT AND MODIFY GRPs
    orient = mc.group(n=rootName + '_OrientGRP', em=1, w=1)
    modifyA = mc.group(n=rootName + '_ModifyA_GRP', em=1, w=1)
    modifyB = mc.group(n=rootName + '_ModifyB_GRP', em=1, w=1)

    # POSITION MATCH
    tmpConstraint = mc.parentConstraint(selJOINT, newCON, mo=False);
    mc.delete(tmpConstraint);

    tmpConstraint = mc.parentConstraint(selJOINT, orient, mo=False);
    mc.delete(tmpConstraint);

    tmpConstraint = mc.parentConstraint(selJOINT, modifyA, mo=False);
    mc.delete(tmpConstraint);

    tmpConstraint = mc.parentConstraint(selJOINT, modifyB, mo=False);
    mc.delete(tmpConstraint);

    # CREATE HIERACHY
    mc.parent(newCON, modifyB)
    mc.parent(modifyB, modifyA)
    mc.parent(modifyA, orient)

    mc.parentConstraint(newCON, selJOINT, mo=False);

    # APPEND TO jointCON
    jointCON.append(orient);

# REPLICATE JOINT HIERARCHY
for item in range(1 , len(jointCON)):

    conName = jointCON[item-1].replace('OrientGRP', 'CON');
    mc.parent(jointCON[item],conName);
