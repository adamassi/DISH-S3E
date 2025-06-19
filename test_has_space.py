import unittest
import numpy as np
from sim_ur5.mujoco_env.sim_env import SimEnv
from DishwasherSemanticEvaluator import DishwasherSemanticEvaluator


class TestHasSpace(unittest.TestCase):
    def setUp(self):
        self.env = SimEnv(render_mode="none")
        self.evaluator = DishwasherSemanticEvaluator(self.env)
        # call get_all_dish_positions for debugging , print also the names of the dishes
        print("Testing has_space with fewer than num_dishs in the upper rack")
        print("Object names in the environment: self.env._object_manager.object_names")
        print(self.env._object_manager.object_names)
        # all_positions = self.env._object_manager.get_all_dish_positions()
        # print("All dish positions:", all_positions)

    # def test_has_space_true(self):
    #     print("Testing has_space with fewer than num_dishs in the upper rack")
    #     # Place fewer than num_dishs in the upper rack (y > 0.5)
    #     positions = [[-0.5, -0.8, 0.03], [-0.6, -0.8, 0.03], [-0.7, -0.8, 0.03]]
    #     self.env.reset(randomize=False, dish_positions=positions)
        
    #     self.assertTrue(self.evaluator.has_space())

    def test_has_space_false(self):
        print("Testing has_space with exactly num_dishs in the upper rack")

        # Fill the dishwasher to capacity (simulate 6 objects y > 0.5)
        positions = [[0, 0.6, 0.03], [0.1, 0.6, 0.03], [0.2, 0.6, 0.03],
                     [0.3, 0.6, 0.03], [0.4, 0.6, 0.03], [0.5, 0.6, 0.03]]
        self.env.reset(randomize=False, dish_positions=positions)

        # Iterate over objects and print those with y > 0.5
        print("Objects with y > 0.5:")
        for d in self.env._object_manager.object_names:
            pos = self.env._object_manager.get_object_pos(d)
            if pos[1] > 0.5:
                print(f"Object: {d}, Position: {pos}")

        self.assertFalse(self.evaluator.has_space())


if __name__ == '__main__':
    unittest.main()
