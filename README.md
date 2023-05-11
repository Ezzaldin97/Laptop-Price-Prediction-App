# Laptop Price Prediction API

![](imgs/model-api.PNG)

## Description:

Machine Learning Model API Using Flask & Docker to Predict Laptop Prices based on Specs Data of Laptop, Once Running Docker Image, WSGI Server will be Running, HTTP Request Can be Send with JSON Data like below
```json
#sample
{
    "laptop_ID": 78,
    "Company": "HP",
    "Product": "",
    "TypeName": "Notebook",
    "Inches": 13.7,
    "ScreenResolution": "Full HD 3840x2160",
    "Cpu": "AMD A10-Series 9620P 2.5GHz",
    "Ram": "24GB",
    "Memory": "500GB HDD",
    "Gpu": "Intel Iris Plus Graphics 650",
    "OpSys": "Windows 10",
    "Weight": "1.5kg"
}
```
and Response will get back as the predicted value of Laptop Price 
```json
# prediction of price
{
    "predicted_price": 1715.9983530577372
}
```
if there are Invalid Data, Response will be 
```json
# example of invalid sample
{
    "error": "Invalid Data"
}
```

## Tech & Dependancies:

- Python 3.10
- Docker
- Github Actions-CI/CD Pipeline
- Knowledge About ML

## Data:

[Laptop Prices](https://www.kaggle.com/datasets/muhammetvarl/laptop-price)

## Project Development:

