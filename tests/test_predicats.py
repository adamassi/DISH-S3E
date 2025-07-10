from sim_ur5.mujoco_env.sim_env import SimEnv
from sim_ur5.motion_planning.motion_executor import MotionExecutor
from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator
from tests.places import dishwasher_objects
import math

# === Setup ===
env = SimEnv()
executor = MotionExecutor(env)
evaluator = DishwasherSemanticEvaluator(env)

# === Open dishwasher for manual placements ===
env.open_dishwasher_door()
executor.wait(10)
env.open_bottom_rack()
executor.wait(30)

# === MANUALLY PLACE OBJECTS HERE ===
# You can change positions below to experiment and re-run

# Example object placements (edit freely)
cup = dishwasher_objects["cups"]["tall_cup_4"]
env.select_body(cup["body"] + "/")
env.update_object_position_and_rotation(cup["geom"], [0.43, -0.52, 0.27], [0, 0, 0])
executor.wait(10)

spoon = dishwasher_objects["utensils"]["spoon"]
env.select_body(spoon["body"] + "/")
env.update_object_position_and_rotation(spoon["geom"], spoon["position"], [0, 0, math.pi/2])
executor.wait(10)

knife = dishwasher_objects["utensils"]["knife"]
env.select_body(knife["body"] + "/")
env.update_object_position_and_rotation(knife["geom"], knife["position"], [0, 0, math.pi/2])
executor.wait(10)

# === Define goal predicates ===
# Feel free to modify this list to match new setups
goal = [
    f"CorrectSlot({cup['body'] + '/'}, cup)",
    f"IsStable({cup['body'] + '/'})",
    f"CorrectSlot({spoon['body'] + '/'}, skom)",
    f"CorrectSlot({knife['body'] + '/'}, skom)",
    "HasSpace(top_rack)",
    "HasSpace(bottom_rack)",
    "HasSpace(dishwasher)"
]

# === Evaluate current state ===
print("\n=== [STATE] Semantic Evaluation ===")
state = evaluator.get_state()
answers, predicates = state
for pred, value in zip(predicates, answers):
    print(f"{pred}: {value}")

# === Evaluate success score ===
print("\n=== [SCORE] Success Score Against Goal ===")
score = evaluator.success_score(state, goal)
print(f"\nSuccess Score: {score}/100")

executor.wait(1000)