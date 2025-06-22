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
def test_fragile_dish(self):
    # Test for fragile dishes
    fragile_dishes = ["glass_cup", "fragile_plate", "glass_bowl"]
    for dish in fragile_dishes:
            if self.evaluator.is_fragile(dish):
                print(f"The dish '{dish}' is fragile.")
            else:
                 return False
    return True

print("Testing fragile dishes:")
test_result = evaluator.test_fragile_dish() 
print(f"Test result for fragile dishes: {test_result}")





executor.wait(1000)