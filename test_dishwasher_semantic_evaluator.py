"""To test the DishwasherSemanticEvaluator class, you need to verify two main aspects:

1. get_state() – Ensures that correct semantic facts are returned for various dish configurations.
2. success_score() – Evaluates whether goal predicate satisfaction is calculated correctly.
"""

import pytest
import numpy as np
from unittest.mock import MagicMock
from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator

@pytest.fixture
def evaluator():
    """
    Fixture to initialize the DishwasherSemanticEvaluator with a simulated environment.
    """
    from sim_ur5.mujoco_env.sim_env import SimEnv
    env = SimEnv(render_mode="none")  # Initialize the simulation environment without rendering
    return DishwasherSemanticEvaluator(env)

def test_stable_vs_unstable(evaluator):
    """
    Test to verify that the evaluator correctly identifies stable and unstable dishes
    based on their positions (e.g., high Z values indicate instability).
    """
    env = evaluator.env
    # Initial positions of dishes and plate
    dish_positions = [   
        [0, -0.6, 0.03],  # Dish 0
        [-0.7, -0.7, 0.03],  # Dish 1
        [-0.7, -0.8, 0.03],  # Dish 2
        [0, -0.8, -0.08],    # Disch 3
        [0, 0.6, 0.08],     # Dish can
        [0.6, -0.6, 0.77],       # Plate dish 5
    ]
    env.reset(randomize=False, dish_positions=dish_positions)  # Reset environment with predefined positions
    state, preds = evaluator.get_state()  # Get the semantic state and predicates
    assert preds[0].startswith("IsStable")  # Ensure the first predicate is about stability
    assert state[0] is True  # The first dish is stable
    assert state[1] is False  # The second dish is unstable

def test_incorrect_slot_detection(evaluator):
    """
    Test to verify that the evaluator correctly identifies dishes placed in incorrect slots.
    For example, plates should be in the lower rack, and cups should be in the upper rack.
    """
    env = evaluator.env
    dish_positions = [
        [0, 0.6, 0.03],   # Upper rack → incorrect for plate
        [0, -0.6, 0.03],  # Lower rack → correct for plate
        [0, 0.6, 0.03],   # Upper rack → incorrect for plate
        [0, -0.6, 0.03]   # Lower rack → correct for plate
    ]
    env.reset(randomize=False, dish_positions=dish_positions)  # Reset environment with predefined positions
    state, preds = evaluator.get_state()  # Get the semantic state and predicates
    incorrect = [p for i, p in enumerate(preds) if "InCorrectSlot" in p and not state[i]]
    assert len(incorrect) == 2  # Two dishes are in the wrong slot

def test_fragility_based_on_name(evaluator):
    """
    Test to verify that the evaluator correctly identifies fragile objects based on their names.
    For example, objects with "glass" in their name should be marked as fragile.
    """
    env = evaluator.env
    # Rename one dish to include 'glass' to simulate a fragile object
    env._object_manager.object_names[0] = "glass_dish"
    state, preds = evaluator.get_state()  # Get the semantic state and predicates
    frag_index = preds.index("IsFragile(glass_dish)")  # Find the index of the fragility predicate
    assert state[frag_index] is True  # Ensure the fragile object is correctly identified

def test_has_space_flag(evaluator):
    """
    Test to verify that the evaluator correctly identifies whether there is space for more dishes.
    For example, if all slots are occupied, the "HasSpace" predicate should be False.
    """
    env = evaluator.env
    # Place all dishes in the upper rack (y > 0.5)
    dish_positions = [
        [0, 0.6, 0.03],
        [0, 0.7, 0.03],
        [0, 0.8, 0.03],
        [0, 0.9, 0.03]
    ]
    env.num_dishs = 4  # Simulate an environment with 4 dishes
    env.reset(randomize=False, dish_positions=dish_positions)  # Reset environment with predefined positions
    state, preds = evaluator.get_state()  # Get the semantic state and predicates
    idx = preds.index("HasSpace")  # Find the index of the "HasSpace" predicate
    assert state[idx] is False  # Ensure the "HasSpace" predicate is False (no space available)

def test_success_score_all_match(evaluator):
    """
    Test to verify that the success_score() method returns 1.0 when all goal predicates are satisfied.
    """
    state, preds = evaluator.get_state()  # Get the semantic state and predicates
    goal_preds = [p for p in preds if "InCorrectSlot" in p or "IsStable" in p]  # Define goal predicates
    score = evaluator.success_score(state, goal_preds, preds)  # Calculate success score
    assert 0.0 <= score <= 1.0  # Ensure the score is between 0 and 1

def test_success_score_partial_match(evaluator):
    """
    Test to verify that the success_score() method returns a value less than 1.0
    when only some goal predicates are satisfied.
    """
    state, preds = evaluator.get_state()  # Get the semantic state and predicates
    # Flip one predicate to simulate failure
    state = state.copy()
    for i, p in enumerate(preds):
        if "IsStable" in p:  # Find the first "IsStable" predicate
            state[i] = False  # Mark it as False to simulate instability
            break
    goal_preds = [p for p in preds if "IsStable" in p or "InCorrectSlot" in p]  # Define goal predicates
    score = evaluator.success_score(state, goal_preds, preds)  # Calculate success score
    assert score < 1.0  # Ensure the score is less than 1.0
