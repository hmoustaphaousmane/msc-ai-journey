import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Experience": [1, 2, 3, 4, 5],
    "Education": [12, 14, 15, 16, 18],
    "Salary": [25000, 32000, 40000, 48000, 60000]
}

df = pd.DataFrame(data)

X = df[["Experience", "Education"]]
Y = df["Salary"]

model = LinearRegression()

model.fit(X, Y)

print("Coefficients")
print(model.coef_)

# Learned equation
# Salary = 6500 * (Experience) + 1500 * (Education) - 1000

print("Intercept")
print(model.intercept_)

prediction = model.predict(
    pd.DataFrame([[6, 18]], columns=["Experience", "Education"])
)
# Salary = 6500 * 6 + 1500 * 18 - 1000

print("Predicted Salary", prediction)
