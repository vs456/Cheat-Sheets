def max_key_value(dict1):

    ret_val = None
    max_value = max(dict1.values())

    for key in dict1.keys():
        if max_value == dict1[key]:
            ret_val = key
        
    return ret_val

print(max_key_value({'a': 5, 'b': 9, 'c': 2}))