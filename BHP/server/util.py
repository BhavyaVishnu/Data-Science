import json
import pickle
import numpy as np

__locations = None  #creating 3  variables
__data_columns = None
__model = None


def get_estimated_price(location,sqft,bhk,bath):
    if location == 'other':
        l = np.zeros(len(__data_columns))
        l[0] = sqft
        l[1] = bath
        l[2] = bhk
        return round(__model.predict([l])[0],2)
    else:
        try:
            loc_index = __data_columns.index(location.lower())  # getting location index
        except:
            loc_index = -1

        z = np.zeros(len(__data_columns))
        z[0] = sqft
        z[1] = bath
        z[2] = bhk
        if loc_index >= 0:
            z[loc_index] = 1
        return round(__model.predict([z])[0], 2)



def get_location_names():
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    global __model
    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts ...done")


if __name__ == 'util':
    #print(get_location_names())
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase Jp Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase Jp Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1200, 2, 2))
    print(get_estimated_price('other', 900, 2, 2))