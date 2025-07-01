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
    [0.6, -0.6, 0.77],       # Plate dish 5
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


env.valid_geometry_names()


# Use get_all_dish_positions_dict from ObjectManager to get the positions of all dishes
print("Current dish positions:")
print(env._object_manager.get_all_dish_positions_dict())




contacts = env._mj_data.contact  # Access the contact data from the simulation environment (SimEnv)






print("Waiting for 5 seconds before opening the dishwasher door...")

# executor.wait(1000)
state = env.get_state()




# geom1 = "plate//unnamed_geom_0"  # Geometry name as a string
# geom2 = "table_black_top"      # Geometry name as a string

# # Debugging: Print the geometry names
# print(f"geom1: {geom1}")
# print(f"geom2: {geom2}")

# # Ensure the geometry names are valid
# if geom1 not in env.get_valid_geometry_names() or geom2 not in env.get_valid_geometry_names():
#     raise ValueError(f"One or both geometries '{geom1}' or '{geom2}' do not exist in the model.")

# # Call get_normal_force
# normal_force = env.get_normal_force(geom2, geom1)
# print(f"Normal force applied by {geom2} on {geom1}: {normal_force}")
# normal_force = env.get_normal_force(geom1, geom2)
# print(f"Normal force applied by {geom1} on {geom2}: {normal_force}")
# normal_force = env.get_normal_force(geom1, geom1)
# print(f"Normal force applied by {geom1} on itself: {normal_force}")


# Replace these with the actual geometry names or objects
geom1 = "can//unnamed_geom_0"  # Geometry name as a string
geom2 = "table_black_top"      # Geometry name as a string

# Call get_normal_force
normal_force = env.get_normal_force(geom2, geom1)
print(f"Normal force applied by {geom2} on {geom1}: {normal_force}")
normal_force = env.get_normal_force(geom1, geom2)
print(f"Normal force applied by {geom1} on {geom2}: {normal_force}")
normal_force = env.get_normal_force(geom1, geom1)
# print(f"Normal force applied by {geom1} on itself: {normal_force}")

# Replace these with the actual geometry names or objects
geom1 = "can//unnamed_geom_0"  # Geometry name as a string
geom2 = "table_white_top"      # Geometry name as a string

# Call get_normal_force
normal_force = env.get_normal_force(geom2, geom1)
print(f"Normal force applied by {geom2} on {geom1}: {normal_force}")
geom1 = "can/"
print("force applied on {geom1} ")
is_stable = env.is_stable_orientation(geom1)
print(f"Is {geom1} stable? {is_stable}")
# normal_force = env.get_force_on_geom(geom1)
# print(f"Force applied on {geom1}: {normal_force}")








# geom1 = "plate//unnamed_geom_0"  # Geometry name as a string
# geom2 = "Dishwasher//unnamed_geom_1"      # Geometry name as a string

# # Call get_normal_force
# normal_force = env.get_normal_force(geom2, geom1)
# print(f"Normal force applied by {geom2} on {geom1}: {normal_force}")
# normal_force = env.get_normal_force(geom1, geom2)
# print(f"Normal force applied by {geom1} on {geom2}: {normal_force}")
# normal_force = env.get_normal_force(geom1, geom1)
# print(f"Normal force applied by {geom1} on itself: {normal_force}")



