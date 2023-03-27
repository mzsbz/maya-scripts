###
#
# NAME : ASSIGN TEA SHADERS
# VER  : 001.r00
# DATE : 03 JUL 2018
#
# ZAIDSALIHIN :)
#
###

import maya.cmds as mc

projectPath = mc.workspace( query = True, rootDirectory = True)
filePath = projectPath + 'assets/_shaders/tea_SHD.ma'

exist = objExists('tea_body_SHD')
print exist
#isReference = mc.referenceQuery(filePath, isLoaded = True)
#print isReference

if (exist == False):
    print 'hi'
    mc.file(filePath, reference=True, mergeNamespacesOnClash=True, namespace=':')

#SELECT AND LABEL GEO

body = mc.ls('*TEA_GEO|body_GEO')
headband = mc.ls('*TEA_GEO|headband*_GEO')
eyeCornea = mc.ls('*TEA_GEO|*|*_eye*_outer')
eyeIris = mc.ls('*TEA_GEO|*|*_eye*_main')
eyeLash = mc.ls('*TEA_GEO|*eyelash*')
eyeLash.extend(mc.ls('*TEA_GEO|*|*eyelashBot_GEO'))
teeth = mc.ls('*TEA_GEO|teeth*_GEO')
tongue = mc.ls('*TEA_GEO|tongue*_GEO')

apparel = mc.ls('*TEA_GEO|hairProxy_GEO')
apparel.extend(mc.ls('*TEA_GEO|bra_GEO'))
apparel.extend(mc.ls('*TEA_GEO|shirt_GEO'))
apparel.extend(mc.ls('*TEA_GEO|buckle_GEO'))
apparel.extend(mc.ls('*TEA_GEO|belt_GEO'))
apparel.extend(mc.ls('*TEA_GEO|shortsB_GEO'))
apparel.extend(mc.ls('*TEA_GEO|wristBands_GEO'))
apparel.extend(mc.ls('*TEA_GEO|shoe_GEO'))

#ASSIGN SHADERS

mc.select(body)
mc.hyperShade(a='tea_body_SHD')

mc.select(headband)
mc.hyperShade(a='tea_headband_SHD')

mc.select(eyeCornea)
mc.hyperShade(a='tea_eyeCornea_SHD')
for item in eyeCornea:
    mc.setAttr(item + 'ShapeDeformed.aiOpaque', 0)

mc.select(eyeIris)
mc.hyperShade(a='tea_eyeIris_SHD')

mc.select(eyeLash)
mc.hyperShade(a='tea_eyeLash_SHD')

mc.select(teeth)
mc.hyperShade(a='tea_teeth_SHD')

mc.select(tongue)
mc.hyperShade(a='tea_tongue_SHD')

mc.select(apparel)
mc.hyperShade(a='tea_apparel_SHD')
