import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
Y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, Y)

prediction = model.predict(X)

print("Slope:", model.coef_)
print("Intercept:", model.intercept_)

plt.scatter(X, Y, c="red")
plt.plot(X, prediction)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression")
plt.show()
