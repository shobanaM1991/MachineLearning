#Excercise K Means Clustering
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.cluster import KMeans
df = pd.read_csv('kmeans_College_Data.csv', index_col = 0)
print(df.head())
sns.lmplot(x = 'Room.Board', y = 'Grad.Rate', data = df, hue = 'Private', fit_reg=False)
sns.lmplot(x = 'Outstate', y = 'F.Undergrad', data = df, hue = 'Private', fit_reg=False)
plt.hist(x = 'Outstate', bins = 30, stacked=True, density= 'Private', data = df)
g = sns.FacetGrid(df, hue = 'Private', palette='coolwarm', aspect = 2)
g.map(plt.hist, 'Outstate', alpha = 0.7)
g.map(plt.hist, 'Grad.Rate', alpha = 0.7)
print(df[df['Grad.Rate']>100])
kmeans_1 = KMeans(n_clusters = 2)
kmeans_1.fit(df.drop('Private', axis = 1))
print(kmeans_1.cluster_centers_)
def converter(private):
    if private == 'Yes':
        return 1
    else:
        return 0
df['cluster']= df['Private'].apply(converter)
print(df.head())
print(classification_report(df['cluster'], kmeans_1.labels_))
print(confusion_matrix(df['cluster'], kmeans_1.labels_))
#plt.show()