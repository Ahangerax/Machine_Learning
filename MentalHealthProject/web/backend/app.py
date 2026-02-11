from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)   # FIX: enable CORS

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "depression_pipeline.pkl")
model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Depression Prediction API is running"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        input_df = pd.DataFrame([data])

        prediction = model.predict(input_df)[0]

        result = "Depressed" if prediction == 1 else "Not Depressed"

        return jsonify({
            "prediction": int(prediction),
            "result": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
