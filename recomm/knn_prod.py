import numpy as np
import pandas as pd
from sklearn.externals import joblib

nbrs = joblib.load('knn.pkl')
X = joblib.load('x.pkl')

t = [5, 200, 300, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
recomm = nbrs.kneighbors([t])

dist = np.array(recomm[0]).T
dist = pd.DataFrame(dist)
med_id = np.array(recomm[1]).T
med_id = pd.DataFrame(med_id)

final = pd.concat([dist, med_id], axis = 1)
final.columns = ['Distance', 'meditationIndex']

rec = X.iloc[final.meditationIndex]
rec.reset_index(level = 0, inplace = True)
final = pd.concat([final, rec], axis = 1)