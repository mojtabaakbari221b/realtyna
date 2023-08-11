import os
import environ
from pathlib import Path


def load_env():
    
    env_file = os.path.join(
        Path(__file__).resolve().parent.parent,
        '.envs',
        '.env',
    )

    env = environ.Env()
    environ.Env.read_env(env_file=env_file)

    return env