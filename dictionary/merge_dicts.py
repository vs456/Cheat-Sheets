def merge_dicts(dict1, dict2):

    for key, value in dict2.items():
        if key in dict1.keys():
            dict1[key] += value
        else:
            dict1[key] = value

    return(dict1)

print(merge_dicts({'a': 1, 'b': 2, 'c': 3},{'b': 3, 'c': 4, 'd': 5}))