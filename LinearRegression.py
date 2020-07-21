#Machine learning algorithm 
#project: Linear Regression algorithm to predict the housing price

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = pd.read_csv('USA_Housing.csv')
from sklearn.datasets import load_boston  
from sklearn import metrics

#print(df.columns)
X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state = 101)
lm = LinearRegression()
lm.fit(X_train, y_train)
print(lm.intercept_)
print(lm.coef_)
print(X_train.columns)
df1 = pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])
print(df1)
boston = load_boston()
print(boston.keys())
 
predictions = lm.predict(X_test) 
print(predictions)
print(y_test)

sns.distplot(y_test - predictions)

print(metrics.mean_absolute_error(y_test, predictions))
print(metrics.mean_squared_error(y_test, predictions))
print(np.sqrt(metrics.mean_squared_error(y_test, predictions)))

sns.pairplot(df)
sns.distplot(df['Price'])
sns.heatmap(df.corr(), annot=True)
plt.show()

