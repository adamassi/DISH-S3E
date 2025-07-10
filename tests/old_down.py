from sim_ur5.mujoco_env.sim_env import SimEnv
from math import pi
from sim_ur5.motion_planning.motion_executor import MotionExecutor
import time
from sim_ur5.mujoco_env.common.ur5e_fk import forward
from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator

from tests.places import dishwasher_objects
import math

# === Setup environment and evaluator ===
env = SimEnv()
executor = MotionExecutor(env)
evaluator = DishwasherSemanticEvaluator(env)

# === Prepare the scene ===
env.open_dishwasher_door()
executor.wait(30)
env.open_bottom_rack()
executor.wait(70)














# from sim_ur5.mujoco_env.sim_env import SimEnv
# from sim_ur5.motion_planning.motion_executor import MotionExecutor
# import math
# from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator
# from tests.places import dishwasher_objects_has_space_down_rack

# # === Setup ===
# env = SimEnv()
# executor = MotionExecutor(env)
# evaluator = DishwasherSemanticEvaluator(env)

# # === Setup dishwasher ===
# env.open_dishwasher_door()
# executor.wait(10)
# env.open_bottom_rack()
# executor.wait(70)

# # Combine both cups and wine_glasses
# cup_dict = {
#     **dishwasher_objects_has_space_down_rack["cups"],
#     **dishwasher_objects_has_space_down_rack["wine_glasses"]
# }

# cup_count = evaluator.num_cups_down_rack  # typically 12
# cup_names = list(cup_dict.keys())[:cup_count]




# # === Test 2: Fill utensils until full ===
# print("\n-- Test 2: Filling utensil rack to capacity --")

# utensil_count = evaluator.num_skom_down_rack  # typically 12
# utensil_names = list(dishwasher_objects_has_space_down_rack["utensils"].keys())
# # assert utensil_count <= len(utensil_names), "❌ Not enough utensils defined for full test"

# for name in utensil_names[:utensil_count]:
#     utensil = dishwasher_objects_has_space_down_rack["utensils"][name]
#     env.select_body(utensil["body"] + "/")
#     env.update_object_position_and_rotation(utensil["geom"], utensil["position"], utensil["rotation"])
#     executor.wait(50)
# executor.wait(300)
# # has_space_utensil = evaluator.has_space_utensil_rack()
# # print(f"has_space_utensil_rack() = {has_space_utensil}")
# # assert not has_space_utensil, "❌ Expected no space in utensil rack, but got True"
# # print("✅ Utensil rack correctly detected as full")

# executor.wait(1000)


















# for category in dishwasher_objects.values():
#     for obj in category.values():
#         env.select_body(obj["body"] + "/")  # Optional: select
#         env.update_object_position(obj["geom"], obj["position"])
#         # env.update_object_position_and_rotation(obj["geom"], obj["position"], obj["rotation"])  # if needed
#         executor.wait(70)


obj = dishwasher_objects["utensils"]["knife"]

# Select the object (this makes it the focus in simulation)
env.select_body(obj["body"] + "/")

# Move it to its designated position
print("[0, 0, pi/2] ")
env.update_object_position_and_rotation(obj["geom"], obj["position"], [0, 0, - math.pi / 2])
executor.wait(70)




obj = dishwasher_objects["utensils"]["spoon"]
obj2 = dishwasher_objects["utensils"]["knife"]
# Select the object (this makes it the focus in simulation)
env.select_body(obj["body"] + "/")




# Move it to its designated position
# env.update_object_position_and_rotation(obj2["geom"], [0.77, -0.21, 0.35], [0, 0, -math.pi / 2])    # this was ok
# env.update_object_position_and_rotation(obj2["geom"], [0.77, -0.175, 0.35], [0, 0, -math.pi / 2])
# executor.wait(70)
# env.select_body(obj2["body"] + "/")
# env.update_object_position_and_rotation(obj2["geom"], obj2["position"], [0, 0, math.pi / 2])
# executor.wait(70)




# cup2 = dishwasher_objects["cups"]["tall_cup_2"]
# env.select_body(cup2["body"] + "/")
# env.simulate_steps(20)
# # env.update_object_position_and_rotation(cup2["geom"], [0.77, -0.32, 1.5], [0, math.pi / 2, 0])
# # executor.wait(30)
# # env.show_label_above_body("hello hello hello", cup2["body"] + "/")
# # env.show_text_overlay("Selected", "tall_cup")

# # env.show_text("Your text here")

# env.update_object_position_and_rotation(cup2["geom"] + "o", [0.77, -0.32, 1.5], [0, 0, math.pi / 2])
# executor.wait(30)

# env.update_object_position_and_rotation(cup2["geom"], [0.77, -0.32, 1.5], [0, 0, -math.pi / 2])
# executor.wait(30)

# env.update_object_position_and_rotation(cup2["geom"], [0.77, -0.32, 1.5], [0, 0, -math.pi / 2])
# executor.wait(30)

# # env.update_object_position_and_rotation(obj["geom"], obj["position"], [0, 0, math.pi / 2])
# # executor.wait(70)
# # env.update_object_position_and_rotation(obj["geom"], obj["position"], [0, 0, math.pi / 2])
# # executor.wait(70)

# executor.wait(700)


# for category in dishwasher_objects.values():
#     for obj in category.values():
#         env.select_body(obj["body"] + "/")  # Optional: select
#         env.update_object_position(obj["geom"], obj["position"])
#         # env.update_object_position_and_rotation(obj["geom"], obj["position"], obj["rotation"])  # if needed
#         executor.wait(70)

# for cup in dishwasher_objects["cups"].values():
#     env.update_object_position(cup["geom"], cup["position"])
#     executor.wait(30)
# executor.wait(3000)





# cuo upowards
# env.update_object_position_and_rotation(cup2["geom"], [0.77, -0.32, 1.5], [0, 0, math.pi / 2])

# cup downwards
# env.update_object_position_and_rotation(cup2["geom"], [0.77, -0.32, 1.5], [0, 0, -math.pi / 2])