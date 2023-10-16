# Importing the required libraries
import pickle
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

model_name = 'model1.bin'
dv_name = 'dv.bin'

# Opening file and loading the model
with open(model_name, 'rb') as f_in:
    model = pickle.load(f_in)

# Opening file and loading the dv
with open(dv_name, 'rb') as f_in:
    dv = pickle.load(f_in)

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()
    client_X = dv.transform([client])
    score = model.predict_proba(client_X)[0, 1]

    result = {
        "credit_probability": float(score),
    }
    return jsonify(result)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
