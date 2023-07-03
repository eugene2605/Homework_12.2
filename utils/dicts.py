def get_val(collection, key, default='animal'):
    if key in collection.keys():
        return collection[key]
    else:
        return default
