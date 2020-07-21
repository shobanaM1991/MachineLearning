#Project1 : K Nearest Neighbors
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv('Classified Data.csv')
df.rename(columns={'Unnamed: 0': 'tobedeleted'}, inplace=True)
df.drop('tobedeleted', axis = 1, inplace = True)
scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis = 1))
scaled_features = scaler.transform(df.drop('TARGET CLASS', axis = 1))
df_feat = pd.DataFrame(scaled_features, columns = df.columns[:-1])
X = df_feat
y = df['TARGET CLASS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state= 101)
knn =KNeighborsClassifier(n_neighbors = 17)
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
#print(df_feat.head())
#elbow method to choose correct K values
eror_rate = []
for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train, y_train)
    predictions_i = knn.predict(X_test)
    eror_rate.append(np.mean(predictions_i != y_test))

plt.figure(figsize=(10,6))
plt.plot(range(1,40), eror_rate, color = 'blue', linestyle='--', marker = 'o', markerfacecolor = 'red', markersize = 10)
plt.show()