import json
import joblib

from flask import Flask, request, jsonify, url_for, render_template
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('RandomForestClassifier_model.joblib')

# Define the microorganism mappings
microorganism_names = {
    0: 'Aspergillus sp',
    1: 'Diatom',
    2: 'Penicillum',
    3: 'Pithophora',
    4: 'Protozoa',
    5: 'Raizopus',
    6: 'Spirogyra',
    7: 'Ulothrix',
    8: 'Volvox',
    9: 'Yeast'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    prediction = model.predict([list(data.values())])
    predicted_microorganism = microorganism_names[prediction[0]]
    return jsonify({'predicted_microorganism': predicted_microorganism})

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    prediction = model.predict([data])
    predicted_microorganism = microorganism_names[prediction[0]]
    return render_template('index.html', prediction_text=f"Predicted Microorganism: {predicted_microorganism}")

if __name__ == "__main__":
    app.run(debug=True)
