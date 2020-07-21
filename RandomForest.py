#Random Forests and Decision trees
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
#from sklearn.tree import export_graphviz
import pydot

df = pd.read_csv('kyphosis.csv')
print(df.head())
sns.pairplot(df, hue = 'Kyphosis')
plt.show()
X = df.drop('Kyphosis', axis = 1)
y = df['Kyphosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)
predictions = dtree.predict(X_test)
print("Decision Tree ConfusionMatrix {} \n".format(confusion_matrix(y_test, predictions)))
print("Decision Tree ClassificationReport {} \n".format(classification_report(y_test, predictions)))
rfc= RandomForestClassifier(n_estimators = 100)
rfc.fit(X_train, y_train)
rfc_predictions = rfc.predict(X_test)
print("Random Forest ConfusionMatrix {} \n".format(confusion_matrix(y_test, rfc_predictions)))
print("Random Forest ClassificationReport {} \n".format(classification_report(y_test, rfc_predictions)))

print(df['Kyphosis'].value_counts())