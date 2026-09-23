from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

model = LogisticRegression(max_iter=200)
model.fit(X_train, Y_train)

prediction = model.predict(X_test)

print("Predicted Classes")
print(prediction)

accuracy = accuracy_score(Y_test, prediction)
print("Accuracy =", accuracy)
