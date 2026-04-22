import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X = np.array([
    [500, 2005],
    [600, 2006],
    [700, 2007],
    [800, 2008],
    [900, 2009]
])
y = np.array([150, 180, 200, 220, 250])

# Model
model = LinearRegression()
model.fit(X, y)

# Coefficients and Intercept
coef = model.coef_
intercept = model.intercept_

# R-squared
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

# Prediction for (750 sq.ft, 2009)
new_data = np.array([[750, 2009]])
prediction = model.predict(new_data)

print("Coefficient:", coef)
print("Intercept:", intercept)
print("R-squared:", r2)
print("Predicted Price:", prediction)