import maya.cmds as mc

joints = []
currCurve = [];

# SELECT CURVE and DISPLAY CV
sel = mc.ls(sl=True);
currCurve = sel[0];
mc.toggle(currCurve, cv=True);

# REBUILD CURVE with 5 SPANS
mc.rebuildCurve(sel, ch=True, rpo=True, rt=0, end=0, kcp=0, kep=0, kt=0, s=5, d=3);

# GET NO of CVs = SPAN + DEGREES (Just so we dont hardcode the no of CVs)
curveCvLength = (mc.getAttr('%s.spans'%currCurve)) + (mc.getAttr('%s.degree'%currCurve));

mc.select(clear=True);

# CREATE JOINTS on CURVE
for cvNum in range (0, curveCvLength):

	# EXCLUDE tangent CVs
    if ((cvNum != 1) & (cvNum != (curveCvLength-2))):

        # CREATE JOINT
        currJoint = mc.joint(n='spine');
        joints.append(currJoint);

        # CREATE CLUSTER and MOVE JOINTS TO CVs
        mc.select('%s.cv[%s]'%(currCurve, cvNum));
        currCluster = mc.cluster(rel=True);

        currConstraint = mc.parentConstraint(currCluster, currJoint, mo=False);

        mc.delete(currConstraint);
        mc.delete(currCluster);

        mc.select(clear=True);

# PARENT JOINTS
for jointNum in range(len(joints)-1):

    mc.parent(joints[jointNum+1], joints[jointNum]);

# ORIENT JOINTS
mc.select(joints[0], hi=True);
mc.joint(e=True, oj=('xyz'), sao=('yup'), ch=True, zso=True);

sel = mc.ls(sl=True)
for item in sel:
    mc.setAttr('%s.displayLocalAxis'%item, 1 )

mc.select(joints[len(joints)-1]);
mc.joint(e=True, o=(0, 0, 0));

print joints

# CREATE DRIVERS ETC
