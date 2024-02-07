from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import numpy as np
import pickle

# Load the dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
models = {
    'random_forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'logistic_regression': LogisticRegression(max_iter=200),
    'svm': SVC(probability=True)
}

# Train models and save them
for name, model in models.items():
    model.fit(X_train, y_train)
    with open(f'models/{name}_model.pkl', 'wb') as file:
        pickle.dump(model, file)
