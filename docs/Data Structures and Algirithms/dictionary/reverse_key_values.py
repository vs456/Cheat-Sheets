def reverse_key_values(dict1):

    return {v:k for k,v in dict1.items()}

print(reverse_key_values({'a': 1, 'b': 2, 'c': 3}))