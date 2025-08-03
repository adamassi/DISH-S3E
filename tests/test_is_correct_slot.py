import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sim_ur5.mujoco_env.sim_env import SimEnv
from sim_ur5.motion_planning.motion_executor import MotionExecutor
import math
from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator
from tests.places import dishwasher_objects

# === Setup environment and evaluator ===
env = SimEnv()
executor = MotionExecutor(env)
evaluator = DishwasherSemanticEvaluator(env)

# === Prepare the scene ===
env.open_dishwasher_door()
executor.wait(30)
env.open_bottom_rack()
executor.wait(70)



# --- 1. tall_cup_1 (Incorrect slot: lying on side)
cup1 = dishwasher_objects["cups"]["tall_cup_1"]
env.select_body(cup1["body"] + "/")
env.simulate_steps(200)
env.update_object_position_and_rotation(cup1["geom"], [0.43, -0.25, 0.32], [0, math.pi / 2, 0])
executor.wait(30)

# --- 2. tall_cup_4 (Correctly placed in bottom rack)
cup4 = dishwasher_objects["cups"]["tall_cup_4"]
env.select_body(cup4["body"] + "/")
env.update_object_position(cup4["geom"], [0.43, -0.52, 0.27])
executor.wait(70)

# --- 3. spoon (Correctly placed in utensil tray)
spoon = dishwasher_objects["utensils"]["spoon"]
env.select_body(spoon["body"] + "/")
env.update_object_position_and_rotation(spoon["geom"], spoon["position"], [0, 0, math.pi / 2])
executor.wait(70)

# --- 4. knife (Correctly placed in utensil tray)
knife = dishwasher_objects["utensils"]["knife"]
env.select_body(knife["body"] + "/")
env.update_object_position_and_rotation(knife["geom"], [0.77, -0.175, 0.35], [0, 0, -math.pi / 2])
executor.wait(70)

# === Run is_correct_slot checks ===

print("\n[TEST] Checking is_correct_slot results:")

# 1. tall_cup_1 → Expected: False
result = evaluator.is_correct_slot(cup1["body"] + "/", expected_slot="cup")
print(f"{cup1['body']}: is_correct_slot = {result}")
assert not result, f"❌ Expected {cup1['body']} to be in wrong slot, but got True"
print(f"✅ {cup1['body']} correctly detected in wrong slot")
executor.wait(300)

# 2. tall_cup_4 → Expected: True
result = evaluator.is_correct_slot(cup4["body"] + "/", expected_slot="cup")
print(f"{cup4['body']}: is_correct_slot = {result}")
assert result, f"❌ Expected {cup4['body']} to be in correct slot, but got False"
print(f"✅ {cup4['body']} correctly detected in correct slot")
executor.wait(300)

# 3. spoon → Expected: True
result = evaluator.is_correct_slot(spoon["body"] + "/", expected_slot="skom")
print(f"{spoon['body']}: is_correct_slot = {result}")
assert result, f"❌ Expected {spoon['body']} to be in correct slot, but got False"
print(f"✅ {spoon['body']} correctly detected in correct slot")
executor.wait(300)

# 4. knife → Expected: True
result = evaluator.is_correct_slot(knife["body"] + "/", expected_slot="skom")
print(f"{knife['body']}: is_correct_slot = {result}")
assert result, f"❌ Expected {knife['body']} to be in correct slot, but got False"
print(f"✅ {knife['body']} correctly detected in correct slot")
executor.wait(300)


# --- 5. tall_cup_2 (Incorrect slot: in the spoon section)
cup2 = dishwasher_objects["cups"]["tall_cup_2"]
env.select_body(cup2["body"] + "/")
env.simulate_steps(200)
env.update_object_position_and_rotation(cup2["geom"], [0.77, -0.32, 0.4], [0, math.pi / 2, 0])
executor.wait(30)

# 5. tall_cup_2 → Expected: False
result = evaluator.is_correct_slot(cup2["body"] + "/", expected_slot="cup")
print(f"{cup2['body']}: is_correct_slot = {result}")
assert not result, f"❌ Expected {cup2['body']} to be in wrong slot, but got True"
print(f"✅ {cup2['body']} correctly detected in wrong slot")
executor.wait(300)


# --- 5. spoon (Correctly placed in utensil tray)
spoon1 = dishwasher_objects["utensils"]["spoon_1"]
env.select_body(spoon1["body"] + "/")
env.update_object_position_and_rotation(spoon1["geom"], [0.63, -0.3, 0.27], [0, 0, math.pi / 2])
executor.wait(70)

# 3. spoon → Expected: False
result = evaluator.is_correct_slot(spoon1["body"] + "/", expected_slot="skom")
print(f"{spoon1['body']}: is_correct_slot = {result}")
assert not result, f"❌ Expected {spoon1['body']} to be in wrong slot, but got True"
print(f"✅ {spoon1['body']} correctly detected in wrong slot")
executor.wait(300)

executor.wait(1000)