# Importing the required libraries
import numpy as np
import pandas as pd


from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import roc_auc_score

import pickle
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

model_name = 'model_C=1.0.bin'

# Opening file and loading the model
with open(model_name, 'rb') as f_in:
    dv, model = pickle.load(f_in)

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    customer_X = dv.transform([customer])
    churn_rate = model.predict_proba(customer_X)[0, 1]
    churn = (churn_rate >= 0.5)

    result = {
        "churn_probability": float(churn_rate),
        "churn": bool(churn)
    }
    return jsonify(result)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)


