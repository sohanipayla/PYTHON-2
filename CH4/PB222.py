import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset
data = pd.read_csv("Housing.csv")

# Display first rows
print(data.head())

# Check missing values
print(data.isnull().sum())

# Convert categorical columns into numeric (if any)
data = pd.get_dummies(data, drop_first=True)

X = data.drop('price', axis=1)   
y = data['price']               

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("Predicted values:\n", y_pred)
print("Coefficients:\n", model.coef_)
print("Intercept:\n", model.intercept_)

# Mean Squared Error
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error:", mse)