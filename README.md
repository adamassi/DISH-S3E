
This repository hosts the **DISH-S3E** project for the AI course (236502) at Technion. It features a simulation-based environment for evaluating **semantic robotic reasoning** tasks using the MuJoCo physics engine and a UR5e robot arm. The project includes two primary domains:
- **Dishwasher Loading**
- **Battery Sorting and Charging Station**

--- 

## 🚀 Overview

The environment is designed for evaluating logic-driven robotic tasks using structured MuJoCo scenes and XML-defined assets. The robot executes simulated pick-and-place actions while answering **semantic questions** and reporting success through interpretable predicates.

### Key Features:
- UR5e robot with adhesive gripper
- MuJoCo-based structured 3D environments
- Predicate-based semantic reasoning
- Scene and object definitions in XML
- Dynamic grasping and placement logic
- `get_state()` and `success_score()` for evaluation

---

## 🧠 Domains & Semantics

### 🧼 Dishwasher Loading
Semantic predicates:
- `IsStable(object)`
- `HasSpace()`
- `IsFragile(object)`
- `InCorrectSlot(object)`


Evaluation is done by matching semantic state to goal predicates using a scoring function (`success_score`).

---

## 🛠️ Setup Instructions

### ✅ Prerequisites
- Python 3.10 or 3.11
- MuJoCo 2.x
- [Activate your MuJoCo license](https://mujoco.readthedocs.io/)
- Install dependencies:

```bash
git clone https://github.com/adamassi/DISH-S3E.git
cd DISH-S3E

# Create and activate a virtual environment
py -3.10 -m venv venv
.\venv\Scripts\Activate      # Windows
# or
python3.10 -m venv venv
source venv/bin/activate     # macOS/Linux

# Install packages
pip install -r requirements.txt
```

> **Note:** Ensure the Python interpreter is set to the virtual environment (3.10+).

---

## ▶️ How to Run

To run the simulation:

```bash
mjpython sim_testing.py
```

Or run any specific test or domain script using:

```bash
mjpython <filename>.py
```

---

## 🧩 Project Structure

```
sim_ur5/
│
├── mujoco_env/
│   ├── sim_env.py               # Main simulation wrapper
│   ├── mujoco_env.py            # Gym-style environment interface
│   ├── world_utils/
│   │   ├── object_manager.py    # Graspable object logic
│   │   ├── grasp_manager.py     # Grasp and release logic
│   │   └── configurations_and_constants.py
│
├── motion_planning/
│   └── motion_executor.py       # High-level motion planning (moveJ, pick/place)
│
├── assets/
│   ├── robot.xml                # UR5e robot model
│   ├── dishwasher_asset.xml     # Dishwasher meshes/materials
│   ├── dishwasher_body.xml      # Dishwasher components (rack, door)
│   ├── plate.obj                # Plate mesh
│   └── scene.xml                # Environment layout
│
├── test/
│   ├── sim_testing.py           # Example simulation scenario
│   └── test_for_normal.py       # Stability/contact force tests
```

---

## 🧪 Evaluation Functions

Each domain includes:
- `get_state()` — returns current semantic state (vector + predicates)
- `success_score(state, goal, predicates)` 

These allow automated benchmarking of semantic success.

---

## 🧠 Sample Output

```python
# Dishwasher domain example
state, predicates = evaluator.get_state()
score = evaluator.success_score(state, goal_predicates, predicates)
print(f"Current Score: {score * 100:.2f}%")
```

---

## 📚 Course Context

Developed as a final project for:

> **Artificial Intelligence (236502)**  
> The Taub Faculty of Computer Science  
> Technion – Israel Institute of Technology  
> By: Adam Assi & Firas Hilu  

---



## 📬 Contact

For academic inquiries or contributions:  
📧 adamassi@campus.technion.ac.il  
📧 firashilu@campus.technion.ac.il
