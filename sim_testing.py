from sim_ur5.mujoco_env.sim_env import SimEnv
from math import pi
from sim_ur5.motion_planning.motion_executor import MotionExecutor
import time
from sim_ur5.mujoco_env.common.ur5e_fk import forward



env = SimEnv()


"""
workspace_x_lims = [-0.9, -0.54]
workspace_y_lims = [-1.0, -0.55]
"""
dishs_position = [   
    [-0.7, -0.6, 0.03],
    [-0.7, -0.7, 0.03],
    [-0.7, -0.8, 0.03],
    [0, -0.6, -0.08], # 
    [0, -0.6, 0.08],
    [0, 0.6, 0.1], # plate
    ]
   

executor = MotionExecutor(env)
print("waiting for 1 second")
start_time = time.time()
while time.time() - start_time < 0.5:
        pass  # wait for 5 seconds to let the simulation start
# Add batterys to the world
env.reset(randomize=False, dish_positions=dishs_position)
#executor.pick_up("ur5e_2", -0.6, -0.5, 0.03)



# Open the dishwasher door
door_joint_name = "Dishwasher/door"  # Correct joint name
door_open_position = -1.5  # Fully open position (in radians)

# Set the joint position
env._mj_data.joint(door_joint_name).qpos[0] = door_open_position

# Pass the current joint positions to the step method
current_joint_positions = {robot: env.robots_joint_pos[robot] for robot in env.robots_joint_pos.keys()}
env.step(current_joint_positions)  # Step the simulation to apply the change



executor.wait(1000)



# Slide out the dishwasher rack
rack_joint_name = "Dishwasher/top_rack"  # Correct joint name
rack_slide_position = 0.274  # Slide almost fully out (range is 0 to 0.274)

# Set the joint position
env._mj_data.joint(rack_joint_name).qpos[0] = rack_slide_position

# Pass the current joint positions to the step method
current_joint_positions = {robot: env.robots_joint_pos[robot] for robot in env.robots_joint_pos.keys()}
env.step(current_joint_positions)  # Step the simulation to apply the change





"""
executor.plan_and_move_to_xyz_facing_down("ur5e_2", [-0.7, -0.6, 0.15])
"""

executor.pick_up("ur5e_1", 0, -0.6, 0.20) #pick up the first dish "box" in the box need to had 20 cm up 
executor.put_down("ur5e_1", 0, 0.9, 0.25)


executor.pick_up("ur5e_1", 0, 0.6, 0.15)
executor.put_down("ur5e_1", 0, 0.8, 0.15)


# executor.pick_up("ur5e_1", 0, -0.6, 0.2)
# executor.plan_and_move_to_xyz_facing_down("ur5e_1", [0.3, 0.3, 0.1])


#executor.wait(10)



#executor.wait(1000)














