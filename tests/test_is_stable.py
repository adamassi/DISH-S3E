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

# === Test 1: Unstable cup ===
cup1_body = 'tall_cup_1/'
cup1_geom = 'tall_cup_1/dish20_fj/'

print(f"\n[TEST 1] Placing {cup1_body} on its side (should be unstable)...")
env.select_body(cup1_body)
env.simulate_steps(200)
env.update_object_position_and_rotation(cup1_geom, [0.43, -0.25, 0.32], [0, math.pi/2, 0])
executor.wait(30)

is_stable = evaluator.is_stable(cup1_body)
print(f"Stability result for {cup1_body}: {is_stable}")
assert not is_stable, f"❌ Expected {cup1_body} to be unstable, but got stable=True"
print("✅ Test 1 passed: cup on side correctly detected as unstable.")

executor.wait(300)

# === Test 2: Stable cup ===
cup2_body = 'tall_cup_4/'
cup2_geom = 'tall_cup_4/dish23_fj/'

print(f"\n[TEST 2] Placing {cup2_body} upright (should be stable)...")
env.select_body(cup2_body)
executor.wait(30)
env.update_object_position(cup2_geom, [0.43, -0.52, 0.27])
executor.wait(100)

is_stable = evaluator.is_stable(cup2_body)
print(f"Stability result for {cup2_body}: {is_stable}")
assert is_stable, f"❌ Expected {cup2_body} to be stable, but got stable=False"
print("✅ Test 2 passed: upright cup correctly detected as stable.")

executor.wait(300)

# === Test 3: Stable spoon ===
spoon = dishwasher_objects["utensils"]["spoon"]
print(f"\n[TEST 3] Placing {spoon['body']} in correct slot (should be stable)...")
env.select_body(spoon["body"] + "/")
env.update_object_position_and_rotation(spoon["geom"], spoon["position"], [0, 0, math.pi / 2])
executor.wait(100)

is_stable = evaluator.is_stable(spoon["body"] + "/")
print(f"Stability result for {spoon['body']}: {is_stable}")
assert is_stable, f"❌ Expected {spoon['body']} to be stable, but got stable=False"
print("✅ Test 3 passed: spoon correctly detected as stable.")

executor.wait(300)

# === Test 4: Stable knife ===
knife = dishwasher_objects["utensils"]["knife"]
print(f"\n[TEST 4] Placing {knife['body']} in correct slot (should be stable)...")
env.select_body(knife["body"] + "/")
env.update_object_position_and_rotation(knife["geom"], knife["position"], [0, 0, math.pi / 2])
executor.wait(70)

is_stable = evaluator.is_stable(knife["body"] + "/")
print(f"Stability result for {knife['body']}: {is_stable}")
assert is_stable, f"❌ Expected {knife['body']} to be stable, but got stable=False"
print("✅ Test 4 passed: knife correctly detected as stable.")

executor.wait(1000)


# from sim_ur5.mujoco_env.sim_env import SimEnv
# from sim_ur5.motion_planning.motion_executor import MotionExecutor
# import math
# from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator

# from tests.places import dishwasher_objects


# # === Setup environment and evaluator ===
# env = SimEnv()
# executor = MotionExecutor(env)
# evaluator = DishwasherSemanticEvaluator(env)

# # === Prepare the scene ===
# env.open_dishwasher_door()
# executor.wait(30)
# env.open_bottom_rack()
# executor.wait(70)



# # === Test 1: Unstable cup ===
# cup1_body = 'tall_cup_1/'
# cup1_geom = 'tall_cup_1/dish20_fj/'

# print(f"\n[TEST 1] Placing {cup1_body} on its side (should be unstable)...")
# env.select_body(cup1_body)
# env.simulate_steps(200)
# # env.show_custom_label(cup1_body, "hello hello hello")
# # executor.wait(700)
# # Place on side
# env.update_object_position_and_rotation(cup1_geom, [0.43, -0.25, 0.32], [0, math.pi/2, 0])
# executor.wait(30)

# # Check stability
# is_stable = evaluator.is_stable(cup1_body)
# print(f"Stability result for {cup1_body}: {is_stable}")
# assert not is_stable, f"❌ Expected {cup1_body} to be unstable, but got stable=True"
# print("✅ Test 1 passed: cup on side correctly detected as unstable.")


# executor.wait(300)

# # === Test 2: Stable cup ===
# cup2_body = 'tall_cup_4/'
# cup2_geom = 'tall_cup_4/dish23_fj/'

# print(f"\n[TEST 2] Placing {cup2_body} upright (should be stable)...")
# env.select_body(cup2_body)
# executor.wait(30)  # Wait to see the selection
# env.update_object_position(cup2_geom, [0.43, -0.52, 0.27])
# executor.wait(100)

# # Check stability
# is_stable = evaluator.is_stable(cup2_body)
# print(f"Stability result for {cup2_body}: {is_stable}")
# assert is_stable, f"❌ Expected {cup2_body} to be stable, but got stable=False"
# print("✅ Test 2 passed: upright cup correctly detected as stable.")


# executor.wait(300)

