import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# a) Load the windpower dataset
df = pd.read_csv('windpower.csv')
df
# b) Check for missing values and remove them permanently
print(df.isnull().sum())
df.dropna(inplace=True)
# c) Split the dataset into training (75%) and testing (25%)
X = df[['Wind speed (m/s)']] 
y = df['Power (kW)']
print("X shape:", X.shape)
print("y shape:", y.shape)
print()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
print("Training data size:", X_train.shape)
print("Testing data size:", X_test.shape)
print("Training data size:", y_train.shape)
print("Testing data size:", y_test.shape)
# d, e, h) Train models, Predict, and Print Metrics/Coefficients
degrees = [3, 4, 5, 6]
MSE = []
for i in degrees:
    # d) Polynomial features create karna
    poly = PolynomialFeatures(degree=i)
    X_train_poly = poly.fit_transform(X_train)
    lr = LinearRegression()
    lr.fit(X_train_poly, y_train)
    X_test_poly = poly.transform(X_test)
    # e) Prediction
    y_pred = lr.predict(X_test_poly)

    mse = mean_squared_error(y_test, y_pred)
    MSE.append(mse)
    R2_score = r2_score(y_test, y_pred)
    print("Degree=",i)
    print("MSE=",mse)
    print("R2_score=",R2_score)
plt.plot(degrees,MSE,'*-r')
plt.show()
