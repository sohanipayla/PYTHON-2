import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset
data = pd.read_csv("student_scores.csv")

# Check dataset
print(data.head())

# Check missing values
print(data.isnull().sum())

X = data[['Hours']]   
y = data['Score']    

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("Predicted values:\n", y_pred)
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

# Mean Squared Error
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error:", mse)