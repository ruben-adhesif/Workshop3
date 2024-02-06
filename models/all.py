# Use XGBoost, RandomForst and SVC on Iris Dataset
# curl "http://127.0.0.1:5000/predict?sepal_length=5.1&sepal_width=3.5&petal_length=1.4&petal_width=0.2"

from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
import numpy as np
import json

from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Introduce errors to the dataset
np.random.seed(42)
error_indices = np.random.choice(len(y), size=10, replace=False)
y_error = np.copy(y)
y_error[error_indices] = np.random.randint(0, 3, size=10)

# Create classifiers
xgb_model = XGBClassifier()
rf_model = RandomForestClassifier()
svm_model = SVC()

# Train the models
xgb_model.fit(X, y_error)
rf_model.fit(X, y_error)
svm_model.fit(X, y_error)


# Flask app
app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    # Get the request parameters
    sepal_length = float(request.args.get('sepal_length'))
    sepal_width = float(request.args.get('sepal_width'))
    petal_length = float(request.args.get('petal_length'))
    petal_width = float(request.args.get('petal_width'))
    data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Make predictions using the trained models
    xgb_prediction = xgb_model.predict(data)
    rf_prediction = rf_model.predict(data)
    svm_prediction = svm_model.predict(data)

    # Map the predictions to the corresponding class labels
    xgb_species = iris.target_names[xgb_prediction[0]]
    rf_species = iris.target_names[rf_prediction[0]]
    svm_species = iris.target_names[svm_prediction[0]]

    # Create the response dictionary
    response = {
        "charactere": {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        },
        "result": {
            "xgb_species": xgb_species,
            "rf_species": rf_species,
            "svm_species": svm_species
        }
    }
    
    # Print
    json_response = json.dumps(response, indent=4)
    print(json_response)
    return jsonify(response)

if __name__ == '__main__':
    # Run the Flask app
    app.run()