executor.wait(1000)
"""
.\venv\Scripts\Activate
:
Geom ID 0: floor,
 Position: [ 0.   0.  -0.7]
Geom ID 1: wall_leftcorner_visual,
 Position: [-1.25  2.25  0.8 ]
Geom ID 2: wall_rightcorner_visual,
 Position: [-1.25 -2.25  0.8 ]
Geom ID 3: wall_left_visual,
 Position: [1.25 3.   0.8 ]
Geom ID 4: wall_right_visual,
 Position: [ 1.25 -3.    0.8 ]
Geom ID 5: wall_rear_visual,
 Position: [-2.   0.   0.8]
Geom ID 6: wall_front_visual,
 Position: [3.  0.  0.8]
Geom ID 7: table_wood_top,
 Position: [0.  0.  0.7]
Geom ID 8: table_wood_leg_1,
 Position: [ 0.24 -0.24 -0.  ]
Geom ID 9: table_wood_leg_2,
 Position: [ 0.24  0.24 -0.  ]
Geom ID 10: table_wood_leg_3,
 Position: [-0.24 -0.24 -0.  ]
Geom ID 11: table_wood_leg_4,
 Position: [-0.24  0.24 -0.  ]
Geom ID 12: table_black_top,
 Position: [0.  0.  0.7]
Geom ID 13: table_black_leg_1,
 Position: [ 0.24 -0.24 -0.  ]
Geom ID 14: table_black_leg_2,
 Position: [ 0.24  0.24 -0.  ]
Geom ID 15: table_black_leg_3,
 Position: [-0.24 -0.24 -0.  ]
Geom ID 16: table_black_leg_4,
 Position: [-0.24  0.24 -0.  ]
Geom ID 17: table_white_top,
 Position: [0.  0.  0.7]
Geom ID 18: table_white_leg_1,
 Position: [ 0.24 -0.24 -0.  ]
Geom ID 19: table_white_leg_2,
 Position: [ 0.24  0.24 -0.  ]
Geom ID 20: table_white_leg_3,
 Position: [-0.24 -0.24 -0.  ]
Geom ID 21: table_white_leg_4,
 Position: [-0.24  0.24 -0.  ]
Geom ID 22: //unnamed_geom_22,
 Position: [0. 0. 0.]
Geom ID 23: //unnamed_geom_23,
 Position: [0. 0. 0.]
Geom ID 24: //unnamed_geom_24,
 Position: [0. 0. 0.]
Geom ID 25: //unnamed_geom_25,
 Position: [0. 0. 0.]
Geom ID 26: bin_dark_wood//unnamed_geom_0,
 Position: [0. 0. 0.]
Geom ID 27: bin_dark_wood//unnamed_geom_1,
 Position: [0. 0. 0.]
Geom ID 28: bin_dark_wood//unnamed_geom_2,
 Position: [0.    0.125 0.05 ]
Geom ID 29: bin_dark_wood//unnamed_geom_3,
 Position: [0.    0.125 0.05 ]
Geom ID 30: bin_dark_wood//unnamed_geom_4,
 Position: [ 0.    -0.125  0.05 ]
Geom ID 31: bin_dark_wood//unnamed_geom_5,
 Position: [ 0.    -0.125  0.05 ]
Geom ID 32: bin_dark_wood//unnamed_geom_6,
 Position: [0.1  0.   0.05]
Geom ID 33: bin_dark_wood//unnamed_geom_7,
 Position: [0.1  0.   0.05]
Geom ID 34: bin_dark_wood//unnamed_geom_8,
 Position: [-0.1   0.    0.05]
Geom ID 35: bin_dark_wood//unnamed_geom_9,
 Position: [-0.1   0.    0.05]
Geom ID 36: plate//unnamed_geom_0,
 Position: [ 1.28856007e-03 -1.13993622e-07  2.85310704e-02]
Geom ID 37: can//unnamed_geom_0,
 Position: [ 5.89018274e-05 -1.33653727e-04  3.58399591e-04]
Geom ID 38: Dishwasher//unnamed_geom_0,
 Position: [3.16545299e-05 2.89189034e-01 3.98390607e-01]
Geom ID 39: Dishwasher//unnamed_geom_1,
 Position: [0.    0.312 0.756]
Geom ID 40: Dishwasher//unnamed_geom_2,
 Position: [0.    0.312 0.055]
Geom ID 41: Dishwasher//unnamed_geom_3,
 Position: [0.26  0.312 0.378]
Geom ID 42: Dishwasher//unnamed_geom_4,
 Position: [-0.26   0.312  0.378]
Geom ID 43: Dishwasher//unnamed_geom_5,
 Position: [0.    0.071 0.378]
Geom ID 44: Dishwasher//unnamed_geom_6,
 Position: [-0.00030629 -0.01362    -0.00803681]
Geom ID 45: Dishwasher//unnamed_geom_7,
 Position: [-3.02441068e-04  1.10072703e-02  3.73325854e-01]
Geom ID 46: Dishwasher//unnamed_geom_8,
 Position: [0.    0.025 0.37 ]
Geom ID 47: Dishwasher//unnamed_geom_9,
 Position: [0.    0.08  0.625]
Geom ID 48: Dishwasher//unnamed_geom_10,
 Position: [0.26  0.06  0.625]
Geom ID 49: Dishwasher//unnamed_geom_11,
 Position: [-0.26   0.06   0.625]
Geom ID 50: Dishwasher//unnamed_geom_12,
 Position: [0.    0.013 0.37 ]
Geom ID 51: Dishwasher//unnamed_geom_13,
 Position: [0.    0.08  0.625]
Geom ID 52: Dishwasher//unnamed_geom_14,
 Position: [0.26  0.06  0.625]
Geom ID 53: Dishwasher//unnamed_geom_15,
 Position: [-0.26   0.06   0.625]
Geom ID 54: rethink_mount_stationary/controller_box_col,
 Position: [-0.325  0.    -0.38 ]
Geom ID 55: rethink_mount_stationary/pedestal_feet_col,
 Position: [-0.1225  0.     -0.758 ]
Geom ID 56: rethink_mount_stationary/torso_vis,
 Position: [ 0.    0.   -0.05]
Geom ID 57: rethink_mount_stationary/pedestal_vis,
 Position: [-0.14880153  0.00164098 -0.52235803]
Geom ID 58: rethink_mount_stationary/pedestal_col,
 Position: [-0.02  0.   -0.29]
Geom ID 59: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_0,
 Position: [ 6.72961329e-07 -3.65824367e-07  9.35735148e-02]
Geom ID 60: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_1,
 Position: [1.50509706e-07 5.02943790e-07 3.11340921e-02]
Geom ID 61: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_2,
 Position: [ 0.00015792 -0.00842293  0.04825544]
Geom ID 62: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_3,
 Position: [ 1.02216025e-06  6.88846243e-02 -5.03284796e-04]
Geom ID 63: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_4,
 Position: [-4.98711159e-05  5.63615023e-04 -1.87577179e-02]
Geom ID 64: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_5,
 Position: [ 0.    0.   -0.04]
Geom ID 65: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_6,
 Position: [-3.57606460e-06 -1.99999688e-04  2.12135178e-01]
Geom ID 66: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_7,
 Position: [-7.53342716e-07 -2.45590248e-02  2.98127459e-01]
Geom ID 67: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_8,
 Position: [ 1.24751939e-05 -2.06137663e-02  2.13547791e-01]
Geom ID 68: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_9,
 Position: [-1.67388601e-05  4.53097233e-02  2.12240461e-01]
Geom ID 69: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_10,
 Position: [ 0.   -0.04  0.  ]
Geom ID 70: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_11,
 Position: [0.  0.  0.2]
Geom ID 71: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_12,
 Position: [ 2.62074506e-05 -3.98692788e-02  3.95889386e-01]
Geom ID 72: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_13,
 Position: [-2.36368332e-05 -4.34091153e-04  2.04343079e-01]
Geom ID 73: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_14,
 Position: [-9.66151675e-06  1.69765091e-02  2.55039022e-01]
Geom ID 74: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_15,
 Position: [2.97520308e-06 1.19606683e-02 1.63616826e-01]
Geom ID 75: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_16,
 Position: [0.   0.08 0.  ]
Geom ID 76: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_17,
 Position: [0.  0.  0.2]
Geom ID 77: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_18,
 Position: [-2.32478155e-05  1.26285141e-01  4.89750597e-02]
Geom ID 78: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_19,
 Position: [-3.66446148e-05  1.30401792e-01 -3.97034887e-02]
Geom ID 79: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_20,
 Position: [-2.09910244e-06  1.12896218e-01  1.23883339e-02]
Geom ID 80: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_21,
 Position: [0.   0.05 0.  ]
Geom ID 81: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_22,
 Position: [-3.80012432e-06  4.85364562e-02  9.94358041e-02]
Geom ID 82: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_23,
 Position: [ 3.16964199e-05 -4.02060557e-02  1.03591199e-01]
Geom ID 83: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_24,
 Position: [9.00023647e-07 1.60566559e-02 9.66318026e-02]
Geom ID 84: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_25,
 Position: [0.   0.   0.04]
Geom ID 85: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_26,
 Position: [0.   0.02 0.1 ]
Geom ID 86: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_27,
 Position: [ 1.37304001e-05  7.93091109e-02 -5.37868509e-04]
Geom ID 87: rethink_mount_stationary/robot_0_ur5e//unnamed_geom_28,
 Position: [0.   0.08 0.  ]
Geom ID 88: rethink_mount_stationary/robot_0_ur5e/robot_0_adhesive gripper//unnamed_geom_0,     
 Position: [0.015 0.015 0.   ]
Geom ID 89: rethink_mount_stationary/robot_0_ur5e/robot_0_adhesive gripper//unnamed_geom_1,     
 Position: [ 0.015 -0.015  0.   ]
Geom ID 90: rethink_mount_stationary/robot_0_ur5e/robot_0_adhesive gripper//unnamed_geom_2,     
 Position: [-0.015  0.015  0.   ]
Geom ID 91: rethink_mount_stationary/robot_0_ur5e/robot_0_adhesive gripper//unnamed_geom_3,     
 Position: [-0.015 -0.015  0.   ]
"""