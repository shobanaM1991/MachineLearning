#support vector machine excercise 2
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC 
from sklearn.model_selection import GridSearchCV
df = sns.load_dataset('iris')
#print(df.info())
sns.pairplot(df, hue="species", palette="Dark2")
setosa = df.loc[df.species == "setosa"]
sns.kdeplot(setosa.sepal_width, setosa.sepal_length, cmap="plasma", shades = True, shades_lowest = False)
plt.show()
#print(df.columns)
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)
svc = SVC()
svc.fit(X_train, y_train)
predictions = svc.predict(X_test)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
param_grid = {'C':[0.1, 1, 10, 100, 1000], 'gamma':[1, 0.1, 0.01, 0.001, 0.0001]}
grid_search = GridSearchCV(SVC(), param_grid, verbose = 2)
#print(grid_search)
grid_search.fit(X_train, y_train)
pred = grid_search.predict(X_test)
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))