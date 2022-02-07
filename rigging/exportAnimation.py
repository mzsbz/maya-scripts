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

#CONSTRUCT FILENAME
currentFileName = mc.file( query=True, sceneName = True, shortName = True)
baseName = currentFileName[:5]
print baseName
exportBaseName = baseName + "_ANIM"
print exportBaseName
projectPath = mc.workspace( query = True, rootDirectory = True)
print projectPath
exportPath = projectPath + "scenes/ANIM_export/"
print exportPath
exportFileName = exportPath + exportBaseName
print exportFileName

#SELECT AND EXPORT
mc.select("animation")
cmds.file( exportFileName, type='mayaAscii', exportSelected=True )
