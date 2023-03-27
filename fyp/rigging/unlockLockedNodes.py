import maya.cmds as mc

######### unlock all nodes
allNodes = mc.ls()
for node in allNodes:
    mc.lockNode(node, l=False)
