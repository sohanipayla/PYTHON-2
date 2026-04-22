import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("Package.csv")
X = data[['x']]   # input (must be 2D)
y = data['y']     # output
model = LinearRegression()
model.fit(X, y)
b = model.coef_[0]
a = model.intercept_
print("Value of a (Intercept):", a)
print("Value of b (Coefficient):", b)
x_new = [[10]]
y_pred = model.predict(x_new)
print("Predicted value of y:", y_pred)