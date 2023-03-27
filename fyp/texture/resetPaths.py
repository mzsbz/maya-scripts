import maya.cmds as cmds
import os

tex=cmds.ls(sl=True,type="file")
for item in tex:

    fullPath = cmds.getAttr("%s.fileTextureName" %item)
    print fullPath
    checkPath = "X:/Team_cuteMonster/production/BERRY/"
    print checkPath
    if checkPath in fullPath:
        newPath = fullPath.replace(checkPath, " ")
        print newPath
        cmds.setAttr("%s.fileTextureName" %item, newPath,type="string");