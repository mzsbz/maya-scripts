
import maya.cmds as mc

# ALIGN LEG CON TO TOE
l_constraint = mc.aimConstraint('l_foot_EFF', 'l_leg_CONHmNULL', aim=[0, 0, 1], u=[0, 1, 0], wut='scene', skip=["x","z"]);
r_constraint = mc.aimConstraint('r_foot_EFF', 'r_leg_CONHmNULL', aim=[0, 0, 1], u=[0, 1, 0], wut='scene', skip=["x","z"]);
mc.delete(l_constraint ,r_constraint);

# PARENT LEG IK TO LEG CON
mc.parent('l_leg_Ik_HNDHmNULL', 'l_leg_CON');
mc.parent('r_leg_Ik_HNDHmNULL', 'r_leg_CON');
