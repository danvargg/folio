import pandas as pd #data manipulation
import gc #Clear memory
from sklearn.externals import joblib #pickle / unpickle
from sklearn.neighbors import NearestNeighbors #KNN machine learning model

#Read data from json to data frame
data = pd.read_json('data.json') #INPUT
data = pd.DataFrame(data['meditationFeedback']) #Choose only this section of database

#Unnest data for modeling and choose the significant features
data = data['meditationFeedback'].apply(pd.Series)
data = data[['userId', 'meditationId', 'rating', 'emotion', 'topic', 'sessionN', 'duration', 'premium']]

data_emotion = pd.get_dummies(data['emotion'])
data_topic = pd.get_dummies(data['topic'])

data = pd.concat([data, data_emotion], axis=1)
data = pd.concat([data, data_topic], axis=1)

data = data.drop('topic', 1)
data = data.drop('emotion', 1)
data = data.drop('userId', 1)

#Just freeing up memory
del data_emotion
del data_topic
gc.collect()

#Dropping NaN values due to sklearn limitations
data = data.dropna(axis = 0, how = 'any')

#Columns types assignment
data['rating'] = data['rating'].astype(int)
data['sessionN'] = data['sessionN'].astype(int) 
data['duration'] = data['duration'].astype(int) 
data['premium'] = data['premium'].astype(bool)
data['anxious'] = data['anxious'].astype(bool)
data['great'] = data['great'].astype(bool)
data['okay'] = data['okay'].astype(bool)
data['sad'] = data['sad'].astype(bool)
data['stressed'] = data['stressed'].astype(bool)
data['anxiety'] = data['anxiety'].astype(bool)
data['focus'] = data['focus'].astype(bool)
data['happiness'] = data['happiness'].astype(bool)
data['healing'] = data['healing'].astype(bool)
data['mindfulness'] = data['mindfulness'].astype(bool)
data['morning'] = data['morning'].astype(bool)
data['selflove'] = data['selflove'].astype(bool)
data['sleep'] = data['sleep'].astype(bool)
data['stress'] = data['stress'].astype(bool)

X = data[['meditationId', 'rating', 'sessionN', 'duration', 'premium', 'anxious', 'great', 'okay', 'sad', 'stressed',
       'anxiety', 'focus', 'happiness', 'healing', 'mindfulness', 'morning', 'selflove', 'sleep', 'stress']] 
X = data.set_index('meditationId')

#Pickle main data frame
joblib.dump(X, 'x.pkl')

del data
gc.collect()

#KNN model training
nbrs = NearestNeighbors(n_neighbors = 10).fit(X)

#Pickle the model for production use
joblib.dump(nbrs, 'knn.pkl')