import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# a) Load dataset
data = pd.read_csv("windpower.csv")

# b) Remove missing values
print(data.isnull().sum())
data = data.dropna()

# c) Define X and y
X = data[['windspeed']]
y = data['power']

# Train-test split (75% train, 25% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)

# Store results
degrees = [3, 4, 5, 6]
mse_list = []

plt.figure(figsize=(10,6))

# d), e), h)
for d in degrees:
    poly = PolynomialFeatures(degree=d)
    
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    
    model = LinearRegression()
    model.fit(X_train_poly, y_train)
    
    # Prediction
    y_pred = model.predict(X_test_poly)
    
    # Metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    mse_list.append(mse)
    
    print(f"\nDegree {d}")
    print("MSE:", mse)
    print("R2 Score:", r2)
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)
    
    # f) Plot actual vs predicted
    plt.scatter(X_test, y_pred, label=f"Degree {d}")

plt.scatter(X_test, y_test, color='black', label='Actual')

plt.xlabel("Wind Speed")
plt.ylabel("Power")
plt.title("Actual vs Predicted (All Degrees)")
plt.legend()
plt.show()

# g) Plot MSE vs Degree
plt.figure()
plt.plot(degrees, mse_list, marker='o')
plt.xlabel("Polynomial Degree")
plt.ylabel("MSE")
plt.title("MSE vs Polynomial Degree")
plt.show()

best_degree = degrees[np.argmin(mse_list)]
print("\nBest Degree (Lowest MSE):", best_degree)