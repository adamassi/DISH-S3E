from sim_ur5.mujoco_env.sim_env import SimEnv
from math import pi
from sim_ur5.motion_planning.motion_executor import MotionExecutor
import time
from sim_ur5.mujoco_env.common.ur5e_fk import forward
from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator

# Initialize the simulation environment
env = SimEnv()



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

# # Set the joint position
# env._mj_data.joint(door_joint_name).qpos[0] = door_open_position

# # Pass the current joint positions to the step method
# current_joint_positions = {robot: env.robots_joint_pos[robot] for robot in env.robots_joint_pos.keys()}
# env.step(current_joint_positions)  # Step the simulation to apply the change

# # Slide out the dishwasher rack slowly
# rack_joint_name = "Dishwasher/bottom_rack"
# rack_start_position = env._mj_data.joint(rack_joint_name).qpos[0]
# rack_end_position = 0.274
# num_steps = 30  # Number of steps for smooth sliding
# for i in range(1, num_steps + 1):
#     # Linear interpolation between start and end
#     rack_position = rack_start_position + (rack_end_position - rack_start_position) * (i / num_steps)
#     env._mj_data.joint(rack_joint_name).qpos[0] = rack_position
#     current_joint_positions = {robot: env.robots_joint_pos[robot] for robot in env.robots_joint_pos.keys()}
#     env.step(current_joint_positions)
    # time.sleep(0.01)  # Adjust for speed (optional)

# Test logic for checking space in the down rack
evaluator = DishwasherSemanticEvaluator(env)
time.sleep(0.30)  # Wait for the environment to stabilize
executor.wait(100)
print(f"the first wine_glass is stable: {evaluator.is_stable('wine_glass/')}")
print(f"the 2 wine_glass is stable: {evaluator.is_stable('wine_glass_1/')}")
print(f"the 3 wine_glass is stable: {evaluator.is_stable('wine_glass_2/')}")
print(f"the 4 wine_glass is stable: {evaluator.is_stable('wine_glass_3/')}")

# the is 12 tall_cup 
print("know we well check the stability of the tall_cups")
print(f"the first tall_cup is stable: {evaluator.is_stable('tall_cup/')}")
# for i in range(1,11):
    # print(f"the {i+1} tall_cup is stable: {evaluator.is_stable(f'tall_cup_{i}/')}")

# there is 4 wood_spoon 
print("know we well check the stability of the wood_spoon")
print(f"the first wood_spoon is stable: {evaluator.is_stable('wood_spoon/')}")
for i in range(1,4):
    print(f"the {i+1} wood_spoon is stable: {evaluator.is_stable(f'wood_spoon_{i}/')}")

print(f"first plate is stable: {evaluator.is_stable('plate/')}")
print(f"second plate is stable: {evaluator.is_stable('plate_1/')}")
print(f"the first knife is stable: {evaluator.is_stable('knife/')}")
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
executor.wait(100)  # Wait for the environment to stabilize
# time.sleep(20)  # Wait for the door to open
env.place_object_in_dishwasher('knife/dish13_fj/', [0.77, -0.15, 0.37])
print(f"the first knife is stable: {evaluator.is_stable('knife/')}")


time.sleep(10)  # Wait for the environment to stabilize