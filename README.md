<div align="center">

<h1>GEAR: Bridging the Planner-Actor Gap<br>via Gradient-Aligned Policy Extraction</h1>

<p><strong>NeurIPS 2026</strong></p>

<p>
Yao-Hui Li, Xin Li, Hasnaa Bennis, Meiju Li,Boya Zhang, Yingfang Yuan, Wei Pang
</p>

<p>Official implementation of <strong>GEAR</strong>.</p>

<p>
  <a href="#overview">Overview</a>
  &nbsp;•&nbsp;
  <a href="#installation">Installation</a>
  &nbsp;•&nbsp;
  <a href="#training">Training</a>
  &nbsp;•&nbsp;
  <a href="#acknowledgements">Acknowledgements</a>
</p>

</div>

## Overview

Hybrid model-based reinforcement learning (MBRL) integrates lookahead planning with actor-critic optimization for sample-efficient control. However, this coupled architecture suffers from a critical **planner-actor mismatch**. Existing policy alignment methods face a structural dilemma: forward KL introduces mode-covering objective conflicts, while reverse KL relies on brittle exploration proxies that lack expressivity.

We propose **G**radient-**E**mbedded **A**lignment **R**egularization (**GEAR**), a unified in-sample policy extraction framework. GEAR derives a first-order geometric alignment metric from the continuous-time **Hamilton-Jacobi-Bellman (HJB) equation** to evaluate action evolution against the local value gradient. By using this metric as an absolute modulation weight, GEAR suppresses spurious imitation and transforms the diffuse forward-KL objective into a focused, **mode-seeking objective**.

Evaluations on the challenging **HumanoidBench** suite demonstrate that GEAR achieves significantly higher **sample efficiency** and **asymptotic performance** than state-of-the-art baselines.

## Installation

Run the following commands from the repository root, where `setup.py` is located.

### 1. Create and activate the environment

```bash
conda create -n GEAR python=3.10
conda activate GEAR
```

### 2. Install the project

```bash
pip install -e .
```

## Training

After installation, enter the `GEAR` directory and launch training:

```bash
cd GEAR
python train.py task=humanoid_h1hand-run-v0
```

The example above trains GEAR on the **HumanoidBench H1 Hand Run** task. Set `task` to the desired task identifier to run other supported tasks.

## Acknowledgements

Our codebase is primarily based on [BOOM](https://github.com/molumitu/BOOM_MBRL). We thank its authors for making their implementation publicly available and providing a valuable foundation for this project.
