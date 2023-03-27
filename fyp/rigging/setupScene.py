import maya.cmds as mc
import maya.mel as mel

projectPath = mc.workspace( query = True, rootDirectory = True)
exportPath = projectPath + "cache/alembic/ANIM_export/"
basicFilter = "*.abc"
filename = cmds.fileDialog2(dir=exportPath, fileFilter=basicFilter, dialogStyle=1, fm=1)
print filename

command = 'AbcImport -mode import -fitTimeRange ' + '"' + str(filename[0]) + '"'
print command

mel.eval(command)

mc.currentUnit(time='pal')
