from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)

knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print("Accuracy:",100*acc,"%")

prec = precision_score(y_test, y_pred,average="weighted")
print("Precision:",100*prec,"%")

recall = recall_score(y_test, y_pred,average="weighted")
print("Recall:",100*recall,"%")




