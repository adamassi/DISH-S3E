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
battery_position = [   
    [-0.7, -0.6, 0.03],
    [-0.7, -0.7, 0.03],
    [-0.7, -0.8, 0.03],
    [-0.7, -0.9, 0.03]]
   

executor = MotionExecutor(env)
print("waiting for 1 second")
start_time = time.time()
while time.time() - start_time < 15:
        pass  # wait for 5 seconds to let the simulation start
# Add batterys to the world
env.reset(randomize=False, dish_positions=battery_position)
#executor.pick_up("ur5e_2", -0.6, -0.5, 0.03)


"""
executor.plan_and_move_to_xyz_facing_down("ur5e_2", [-0.7, -0.6, 0.15])
"""
#current_joint_angles = env.robots_joint_pos["ur5e_2"]
#print(f"current_joint_angles {current_joint_angles}")
#move_to = [1.305356658502026, -0.7908733209856437, 1.4010098471710881, 4.102251451313659, -1.5707962412281837, -0.26543967541515895]
#executor.moveJ("ur5e_2", move_to)
# executor.pick_up("ur5e_2", -.5, -0.8, 0.03)

executor.pick_up("ur5e_1", -0.1, -0.1, 0.7)
executor.plan_and_move_to_xyz_facing_down("ur5e_1", [0.3, 0.3, 0.1])

#executor.put_down("ur5e_2", -0.4, -0.4, 0.2)
executor.wait(1000)

# Open the dishwasher door
door_joint_name = "Dishwasher/door"  # Correct joint name
door_open_position = -1.5  # Fully open position (in radians)

# Set the joint position
env._mj_data.joint(door_joint_name).qpos[0] = door_open_position

# Pass the current joint positions to the step method
current_joint_positions = {robot: env.robots_joint_pos[robot] for robot in env.robots_joint_pos.keys()}
env.step(current_joint_positions)  # Step the simulation to apply the change

executor.wait(9000)














