# app.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model into memory when the app starts
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract JSON data from the request
    data = request.get_json()
    
    # Convert the JSON payload into a DataFrame
    input_data = pd.DataFrame([data])
    
    # Make a prediction
    prediction = model.predict(input_data)
    
    # Return the result as JSON
    return jsonify({'churn_prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)