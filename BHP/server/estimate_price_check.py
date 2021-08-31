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
