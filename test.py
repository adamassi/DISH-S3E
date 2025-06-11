from sim_ur5.mujoco_env.sim_env import SimEnv
from math import pi
from sim_ur5.motion_planning.motion_executor import MotionExecutor
import time
from sim_ur5.mujoco_env.common.ur5e_fk import forward



env = SimEnv()


"""
workspace_x_lims = [-0.9, -0.54]
workspace_y_lims = [-1.0, -0.55]
"""

# Initial positions of dishes and plate
dishs_position = [   
    [0, -0.6, 0.03],  # Dish 0
    [-0.7, -0.7, 0.03],  # Dish 1
    [-0.7, -0.8, 0.03],  # Dish 2
    [0, -0.8, -0.08],    # Disch 3
    [0, 0.6, 0.08],     # Dish can
    [0, 0.6, 0.1],       # Plate dish 5
]
   

executor = MotionExecutor(env)
print("waiting for 1 second")
# Add batterys to the world

env.reset(randomize=False, dish_positions=dishs_position)

joint_id = env._mj_model.joint('plate/dish5_fj/').id
body_id = env._mj_model.jnt_bodyid[joint_id]

start_time = time.time()
while time.time() - start_time < 5:
        pass  # wait for 5 seconds to let the simulation start

print("call update_object_position*************")
# Change the position of the plate dynamically
env.update_object_position("plate/dish5_fj/", [0.7, -0.6, .95])  # Update the plate's position
env.update_object_position("dish1_fj", [0.5, 0, 1])  # Update the can's position

# Use get_all_dish_positions_dict from ObjectManager to get the positions of all dishes
print("Current dish positions:")
print(env._object_manager.get_all_dish_positions_dict())


"""
Current dish positions:
{'dish0_fj': array([-1.69135539e-20, -6.00000000e-01,  3.74143128e-02])
,'dish1_fj': array([0.5, 0., 0.842059]),
,'dish2_fj': array([-0.7, -0.8, -0.0304296])
,'dish3_fj': array([ 0., -0.8, -0.1404296])
,'plate/dish5_fj/': array([ 0.69955353, -0.60060461,0.93246688])
,'can/dish4_fj/': array([-3.60637794e-04,6.00468559e-01,5.00558165e-02])



contact = env._mj_data.contact[i]
geom1_id = contact.geom1
geom2_id = contact.geom2
body1_id = env._mj_model.geom_bodyid[geom1_id]
body2_id = env._mj_model.geom_bodyid[geom2_id]

"""

