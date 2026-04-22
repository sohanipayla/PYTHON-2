import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset
data = pd.read_csv("winequality.csv")

# Check null values
print(data.isnull().sum())

# Replace null values with mean of columns
data = data.fillna(data.mean())

X = data.drop('quality', axis=1)
y = data['quality']

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("Coefficients:\n", model.coef_)
print("Intercept:\n", model.intercept_)

# Mean Squared Error
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error:", mse)

# Prediction for given input
new_data = np.array([[8, 0.4, 0.40, 15, 0.048, 40, 150, 0.99, 3, 0.45, 10.5]])
predicted_quality = model.predict(new_data)
print("Predicted Wine Quality:", predicted_quality)