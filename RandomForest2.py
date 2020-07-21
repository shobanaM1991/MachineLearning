#Random forest project 2
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv('DT_RFC_loan_data.csv')
print(df['not.fully.paid'])
df[df['credit.policy'] == 1]['fico'].hist(bins = 35, color = 'blue', label = 'Credit policy = 1', alpha = 0.6)
df[df['credit.policy'] == 0]['fico'].hist(bins = 35, color = 'red', label = 'Credit policy = 0', alpha = 0.6)

df[df['not.fully.paid'] == 1]['fico'].hist(bins = 35, color = 'blue', label = 'not.fully.paid = 1', alpha = 0.6)
df[df['not.fully.paid'] == 0]['fico'].hist(bins = 35, color = 'red',label = 'not.fully.paid = 0', alpha = 0.6)
plt.legend()
plt.xlabel('FICO')
cplot = df[df['not.fully.paid'] == 1]['purpose']
plt.figure(figsize = (11,7))
sns.countplot(x = 'purpose', hue = 'not.fully.paid', data = df, palette='Set1')
sns.countplot(df[df['not.fully.paid'] == 0]['purpose'])
sns.jointplot(x = 'fico', y = 'int.rate', data = df)

sns.lmplot(x = 'fico', y= 'int.rate', data = df, hue = 'credit.policy', col = 'not.fully.paid', palette ='Set1')
plt.legend()
plt.show()
columns with categorical has to splitted into numertical values and each category be each column with values 0 and 1
df1 = pd.get_dummies(df['purpose'], drop_first=True)
df = pd.concat([df, df1], axis = 1)
df = df.drop('purpose', axis = 1) 

X = df.drop('not.fully.paid', axis = 1) 
y = df['not.fully.paid']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)
dt_predictions = dtree.predict(X_test)
print(classification_report(y_test, dt_predictions))
print(confusion_matrix(y_test, dt_predictions))
RFC = RandomForestClassifier(n_estimators = 300)
RFC.fit(X_train, y_train)
RFC_Predictions = RFC.predict(X_test)
print(classification_report(y_test, RFC_Predictions))
print(confusion_matrix(y_test, RFC_Predictions))
#print(df.head())

#print(df.info())
