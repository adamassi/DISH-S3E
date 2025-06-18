from sim_ur5.mujoco_env.sim_env import SimEnv
from math import pi
from sim_ur5.motion_planning.motion_executor import MotionExecutor
import time
from sim_ur5.mujoco_env.common.ur5e_fk import forward
from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator



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



# Create an instance of DishwasherSemanticEvaluator
evaluator = DishwasherSemanticEvaluator(env)

# Specify the dish name to check stability
dish_name = "dish0_fj"  # Replace with the actual dish name in your environment

# Call the is_stable method
is_stable_result = evaluator.is_stable(dish_name)

# Print the result
print(f"Is the dish '{dish_name}' stable? {is_stable_result}")

executor.wait(1000)