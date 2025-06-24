from sim_ur5.mujoco_env.sim_env import SimEnv
from math import pi
from sim_ur5.motion_planning.motion_executor import MotionExecutor
import time
from sim_ur5.mujoco_env.common.ur5e_fk import forward
from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator

# Initialize the simulation environment
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
    [0, -0.8, -0.08],    # Dish 3
    [0, 0.6, 0.08],     # Dish can
    [0.6, -0.6, 0.77],  # Plate dish 5
]

executor = MotionExecutor(env)

print("waiting for 1 second")
env.reset(randomize=False, dish_positions=dishs_position)

# Open the dishwasher door
door_joint_name = "Dishwasher/door"  # Correct joint name
door_open_position = -1.5  # Fully open position (in radians)

# Set the joint position
env._mj_data.joint(door_joint_name).qpos[0] = door_open_position

# Pass the current joint positions to the step method
current_joint_positions = {robot: env.robots_joint_pos[robot] for robot in env.robots_joint_pos.keys()}
env.step(current_joint_positions)  # Step the simulation to apply the change

# Slide out the dishwasher rack slowly
rack_joint_name = "Dishwasher/bottom_rack"
rack_start_position = env._mj_data.joint(rack_joint_name).qpos[0]
rack_end_position = 0.274
num_steps = 30  # Number of steps for smooth sliding
for i in range(1, num_steps + 1):
    # Linear interpolation between start and end
    rack_position = rack_start_position + (rack_end_position - rack_start_position) * (i / num_steps)
    env._mj_data.joint(rack_joint_name).qpos[0] = rack_position
    current_joint_positions = {robot: env.robots_joint_pos[robot] for robot in env.robots_joint_pos.keys()}
    env.step(current_joint_positions)
    time.sleep(0.01)  # Adjust for speed (optional)

# Test logic for checking space in the down rack
evaluator = DishwasherSemanticEvaluator(env)

# Define the positions of dishes in the down rack
positions = [
    [0.5, -0.3, 0.2],  # Dish 1 in the down rack
    [0.6, -0.4, 0.25],  # Dish 2 in the down rack
    [0.7, -0.5, 0.18],  # Dish 3 in the down rack
]

# env.place_object_in_dishwasher('wood_spoon_3/dish10_fj/', [0.79, -0.5, 0.23])
env.valid_geometry_names()
geom2_name= 'table_black_top'
geom1_name='wine_glass//unnamed_geom_0'
print(f"geom1_name: {geom1_name}, geom2_name: {geom2_name}")
print(env.get_normal_force(geom1_name, geom2_name))
geom1_name='tall_cup//unnamed_geom_0'
print(f"geom1_name: {geom1_name}, geom2_name: {geom2_name}")
print(env.get_normal_force(geom1_name, geom2_name))
# env.simulate_steps(10)
# executor.wait(10)
# wooden_fork d5lat block in the lift 
# env.place_object_in_dishwasher('wooden_fork/dish11_fj/', [0.77, -0.18, 0.37]) 
executor.wait(10)


# knife d5lt  block in the right
env.place_object_in_dishwasher('knife/dish13_fj/', [0.74, -0.15, 0.37])
executor.wait(30)
# executor.wait(30)
env.update_object_position('tall_cup_8/dish27_fj/',[0.45,-0.4,0.25])
executor.wait(30)
env.place_object_in_dishwasher('spoon/dish31_fj/', [0.77, -0.18, 0.27])
executor.wait(30)

env.update_object_position('tall_cup_2/dish21_fj/',[0.43,-0.3,0.25])
executor.wait(40)
env.update_object_position('tall_cup_1/dish20_fj/',[0.43,-0.2,0.26])
executor.wait(30)
env.update_object_position('tall_cup_4/dish23_fj/',[0.43,-0.5,0.27])
executor.wait(60)
env.update_object_position('tall_cup/dish19_fj/',[0.53,-0.5,0.27])
executor.wait(30)
env.update_object_position('wine_glass/dish15_fj/',[0.53,-0.4,0.25])
executor.wait(30)
env.place_object_in_dishwasher('wine_glass_1/dish16_fj/',[0.53,-0.3,0.25])
executor.wait(30)
env.update_object_position('wine_glass_2/dish17_fj/',[0.54,-0.2,0.25])
executor.wait(30)
env.update_object_position('tall_cup_3/dish22_fj/',[0.63,-0.2,0.25])
executor.wait(30)
env.update_object_position('tall_cup_5/dish24_fj/',[0.63,-0.4,0.25])
executor.wait(30)
env.update_object_position('tall_cup_7/dish26_fj/',[0.63,-0.3,0.25])
executor.wait(30)
# env.update_object_position('tall_cup_6/dish25_fj/',[0.63,-0.5,0.25])
env.place_object_in_dishwasher('tall_cup_6/dish25_fj/', [0.63, -0.5, 0.25])
executor.wait(30)


geom2_name='Dishwasher//unnamed_geom_7'
geom1_name='tall_cup_1//unnamed_geom_0'
print(f"geom1_name: {geom1_name}, geom2_name: {geom2_name}")
print(env.get_normal_force(geom1_name, geom2_name))
# executor.wait(10000)

geom_names = env.get_valid_geometry_names()
num_cups = 0
for geom_name in geom_names :
    if 'cup' in geom_name.lower() or 'glass' in geom_name.lower():
        normal_force = env.get_normal_force(geom_name, geom2_name)
        print(f"Normal force on {geom_name} with respect to {geom2_name}:")
        print(normal_force)
        if normal_force[2] not in [0, 0.0]:
            num_cups += 1
print(f"Number of cups/glasses in the dishwasher: {num_cups}")
num_skoms = 0
for geom_name in geom_names :
    if 'spoon' in geom_name.lower() or 'fork' in geom_name.lower() or 'knife' in geom_name.lower():
        normal_force = env.get_normal_force(geom_name, geom2_name)
        print(f"Normal force on {geom_name} with respect to {geom2_name}:")
        print(normal_force)
        if normal_force[2] not in [0, 0.0]:
            num_skoms += 1

print(f"Number of spoons/forks/knives in the dishwasher: {num_skoms}")
          

# Check if there is space in the down rack
down_rack_space = len([
    d for d in env._object_manager.object_names
    if 0.4 <= env._object_manager.get_object_pos(d)[0] <= 0.8 and
       -0.551 <= env._object_manager.get_object_pos(d)[1] <= -0.151 and
       0.165 <= env._object_manager.get_object_pos(d)[2] <= 0.285
]) < env.num_dishs


# executor.wait(1000)

print("Is there space in the down rack?", down_rack_space)

assert down_rack_space, "There should be space in the down rack"