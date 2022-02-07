import maya.cmds as mc

sel = mc.ls(sl=True)

print sel[0]
selOri = sel[0]
print selOri

mc.spaceLocator()
sel = mc.ls(sl=True)

mc.rename(sel[0], selOri + 'HmNULL')

mc.select( selOri , add=True);
sel = mc.ls(sl=True)

mc.parentConstraint(sel[1], sel[0], mo=False)
mc.delete(sel[0]+'_parentConstraint1')
mc.parent(sel[1], sel[0])