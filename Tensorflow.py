import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

df  = pd.read_csv(r'D:\Projects\Excel_Data_Automation\Machine_Learning\TensorFlow_FILES\TensorFlow_FILES\DATA\fake_reg.csv')
#print(df.head())

#sns.pairplot(df)
#plt.show()
X = df[['feature1', 'feature2']].values #(return it as numpy array)
y = df['price'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)
#print(help(MinMaxScaler))
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train) 
X_test = scaler.transform(X_test) 
#print(X_train)
model = Sequential()
model.add(Dense(4, activation='relu'))
model.add(Dense(2, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='rmsprop', loss='mse')
model.fit(x = X_train, y = y_train, epochs = 250, verbose = 1) 
loss_df = pd.DataFrame(model.history.history)
#loss_df.plot()
#plt.show()
model.evaluate(X_test, y_test, verbose = 0)
print(model.evaluate(X_test, y_test, verbose = 0))
test_predictions = model.predict(X_test)
test_predictions = pd.Series(test_predictions.reshape(300,))
predict_df = pd.DataFrame(y_test, columns=['Test True Y'])
predict_df = pd.concat([predict_df, test_predictions])
predict_df.columns = ['Test True Y', 'Model Predictions']
print(len(predict_df['Model Predictions']))
sns.scatterplot(x = 'Test True Y', y = 'Model Predictions', data = predict_df)
#plt.show()
print(predict_df.describe())