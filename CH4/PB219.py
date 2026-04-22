import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

x = np.arange(0, 30).reshape((-1, 1))
y = np.array([3, 4, 5, 7, 10, 8, 9, 10, 10, 23, 27, 44, 50, 63, 67, 60, 62, 70, 75, 88, 81, 87, 95, 100, 108, 135, 151, 160, 169, 179])

# Polynomial Features (degree = 2)
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

# Model
model = LinearRegression()
model.fit(x_poly, y)

# Coefficients and Intercept
coef = model.coef_
intercept = model.intercept_

# R-squared
y_pred = model.predict(x_poly)
r2 = r2_score(y, y_pred)

# Prediction for x = np.arange(5)
x_new = np.arange(5).reshape((-1, 1))
y_new = model.predict(poly.transform(x_new))

print("Coefficient:", coef)
print("Intercept:", intercept)
print("R-squared:", r2)
print("Predicted y:", y_new)