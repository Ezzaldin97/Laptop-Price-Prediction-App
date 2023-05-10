import os
import sys
sys.path.append(os.path.abspath("."))

import pytest
from app import inference


valid_data = {
    "laptop_ID": 78,
    "Company": "Razer",
    "Product": "MacBook Pro",
    "TypeName": "Workstation",
    "Inches": 18.7,
    "ScreenResolution": "4K Ultra HD / Touchscreen 3840x2160",
    "Cpu": "Intel Core i7 3.5GHz",
    "Ram": "128GB",
    "Memory": "1TB SSD",
    "Gpu": "Intel Iris Plus Graphics 650",
    "OpSys": "Linux",
    "Weight": "1.5kg"
}

def test_prediction_on_valid_data():
    inf = inference.Inference(valid_data)
    transformed_data = inf.transform()
    excepted = inf.predict(transformed_data)
    actual = 2780.181198010081
    assert(excepted == actual)