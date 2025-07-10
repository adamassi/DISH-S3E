from sim_ur5.mujoco_env.sim_env import SimEnv
from math import pi
from sim_ur5.motion_planning.motion_executor import MotionExecutor
import time
from sim_ur5.mujoco_env.common.ur5e_fk import forward
from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator
import math

env = SimEnv()

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



env.open_dishwasher_door()
executor.wait(30)
env.open_bottom_rack()
executor.wait(30)



print("Selecting tall_cup_5/...")
env.select_body("tall_cup_5/")
# executor.wait(30) # Wait 3 seconds to see the selection

cup_joint_name = "tall_cup_5/dish24_fj/" 

# 2. Rotate the cup 90 degrees onto its side (pitch rotation)
print(f"Rotating {cup_joint_name} onto its side...")
# Angles are [roll, pitch, yaw] in radians. math.pi / 2 is 90 degrees.
rotation_on_side = [0, math.pi / 2, 0] 
env.rotate_object(cup_joint_name, rotation_on_side)
executor.wait(300) # Pause for 3 seconds to see the result

# 3. Rotate the cup back to its original upright position
print(f"Rotating {cup_joint_name} back to upright...")
rotation_upright = [0, 0, 0]
env.rotate_object(cup_joint_name, rotation_upright)
executor.wait(3000)


env.open_dishwasher_door()
executor.wait(30)
# env.open_bottom_rack()
# executor.wait(30) # Wait 3 seconds to see the bottom rack opening

# 2. Select a different object. This automatically deselects the Dishwasher.
print("Selecting the bottom rack...")
env.select_body("Dishwasher/bottom_rack")
executor.wait(30) # Wait 3 seconds

# selecting the spoon
print("Selecting the wooden spoon...")
env.select_body("tall_cup_5/")
executor.wait(50) # Wait 3 seconds

# 3. Unselect everything
print("Deselecting all objects...")
env.select_body(None)
executor.wait(30)

print("Dishwasher door opened and bottom rack slid outtttttttttttttttttttttttttttttt\n \n \n \n \n tttttt \n.")

evaluator = DishwasherSemanticEvaluator(env)

positions = [
    [0.5, -0.3, 0.2],  # Dish 1 in the down rack
    [0.6, -0.4, 0.25],  # Dish 2 in the down rack
    [0.7, -0.5, 0.18],  # Dish 3 in the down rack
]
# evaluator.has_space()



env.update_object_position('tall_cup_2/dish21_fj/',[0.43,-0.3,0.25])
executor.wait(40)
env.update_object_position('tall_cup_1/dish20_fj/',[0.43,-0.2,0.26])
executor.wait(30)

