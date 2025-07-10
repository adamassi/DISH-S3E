from sim_ur5.mujoco_env.sim_env import SimEnv
from sim_ur5.motion_planning.motion_executor import MotionExecutor
from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator

# === Setup ===
env = SimEnv()
executor = MotionExecutor(env)
evaluator = DishwasherSemanticEvaluator(env)

# === Fragile object names ===
fragile_objects = [
    "wine_glass",
    "tall_cup_1",
    "plate",
]

# === Non-fragile object names ===
non_fragile_objects = [
    "spoon",
    "knife",
    "fork",
]
# === Prepare the scene ===
env.open_dishwasher_door()
executor.wait(30)

# === Test Fragile ===
print("\n[TEST] Fragile object detection")

for name in fragile_objects:
    env.select_body(name + "/")
    result = evaluator.is_fragile(name)
    print(f"{name}: is_fragile = {result}")
    assert result, f"❌ Expected {name} to be fragile, but got False"
    print(f"✅ {name} correctly detected as fragile")
    executor.wait(50)

# === Test Non-Fragile ===
print("\n[TEST] Non-fragile object detection")

for name in non_fragile_objects:
    env.select_body(name + "/")
    result = evaluator.is_fragile(name)
    print(f"{name}: is_fragile = {result}")
    assert not result, f"❌ Expected {name} to be non-fragile, but got True"
    print(f"✅ {name} correctly detected as non-fragile")
    executor.wait(50)

executor.wait(50)














# from sim_ur5.mujoco_env.sim_env import SimEnv
# from math import pi
# from sim_ur5.motion_planning.motion_executor import MotionExecutor
# import time
# from sim_ur5.mujoco_env.common.ur5e_fk import forward
# from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator



# env = SimEnv()


# """
# workspace_x_lims = [-0.9, -0.54]
# workspace_y_lims = [-1.0, -0.55]
# """

# # Initial positions of dishes and plate
# dishs_position = [   
#     [0, -0.6, 0.03],  # Dish 0
#     [-0.7, -0.7, 0.03],  # Dish 1
#     [-0.7, -0.8, 0.03],  # Dish 2
#     [0, -0.8, -0.08],    # Disch 3
#     [0, 0.6, 0.08],     # Dish can
#     [0.6, -0.6, 0.77],       # Plate dish 5
# ]
   

# executor = MotionExecutor(env)

# print("waiting for 1 second")
# # Add batterys to the world

# env.reset(randomize=False, dish_positions=dishs_position)


# # Open the dishwasher door
# door_joint_name = "Dishwasher/door"  # Correct joint name
# door_open_position = -1.5  # Fully open position (in radians)

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
#     time.sleep(0.01)  # Adjust for speed (optional)
# executor.wait(100)
# env.update_object_position('cup_2/dish21_fj/',[0.43,-0.3,0.25])
# executor.wait(40)
# env.update_object_position('cup_1/dish20_fj/',[0.46,-0.22,0.26])
# executor.wait(1000)



# # Create an instance of DishwasherSemanticEvaluator
# evaluator = DishwasherSemanticEvaluator(env)
# def test_fragile_dish():
#     # Test for fragile dishes
#     fragile_dishes = ["glass_cup", "fragile_plate", "glass_bowl"]
#     for dish in fragile_dishes:
#             if evaluator.is_fragile(dish):
#                 print(f"The dish '{dish}' is fragile.")
#             else:
#                  return False
#     return True

# print("Testing fragile dishes:")
# test_result = test_fragile_dish()
# print(f"Test result for fragile dishes: {test_result}") 






# executor.wait(1000)