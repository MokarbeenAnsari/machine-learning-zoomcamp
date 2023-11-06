# Importing the required libraries
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import mutual_info_score
from sklearn.metrics import r2_score

from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import GradientBoostingRegressor

import pickle
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

model_name = 'gbr_model.bin'

# Opening file and loading the model
with open(model_name, 'rb') as f_in:
    dv, model = pickle.load(f_in)

@app.route('/predict', methods=['POST'])
def predict():
    house = request.get_json()
    house_X = dv.transform([house])
    price = model.predict(house_X)[0]

    result = {
        "house_price": float(price)
    }
    return jsonify(result)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)