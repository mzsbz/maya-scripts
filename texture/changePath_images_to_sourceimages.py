import maya.cmds as cmds
import os

tex=cmds.ls(sl=True,type="file")
for item in tex:

    fullpath = cmds.getAttr("%s.fileTextureName" %item)
    print fullpath
    fileName= fullpath.split("//")[-1]
    checkPath = fileName[:6];
    print checkPath;
    if (checkPath == "images"):
        fileName = fileName[6:];
        print fileName;
        newPath= "sourceimages" + fileName;
        cmds.setAttr("%s.fileTextureName" %item, newPath,type="string");