###
#
# NAME : EXPORT ANIMATION AS ALEMBIC
# VER  : 002.01
# DATE : 15 APRIL 2018
#
# ZAIDSALIHIN :)
#
###

import maya.cmds as mc

selected =  mc.ls(sl = True)
mc.group(selected, name = "animation", world = True)

#IMPORT REFERENCES
toImport = mc.listRelatives("animation")
for i in toImport:
    isReference = mc.referenceQuery(i, isNodeReferenced = True)
    if isReference:
        rFile = mc.referenceQuery(i, f = True)
        mc.file(rFile, importReference = True)

#PARENT RENDERCAM AND DELETE DISPLAYLAYERS
mc.parent("|RENDERCAM", "animation")
mc.delete(mc.ls(type = "displayLayer"))

#SELECT GEOMETRY AND CAMERA
animated = mc.listRelatives(mc.ls('animation'), ad=True, path=True)
geometry = mc.ls(animated, type=['mesh', 'nurbsSurface'])
mc.select(geometry)
mc.select('animation|RENDERCAM|RENDERCAMshape', add=True)

#CONSTRUCT FILENAME
currentFileName = mc.file( query=True, sceneName = True, shortName = True)
baseName = currentFileName[:5]
print baseName
exportBaseName = baseName + "_ANIM"
print exportBaseName
projectPath = mc.workspace( query = True, rootDirectory = True)
print projectPath
exportPath = projectPath + "cache/alembic/ANIM_export/"
print exportPath
exportFileName = exportPath + exportBaseName + '.abc'
print exportFileName

#EXPORT ALEMBIC
start = str(mc.playbackOptions(query=True, min=True))
end = str(mc.playbackOptions(query=True, max=True))
root = '-root animation'
save_name = exportFileName

print start
print end

command = "-sl -frameRange " + start + " " + end +" -uvWrite -worldSpace " + root + " -file " + save_name
mc.AbcExport ( j = command )
