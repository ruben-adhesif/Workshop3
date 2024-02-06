from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
import numpy as np
import json

from xgboost import XGBClassifier

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Introduce errors to the dataset
np.random.seed(42)
error_indices = np.random.choice(len(y), size=10, replace=False)
y_error = np.copy(y)
y_error[error_indices] = np.random.randint(0, 3, size=10)

# Train classifiers
xgb_model = XGBClassifier()
xgb_model.fit(X, y_error)

# Flask app
app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    # Get the request parameters
    sepal_length = float(request.args.get('sepal_length'))
    sepal_width = float(request.args.get('sepal_width'))
    petal_length = float(request.args.get('petal_length'))
    petal_width = float(request.args.get('petal_width'))
    
    # Make predictions using the trained models
    data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    xgb_prediction = xgb_model.predict(data)
    xgb_species = iris.target_names[xgb_prediction[0]]

    # Create the response dictionary
    response = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
        "species": xgb_species,
    }
    
    # Print
    json_response = json.dumps(response, indent=4)
    print(json_response)
    return jsonify(response)

if __name__ == '__main__':
    app.run()