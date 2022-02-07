# ATTACH PROXIES TO CTRs

import maya.cmds as mc

#DEFINE mkHmNULL
def mkHmNULL(toMkHmNULLS):

    mc.spaceLocator()
    sel = mc.ls(sl=True)
    
    mc.rename(sel[0], toMkHmNULLS + 'HmNULL')
    
    mc.select( toMkHmNULLS , add=True);
    sel = mc.ls(sl=True)
    
    mc.parentConstraint(sel[1], sel[0], mo=False)
    mc.delete(sel[0]+'_parentConstraint1')
    mc.parent(sel[1], sel[0])

#select the top joint
#store selected joint in 'sel'
poly = mc.ls(selection=True)

print poly

for item in poly:

    polyName =  item;
    baseName = polyName[:-3];
    jointName = baseName + 'CTR';
    
    proxyLocator = mc.spaceLocator(n=baseName + 'PROXY')
    mc.parentConstraint(jointName, proxyLocator, mo=False)
    
    mc.parent(polyName, proxyLocator);
    
    mkHmNULL(proxyLocator[0]);
    mc.rename(proxyLocator[0] + 'HmNULL' , baseName + 'ProxyHmNULL');