import yaml
import os

class Config:
    def __init__(self):
        with open(os.path.join(".", "app", "conf", "config.yml"), "r") as f:
            self.config = yaml.safe_load(f)