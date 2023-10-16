import requests
import json

url = 'http://localhost:9696/predict'

# Customer data
customer = {
    "gender": "male",
    "seniorcitizen": 0,
    "partner": "no",
    "dependents": "no",
    "phoneservice": "yes",
    "multiplelines": "no",
    "internetservice": "no",
    "onlinesecurity": "no_internet_service",
    "onlinebackup": "no_internet_service",
    "deviceprotection": "no_internet_service",
    "techsupport": "no_internet_service",
    "streamingtv": "no_internet_service",
    "streamingmovies": "no_internet_service",
    "contract": "month-to-month",
    "paperlessbilling": "no",
    "paymentmethod": "mailed_check",
    "tenure": 1,
    "monthlycharges": 20.2,
    "totalcharges": 20.2
}

response = requests.post(url, json=customer).json()

if response['churn'] == True:
    print(f"Sending promo mail to customer xyz-123!")
else:
    print(f"Not sending any promo code!")