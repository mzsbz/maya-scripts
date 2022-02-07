import maya.cmds as mc

source = 'tree_A_trunk'
target = mc.ls(sl=1)

mc.showHidden(source)

for item in target:
    new = mc.duplicate(source, n='temp')
    mc.delete(mc.parentConstraint(item, new[0], mo=0))
    mc.delete(item)
    mc.rename(new[0], item)

mc.hide(source)
