# Importing the required libraries
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import pickle
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

model_name = 'rfc_model.bin'

# Opening file and loading the model
with open(model_name, 'rb') as f_in:
    model = pickle.load(f_in)

@app.route('/predict', methods=['POST'])
def predict():
    apple = request.get_json()
    apple_df = pd.DataFrame([apple])
    quality = model.predict(apple_df)[0]

    quality_label = 'good' if int(quality) == 1 else 'bad'

    result = {
        "apple_quality": quality_label
    }
    return jsonify(result)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)