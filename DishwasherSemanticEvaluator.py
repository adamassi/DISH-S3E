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
        self.env.num_dishs = 6  # Example capacity, can be adjusted based on the environment

    """
    Valid names for is stable: 
    ['Dishwasher/door', 'Dishwasher/top_rack', 'can/dish4_fj/',
    'dish0_fj', 'dish1_fj', 'dish2_fj', 'dish3_fj', 'plate/dish5_fj/',
    'plate_1/dish6_fj/', 'rethink_mount_stationary/robot_0_ur5e/elbow_joint',
    'rethink_mount_stationary/robot_0_ur5e/shoulder_lift_joint', 'rethink_mount_stationary/robot_0_ur5e/shoulder_pan_joint', 'rethink_mount_stationary/robot_0_ur5e/wrist_1_joint', 'rethink_mount_stationary/robot_0_ur5e/wrist_2_joint', 'rethink_mount_stationary/robot_0_ur5e/wrist_3_joint']"
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
        return self.env.is_stable_orientation(dish_name)

    def has_space(self) -> bool:
        """
        Checks if there's still available space in the dishwasher.
        This is based on how many dishes are already placed in a defined region.
        """
        occupied = len([d for d in self.env._object_manager.object_names
                        if self.env._object_manager.get_object_pos(d)[1] > 0.5])
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
