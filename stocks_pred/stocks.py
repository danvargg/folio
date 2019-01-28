from pandas_datareader import data
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
ticker = 'GOOGL'

# Define which online source one should use
data_source = 'yahoo'

start = '2010-01-01'
end = '2017-12-31'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
data = data.DataReader(ticker, data_source, start, end)
data['Date'] = data.index
data = data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
data = data.sort_values(by = ['Date'], ascending = False)
data['close_greater_than_open'] = np.where(data['Close'] > data['Open'], 'yes', 'no')
validation = pd.DataFrame(data.iloc[0, :])
validation = validation.transpose()
data = data.iloc[1:]

y = data['close_greater_than_open']
X = data[['Open', 'High', 'Low', 'Close', 'Volume']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

predicted = model.predict(X_test)
accuracy = model .score(X_test, y_test)

#Predicting if open > close
val_x = validation[['Open', 'High', 'Low', 'Close', 'Volume']]
predict = model.predict(val_x)

print('Accuracy:', accuracy)
print('Is close greater than open?:', predict)