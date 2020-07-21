#logistic regression Project
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv('advertising.csv')
print(df.head())
sns.distplot(df['Age'], bins=30, kde = False)
sns.jointplot(x = df['Age'], y = df['Area Income'], data = df)
sns.jointplot(x = df['Age'], y = df['Area Income'], data = df, kind = 'kde')
sns.jointplot(x = df['Daily Time Spent on Site'], y = df['Daily Internet Usage'], data = df)
sns.pairplot(data = df, hue='Clicked on Ad')
plt.show()
print(df.columns)
X = df[['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Male']]
y = df['Clicked on Ad']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state= 101)
logReg = LogisticRegression()
logReg.fit(X_train, y_train)
predictions=logReg.predict(X_test)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))