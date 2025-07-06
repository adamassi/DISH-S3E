# dishwasher_semantics.py
# This module defines semantic questions and their corresponding evaluation logic
# for determining whether a dish has been loaded into a dishwasher correctly.
#
# It includes:
# - Stability check of the dish
# - Space availability in the dishwasher
# - Fragility of the dish
# - Placement correctness based on dish type (e.g., cup vs. plate)
# - State extraction of semantic facts
# - Success scoring based on desired predicates

from typing import List, Tuple
import numpy as np

class DishwasherSemanticEvaluator:
    def __init__(self, env):
        # Reference to the simulation environment
        self.env = env
        # TODO : Initialize MAX_DISHES based on the capacity of the dishwasher
        self.num_dishs_top_rack = 6  # Example capacity, can be adjusted based on the environment
        self.num_cups_down_rack = 12  # Example capacity for the down rack, can be adjusted based on the environment
        self.num_skom_down_rack = 12
    """
    Valid names to use for the is_stable method:
    ['Dishwasher/', 'Dishwasher//unnamed_body_0', 'Dishwasher/dishwasher', 'Dishwasher/door', 'Dishwasher/top_rack', 
    'bin_dark_wood/', 'bin_dark_wood/bin_dark_wood', 'can/', 'can/object', 'dish0', 'dish1', 'dish2', 'dish3', 
    'plate/', 'plate/object', 'plate_1/', 'plate_1/object', 'rethink_mount_stationary/', 
    'rethink_mount_stationary/base', 'rethink_mount_stationary/controller_box', 'rethink_mount_stationary/pedestal', 
    'rethink_mount_stationary/pedestal_feet', 'rethink_mount_stationary/robot_0_ur5e/', 
    'rethink_mount_stationary/robot_0_ur5e/base', 'rethink_mount_stationary/robot_0_ur5e/forearm_link', 
    'rethink_mount_stationary/robot_0_ur5e/robot_0_adhesive gripper/', 
    'rethink_mount_stationary/robot_0_ur5e/robot_0_adhesive gripper/4boxes', 
    'rethink_mount_stationary/robot_0_ur5e/shoulder_link', 'rethink_mount_stationary/robot_0_ur5e/upper_arm_link', 
    'rethink_mount_stationary/robot_0_ur5e/wrist_1_link', 'rethink_mount_stationary/robot_0_ur5e/wrist_2_link', 
    'rethink_mount_stationary/robot_0_ur5e/wrist_3_link', 'rethink_mount_stationary/torso', 'table_black', 
    'table_wood', 'tale_white', 'world']
    **'plate/', 'plate/object': These are the names of the same plate object in the environment.
    """
    def is_stable(self, dish_name: str) -> bool:
        """
        Checks if a dish is placed stably on a surface by checking its orientation.

        Args:
            dish_name: The name of the dish to check.

        Returns:
            True if the dish is stable, False otherwise.
        """
        # Use the is_stable_orientation method from the environment
        if "wine_glass" in dish_name.lower() or "tall_cup" in dish_name.lower():
            # Wine glasses and tall cups are considered fragile and should not be checked for stability
            return self.env.is_stable_orientation(dish_name, 90)
        if "plate" in dish_name.lower():
            # Plates are considered stable if they are upright
            geom_names = self.env.get_valid_geometry_names()
            geom_name = next((name for name in geom_names if name.startswith(dish_name)), None)
            # print(f"Checking stability for plate: {geom_name}")
            # print(geom_names)
            gemo2_name = "Dishwasher/top_rack_base"
            normal_force = self.env.get_normal_force(geom_name, gemo2_name)
            if normal_force[2] not in [0, 0.0]: #its mean that the skom is in the down rack
                return self.env.is_stable_orientation(dish_name, 90,10)
            return self.env.is_stable_orientation(dish_name, 0)
       

        # return self.env.is_stable_orientation(dish_name, 0)  # Default orientation check for other dishes
        # lazem arg3ha 
        return True
    
    def has_space_top_rack(self) -> bool:
        """
        Checks if there's still available space in the top rack of the dishwasher.
        This is based on how many dishes are already placed in the top rack.

        Returns:
            True if there is space, False otherwise.
        """
        gemo2_name = "Dishwasher/top_rack_base"
        geom_names = self.env.get_valid_geometry_names()
        num_dishes = 0
        for geom_name in geom_names:
            if 'plate' in geom_name.lower():
                normal_force = self.env.get_normal_force(geom_name, gemo2_name)
                # print(f"Normal force on {geom_name} with respect to {gemo2_name}:")
                # print(normal_force)
                if normal_force[2] not in [0, 0.0]:
                    num_dishes += 1
        return num_dishes < self.num_dishs_top_rack
        
    def has_space_down_rack(self) -> bool:
        geom2_name= "Dishwasher//unnamed_geom_7"  
        geom_names = self.env.get_valid_geometry_names()
        num_cups = 0
        for geom_name in geom_names :
            if 'cup' in geom_name.lower() or 'glass' in geom_name.lower():
                normal_force = self.env.get_normal_force(geom_name, geom2_name)
                print(f"Normal force on {geom_name} with respect to {geom2_name}:")
                print(normal_force)
                if normal_force[2] not in [0, 0.0]:
                    num_cups += 1
        print(f"Number of cups/glasses in the dishwasher: {num_cups}")
        geom2_name='Dishwasher//unnamed_geom_8'
        num_skoms = 0
        for geom_name in geom_names :
            if 'spoon' in geom_name.lower() or 'fork' in geom_name.lower() or 'knife' in geom_name.lower():
                normal_force = self.env.get_normal_force(geom_name, geom2_name)
                print(f"Normal force on {geom_name} with respect to {geom2_name}:")
                print(normal_force)
                if normal_force[2] not in [0, 0.0]:
                    num_skoms += 1
        print(f"Number of spoons/forks/knives in the dishwasher: {num_skoms}")
        return (num_cups < self.num_cups_down_rack) and (num_skoms < self.num_skom_down_rack)
    def has_space(self) -> bool:
        """
        Checks if there's still available space in the dishwasher.
        This is based on how many dishes are already placed in a defined region.

        x_limit for the top rack when it is closed:
        x_min = 0.6 - 0.229 = 0.371
        x_max = 0.6 + 0.229 = 0.829
        Midpoint is:
            x = 0.6 + 0     = 0.6 
            y =
            z = 0.0 + 0.485 = 0.485
        when is closed:
        y_limit is:
        y_min = -0.625 - 0.2075 = -0.8325
        y_max = -0.625 + 0.2075 = -0.4175
        x_min = 0.4
        x_max = 0.8
        y_min = -0.151   
        y_max = -0.551
        down rack is:
        x_min = 0.4
        x_max = 0.8
        y_min = -0.151   
        y_max = -0.551
        z_min = 0.165
        z_max = 0.285
        """
        return  self.has_space_top_rack() and self.has_space_down_rack()
      

    def is_fragile(self, dish_name: str) -> bool:
        """
        Assumes fragility based on the name of the object.
        """
        return 'glass' in dish_name or 'fragile' in dish_name.lower() or 'plate' in dish_name.lower() or 'tall_cup' in dish_name.lower()

    def is_correct_slot(self, dish_name: str, expected_slot="") -> bool:
        """
        Determines whether the dish is placed in the correct rack according to type.
        """
    
        
        geom_names = self.env.get_valid_geometry_names()
        geom_name = next((name for name in geom_names if name.startswith(dish_name)), None)

        if expected_slot == 'cup':
            geom2_name= "Dishwasher//unnamed_geom_7"  
            # for geom_name in geom_names :

            # if 'cup' in geom_name.lower() or 'glass' in geom_name.lower():
            normal_force = self.env.get_normal_force(geom_name, geom2_name)
            print(f"Normal force on {geom_name} with respect to {geom2_name}:")
            print(normal_force)
            if normal_force[2] not in [0, 0.0]:
                return True
            return False
                    
        elif expected_slot == 'plate':
            geom2_name = "Dishwasher/top_rack_base"

            # if 'cup' in geom_name.lower() or 'glass' in geom_name.lower():
            normal_force = self.env.get_normal_force(geom_name, geom2_name)
            print(f"Normal force on {geom_name} with respect to {geom2_name}:")
            print(normal_force)
            if normal_force[2] not in [0, 0.0]:
                return True
            return False
        elif expected_slot == 'skom':
            geom2_name = "Dishwasher//unnamed_geom_8"
            # if 'cup' in geom_name.lower() or 'glass' in geom_name.lower():
            normal_force = self.env.get_normal_force(geom_name, geom2_name)
            print(f"Normal force on {geom_name} with respect to {geom2_name}:")
            print(normal_force)
            if normal_force[2] not in [0, 0.0]:
                return True
            return False
        return False
    def has_space_top_rack(self) -> bool:
        """
        Checks if there's still available space in the top rack of the dishwasher.
        This is based on how many dishes are already placed in the top rack.

        Returns:
            True if there is space, False otherwise.
        """
        gemo2_name = "Dishwasher/top_rack_base"
        geom_names = self.env.get_valid_geometry_names()
        num_dishes = 0
        for geom_name in geom_names:
            if 'plate' in geom_name.lower():
                normal_force = self.env.get_normal_force(geom_name, gemo2_name)
                # print(f"Normal force on {geom_name} with respect to {gemo2_name}:")
                # print(normal_force)
                if normal_force[2] not in [0, 0.0]:
                    num_dishes += 1
        return num_dishes < self.num_dishs_top_rack

    # def get_state(self) -> Tuple[np.ndarray, List[str]]:
    #     """
    #     Returns a binary vector and corresponding predicate list
    #     describing the current semantic state of the dishwasher domain.
    #     """
    #     predicates = []
    #     values = []
    #     for dish in self.env._object_manager.object_names:
    #         stable = self.is_stable(dish)
    #         predicates.append(f"IsStable({dish})")
    #         values.append(stable)

    #         fragile = self.is_fragile(dish)
    #         predicates.append(f"IsFragile({dish})")
    #         values.append(fragile)

    #         correct_slot = self.is_correct_slot(dish, 'plate')  # or infer type of dish
    #         predicates.append(f"InCorrectSlot({dish})")
    #         values.append(correct_slot)

    #     space = self.has_space()
    #     predicates.append("HasSpace")
    #     values.append(space)

    #     return np.array(values), predicates
    
    def get_state(self) -> Tuple[np.ndarray, List[str]]:
        """
        Evaluates the semantic state of the dishwasher environment.

        Returns:
            A tuple:
            - np.ndarray of booleans for each semantic question.
            - List of strings with the corresponding grounded predicates.
        """
        answers = []
        predicates = []

        # Get all geometry/dish names from the environment
        dish_names = self.env.get_valid_geometry_names()

        # === 1. Check individual dish-level semantics ===
        for name in dish_names:
        
            # 1a. Stability
            stable = self.is_stable(name)
            answers.append(stable)
            predicates.append(f"IsStable({name})")

            # 1b. Fragility
            fragile = self.is_fragile(name)
            answers.append(fragile)
            predicates.append(f"IsFragile({name})")

            # 1c. Correct placement
            expected_slot = ''
            if 'plate' in name.lower():
                expected_slot = 'plate'
            elif 'cup' in name.lower() or 'glass' in name.lower():
                expected_slot = 'cup'
            else: 
                expected_slot = 'skom'
            if expected_slot:
                correct_slot = self.is_correct_slot(name, expected_slot)
                answers.append(correct_slot)
                predicates.append(f"CorrectSlot({name}, {expected_slot})")

        # === 2. Check global dishwasher state ===

        # 2a. Space in top rack
        top_space = self.has_space_top_rack()
        answers.append(top_space)
        predicates.append("HasSpace(top_rack)")

        # 2b. Space in bottom rack
        bottom_space = self.has_space_down_rack()
        answers.append(bottom_space)
        predicates.append("HasSpace(bottom_rack)")

        # 2c. Overall space
        overall_space = self.has_space()
        answers.append(overall_space)
        predicates.append("HasSpace(dishwasher)")

        # === Return final state ===
        return np.array(answers, dtype=bool), predicates
    
    def success_score(self, state: Tuple[np.ndarray, List[str]], goal: List[str]) -> float:
        """
        Computes a score (0–100) that measures how close the current state is to satisfying the goal predicates.

        Args:
            state: Tuple of (answers_array, predicates_list) from get_state().
            goal: List of grounded predicates (strings) that define the desired goal state.

        Returns:
            A float score between 0 and 100.
        """
        answers, predicates = state

        # Map from predicate to its boolean value
        state_dict = dict(zip(predicates, answers))

        # Track per-object score and total weight
        total_score = 0.0
        object_scores = []
        valid_objects = []

        # Precompute slot availability
        top_rack_has_space = self.has_space_top_rack()
        bottom_rack_has_space = self.has_space_down_rack()

        for pred in goal:
            if pred.startswith("CorrectSlot("):
                # Extract object name and expected slot
                inside = pred[len("CorrectSlot("):-1]
                obj_name, expected_slot = [s.strip() for s in inside.split(",")]

                correct_slot_pred = f"CorrectSlot({obj_name}, {expected_slot})"
                stable_pred = f"IsStable({obj_name})"

                correct_slot = state_dict.get(correct_slot_pred, False)

                # Determine if the correct slot is full
                if not correct_slot:
                    if expected_slot == 'plate' and not top_rack_has_space:
                        continue  # skip object
                    elif expected_slot == 'cup' and not bottom_rack_has_space:
                        continue  # skip object

                # Now count it as a valid object
                valid_objects.append(obj_name)

                if correct_slot:
                    is_stable = state_dict.get(stable_pred, False)
                    obj_score = 100 if is_stable else 70  # you can change 70 to any value you want
                else:
                    obj_score = 0

                object_scores.append(obj_score)

        # Score per-object (weighted evenly)
        if valid_objects:
            total_object_score = sum(object_scores)
            object_score = total_object_score / len(valid_objects)
        else:
            object_score = 0

        # Optional: Add global predicates
        global_score = 0
        global_weights = {
            "HasSpace(top_rack)": 7,
            "HasSpace(bottom_rack)": 7,
            "HasSpace(dishwasher)": 6,
        }

        for pred, weight in global_weights.items():
            if pred in goal and state_dict.get(pred, False):
                global_score += weight

        # Final score
        final_score = object_score * 0.8 + global_score  # 80% object-based, 20% global

        return round(final_score, 2)


    # def success_score(self, state: np.ndarray, goal_predicates: List[str], all_predicates: List[str]) -> float:
    #     """
    #     Computes a success score based on how many goal predicates are satisfied.
    #     Returns a float between 0 and 1.
    #     """
    #     success_flags = [(pred in goal_predicates and state[i]) for i, pred in enumerate(all_predicates)]
    #     return sum(success_flags) / len(goal_predicates) if goal_predicates else 0.0
