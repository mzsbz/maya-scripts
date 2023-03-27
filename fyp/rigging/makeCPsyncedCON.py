import maya.cmds as mc

sel = mc.ls(sl=True)

for item in sel:

    directName = item.replace('CPCON', 'CON')
    print directName

    constraintA = mc.parentConstraint(item, directName, mo=1)
    mc.setAttr(constraintA[0] + '.nodeState', 2)

    constraintB = mc.parentConstraint(directName, item, mo=1)

    conditionA = mc.shadingNode('condition', n= item + '_CDN', asUtility=True)
    conditionB = mc.shadingNode('condition', n= directName + '_CDN', asUtility=True)

    mc.setAttr(conditionA + '.secondTerm', 1)
    mc.setAttr(conditionA + '.colorIfFalseR', 2)
    mc.setAttr(conditionB + '.colorIfFalseR', 2)

    mc.connectAttr('m_head_CON.controlType', conditionA + '.firstTerm')
    mc.connectAttr('m_head_CON.controlType', conditionB + '.firstTerm')

    mc.connectAttr(conditionA + '.outColor.outColorR', constraintA[0] + '.nodeState')
    mc.connectAttr(conditionB + '.outColor.outColorR', constraintB[0] + '.nodeState')

    
