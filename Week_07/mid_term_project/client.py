# Importing required libraries
import requests
import json

# Server url
url = 'http://localhost:9696/predict'

# House data
house = {
    "location": "other",
    "total_sqft": 4500.0,
    "bath": 9,
    "bhk": 9
}

# Testing
response = requests.post(url, json=house).json()
print("Price of House: ", round(response['house_price'], 2))