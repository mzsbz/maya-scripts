import maya.cmds as mc

selection = mc.ls(sl=True)[0]
bindChain = mc.listRelatives(selection, ad=True)
bindChain.append(selection)
for jnt in bindChain:
      if "END" in jnt:
          print "end joint"
      else:
          target = jnt.replace("JNT", "CTR")
          mc.pointConstraint(target, jnt, mo=True)
          mc.orientConstraint(target, jnt, mo=True)