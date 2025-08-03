import random
import numpy as np
from typing import Dict, List


class ObjectManager:
    """convenience class to manage graspable objects in the mujoco simulation"""

    def __init__(self, mj_model, mj_data):
        self._mj_model = mj_model
        self._mj_data = mj_data
        
        # manipulated objects have 6dof free joint that must be named in the mcjf.
        all_joint_names = [self._mj_model.joint(i).name for i in range(self._mj_model.njnt)]
        #prinr all joint names
        # print(f"AAAAAAAAAAAAAAAAAAAAAAAAAAAAall_joint_names: {all_joint_names}")
        # Step 1: Get the body ID of the top rack
        body_id = self._mj_model.body("Dishwasher/top_rack").id

        # Step 2: Find all geoms that belong to that body
        geom_ids = [
            i for i in range(self._mj_model.ngeom)
            if self._mj_model.geom_bodyid[i] == body_id
        ]

        # Step 3: Get their sizes
        sizes = [self._mj_model.geom_size[i] for i in geom_ids]

        # Print the result
        # for i, size in zip(geom_ids, sizes):
        #     name = self._mj_model.geom(i).name
        #     print(f"Geom {i} (name: {name}) size: {size}")



        #itorat over all joint names if start with dish icremant counter if name starts with can rename and increment counter
        # dish_counter = 0
        # for name in all_joint_names:
        #     if name.startswith("dish"):
        #         dish_counter += 1
        #     elif name.startswith("can"):
        #         # rename the joint to dishX
        #         new_name = f"dish{dish_counter}_fj"
        #         self._mj_model.joint(name).name = new_name
        #         # increment the counter
        #         dish_counter += 1
        

                
        # all bodies that ends with 
        self.object_names = [name for name in all_joint_names if name.startswith("dish") or name.startswith("can") or name.startswith("plate") or name.startswith("wood_spoon")]
        # print(f"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBobject_names:                                     {self.object_names}")
        self.objects_mjdata_dict = {name: self._mj_model.joint(name) for name in self.object_names}
        self.initial_positions_dict = self.get_all_dish_positions()
        self.workspace_x_lims = [-0.9, -0.54]
        self.workspace_y_lims = [-1.0, -0.55]
        self.dish_size = .02

    def reset(self, randomize=True, dish_positions=None):
        """
        Reset the object positions in the simulation.
        Args:
            randomize: if True, randomize the positions of the dishs, otherwise set them to initial positions.
        """
        # print("resetting object positionsAAAAAAAAAAAAAAAAAAAAAAAAA")
        # orint the dish positions
        # print(f"dish_positions: {dish_positions}")
        def check_dish_collision(new_pos):
            """Tests if new position for dish collides with any other dish"""
            for pos in dish_positions:
                # print("checking collisionBBBBBBBBBBBBBBBBBBB")
                # print(f"new_pos: {new_pos}, pos: {pos}")
                pos_np = np.array(pos)
                if np.linalg.norm(new_pos - pos_np) < 2 * self.dish_size:
                    return True
            dish_positions.append(list(new_pos))
            return False

        if randomize:
            # print("randomizing dish positionsCCCCCCCCCCCCCCCCC")
            # randomize dish positions
            dish_positions = []
            print(self.object_names)
            for _ in range(7,len(self.object_names)):
                # generate random position for dish
                dish_location = [random.uniform(*self.workspace_x_lims), random.uniform(*self.workspace_y_lims), 0.05]
                # check if dish collides with any other previous new dish position
                while check_dish_collision(np.array(dish_location)):
                    # generate new random position for dish
                    dish_location = [random.uniform(*self.workspace_x_lims), random.uniform(*self.workspace_y_lims),
                                      0.05]
            # set dishs to new positions
            dish_positions1=[[-11.5, -0.7, 0.025],[-10.5, -0.7 ,0.025],[-10, -0.7, 0.025],[-9.5, -0.7, 0.025],[-0.2, -0.5, 0.05],[0.6, -0.6,0.8],[0.7, -0.6,0.8]]
            self.set_all_dish_positions(dish_positions1 + dish_positions)
        else:
            if dish_positions:
                self.set_all_dish_positions(dish_positions)
            else:
                self.set_all_dish_positions(list(self.initial_positions_dict.values()))

    def get_object_pos(self, name: str):
        return self._mj_data.joint(name).qpos[:3]

    def set_object_pose(self, name: str, pos, quat):
        joint_id = self.objects_mjdata_dict[name].id
        pos_adr = self._mj_model.jnt_qposadr[joint_id]
        self._mj_data.qpos[pos_adr:pos_adr + 7] = np.concatenate([pos, quat])

    def set_object_vel(self, name: str, cvel):
        joint_id = self.objects_mjdata_dict[name].id
        vel_adr = self._mj_model.jnt_dofadr[joint_id]
        self._mj_data.qvel[vel_adr:vel_adr + 6] = cvel

    def get_dish_position_from_mj_id(self, dish_id: int) -> np.ndarray:
        """
        Get the position of a dish in the simulation.
        Args:
            dish_id: the id of the dish to get the position of.
        Returns:
            the position of the dish in format [x, y ,z].
        """
        return self._mj_data.joint(dish_id).qpos[:3]

    def get_all_dish_positions_dict(self) -> Dict[str, np.ndarray]:
        """
        Get the positions of all dishs in the simulation.
        Returns:
            a dictionary of dish names to their positions, positions will be in format {name: [x, y ,z], ...}.
        """
        return {name: self.get_dish_position_from_mj_id(self.objects_mjdata_dict[name].id) for name in self.object_names}

    def get_all_dish_positions(self) -> List[np.ndarray]:
        """
        Get the positions of all dishs in the simulation.
        Returns:
            a dictionary of dish names to their positions, positions will be in format {name: [x, y ,z], ...}.
        """
        return [self.get_dish_position_from_mj_id(self.objects_mjdata_dict[name].id) for name in self.object_names]

    def set_dish_position(self, dish_id, position):
        """
        Set the position of a dish in the simulation.
        Args:
            dish_id: the id of the dish to set the position of.
            position: the position to set the dish to, position will be in format [x, y ,z].
        """
        # print(f"setting dish {dish_id} position to {position}")
        if dish_id == 4:
            joint_name = f"can/dish{dish_id}_fj/"
        elif dish_id == 5:
            joint_name = f"plate/dish{dish_id}_fj/"
        elif dish_id == 6:
            joint_name = f"plate_1/dish{dish_id}_fj/"
        elif dish_id == 7:
            joint_name = f"wood_spoon/dish{dish_id}_fj/"
        elif dish_id == 8:
            joint_name = f"wood_spoon_1/dish{dish_id}_fj/"
        elif dish_id == 9:
            joint_name = f"wood_spoon_2/dish{dish_id}_fj/"
        elif dish_id == 10:
            joint_name = f"wood_spoon_3/dish{dish_id}_fj/"
        elif dish_id == 11:
            joint_name = f"wooden_fork/dish{dish_id}_fj/"
        elif dish_id == 12:
            joint_name = f"wooden_fork_1/dish{dish_id}_fj/"
        elif dish_id == 13:
            joint_name= f"knife/dish{dish_id}_fj/"
        elif dish_id == 14:
            joint_name = f"knife_1/dish{dish_id}_fj/"
        elif dish_id == 15:
            joint_name = f"wine_glass/dish{dish_id}_fj/"
        elif dish_id == 16:
            joint_name = f"wine_glass_1/dish{dish_id}_fj/"
        elif dish_id == 17:
            joint_name = f"wine_glass_2/dish{dish_id}_fj/"
        elif dish_id == 18:
            joint_name = f"wine_glass_3/dish{dish_id}_fj/"
        elif dish_id == 19:
            joint_name = f"tall_cup/dish{dish_id}_fj/"
        elif dish_id == 20:
            joint_name = f"tall_cup_1/dish{dish_id}_fj/"
        elif dish_id == 21:
            joint_name = f"tall_cup_2/dish{dish_id}_fj/"
        else:
            joint_name = f"dish{dish_id}_fj"
        
        # joint_name =  f"dish{dish_id}_fj"
        joint_id = self._mj_model.joint(joint_name).id
        pos_adrr = self._mj_model.jnt_qposadr[joint_id]
        self._mj_data.qpos[pos_adrr:pos_adrr + 3] = position

    def set_all_dish_positions(self, positions):
        """
        Set the positions of all dishs in the simulation.
        Args:
            positions: a list of positions to set the dishs to, positions will be in format [[x, y ,z], ...].
        """
        # set dishs positions
        for i, pos in enumerate(positions):
            self.set_dish_position(i, pos)
