import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tensorflow
from tensorflow.keras.models import Sequential
#from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

df  = pd.read_csv(r'D:\Projects\Excel_Data_Automation\Machine_Learning\TensorFlow_FILES\TensorFlow_FILES\DATA\kc_house_data.csv')
#print(df.head())
sns.distplot(df['price'])
sns.countplot(x= df['bedrooms'])
#plt.show()
#print(df[df['bedrooms'] == 33])
#print(df.corr()['price'].sort_values())
sns.scatterplot(x ='price', y='sqft_living', data =df)
sns.boxplot(x = 'bedrooms', y = 'price', data=df)
sns.scatterplot(x = 'price', y = 'lat', data = df)
sns.scatterplot(x = 'long', y = 'lat', data = df, hue = 'price')
# plt.show()
#print(df.sort_values('price', ascending = False).head(20))
low_price = df.sort_values('price', ascending = False).iloc[216:]
plt.figure(figsize = (12,8))
sns.scatterplot(x = 'long', y = 'lat', data = low_price, edgecolor = None, alpha = 0.2, palette = 'RdYlGn', hue = 'price')
sns.boxplot(x = 'waterfront', y = 'price', data=low_price)
#plt.show()
df = df.drop('id', axis = 1)
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].apply(lambda date: date.year)
df['month'] = df['date'].apply(lambda date: date.month)
df['year'] = df['date'].apply(lambda date: date.year)
sns.boxplot(x = 'month', y = 'price', data=df)
df.groupby('year').mean()['price'].plot()
#plt.show()
df = df.drop('date', axis = 1)
#print(df['zipcode'].value_counts())
df = df.drop('zipcode', axis = 1)
#print(df.head())
X = df.drop('price', axis = 1).values
y = df['price'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = Sequential()
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))

model.add(Dense(1))
model.compile(optimizer = 'adam', loss = 'mse')
model.fit(x = X_train, y = y_train, validation_data = (X_test, y_test), batch_size = 128, epochs = 400)
losses = pd.DataFrame(model.history.history)
#losses.plot()
#plt.show()

from sklearn.metrics import mean_absolute_error, mean_squared_error, explained_variance_score
predict = model.predict(X_test)
print(np.sqrt(mean_squared_error(y_test, predict)))
print(mean_absolute_error(y_test, predict))
print(explained_variance_score(y_test, predict))
plt.scatter(y_test, predict)
plt.plot(y_test, y_test, 'r')
# plt.show()
single_house = df.drop('price', axis = 1).iloc[0]
single_house = scaler.transform(single_house.values.reshape(-1, 19))
predictions = model.predict(single_house)
print(predictions)