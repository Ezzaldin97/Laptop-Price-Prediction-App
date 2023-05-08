from flask import Flask, request, jsonify
import pickle
import os
from app.inference import Inference
from app.validator import Laptop
from app import app
import pydantic

model = pickle.load(open(os.path.join(".", "app", "bin", "model-pipeline.pkl"), "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # validate the data before give to model pipeline..
    try:
        Laptop(data)
        inf = Inference(data)
        transformed_data = inf.transform()
        prediction = inf.predict(transformed_data)
        return jsonify({"predicted_price": prediction})
    except pydantic.error_wrappers.ValidationError:
        return jsonify({"error": "Invalid Data"}), 400
