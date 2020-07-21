#KNN project No 2
import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Classified Data_pro.csv')
sns.pairplot(df, hue = 'TARGET CLASS')
plt.show()
print(df.head())
scaler_1 = StandardScaler()
scaler_1.fit(df.drop('TARGET CLASS', axis = 1))
scaled_features_1 = scaler_1.transform(df.drop('TARGET CLASS', axis = 1))
df_feat_1 = pd.DataFrame(scaled_features_1, columns = df.columns[:-1])
#print(df_feat_1)
X = df_feat_1
y = df['TARGET CLASS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)
knn = KNeighborsClassifier(n_neighbors = 31)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))
error_rate = []
for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(10,6))
plt.plot(range(1,40), error_rate, color = 'blue', linestyle='--', marker = 'o', markerfacecolor = 'red', markersize = 10)
plt.show()