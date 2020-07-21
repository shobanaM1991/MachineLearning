#NLP Project Excercise
""" """ import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report
df = pd.read_csv('nltk_yelp.csv')
print((df['text'].apply(len)))
df['text_length'] = df['text'].apply(len)
print(df[df['stars'] == 5]['text_length'])

g = sns.FacetGrid(df, col = 'stars')
g.map(plt.hist, 'text_length', alpha = 0.7)
sns.boxplot(x = 'stars', y = 'text_length', data=df)
sns.countplot(x = 'stars', data = df)
#plt.show()
df1 = df.select_dtypes(include = ['int64'])
df1 = df1.set_index('stars')
print(df1.mean())
print(df1.corr())
sns.heatmap(df1.corr(), cmap = 'coolwarm', annot = True)
#plt.show()
#print(df[(df['stars'] == 1) | (df['stars'] == 5)])
yelp_class = df[(df['stars'] == 1) | (df['stars'] == 5)]
#print(yelp_class.info())

X = yelp_class['text']
y = yelp_class['stars']
c_vect = CountVectorizer()
X = c_vect.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)
nb = MultinomialNB()
nb.fit(X_train, y_train)
predictions = nb.predict(X_test)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
tfidf = TfidfTransformer()
piplin = Pipeline([('bow', CountVectorizer()), ('tfidf', TfidfTransformer()),('mulnominalnb', MultinomialNB())])
X = yelp_class['text']
y = yelp_class['stars']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)
piplin.fit(X_train, y_train)
pred = piplin.predict(X_test)
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred)) 
