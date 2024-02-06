# Using XGBoost model on Iris dataset
import numpy as np
import xgboost as xgb

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Get data
iris = load_iris()
X = iris.data
y = iris.target

# Introduce errors to the dataset
np.random.seed(42)
error_indices = np.random.choice(len(y), size=10, replace=False)
y_error = np.copy(y)
y_error[error_indices] = np.random.randint(0, 3, size=10)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_error, test_size=0.2, random_state=42)

# Train the XGBoost model
xgb_model = xgb.XGBClassifier()
xgb_model.fit(X_train, y_train)

# Calculate the accuracy of the model
y_pred = xgb_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)