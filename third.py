from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("\nTraining data -")
for i in range(len(X_train)):
    print(X_train[i],"->",y_train[i])
print("\nDecision tree model - ")
text_representation = tree.export_text(clf)
print(text_representation)
acc = accuracy_score(y_test, y_pred)
print("Accuracy:",100*acc,"%")


