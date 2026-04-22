import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset
data = pd.read_csv("insurance.csv")

# Check data
print(data.head())

# Check null values
print(data.isnull().sum())

# Convert categorical data to numeric
data = pd.get_dummies(data, drop_first=True)

X = data.drop('charges', axis=1)
y = data['charges']

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("Predicted values:\n", y_pred)
print("Coefficients:\n", model.coef_)
print("Intercept:\n", model.intercept_)

# Mean Squared Error
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error:", mse)