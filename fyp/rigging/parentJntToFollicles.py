import maya.cmds as mc

follicles = mc.ls(selection=True);
mc.select(clear=True)

for item in follicles:

    jntName = item.replace('FOL', 'JNT')

    mc.select(item)
    jnt = mc.joint(n=jntName)

    mc.select(clear=True)
