import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
iris = load_iris()
x = iris.data[:100, [0, 2]]  # sepal length and petal length
y = iris.target[:100]        # setosa (0) or versicolor (1)
y = np.where(y == 0, -1, 1)  # setosa (-1) or versicolor (1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=43)
model = Perceptron(random_state=39,max_iter=10,tol=0.001)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
accuracy = np.mean(y_pred==y_test)
print("Accuracy: ",accuracy)

x_min, x_max = x_test[:, 0].min() - 0.5, x_test[:, 0].max() + 0.5
y_min, y_max = x_test[:, 1].min() - 0.5, x_test[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))
# make predictions on the meshgrid
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
# plot the input scatter plot and decision surface
plt.figure()
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_test, cmap=plt.cm.Paired)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.5)
plt.xlabel('Sepal length')
plt.ylabel('Petal length')
plt.title('Perceptron Classification')
plt.show()

