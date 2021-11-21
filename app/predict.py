import numpy as np
import pandas as pd
import joblib


model = joblib.load('models/forest_reg_model.joblib')



def get_form_data(data):


    feature_values = {
        'budget' :100000,
        'popularity':1,
        'runtime':107



    }
    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]

    return feature_values



def predict (data,debug=False):

    values = get_form_data(data)

    if debug: print(f'Feature values:{values}\n')

    column_order=['budget','popularity','runtime']
    values = np.array([values[feature] for feature in column_order], dtype=object)

    if debug:
        print('Ordered feature values: ')
        print(list(zip(column_order,values)))

    pred = model.predict(values.reshape(1,-1))

    return str(pred[0])