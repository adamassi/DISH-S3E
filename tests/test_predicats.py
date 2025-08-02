from sim_ur5.mujoco_env.sim_env import SimEnv
from sim_ur5.motion_planning.motion_executor import MotionExecutor
from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator
from tests.places import dishwasher_objects
import math
from tests.places import dishwasher_objects_has_space_down_rack

# === Setup ===
env = SimEnv()
executor = MotionExecutor(env)
evaluator = DishwasherSemanticEvaluator(env)

# === Open dishwasher ===
env.open_dishwasher_door()
executor.wait(10)
env.open_bottom_rack()
executor.wait(30)

# === Place Initial Objects ===
cup = dishwasher_objects["cups"]["tall_cup_4"]
spoon = dishwasher_objects["utensils"]["spoon"]
knife = dishwasher_objects["utensils"]["knife"]

env.select_body(cup["body"] + "/")
env.update_object_position_and_rotation(cup["geom"], [0.43, -0.52, 0.27], [0, 0, 0])
executor.wait(10)

env.select_body(spoon["body"] + "/")
env.update_object_position_and_rotation(spoon["geom"], spoon["position"], [0, 0, math.pi/2])
executor.wait(10)

env.select_body(knife["body"] + "/")
env.update_object_position_and_rotation(knife["geom"], knife["position"], [0, 0, - math.pi/2])
executor.wait(10)

# === Goal 1 ===
goal_1 = {
    "CorrectSlot(tall_cup_4, cup)": True,
    "IsStable(tall_cup_4)": True,
    "CorrectSlot(spoon, skom)": True,
    "IsStable(spoon)": True,
    "CorrectSlot(knife, skom)": True,
    "IsStable(knife)": True
}

# === Evaluate state and Goal 1 ===
print("\n=== [STATE] Semantic Evaluation ===")
state = evaluator.get_state()
answers, predicates = state
for pred, value in zip(predicates, answers):
    print(f"{pred}: {value}")

print("\n=== [SCORE] Against Goal 1 ===")
score_1 = evaluator.success_score(state, goal_1)
print(f"\nSuccess Score: {score_1}/100")

executor.wait(500)


# === fix the knife ===
knife = dishwasher_objects_has_space_down_rack["utensils"]["knife"]
env.select_body(knife["body"] + "/")
env.update_object_position_and_rotation(knife["geom"], knife["position"], [0, 0, - math.pi/2])
executor.wait(10)

state = evaluator.get_state()
answers, predicates = state
score_3 = evaluator.success_score(state, goal_1)
score_1 = evaluator.success_score(state, goal_1)
print(f"\nSuccess Score: {score_3}/100")

executor.wait(100)


# === Fill Dishwasher ===
cup_dict = {**dishwasher_objects_has_space_down_rack["cups"], **dishwasher_objects_has_space_down_rack["wine_glasses"]}
cup_names = list(cup_dict.keys())[:evaluator.num_cups_down_rack]

for name in cup_names:
    cup_obj = cup_dict[name]
    env.select_body(cup_obj["body"] + "/")
    env.update_object_position_and_rotation(cup_obj["geom"], cup_obj["position"], [0, 0, math.pi / 2])
    executor.wait(50)

utensil_names = list(dishwasher_objects_has_space_down_rack["utensils"].keys())[:evaluator.num_skom_down_rack]

for name in utensil_names:
    utensil = dishwasher_objects_has_space_down_rack["utensils"][name]
    env.select_body(utensil["body"] + "/")
    env.update_object_position_and_rotation(utensil["geom"], utensil["position"], utensil["rotation"])
    executor.wait(50)

executor.wait(100)

# === Evaluate state after everything ===
print("\n=== [STATE] Semantic Evaluation AFTER FILL ===")
state_filled = evaluator.get_state()
answers_filled, predicates_filled = state_filled
for pred, value in zip(predicates_filled, answers_filled):
    print(f"{pred}: {value}")

