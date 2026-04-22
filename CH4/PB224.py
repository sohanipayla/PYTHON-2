import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset
data = pd.read_csv("petrol_consumption.csv")

# Check first rows
print(data.head())

# Check missing values
print(data.isnull().sum())

X = data.drop('Petrol_Consumption', axis=1)   
y = data['Petrol_Consumption']            

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("Predicted values:\n", y_pred)
print("Coefficients:\n", model.coef_)
print("Intercept:\n", model.intercept_)

# Mean Squared Error
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error:", mse)