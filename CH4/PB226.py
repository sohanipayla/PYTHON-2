# 1. Import libraries 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 2. Load dataset
data = pd.read_csv("RealEstate.csv")
print(data.info())

# 3. Remove 'No' column
data = data.drop('No', axis=1)

# 4. Check null values
print(data.isnull().sum())

# 5. Create feature variables X and y
X = data.drop('Y house price of unit area', axis=1)
y = data['Y house price of unit area']

# 6. Train-test split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=110)

# 7. Create and fit model
model = LinearRegression()
model.fit(X_train, y_train)

# 8. Prediction on test set
y_pred = model.predict(X_test)
print("Predicted values:\n", y_pred)

# 9. Coefficient and MSE
print("Coefficients:\n", model.coef_)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)