# === Goal 2: From previous output ===
goal_2 = {
    "IsObjectGrasped": False,
    "IsStable(plate)": True,
    "IsFragile(plate)": True,
    "CorrectSlot(plate, plate)": False,
    "IsStable(plate_1)": True,
    "IsFragile(plate_1)": True,
    "CorrectSlot(plate_1, plate)": False,
    "IsStable(knife)": True,
    "IsFragile(knife)": False,
    "CorrectSlot(knife, skom)": True,
    "IsStable(wine_glass)": True,
    "IsFragile(wine_glass)": True,
    "CorrectSlot(wine_glass, cup)": True,
    "IsStable(wine_glass_1)": True,
    "IsFragile(wine_glass_1)": True,
    "CorrectSlot(wine_glass_1, cup)": True,
    "IsStable(wine_glass_2)": True,
    "IsFragile(wine_glass_2)": True,
    "CorrectSlot(wine_glass_2, cup)": True,
    "IsStable(wine_glass_3)": False,
    "IsFragile(wine_glass_3)": True,
    "CorrectSlot(wine_glass_3, cup)": False,
    "IsStable(tall_cup)": True,
    "IsFragile(tall_cup)": True,
    "CorrectSlot(tall_cup, cup)": True,
    "IsStable(tall_cup_1)": True,
    "IsFragile(tall_cup_1)": True,
    "CorrectSlot(tall_cup_1, cup)": True,
    "IsStable(tall_cup_2)": True,
    "IsFragile(tall_cup_2)": True,
    "CorrectSlot(tall_cup_2, cup)": True,
    "IsStable(tall_cup_3)": True,
    "IsFragile(tall_cup_3)": True,
    "CorrectSlot(tall_cup_3, cup)": True,
    "IsStable(tall_cup_4)": True,
    "IsFragile(tall_cup_4)": True,
    "CorrectSlot(tall_cup_4, cup)": True,
    "IsStable(tall_cup_5)": True,
    "IsFragile(tall_cup_5)": True,
    "CorrectSlot(tall_cup_5, cup)": True,
    "IsStable(tall_cup_6)": True,
    "IsFragile(tall_cup_6)": True,
    "CorrectSlot(tall_cup_6, cup)": True,
    "IsStable(tall_cup_7)": True,
    "IsFragile(tall_cup_7)": True,
    "CorrectSlot(tall_cup_7, cup)": True,
    "IsStable(tall_cup_8)": True,
    "IsFragile(tall_cup_8)": True,
    "CorrectSlot(tall_cup_8, cup)": True,
    "IsStable(spoon)": True,
    "IsFragile(spoon)": False,
    "CorrectSlot(spoon, skom)": True,
    "IsStable(spoon_1)": True,
    "IsFragile(spoon_1)": False,
    "CorrectSlot(spoon_1, skom)": True,
    "HasSpace(top_rack)": True,
    "HasSpace(cup_rack)": False,
    "HasSpace(utensil_rack)": True
}

# === Evaluate score ===
print("\n=== [SCORE] Against Full Goal 2 ===")
score_2 = evaluator.success_score(state_filled, goal_2)
print(f"\nSuccess Score: {score_2}/100")

executor.wait(1000)
































# from sim_ur5.mujoco_env.sim_env import SimEnv
# from sim_ur5.motion_planning.motion_executor import MotionExecutor
# from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator
# from tests.places import dishwasher_objects
# import math
# from tests.places import dishwasher_objects_has_space_down_rack

# # === Setup ===
# env = SimEnv()
# executor = MotionExecutor(env)
# evaluator = DishwasherSemanticEvaluator(env)

# # === Open dishwasher ===
# env.open_dishwasher_door()
# executor.wait(10)
# env.open_bottom_rack()
# executor.wait(30)

# # === Place 3 initial objects ===
# cup = dishwasher_objects["cups"]["tall_cup_4"]
# spoon = dishwasher_objects["utensils"]["spoon"]
# knife = dishwasher_objects["utensils"]["knife"]

