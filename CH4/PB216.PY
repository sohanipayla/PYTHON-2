import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

SAT = np.array([1000, 1100, 1200, 1300, 1400]).reshape((-1, 1))
GPA = np.array([2.5, 2.7, 3.0, 3.2, 3.5])

# Model
model = LinearRegression()
model.fit(SAT, GPA)

# Coefficient and Intercept
coef = model.coef_
intercept = model.intercept_

# R-squared
GPA_pred = model.predict(SAT)
r2 = r2_score(GPA, GPA_pred)

print("Coefficient:", coef)
print("Intercept:", intercept)
print("R-squared:", r2)