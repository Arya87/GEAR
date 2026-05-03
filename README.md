## Quick Start Instructions

```bash
conda create -n GEAR python=3.10
conda activate GEAR
pip install -e .  # Ensure setup.py exists in the current directory
cd GEAR
python train.py task=humanoid_h1hand-run-v0
# The code is based on BOOM.
```