# env.select_body(cup["body"] + "/")
# env.update_object_position_and_rotation(cup["geom"], [0.43, -0.52, 0.27], [0, 0, 0])
# executor.wait(10)

# env.select_body(spoon["body"] + "/")
# env.update_object_position_and_rotation(spoon["geom"], spoon["position"], [0, 0, math.pi/2])
# executor.wait(10)

# env.select_body(knife["body"] + "/")
# env.update_object_position_and_rotation(knife["geom"], knife["position"], [0, 0, -math.pi/2])
# executor.wait(10)

# # === First goal: all 3 placed correctly & stable ===
# goal = [
#     f"CorrectSlot({cup['body'] + '/'}, cup)",
#     f"IsStable({cup['body'] + '/'})",
#     f"CorrectSlot({spoon['body'] + '/'}, skom)",
#     f"IsStable({spoon['body'] + '/'})",
#     f"CorrectSlot({knife['body'] + '/'}, skom)",
#     f"IsStable({knife['body'] + '/'})",
# ]

# print("\n=== [STATE] After Placing 3 Objects ===")
# state = evaluator.get_state()
# for pred, val in zip(state[1], state[0]):
#     print(f"{pred}: {val}")

# print("\n=== [SCORE] Goal: all 3 objects correctly placed and stable ===")
# score = evaluator.success_score(state, goal)
# print(f"Success Score: {score}/100")

# executor.wait(500)

# # === Second goal: only cup, spoon, knife in correct slot & stable ===
# goal = [
#     f"CorrectSlot({cup['body'] + '/'}, cup)",
#     f"IsStable({cup['body'] + '/'})",
#     f"CorrectSlot({spoon['body'] + '/'}, skom)",
#     f"IsStable({spoon['body'] + '/'})",
#     f"CorrectSlot({knife['body'] + '/'}, skom)",
#     f"IsStable({knife['body'] + '/'})",
# ]

# print("\n=== [SCORE] Goal: only cup, spoon, knife ===")
# score = evaluator.success_score(state, goal)
# print(f"Success Score: {score}/100")

# # === Fill dishwasher completely ===
# cup_dict = {
#     **dishwasher_objects_has_space_down_rack["cups"],
#     **dishwasher_objects_has_space_down_rack["wine_glasses"]
# }
# cup_count = evaluator.num_cups_down_rack
# cup_names = list(cup_dict.keys())[:cup_count]

# for name in cup_names:
#     obj = cup_dict[name]
#     env.select_body(obj["body"] + "/")
#     env.update_object_position_and_rotation(obj["geom"], obj["position"], [0, 0, math.pi / 2])
#     executor.wait(30)

# utensil_count = evaluator.num_skom_down_rack
# utensils = list(dishwasher_objects_has_space_down_rack["utensils"].values())[:utensil_count]

# for utensil in utensils:
#     env.select_body(utensil["body"] + "/")
#     env.update_object_position_and_rotation(utensil["geom"], utensil["position"], utensil["rotation"])
#     executor.wait(30)

# executor.wait(100)

# # === Final Evaluation ===
# print("\n=== [STATE] After Full Placement ===")
# state = evaluator.get_state()
# for pred, val in zip(state[1], state[0]):
#     print(f"{pred}: {val}")

# # === Build goal from state dynamically ===
# goal = [p for p in state[1] if p.startswith("CorrectSlot(") or p.startswith("IsStable(")]

# print("\n=== [SCORE] Goal: Everything in correct slot and stable ===")
# score = evaluator.success_score(state, goal)
# print(f"Success Score: {score}/100")

# executor.wait(1000)






















# from sim_ur5.mujoco_env.sim_env import SimEnv
# from sim_ur5.motion_planning.motion_executor import MotionExecutor
# from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator
# from tests.places import dishwasher_objects
# import math
# from tests.places import dishwasher_objects_has_space_down_rack

