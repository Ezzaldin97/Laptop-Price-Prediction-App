from pydantic import BaseModel, validator
import re

class Laptop(BaseModel):
    laptop_ID: int
    Company: str
    Product: str
    TypeName: str
    Inches: float
    ScreenResolution: str
    Cpu: str
    Ram: str
    Memory: str
    Gpu: str
    OpSys: str
    Weight: str
    
    @validator('OpSys')
    def valid_os(cls, value):
        if value not in ['macOS', 'No OS', 'Windows 10', 'Mac OS X', 'Linux', 'Android', 'Windows 10 S', 'Chrome OS', 'Windows 7']:
            raise ValueError("invalid Operating System")
        return value
    
    @validator('Company')
    def valid_company(cls, value):
        if value not in ['Apple','HP','Acer','Asus','Dell','Lenovo','Chuwi','MSI','Microsoft','Toshiba','Huawei','Xiaomi','Vero','Razer','Mediacom','Samsung','Google','Fujitsu','LG']:
            raise ValueError("invalid Company Name")
        return value
    
    @validator('TypeName')
    def valid_device_type(cls, value):
        if value not in ['Ultrabook','Notebook','Netbook','Gaming','2 in 1 Convertible','Workstation']:
            raise ValueError("invalid device Type")
        return value
    
    @validator('Gpu')
    def valid_gpu_provider(cls, value):
        provider = value.split()[0]
        if provider not in ['Intel', 'AMD', 'Nividia', 'ARM']:
            raise ValueError("invalid GPU Provider")
        return value
    
    @validator('Cpu')
    def valid_cpu_provider(cls, value):
        provider = value.split()[0]
        if provider not in ["Intel", "AMD", "Samsung"]:
            raise ValueError("invalid CPU Provider")
        return value
    
    @validator('Weight')
    def valid_weight_format(cls, value):
        pattern = r"[\d\.]+[kg]+"
        if not re.match(pattern=pattern, string=value):
            raise ValueError("invalid Weight input")
        return value
    
    @validator('Ram')
    def valid_ram_format(cls, value):
        pattern = r"[\d]+[GB]+"
        if not re.match(pattern=pattern, string=value):
            raise ValueError("invalid RAM input")
        return value       