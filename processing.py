import numpy as np
import pandas as pd


def X_y_split(df):
    ''' ** Split DataFrame into feature and target** 
    input 
    df : pd.DatFrame

    return
    X : pd.DatFrame
    y : pd.DatFrame
    
    '''
    X = df.drop('EnvRatingNumeric', axis=1)
    y = df['EnvRatingNumeric']
    return X, y

def to_EnvRating(x):

    '''** This function find the corresponding value in EnvRating for a given x**

    input

    x : float

    return
    x : str

    '''
    if x < 1.25 : 
        return 'D-'
    if x < 1.5 : 
        return 'D'
    if x < 1.75 : 
        return 'D+'
    if x < 2 : 
        return 'C-'
    if x < 2.25 : 
        return 'C'
    if x < 2.5 : 
        return 'C+'
    if x < 2.75 : 
        return 'B-'
    if x < 3 : 
        return 'B'
    if x < 3.25 : 
        return 'B+'
    if x < 3.5 : 
        return 'A-'
    if x < 3.75 : 
        return 'A'
    else : 
        return 'A+'
 

def export_pred(model, test, name):
    '''** This function generates the prediction file x**

    input

    model : Machine Learning model
    test : pd.DataFrame
    name : str

    '''
    pred = model.predict(test)

    # Create an array of EnvRating
    predictions_A = []
    for p in pred:
        predictions_A.append(to_EnvRating(p))

    # Transform predictions to a DataFrame
    predictions_df = pd.DataFrame({'index': np.arange(0,test.shape[0]), 'EnvRating' : predictions_A, 
                                   'EnvRatingNumeric': list(pred)})
    predictions_df.to_csv(name + '.csv')


