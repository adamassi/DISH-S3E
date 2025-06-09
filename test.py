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
env.update_object_position("plate/dish5_fj/", [2, 1, 0.15])  # Update the plate's position





print("Waiting for 5 seconds before opening the dishwasher door...")

executor.wait(1000)

