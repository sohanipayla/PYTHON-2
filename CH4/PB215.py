import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Given data
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

# Model
model = LinearRegression()
model.fit(x, y)

# Coefficient and Intercept
coef = model.coef_
intercept = model.intercept_

# R-squared
y_pred = model.predict(x)
r2 = r2_score(y, y_pred)

# Prediction for x = np.arange(5)
x_new = np.arange(5).reshape((-1, 1))
y_new = model.predict(x_new)

print("Coefficient:", coef)
print("Intercept:", intercept)
print("R-squared:", r2)
print("Predicted y:", y_new)