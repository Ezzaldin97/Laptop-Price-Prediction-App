import json
import os
import pickle
import re
import numpy as np
from app.config_parser import Config
from typing import Dict, List, Any

conf = Config()

class Inference:
    def __init__(self, json_file) -> None:
        self.json_file = json_file
        self.model = pickle.load(os.path.join("bin", "model-pipeline.pkl"))
        self.cat_cols_indices = conf.config["categorical_columns_indices"]
        self.num_cols_indices = conf.config["numerical_columns_indices"]
    @staticmethod
    def handle_storage_space(x:str) -> int:
        spaces_lst = []
        for val in x.split():
            if "GB" in val or "TB" in val:
                if "TB" in val:
                    spaces_lst.append(int(re.findall("\d+", val)[0])*1000)
                else:
                    spaces_lst.append(int(re.findall("\d+", val)[0]))
        return sum(spaces_lst) 
    def transform(self) -> Dict[Any]:
        transformed_data = dict()
        transformed_data["Ram"] = self.json_file["Ram"][:-2]
        transformed_data["Weight"] = self.json_file["Weight"][:-2]
        transformed_data["CPU_manufacturer"] = self.json_file["Cpu"].split()[0]
        transformed_data["CPU_frequency"] = self.json_file["Cpu"].split()[1]
        transformed_data["CPU_frequency"] = transformed_data["CPU_frequency"].split()[:-3]
        transformed_data["CPU_frequency"] = float(transformed_data["CPU_frequency"])
        transformed_data["CPU_model"] = self.json_file["Cpu"].split()[1:-1]
        transformed_data["CPU_model"] = ''.join(val+'-' if idx != len(transformed_data["CPU_model"])-1 else val for idx, val in enumerate(transformed_data["CPU_model"]))
        width_lst = int(self.json_file["ScreenResolution"].split()[-1].split(sep = "x")[0]) * 0.0264583333
        height_lst = int(self.json_file["ScreenResolution"].split()[-1].split(sep = "x")[1]) * 0.0264583333
        transformed_data["screen_area_cm2"] = list(map(lambda x, y: x*y, width_lst, height_lst))
        transformed_data["is_4K"] = 1 if "4K Ultra HD" in self.json_file["ScreenResolution"] else 0
        transformed_data["is_touchscreen"] = 1 if "Touchscreen" in self.json_file["ScreenResolution"] else 0
        transformed_data["is_full_HD"] = 1 if "Full HD" in self.json_file["ScreenResolution"] else 0
        transformed_data["is_Quad"] = 1 if "Quad" in self.json_file["ScreenResolution"] else 0
        transformed_data["is_HD+"] = 1 if "HD+" in self.json_file["ScreenResolution"] else 0
        transformed_data["is_ips_panel"] = 1 if "IPS Panel" in self.json_file["ScreenResolution"] else 0
        transformed_data["is_retina_display"] = 1 if "Retina Display" in self.json_file["ScreenResolution"] else 0
        transformed_data["is_ssd"] = 1 if "SSD" in self.json_file["Memory"] else 0
        transformed_data["is_hdd"] = 1 if "HDD" in self.json_file["Memory"] else 0
        transformed_data["is_hybrid_storage"] = 1 if "Hybrid" in self.json_file["Memory"] else 0
        transformed_data["is_flash_storage"] = 1 if "Flash" in self.json_file["Memory"] else 0
        transformed_data["unique_storage_types"] = transformed_data["is_ssd"] + transformed_data["is_hdd"] + transformed_data["is_hybrid_storage"] + transformed_data["is_flash_storage"]
        transformed_data["total_storage"] = Inference.handle_storage_space(self.json_file["Memory"])
        transformed_data["GPU_manufacturer"] = self.json_file["Gpu"].split()[0]
        return transformed_data
    def predict(self, data:Dict[Any]) -> np.array:
        prediction = self.model.predict(np.array(list(data.values())).reshape(1,-1))
        return prediction
        