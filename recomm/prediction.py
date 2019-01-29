'''
These are the inputs from user: (on a json file):

- Rating is fixed on 5 to ensure that the 'neirest neighbor' model (knn) always recommends the highest rated
meditations.
- emotion and topic are turned into dummy variables (true /false). The user inputs them (only one each).

User input: {"duration", , "emotion", "topic"}
Other inputs: {"userId", "sessionN", "premium"} / These come from the user's profile

Dummy variables: {"anxious", "great", "okay", "sad", "stressed", "anxiety", "focus", "happiness", 
"healing", "mindfulness", "morning", "selflove", "sleep","stress"}
'''

def lambda_handler(event, context):
    request = event 

    import numpy as np
    from sklearn.externals import joblib
    
    request = np.array(dict['request'])
        
    nbrs = joblib.load('knn.pkl')
    X = joblib.load('x.pkl')
            
    recomm = nbrs.kneighbors([request])
    
    dist = np.array(recomm[0])
    med_id = np.array(recomm[1])
    
    response = np.concatenate([dist, med_id], axis = 0)
    response = X.iloc[response[1]]
    response.reset_index(level = 0, inplace = True)
    response = response['meditationId'].values
        
    return response