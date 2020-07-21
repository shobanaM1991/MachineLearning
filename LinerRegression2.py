#Linear Regression
#Project No:2
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df1 = pd.read_csv('Ecommerce_Customers.csv')
print(df1.head())
sns.jointplot(x = df1['Time on Website '], y = df1['Yearly Amount Spent'])
sns.jointplot(x = df1['Time on App '], y = df1['Yearly Amount Spent'])
sns.jointplot(x = df1['Length of Membership'], y = df1['Time on App'], kind = 'hex')
sns.pairplot(df1)
sns.lmplot(x = 'Length of Membership', y = 'Yearly Amount Spent', data=df1)
print(df1.columns)

X = df1[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = df1['Yearly Amount Spent']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state= 101)
lm = LinearRegression()
lm.fit(X_train, y_train)
print(lm.intercept_)
print(lm.coef_)
print(X_train.columns)
df2 = pd.DataFrame(data=lm.coef_, index = X_train.columns, columns =['Coeff'])
print(df2)
predictions = lm.predict(X_test)
print(predictions)
print(y_test)
plt.scatter(x = y_test, y = predictions)
plt.show()
print(metrics.mean_absolute_error(y_test, predictions))
print(metrics.mean_squared_error(y_test, predictions))
print(np.sqrt(metrics.mean_squared_error(y_test, predictions)))
sns.distplot(y_test - predictions)
plt.show()