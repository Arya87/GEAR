# tasks=(
#     "humanoid_h1hand-balance_hard-v0" ----
#     "humanoid_h1hand-balance_simple-v0"----
#     "humanoid_h1hand-crawl-v0"----
#     "humanoid_h1hand-hurdle-v0"----
#     "humanoid_h1hand-maze-v0"----
#     "humanoid_h1hand-pole-v0"-----
#     "humanoid_h1hand-reach-v0"-----
#     "humanoid_h1hand-run-v0" 
#     "humanoid_h1hand-sit_hard-v0"----
#     "humanoid_h1hand-sit_simple-v0"----
#     "humanoid_h1hand-slide-v0"
#     "humanoid_h1hand-stair-v0"-----
#     "humanoid_h1hand-stand-v0"
#     "humanoid_h1hand-walk-v0"---
# )

task=humanoid_h1hand-pole-v0
exp_name=boom_inpg_vis
steps=1000000

mkdir -p console_log/${exp_name}

seed=1
CUDA_VISIBLE_DEVICES=0 nohup python train.py \
    task=${task} \
    steps=${steps} \
    exp_name=${exp_name} \
    seed=${seed} > console_log/${exp_name}/${task}_${seed}.log &