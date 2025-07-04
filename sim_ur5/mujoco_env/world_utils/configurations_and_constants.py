import numpy as np

from sim_ur5.mujoco_env.tasks.null_task import NullTask
from sim_ur5.mujoco_env.episode import *



# Scene configuration for HouseTableWorld
sceneHouseTableWorld = SceneSpec(
    'housetableworld',
    objects=(
        # Define objects in the HouseTableWorld scene
        ObjectSpec('bin_dark_wood', base_pos=[0.0, -0.6, 0.]),  # Bin object
        ObjectSpec('plate', base_pos=[0, 0.6, 0.01], base_joints=(JointSpec('free',attrs={'name': 'dish5_fj'}),),),
        ObjectSpec('dish_can', base_pos=[0.0, 0.6, 0.4], base_joints=(JointSpec('free',attrs={'name': 'dish4_fj'}),),),  # Can object with a free joint
        ObjectSpec('Dishwasher', base_pos=[0.6, -1, 0.]),  # Dishwasher object

        # ObjectSpec('plate', base_pos=[0.6, -0.421, 0.57], base_joints=(JointSpec('free',attrs={'name': 'dish6_fj'}),), base_rot=[1.57079632679, 0, 0]),
        

        ObjectSpec('plate', base_pos=[0.6, -0.48, 0.57], base_joints=(JointSpec('free',attrs={'name': 'dish6_fj'}),), base_rot=[1.57079632679, 0, 0]),
        ObjectSpec('wood_spoon', base_pos=[-0.6, -0.6, 0.03], base_joints=(JointSpec('free',attrs={'name': 'dish7_fj'}),),),  # Wooden spoon object
        ObjectSpec('wood_spoon', base_pos=[-0.6, -0.6, 0.2], base_joints=(JointSpec('free',attrs={'name': 'dish8_fj'}),),),  # Wooden spoon object
        ObjectSpec('wood_spoon', base_pos=[-0.6, -0.6, 0.1], base_joints=(JointSpec('free',attrs={'name': 'dish9_fj'}),),),  # Wooden spoon object
        ObjectSpec('wood_spoon', base_pos=[-0.6, -0.6, 0.23], base_joints=(JointSpec('free',attrs={'name': 'dish10_fj'}),),),  # Wooden spoon object
        ObjectSpec('wooden_fork', base_pos=[0.7, 0.6, 0.05], base_joints=(JointSpec('free',attrs={'name': 'dish11_fj'}),),),  # Wooden fork object
        ObjectSpec('wooden_fork', base_pos=[0.8, 0.6, 0.25], base_joints=(JointSpec('free',attrs={'name': 'dish12_fj'}),),),  # Wooden fork object
        ObjectSpec('knife', base_pos=[0.7, 0.6, 0.15], base_joints=(JointSpec('free',attrs={'name': 'dish13_fj'}),),),  # Knife object
        ObjectSpec('knife', base_pos=[0.8, 0.6, 0.35], base_joints=(JointSpec('free',attrs={'name': 'dish14_fj'}),),),  # Knife object
        ObjectSpec('wine_glass', base_pos=[-0.1, 0.7, 0.25], base_joints=(JointSpec('free',attrs={'name': 'dish15_fj'}),),base_rot=[-1.57079632679, 0, 0]),  # Wine glass object
        ObjectSpec('wine_glass', base_pos=[0.2, 0.7, 0.15], base_joints=(JointSpec('free',attrs={'name': 'dish16_fj'}),),base_rot=[-1.57079632679, 0, 0]),  # Wine glass object
        ObjectSpec('wine_glass', base_pos=[0.1, 0.7, 0.2], base_joints=(JointSpec('free',attrs={'name': 'dish17_fj'}),),base_rot=[-1.57079632679, 0, 0]),  # Wine glass object
        ObjectSpec('wine_glass', base_pos=[0., 0.7, 0.1], base_joints=(JointSpec('free',attrs={'name': 'dish18_fj'}),),base_rot=[1.57079632679, 0, 0]),  # Wine glass object
        ObjectSpec('tall_cup', base_pos=[0.2, 0.5, 0.05], base_joints=(JointSpec('free',attrs={'name': 'dish19_fj'}),),base_rot=[-1.57079632679, 0, 0]),  # Cup object
        ObjectSpec('tall_cup', base_pos=[0.2, 0.5, 0.2], base_joints=(JointSpec('free',attrs={'name': 'dish20_fj'}),),base_rot=[-1.57079632679, 0, 0]),  # Cup object
        ObjectSpec('tall_cup', base_pos=[0.2, 0.5, 0.35], base_joints=(JointSpec('free',attrs={'name': 'dish21_fj'}),),base_rot=[-1.57079632679, 0, 0]),  # Cup object
        ObjectSpec('tall_cup', base_pos=[0.1, 0.5, 0.05], base_joints=(JointSpec('free',attrs={'name': 'dish22_fj'}),),base_rot=[-1.57079632679, 0, 0]),  # Cup object
        ObjectSpec('tall_cup', base_pos=[0.1, 0.5, 0.15], base_joints=(JointSpec('free',attrs={'name': 'dish23_fj'}),),base_rot=[-1.57079632679, 0, 0]),  # Cup object
        ObjectSpec('tall_cup', base_pos=[0., 0.5, 0.], base_joints=(JointSpec('free',attrs={'name': 'dish24_fj'}),),base_rot=[-1.57079632679, 0, 0]),  # Cup object
        ObjectSpec('tall_cup', base_pos=[-0.2, 0.5, 0.05], base_joints=(JointSpec('free',attrs={'name': 'dish25_fj'}),),base_rot=[-1.57079632679, 0, 0]),  # Cup object
        ObjectSpec('tall_cup', base_pos=[-0.2, 0.5, 0.15], base_joints=(JointSpec('free',attrs={'name': 'dish26_fj'}),),base_rot=[-1.57079632679, 0, 0]),  # Cup object
        ObjectSpec('tall_cup', base_pos=[-0.2, 0.5, 0.3], base_joints=(JointSpec('free',attrs={'name': 'dish27_fj'}),),base_rot=[-1.57079632679, 0, 0]),  # Cup object
        ObjectSpec('tall_cup', base_pos=[-0.1, 0.5, 0.05], base_joints=(JointSpec('free',attrs={'name': 'dish28_fj'}),),base_rot=[-1.57079632679, 0, 0]),  # Cup object
        ObjectSpec('tall_cup', base_pos=[-0.1, 0.5, 0.2], base_joints=(JointSpec('free',attrs={'name': 'dish29_fj'}),),base_rot=[-1.57079632679, 0, 0]),  # Cup object
        ObjectSpec('tall_cup', base_pos=[-0.1, 0.5, 0.35], base_joints=(JointSpec('free',attrs={'name': 'dish30_fj'}),),base_rot=[-1.57079632679, 0, 0]),  # Cup object
        ObjectSpec('spoon', base_pos=[-0.8, 0.4, -0.35], base_joints=(JointSpec('free',attrs={'name': 'dish31_fj'}),),),  # Spoon object
        ObjectSpec('spoon', base_pos=[1, 0.8, -0.35], base_joints=(JointSpec('free',attrs={'name': 'dish32_fj'}),),),  # Spoon object
        ObjectSpec('fork', base_pos=[0.8, 0.4, -0.35], base_joints=(JointSpec('free',attrs={'name': 'dish33_fj'}),),),  # Spoon object
        ObjectSpec('arrow', base_pos=[-0.1, 0.5, 0.45], ),

        

        
    ),
    render_camera='top-right',  # Camera used for rendering
    init_keyframe='home'  # Initial keyframe for the scene
)


# Configuration for the MuJoCo environment with one UR5e robot
muj_env_config = dict(
    scene=sceneHouseTableWorld,  # Use the HouseTableWorld scene
    robots=dict(
        # Define the first UR5e robot
        ur5e_1=dict(
            resource='ur5e',
            attachments=['adhesive_gripper'],  # Attach an adhesive gripper
            mount='rethink_stationary',  # Mount the robot on a stationary base
            base_pos=[0, 0.0, -0.7],  # Base position of the robot
            base_rot=[0, 0, 1.57079632679],  # Base rotation of the robot
            privileged_info=True,  # Enable privileged information
        ),
    ),
    tasks=dict(
        ur5e_1=NullTask,  # Assign a null task to the first robot
    ),
)

# Maximum velocity for initialization
INIT_MAX_VELOCITY = np.array([3] * 6)

# Relative position of the grasped object from the end effector
grasp_offset = 0.02

# Frame skip for simulation
frame_skip = 5
