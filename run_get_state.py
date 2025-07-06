from sim_ur5.mujoco_env.sim_env import SimEnv
from sim_ur5.motion_planning.motion_executor import MotionExecutor
import time
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
# Test logic for checking space in the down rack
evaluator = DishwasherSemanticEvaluator(env)
env.valid_names_dishs()

time.sleep(5)  # Wait for the environment to stabilize
state=evaluator.get_state()
for key, value in state.items():
    print(f"{key}: {value}")

###########
#the dishwasher door is closed by default, so we need to open it
env.open_dishwasher_door()
time.sleep(10)  