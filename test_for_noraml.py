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
    [0, -0.9, 0.1],       # Plate dish 5
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
# executor.wait(1000)
# Change the position of the plate dynamically
# env.update_object_position("dish1_fj", [0.5, 0, 1])  # Update the can's position
# env.update_object_position("plate/dish5_fj/", [0.7, -0.6, .95])  # Update the plate's position

# Use get_all_dish_positions_dict from ObjectManager to get the positions of all dishes
print("Current dish positions:")
print(env._object_manager.get_all_dish_positions_dict())




contacts = env._mj_data.contact  # Access the contact data from the simulation environment (SimEnv)






print("Waiting for 5 seconds before opening the dishwasher door...")

# executor.wait(1000)
state = env.get_state()



geom1 = "plat//unnamed_geom_0"  # Geometry name as a string
geom2 = "table_black_top"      # Geometry name as a string

# Call get_normal_force
normal_force = env.get_normal_force(geom2, geom1)
print(f"Normal force applied by {geom2} on {geom1}: {normal_force}")
normal_force = env.get_normal_force(geom1, geom2)
print(f"Normal force applied by {geom1} on {geom2}: {normal_force}")
normal_force = env.get_normal_force(geom1, geom1)
print(f"Normal force applied by {geom1} on itself: {normal_force}")


# Replace these with the actual geometry names or objects
geom1 = "can//unnamed_geom_0"  # Geometry name as a string
geom2 = "table_black_top"      # Geometry name as a string

# Call get_normal_force
normal_force = env.get_normal_force(geom2, geom1)
print(f"Normal force applied by {geom2} on {geom1}: {normal_force}")
normal_force = env.get_normal_force(geom1, geom2)
print(f"Normal force applied by {geom1} on {geom2}: {normal_force}")
normal_force = env.get_normal_force(geom1, geom1)
print(f"Normal force applied by {geom1} on itself: {normal_force}")


executor.wait(1000)