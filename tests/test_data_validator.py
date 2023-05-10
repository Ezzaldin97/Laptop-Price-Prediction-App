import os
import sys
sys.path.append(os.path.abspath("."))

import pytest
import pydantic
from app import validator

valid_data = {
    "laptop_ID":78,
    "Company":"Apple",
    "Product":"MacBook Pro",
    "TypeName":"Ultrabook",
    "Inches":15.7,
    "ScreenResolution":"IPS Panel Retina Display 2560x1600",
    "Cpu":"Intel Core i7 2.7GHz",
    "Ram":"16GB",
    "Memory":"512GB SSD",
    "Gpu":"Intel Iris Plus Graphics 650",
    "OpSys":"macOS",
    "Weight":"1.37kg"
}

invalid_data = {
    "laptop_ID":78,
    "Company":"Nokia",
    "Product":"MacBook Pro",
    "TypeName":"Ultrabook",
    "Inches":15,
    "ScreenResolution":"IPS Panel Retina Display 2560x1600",
    "Cpu":"Intel Core i7 2.7GHz",
    "Ram":"16GB",
    "Memory":"512GB SSD",
    "Gpu":"Intel Iris Plus Graphics 650",
    "OpSys":"macOS",
    "Weight":"1.37kg"
}

def test_valid_sample():
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        validator.Laptop(**invalid_data)
        
def test_invalid_sample():
    data = validator.Laptop(**valid_data)
    assert(data.Cpu == "Intel Core i7 2.7GHz")
    assert(data.Ram == "16GB")
    assert(data.Memory == "512GB SSD")
    assert(data.Gpu == "Intel Iris Plus Graphics 650")
    assert(data.OpSys == "macOS")
    assert(data.Weight == "1.37kg")