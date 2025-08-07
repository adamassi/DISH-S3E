# Temporary Simulation Environment

This repository contains a temporary simulation environment for testing and developing robot control algorithms using the UR5e robot model in a MuJoCo physics simulation.

## Overview

The simulation environment provides a simplified setup for:
- UR5e robot arm simulation
- Basic pick and place operations
- Motion planning and execution
- Block manipulation tasks

## Prerequisites

- Python 3.10 or 3.11
- MuJoCo physics engine
- Required Python packages (see `requirements.txt`)

## Clone the repository:
git clone https://github.com/adamassi/DISH-S3E.git


```
## to run :
1
py -3.10 -m venv venv
2
.\venv\Scripts\Activate
3
pip install -r requirements.txt

slect interpreter to be 3.10 (venv)
 
if mac:
python3.10 -m venv venv  
source venv/bin/activate 
pip install -r requirements.txt
mjpython -m "name_the_file".py 






## Key Components

### SimEnv Class
- Main simulation environment
- Handles physics simulation
- Manages robot and object states

### MotionExecutor Class
- Executes robot movements
- Provides high-level movement commands
- Handles pick and place operations

## Common Issues and Solutions

1. **Robot Out of Workspace**
   - Ensure target positions are within workspace limits
   - Check z-height for pick and place operations

2. **Motion Planning Failures**
   - Verify start and goal positions are valid
   - Check for obstacles in the path
////






