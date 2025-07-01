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
        return self.env.is_stable_orientation(dish_name)
    def has_space_top_rack(self) -> bool:
        """
        Checks if there's still available space in the top rack of the dishwasher.
        This is based on how many dishes are already placed in the top rack.

        Returns:
            True if there is space, False otherwise.
        """
        # Count the number of dishes in the upper rack (y > 0.5)
        occupied = len([d for d in self.env._object_manager.object_names
                        if self.env._object_manager.get_object_pos(d)[1] > 0.5])
        
        # Check if the number of dishes is less than the maximum capacity
        return occupied < self.num_dishs_top_rack
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
        
        # Count the number of dishes in the upper rack (y > 0.5)
        occupied = len([d for d in self.env._object_manager.object_names
                        if self.env._object_manager.get_object_pos(d)[1] > 0.5])
        
        # Check if the number of dishes is less than the maximum capacity
        return occupied < self.env.num_dishs

    def is_fragile(self, dish_name: str) -> bool:
        """
        Assumes fragility based on the name of the object.
        """
        return 'glass' in dish_name or 'fragile' in dish_name.lower()

    def is_correct_slot(self, dish_name: str, expected_slot: str) -> bool:
        """
        Determines whether the dish is placed in the correct rack according to type.
        """
        pos = self.env._object_manager.get_object_pos(dish_name)
        if expected_slot == 'cup':
            return pos[1] > 0.5  # Cups should be in the upper rack
        elif expected_slot == 'plate':
            return pos[1] < 0.0  # Plates should be in the bottom rack
        return False

    def get_state(self) -> Tuple[np.ndarray, List[str]]:
        """
        Returns a binary vector and corresponding predicate list
        describing the current semantic state of the dishwasher domain.
        """
        predicates = []
        values = []
        for dish in self.env._object_manager.object_names:
            stable = self.is_stable(dish)
            predicates.append(f"IsStable({dish})")
            values.append(stable)

            fragile = self.is_fragile(dish)
            predicates.append(f"IsFragile({dish})")
            values.append(fragile)

            correct_slot = self.is_correct_slot(dish, 'plate')  # or infer type of dish
            predicates.append(f"InCorrectSlot({dish})")
            values.append(correct_slot)

        space = self.has_space()
        predicates.append("HasSpace")
        values.append(space)

        return np.array(values), predicates

    def success_score(self, state: np.ndarray, goal_predicates: List[str], all_predicates: List[str]) -> float:
        """
        Computes a success score based on how many goal predicates are satisfied.
        Returns a float between 0 and 1.
        """
        success_flags = [(pred in goal_predicates and state[i]) for i, pred in enumerate(all_predicates)]
        return sum(success_flags) / len(goal_predicates) if goal_predicates else 0.0
