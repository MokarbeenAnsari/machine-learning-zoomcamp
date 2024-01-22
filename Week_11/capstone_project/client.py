# Importing required libraries
import requests
import json

# Server url
url = 'http://localhost:9696/predict'

# Apple data
apple = {'size': -1.193551717,
 'weight': -1.484548885,
 'sweetness': -1.682801417,
 'crunchiness': -0.255826272,
 'juiciness': 1.888296732,
 'ripeness': 1.369561333,
 'acidity': 1.640197921}

# Testing
response = requests.post(url, json=apple).json()
print("Quality of Apple: ", response['apple_quality'])