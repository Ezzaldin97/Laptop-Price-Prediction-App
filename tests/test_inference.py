import os
import sys
sys.path.append(os.path.abspath("."))

import pytest
from app import inference


valid_data = {
    "laptop_ID": 78,
    "Company": "HP",
    "Product": "",
    "TypeName": "Notebook",
    "Inches": 13.7,
    "ScreenResolution": "Full HD 3840x2160",
    "Cpu": "AMD A10-Series 9620P 2.7GHz",
    "Ram": "16GB",
    "Memory": "500GB HDD",
    "Gpu": "Intel Iris Plus Graphics 650",
    "OpSys": "Windows 10",
    "Weight": "1.5kg"
}

def test_prediction_on_valid_data():
    inf = inference.Inference(valid_data)
    transformed_data = inf.transform()
    excepted = inf.predict(transformed_data)
    actual = 1672.7878869982583
    assert(excepted == actual)