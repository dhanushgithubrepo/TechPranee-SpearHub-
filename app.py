from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model from the file (update the path to your model file)
model = joblib.load('E:\Techspree\downtime_model.pkl')

@app.route('/')
def home():
    return "Welcome to the Machine Downtime Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.get_json()

    # Extract features from the incoming JSON request
    temperature = data['Temperature']
    run_time = data['Run_Time']

    # Prepare the input data for prediction
    features = np.array([[temperature, run_time]])

    # Make a prediction using the model
    downtime_prediction = model.predict(features)

    # Confidence score (probability of downtime)
    downtime_probability = model.predict_proba(features)[0][1]

    # Convert prediction (0 or 1) to "Yes" or "No"
    downtime_result = "Yes" if downtime_prediction[0] == 1 else "No"

    # Return the prediction and confidence score in JSON format
    return jsonify({'Downtime': downtime_result, 'Confidence': round(downtime_probability, 2)})


if __name__ == '__main__':
    app.run(debug=True)
