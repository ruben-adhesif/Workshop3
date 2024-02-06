from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load models
model_files = ['models//random_forest_model.pkl', 'models//logistic_regression_model.pkl', 'models//svm_model.pkl']
models = {f.split('_')[0]: pickle.load(open(f, 'rb')) for f in model_files}

def get_model_prediction(model, features):
    return model.predict([features])[0]

def get_consensus_prediction(features):
    predictions = [get_model_prediction(model, features) for model in models.values()]
    return int(np.mean(predictions))

@app.route('/predict', methods=['GET'])
def predict():
    features = [float(request.args.get(f)) for f in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    predictions = {name: int(get_model_prediction(model, features)) for name, model in models.items()}  # Cast to int
    return jsonify(predictions)

@app.route('/consensus', methods=['GET'])
def consensus():
    features = [float(request.args.get(f)) for f in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    consensus_pred = int(get_consensus_prediction(features))  # Cast to int
    return jsonify({'consensus_prediction': consensus_pred})


# slashinh mechanism
import json

def update_model_balances(model_name, correct):
    with open('model_balances.json', 'r+') as file:
        balances = json.load(file)
        if correct:
            balances[model_name] += 10  # Reward for correct prediction
        else:
            balances[model_name] -= 50  # Penalty for incorrect prediction
        file.seek(0)
        json.dump(balances, file, indent=4)
        file.truncate()

@app.route('/update_balances', methods=['POST'])
def update_balances():
    data = request.json
    model_name = data['model_name']
    correct = data['correct']
    update_model_balances(model_name, correct)
    return jsonify({'message': 'Balance updated successfully'})


if __name__ == '__main__':
    app.run(debug=True)
