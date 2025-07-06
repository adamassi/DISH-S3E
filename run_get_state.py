from sim_ur5.mujoco_env.sim_env import SimEnv
from sim_ur5.motion_planning.motion_executor import MotionExecutor
import time
from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator

# Initialize the simulation environment
env = SimEnv()
# Initial positions of dishes and plate



executor = MotionExecutor(env)
# Test logic for checking space in the down rack
evaluator = DishwasherSemanticEvaluator(env)
dishes=env.valid_names_dishs()
print(f"the valid dishes are: {dishes}")

time.sleep(5)  # Wait for the environment to stabilize
state = evaluator.get_state()
# Iterate over answers and predicates
for answer, predicate in zip(state[0], state[1]):
    print(f"{predicate}: {answer}")
    #TODO ADD time sleep to see the results better 

###########
#the dishwasher door is closed by default, so we need to open it
env.open_dishwasher_door()
time.sleep(30)



