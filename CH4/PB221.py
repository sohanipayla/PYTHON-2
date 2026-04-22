import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("data.csv")
X = data[['x1']]   
y = data['y']      
model = LinearRegression()
model.fit(X, y)
a = model.intercept_
b = model.coef_[0]
print("Value of a (Intercept):", a)
print("Value of b (Coefficient):", b)
x_new = [[10]]
y_pred = model.predict(x_new)
print("Predicted value of y:", y_pred)