# # === Setup ===
# env = SimEnv()
# executor = MotionExecutor(env)
# evaluator = DishwasherSemanticEvaluator(env)

# # === Open dishwasher for manual placements ===
# env.open_dishwasher_door()
# executor.wait(10)
# env.open_bottom_rack()
# executor.wait(30)

# # === MANUALLY PLACE OBJECTS HERE ===
# # You can change positions below to experiment and re-run


# cup = dishwasher_objects["cups"]["tall_cup_4"]
# env.select_body(cup["body"] + "/")
# env.update_object_position_and_rotation(cup["geom"], [0.43, -0.52, 0.27], [0, 0, 0])
# executor.wait(10)

# spoon = dishwasher_objects["utensils"]["spoon"]
# env.select_body(spoon["body"] + "/")
# env.update_object_position_and_rotation(spoon["geom"], spoon["position"], [0, 0, math.pi/2])
# executor.wait(10)

# knife = dishwasher_objects["utensils"]["knife"]
# env.select_body(knife["body"] + "/")
# env.update_object_position_and_rotation(knife["geom"], knife["position"], [0, 0, - math.pi/2])
# executor.wait(10)

# # === Define goal predicates ===
# # Feel free to modify this list to match new setups
# goal = [
#     f"CorrectSlot({cup['body'] + '/'}, cup)",
#     f"IsStable({cup['body'] + '/'})",
#     f"CorrectSlot({spoon['body'] + '/'}, skom)",
#     f"CorrectSlot({knife['body'] + '/'}, skom)",
#     "HasSpace(top_rack)",
#     "HasSpace(bottom_rack)",
#     "HasSpace(dishwasher)"
# ]

# # === Evaluate current state ===
# print("\n=== [STATE] Semantic Evaluation ===")
# state = evaluator.get_state()
# answers, predicates = state
# for pred, value in zip(predicates, answers):
#     print(f"{pred}: {value}")

# # === Evaluate success score ===
# print("\n=== [SCORE] Success Score Against Goal ===")
# score = evaluator.success_score(state, goal)
# print(f"\nSuccess Score: {score}/100")

# # executor.wait(100)


# # === second set ===

# executor.wait(500)









# # Combine both cups and wine_glasses
# cup_dict = {
#     **dishwasher_objects_has_space_down_rack["cups"],
#     **dishwasher_objects_has_space_down_rack["wine_glasses"]
# }

# cup_count = evaluator.num_cups_down_rack  # typically 12
# cup_names = list(cup_dict.keys())[:cup_count]

# for name in cup_names:
    
#     cup = cup_dict[name]
#     env.select_body(cup["body"] + "/")
#     env.update_object_position_and_rotation(cup["geom"], cup["position"], [0, 0, math.pi / 2])
#     executor.wait(50)






# # === Test 2: Fill utensils until full ===

# utensil_count = evaluator.num_skom_down_rack  # typically 12
# utensil_names = list(dishwasher_objects_has_space_down_rack["utensils"].keys())
# # assert utensil_count <= len(utensil_names), "❌ Not enough utensils defined for full test"

# for name in utensil_names[:utensil_count]:
#     utensil = dishwasher_objects_has_space_down_rack["utensils"][name]
#     env.select_body(utensil["body"] + "/")
#     env.update_object_position_and_rotation(utensil["geom"], utensil["position"], utensil["rotation"]) #[0, 0, - math.pi / 2])
#     executor.wait(50)





# executor.wait(100)


# # === Evaluate current state ===
# print("\n=== [STATE] Semantic Evaluation ===")
# state = evaluator.get_state()
# answers, predicates = state
# for pred, value in zip(predicates, answers):
#     print(f"{pred}: {value}")

# # === Evaluate success score ===
# print("\n=== [SCORE] Success Score Against Goal ===")
# score = evaluator.success_score(state, goal)
# print(f"\nSuccess Score: {score}/100")

# executor.wait(1000)