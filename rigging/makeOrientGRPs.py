###
#
# NAME : MAKE ORIENT GROUPS
# VER  : 001
# DATE : 28 JANUARY 2018
#
# ZAIDSALIHIN :)
#
###

import maya.cmds as mc

sel = mc.ls(sl=True)

for item in sel:

    grpName = item + '_OrientGRP'
    grp = mc.group(n=grpName, w=1, em=1)

    tmpConstraint = mc.parentConstraint(item, grp, mo=False)
    mc.delete(tmpConstraint)
    mc.parent(item, grp)
