import os
import sys

if sys.platform != "darwin":
    os.environ["MUJOCO_GL"] = "osmesa"
    os.environ["PYOPENGL_PLATFORM"] = "osmesa"
    os.environ["HYDRA_FULL_ERROR"]="1"
os.environ["LAZY_LEGACY_OP"] = "0"

os.environ["WANDB_MODE"] = "offline"
import warnings
warnings.filterwarnings('ignore')
import torch
import hydra
from termcolor import colored

from GEAR.common.parser import parse_cfg
from GEAR.common.seed import set_seed
from GEAR.common.buffer import Buffer
from GEAR.envs import make_env
from GEAR.boom_alg import BOOM
from GEAR.GEAR.gear import GEAR
from GEAR.trainer.online_trainer import OnlineTrainer
from GEAR.common.logger import Logger

torch.backends.cudnn.benchmark = True
import os

@hydra.main(config_name="config", config_path=".")
def train(cfg: dict):
    """
    Script for training BOOM agents.
    """
    assert cfg.steps > 0, "Must train for at least 1 step."
    cfg = parse_cfg(cfg)
    set_seed(cfg.seed)
    print(colored("Work dir:", "yellow", attrs=["bold"]), cfg.work_dir)

    trainer_cls = OnlineTrainer
    trainer = trainer_cls(
        cfg=cfg,
        env=make_env(cfg),
        agent=GEAR(cfg),
        buffer=Buffer(cfg),
        logger=Logger(cfg),
    )
    trainer.train()
    print("\nTraining completed successfully")


if __name__ == "__main__":
    train()
